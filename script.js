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

const canvas = document.getElementById("wheelCanvas");
const ctx = canvas.getContext("2d");
const spinSound = new Audio("audio/spin.mp3");
const winSound = new Audio("audio/win.mp3");

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
  const size = Math.min(container.offsetWidth * 0.9, container.offsetHeight * 0.9);
  canvas.width = size;
  canvas.height = size;
  drawWheel();
  updatePointerPosition();
}
window.addEventListener("resize", resizeCanvas);

function updatePointerPosition() {
  const canvasRect = canvas.getBoundingClientRect();
  const centerY = canvasRect.top + canvas.height / 2;
  const outsideRadius = canvas.width / 2 - 10;
  document.getElementById("pointer").style.top = (centerY + outsideRadius - 40) + "px";
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
    ctx.save();
    ctx.fillStyle = "white";
    const textX = centerX + Math.cos(angle + arc / 2) * textRadius;
    const textY = centerY + Math.sin(angle + arc / 2) * textRadius;
    ctx.translate(textX, textY);
    ctx.rotate(angle + arc / 2);
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.font = `bold ${canvas.width < 768 ? 20 : 40}px 'Quicksand', sans-serif`;
    ctx.fillText(names[i], 0, 0);
    ctx.restore();
  }
  ctx.beginPath();
  ctx.arc(centerX, centerY, 30, 0, 2 * Math.PI);
  ctx.fillStyle = "#ffffff";
  ctx.fill();
  ctx.beginPath();
  ctx.arc(centerX, centerY, outsideRadius + 10, 0, 2 * Math.PI);
  ctx.strokeStyle = "rgba(255, 255, 255, 0.5)";
  ctx.lineWidth = 5;
  ctx.shadowBlur = 20;
  ctx.shadowColor = "rgba(255, 255, 255, 0.8)";
  ctx.stroke();
  ctx.shadowBlur = 0;
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
  if (isSpinning || isAnimatingWinner || names.length < 2) return; // Impede novo giro durante animação
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
  angleCurrent += (spinAngle * Math.PI / 180);
  drawWheel();
  requestAnimationFrame(rotateWheel);
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
    addScoreboard(winningName);
    triggerWinnerAnimation(winningName, () => {
      names.splice(index, 1);
      addScoreboard(names[0]); // Adiciona o último nome ao placar sem animação
      names = [];
      resetGame();
    });
  } else if (names.length >= 3) {
    const index = getWinningIndex();
    const winningName = names[index];
    addScoreboard(winningName);
    triggerWinnerAnimation(winningName, () => {
      names.splice(index, 1);
      drawWheel();
      updatePointerPosition();
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
