let names = [];
let originalNames = [];
let colors = [];
let angleCurrent = 0;
let isSpinning = false;
let spinAngleStart = 0;
let spinTime = 0;
let spinTimeTotal = 0;
let isAnimatingWinner = false;
let spinOrder = 0;
let highlightIndex = null;
let lastTickIndex = null;
let audioCtx = null;

// Persistent list snapshot used for share image / share link even after resetGame clears state.
let shareSnapshotNames = [];

// Blink state for winner slice
let blinkActive = false;     // only during winner animation
let blinkOn = false;         // toggles light/dark

const STORAGE_KEYS = {
  theme: "wheeloflist_theme",
  names: "wheeloflist_names",
};

const TOOL_ROUTES = {
  randomNumberGenerator: "/random-number/",
  diceLoader: "/dice-roller/",
};

const ROUTE_TO_TOOL = {
  "random-number": "randomNumberGenerator",
  "dice-roller": "diceLoader",
};

let currentView = "wheel";

const canvas = document.getElementById("wheelCanvas");
const ctx = canvas.getContext("2d");

// Audio objects are loaded only if files exist to avoid 404 errors.
let spinSound = { play: () => {}, pause: () => {}, loop: false, currentTime: 0 };
let winSound  = { play: () => {}, pause: () => {}, loop: false, currentTime: 0 };

// Attempt to load audio files (HEAD check) and replace the stubs when available.
function tryLoadAudio(path, assignTo) {
  try {
    fetch(path, { method: "HEAD" })
      .then((res) => {
        if (res.ok) {
          try {
            const a = new Audio(path);
            if (assignTo === "spin") spinSound = a;
            if (assignTo === "win")  winSound  = a;
          } catch (e) {}
        }
      })
      .catch(() => {});
  } catch (e) {}
}
tryLoadAudio("audio/spin.mp3", "spin");
tryLoadAudio("audio/win.mp3", "win");

// ---------------- URL helpers ----------------
function getBaseUrl() {
  return window.location.origin + window.location.pathname;
}

function base64UrlEncode(str) {
  const bytes = new TextEncoder().encode(str);
  let binary = "";
  bytes.forEach((b) => (binary += String.fromCharCode(b)));
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}

function base64UrlDecode(b64url) {
  const b64 = b64url.replace(/-/g, "+").replace(/_/g, "/") + "===".slice((b64url.length + 3) % 4);
  const binary = atob(b64);
  const bytes = Uint8Array.from(binary, (c) => c.charCodeAt(0));
  return new TextDecoder().decode(bytes);
}

function syncUrlWithItems(list) {
  try {
    const url = new URL(window.location.href);
    if (list && list.length) {
      const payload = list.join("\n");
      url.searchParams.set("items", base64UrlEncode(payload));
    } else {
      url.searchParams.delete("items");
    }
    history.replaceState(null, "", url.toString());
  } catch (e) {}
}

function readItemsFromUrl() {
  try {
    const url = new URL(window.location.href);
    const encoded = url.searchParams.get("items");
    if (!encoded) return null;
    const decoded = base64UrlDecode(encoded);
    const list = decoded.split(/\r?\n/).map((x) => x.trim()).filter(Boolean);
    return list.length ? list : null;
  } catch (e) {
    return null;
  }
}

function getToolFromLocation() {
  try {
    const url = new URL(window.location.href);

    const toolParam = (url.searchParams.get("tool") || "").trim().toLowerCase();
    if (toolParam && ROUTE_TO_TOOL[toolParam]) return ROUTE_TO_TOOL[toolParam];

    const path = url.pathname.toLowerCase().replace(/\/+$/, "");
    const segment = path.split("/").filter(Boolean).pop() || "";
    if (segment && ROUTE_TO_TOOL[segment]) return ROUTE_TO_TOOL[segment];

    return null;
  } catch (e) {
    return null;
  }
}

function getRouteFromLocation() {
  const toolFromLocation = getToolFromLocation();
  if (toolFromLocation) {
    return { type: "tool", toolName: toolFromLocation };
  }
  return { type: "wheel" };
}

function setUrlForTool(toolName, mode = "push") {
  const routePath = TOOL_ROUTES[toolName];
  if (!routePath) return;

  try {
    const url = new URL(window.location.href);
    url.pathname = routePath;
    url.searchParams.delete("tool");

    if (mode === "replace") {
      history.replaceState(null, "", url.toString());
    } else {
      history.pushState(null, "", url.toString());
    }
  } catch (e) {}
}

