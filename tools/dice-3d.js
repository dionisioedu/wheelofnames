/**
 * 3D Dice Renderer using Three.js
 * Renders multiple 3D dice and handles rotation animations
 */

class Dice3D {
  constructor(containerId, diceCount = 2) {
    this.containerId = containerId;
    this.diceCount = diceCount;
    this.scene = null;
    this.camera = null;
    this.renderer = null;
    this.cubes = [];
    this.isAnimating = false;
    this.isFrozen = false;
    this.frozenUntil = 0;
    this.init();
  }

  init() {
    const container = document.getElementById(this.containerId);
    if (!container) {
      console.error(`[3D Dice] Container ${this.containerId} not found`);
      return;
    }

    // Clear previous content
    container.innerHTML = '';

    // Scene setup
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0xfafafa);

    // Camera setup
    const width = container.clientWidth;
    const height = container.clientHeight;
    this.camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
    this.camera.position.z = 3.5;

    // Renderer setup
    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    this.renderer.setSize(width, height);
    this.renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(this.renderer.domElement);

    // Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
    this.scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.9);
    directionalLight.position.set(5, 5, 5);
    this.scene.add(directionalLight);

    // Create dice cubes
    this.createDice();

    // Handle window resize
    window.addEventListener('resize', () => this.onWindowResize());

    // Start animation loop
    this.animate();
  }

  createDice() {
    const geometry = new THREE.BoxGeometry(1.2, 1.2, 1.2);
    
    // Mapping for a real dice where opposite faces sum to 7
    // Three.js face order: [Right(+X), Left(-X), Top(+Y), Bottom(-Y), Front(+Z), Back(-Z)]
    const faceNumbers = [1, 6, 2, 5, 3, 4]; // Opposite faces sum to 7
    
    // Calculate positions for multiple dice
    const spacing = 1.8;
    const totalWidth = (this.diceCount - 1) * spacing;
    const startX = -totalWidth / 2;

    for (let diceIndex = 0; diceIndex < this.diceCount; diceIndex++) {
      const materials = [];

      // Create material for each face
      for (let faceIndex = 0; faceIndex < 6; faceIndex++) {
        const canvas = document.createElement('canvas');
        canvas.width = 256;
        canvas.height = 256;
        const ctx = canvas.getContext('2d');

        const faceNumber = faceNumbers[faceIndex];

        // Draw face background
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, 256, 256);
        ctx.strokeStyle = '#667eea';
        ctx.lineWidth = 8;
        ctx.strokeRect(10, 10, 236, 236);

        // Draw dots for this face number
        ctx.fillStyle = '#667eea';
        this.drawDotPattern(ctx, faceNumber);

        const texture = new THREE.CanvasTexture(canvas);
        const material = new THREE.MeshPhongMaterial({ map: texture });
        materials.push(material);
      }

      const cube = new THREE.Mesh(geometry, materials);
      cube.position.x = startX + diceIndex * spacing;
      cube.diceIndex = diceIndex;
      cube.currentValue = 1;
      this.scene.add(cube);
      this.cubes.push(cube);
    }
  }

  drawDotPattern(ctx, number) {
    const dotRadius = 20;
    const positions = {
      1: [[128, 128]],
      2: [[80, 80], [176, 176]],
      3: [[80, 80], [128, 128], [176, 176]],
      4: [[80, 80], [176, 80], [80, 176], [176, 176]],
      5: [[80, 80], [176, 80], [128, 128], [80, 176], [176, 176]],
      6: [[80, 80], [176, 80], [80, 128], [176, 128], [80, 176], [176, 176]]
    };

    const dots = positions[number] || [];
    dots.forEach(([x, y]) => {
      ctx.beginPath();
      ctx.arc(x, y, dotRadius, 0, Math.PI * 2);
      ctx.fill();
    });
  }

  animate() {
    requestAnimationFrame(() => this.animate());

    // Check if frozen period has ended
    if (this.isFrozen && Date.now() > this.frozenUntil) {
      this.isFrozen = false;
      console.log('[3D Dice] Unfroze dice, returning to idle animation');
    }

    // Slow rotation when idle (not animating and not frozen)
    if (!this.isAnimating && !this.isFrozen) {
      this.cubes.forEach((cube, index) => {
        cube.rotation.x += 0.003 + index * 0.001;
        cube.rotation.y += 0.005 + index * 0.001;
      });
    }

    this.renderer.render(this.scene, this.camera);
  }

  rollDice(values, duration = 1000) {
    if (this.isAnimating) return;

    this.isAnimating = true;
    this.isFrozen = false;
    const startTime = Date.now();

    // Setup target rotations for each cube with staggered timing
    this.cubes.forEach((cube, index) => {
      const staggerDelay = index * 100;
      
      const targetRotX = Math.random() * Math.PI * 4;
      const targetRotY = Math.random() * Math.PI * 4;
      const targetRotZ = Math.random() * Math.PI * 2;

      const startRotX = cube.rotation.x;
      const startRotY = cube.rotation.y;
      const startRotZ = cube.rotation.z;

      const animationFrame = () => {
        const elapsed = Math.max(0, Date.now() - startTime - staggerDelay);
        const progress = Math.min(elapsed / duration, 1);

        // Easing function (ease-out cubic)
        const easeProgress = 1 - Math.pow(1 - progress, 3);

        cube.rotation.x = startRotX + (targetRotX - startRotX) * easeProgress;
        cube.rotation.y = startRotY + (targetRotY - startRotY) * easeProgress;
        cube.rotation.z = startRotZ + (targetRotZ - startRotZ) * easeProgress;

        if (progress < 1) {
          requestAnimationFrame(animationFrame);
        }
      };

      animationFrame();
    });

    // After animation completes, show results with correct values
    setTimeout(() => {
      this.isAnimating = false;
      this.emphasisResults(values);
    }, duration + (this.diceCount - 1) * 100 + 200);
  }

  emphasisResults(values) {
    // First, rotate dice to show the correct face with the rolled value
    this.rotateDiceToShowValue(values);

    // Add pulse animation to cubes to emphasize results
    this.cubes.forEach((cube, index) => {
      const startScale = 1;
      const startTime = Date.now();
      const pulseDuration = 600;

      const pulseFrame = () => {
        const elapsed = Date.now() - startTime;
        const progress = elapsed / pulseDuration;

        if (progress < 1) {
          // Pulse animation: scale up and down
          const pulse = 1 + Math.sin(progress * Math.PI) * 0.15;
          cube.scale.set(pulse, pulse, pulse);
          requestAnimationFrame(pulseFrame);
        } else {
          cube.scale.set(1, 1, 1);
        }
      };

      pulseFrame();
    });

    // Freeze dice for 5 seconds before returning to idle
    this.isFrozen = true;
    this.frozenUntil = Date.now() + 5000;
    console.log('[3D Dice] Dice frozen for 5 seconds');
  }

  rotateDiceToShowValue(values) {
    // Three.js BoxGeometry face order: [+X, -X, +Y, -Y, +Z, -Z]
    // Our face numbers: [1, 6, 2, 5, 3, 4]
    // Camera is looking at +Z, so we need to rotate to bring each face to +Z position
    
    const rotationMap = {
      1: { x: 0, y: -Math.PI / 2, z: 0 },       // +X to front (-π/2 around Y)
      6: { x: 0, y: Math.PI / 2, z: 0 },        // -X to front (π/2 around Y)
      2: { x: Math.PI / 2, y: 0, z: 0 },        // +Y to front (π/2 around X)
      5: { x: -Math.PI / 2, y: 0, z: 0 },       // -Y to front (-π/2 around X)
      3: { x: 0, y: 0, z: 0 },                  // +Z is already front
      4: { x: 0, y: Math.PI, z: 0 }             // -Z to front (π around Y)
    };

    this.cubes.forEach((cube, index) => {
      const value = values[index] || 1;
      const targetRot = rotationMap[value] || rotationMap[1];

      // Rotate to show the correct face
      cube.rotation.order = 'YXZ';
      cube.rotation.x = targetRot.x;
      cube.rotation.y = targetRot.y;
      cube.rotation.z = targetRot.z;

      console.log(`[3D Dice] Cube ${index} rotating to show value: ${value}`);
    });
  }

  setDiceCount(count) {
    this.diceCount = count;
    // Recreate the scene with new dice count
    if (this.renderer) {
      this.renderer.dispose();
    }
    this.cubes = [];
    this.init();
  }

  onWindowResize() {
    const container = document.getElementById(this.containerId);
    if (!container) return;

    const width = container.clientWidth;
    const height = container.clientHeight;

    this.camera.aspect = width / height;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(width, height);
  }

  dispose() {
    if (this.renderer) {
      this.renderer.dispose();
      this.renderer.domElement.remove();
    }
  }
}
