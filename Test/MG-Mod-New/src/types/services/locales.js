"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Locales = void 0;
const LogTextColor_1 = require("C:/snapshot/project/obj/models/spt/logging/LogTextColor");
class Locales {
    mod;
    ConfigJson;
    color;
    globalLocales;
    constructor(mod, configJson) {
        this.mod = mod;
        this.ConfigJson = configJson;
        this.color = LogTextColor_1.LogTextColor;
        this.init();
    }
    init() {
        this.globalLocales = this.mod.container.resolve("DatabaseServer").getTables().locales.global;
        this.mod.Logger.log(Object.keys(this.globalLocales), this.color.RED);
    }
    addInfo(info) {
        for (let lang in this.globalLocales) {
            this.globalLocales[lang][info.id] = info.desc;
        }
    }
    addItemInfo(info) {
        const DescList = ["Name", "ShortName", "Description"];
        for (let lang in this.globalLocales) {
            this.globalLocales[lang][info.id] = info.desc;
        }
    }
    addQuestInfo(info) {
        const DescList = ["Name", "ShortName", "Description"];
        for (let lang in this.globalLocales) {
            this.globalLocales[lang][info.id] = info.desc;
        }
    }
    addTraderInfo(info) {
        const DescList = ["Name", "ShortName", "Description"];
        for (let lang in this.globalLocales) {
            this.globalLocales[lang][info.id] = info.desc;
        }
    }
}
exports.Locales = Locales;
//# sourceMappingURL=locales.js.map