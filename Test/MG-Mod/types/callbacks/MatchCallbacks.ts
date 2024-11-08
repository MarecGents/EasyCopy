import { MatchController } from "@spt/controllers/MatchController";
import { IEmptyRequestData } from "@spt/models/eft/common/IEmptyRequestData";
import { IGetBodyResponseData } from "@spt/models/eft/httpResponse/IGetBodyResponseData";
import { INullResponseData } from "@spt/models/eft/httpResponse/INullResponseData";
import { IEndOfflineRaidRequestData } from "@spt/models/eft/match/IEndOfflineRaidRequestData";
import { IGetRaidConfigurationRequestData } from "@spt/models/eft/match/IGetRaidConfigurationRequestData";
import { IGroupCharacter } from "@spt/models/eft/match/IGroupCharacter";
import { IMatchGroupCurrentResponse } from "@spt/models/eft/match/IMatchGroupCurrentResponse";
import { IMatchGroupInviteSendRequest } from "@spt/models/eft/match/IMatchGroupInviteSendRequest";
import { IMatchGroupPlayerRemoveRequest } from "@spt/models/eft/match/IMatchGroupPlayerRemoveRequest";
import { IMatchGroupStartGameRequest } from "@spt/models/eft/match/IMatchGroupStartGameRequest";
import { IMatchGroupStatusRequest } from "@spt/models/eft/match/IMatchGroupStatusRequest";
import { IMatchGroupStatusResponse } from "@spt/models/eft/match/IMatchGroupStatusResponse";
import { IMatchGroupTransferRequest } from "@spt/models/eft/match/IMatchGroupTransferRequest";
import { IProfileStatusResponse } from "@spt/models/eft/match/IProfileStatusResponse";
import { IPutMetricsRequestData } from "@spt/models/eft/match/IPutMetricsRequestData";
import { IRequestIdRequest } from "@spt/models/eft/match/IRequestIdRequest";
import { IUpdatePingRequestData } from "@spt/models/eft/match/IUpdatePingRequestData";
import { DatabaseService } from "@spt/services/DatabaseService";
import { HttpResponseUtil } from "@spt/utils/HttpResponseUtil";
import { JsonUtil } from "@spt/utils/JsonUtil";
import { inject, injectable } from "tsyringe";

@injectable()
export class MatchCallbacks {
    constructor(
        @inject("HttpResponseUtil") protected httpResponse: HttpResponseUtil,
        @inject("JsonUtil") protected jsonUtil: JsonUtil,
        @inject("MatchController") protected matchController: MatchController,
        @inject("DatabaseService") protected databaseService: DatabaseService,
    ) {}

    /** Handle client/match/updatePing */
    public updatePing(url: string, info: IUpdatePingRequestData, sessionID: string): INullResponseData {
        return this.httpResponse.nullResponse();
    }

    // Handle client/match/exit
    public exitMatch(url: string, info: IEmptyRequestData, sessionID: string): INullResponseData {
        return this.httpResponse.nullResponse();
    }

    /** Handle client/match/group/exit_from_menu */
    public exitToMenu(url: string, info: IEmptyRequestData, sessionID: string): INullResponseData {
        return this.httpResponse.nullResponse();
    }

    public groupCurrent(
        url: string,
        info: IEmptyRequestData,
        sessionID: string,
    ): IGetBodyResponseData<IMatchGroupCurrentResponse> {
        return this.httpResponse.getBody({ squad: [] });
    }

    public startGroupSearch(url: string, info: IEmptyRequestData, sessionID: string): INullResponseData {
        return this.httpResponse.nullResponse();
    }

    public stopGroupSearch(url: string, info: IEmptyRequestData, sessionID: string): INullResponseData {
        return this.httpResponse.nullResponse();
    }

    /** Handle client/match/group/invite/send */
    public sendGroupInvite(
        url: string,
        info: IMatchGroupInviteSendRequest,
        sessionID: string,
    ): IGetBodyResponseData<string> {
        return this.httpResponse.getBody("2427943f23698ay9f2863735");
    }

    /** Handle client/match/group/invite/accept */
    public acceptGroupInvite(
        url: string,
        info: IRequestIdRequest,
        sessionId: string,
    ): IGetBodyResponseData<IGroupCharacter[]> {
        const result = [];
        result.push({});

        return this.httpResponse.getBody(result);
    }

