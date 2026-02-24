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

const canvas = document.getElementById("wheelCanvas");
const ctx = canvas.getContext("2d");
// Audio objects are loaded only if files exist to avoid 404 errors.
let spinSound = { play: () => {}, pause: () => {}, loop: false, currentTime: 0 };
let winSound = { play: () => {}, pause: () => {}, loop: false, currentTime: 0 };

// Attempt to load audio files (HEAD check) and replace the stubs when available.
function tryLoadAudio(path, assignTo) {
  try {
    fetch(path, { method: 'HEAD' }).then(res => {
      if (res.ok) {
        try {
          const a = new Audio(path);
          // preserve object reference assignment
          if (assignTo === 'spin') spinSound = a;
          if (assignTo === 'win') winSound = a;
        } catch (e) { /* ignore audio creation errors */ }
      }
    }).catch(() => {});
  } catch (e) {}
}
tryLoadAudio('audio/spin.mp3', 'spin');
tryLoadAudio('audio/win.mp3', 'win');

function updateOverlay() {
  const overlay = document.getElementById("overlayButton");
  const winnerOverlay = document.getElementById("winnerOverlay");
  overlay.style.display = (names.length >= 2 && !isSpinning && !isAnimatingWinner) ? "block" : "none";
  if (!isAnimatingWinner) winnerOverlay.style.display = "none";
}

function initDefaultNames() {
  if (names.length === 0) {
    names = ["Alice", "Bob", "Carol", "Dave", "Eve"];
    originalNames = names.slice();
    colors = generateColors(names.length);
    document.getElementById("namesInput").value = names.join("\n");
  }
}

function resizeCanvas() {
  const container = document.getElementById("wheel-container");
  // Use client sizes for more accurate layout calculations
  const containerRect = container.getBoundingClientRect();
  const maxSize = Math.min(containerRect.width, containerRect.height) * 0.9;
  const size = Math.floor(maxSize);
  canvas.width = size;
  canvas.height = size;
  canvas.style.width = size + 'px';
  canvas.style.height = size + 'px';
  // Update visuals that depend on canvas size and position
  drawWheel();
  updatePointerPosition();

  // Center overlay (spin button) over canvas
  const overlay = document.getElementById('overlayButton');
  if (overlay) {
    const canvasRect = canvas.getBoundingClientRect();
    // position relative to container to avoid page-coordinate issues
    const relLeft = (canvasRect.left - containerRect.left) + (canvasRect.width / 2);
    const relTop = (canvasRect.top - containerRect.top) + (canvasRect.height / 2);
    overlay.style.left = relLeft + 'px';
    overlay.style.top = relTop + 'px';
    overlay.style.transform = 'translate(-50%, -50%)';
  }

  // Update center knob element size/position
  const centerEl = document.getElementById('wheel-center');
  if (centerEl) {
    const knobSize = Math.max(48, Math.floor(size * 0.12));
    centerEl.style.width = knobSize + 'px';
    centerEl.style.height = knobSize + 'px';
    const canvasRect = canvas.getBoundingClientRect();
    const relLeft = (canvasRect.left - containerRect.left) + (canvasRect.width / 2);
    const relTop = (canvasRect.top - containerRect.top) + (canvasRect.height / 2);
    centerEl.style.left = relLeft + 'px';
    centerEl.style.top = relTop + 'px';
    centerEl.style.transform = 'translate(-50%, -50%)';
  }
}
window.addEventListener("resize", resizeCanvas);

function updatePointerPosition() {
  const canvasRect = canvas.getBoundingClientRect();
  const container = document.getElementById('wheel-container');
  const containerRect = container.getBoundingClientRect();
  const pointer = document.getElementById("pointer");

  // Simple positioning: pointer at bottom of wheel
  const relLeft = (canvasRect.left - containerRect.left) + (canvasRect.width / 2);
  const relTop = (canvasRect.top - containerRect.top) + canvasRect.height - 30;

  pointer.style.left = relLeft + 'px';
  pointer.style.top = relTop + 'px';
}

