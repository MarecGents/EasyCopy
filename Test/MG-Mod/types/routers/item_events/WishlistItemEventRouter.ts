import { WishlistCallbacks } from "@spt/callbacks/WishlistCallbacks";
import { HandledRoute, ItemEventRouterDefinition } from "@spt/di/Router";
import { IPmcData } from "@spt/models/eft/common/IPmcData";
import { IItemEventRouterResponse } from "@spt/models/eft/itemEvent/IItemEventRouterResponse";
import { inject, injectable } from "tsyringe";

@injectable()
export class WishlistItemEventRouter extends ItemEventRouterDefinition {
    constructor(@inject("WishlistCallbacks") protected wishlistCallbacks: WishlistCallbacks) {
        super();
    }

    public override getHandledRoutes(): HandledRoute[] {
        return [new HandledRoute("AddToWishList", false), new HandledRoute("RemoveFromWishList", false)];
    }

    public override async handleItemEvent(
        url: string,
        pmcData: IPmcData,
        body: any,
        sessionID: string,
    ): Promise<IItemEventRouterResponse> {
        switch (url) {
            case "AddToWishList":
                return this.wishlistCallbacks.addToWishlist(pmcData, body, sessionID);
            case "RemoveFromWishList":
                return this.wishlistCallbacks.removeFromWishlist(pmcData, body, sessionID);
        }
    }
}