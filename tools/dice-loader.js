class DiceLoader {
  constructor() {
    this.diceCount = 2;
    this.maxDice = 10;
    this.history = [];
    this.maxHistorySize = 10;
    this.isAnimating = false;
    this.winSound = new Audio("audio/win.mp3");
    this.dice3D = null; // 3D dice renderer
    // Load history during construction
    this.loadHistory();
  }

  activate() {
    const container = document.getElementById('tools-container');
    
    // Generate history HTML with loaded data
    const historyHTML = this.generateHistoryHTML();
    
    container.innerHTML = `
      <div class="tools-section" id="dice-loader-section">
        <div class="tools-header">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
              <h2>🎰 Dice Roller</h2>
              <p class="tools-subtitle">Roll multiple dices and track your results</p>
            </div>
            <button class="btn-back-to-wheel" onclick="backToWheel()" title="Back to spinner">
              ← Back
            </button>
          </div>
        </div>

        <div class="tools-content">
          <div class="dice-roller-wrapper">
            <!-- Dice Count Control -->
            <div class="dice-controls-section">
              <label for="dice-count-slider" class="controls-label">Number of Dice</label>
              <div class="dice-count-control">
                <button class="dice-count-btn" onclick="moduleManager.getActiveTool().changeDiceCount(-1)">−</button>
                <input 
                  type="range" 
                  id="dice-count-slider"
                  class="dice-slider"
                  min="1" 
                  max="10" 
                  value="2"
                  onchange="moduleManager.getActiveTool().updateDiceCount(this.value)"
                  oninput="moduleManager.getActiveTool().updateDiceCount(this.value)"
                >
                <button class="dice-count-btn" onclick="moduleManager.getActiveTool().changeDiceCount(1)">+</button>
                <span class="dice-count-display" id="dice-count-display">2</span>
              </div>
            </div>

            <!-- Dice Animation Display -->
            <div class="dice-animation-section">
              <div id="dice3d-container" class="dice-3d-container" style="width: 100%; height: 400px; background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)); border-radius: 12px; overflow: hidden;"></div>
            </div>

            <!-- Roll Button -->
            <div class="dice-button-section">
              <button class="btn btn-primary dice-roll-btn" id="roll-btn" onclick="moduleManager.getActiveTool().rollDices()">
                <span class="btn-text">Roll Dices</span>
                <span class="btn-icon">🎲</span>
              </button>
            </div>

            <!-- Results Section -->
            <div class="dice-results-section" id="diceResults" style="display: none;">
              <div class="results-container">
                <div class="result-item">
                  <div class="result-label">Individual Results</div>
                  <div class="result-values" id="resultValues"></div>
                </div>
                <div class="result-item total">
                  <div class="result-label">Total</div>
                  <div class="result-total" id="resultTotal">0</div>
                </div>
              </div>
            </div>

            <!-- History Section -->
            <div class="dice-history-section">
              <div class="history-header">
                <h4>📋 History (last ${this.maxHistorySize})</h4>
                <button class="btn-icon-small" id="clear-history-dice" onclick="moduleManager.getActiveTool().clearHistory()" title="Clear history">
                  🗑️
                </button>
              </div>
              <div class="dice-history-list" id="dice-history-list">
                ${historyHTML}
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    container.style.display = 'block';
    
    // Initialize 3D dice renderer with correct count
    setTimeout(() => {
      if (!this.dice3D) {
        this.dice3D = new Dice3D('dice3d-container', this.diceCount);
        console.log(`[DiceLoader] 3D dice renderer initialized with ${this.diceCount} dice`);
      }
    }, 100);
  }

  deactivate() {
    const container = document.getElementById('tools-container');
    if (container) {
      container.innerHTML = '';
      container.style.display = 'none';
    }
    
    // Dispose 3D renderer
    if (this.dice3D) {
      this.dice3D.dispose();
      this.dice3D = null;
    }
  }

  generateHistoryHTML() {
    if (this.history.length === 0) {
      return '<p class="empty-history">No rolls yet. Roll some dices!</p>';
    }

    return this.history.map((entry) => `
      <div class="dice-history-item">
        <div class="history-content">
          <div class="history-dice-info">
            <span class="history-dice-badge">${entry.diceCount}D</span>
            <span class="history-results">${entry.results.join(' + ')}</span>
          </div>
          <div class="history-total">= <strong>${entry.total}</strong></div>
        </div>
        <div class="history-time">${entry.timestamp}</div>
      </div>
    `).join('');
  }

  changeDiceCount(delta) {
    let newCount = this.diceCount + delta;
    newCount = Math.max(1, Math.min(this.maxDice, newCount));
    this.updateDiceCount(newCount);
  }

  updateDiceCount(value) {
    const count = parseInt(value);
    if (count >= 1 && count <= this.maxDice) {
      this.diceCount = count;
      document.getElementById('dice-count-slider').value = this.diceCount;
      document.getElementById('dice-count-display').textContent = this.diceCount;
      
      // Update 3D dice if renderer exists
      if (this.dice3D) {
        this.dice3D.setDiceCount(this.diceCount);
        console.log(`[DiceLoader] Updated to ${this.diceCount} dice`);
      }
      
      // Hide results when changing dice count
      const resultsSection = document.getElementById('diceResults');
      if (resultsSection) {
        resultsSection.style.display = 'none';
      }
    }
  }

  rollDices() {
    if (this.isAnimating) return;
    
    this.isAnimating = true;
    document.getElementById('roll-btn').disabled = true;

    // Generate random results BEFORE animation starts
    const results = [];
    for (let i = 0; i < this.diceCount; i++) {
      const finalValue = Math.floor(Math.random() * 6) + 1;
      results.push(finalValue);
    }
    
    console.log('[DiceLoader] Generated values:', results);

    // Animate 3D dice with the results
    if (this.dice3D) {
      this.dice3D.rollDice(results, 1000);
    }

    const animationDuration = 1000;
    const startTime = Date.now();

    const animate = () => {
      const elapsed = Date.now() - startTime;
      const progress = Math.min(elapsed / animationDuration, 1);

      if (progress < 1) {
        requestAnimationFrame(animate);
      } else {
        // Finalize animation
        this.finalizeRoll(results);
      }
    };

    animate();
  }

  finalizeRoll(results) {
    let total = 0;
    results.forEach(val => total += val);

    // Show results
    this.showResults(results, total);

    // Save to history
    this.addToHistory(results, total);

    // Play sound
    this.winSound.currentTime = 0;
    this.winSound.play().catch(() => {});

    // Re-enable button after 5 seconds (when dice unfreezes) or when user clicks again
    setTimeout(() => {
      this.isAnimating = false;
      document.getElementById('roll-btn').disabled = false;
    }, 5500); // 5 seconds frozen + animation time
  }

  showResults(results, total) {
    const resultsSection = document.getElementById('diceResults');
    const resultValues = document.getElementById('resultValues');
    const resultTotal = document.getElementById('resultTotal');

    resultValues.innerHTML = results.map(val => `<span class="result-value-item">${val}</span>`).join('');
    resultTotal.textContent = total;
    
    resultsSection.style.display = 'block';
    resultsSection.classList.remove('animate-in');
    setTimeout(() => resultsSection.classList.add('animate-in'), 10);
  }

  addToHistory(results, total) {
    const timestamp = new Date().toLocaleTimeString();
    const entry = {
      diceCount: this.diceCount,
      results: results,
      total: total,
      timestamp: timestamp
    };

    this.history.unshift(entry);
    if (this.history.length > this.maxHistorySize) {
      this.history.pop();
    }

    this.saveHistory();
    this.updateHistoryDisplay();
  }

  updateHistoryDisplay() {
    const historyList = document.getElementById('dice-history-list');
    
    if (!historyList) {
      console.error('[DiceLoader] History list element NOT found');
      return;
    }
    
    console.log(`[DiceLoader] Rendering history in DOM (${this.history.length} items)`);
    const html = this.generateHistoryHTML();
    console.log('[DiceLoader] HTML generated:', html.substring(0, 100) + '...');
    historyList.innerHTML = html;
    console.log('[DiceLoader] innerHTML set. Current content:', historyList.innerHTML.substring(0, 100) + '...');
  }

  saveHistory() {
    localStorage.setItem('dice-history', JSON.stringify(this.history));
    console.log(`[DiceLoader] Saved ${this.history.length} history items`);
  }

  loadHistory() {
    const saved = localStorage.getItem('dice-history');
    if (saved) {
      try {
        this.history = JSON.parse(saved);
        console.log(`[DiceLoader] Loaded ${this.history.length} history items`);
      } catch (e) {
        console.error('[DiceLoader] Error loading history:', e);
        this.history = [];
      }
    } else {
      console.log('[DiceLoader] No history found in localStorage');
    }
  }

  clearHistory() {
    if (confirm('Clear all dice rolls history?')) {
      this.history = [];
      this.saveHistory();
      this.updateHistoryDisplay();
    }
  }
}

moduleManager.register('diceLoader', DiceLoader);