function generateColors(count) {
  const colorPairs = [];
  for (let i = 0; i < count; i++) {
    const hue = (i * 360 / count);
    colorPairs.push({
      start: `hsl(${hue}, 70%, 50%)`,
      end: `hsl(${hue + 30}, 70%, 70%)`
    });
  }
  return colorPairs;
}

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
    ctx.fillStyle = "black";
    ctx.font = "20px 'Quicksand', sans-serif";
    ctx.textAlign = "center";
    ctx.fillText("Enter names and update", centerX, centerY);
    updateOverlay();
    return;
  }

  const innerRadius = 30;
  const textRadius = innerRadius + ((outsideRadius - innerRadius) / 2);
  const arc = Math.PI * 2 / names.length;
  for (let i = 0; i < names.length; i++) {
    const angle = angleCurrent + i * arc;
    const gradient = ctx.createLinearGradient(centerX - outsideRadius, centerY - outsideRadius, centerX + outsideRadius, centerY + outsideRadius);
    gradient.addColorStop(0, colors[i].start);
    gradient.addColorStop(1, colors[i].end);
    ctx.fillStyle = gradient;
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.arc(centerX, centerY, outsideRadius, angle, angle + arc);
    ctx.fill();
    // Draw slice label with auto-scaling font to better fit long text
    ctx.save();
    ctx.fillStyle = "white";
    const textX = centerX + Math.cos(angle + arc / 2) * textRadius;
    const textY = centerY + Math.sin(angle + arc / 2) * textRadius;
    ctx.translate(textX, textY);
    ctx.rotate(angle + arc / 2);
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    // Determine max arc width available for text (approx)
    const arcLength = outsideRadius * arc;
    let fontSize = canvas.width < 768 ? 20 : 40;
    ctx.font = `bold ${fontSize}px 'Quicksand', sans-serif`;
    let measured = ctx.measureText(names[i]).width;
    // Reduce font until it fits within 80% of the arc length
    while (measured > arcLength * 0.8 && fontSize > 10) {
      fontSize -= 1;
      ctx.font = `bold ${fontSize}px 'Quicksand', sans-serif`;
      measured = ctx.measureText(names[i]).width;
    }
    ctx.fillText(names[i], 0, 0);
    ctx.restore();
    // If this slice is the highlighted winner, draw an accent border
    if (highlightIndex !== null && i === highlightIndex) {
      ctx.beginPath();
      ctx.moveTo(centerX, centerY);
      // Scale the slice by ~20% (increase radius)
      const scaleUp = 1.2;
      ctx.arc(centerX, centerY, outsideRadius * scaleUp, angle, angle + arc);
      ctx.closePath();
      ctx.lineWidth = 6;
      ctx.strokeStyle = 'rgba(255,255,255,0.95)';
      ctx.shadowBlur = 20;
      ctx.shadowColor = 'rgba(255,255,255,0.8)';
      ctx.stroke();
      ctx.shadowBlur = 0;
      ctx.lineWidth = 1;
    }
  }
  // Central circle is rendered via the overlay `#wheel-center` element for richer visuals.
  // Draw a textured/contrasting rim for the wheel to improve separation from white background
  ctx.save();
  const ringWidth = Math.max(8, Math.floor(canvas.width * 0.015));
  const grad = ctx.createLinearGradient(centerX - outsideRadius, centerY - outsideRadius, centerX + outsideRadius, centerY + outsideRadius);
  grad.addColorStop(0, '#ffffff');
  grad.addColorStop(0.45, '#f5f7fa');
  grad.addColorStop(0.6, '#e9eef5');
  grad.addColorStop(1, '#e0e6ee');
  ctx.lineWidth = ringWidth;
  ctx.strokeStyle = grad;
  ctx.shadowColor = 'rgba(0,0,0,0.12)';
  ctx.shadowBlur = 14;
  ctx.beginPath();
  ctx.arc(centerX, centerY, outsideRadius + (ringWidth / 2), 0, 2 * Math.PI);
  ctx.stroke();
  // subtle inner rim for contrast
  ctx.shadowBlur = 0;
  ctx.lineWidth = 2;
  ctx.strokeStyle = 'rgba(0,0,0,0.06)';
  ctx.beginPath();
  ctx.arc(centerX, centerY, outsideRadius + (ringWidth / 2) - 4, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.restore();
  updateOverlay();
}

document.getElementById("updateNames").addEventListener("click", () => {
  const btn = document.getElementById("updateNames");
  btn.classList.add("loading");
  setTimeout(() => btn.classList.remove("loading"), 500);
  const inputText = document.getElementById("namesInput").value;
  names = inputText.split("\n").map(n => n.trim()).filter(n => n);
  if (names.length === 0) {
    originalNames = [];
    spinOrder = 0;
    document.getElementById("scoreboard").innerHTML = "";
    drawWheel();
    return;
  }
  originalNames = names.slice();
  colors = generateColors(names.length);
  spinOrder = 0;
  document.getElementById("scoreboard").innerHTML = "";
  angleCurrent = 0;
  drawWheel();
  updatePointerPosition();
});

let debounceTimeout;
document.getElementById("namesInput").addEventListener("input", () => {
  clearTimeout(debounceTimeout);
  debounceTimeout = setTimeout(() => document.getElementById("updateNames").click(), 500);
});

