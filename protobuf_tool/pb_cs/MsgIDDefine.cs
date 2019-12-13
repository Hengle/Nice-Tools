using System;
using System.Collections.Generic;
using System.Text;
public class MsgIDDefine
{
	static Dictionary<int, string> msgid2msgname = new Dictionary<int, string>();
	static Dictionary<string, int> msgname2msgid = new Dictionary<string, int>();
	static void Initialize()
	{
		msgid2msgname[10000] = "common.test4";
		msgname2msgid["common.test4"] = 10000;
		msgid2msgname[10001] = "common.test3";
		msgname2msgid["common.test3"] = 10001;
		msgid2msgname[10002] = "common.client_info";
		msgname2msgid["common.client_info"] = 10002;
		msgid2msgname[10003] = "common.match_player";
		msgname2msgid["common.match_player"] = 10003;
		msgid2msgname[20000] = "login.test2";
		msgname2msgid["login.test2"] = 20000;
		msgid2msgname[20001] = "login.test1";
		msgname2msgid["login.test1"] = 20001;
		msgid2msgname[20002] = "login.req_login";
		msgname2msgid["login.req_login"] = 20002;
		msgid2msgname[20003] = "login.rsp_login";
		msgname2msgid["login.rsp_login"] = 20003;
		msgid2msgname[20004] = "login.ntf_logout";
		msgname2msgid["login.ntf_logout"] = 20004;
		msgid2msgname[20010] = "user.req_create_user";
		msgname2msgid["user.req_create_user"] = 20010;
		msgid2msgname[20011] = "user.rsp_create_user";
		msgname2msgid["user.rsp_create_user"] = 20011;
		msgid2msgname[20012] = "user.req_change_name";
		msgname2msgid["user.req_change_name"] = 20012;
		msgid2msgname[20013] = "user.rsp_change_name";
		msgname2msgid["user.rsp_change_name"] = 20013;
		msgid2msgname[20020] = "room.req_join_match";
		msgname2msgid["room.req_join_match"] = 20020;
		msgid2msgname[20021] = "room.rsp_join_match";
		msgname2msgid["room.rsp_join_match"] = 20021;
		msgid2msgname[20022] = "room.ntf_join_match_mateinfo";
		msgname2msgid["room.ntf_join_match_mateinfo"] = 20022;
		msgid2msgname[20023] = "room.ntf_join_match_result";
		msgname2msgid["room.ntf_join_match_result"] = 20023;
		msgid2msgname[20024] = "room.req_cancel_join_match";
		msgname2msgid["room.req_cancel_join_match"] = 20024;
		msgid2msgname[20025] = "room.rsp_cancel_join_match";
		msgname2msgid["room.rsp_cancel_join_match"] = 20025;
	}
	static string GetMsgNameByID(int msgid)
	{
		string msgname = null;
		if (msgid2msgname.TryGetValue(msgid,out msgname))
		{
			return msgname;
		}
		return "";
	}
	static int GetMsgIDByName(string msgname)
	{
		int msgid = 0;
		if (msgname2msgid.TryGetValue(msgname,out msgid))
		{
			return msgid;
		}
		return 0;
	}
}
