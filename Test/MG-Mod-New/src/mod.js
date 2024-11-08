"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const loadMod_1 = require("./types/loadMod");
class Mod {
    container;
    // public container2: DependencyContainer;
    // public container3: DependencyContainer;
    Logger;
    VFS;
    modpath;
    clone;
    preSptLoad(container) {
        this.container = container;
        this.Logger = container.resolve("WinstonLogger");
        this.VFS = container.resolve("VFS");
        const PreSptModLoader = container.resolve('PreSptModLoader');
        this.modpath = PreSptModLoader.getModPath("MG-Mod-New");
    }
    postDBLoad(container) {
        this.container = container;
        (new loadMod_1.loadMod(this)).load();
    }
    postSptLoad(container) {
        this.container = container;
    }
}
module.exports = { mod: new Mod() };
//# sourceMappingURL=mod.js.map