function setUrlForWheel(mode = "push") {
  try {
    const url = new URL(window.location.href);
    url.pathname = "/";
    url.searchParams.delete("tool");

    if (mode === "replace") {
      history.replaceState(null, "", url.toString());
    } else {
      history.pushState(null, "", url.toString());
    }
  } catch (e) {}
}

function ensureToolsContainer() {
  let toolsContainer = document.getElementById("tools-container");
  if (!toolsContainer) {
    toolsContainer = document.createElement("div");
    toolsContainer.id = "tools-container";
    document.body.insertBefore(toolsContainer, document.querySelector("section"));
  }
  return toolsContainer;
}

function showWheelView() {
  const wheelSection = document.querySelector(".container-fluid > .row");
  const quickToolsSection = document.querySelector(".quick-tools-section");
  const toolsContainer = document.getElementById("tools-container");

  if (wheelSection) wheelSection.style.display = "";
  if (quickToolsSection) quickToolsSection.style.display = "";

  const activeTool = moduleManager.getActiveTool?.();
  activeTool?.deactivate?.();
  if (moduleManager && Object.prototype.hasOwnProperty.call(moduleManager, "activeModule")) {
    moduleManager.activeModule = null;
  }

  if (toolsContainer) {
    toolsContainer.innerHTML = "";
    toolsContainer.style.display = "none";
  }

  currentView = "wheel";
}

function showToolView(toolName) {
  const wheelSection = document.querySelector(".container-fluid > .row");
  const quickToolsSection = document.querySelector(".quick-tools-section");
  const toolsContainer = ensureToolsContainer();

  if (wheelSection) wheelSection.style.display = "none";
  if (quickToolsSection) quickToolsSection.style.display = "none";
  if (toolsContainer) toolsContainer.style.display = "block";

  moduleManager.switchTo(toolName);
  currentView = "tool";
}

function renderRoute(route) {
  if (route.type === "tool" && route.toolName) {
    showToolView(route.toolName);
  } else {
    showWheelView();
  }
}

