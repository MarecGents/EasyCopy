"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.loadMod = void 0;
const IClone_1 = require("./utils/IClone");
const PathTypes_1 = require("./models/enums/PathTypes");
const locales_1 = require("./services/locales");
class loadMod {
    mod;
    constructor(mod) {
        this.mod = mod;
    }
    load() {
        const ConfigJson = new IClone_1.IClone(this.mod).clone(this.mod.modpath + PathTypes_1.PathTypes.ModConfigList).config;
        (new locales_1.Locales(this.mod, ConfigJson));
    }
}
exports.loadMod = loadMod;
//# sourceMappingURL=loadMod.js.map