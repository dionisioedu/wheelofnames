/**
 * Random Number Generator - Ferramenta para gerar números aleatórios
 * Com histórico, temas, e excelente UX
 */

class RandomNumberGenerator {
  constructor() {
    this.minValue = 1;
    this.maxValue = 100;
    this.history = [];
    this.maxHistorySize = 10;
    this.isGenerating = false;
    
    // Audio elements
    this.spinSound = new Audio("audio/spin.mp3");
    this.winSound = new Audio("audio/win.mp3");
    
    this.init();
  }

  init() {
    this.setupDOM();
    this.attachEventListeners();
    this.loadHistory();
  }

  setupDOM() {
    const container = document.getElementById('tools-container');
    if (!container) return;

    this.html = `
      <div class="tools-section" id="number-generator-section">
        <div class="tools-header">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
              <h2>🎲 Random Number Generator</h2>
              <p class="tools-subtitle">Generate random numbers with ease</p>
            </div>
            <button class="btn-back-to-wheel" onclick="backToWheel()" title="Back to spinner">
              ← Back
            </button>
          </div>
        </div>

        <div class="tools-content">
          <div class="number-generator-wrapper">
            <!-- Input Section -->
            <div class="generator-inputs">
              <div class="input-group">
                <label for="min-value">Minimum</label>
                <input 
                  type="number" 
                  id="min-value" 
                  class="generator-input" 
                  value="1" 
                  placeholder="Minimum"
                >
              </div>

              <div class="input-group">
                <label for="max-value">Maximum</label>
                <input 
                  type="number" 
                  id="max-value" 
                  class="generator-input" 
                  value="100" 
                  placeholder="Maximum"
                >
              </div>

              <button class="btn btn-primary generator-btn" id="generate-btn">
                <span class="btn-text">Generate Number</span>
                <span class="btn-icon">🎲</span>
              </button>
            </div>

            <!-- Display Section -->
            <div class="generator-display">
              <div class="number-display-container">
                <div class="number-label">Random Number</div>
                <div class="number-display" id="number-result">-</div>
                <div class="number-range" id="number-range-display"></div>
              </div>
            </div>

            <!-- History Section -->
            <div class="generator-history">
              <div class="history-header">
                <h4>📊 History (last 10)</h4>
                <button class="btn-icon-small" id="clear-history-btn" title="Clear history">
                  🗑️
                </button>
              </div>
              <div class="history-list" id="history-list">
                <p class="empty-history">No numbers generated yet</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  attachEventListeners() {
    // Esperar o DOM estar pronto
    setTimeout(() => {
      const container = document.getElementById('tools-container');
      if (!container) return;

      const generateBtn = document.getElementById('generate-btn');
      const minInput = document.getElementById('min-value');
      const maxInput = document.getElementById('max-value');
      const clearBtn = document.getElementById('clear-history-btn');

      if (generateBtn) {
        generateBtn.addEventListener('click', () => this.generateNumber());
        generateBtn.addEventListener('keypress', (e) => {
          if (e.key === 'Enter') this.generateNumber();
        });
      }

      if (minInput && maxInput) {
        minInput.addEventListener('change', (e) => {
          this.minValue = parseInt(e.target.value) || 1;
          this.updateRangeDisplay();
        });
        maxInput.addEventListener('change', (e) => {
          this.maxValue = parseInt(e.target.value) || 100;
          this.updateRangeDisplay();
        });
      }

      if (clearBtn) {
        clearBtn.addEventListener('click', () => this.clearHistory());
      }

      // Permitir gerar com Enter nos inputs
      const inputs = [minInput, maxInput];
      inputs.forEach(input => {
        if (input) {
          input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.generateNumber();
          });
        }
      });

      this.updateRangeDisplay();
    }, 100);
  }

  generateNumber() {
    if (this.isGenerating) return;

    const minInput = document.getElementById('min-value');
    const maxInput = document.getElementById('max-value');
    
    const min = parseInt(minInput.value) || this.minValue;
    const max = parseInt(maxInput.value) || this.maxValue;

    if (min >= max) {
      alert('Minimum must be less than maximum!');
      return;
    }

    this.isGenerating = true;

    // Animação de geração
    const result = document.getElementById('number-result');
    const btn = document.getElementById('generate-btn');

    btn.classList.add('loading');
    result.classList.add('generating');

    // Simular "suspense" com números aleatórios rápidos
    let count = 0;
    const interval = setInterval(() => {
      const randomNum = Math.floor(Math.random() * (max - min + 1)) + min;
      result.textContent = randomNum;
      count++;

      if (count > 15) {
        clearInterval(interval);
        
        // Número final
        const finalNumber = Math.floor(Math.random() * (max - min + 1)) + min;
        result.textContent = finalNumber;
        result.classList.remove('generating');
        result.classList.add('generated');
        btn.classList.remove('loading');

        // Play win sound
        this.winSound.currentTime = 0;
        this.winSound.play();

        // Adicionar ao histórico
        this.addToHistory(finalNumber, min, max);

        // Remover animação após 1s
        setTimeout(() => {
          result.classList.remove('generated');
          this.isGenerating = false;
        }, 1000);
      }
    }, 30);
  }

  updateRangeDisplay() {
    const minInput = document.getElementById('min-value');
    const maxInput = document.getElementById('max-value');
    const rangeDisplay = document.getElementById('number-range-display');

    const min = parseInt(minInput.value) || this.minValue;
    const max = parseInt(maxInput.value) || this.maxValue;

    if (rangeDisplay) {
      rangeDisplay.textContent = `Between ${min} and ${max}`;
    }
  }

  addToHistory(number, min, max) {
    const timestamp = new Date().toLocaleTimeString('en-US');
    const entry = { number, min, max, timestamp };

    this.history.unshift(entry);

    if (this.history.length > this.maxHistorySize) {
      this.history.pop();
    }

    this.saveHistory();
    this.renderHistory();
  }

  renderHistory() {
    const historyList = document.getElementById('history-list');
    if (!historyList) return;

    if (this.history.length === 0) {
      historyList.innerHTML = '<p class="empty-history">No numbers generated yet</p>';
      return;
    }

    historyList.innerHTML = this.history
      .map((entry, index) => `
        <div class="history-item" style="animation-delay: ${index * 50}ms;">
          <div class="history-number">${entry.number}</div>
          <div class="history-info">
            <span class="history-range">${entry.min} - ${entry.max}</span>
            <span class="history-time">${entry.timestamp}</span>
          </div>
          <button class="btn-copy-small" onclick="navigator.clipboard.writeText('${entry.number}')">
            📋
          </button>
        </div>
      `)
      .join('');
  }

  clearHistory() {
    if (confirm('Are you sure you want to clear the history?')) {
      this.history = [];
      this.saveHistory();
      this.renderHistory();
    }
  }

  saveHistory() {
    localStorage.setItem('rng-history', JSON.stringify(this.history));
  }

  loadHistory() {
    const saved = localStorage.getItem('rng-history');
    if (saved) {
      this.history = JSON.parse(saved);
      setTimeout(() => this.renderHistory(), 150);
    }
  }

  activate() {
    const container = document.getElementById('tools-container');
    if (container && !document.getElementById('number-generator-section')) {
      container.innerHTML = this.html;
      this.attachEventListeners();
    }
    
    const section = document.getElementById('number-generator-section');
    if (section) {
      section.classList.add('active');
      section.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  deactivate() {
    const section = document.getElementById('number-generator-section');
    if (section) {
      section.classList.remove('active');
    }
  }
}

// Registrar o módulo
moduleManager.register('randomNumberGenerator', RandomNumberGenerator);
