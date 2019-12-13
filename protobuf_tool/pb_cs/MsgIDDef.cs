using System;
using System.Collections.Generic;
using System.Text;
public class MsgIDDef
{
	private Dictionary<int, Type> sc_msg_dic = new Dictionary<int, Type>();
	private static MsgIDDef instance;
	public static MsgIDDef Instance()
	{
		if (null == instance)
		{
			instance = new MsgIDDef();
		}
		return instance;
	}
	private MsgIDDef()
	{
		sc_msg_dic.Add(10000,typeof(common.test4));
		sc_msg_dic.Add(10001,typeof(common.test3));
		sc_msg_dic.Add(10002,typeof(common.client_info));
		sc_msg_dic.Add(10003,typeof(common.match_player));
		sc_msg_dic.Add(20000,typeof(login.test2));
		sc_msg_dic.Add(20001,typeof(login.test1));
		sc_msg_dic.Add(20002,typeof(login.req_login));
		sc_msg_dic.Add(20003,typeof(login.rsp_login));
		sc_msg_dic.Add(20004,typeof(login.ntf_logout));
		sc_msg_dic.Add(20010,typeof(user.req_create_user));
		sc_msg_dic.Add(20011,typeof(user.rsp_create_user));
		sc_msg_dic.Add(20012,typeof(user.req_change_name));
		sc_msg_dic.Add(20013,typeof(user.rsp_change_name));
		sc_msg_dic.Add(20020,typeof(room.req_join_match));
		sc_msg_dic.Add(20021,typeof(room.rsp_join_match));
		sc_msg_dic.Add(20022,typeof(room.ntf_join_match_mateinfo));
		sc_msg_dic.Add(20023,typeof(room.ntf_join_match_result));
		sc_msg_dic.Add(20024,typeof(room.req_cancel_join_match));
		sc_msg_dic.Add(20025,typeof(room.rsp_cancel_join_match));
	}
	public Type GetMsgType(int msgID)
	{
		Type msgType = null;
		sc_msg_dic.TryGetValue(msgID, out msgType);
		if (msgType==null)
		{
			return null;
		}
		return msgType;
	}
}
