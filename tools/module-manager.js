/**
 * Module Manager - Gerencia as ferramentas/módulos da aplicação
 * Permite adicionar, remover e controlar ferramentas facilmente
 */

class ModuleManager {
  constructor() {
    this.modules = {};
    this.activeModule = null;
  }

  register(moduleName, moduleClass) {
    this.modules[moduleName] = moduleClass;
    console.log(`✓ Módulo registrado: ${moduleName}`);
  }

  initialize(moduleName) {
    if (!this.modules[moduleName]) {
      console.error(`Módulo não encontrado: ${moduleName}`);
      return null;
    }

    const ModuleClass = this.modules[moduleName];
    return new ModuleClass();
  }

  switchTo(moduleName) {
    if (this.activeModule) {
      this.activeModule.deactivate?.();
    }
    this.activeModule = this.initialize(moduleName);
    this.activeModule?.activate?.();
  }

  getActiveModule() {
    return this.activeModule;
  }

  listModules() {
    return Object.keys(this.modules);
  }
}

// Criar instância global
const moduleManager = new ModuleManager();