function navigateToTool(toolName, options = {}) {
  const historyMode = options.historyMode || "push";
  const scroll = options.scroll !== false;

  renderRoute({ type: "tool", toolName });

  if (options.updateUrl !== false) {
    setUrlForTool(toolName, historyMode);
  }

  if (scroll) {
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
}

function navigateToWheel(options = {}) {
  const historyMode = options.historyMode || "push";
  const scroll = options.scroll !== false;

  renderRoute({ type: "wheel" });

  if (options.updateUrl !== false) {
    setUrlForWheel(historyMode);
  }

  if (scroll) {
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
}

function bindNavigationLinks() {
  document.addEventListener("click", (e) => {
    const anchor = e.target.closest("a[data-nav]");
    if (!anchor) return;

    if (e.defaultPrevented || e.button !== 0) return;
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;

    const nav = (anchor.getAttribute("data-nav") || "").trim();
    if (!nav) return;

    e.preventDefault();

    if (nav === "wheel") {
      navigateToWheel({ updateUrl: true, historyMode: "push", scroll: true });
      return;
    }

    if (ROUTE_TO_TOOL[nav]) {
      navigateToTool(ROUTE_TO_TOOL[nav], { updateUrl: true, historyMode: "push", scroll: true });
    }
  });
}

// ---------------- Local storage helpers ----------------
function getStoredValue(key) {
  try {
    return localStorage.getItem(key);
  } catch (e) {
    return null;
  }
}

function setStoredValue(key, value) {
  try {
    if (value === null || value === undefined || value === "") {
      localStorage.removeItem(key);
      return;
    }
    localStorage.setItem(key, value);
  } catch (e) {}
}

function applyStoredTheme() {
  const savedTheme = getStoredValue(STORAGE_KEYS.theme);
  const theme = savedTheme === "dark" ? "dark" : "light";

  document.body.classList.toggle("dark-theme", theme === "dark");

  const themeSelect = document.getElementById("themeSelect");
  if (themeSelect) themeSelect.value = theme;
}

// ---------------- UI helpers ----------------
function showToast(message) {
  try {
    const body = document.getElementById("appToastBody");
    const el = document.getElementById("appToast");
    if (!body || !el || !window.bootstrap) return;
    body.textContent = message;
    const toast = bootstrap.Toast.getOrCreateInstance(el, { delay: 2200 });
    toast.show();
  } catch (e) {}
}

function updateOverlay() {
  const overlay = document.getElementById("overlayButton");
  const emptyOverlay = document.getElementById("emptyWheelOverlay");
  const winnerOverlay = document.getElementById("winnerOverlay");

  overlay.style.display = names.length >= 2 && !isSpinning && !isAnimatingWinner ? "block" : "none";
  if (emptyOverlay) {
    emptyOverlay.style.display = names.length === 0 && !isSpinning && !isAnimatingWinner ? "block" : "none";
  }
  if (!isAnimatingWinner) winnerOverlay.style.display = "none";
}

// ---------------- Clipboard ----------------
async function copyToClipboard(text) {
  if (!text) {
    showToast("Nothing to copy.");
    return false;
  }

  try {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return true;
    }
  } catch (e) {}

  try {
    const ta = document.createElement("textarea");
    ta.value = text;
    ta.style.position = "fixed";
    ta.style.left = "-9999px";
    ta.style.top = "0";
    ta.setAttribute("readonly", "");
    document.body.appendChild(ta);
    ta.select();
    const ok = document.execCommand("copy");
    document.body.removeChild(ta);
    return ok;
  } catch (e) {
    return false;
  }
}

// ---------------- Scoreboard helpers ----------------
function getScoreboardWinners() {
  const items = Array.from(document.querySelectorAll("#scoreboard li"));
  return items
    .map((li) => li.dataset.winner || li.textContent.replace(/^\s*\d+\s*/, "").trim())
    .filter(Boolean);
}

function getLatestWinner() {
  const winners = getScoreboardWinners();
  return winners.length ? winners[winners.length - 1] : "";
}

function findWinnerIndexInList(winner, list) {
  if (!winner || !list || !list.length) return null;
  const w = String(winner).trim().toLowerCase();
  const idx = list.findIndex((x) => String(x).trim().toLowerCase() === w);
  return idx >= 0 ? idx : null;
}

// ---------------- Wheel init & sizing ----------------
function initDefaultNames() {
  const inputEl = document.getElementById("namesInput");
  const hasInputContent = inputEl && inputEl.value.trim().length > 0;

  if (names.length === 0 && !hasInputContent) {
    names = ["Alice", "Bob", "Carol", "Dave", "Eve"];
    originalNames = names.slice();
    colors = generateColors(names.length);
    inputEl.value = names.join("\n");
  }
}

function resizeCanvas() {
  const container = document.getElementById("wheel-container");
  const containerRect = container.getBoundingClientRect();
  const maxSize = Math.min(containerRect.width, containerRect.height) * 0.9;
  const size = Math.floor(maxSize);

  canvas.width = size;
  canvas.height = size;
  canvas.style.width = size + "px";
  canvas.style.height = size + "px";

  drawWheel();
  updatePointerPosition();

  // Keep URL synced to last loaded list (not current leftover state)
  const listForUrl = shareSnapshotNames && shareSnapshotNames.length ? shareSnapshotNames : originalNames;
  syncUrlWithItems(listForUrl);

  // Center overlay (spin button) over canvas
  const overlay = document.getElementById("overlayButton");
  if (overlay) {
    const canvasRect = canvas.getBoundingClientRect();
    const relLeft = canvasRect.left - containerRect.left + canvasRect.width / 2;
    const relTop  = canvasRect.top  - containerRect.top  + canvasRect.height / 2;
    overlay.style.left = relLeft + "px";
    overlay.style.top  = relTop + "px";
    overlay.style.transform = "translate(-50%, -50%)";
  }

  const emptyOverlay = document.getElementById("emptyWheelOverlay");
  if (emptyOverlay) {
    const canvasRect = canvas.getBoundingClientRect();
    const relLeft = canvasRect.left - containerRect.left + canvasRect.width / 2;
    const relTop  = canvasRect.top  - containerRect.top  + canvasRect.height / 2;
    emptyOverlay.style.left = relLeft + "px";
    emptyOverlay.style.top  = relTop + "px";
    emptyOverlay.style.transform = "translate(-50%, -50%)";
  }

  // Update center knob element size/position
  const centerEl = document.getElementById("wheel-center");
  if (centerEl) {
    const knobSize = Math.max(48, Math.floor(size * 0.12));
    centerEl.style.width = knobSize + "px";
    centerEl.style.height = knobSize + "px";

    const canvasRect = canvas.getBoundingClientRect();
    const relLeft = canvasRect.left - containerRect.left + canvasRect.width / 2;
    const relTop  = canvasRect.top  - containerRect.top  + canvasRect.height / 2;
    centerEl.style.left = relLeft + "px";
    centerEl.style.top  = relTop + "px";
    centerEl.style.transform = "translate(-50%, -50%)";
  }
}
window.addEventListener("resize", resizeCanvas);

function updatePointerPosition() {
  const canvasRect = canvas.getBoundingClientRect();
  const container = document.getElementById("wheel-container");
  const containerRect = container.getBoundingClientRect();
  const pointer = document.getElementById("pointer");

  const relLeft = canvasRect.left - containerRect.left + canvasRect.width / 2;
  const relTop  = canvasRect.top  - containerRect.top  + canvasRect.height - 30;

  pointer.style.left = relLeft + "px";
  pointer.style.top  = relTop + "px";
}

function generateColors(count) {
  const colorPairs = [];
  for (let i = 0; i < count; i++) {
    const hue = (i * 360) / count;
    colorPairs.push({
      start: `hsl(${hue}, 70%, 50%)`,
      end:   `hsl(${hue + 30}, 70%, 70%)`,
    });
  }
  return colorPairs;
}

// ---------------- Wheel rendering ----------------
function drawWheel() {
  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;
  const outsideRadius = canvas.width / 2 - 10;

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  if (names.length === 0) {
    ctx.fillStyle = "#ccc";
    ctx.beginPath();
    ctx.arc(centerX, centerY, outsideRadius, 0, 2 * Math.PI);
    ctx.fill();
    updateOverlay();
    return;
  }

  const innerRadius = 30;
  const textRadius = innerRadius + (outsideRadius - innerRadius) / 2;
  const arc = (Math.PI * 2) / names.length;

  for (let i = 0; i < names.length; i++) {
    const angle = angleCurrent + i * arc;

    const gradient = ctx.createLinearGradient(
      centerX - outsideRadius,
      centerY - outsideRadius,
      centerX + outsideRadius,
      centerY + outsideRadius
    );
    gradient.addColorStop(0, colors[i].start);
    gradient.addColorStop(1, colors[i].end);

    ctx.fillStyle = gradient;
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.arc(centerX, centerY, outsideRadius, angle, angle + arc);
    ctx.fill();

    // Winner blink overlay (light/dark), NO size emphasis
    if (highlightIndex !== null && i === highlightIndex && blinkActive) {
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(centerX, centerY);
      ctx.arc(centerX, centerY, outsideRadius, angle, angle + arc);
      ctx.closePath();
      ctx.fillStyle = blinkOn ? "rgba(255,255,255,0.22)" : "rgba(0,0,0,0.18)";
      ctx.fill();
      ctx.restore();
    }

    // Slice label with auto-scaling font
    ctx.save();
    ctx.fillStyle = "white";
    const textX = centerX + Math.cos(angle + arc / 2) * textRadius;
    const textY = centerY + Math.sin(angle + arc / 2) * textRadius;
    ctx.translate(textX, textY);
    ctx.rotate(angle + arc / 2);
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";

    const arcLength = outsideRadius * arc;
    let fontSize = canvas.width < 768 ? 20 : 40;
    ctx.font = `bold ${fontSize}px 'Quicksand', sans-serif`;

    let measured = ctx.measureText(names[i]).width;
    while (measured > arcLength * 0.8 && fontSize > 10) {
      fontSize -= 1;
      ctx.font = `bold ${fontSize}px 'Quicksand', sans-serif`;
      measured = ctx.measureText(names[i]).width;
    }
    ctx.fillText(names[i], 0, 0);
    ctx.restore();
  }

  // Rim
  ctx.save();
  const ringWidth = Math.max(8, Math.floor(canvas.width * 0.015));
  const rimGrad = ctx.createLinearGradient(
    centerX - outsideRadius,
    centerY - outsideRadius,
    centerX + outsideRadius,
    centerY + outsideRadius
  );
  rimGrad.addColorStop(0, "#ffffff");
  rimGrad.addColorStop(0.45, "#f5f7fa");
  rimGrad.addColorStop(0.6, "#e9eef5");
  rimGrad.addColorStop(1, "#e0e6ee");

  ctx.lineWidth = ringWidth;
  ctx.strokeStyle = rimGrad;
  ctx.shadowColor = "rgba(0,0,0,0.12)";
  ctx.shadowBlur = 14;

  ctx.beginPath();
  ctx.arc(centerX, centerY, outsideRadius + ringWidth / 2, 0, 2 * Math.PI);
  ctx.stroke();

  ctx.shadowBlur = 0;
  ctx.lineWidth = 2;
  ctx.strokeStyle = "rgba(0,0,0,0.06)";
  ctx.beginPath();
  ctx.arc(centerX, centerY, outsideRadius + ringWidth / 2 - 4, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.restore();

  updateOverlay();
}

// ---------------- Apply names ----------------
function applyNamesFromTextarea() {
  const btn = document.getElementById("updateNames");
  if (btn) {
    btn.classList.add("loading");
    setTimeout(() => btn.classList.remove("loading"), 500);
  }

  const inputText = document.getElementById("namesInput").value;
  names = inputText.split("\n").map((n) => n.trim()).filter(Boolean);
  setStoredValue(STORAGE_KEYS.names, names.join("\n"));

  if (names.length === 0) {
    originalNames = [];
    colors = [];
    angleCurrent = 0;
    spinOrder = 0;
    highlightIndex = null;
    blinkActive = false;
    blinkOn = false;
    document.getElementById("scoreboard").innerHTML = "";
    drawWheel();
    syncUrlWithItems([]);
    updatePointerPosition();
    // Keep shareSnapshotNames intact (so user can still share last list if they want)
    return;
  }

  originalNames = names.slice();
  colors = generateColors(names.length);
  angleCurrent = 0;
  highlightIndex = null;
  blinkActive = false;
  blinkOn = false;

  // Persist for sharing (survives resetGame())
  shareSnapshotNames = originalNames.slice();

  spinOrder = 0;
  document.getElementById("scoreboard").innerHTML = "";

  drawWheel();
  updatePointerPosition();
  syncUrlWithItems(shareSnapshotNames);
}

document.getElementById("updateNames").addEventListener("click", applyNamesFromTextarea);

let debounceTimeout;
document.getElementById("namesInput").addEventListener("input", () => {
  clearTimeout(debounceTimeout);
  debounceTimeout = setTimeout(() => {
    document.getElementById("updateNames").click();
  }, 500);
});

// ---------------- Actions (buttons) ----------------
document.getElementById("removeDuplicates").addEventListener("click", () => {
  const input = document.getElementById("namesInput");
  const lines = input.value.split(/\r?\n/).map((x) => x.trim()).filter(Boolean);

  const seen = new Set();
  const unique = [];
  for (const item of lines) {
    const key = item.toLowerCase();
    if (!seen.has(key)) {
      seen.add(key);
      unique.push(item);
    }
  }

  input.value = unique.join("\n");
  document.getElementById("updateNames").click();
  showToast("Duplicates removed.");
});

document.getElementById("shuffleNames").addEventListener("click", () => {
  const input = document.getElementById("namesInput");
  const lines = input.value.split(/\r?\n/).map((x) => x.trim()).filter(Boolean);

  for (let i = lines.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [lines[i], lines[j]] = [lines[j], lines[i]];
  }

  input.value = lines.join("\n");
  document.getElementById("updateNames").click();
  showToast("Shuffled.");
});

document.getElementById("loadSample").addEventListener("click", () => {
  const sample = ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace", "Heidi"];
  document.getElementById("namesInput").value = sample.join("\n");
  document.getElementById("updateNames").click();
  showToast("Sample loaded.");
});

// ---------------- Spin logic ----------------
function spin() {
  if (isSpinning || isAnimatingWinner || names.length < 2) return;

  highlightIndex = null;
  blinkActive = false;
  blinkOn = false;

  document.getElementById("overlayButton").style.display = "none";

  spinAngleStart = Math.random() * 10 + 10;
  spinTime = 0;
  spinTimeTotal = Math.random() * 3000 + 4000;
  isSpinning = true;

  spinSound.loop = true;
  spinSound.play();

  requestAnimationFrame(rotateWheel);
}

function rotateWheel() {
  if (!isSpinning) return;

  spinTime += 30;
  if (spinTime >= spinTimeTotal) {
    spinSound.pause();
    spinSound.currentTime = 0;
    stopRotateWheel();
    return;
  }

  const spinAngle = spinAngleStart - easeOut(spinTime, 0, spinAngleStart, spinTimeTotal);
  angleCurrent += (spinAngle * Math.PI) / 180;
  angleCurrent = angleCurrent % (2 * Math.PI);

  if (names.length > 0) {
    const currentIndex = getWinningIndex();
    if (lastTickIndex === null) lastTickIndex = currentIndex;
    if (currentIndex !== lastTickIndex) {
      playTick();
      lastTickIndex = currentIndex;
    }
  }

  drawWheel();
  requestAnimationFrame(rotateWheel);
}

function playTick() {
  try {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const o = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    o.type = "square";
    o.frequency.value = 1200;
    g.gain.value = 0.02;
    o.connect(g);
    g.connect(audioCtx.destination);
    o.start();
    setTimeout(() => o.stop(), 30);
  } catch (e) {}
}

function easeOut(t, b, c, d) {
  t /= d;
  return c * (--t * t * t + 1) + b;
}

function getWinningIndex() {
  const angleCurrentDeg = ((angleCurrent * 180) / Math.PI) % 360;
  const pointerAngle = 90;
  const effectiveAngle = (pointerAngle - angleCurrentDeg + 360) % 360;
  const arc = 360 / names.length;
  return Math.floor(effectiveAngle / arc);
}

function stopRotateWheel() {
  isSpinning = false;

  if (names.length === 1) {
    const lastName = names[0];
    addScoreboard(lastName);
    triggerWinnerAnimation(lastName, () => {
      names = [];
      setTimeout(resetGame, 1000);
    });
    return;
  }

  if (names.length === 2) {
    const index = getWinningIndex();
    const winningName = names[index];
    highlightIndex = index;
    addScoreboard(winningName);
    triggerWinnerAnimation(winningName, () => {
      names.splice(index, 1);
      addScoreboard(names[0]);
      names = [];
      resetGame();
    });
    return;
  }

  const index = getWinningIndex();
  const winningName = names[index];
  highlightIndex = index;
  addScoreboard(winningName);
  triggerWinnerAnimation(winningName, () => {
    names.splice(index, 1);
    drawWheel();
    updatePointerPosition();
    highlightIndex = null;
  });
}

function addScoreboard(winner) {
  spinOrder++;
  const scoreboardEl = document.getElementById("scoreboard");
  const li = document.createElement("li");
  li.className = "list-group-item";
  li.dataset.winner = winner;
  li.innerHTML = `<span class="order-number">${spinOrder}</span> ${winner}`;
  scoreboardEl.appendChild(li);
}

// ---------------- Winner animation (blink only) ----------------
function triggerWinnerAnimation(winningName, callback) {
  isAnimatingWinner = true;

  const winnerOverlay = document.getElementById("winnerOverlay");
  winnerOverlay.textContent = `${winningName} Wins!`;
  winnerOverlay.style.display = "block";

  winSound.play();

  // Enable blink during the animation
  blinkActive = true;
  blinkOn = true;

  const duration = 2400;
  const startTime = Date.now();

  function animate() {
    const elapsed = Date.now() - startTime;

    // Toggle blink every 180ms
    blinkOn = (Math.floor(elapsed / 180) % 2) === 0;

    // Redraw wheel with blink overlay
    drawWheel();

    if (elapsed < duration) {
      requestAnimationFrame(animate);
    } else {
      // End animation
      isAnimatingWinner = false;
      blinkActive = false;
      blinkOn = false;

      winnerOverlay.style.display = "none";
      drawWheel();
      updateOverlay();

      if (callback) callback();
    }
  }

  requestAnimationFrame(animate);
}

function resetGame() {
  // Keep shareSnapshotNames intact for sharing after game finishes.
  names = [];
  originalNames = [];
  angleCurrent = 0;
  isSpinning = false;
  spinOrder = 0;
  highlightIndex = null;
  blinkActive = false;
  blinkOn = false;
  drawWheel();
  updateOverlay();
}

// ---------------- UI triggers ----------------
document.getElementById("overlayButton").addEventListener("click", () => {
  if (!isSpinning && !isAnimatingWinner && names.length >= 2) spin();
});

canvas.addEventListener("click", () => {
  if (!isSpinning && !isAnimatingWinner && names.length >= 2) {
    spin();
  } else if (!isSpinning && !isAnimatingWinner && names.length === 1) {
    addScoreboard(names[0]);
    triggerWinnerAnimation(names[0], () => {
      names = [];
      resetGame();
    });
  }
});

// ---------------- Share Result ----------------
document.getElementById("shareResult").addEventListener("click", async () => {
  const resultLines = Array.from(document.querySelectorAll("#scoreboard li"))
    .map((li) => li.textContent.trim())
    .filter(Boolean);

  const result = resultLines.join("\n");

  const shareUrl = new URL(getBaseUrl());
  const listForShare =
    shareSnapshotNames && shareSnapshotNames.length ? shareSnapshotNames :
    originalNames && originalNames.length ? originalNames : [];

  if (listForShare.length) {
    shareUrl.searchParams.set("items", base64UrlEncode(listForShare.join("\n")));
  }

  const shareText = result
    ? "Check out my Wheel Of List results!\n\n" + result
    : "Try Wheel Of List — a free spinner for draws, classrooms, raffles and games.";

  try {
    if (navigator.share) {
      await navigator.share({ title: "Wheel Of List", text: shareText, url: shareUrl.toString() });
      showToast("Shared!");
      return;
    }
  } catch (e) {}

  const fallback = shareText + "\n\n" + shareUrl.toString();
  const ok = await copyToClipboard(fallback);
  showToast(ok ? "Copied to clipboard." : "Could not copy.");
});

// ---------------- Copy winner / ranking ----------------
document.getElementById("copyWinner").addEventListener("click", async () => {
  const winner = getLatestWinner();
  if (!winner) return showToast("No winner yet.");
  const ok = await copyToClipboard(winner);
  showToast(ok ? "Winner copied." : "Copy failed.");
});

document.getElementById("copyRanking").addEventListener("click", async () => {
  const winners = getScoreboardWinners();
  if (!winners.length) return showToast("No results yet.");
  const text = winners.map((w, i) => `${i + 1}. ${w}`).join("\n");
  const ok = await copyToClipboard(text);
  showToast(ok ? "Ranking copied." : "Copy failed.");
});

// ---------------- Share image (filled wheel + Top 5 + highlight FIRST winner row) ----------------
function downloadDataUrl(dataUrl, filename) {
  const a = document.createElement("a");
  a.href = dataUrl;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}

function renderWheelSnapshotDataUrl(list) {
  // IMPORTANT: in the download image, we don't need any winner highlight on the wheel.
  const prev = {
    names: names.slice(),
    originalNames: originalNames.slice(),
    colors: colors.slice(),
    angleCurrent,
    highlightIndex,
    blinkActive,
    blinkOn,
  };

  try {
    const useList =
      (list && list.length) ? list.slice()
      : (shareSnapshotNames && shareSnapshotNames.length) ? shareSnapshotNames.slice()
      : (originalNames && originalNames.length) ? originalNames.slice()
      : prev.names;

    names = useList.slice();
    originalNames = useList.slice();
    colors = generateColors(names.length);

    highlightIndex = null; // no wheel highlight for download image
    blinkActive = false;
    blinkOn = false;
    angleCurrent = 0;

    drawWheel();
    return canvas.toDataURL("image/png");
  } finally {
    names = prev.names;
    originalNames = prev.originalNames;
    colors = prev.colors;
    angleCurrent = prev.angleCurrent;
    highlightIndex = prev.highlightIndex;
    blinkActive = prev.blinkActive;
    blinkOn = prev.blinkOn;
    try { drawWheel(); } catch (e) {}
  }
}

async function generateShareImageDataUrl() {
  if (!canvas.width || !canvas.height) {
    try { resizeCanvas(); } catch (e) {}
  }
  if (!canvas.width || !canvas.height) return null;

  const ranking = getScoreboardWinners();
  const latest = ranking.length ? ranking[ranking.length - 1] : "";
  const firstWinner = ranking.length ? ranking[0] : "";

  const listForSnapshot =
    (shareSnapshotNames && shareSnapshotNames.length) ? shareSnapshotNames :
    (originalNames && originalNames.length) ? originalNames :
    [];

  const wheelDataUrl = renderWheelSnapshotDataUrl(listForSnapshot);

  const W = 1200, H = 630;
  const out = document.createElement("canvas");
  out.width = W;
  out.height = H;
  const octx = out.getContext("2d");

  // Background
  octx.fillStyle = "#0b1220";
  octx.fillRect(0, 0, W, H);

  const g = octx.createLinearGradient(0, 0, W, H);
  g.addColorStop(0, "rgba(255,255,255,0.06)");
  g.addColorStop(1, "rgba(255,255,255,0)");
  octx.fillStyle = g;
  octx.fillRect(0, 0, W, H);

  // Load wheel image
  const wheelImg = await new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = reject;
    img.src = wheelDataUrl;
  });

  // Wheel on right
  const wheelSize = 520;
  const wheelX = W - wheelSize - 80;
  const wheelY = Math.floor((H - wheelSize) / 2);

  octx.save();
  octx.shadowColor = "rgba(0,0,0,0.45)";
  octx.shadowBlur = 30;
  octx.drawImage(wheelImg, wheelX, wheelY, wheelSize, wheelSize);
  octx.restore();

  // Title / subtitle
  octx.fillStyle = "#ffffff";
  octx.font = "800 64px system-ui, -apple-system, Segoe UI, Roboto, Arial";
  octx.fillText("Wheel Of List", 80, 140);

  octx.fillStyle = "rgba(255,255,255,0.85)";
  octx.font = "500 34px system-ui, -apple-system, Segoe UI, Roboto, Arial";
  octx.fillText("Spin the wheel. Pick a winner.", 80, 200);

  // Keep “First winner” line 
  const winnerLine = firstWinner ? `Winner: ${firstWinner}` : "Winner: —";
  octx.fillStyle = "rgba(255,255,255,0.92)";
  octx.font = "700 36px system-ui, -apple-system, Segoe UI, Roboto, Arial";
  octx.fillText(winnerLine, 80, 250);

  // Ranking block (Top 5 only)
  const boxX = 80;
  const boxY = 280;
  const boxW = 560;
  const boxH = 270;

  octx.fillStyle = "rgba(255,255,255,0.06)";
  octx.fillRect(boxX, boxY, boxW, boxH);
  octx.strokeStyle = "rgba(255,255,255,0.14)";
  octx.lineWidth = 2;
  octx.strokeRect(boxX, boxY, boxW, boxH);

  octx.fillStyle = "#ffffff";
  octx.font = "800 30px system-ui, -apple-system, Segoe UI, Roboto, Arial";
  octx.fillText("Results (Top 5)", boxX + 18, boxY + 42);

  const maxLines = 5;
  const shown = ranking.slice(0, maxLines);

  let y = boxY + 78;
  const lineH = 36;
  octx.font = "600 28px system-ui, -apple-system, Segoe UI, Roboto, Arial";

  for (let i = 0; i < shown.length; i++) {
    const n = shown[i];
    const isFirst = firstWinner && n.trim().toLowerCase() === firstWinner.trim().toLowerCase();

    // Highlight ONLY the first winner row
    if (isFirst) {
      octx.fillStyle = "rgba(34,197,94,0.22)";
      octx.fillRect(boxX + 12, y - 26, boxW - 24, 34);
      octx.fillStyle = "#ffffff";
    } else {
      octx.fillStyle = "rgba(255,255,255,0.92)";
    }

    octx.fillText(`${i + 1}. ${n}`, boxX + 20, y);
    y += lineH;
  }

  if (ranking.length > shown.length) {
    octx.fillStyle = "rgba(255,255,255,0.70)";
    octx.font = "500 22px system-ui, -apple-system, Segoe UI, Roboto, Arial";
    octx.fillText(`+ ${ranking.length - shown.length} more…`, boxX + 20, boxY + boxH - 18);
  }

  // Footer / URL
  octx.fillStyle = "rgba(255,255,255,0.75)";
  octx.font = "500 24px system-ui, -apple-system, Segoe UI, Roboto, Arial";
  octx.fillText("wheeloflist.com", 80, 600);

  return out.toDataURL("image/png");
}