    /** Handle client/match/group/invite/decline */
    public declineGroupInvite(url: string, info: IRequestIdRequest, sessionId: string): IGetBodyResponseData<boolean> {
        return this.httpResponse.getBody(true);
    }

    /** Handle client/match/group/invite/cancel */
    public cancelGroupInvite(url: string, info: IRequestIdRequest, sessionID: string): IGetBodyResponseData<boolean> {
        return this.httpResponse.getBody(true);
    }

    /** Handle client/match/group/transfer */
    public transferGroup(
        url: string,
        info: IMatchGroupTransferRequest,
        sessionId: string,
    ): IGetBodyResponseData<boolean> {
        return this.httpResponse.getBody(true);
    }

    /** Handle client/match/group/invite/cancel-all */
    public cancelAllGroupInvite(
        url: string,
        info: IEmptyRequestData,
        sessionId: string,
    ): IGetBodyResponseData<boolean> {
        return this.httpResponse.getBody(true);
    }

    /** @deprecated - not called on raid start/end or game start/exit */
    public putMetrics(url: string, info: IPutMetricsRequestData, sessionId: string): INullResponseData {
        return this.httpResponse.nullResponse();
    }

    // Handle client/match/available
    public serverAvailable(url: string, info: IEmptyRequestData, sessionId: string): IGetBodyResponseData<boolean> {
        const output = this.matchController.getEnabled();

        return this.httpResponse.getBody(output);
    }

    /** Handle match/group/start_game */
    public joinMatch(
        url: string,
        info: IMatchGroupStartGameRequest,
        sessionID: string,
    ): IGetBodyResponseData<IProfileStatusResponse> {
        return this.httpResponse.getBody(this.matchController.joinMatch(info, sessionID));
    }

    /** Handle client/getMetricsConfig */
    public getMetrics(url: string, info: any, sessionID: string): IGetBodyResponseData<string> {
        return this.httpResponse.getBody(this.jsonUtil.serialize(this.databaseService.getMatch().metrics));
    }

    /**
     * Called periodically while in a group
     * Handle client/match/group/status
     * @returns
     */
    public getGroupStatus(
        url: string,
        info: IMatchGroupStatusRequest,
        sessionID: string,
    ): IGetBodyResponseData<IMatchGroupStatusResponse> {
        return this.httpResponse.getBody(this.matchController.getGroupStatus(info));
    }

    /** Handle client/match/group/delete */
    public deleteGroup(url: string, info: IEmptyRequestData, sessionID: string): IGetBodyResponseData<boolean> {
        this.matchController.deleteGroup(info);
        return this.httpResponse.getBody(true);
    }

    // Handle client/match/group/leave
    public leaveGroup(url: string, info: IEmptyRequestData, sessionID: string): IGetBodyResponseData<boolean> {
        return this.httpResponse.getBody(true);
    }

    /** Handle client/match/group/player/remove */
    public removePlayerFromGroup(
        url: string,
        info: IMatchGroupPlayerRemoveRequest,
        sessionID: string,
    ): IGetBodyResponseData<boolean> {
        return this.httpResponse.getBody(true);
    }

    /** Handle client/match/offline/end */
    public endOfflineRaid(url: string, info: IEndOfflineRaidRequestData, sessionID: string): INullResponseData {
        this.matchController.endOfflineRaid(info, sessionID);
        return this.httpResponse.nullResponse();
    }

    /** Handle client/raid/configuration */
    public getRaidConfiguration(
        url: string,
        info: IGetRaidConfigurationRequestData,
        sessionID: string,
    ): INullResponseData {
        this.matchController.startOfflineRaid(info, sessionID);
        return this.httpResponse.nullResponse();
    }

    /** Handle client/raid/configuration-by-profile */
    public getConfigurationByProfile(
        url: string,
        info: IGetRaidConfigurationRequestData,
        sessionID: string,
    ): INullResponseData {
        return this.httpResponse.nullResponse();
    }

    /** Handle client/match/group/raid/ready */
    public raidReady(url: string, info: IEmptyRequestData, sessionId: string): IGetBodyResponseData<boolean> {
        return this.httpResponse.getBody(true);
    }

    /** Handle client/match/group/raid/not-ready */
    public notRaidReady(url: string, info: IEmptyRequestData, sessionId: string): IGetBodyResponseData<boolean> {
        return this.httpResponse.getBody(true);
    }
}