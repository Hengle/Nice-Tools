#! python2
import sys
import os

luamsg_dir = "../pb_proto/"
msgid_conf = "../msgid.conf"

target_dir = "../pb_java/"

def compile_proto(proto_dir,target_dir):
	files = os.listdir(proto_dir)
	for f in files:
		if not f.endswith('.proto'):
			continue
		target_file = f.replace(".proto",".java")
		print ".\ProtoGen\protoc.exe --proto_path=" + proto_dir + " --java_out=" + target_dir + " " + proto_dir + f
		os.system(".\ProtoGen\protoc.exe --proto_path=" + proto_dir + " --java_out=" + target_dir + " " + proto_dir + f)
		

# compile_proto(cppmsg_dir,target_dir)
compile_proto(luamsg_dir,target_dir)


class MsgInfo(object):
	def __init__(self,msgid,msgname,comment):
		self.msgid = msgid
		self.msgname = msgname
		self.comment = comment
		
	msgid = ""
	msgname = ""
	comment = ""
	
def ParseMsgIDDefine(fs,msgidList):
	fs.writelines("");
	fs.writelines("import java.util.HashMap;");
	fs.writelines("import java.util.Map;");
	fs.writelines("public class MsgIDDefine");
	fs.writelines("{");
	fs.writelines("\tstatic Map<Integer, String> msgid2msgname = new HashMap<>();");
	fs.writelines("\tstatic Map<String, Integer> msgname2msgid = new HashMap<>();");
	fs.writelines("\tstatic void initialize()");
	fs.writelines("\t{");

	for _msgDef  in msgidList:
		fs.writelines("\t\tmsgid2msgname.put(%s,\"%s\");" % (_msgDef.msgid, _msgDef.msgname));
		fs.writelines("\t\tmsgname2msgid.put(\"%s\",%s);" % (_msgDef.msgname, _msgDef.msgid));
	fs.writelines("\t}");
	fs.writelines("\tstatic String getMsgNameByID(int msgid)");
	fs.writelines("\t{");

	fs.writelines("\t\treturn return msgid2msgname.getOrDefault(msgid,"");");
	fs.writelines("\t}");

	fs.writelines("\tstatic int getMsgIDByName(String msgname)");
	fs.writelines("\t{");
	fs.writelines("\t\treturn msgname2msgid.getOrDefault(msgname,0);");
	fs.writelines("\t}");
	fs.writelines("}");
	fs.flush();

	fs.close();
	
def ParseMsgIDDef(fs,msgidList):
	fs.writelines("");
	fs.writelines("using System;");
	fs.writelines("using System.Collections.Generic;");
	fs.writelines("using System.Text;");
	fs.writelines("public class MsgIDDef");
	fs.writelines("{");

	fs.writelines("\tprivate Dictionary<int, Type> sc_msg_dic = new Dictionary<int, Type>();");
	fs.writelines("\tprivate static MsgIDDef instance;");
	fs.writelines("\tpublic static MsgIDDef Instance()");

	fs.writelines("\t{");

	fs.writelines("\t\tif (null == instance)");
	fs.writelines("\t\t{");
	fs.writelines("\t\t\tinstance = new MsgIDDef();");
	fs.writelines("\t\t}");
	fs.writelines("\t\treturn instance;");
	fs.writelines("\t}");


	fs.writelines("\tprivate MsgIDDef()");
	fs.writelines("\t{");
	for _msgDef in msgidList:
		tmpMsgName = _msgDef.msgname;
		fs.writelines("\t\tsc_msg_dic.Add(%s,typeof(%s));"% (_msgDef.msgid, tmpMsgName));

	fs.writelines("\t}");
	fs.writelines("\tpublic Type getMsgType(int msgID)");
	fs.writelines("\t{");
	fs.writelines("\t\tType msgType = null;");
	fs.writelines("\t\tsc_msg_dic.TryGetValue(msgID, out msgType);");
	fs.writelines("\t\tif (msgType==null)");
	fs.writelines("\t\t{");
	fs.writelines("\t\t\treturn null;");
	fs.writelines("\t\t}");
	fs.writelines("\t\treturn msgType;");
	fs.writelines("\t}");
	fs.writelines("}");

	fs.flush();
	fs.close();

def ParseMsgIDDefineDic(fs,msgidList):
	fs.writelines("");
	fs.writelines("package net.protol;");
	fs.writelines("public class MsgIDDefineDic");
	fs.writelines("{");

	for _msgDef in msgidList:
		fs.writelines("\tpublic static final int %s = %s; %s"%( _msgDef.msgname.upper().replace(".","_"), _msgDef.msgid,_msgDef.comment));

	fs.writelines("}");
	fs.flush();
	fs.close();

def parse_msgfile(msgid_conf):
	msg_info_list = []
	msg_file = open(msgid_conf,"r")
	for line in msg_file.readlines():
		line = line.strip().rstrip()

		if not len(line) or line.startswith("#"):
			continue
		array_info = line.split("=")
		msgid = array_info[0].strip().rstrip()	#MSGID
		
		if int(msgid) < 100:		#server internal msg
			continue
		
		#array_info = array_info[1].split(',')	#MSGNAME
		#msgname = array_info[0].strip().rstrip()
		
		array_info = array_info[1].split("#")		
		comment = ""
		msgname = array_info[0].strip().rstrip()

		if len(array_info) > 1:
			comment = "//" + array_info[1].strip().rstrip()

		msg_info_list.append(MsgInfo(msgid,msgname,comment))
		
	return msg_info_list
	
class WrapFile:
	fs = None
	def __init__(self,real_file):
		self.fs = real_file
	def writelines(self,s):
		self.fs.write(s + "\n")
	def flush(self):
		self.fs.flush()
	def close(self):
		self.fs.close()
	
l=parse_msgfile(msgid_conf)

targetMsgIDPath = "../pb_java/net/protol/MsgIDDefineDic.java";
targetCSPath = "../pb_java/MsgIDDefine.java";
targetCSPath2 = "../pb_java/MsgIDDef.java";

# f = WrapFile(open(targetCSPath,"w+"))
# ParseMsgIDDefine(f,l)

# f = WrapFile(open(targetCSPath2,"w+"))
# ParseMsgIDDef(f,l)

f = WrapFile(open(targetMsgIDPath,"w+"))
ParseMsgIDDefineDic(f,l)

os.system("pause")