document.getElementById("downloadShareImage").addEventListener("click", async () => {
  try {
    const dataUrl = await generateShareImageDataUrl();
    if (!dataUrl) return showToast("Could not generate image.");
    downloadDataUrl(dataUrl, "wheeloflist-result.png");
    showToast("Image downloaded.");
  } catch (e) {
    console.error(e);
    showToast("Could not generate image.");
  }
});

// ---------------- Theme ----------------
document.getElementById("themeSelect").addEventListener("change", (e) => {
  const selectedTheme = e.target.value === "dark" ? "dark" : "light";
  document.body.classList.toggle("dark-theme", selectedTheme === "dark");
  setStoredValue(STORAGE_KEYS.theme, selectedTheme);
  drawWheel();
});

// Keyboard
document.addEventListener("keydown", (e) => {
  const target = e.target;
  const tagName = target && target.tagName ? target.tagName.toLowerCase() : "";
  const isTypingField =
    (target && target.isContentEditable) ||
    tagName === "input" ||
    tagName === "textarea" ||
    tagName === "select" ||
    tagName === "button";

  if (isTypingField) return;

  const isSpace = e.code === "Space" || e.key === " ";
  const isEnter = e.key === "Enter";

  if ((isSpace || isEnter) && currentView === "wheel" && !isSpinning && !isAnimatingWinner && names.length >= 2) {
    if (isSpace) e.preventDefault();
    spin();
  }
});