function spin() {
  if (isSpinning || isAnimatingWinner || names.length < 2) return; // Prevent new spin while animation is running
  // Clear any previous highlight
  highlightIndex = null;
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
  // Use elapsed time for smoother animation
  spinTime += 30;
  if (spinTime >= spinTimeTotal) {
    spinSound.pause();
    spinSound.currentTime = 0;
    stopRotateWheel();
    return;
  }
  const spinAngle = spinAngleStart - easeOut(spinTime, 0, spinAngleStart, spinTimeTotal);
  angleCurrent += (spinAngle * Math.PI / 180);
  // Normalize angle to avoid large numbers
  angleCurrent = angleCurrent % (2 * Math.PI);
  // Detect slice crossing for tick sound
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

function playTick(){
  // small click using WebAudio to avoid missing audio file dependencies
  try{
    if(!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const o = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    o.type = 'square';
    o.frequency.value = 1200;
    g.gain.value = 0.02;
    o.connect(g);
    g.connect(audioCtx.destination);
    o.start();
    setTimeout(()=>{ o.stop(); }, 30);
  }catch(e){}
}

function easeOut(t, b, c, d) {
  t /= d;
  return c * (--t * t * t + 1) + b;
}

function getWinningIndex() {
  const angleCurrentDeg = (angleCurrent * 180 / Math.PI) % 360;
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
  } else if (names.length === 2) {
    const index = getWinningIndex();
    const winningName = names[index];
    highlightIndex = index;
    addScoreboard(winningName);
    triggerWinnerAnimation(winningName, () => {
      names.splice(index, 1);
      addScoreboard(names[0]); // Add the last name to the scoreboard without animation
      names = [];
      resetGame();
    });
  } else if (names.length >= 3) {
    const index = getWinningIndex();
    const winningName = names[index];
    highlightIndex = index;
    addScoreboard(winningName);
    triggerWinnerAnimation(winningName, () => {
      names.splice(index, 1);
      drawWheel();
      updatePointerPosition();
      // remove highlight once the wheel updates
      highlightIndex = null;
    });
  }
}

function addScoreboard(winner) {
  spinOrder++;
  const scoreboardEl = document.getElementById("scoreboard");
  const li = document.createElement("li");
  li.className = "list-group-item";
  li.innerHTML = `<span class="order-number">${spinOrder}</span> ${winner}`;
  scoreboardEl.appendChild(li);
}

function triggerWinnerAnimation(winningName, callback) {
  isAnimatingWinner = true;
  const winnerOverlay = document.getElementById("winnerOverlay");
  winnerOverlay.textContent = `${winningName} Wins!`;
  winnerOverlay.style.display = "block";
  winSound.play();

  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;
  const particles = [];
  for (let i = 0; i < 50; i++) {
    particles.push({
      x: centerX,
      y: centerY,
      angle: Math.random() * 2 * Math.PI,
      speed: Math.random() * 4 + 1,
      radius: Math.random() * 2 + 1,
      alpha: 1
    });
  }
  const duration = 3000;
  const startTime = Date.now();

  function animate() {
    const elapsed = Date.now() - startTime;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawWheel();
    particles.forEach(p => {
      p.x += Math.cos(p.angle) * p.speed;
      p.y += Math.sin(p.angle) * p.speed;
      p.alpha -= 0.02;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.radius, 0, 2 * Math.PI);
      ctx.fillStyle = `rgba(255,215,0,${Math.max(p.alpha, 0)})`;
      ctx.fill();
    });

    if (elapsed < duration) {
      requestAnimationFrame(animate);
    } else {
      isAnimatingWinner = false;
      winnerOverlay.style.display = "none";
      drawWheel();
      updateOverlay();
      if (callback) callback();
    }
  }
  requestAnimationFrame(animate);
}

function resetGame() {
  names = [];
  originalNames = [];
  angleCurrent = 0;
  isSpinning = false;
  spinOrder = 0;
  drawWheel();
  updateOverlay();
}

document.getElementById("overlayButton").addEventListener("click", () => {
  if (!isSpinning && !isAnimatingWinner && names.length >= 2) {
    spin();
  }
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

document.getElementById("shareResult").addEventListener("click", () => {
  const result = Array.from(document.querySelectorAll("#scoreboard li")).map(li => li.textContent).join("\n");
  const shareText = `Check out my Wheel of List results!\n${result}`;
  navigator.clipboard.writeText(shareText).then(() => alert("Results copied to clipboard!"));
});

document.getElementById("themeSelect").addEventListener("change", (e) => {
  document.body.classList.toggle("dark-theme", e.target.value === "dark");
  drawWheel();
});

document.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !isSpinning && !isAnimatingWinner && names.length >= 2) {
    spin();
  }
});

initDefaultNames();
resizeCanvas();

// ====== Module System ======
function switchToTool(toolName) {
  // Hide the wheel section
  const wheelSection = document.querySelector('.container-fluid > .row');
  const quickToolsSection = document.querySelector('.quick-tools-section');
  const toolsContainer = document.getElementById('tools-container');
  
  if (wheelSection) {
    wheelSection.style.display = 'none';
  }

  if (quickToolsSection) {
    quickToolsSection.style.display = 'none';
  }

  // Show tools container
  if (!toolsContainer) {
    const container = document.createElement('div');
    container.id = 'tools-container';
    document.body.insertBefore(container, document.querySelector('section'));
  }

  // Load the requested tool
  moduleManager.switchTo(toolName);

  // Scroll to top
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function backToWheel() {
  // Reload the page to restore the original state
  location.reload();
}