// ---------------- Init ----------------
(function init() {
  bindNavigationLinks();

  applyStoredTheme();

  const fromUrl = readItemsFromUrl();
  if (fromUrl && fromUrl.length) {
    document.getElementById("namesInput").value = fromUrl.join("\n");
  } else {
    const storedNames = getStoredValue(STORAGE_KEYS.names);
    if (storedNames && storedNames.trim()) {
      document.getElementById("namesInput").value = storedNames;
    }
  }

  initDefaultNames();
  resizeCanvas();
  applyNamesFromTextarea();

  const initialRoute = getRouteFromLocation();
  renderRoute(initialRoute);

  try {
    const hasToolQuery = new URL(window.location.href).searchParams.has("tool");
    if (hasToolQuery && initialRoute.type === "tool") {
      setUrlForTool(initialRoute.toolName, "replace");
    }
  } catch (e) {}

  window.addEventListener("popstate", () => {
    const route = getRouteFromLocation();
    renderRoute(route);
  });
})();

// ====== Module System ======
function switchToTool(toolName, options = {}) {
  navigateToTool(toolName, {
    updateUrl: options.updateUrl !== false,
    historyMode: options.historyMode || "push",
    scroll: options.scroll !== false,
  });
}

function backToWheel() {
  navigateToWheel({ updateUrl: true, historyMode: "push", scroll: true });
}