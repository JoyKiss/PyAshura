#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-31 13:16:28

'''
pyuic5 test.ui –o test.py
if __name__=='__main__':

    app=QtWidgets.QApplication(sys.argv)

    Form=QtWidgets.QWidget()

    ui=Ui_Dialog()

    ui.setupUi(Form)

    Form.show()

    sys.exit(app.exec_())
'''

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *  
import cv2
myuser="958685878@qq.com"
mypasswd="958685878jayxk"
import urllib.request
import re
import ssl
import urllib.parse
import http.cookiejar
import datetime
import time

#为了防止ssl出现问题，你可以加上下面一行代码
ssl._create_default_https_context = ssl._create_unverified_context
#查票
#常用三字码与站点对应关系
areatocode={"北京北":"VAP","北京东":"BOP","北京":"BJP","北京南":"VNP","北京西":"BXP","广州南":"IZQ","重庆北":"CUW","重庆":"CQW","重庆南":"CRW","重庆西":"CXW","广州东":"GGQ","上海":"SHH","上海南":"SNH","上海虹桥":"AOH","上海西":"SXH","天津北":"TBP","天津":"TJP","天津南":"TIP","天津西":"TXP","长春":"CCT","长春南":"CET","长春西":"CRT","成都东":"ICW","成都南":"CNW","成都":"CDW","长沙":"CSQ","长沙南":"CWQ","福州":"FZS","福州南":"FYS","贵阳":"GIW","广州":"GZQ","广州西":"GXQ","哈尔滨":"HBB","哈尔滨东":"VBB","哈尔滨西":"VAB","合肥":"HFH","合肥西":"HTH","呼和浩特东":"NDC","呼和浩特":"HHC","海  口东":"KEQ","海口东":"HMQ","海口":"VUQ","杭州东":"HGH","杭州":"HZH","杭州南":"XHH","济南":"JNK","济南东":"JAK","济南西":"JGK","昆明":"KMM","昆明西":"KXM","拉萨":"LSO","兰州东":"LVJ","兰州":"LZJ","兰州西":"LAJ","南昌":"NCG","南京":"NJH","南京南":"NKH","南宁":"NNZ","石家庄北":"VVP","石家庄":"SJP","沈阳":"SYT","沈阳北":"SBT","沈阳东":"SDT","沈阳南":"SOT","太原北":"TBV","太原东":"TDV","太原":"TYV","武汉":"WHN","王家营西":"KNM","乌鲁木齐南":"WMR","西安北":"EAY","西安":"XAY","西安南":"CAY","西宁":"XNO","银川":"YIJ","郑州":"ZZF","阿尔山":"ART","安康":"AKY","阿克苏":"ASR","阿里河":"AHX","阿拉山口":"AKR","安平":"APT","安庆":"AQH","安顺":"ASW","鞍山":"AST","安阳":"AYF","北安":"BAB","蚌埠":"BBH","白城":"BCT","北海":"BHZ","白河":"BEL","白涧":"BAP","宝鸡":"BJY","滨江":"BJB","博克图":"BKX","百色":"BIZ","白山市":"HJL","北台":"BTT","包头东":"BDC","包头":"BTC","北屯市":"BXR","本溪":"BXT","白云鄂博":"BEC","白银西":"BXJ","亳州":"BZH","赤壁":"CBN","常德":"VGQ","承德":"CDP","长甸":"CDT","赤峰":"CFD","茶陵":"CDG","苍南":"CEH","昌平":"CPP","崇仁":"CRG","昌图":"CTT","长汀镇":"CDB","曹县":"CXK","楚雄南":"COM","陈相屯":"CXT","长治北":"CBF","池州":"IYH","长征":"CZJ","常州":"CZH","郴州":"CZQ","长治":"CZF","沧州":"COP","崇左":"CZZ","大安北":"RNT","大成":"DCT","丹东":"DUT","东方红":"DFB","东莞东":"DMQ","大虎山":"DHD","敦煌":"DHJ","敦化":"DHL","德惠":"DHT","东京城":"DJB","大涧":"DFP","都江堰":"DDW","大连北":"DFT","大理":"DKM","大连":"DLT","定南":"DNG","大庆":"DZX","东胜":"DOC","大石桥":"DQT","大同":"DTV","东营":"DPK","大杨树":"DUX","都匀":"RYW","邓州":"DOF","达州":"RXW","德州":"DZP","额济纳":"EJC","二连":"RLC","恩施":"ESN","福鼎":"FES","凤凰机场":"FJQ","风陵渡":"FLV","涪陵":"FLW","富拉尔基":"FRX","抚顺北":"FET","佛山":"FSQ","阜新南":"FXD","阜阳":"FYH","格尔木":"GRO","广汉":"GHW","古交":"GJV","桂林北":"GBZ","古莲":"GRX","桂林":"GLZ","固始":"GXN","广水":"GSN","干塘":"GNJ","广元":"GYW","广州北":"GBQ","赣州":"GZG","公主岭":"GLT","公主岭南":"GBT","淮安":"AUH","淮北":"HRH","鹤北":"HMB","淮滨":"HVN","河边":"HBV","潢川":"KCN","韩城":"HCY","邯郸":"HDP","横道河子":"HDB","鹤岗":"HGB","皇姑屯":"HTT","红果":"HEM","黑河":"HJB","怀化":"HHQ","汉口":"HKN","葫芦岛":"HLD","海拉尔":"HRX","霍林郭勒":"HWD","海伦":"HLB","侯马":"HMV","哈密":"HMR","淮南":"HAH","桦南":"HNB","海宁西":"EUH","鹤庆":"HQM","怀柔北":"HBP","怀柔":"HRP","黄石东":"OSN","华山":"HSY","黄山":"HKH","黄石":"HSN","衡水":"HSP","衡阳":"HYQ","菏泽":"HIK","贺州":"HXZ","汉中":"HOY","惠州":"HCQ","吉安":"VAG","集安":"JAL","江边村":"JBG","晋城":"JCF","金城江":"JJZ","景德镇":"JCG","嘉峰":"JFF","加格达奇":"JGX","井冈山":"JGG","蛟河":"JHL","金华南":"RNH","金华":"JBH","九江":"JJG","吉林":"JLL","荆门":"JMN","佳木斯":"JMB","济宁":"JIK","集宁南":"JAC","酒泉":"JQJ","江山":"JUH","吉首":"JIQ","九台":"JTL","镜铁山":"JVJ","鸡西":"JXB","绩溪县":"JRH","嘉峪关":"JGJ","江油":"JFW","锦州":"JZD","金州":"JZT","蓟州":"JKP","库尔勒":"KLR","开封":"KFF","岢岚":"KLV","凯里":"KLW","喀什":"KSR","昆山南":"KNH","奎屯":"KTR","开原":"KYT","六安":"UAH","灵宝":"LBF","芦潮港":"UCH","隆昌":"LCW","陆川":"LKZ","利川":"LCN","临川":"LCG","潞城":"UTP","鹿道":"LDL","娄底":"LDQ","临汾":"LFV","良各庄":"LGP","临河":"LHC","漯河":"LON","绿化":"LWJ","隆化":"UHP","丽江":"LHM","临江":"LQL","龙井":"LJL","吕梁":"LHV","醴陵":"LLG","柳林南":"LKV","滦平":"UPP","六盘水":"UMW","灵丘":"LVV","旅顺":"LST","兰溪":"LWH","陇西":"LXJ","澧县":"LEQ","临西":"UEP","龙岩":"LYS","耒阳":"LYQ","洛阳":"LYF","连云港东":"UKH","洛阳东":"LDF","临沂":"LVK","洛阳龙门":"LLF","柳园":"DHR","凌源":"LYD","辽源":"LYL","立志":"LZX","柳州":"LZZ","辽中":"LZD","麻城":"MCN","免渡河":"MDX","牡丹江":"MDB","莫尔道嘎":"MRX","明光":"MGH","满归":"MHX","漠河":"MVX","茂名":"MDQ","茂名西":"MMZ","密山":"MSB","马三家":"MJT","麻尾":"VAW","绵阳":"MYW","梅州":"MOQ","满洲里":"MLX","宁波东":"NVH","宁波":"NGH","南岔":"NCB","南充":"NCW","南丹":"NDZ","南大庙":"NMP","南芬":"NFT","讷河":"NHX","嫩江":"NGX","内江":"NJW","南平":"NPS","南通":"NUH","南阳":"NFF","碾子山":"NZX","平顶山":"PEN","盘锦":"PVD","平凉":"PIJ","平凉南":"POJ","平泉":"PQP","坪石":"PSQ","萍乡":"PXG","凭祥":"PXZ","郫县西":"PCW","攀枝花":"PRW","蕲春":"QRN","青城山":"QSW","青岛":"QDK","清河城":"QYP","曲靖":"QJM","黔江":"QNW","前进镇":"QEB","齐齐哈尔":"QHX","七台河":"QTB","沁县":"QVV","泉州东":"QRS","泉州":"QYS","衢州":"QEH","融安":"RAZ","汝箕沟":"RQJ","瑞金":"RJG","日照":"RZK","双城堡":"SCB","绥芬河":"SFB","韶关东":"SGQ","山海关":"SHD","绥化":"SHB","三间房":"SFX","苏家屯":"SXT","舒兰":"SLL","三明":"SMS","神木南":"OMY","三门峡":"SMF","商南":"ONY","遂宁":"NIW","四平":"SPT","商丘":"SQF","上饶":"SRG","韶山":"SSQ","宿松":"OAH","汕头":"OTQ","邵武":"SWS","涉县":"OEP","三亚":"SEQ","三  亚":"JUQ","邵阳":"SYQ","十堰":"SNN","双鸭山":"SSB","松原":"VYT","苏州":"SZH","深圳":"SZQ","宿州":"OXH","随州":"SZN","朔州":"SUV","深圳西":"OSQ","塘豹":"TBQ","塔尔气":"TVX","潼关":"TGY","塘沽":"TGP","塔河":"TXX","通化":"THL","泰来":"TLX","吐鲁番":"TFR","通辽":"TLD","铁岭":"TLT","陶赖昭":"TPT","图们":"TML","铜仁":"RDQ","唐山北":"FUP","田师府":"TFT","泰山":"TAK","唐山":"TSP","天水":"TSJ","通远堡":"TYT","太阳升":"TQT","泰州":"UTH","桐梓":"TZW","通州西":"TAP","五常":"WCB","武昌":"WCN","瓦房店":"WDT","威海":"WKK","芜湖":"WHH","乌海西":"WXC","吴家屯":"WJT","武隆":"WLW","乌兰浩特":"WWT","渭南":"WNY","威舍":"WSM","歪头山":"WIT","武威":"WUJ","武威南":"WWJ","无锡":"WXH","乌西":"WXR","乌伊岭":"WPB","武夷山":"WAS","万源":"WYY","万州":"WYW","梧州":"WZZ","温州":"RZH","温州南":"VRH","西昌":"ECW","许昌":"XCF","西昌南":"ENW","香坊":"XFB","轩岗":"XGV","兴国":"EUG","宣汉":"XHY","新会":"EFQ","新晃":"XLQ","锡林浩特":"XTC","兴隆县":"EXP","厦门北":"XKS","厦门":"XMS","厦门高崎":"XBS","小市":"XST","秀山":"ETW","向塘":"XTG","宣威":"XWM","新乡":"XXF","信阳":"XUN","咸阳":"XYY","襄阳":"XFN","熊岳城":"XYT","新沂":"VIH","兴义":"XRZ","新余":"XUG","徐州":"XCH","延安":"YWY","宜宾":"YBW","亚布力南":"YWB","叶柏寿":"YBD","宜昌东":"HAN","永川":"YCW","盐城":"AFH","宜昌":"YCN","运城":"YNV","伊春":"YCB","榆次":"YCV","杨村":"YBP","宜春西":"YCG","伊尔施":"YET","燕岗":"YGW","永济":"YIV","延吉":"YJL","营口":"YKT","牙克石":"YKX","阎良":"YNY","玉林":"YLZ","榆林":"ALY","亚龙湾":"TWQ","一面坡":"YPB","伊宁":"YMR","阳平关":"YAY","玉屏":"YZW","原平":"YPV","延庆":"YNP","阳泉曲":"YYV","玉泉":"YQB","阳泉":"AQP","营山":"NUW","玉山":"YNG","燕山":"AOP","榆树":"YRT","鹰潭":"YTG","烟台":"YAK","伊图里河":"YEX","玉田县":"ATP","义乌":"YWH","阳新":"YON","义县":"YXD","益阳":"AEQ","岳阳":"YYQ","崖州":"YUQ","永州":"AOQ","扬州":"YLH","淄博":"ZBK","镇城底":"ZDV","自贡":"ZGW","珠海":"ZHQ","珠海北":"ZIQ","湛江":"ZJZ","镇江":"ZJH","张家界":"DIQ","张家口":"ZKP","张家口南":"ZMP","周口":"ZKN","哲里木":"ZLC","扎兰屯":"ZTX","驻马店":"ZDN","肇庆":"ZVQ","周水子":"ZIT","昭通":"ZDW","中卫":"ZWJ","资阳":"ZYW","遵义西":"ZIW","枣庄":"ZEK","资中":"ZZW","株洲":"ZZQ","枣庄西":"ZFK","昂昂溪":"AAX","阿城":"ACB","安达":"ADX","安德":"ARW","安定":"ADP","安多":"ADO","安广":"AGT","敖汉":"YED","艾河":"AHP","安化":"PKQ","艾家村":"AJJ","鳌江":"ARH","安家":"AJB","阿金":"AJD","安靖":"PYW","阿克陶":"AER","安口窑":"AYY","敖力布告":"ALD","安龙":"AUZ","阿龙山":"ASX","安陆":"ALN","阿木尔":"JTX","阿南庄":"AZM","安庆西":"APH","鞍山西":"AXT","安塘":"ATV","安亭北":"ASH","阿图什":"ATR","安图":"ATL","安溪":"AXS","博鳌":"BWQ","北碚":"BPW","白壁关":"BGV","蚌埠南":"BMH","巴楚":"BCR","板城":"BUP","北戴河":"BEP","保定":"BDP","宝坻":"BPP","八达岭":"ILP","巴东":"BNN","柏果":"BGM","布海":"BUT","白河东":"BIY","贲红":"BVC","宝华山":"BWH","白河县":"BEY","白芨沟":"BJJ","碧鸡关":"BJM","北滘":"IBQ","碧江":"BLQ","白鸡坡":"BBM","笔架山":"BSB","八角台":"BTD","保康":"BKD","白奎堡":"BKB","白狼":"BAT","百浪":"BRZ","博乐":"BOR","宝拉格":"BQC","巴林":"BLX","宝林":"BNB","北流":"BOZ","勃利":"BLB","布列开":"BLR","宝龙山":"BND","百里峡":"AAP","八面城":"BMD","班猫箐":"BNM","八面通":"BMB","北马圈子":"BRP","北票南":"RPD","白旗":"BQP","宝泉岭":"BQB","白泉":"BQL","巴山":"BAY","白水江":"BSY","白沙坡":"BPM","白石山":"BAL","白水镇":"BUM","包头 东":"FDC","坂田":"BTQ","泊头":"BZP","北屯":"BYP","本溪湖":"BHT","博兴":"BXK","八仙筒":"VXD","白音察干":"BYC","背荫河":"BYB","北营":"BIV","巴彦高勒":"BAC","白音他拉":"BID","鲅鱼圈":"BYT","白银市":"BNJ","白音胡硕":"BCD","巴中":"IEW","霸州":"RMP","北宅":"BVP","赤壁北":"CIN","查布嘎":"CBC","长城":"CEJ","长冲":"CCM","承德东":"CCP","赤峰西":"CID","嵯岗":"CAX","柴岗":"CGT","长葛":"CEF","柴沟堡":"CGV","城固":"CGY","陈官营":"CAJ","成高子":"CZB","草海":"WBW","柴河":"CHB","册亨":"CHZ","草河口":"CKT","崔黄口":"CHP","巢湖":"CIH","蔡家沟":"CJT","成吉思汗":"CJX","岔江":"CAM","蔡家坡":"CJY","昌乐":"CLK","超梁沟":"CYP","慈利":"CUQ","昌黎":"CLP","长岭子":"CLT","晨明":"CMB","长农":"CNJ","昌平北":"VBP","常平":"DAQ","长坡岭":"CPM","辰清":"CQB","蔡山":"CON","楚山":"CSB","长寿":"EFW","磁山":"CSP","苍石":"CST","草市":"CSL","察素齐":"CSC","长山屯":"CVT","长汀":"CES","朝天南":"CTY","昌图西":"CPT","春湾":"CQQ","磁县":"CIP","岑溪":"CNZ","辰溪":"CXQ","磁西":"CRP","长兴南":"CFH","磁窑":"CYK","春阳":"CAL","城阳":"CEK","创业村":"CEX","朝阳川":"CYL","朝阳地":"CDD","朝阳南":"CYD","长垣":"CYF","朝阳镇":"CZL","滁州北":"CUH","常州北":"ESH","滁州":"CXH","潮州":"CKQ","常庄":"CVK","曹子里":"CFP","车转湾":"CWM","郴州西":"ICQ","沧州西":"CBP","德安":"DAG","大安":"RAT","大坝":"DBJ","大板":"DBC","大巴":"DBD","到保":"RBT","定边":"DYJ","东边井":"DBB","德伯斯":"RDT","打柴沟":"DGJ","德昌":"DVW","滴道":"DDB","大磴沟":"DKJ","刀尔登":"DRD","得耳布尔":"DRX","杜尔伯特":"TKX","东方":"UFQ","丹凤":"DGY","东丰":"DIL","都格":"DMM","大官屯":"DTT","大关":"RGW","东光":"DGP","东海":"DHB","大灰厂":"DHP","大红旗":"DQD","大禾塘":"SOQ","东海县":"DQH","德惠西":"DXT","达家沟":"DJT","东津":"DKB","杜家":"DJL","大口屯":"DKP","东来":"RVD","德令哈":"DHO","大陆号":"DLC","带岭":"DLB","大林":"DLD","达拉特旗":"DIC","独立屯":"DTX","豆罗":"DLV","达拉特西":"DNC","大连西":"GZT","东明村":"DMD","洞庙河":"DEP","东明县":"DNF","大拟":"DNZ","大平房":"DPD","大盘石":"RPP","大埔":"DPI","大堡":"DVT","大庆东":"LFX","大其拉哈":"DQX","道清":"DML","对青山":"DQB","德清西":"MOH","大庆西":"RHX","东升":"DRQ","砀山":"DKH","独山":"RWW","登沙河":"DWT","读书铺":"DPM","大石头":"DSL","东胜西":"DYC","大石寨":"RZT","东台":"DBH","定陶":"DQK","灯塔":"DGT","大田边":"DBM","东通化":"DTL","丹徒":"RUH","大屯":"DNT","东湾":"DRJ","大武口":"DFJ","低窝铺":"DWJ","大王滩":"DZZ","大湾子":"DFM","大兴沟":"DXL","大兴":"DXX","定西":"DSJ","甸心":"DXM","东乡":"DXG","代县":"DKV","定襄":"DXV","东戌":"RXP","东辛庄":"DXD","丹阳":"DYH","德阳":"DYW","大雁":"DYX","当阳":"DYN","丹阳北":"EXH","大英东":"IAW","东淤地":"DBV","大营":"DYV","定远":"EWH","岱岳":"RYV","大元":"DYZ","大营镇":"DJP","大营子":"DZD","大战场":"DTJ","德州东":"DIP","东至":"DCH","低庄":"DVQ","东镇":"DNV","道州":"DFZ","东庄":"DZV","兑镇":"DWV","豆庄":"ROP","定州":"DXP","大竹园":"DZY","大杖子":"DAP","豆张庄":"RZP","峨边":"EBW","二道沟门":"RDP","二道湾":"RDX","鄂尔多斯":"EEC","二龙":"RLD","二龙山屯":"ELA","峨眉":"EMW","二密河":"RML","二营":"RYJ","鄂州":"ECN","福安":"FAS","丰城":"FCG","丰城南":"FNG","肥东":"FIH","发耳":"FEM","富海":"FHX","福海":"FHR","凤凰城":"FHT","汾河":"FEV","奉化":"FHH","富锦":"FIB","范家屯":"FTT","福利区":"FLJ","福利屯":"FTB","丰乐镇":"FZB","阜南":"FNH","阜宁":"AKH","抚宁":"FNP","福清":"FQS","福泉":"VMW","丰水村":"FSJ","丰顺":"FUQ","繁峙":"FSV","抚顺":"FST","福山口":"FKP","扶绥":"FSZ","冯屯":"FTX","浮图峪":"FYP","富县东":"FDY","凤县":"FXY","富县":"FEY","费县":"FXK","凤阳":"FUH","汾阳":"FAV","扶余北":"FBT","分宜":"FYG","富源":"FYM","扶余":"FYT","富裕":"FYX","抚州北":"FBG","凤州":"FZY","丰镇":"FZC","范镇":"VZK","固安":"GFP","广安":"VJW","高碑店":"GBP","沟帮子":"GBD","甘草店":"GDJ","谷城":"GCN","藁城":"GEP","高村":"GCV","古城镇":"GZB","广德":"GRH","贵定":"GTW","贵定南":"IDW","古东":"GDV","贵港":"GGZ","官高":"GVP","葛根庙":"GGT","干沟":"GGL","甘谷":"GGJ","高各庄":"GGP","甘河":"GAX","根河":"GEX","郭家店":"GDT","孤家子":"GKT","古浪":"GLJ","皋兰":"GEJ","高楼房":"GFM","归流河":"GHT","关林":"GLF","甘洛":"VOW","郭磊庄":"GLP","高密":"GMK","公庙子":"GMC","工农湖":"GRT","广宁寺南":"GNT","广南卫":"GNM","高平":"GPF","甘泉北":"GEY","共青城":"GAG","甘旗卡":"GQD","甘泉":"GQY","高桥镇":"GZD","灌水":"GST","赶水":"GSW","孤山口":"GSP","果松":"GSL","高山子":"GSD","嘎什甸子":"GXD","高台":"GTJ","高滩":"GAY","古田":"GTS","官厅":"GTP","官厅西":"KEP","贵溪":"GXG","涡阳":"GYH","巩义":"GXF","高邑":"GIP","巩义南":"GYF","广元南":"GAW","固原":"GUJ","菇园":"GYL","公营子":"GYD","光泽":"GZS","古镇":"GNQ","固镇":"GEH","虢镇":"GZY","瓜州":"GZJ","高州":"GSQ","盖州":"GXT","官字井":"GOT","冠豸山":"GSS","盖州西":"GAT","淮安南":"AMH","红安":"HWN","海安县":"HIH","红安西":"VXN","黄柏":"HBL","海北":"HEB","鹤壁":"HAF","会昌北":"XEG","华城":"VCQ","河唇":"HCZ","汉川":"HCN","海城":"HCT","合川":"WKW","黑冲滩":"HCJ","黄村":"HCP","海城西":"HXT","化德":"HGC","洪洞":"HDV","霍尔果斯":"HFR","横峰":"HFG","韩府湾":"HXJ","汉沽":"HGP","黄瓜园":"HYM","红光镇":"IGW","浑河":"HHT","红花沟":"VHD","黄花筒":"HUD","贺家店":"HJJ","和静":"HJR","红江":"HFM","黑井":"HIM","获嘉":"HJF","河津":"HJV","涵江":"HJS","华家":"HJT","杭锦后旗":"HDC","河间西":"HXP","花家庄":"HJM","河口南":"HKJ","湖口":"HKG","黄口":"KOH","呼兰":"HUB","葫芦岛北":"HPD","浩良河":"HHB","哈拉海":"HIT","鹤立":"HOB","桦林":"HIB","黄陵":"ULY","海林":"HRB","虎林":"VLB","寒岭":"HAT","和龙":"HLL","海龙":"HIL","哈拉苏":"HAX","呼鲁斯太":"VTJ","火连寨":"HLT","黄梅":"VEH","韩麻营":"HYP","黄泥河":"HHL","海宁":"HNH","惠农":"HMJ","和平":"VAQ","花棚子":"HZM","花桥":"VQH","宏庆":"HEY","怀仁":"HRV","华容":"HRN","华山北":"HDY","黄松甸":"HDL","和什托洛盖":"VSR","红山":"VSB","汉寿":"VSQ","衡山":"HSQ","黑水":"HOT","惠山":"VCH","虎什哈":"HHP","红寺堡":"HSJ","虎石台":"HUT","海石湾":"HSO","衡山西":"HEQ","红砂岘":"VSJ","黑台":"HQB","桓台":"VTK","和田":"VTR","会同":"VTQ","海坨子":"HZT","黑旺":"HWK","海湾":"RWH","红星":"VXB","徽县":"HYY","红兴隆":"VHB","换新天":"VTB","红岘台":"HTJ","红彦":"VIX","合阳":"HAY","海阳":"HYK","衡阳东":"HVQ","华蓥":"HUW","汉阴":"HQY","黄羊滩":"HGJ","汉源":"WHW","河源":"VIQ","花园":"HUN","湟源":"HNO","黄羊镇":"HYJ","湖州":"VZH","化州":"HZZ","黄州":"VON","霍州":"HZV","惠州西":"VXQ","巨宝":"JRT","靖边":"JIY","金宝屯":"JBD","晋城北":"JEF","金昌":"JCJ","鄄城":"JCK","交城":"JNV","建昌":"JFD","峻德":"JDB","井店":"JFP","鸡东":"JOB","江都":"UDH","鸡冠山":"JST","金沟屯":"VGP","静海":"JHP","金河":"JHX","锦河":"JHB","精河":"JHR","精河南":"JIR","江华":"JHZ","建湖":"AJH","纪家沟":"VJD","晋江":"JJS","锦界":"JEY","姜家":"JJB","江津":"JJW","金坑":"JKT","芨岭":"JLJ","金马村":"JMM","江门东":"JWQ","角美":"JES","莒南":"JOK","井南":"JNP","建瓯":"JVS","经棚":"JPC","江桥":"JQX","九三":"SSX","金山北":"EGH","嘉善":"JSH","京山":"JCN","建始":"JRN","稷山":"JVV","吉舒":"JSL","建设":"JET","甲山":"JOP","建三江":"JIB","嘉善南":"EAH","金山屯":"JTB","江所田":"JOM","景泰":"JTJ","九台南":"JNL","吉文":"JWX","进贤":"JUG","莒县":"JKK","嘉祥":"JUK","介休":"JXV","嘉兴":"JXH","井陉":"JJP","嘉兴南":"EPH","夹心子":"JXT","姜堰":"UEH","揭阳":"JRQ","建阳":"JYS","简阳":"JYW","巨野":"JYK","江永":"JYZ","缙云":"JYH","靖远":"JYJ","江源":"SZL","济源":"JYF","靖远西":"JXJ","胶州北":"JZK","焦作东":"WEF","金寨":"JZH","靖州":"JEQ","荆州":"JBN","胶州":"JXK","晋州":"JXP","锦州南":"JOD","焦作":"JOF","旧庄窝":"JVP","金杖子":"JYD","开安":"KAT","库车":"KCR","康城":"KCP","库都尔":"KDX","宽甸":"KDT","克东":"KOB","昆都仑召":"KDC","开江":"KAW","康金井":"KJB","喀喇其":"KQX","开鲁":"KLC","克拉玛依":"KHR","口前":"KQL","昆山":"KSH","奎山":"KAB","克山":"KSB","开通":"KTT","康熙岭":"KXZ","昆阳":"KAM","克一河":"KHX","开原西":"KXT","康庄":"KZP","来宾":"UBZ","老边":"LLT","灵宝西":"LPF","龙川":"LUQ","乐昌":"LCQ","黎城":"UCP","聊城":"UCK","蓝村":"LCK","两当":"LDY","林东":"LRC","乐都":"LDO","梁底下":"LDP","六道河子":"LVP","鲁番":"LVM","廊坊":"LJP","落垡":"LOP","廊坊北":"LFP","老府":"UFD","兰岗":"LNB","龙骨甸":"LGM","芦沟":"LOM","龙沟":"LGJ","拉古":"LGB","临海":"UFH","林海":"LXX","拉哈":"LHX","凌海":"JID","柳河":"LNL","六合":"KLH","龙华":"LHP","滦河沿":"UNP","六合镇":"LEX","亮甲店":"LRT","刘家店":"UDT","刘家河":"LVT","连江":"LKS","庐江":"UJH","李家":"LJB","罗江":"LJW","廉江":"LJZ","两家":"UJT","龙江":"LJX","龙嘉":"UJL","莲江口":"LHB","蔺家楼":"ULK","李家坪":"LIJ","兰考":"LKF","林口":"LKB","路口铺":"LKQ","老莱":"LAX","拉林":"LAB","陆良":"LRM","龙里":"LLW","临澧":"LWQ","兰棱":"LLB","零陵":"UWZ","卢龙":"UAP","喇嘛甸":"LMX","里木店":"LMB","洛门":"LMJ","龙南":"UNG","梁平":"UQW","罗平":"LPM","落坡岭":"LPP","六盘山":"UPJ","乐平市":"LPG","临清":"UQK","龙泉寺":"UQJ","乐山北":"UTW","乐善村":"LUM","冷水江东":"UDQ","连山关":"LGT","流水沟":"USP","丽水":"USH","陵水":"LIQ","罗山":"LRN","鲁山":"LAF","梁山":"LMK","灵石":"LSV","露水河":"LUL","庐山":"LSG","林盛堡":"LBT","柳树屯":"LSD","龙山镇":"LAS","梨树镇":"LSB","李石寨":"LET","黎塘":"LTZ","轮台":"LAR","芦台":"LTP","龙塘坝":"LBM","濑湍":"LVZ","骆驼巷":"LTJ","李旺":"VLJ","莱芜东":"LWK","狼尾山":"LRJ","灵武":"LNJ","莱芜西":"UXK","朗乡":"LXB","陇县":"LXY","临湘":"LXQ","芦溪":"LUG","莱西":"LXK","林西":"LXC","滦县":"UXP","略阳":"LYY","莱阳":"LYK","辽阳":"LYT","临沂北":"UYK","凌源东":"LDD","连云港":"UIH","临颍":"LNF","老营":"LXL","龙游":"LMH","罗源":"LVS","林源":"LYX","涟源":"LAQ","涞源":"LYP","耒阳西":"LPQ","临泽":"LEJ","龙爪沟":"LZT","雷州":"UAQ","六枝":"LIW","鹿寨":"LIZ","来舟":"LZS","龙镇":"LZA","拉鲊":"LEM","兰州新区":"LQJ","马鞍山":"MAH","毛坝":"MBY","毛坝关":"MGY","麻城北":"MBN","渑池":"MCF","明城":"MCL","庙城":"MAP","渑池南":"MNF","茅草坪":"KPM","猛洞河":"MUQ","磨刀石":"MOB","弥渡":"MDF","帽儿山":"MRB","明港":"MGN","梅河口":"MHL","马皇":"MHZ","孟家岗":"MGB","美兰":"MHQ","汨罗东":"MQQ","马莲河":"MHB","茅岭":"MLZ","庙岭":"MLL","茂林":"MLD","穆棱":"MLB","马林":"MID","马龙":"MGM","木里图":"MUD","汨罗":"MLQ","玛纳斯湖":"MNR","冕宁":"UGW","沐滂":"MPQ","马桥河":"MQB","闽清":"MQS","民权":"MQF","明水河":"MUT","麻山":"MAB","眉山":"MSW","漫水湾":"MKW","茂舍祖":"MOM","米沙子":"MST","美溪":"MEB","勉县":"MVY","麻阳":"MVQ","密云北":"MUP","米易":"MMW","麦园":"MYS","墨玉":"MUR","庙庄":"MZJ","米脂":"MEY","明珠":"MFQ","宁安":"NAB","农安":"NAT","南博山":"NBK","南仇":"NCK","南城司":"NSP","宁村":"NCZ","宁德":"NES","南观村":"NGP","南宫东":"NFP","南关岭":"NLT","宁国":"NNH","宁海":"NHH","南华北":"NHS","南河川":"NHJ","泥河子":"NHD","宁家":"NVT","南靖":"NJS","牛家":"NJB","能家":"NJD","南口":"NKP","南口前":"NKT","南朗":"NNQ","乃林":"NLD","尼勒克":"NIR","那罗":"ULZ","宁陵县":"NLF","奈曼":"NMD","宁明":"NMZ","南木":"NMX","南平南":"NNS","那铺":"NPZ","南桥":"NQD","那曲":"NQO","暖泉":"NQJ","南台":"NTT","南头":"NOQ","宁武":"NWV","南湾子":"NWP","南翔北":"NEH","宁乡":"NXQ","内乡":"NXF","牛心台":"NXT","南峪":"NUP","娘子关":"NIP","南召":"NAF","南杂木":"NZT","蓬安":"PAW","平安":"PAL","平安驿":"PNO","磐安镇":"PAJ","平安镇":"PZT","蒲城东":"PEY","蒲城":"PCY","裴德":"PDB","偏店":"PRP","平顶山西":"BFF","坡底下":"PXJ","瓢儿屯":"PRT","平房":"PFB","平岗":"PGL","平关":"PGM","盘关":"PAM","平果":"PGZ","徘徊北":"PHP","平河口":"PHM","平湖":"PHQ","盘锦北":"PBD","潘家店":"PDP","皮口南":"PKT","普兰店":"PLT","偏岭":"PNT","平山":"PSB","彭山":"PSW","皮山":"PSR","磐石":"PSL","平社":"PSV","彭水":"PHW","平台":"PVT","平田":"PTM","莆田":"PTS","葡萄菁":"PTW","普湾":"PWT","平旺":"PWV","平型关":"PGV",
"普雄":"POW","郫县":"PWW","平洋":"PYX","彭阳":"PYJ","平遥":"PYV","平邑":"PIK","平原堡":"PPJ","平原":"PYK","平峪":"PYP","彭泽":"PZG","邳州":"PJH","平庄":"PZD","泡子":"POD","平庄南":"PND","乾安":"QOT","庆安":"QAB","迁安":"QQP","祁东北":"QRQ","七甸":"QDM","曲阜东":"QAK","庆丰":"QFT","奇峰塔":"QVP","曲阜":"QFK","琼海":"QYQ","秦皇岛":"QTP","千河":"QUY","清河":"QIP","清河门":"QHD","清华园":"QHP","全椒":"INH","渠旧":"QJZ","潜江":"QJN","秦家":"QJB","綦江":"QJW","祁家堡":"QBT","清涧县":"QNY","秦家庄":"QZV","七里河":"QLD","秦岭":"QLY","渠黎":"QLZ","青龙":"QIB","青龙山":"QGH","祁门":"QIH","前磨头":"QMP","青山":"QSB","确山":"QSN","前山":"QXQ","清水":"QUJ","戚墅堰":"QYH","青田":"QVH","桥头":"QAT","青铜峡":"QTJ","前卫":"QWD","前苇塘":"QWP","渠县":"QRW","祁县":"QXV","青县":"QXP","桥西":"QXJ","清徐":"QUV","旗下营":"QXC","千阳":"QOY","沁阳":"QYF","泉阳":"QYL","祁阳北":"QVQ","七营":"QYJ","庆阳山":"QSJ","清远":"QBQ","清原":"QYT","钦州东":"QDZ","钦州":"QRZ","青州市":"QZK","瑞安":"RAH","荣昌":"RCW","瑞昌":"RCG","如皋":"RBH","容桂":"RUQ","任丘":"RQP","乳山":"ROK","融水":"RSZ","热水":"RSD","容县":"RXZ","饶阳":"RVP","汝阳":"RYF","绕阳河":"RHD","汝州":"ROF","石坝":"OBJ","上板城":"SBP","施秉":"AQW","上板城南":"OBP","世博园":"ZWT","双城北":"SBB","舒城":"OCH","商城":"SWN","莎车":"SCR","顺昌":"SCS","神池":"SMV","沙城":"SCP","石城":"SCT","山城镇":"SCL","山丹":"SDJ","顺德":"ORQ","绥德":"ODY","水洞":"SIL","商都":"SXC","十渡":"SEP","四道湾":"OUD","顺德学院":"OJQ","绅坊":"OLH","双丰":"OFB","四方台":"STB","水富":"OTW","三关口":"OKJ","桑根达来":"OGC","韶关":"SNQ","上高镇":"SVK","上杭":"JBS","沙海":"SED","蜀河":"SHY","松河":"SBM","沙河":"SHP","沙河口":"SKT","赛汗塔拉":"SHC","沙河市":"VOP","沙后所":"SSD","山河屯":"SHL","三河县":"OXP","四合永":"OHD","三汇镇":"OZW","双河镇":"SEL","石河子":"SZR","三合庄":"SVP","三家店":"ODP","水家湖":"SQH","沈家河":"OJJ","松江河":"SJL","尚家":"SJB","孙家":"SUB","沈家":"OJB","双吉":"SML","松江":"SAH","三江口":"SKD","司家岭":"OLK","松江南":"IMH","石景山南":"SRP","邵家堂":"SJJ","三江县":"SOZ","三家寨":"SMM","十家子":"SJD","松江镇":"OZL","施家嘴":"SHM","深井子":"SWT","什里店":"OMP","疏勒":"SUR","疏勒河":"SHJ","舍力虎":"VLD","石磷":"SPB","石林":"SLM","双辽":"ZJD","绥棱":"SIB","石岭":"SOL","石林南":"LNM","石龙":"SLQ","萨拉齐":"SLC","索伦":"SNT","商洛":"OLY","沙岭子":"SLP","石门县北":"VFQ","三门峡南":"SCF","三门县":"OQH","石门县":"OMQ","三门峡西":"SXF","肃宁":"SYP","宋":"SOB","双牌":"SBZ","沙坪坝":"CYW","四平东":"PPT","遂平":"SON","沙坡头":"SFJ","沙桥":"SQM","商丘南":"SPF","水泉":"SID","石泉县":"SXY","石桥子":"SQT","石人城":"SRB","石人":"SRL","山市":"SQB","神树":"SWB","鄯善":"SSR","三水":"SJQ","泗水":"OSK","石山":"SAD","松树":"SFT","首山":"SAT","三十家":"SRD","三十里堡":"SST","松树镇":"SSL","松桃":"MZQ","索图罕":"SHX","三堂集":"SDH","石头":"OTB","神头":"SEV","沙沱":"SFM","上万":"SWP","孙吴":"SKB","沙湾县":"SXR","歙县":"OVH","遂溪":"SXZ","沙县":"SAS","绍兴":"SOH","石岘":"SXL","上西铺":"SXM","石峡子":"SXJ","沭阳":"FMH","绥阳":"SYB","寿阳":"SYV","水洋":"OYP","三阳川":"SYJ","上腰墩":"SPJ","三营":"OEJ","顺义":"SOP","三义井":"OYD","三源浦":"SYL","上虞":"BDH","三原":"SAY","上园":"SUD","水源":"OYJ","桑园子":"SAJ","绥中北":"SND","苏州北":"OHH","宿州东":"SRH","深圳东":"BJQ","深州":"OZP","孙镇":"OZY","绥中":"SZD","尚志":"SZB","师庄":"SNM","松滋":"SIN","师宗":"SEM","苏州园区":"KAH","苏州新区":"ITH","泰安":"TMK","台安":"TID","通安驿":"TAJ","桐柏":"TBF","通北":"TBB","桐城":"TTH","汤池":"TCX","郯城":"TZK","铁厂":"TCL","桃村":"TCK","通道":"TRQ","田东":"TDZ","天岗":"TGL","土贵乌拉":"TGC","通沟":"TOL","太谷":"TGV","塔哈":"THX","棠海":"THM","唐河":"THF","泰和":"THG","太湖":"TKH","团结":"TIX","谭家井":"TNJ","陶家屯":"TOT","唐家湾":"PDQ","统军庄":"TZP","吐列毛杜":"TMD","图里河":"TEX","铜陵":"TJH","田林":"TFZ","亭亮":"TIZ","铁力":"TLB","铁岭西":"PXT","图们北":"QSL","天门":"TMN","天门南":"TNN","太姥山":"TLS","土牧尔台":"TRC","土门子":"TCJ","洮南":"TVT","潼南":"TVW","太平川":"TIT","太平镇":"TEB","图强":"TQX","台前":"TTK","天桥岭":"TQL","土桥子":"TQJ","汤山城":"TCT","桃山":"TAB","塔石嘴":"TIM","通途":"TUT","汤旺河":"THB","同心":"TXJ","土溪":"TSW","桐乡":"TCH","田阳":"TRZ","天义":"TND","汤阴":"TYF","驼腰岭":"TIL","太阳山":"TYJ","汤原":"TYB","塔崖驿":"TYP","滕州东":"TEK","台州":"TZH","天祝":"TZJ","滕州":"TXK","天镇":"TZV","桐子林":"TEW","天柱山":"QWH","文安":"WBP","武安":"WAP","王安镇":"WVP","吴堡":"WUY","旺苍":"WEW","五叉沟":"WCT","文昌":"WEQ","温春":"WDB","五大连池":"WRB","文登":"WBK","五道沟":"WDL","五道河":"WHP","文地":"WNZ","卫东":"WVT","武当山":"WRN","望都":"WDP","乌尔旗汗":"WHX","潍坊":"WFK","万发屯":"WFB","王府":"WUT","瓦房店西":"WXT","王岗":"WGB","武功":"WGY","湾沟":"WGL","吴官田":"WGM","乌海":"WVC","苇河":"WHB","卫辉":"WHF","吴家川":"WCJ","五家":"WUB","威箐":"WAM","午汲":"WJP","渭津":"WJL","王家湾":"WJJ","倭肯":"WQB","五棵树":"WKT","五龙背":"WBT","乌兰哈达":"WLC","万乐":"WEB","瓦拉干":"WVX","温岭":"VHH","五莲":"WLK","乌拉特前旗":"WQC","乌拉山":"WSC","卧里屯":"WLX","渭南北":"WBY","乌奴耳":"WRX","万宁":"WNQ","万年":"WWG","渭南南":"WVY","渭南镇":"WNJ","沃皮":"WPT","吴桥":"WUP","汪清":"WQL","武清":"WWP","武山":"WSJ","文水":"WEV","魏善庄":"WSP","王瞳":"WTP","五台山":"WSV","王团庄":"WZJ","五五":"WVR","无锡东":"WGH","卫星":"WVB","闻喜":"WXV","武乡":"WVV","无锡新区":"IFH","武穴":"WXN","吴圩":"WYZ","王杨":"WYB","武义":"RYH","五营":"WWB","瓦窑田":"WIM","五原":"WYC","苇子沟":"WZL","韦庄":"WZY","五寨":"WZV","王兆屯":"WZB","微子镇":"WQP","魏杖子":"WKD","新安":"EAM","兴安":"XAZ","新安县":"XAF","新保安":"XAP","下板城":"EBP","西八里":"XLP","宣城":"ECH","兴城":"XCD","小村":"XEM","新绰源":"XRX","下城子":"XCB","新城子":"XCT","喜德":"EDW","小得江":"EJM","西大庙":"XMP","小董":"XEZ","小东":"XOD","信丰":"EFG","襄汾":"XFV","息烽":"XFW","新干":"EGG","孝感":"XGN","西固城":"XUJ","西固":"XIJ","夏官营":"XGJ","西岗子":"NBB","襄河":"XXB","新和":"XIR","宣和":"XWJ","斜河涧":"EEP","新华屯":"XAX","新华":"XHB","新化":"EHQ","宣化":"XHP","兴和西":"XEC","小河沿":"XYD","下花园":"XYP","小河镇":"EKY","徐家":"XJB","峡江":"EJG","新绛":"XJV","辛集":"ENP","新江":"XJM","西街口":"EKM","许家屯":"XJT","许家台":"XTJ","谢家镇":"XMT","兴凯":"EKB","小榄":"EAQ","香兰":"XNB","兴隆店":"XDD","新乐":"ELP","新林":"XPX","小岭":"XLB","新李":"XLJ","西林":"XYB","西柳":"GCT","仙林":"XPH","新立屯":"XLD","兴隆镇":"XZB","新立镇":"XGT","新民":"XMD","西麻山":"XMB","下马塘":"XAT","孝南":"XNV","咸宁北":"XRN","兴宁":"ENQ","咸宁":"XNN","犀浦东":"XAW","西平":"XPN","兴平":"XPY","新坪田":"XPM","霞浦":"XOS","溆浦":"EPQ","犀浦":"XIW","新青":"XQB","新邱":"XQD","兴泉堡":"XQJ","仙人桥":"XRL","小寺沟":"ESP","杏树":"XSB","浠水":"XZN","下社":"XSV","徐水":"XSP","夏石":"XIZ","小哨":"XAM","新松浦":"XOB","杏树屯":"XDT","许三湾":"XSJ","湘潭":"XTQ","邢台":"XTP","仙桃西":"XAN","下台子":"EIP","徐闻":"XJQ","新窝铺":"EPD","修武":"XWF","新县":"XSN","息县":"ENN","西乡":"XQY","湘乡":"XXQ","西峡":"XIF","孝西":"XOV","小新街":"XXM","新兴县":"XGQ","西小召":"XZC","小西庄":"XXP","向阳":"XDB","旬阳":"XUY","旬阳北":"XBY","襄阳东":"XWN","兴业":"SNZ","小雨谷":"XHM","信宜":"EEQ","小月旧":"XFM","小扬气":"XYX","襄垣":"EIF","夏邑县":"EJH","祥云西":"EXM","新友谊":"EYB","新阳镇":"XZJ","徐州东":"UUH","新帐房":"XZX","悬钟":"XRP","新肇":"XZT","忻州":"XXV","汐子":"XZD","西哲里木":"XRD","新杖子":"ERP","姚安":"YAC","依安":"YAX","永安":"YAS","永安乡":"YNB","亚布力":"YBB","元宝山":"YUD","羊草":"YAB","秧草地":"YKM","阳澄湖":"AIH","迎春":"YYB","叶城":"YER","盐池":"YKJ","砚川":"YYY","阳春":"YQQ","宜城":"YIN","应城":"YHN","禹城":"YCK","晏城":"YEK","阳城":"YNF","阳岔":"YAL","郓城":"YPK","雁翅":"YAP","云彩岭":"ACP","虞城县":"IXH","营城子":"YCT","英德":"YDQ","永登":"YDJ","尹地":"YDM","永定":"YGS","雁荡山":"YGH","于都":"YDG","园墩":"YAJ","英德西":"IIQ","永丰营":"YYM","杨岗":"YRB","阳高":"YOV","阳谷":"YIK","友好":"YOB","余杭":"EVH","沿河城":"YHP","岩会":"AEP","羊臼河":"YHM","永嘉":"URH","营街":"YAM","盐津":"AEW","余江":"YHG","燕郊":"AJP","姚家":"YAT","岳家井":"YGJ","一间堡":"YJT","英吉沙":"YIR","云居寺":"AFP","燕家庄":"AZK","永康":"RFH","营口东":"YGT","银浪":"YJX","永郎":"YLW","宜良北":"YSM","永乐店":"YDY","伊拉哈":"YLX","伊林":"YLB","杨陵":"YSY","彝良":"ALW","杨林":"YLM","余粮堡":"YLD","杨柳青":"YQP","月亮田":"YUM","义马":"YMF","阳明堡":"YVV","玉门":"YXJ","云梦":"YMN","元谋":"YMM","一面山":"YST","沂南":"YNK","宜耐":"YVM","伊宁东":"YNR","营盘水":"YZJ","羊堡":"ABM","阳泉北":"YPP","乐清":"UPH","焉耆":"YSR","源迁":"AQK","姚千户屯":"YQT","阳曲":"YQV","榆树沟":"YGP","月山":"YBF","玉石":"YSJ","玉舍":"AUM","偃师":"YSF","沂水":"YUK","榆社":"YSV","颍上":"YVH","窑上":"ASP","元氏":"YSP","杨树岭":"YAD","野三坡":"AIP","榆树屯":"YSX","榆树台":"YUT","鹰手营子":"YIP","源潭":"YTQ","牙屯堡":"YTZ","烟筒山":"YSL","烟筒屯":"YUX","羊尾哨":"YWM","越西":"YHW","攸县":"YOG","永修":"ACG","玉溪西":"YXM","弋阳":"YIG","余姚":"YYH","酉阳":"AFW","岳阳东":"YIQ","阳邑":"ARP","鸭园":"YYL","鸳鸯镇":"YYJ","燕子砭":"YZY","仪征":"UZH","宜州":"YSZ","兖州":"YZK","迤资":"YQM","羊者窝":"AEM","杨杖子":"YZD","镇安":"ZEY","治安":"ZAD","招柏":"ZBP","张百湾":"ZUP","中川机场":"ZJJ","枝城":"ZCN","子长":"ZHY","诸城":"ZQK","邹城":"ZIK","赵城":"ZCV","章党":"ZHT","正定":"ZDP","肇东":"ZDB","照福铺":"ZFM","章古台":"ZGD","赵光":"ZGB","中和":"ZHX","中华门":"VNH","枝江北":"ZIN","钟家村":"ZJY","朱家沟":"ZUB","紫荆关":"ZYP","周家":"ZOB","诸暨":"ZDH","镇江南":"ZEH","周家屯":"ZOD","褚家湾":"CWJ","湛江西":"ZWQ","朱家窑":"ZUJ","曾家坪子":"ZBW","张兰":"ZLV","镇赉":"ZLT","枣林":"ZIV","扎鲁特":"ZLD","扎赉诺尔西":"ZXX","樟木头":"ZOQ","中牟":"ZGF","中宁东":"ZDJ","中宁":"VNJ","中宁南":"ZNJ","镇平":"ZPF","漳平":"ZPS","泽普":"ZPR","枣强":"ZVP","张桥":"ZQY","章丘":"ZTK","朱日和":"ZRC","泽润里":"ZLM","中山北":"ZGQ","樟树东":"ZOG","珠斯花":"ZHD","中山":"ZSQ","柞水":"ZSY","钟山":"ZSZ","樟树":"ZSG","珠窝":"ZOP","张维屯":"ZWB","彰武":"ZWD","棕溪":"ZOY","钟祥":"ZTN","资溪":"ZXS","镇西":"ZVT","张辛":"ZIP","正镶白旗":"ZXC","紫阳":"ZVY","枣阳":"ZYN","竹园坝":"ZAW","张掖":"ZYJ","镇远":"ZUW","漳州东":"GOS","漳州":"ZUS","壮志":"ZUX","子洲":"ZZY","中寨":"ZZM","涿州":"ZXP","咋子":"ZAL","卓资山":"ZZC","株洲西":"ZAQ","郑州西":"XPF","阿巴嘎旗":"AQC","阿尔山北":"ARX","阿勒泰":"AUR","安仁":"ARG","安顺西":"ASE","安图西":"AXL","安阳东":"ADF","博白":"BBZ","八步":"BBE","栟茶":"FWH","保定东":"BMP","八方山":"FGQ","白沟":"FEP","滨海":"FHP","滨海北":"FCP","宝鸡南":"BBY","北井子":"BRT","白马井":"BFQ","宝清":"BUB","璧山":"FZW","白沙铺":"BSN","白水县":"BGY","板塘":"NGQ","本溪新城":"BVT","彬县":"BXY","宾阳":"UKZ","白洋淀":"FWP","百宜":"FHW","白音华南":"FNC","巴中东":"BDE","滨州":"BIK","霸州西":"FOP","澄城":"CUY","城固北":"CBY","查干湖":"VAT","巢湖东":"GUH","从江":"KNW","茶卡":"CVO","长临河":"FVH","茶陵南":"CNG","常平东":"FQQ","常平南":"FPQ","长庆桥":"CQJ","长寿北":"COW","长寿湖":"CSE","常山":"CSU","潮汕":"CBQ","长沙西":"RXQ","朝天":"CTE","长汀南":"CNS","长武":"CWY","长兴":"CBH","苍溪":"CXE","长阳":"CYN","潮阳":"CNQ","城子坦":"CWT","东安东":"DCZ","德保":"RBZ","都昌":"DCG","东岔":"DCJ","东城南":"IYQ","东戴河":"RDD","丹东西":"RWT","东二道河":"DRB","大丰":"KRQ","大方南":"DNE","东港北":"RGT","大孤山":"RMT","东莞":"RTQ","鼎湖东":"UWQ","鼎湖山":"NVQ","道滘":"RRQ","洞井":"FWQ","垫江":"DJE","大苴":"DIM","大荔":"DNY","大朗镇":"KOQ","大青沟":"DSD","德清":"DRH","东胜东":"RSC","砀山南":"PRH","大石头南":"DAL","当涂东":"OWH","大通西":"DTO","大旺":"WWQ","定西北":"DNJ","德兴东":"DDG","德兴":"DWG","丹霞山":"IRQ","大冶北":"DBN","都匀东":"KJW","东营南":"DOK","大余":"DYG","定州东":"DOP","端州":"WZQ","大足南":"FQW","峨眉山":"IXW","阿房宫":"EGY","鄂州东":"EFN","防城港北":"FBZ","凤城东":"FDT","富川":"FDZ","繁昌西":"PUH","丰都":"FUW","涪陵北":"FEW","枫林":"FLN","富宁":"FNM","佛坪":"FUY","法启":"FQE","芙蓉南":"KCQ","复盛":"FAW","抚松":"FSL","佛山西":"FOQ","福山镇":"FZQ","福田":"NZQ","富源北":"FBM","抚远":"FYB","抚州东":"FDG","抚州":"FZG","高安":"GCG","广安南":"VUW","贵安":"GAE","高碑店东":"GMP","恭城":"GCZ","藁城南":"GUP","贵定北":"FMW","葛店南":"GNN","贵定县":"KIW","广汉北":"GVW","高花":"HGD","革居":"GEM","关岭":"GLE","桂林西":"GEZ","光明城":"IMQ","广宁":"FBQ","广宁寺":"GQT","广南县":"GXM","桂平":"GAZ","弓棚子":"GPT","赶水东":"GDE","光山":"GUN","谷山":"FFQ","观沙岭":"FKQ","古田北":"GBS","广通北":"GPM","高台南":"GAJ","古田会址":"STS","贵阳北":"KQW","贵阳东":"KEW","高邑西":"GNP","惠安":"HNS","淮北北":"PLH","鹤壁东":"HFF","寒葱沟":"HKB","霍城":"SER","珲春":"HUL","邯郸东":"HPP","惠东":"KDQ","哈达铺":"HDJ","海东西":"HDO","洪洞西":"HTV","哈尔滨北":"HTB","合肥北城":"COH","合肥南":"ENH","黄冈":"KGN","黄冈东":"KAN","横沟桥东":"HNN","黄冈西":"KXN","洪河":"HPB","怀化南":"KAQ","黄河景区":"HCF","花湖":"KHN","惠环":"KHQ","后湖":"IHN","怀集":"FAQ","河口北":"HBM","黄流":"KLQ","黄陵南":"VLY","鲘门":"KMQ","虎门":"IUQ","侯马西":"HPV","衡南":"HNG","淮南东":"HOH","合浦":"HVZ","霍邱":"FBH","怀仁东":"HFV","华容东":"HPN","华容南":"KRN","黄石北":"KSN","黄山北":"NYH","衡水北":"IHP","贺胜桥东":"HLN","和硕":"VUR","花山南":"KNN","荷塘":"KXQ","黄土店":"HKP","合阳北":"HTY","海阳北":"HEK","槐荫":"IYN","鄠邑":"KXY","花园口":"HYT","霍州东":"HWV","惠州南":"KNQ","建安":"JUL","泾川":"JAJ","景德镇北":"JDG","旌德":"NSH","尖峰":"PFQ","近海":"JHD","蛟河西":"JOL","军粮城北":"JMP","将乐":"JLS","贾鲁河":"JLF","九郎山":"KJQ","即墨北":"JVK","剑门关":"JME","建宁县北":"JCS","江宁":"JJH","江宁西":"OKH","建瓯西":"JUS","酒泉南":"JNJ","句容西":"JWH","建水":"JSM","尖山":"JPQ","界首市":"JUN","绩溪北":"NRH","介休东":"JDV","泾县":"LOH","靖西":"JMZ","进贤南":"JXG","江油北":"JBE","嘉峪关南":"JBJ","简阳南":"JOW","金银潭":"JTN","靖宇":"JYL","金月湾":"PYQ","缙云西":"PYH","晋中":"JZV","景州":"JEP","开封北":"KBF","开福寺":"FLQ","开化":"KHU","凯里南":"QKW","库伦":"KLD","昆明南":"KOM","葵潭":"KTQ","开阳":"KVW","隆安东":"IDZ","来宾北":"UCZ","灵璧":"GMH","寮步":"LTQ","绿博园":"LCF","隆昌北":"NWW","乐昌东":"ILQ","临城":"UUP","罗城":"VCZ","陵城":"LGK","老城镇":"ACQ","龙洞堡":"FVW","乐都南":"LVO","娄底南":"UOQ","乐东":"UQQ","离堆公园":"INW","陆丰":"LLQ","龙丰":"KFQ","禄丰南":"LQM","临汾西":"LXV","临高南":"KGQ","麓谷":"BNQ","滦河":"UDP","珞璜南":"LNE","漯河西":"LBN","罗江东":"IKW","柳江":"UQZ","利津南":"LNK","兰考南":"LUF","龙口市":"UKK","兰陵北":"COK","龙里北":"KFW","沥林北":"KBQ","醴陵东":"UKQ","陇南":"INJ","梁平南":"LPE","礼泉":"LGY","灵石东":"UDV","乐山":"IVW","龙市":"LAG","溧水":"LDH","娄山关南":"LSE","洛湾三江":"KRW","莱西北":"LBK","溧阳":"LEH","临邑":"LUK","柳园南":"LNR","鹿寨北":"LSZ","阆中":"LZE","临泽南":"LDJ","马鞍山东":"OMH","毛陈":"MHN","明港东":"MDN","民和南":"MNO","闵集":"MJN","马兰":"MLR","民乐":"MBJ","弥勒":"MLM","玛纳斯":"MSR","牟平":"MBK","闽清北":"MBS","民权北":"MIF","眉山东":"IUW","庙山":"MSN","岷县":"MXJ","门源":"MYO","暮云":"KIQ","蒙自北":"MBM","孟庄":"MZF","蒙自":"MZM","南部":"NBE","南曹":"NEF","南充北":"NCE","南城":"NDG","南昌西":"NXG","宁东南":"NDJ","宁东":"NOJ","南芬北":"NUT","南丰":"NFG","南湖东":"NDN","内江北":"NKW","南江":"FIW","南江口":"NDQ","南陵":"LLH","尼木":"NMO","南宁东":"NFZ","南宁西":"NXZ","南平北":"NBS","宁强南":"NOY","南雄":"NCQ","纳雍":"NYE","南阳寨":"NYF","普安":"PAN","普安县":"PUE","屏边":"PBM","平坝南":"PBE","平昌":"PCE","普定":"PGW","平度":"PAK","皮口":"PUT","盘龙城":"PNN","蓬莱市":"POK","普宁":"PEQ","平南南":"PAZ","彭山北":"PPW","盘山":"PUD","坪上":"PSK","萍乡北":"PBG","鄱阳":"PYG","濮阳":"PYF","平遥古城":"PDV","平原东":"PUK","普者黑":"PZM","盘州":"PAE","彭州":"PMW","秦安":"QGJ","青白江东":"QFW","青川":"QCE","青岛北":"QHK","祁东":"QMQ","青堆":"QET","前锋":"QFB","曲靖北":"QBM","綦江东":"QDE","曲江":"QIM","青莲":"QEW","齐齐哈尔南":"QNB","清水北":"QEJ","青神":"QVW","岐山":"QAY","庆盛":"QSQ","清水县":"QIJ","曲水县":"QSO","祁县东":"QGV","乾县":"QBY","旗下营南":"QNC","祁阳":"QWQ","全州南":"QNZ","棋子湾":"QZQ","仁布":"RUO","荣昌北":"RQW","荣成":"RCK","瑞昌西":"RXG","如东":"RIH","榕江":"RVW","日喀则":"RKO","饶平":"RVQ","宋城路":"SFF","三道湖":"SDL","邵东":"FIQ","三都县":"KKW","胜芳":"SUP","双峰北":"NFQ","商河":"SOK","泗洪":"GQH","四会":"AHQ","石家庄东":"SXP","三江南":"SWZ","三井子":"OJT","双流机场":"IPW","石林西":"SYM","沙岭子西":"IXP","双流西":"IQW","三明北":"SHS","嵩明":"SVM","树木岭":"FMQ","神木":"HMY","苏尼特左旗":"ONC","山坡东":"SBN","石桥":"SQE","沈丘":"SQN","鄯善北":"SMR","狮山北":"NSQ","三水北":"ARQ","松山湖北":"KUQ","狮山":"KSQ","三水南":"RNQ","韶山南":"INQ","三穗":"QHW","石梯":"STE","汕尾":"OGQ","歙县北":"NPH","绍兴北":"SLH","绍兴东":"SSH","泗县":"GPH","始兴":"IPQ","泗阳":"MPH","双阳":"OYT","邵阳北":"OVQ","松原北":"OCT","山阴":"SNV","深圳北":"IOQ","神州":"SRQ","深圳坪山":"IFQ","石嘴山":"QQJ","石柱县":"OSW","台安南":"TAD","桃村北":"TOK","田东北":"TBZ","土地堂东":"TTN","太谷西":"TIV","吐哈":"THR","通海":"TAM","太和北":"JYN","天河机场":"TJN","天河街":"TEN","通化县":"TXL","同江":"TJB","铜陵北":"KXH","吐鲁番北":"TAR","泰宁":"TNS","铜仁南":"TNW","天水南":"TIJ","通渭":"TWJ","田心东":"KQQ","汤逊湖":"THN","藤县":"TAZ","太原南":"TNV","通远堡西":"TST","桐梓北":"TBE","桐梓东":"TDE","通州":"TOP","文登东":"WGK","五府山":"WFG","威虎岭北":"WBL","威海北":"WHK","乌兰察布":"WPC","五龙背东":"WMT","乌龙泉南":"WFN","乌鲁木齐":"WAR","五女山":"WET","武胜":"WSE","五通":"WTZ","无为":"IIH","瓦屋山":"WAH","闻喜西":"WOV","武义北":"WDH","武夷山北":"WBS","武夷山东":"WCS","婺源":"WYG","渭源":"WEJ","万州北":"WZE","武陟":"WIF","梧州南":"WBZ","兴安北":"XDZ","许昌东":"XVF","项城":"ERN","新都东":"EWW","西丰":"XFT","先锋":"NQQ","湘府路":"FVQ","襄汾西":"XTV","孝感北":"XJN","孝感东":"GDN","西湖东":"WDQ","新化南":"EJQ","新晃西":"EWQ","新津":"IRW","小金口":"NKQ","辛集南":"IJP","新津南":"ITW","咸宁东":"XKN","咸宁南":"UNN","溆浦南":"EMQ","西平西":"EGQ","湘潭北":"EDQ","邢台东":"EDP","西乌旗":"XWC","修武西":"EXF","修文县":"XWE","萧县北":"QSH","新乡东":"EGF","新余北":"XBG","西阳村":"XQF","信阳东":"OYN","咸阳秦都":"XOY","仙游":"XWS","新郑机场":"EZF","香樟路":"FNQ","迎宾路":"YFW","永城北":"RGH","运城北":"ABV","永川东":"WMW","禹城东":"YSK","宜春":"YEG","岳池":"AWW","云东海":"NAQ","姚渡":"AOJ","云浮东":"IXQ","永福南":"YBZ","雨格":"VTM","洋河":"GTH","永济北":"AJV","弋江":"RVH","于家堡":"YKP","延吉西":"YXL","永康南":"QUH","运粮河":"YEF","炎陵":"YAG","杨陵南":"YEY","伊敏":"YMX","郁南":"YKQ","银瓶":"KPQ","永寿":"ASY","阳朔":"YCZ","云山":"KZQ","玉山南":"YGG","永泰":"YTS","银滩":"CTQ","鹰潭北":"YKG","烟台南":"YLK","伊通":"YTL","烟台西":"YTK","尤溪":"YXS","云霄":"YBS","宜兴":"YUH","玉溪":"AXM","阳信":"YVK","应县":"YZV","攸县南":"YXG","洋县西":"YXY","余姚北":"CTH","榆中":"IZJ","诏安":"ZDS","正定机场":"ZHP","纸坊东":"ZMN","准格尔":"ZEC","庄河北":"ZUT","昭化":"ZHW","织金北":"ZJE","张家川":"ZIJ","芷江":"ZPQ","织金":"IZW","仲恺":"KKQ","曾口":"ZKE","左岭":"ZSN","樟木头东":"ZRQ","驻马店西":"ZLN","漳浦":"ZCS","肇庆东":"FCQ","庄桥":"ZQH","昭山":"KWQ","钟山西":"ZAZ","漳县":"ZXJ","资阳北":"FYW","遵义":"ZYE","遵义南":"ZNE","张掖西":"ZEJ","资中北":"WZW","涿州东":"ZAP","枣庄东":"ZNK","卓资东":"ZDC","郑州东":"ZAF","株洲南":"KVQ"}

class Ui_MainWindow(QWidget):
    step = 0;
    start = ""
    start = ""
    student = ""
    date = ""
    isdo = ""
    yzm = ""
    thiscode = ""
    to = ""
    chooseno = ""
    continueFlag = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1275, 670)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(1110, 20, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.A)
        # self.pushButton.keyPressEvent = self.keyPressEvent


        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(810, 20, 280, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(5, 11, 800, 591))
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser.setObjectName("textBrowser")

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(810, 310, 450, 300))
        self.label.setText("")
        self.label.setObjectName("label")

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralWidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.calendarWidget.clicked.connect(self.B)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1275, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.textEdit.setFocus()
        MainWindow.setTabOrder(self.textEdit,self.pushButton)
        MainWindow.setTabOrder(self.pushButton,self.textBrowser)
        MainWindow.setTabOrder(self.textBrowser,self.textEdit)

        if self.step == 0:
            self.addMessage("请输入起始站:")
            self.step = 1
        # _translate = QtCore.QCoreApplication.translate

        # self.label.setText(_translate("Dialog", EditText))
    # def keyPressEvent(self, e):  
      
    #     if e.key() == Qt.Key_Escape:  
    #         self.close() 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
    def B(self,Dialog):
        date = self.calendarWidget.selectedDate()
        datestr=date.toString("yyyy-MM-dd")
        self.textEdit.setText(datestr)
    def A(self,Dialog):
        text = self.textEdit.toPlainText()
        if len(text) == 0 and (self.step != -1 or self.continueFlag == 1):
            self.addMessage("请输入内容")
        else:
            if self.step == 0:
                self.addMessage("请输入起始站:") 
            elif self.step == 1:
                self.start1 = text
                self.start=areatocode.get(text,"")
                if self.start == "":
                    self.addMessage("输入站名不正确，请重新输入")
                else :
                    self.addMessage(text+":"+self.start) 
                    self.addMessage("请输入到站:") 
                    self.step = 2
            elif self.step == 2:
                self.to1 = text
                self.to=areatocode.get(text,"")
                if self.to == "":
                    self.addMessage("输入站名不正确，请重新输入")
                else :
                    self.addMessage(text+":"+self.to) 
                    self.addMessage("是学生吗？是：1，不是：0") 
                    self.step = 3
            elif self.step == 3:
                self.isstudent=text
                self.addMessage(self.isstudent) 
                if(self.isstudent=="0"):
                    self.student="ADULT"
                else:
                    self.student="0X00"
                self.addMessage("请输入要查询的乘车开始日期的年月，如2017-03-05：") 
                self.calendarWidget.setGeometry(QtCore.QRect(810, 70, 296, 236))
                self.step = 4
            elif self.step == 4:
                self.date=text
                self.addMessage(self.date) 
                # self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 0, 0))
                self.calendarWidget.setVisible(False)
                url="https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date="+self.date+"&\
leftTicketDTO.from_station="+self.start+"&leftTicketDTO.to_station="+self.to+"&purpose_codes="+self.student
                context = ssl._create_unverified_context()
                data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
                patrst01='"result":\[(.*?)\]'
                rst01=re.compile(patrst01).findall(data)[0]
                allcheci=rst01.split(",")
                checimap_pat='"map":({.*?})'
                checimap=eval(re.compile(checimap_pat).findall(data)[0])
                self.addMessage("车次\t出发站名\t到达站名\t出发时间\t到达时间\t一等座\t二等座\t硬座\t无座")
                for i in range(0,len(allcheci)):
                    try:
                        thischeci=allcheci[i].split("|")
                        #[3]---code
                        code=thischeci[3]
                        #[6]---fromname
                        fromname=thischeci[6]
                        fromname=checimap[fromname]
                        #[7]---toname
                        toname=thischeci[7]
                        toname=checimap[toname]
                        #[8]---stime
                        stime=thischeci[8]
                        #[9]---atime
                        atime=thischeci[9]
                        #[28]---yz
                        yz=thischeci[31]
                        #[29]---wz
                        wz=thischeci[30]
                        #[30]---ze
                        ze=thischeci[29]
                        #[31]---zy
                        zy=thischeci[26]
                        self.addMessage(code+"\t"+fromname+"\t"+toname+"\t"+stime+"\t"+atime+"\t"
                            +str(zy)+"\t"+str(ze)+"\t\
                              "+str(yz)+"\t"+str(wz))
                    except Exception as err:
                        pass
                self.addMessage("查票完成，请输入1继续…")
                self.step = 5
            elif self.step == 5:
                self.isdo=text
                self.addMessage(self.isdo) 
                if(self.isdo==1 or self.isdo=="1"):
                    pass
                else:
                    raise self.addMessage("输入不是1，结束执行")
                self.addMessage("Cookie处理中…") 
                #建立cookie处理
                cjar=http.cookiejar.CookieJar()
                opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
                urllib.request.install_opener(opener)
                #以下进入自动登录部分
                loginurl="https://kyfw.12306.cn/otn/login/init#"
                req0 = urllib.request.Request(loginurl)
                req0.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lik\
                e Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req0data=urllib.request.urlopen(req0).read().decode("utf-8","ignore")

                yzmurl="https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand"
                # while True:
                urllib.request.urlretrieve(yzmurl,"./12306_yzm.jpg")
                self.image = QtGui.QImage()
                self.image.load("12306_yzm.jpg")

                self.label.setPixmap(QtGui.QPixmap.fromImage(self.image).scaled(450,300))
                self.addMessage("请输入验证码，输入第几张图片即可")
                # if(yzm!="re"):
                        # break
                self.step = 6
            elif self.step == 6:
                self.yzm=text
                allpic = self.yzm.split(",")
                def getxy(pic):
                    if(pic==1):
                        xy=(35,45)
                    if(pic==2):
                        xy=(112,45)
                    if(pic==3):
                        xy=(173,45)
                    if(pic==4):
                        xy=(253,45)        
                    if(pic==5):
                        xy=(35,114)
                    if(pic==6):
                        xy=(112,114)
                    if(pic==7):
                        xy=(173,114)
                    if(pic==8):
                        xy=(253,114)
                    return xy
                print(allpic)
                allpicpos=""
                for i in allpic:
                    thisxy=getxy(int(i))
                    for j in thisxy:
                        allpicpos=allpicpos+str(j)+","
                print(allpicpos)
                allpicpos2=re.compile("(.*?).$").findall(allpicpos)[0]
                print(allpicpos2)
                #post验证码验证
                yzmposturl="https://kyfw.12306.cn/passport/captcha/captcha-check"
                yzmpostdata =urllib.parse.urlencode({
                "answer":allpicpos2,
                "rand":"sjrand",
                "login_site":"E",
                }).encode('utf-8')
                req1 = urllib.request.Request(yzmposturl,yzmpostdata)
                req1.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lik\
                e Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req1data=urllib.request.urlopen(req1).read().decode("utf-8","ignore")
                #post账号密码验证
                loginposturl="https://kyfw.12306.cn/passport/web/login"
                loginpostdata =urllib.parse.urlencode({
                "username":myuser,
                "password":mypasswd,
                "appid":"otn",
                }).encode('utf-8')
                req2 = urllib.request.Request(loginposturl,loginpostdata)
                req2.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lik\
                e Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req2data=urllib.request.urlopen(req2).read().decode("utf-8","ignore")
                #其他验证
                loginposturl2="https://kyfw.12306.cn/otn/login/userLogin"
                loginpostdata2 =urllib.parse.urlencode({
                "_json_att":"",
                }).encode('utf-8')
                req2_2 = urllib.request.Request(loginposturl2,loginpostdata2)
                req2_2.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lik\
                e Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req2data_2=urllib.request.urlopen(req2_2).read().decode("utf-8","ignore")

                loginposturl3="https://kyfw.12306.cn/passport/web/auth/uamtk"
                loginpostdata3 =urllib.parse.urlencode({
                "appid":"otn",
                }).encode('utf-8')
                req2_3 = urllib.request.Request(loginposturl3,loginpostdata3)
                req2_3.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lik\
                e Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req2data_3=urllib.request.urlopen(req2_3).read().decode("utf-8","ignore")
                pat_req2='"newapptk":"(.*?)"'
                tk=re.compile(pat_req2,re.S).findall(req2data_3)[0]

                loginposturl4="https://kyfw.12306.cn/otn/uamauthclient"
                loginpostdata4 =urllib.parse.urlencode({
                "tk":tk,
                }).encode('utf-8')
                req2_4 = urllib.request.Request(loginposturl4,loginpostdata4)
                req2_4.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lik\
                e Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req2data_4=urllib.request.urlopen(req2_4).read().decode("utf-8","ignore")
                #爬个人中心页面
                centerurl="https://kyfw.12306.cn/otn/index/initMy12306"
                req3 = urllib.request.Request(centerurl)
                req3.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lik\
                e Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req3data=urllib.request.urlopen(req3).read().decode("utf-8","ignore")
                self.addMessage("登陆完成")
                self.addMessage("如果需要订票，请输入1继续，否则请输入其他数据")
                self.step = 7
            elif self.step == 7:
                self.isdo=text
                if(self.isdo==1 or self.isdo=="1"):
                    pass
                else:
                    raise self.addMessage("输入不是1，结束执行")
                self.addMessage("请输入要预定的车次：")
                self.step = 8
            elif self.step == 8:
                if self.continueFlag != 1:
                    self.thiscode=text
                    self.addMessage(text)
                    self.chooseno = ""
                #订票
                #先初始化一下订票界面
                initurl="https://kyfw.12306.cn/otn/leftTicket/init"
                reqinit=urllib.request.Request(initurl)
                reqinit.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3\
        6 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                initdata=urllib.request.urlopen(reqinit).read().decode("utf-8","ignore")
                #再爬对应订票信息
                bookurl="https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date="+self.date+"&leftTi\
        cketDTO.from_station="+self.start+"&leftTicketDTO.to_station="+self.to+"&purpose_codes="+self.student
                req4 = urllib.request.Request(bookurl)
                req4.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHT\
        ML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req4data=urllib.request.urlopen(req4).read().decode("utf-8","ignore")
                #存储车次与secretStr信息
                patrst01='"result":\[(.*?)\]'
                rst01=re.compile(patrst01).findall(req4data)[0]
                allcheci=rst01.split(",")
                checimap_pat='"map":({.*?})'
                checimap=eval(re.compile(checimap_pat).findall(req4data)[0])
                code=[]
                secretStr=[]
                zy=[]
                for i in range(0,len(allcheci)):
                    try:
                        thischeci=allcheci[i].split("|")
                        #print(thischeci)
                        #[3]---code
                        thiscode1=thischeci[3]
                        code.append(thiscode1)
                        #[0]---secretStr
                        secretStr.append(thischeci[0].replace('"',""))
                        #[31]-zy
                        thiszy=thischeci[31]
                        zy.append(thiszy)
                    except Exception as err:
                        pass
                #用字典trainzy存储车次有没有票的信息
                self.trainzy={}
                for i in range(0,len(code)):
                    self.trainzy[code[i]]=zy[i]
                #用字典traindata存储车次secretStr信息，以供后续订票操作
                #存储的格式是：traindata={"车次1":secretStr1,"车次2":secretStr2,…}
                traindata={}
                for i in range(0,len(code)):
                    traindata[code[i]]=secretStr[i]
                #订票-第1次post-主要进行确认用户状态
                checkurl="https://kyfw.12306.cn/otn/login/checkUser"
                checkdata =urllib.parse.urlencode({
                "_json_att":""
                }).encode('utf-8')
                req5 = urllib.request.Request(checkurl,checkdata)
                req5.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3\
        6 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req5data=urllib.request.urlopen(req5).read().decode("utf-8","ignore")
                #自动得到当前时间并转为年-月-格式，因为后面请求数据需要用到当前时间作为返程时间backdate
                backdate=datetime.datetime.now()
                backdate=backdate.strftime("%Y-%m-%d")
                #订票-第2次post-主要进行“预订”提交
                submiturl="https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest"
                submitdata =urllib.parse.urlencode({
                "secretStr":traindata[self.thiscode],
                "train_date":self.date,
                "back_train_date":backdate,
                "tour_flag":"dc",
                "purpose_codes":self.student,
                "query_from_station_name":self.start1,
                "query_to_station_name":self.to1,
                })
                submitdata2=submitdata.replace("%25","%")
                submitdata3=submitdata2.encode('utf-8')
                req6 = urllib.request.Request(submiturl,submitdata3)
                req6.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3\
        6 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req6data=urllib.request.urlopen(req6).read().decode("utf-8","ignore")
                #订票-第3次post-主要获取Token、leftTicketStr、key_check_isChange、train_location
                initdcurl="https://kyfw.12306.cn/otn/confirmPassenger/initDc"
                initdcdata =urllib.parse.urlencode({
                "_json_att":""
                }).encode('utf-8')
                req7 = urllib.request.Request(initdcurl,initdcdata)
                req7.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3\
        6 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req7data=urllib.request.urlopen(req7).read().decode("utf-8","ignore")
                #获取train_no、leftTicketStr、fromStationTelecode、toStationTelecode、train_location
                train_no_pat="'train_no':'(.*?)'"
                leftTicketStr_pat="'leftTicketStr':'(.*?)'"
                fromStationTelecode_pat="from_station_telecode':'(.*?)'"
                toStationTelecode_pat="'to_station_telecode':'(.*?)'"
                train_location_pat="'train_location':'(.*?)'"
                pattoken="var globalRepeatSubmitToken.*?'(.*?)'"
                patkey="'key_check_isChange':'(.*?)'"
                print(req7data)
                train_no_all=re.compile(train_no_pat).findall(req7data)
                if(len(train_no_all)!=0):
                    self.train_no=train_no_all[0]
                else:
                    raise Exception("train_no获取失败")
                leftTicketStr_all=re.compile(leftTicketStr_pat).findall(req7data)
                if(len(leftTicketStr_all)!=0):
                    self.leftTicketStr=leftTicketStr_all[0]
                else:
                    raise Exception("leftTicketStr获取失败")
                fromStationTelecode_all=re.compile(fromStationTelecode_pat).findall(req7data)
                if(len(fromStationTelecode_all)!=0):
                    self.fromStationTelecode=fromStationTelecode_all[0]
                else:
                    raise Exception("fromStationTelecod获取失败")
                toStationTelecode_all=re.compile(toStationTelecode_pat).findall(req7data)
                if(len(toStationTelecode_all)!=0):
                    self.toStationTelecode=toStationTelecode_all[0]
                else:
                    raise Exception("toStationTelecode获取失败")
                train_location_all=re.compile(train_location_pat).findall(req7data)
                if(len(train_location_all)!=0):
                    self.train_location=train_location_all[0]
                else:
                    raise Exception("train_location获取失败")
                tokenall=re.compile(pattoken).findall(req7data)
                if(len(tokenall)!=0):
                    self.token=tokenall[0]
                else:
                    raise Exception("Token获取失败")
                keyall=re.compile(patkey).findall(req7data)
                if(len(keyall)!=0):
                    self.key=keyall[0]
                else:
                    raise Exception("key_check_isChange获取失败")
                #还需要获取train_location
                pattrain_location="'tour_flag':'dc','train_location':'(.*?)'"
                train_locationall=re.compile(pattrain_location).findall(req7data)
                if(len(train_locationall)!=0):
                    self.train_location=train_locationall[0]
                else:
                    raise Exception("train_location获取失败")
                #自动post网址4-获取乘客信息
                getuserurl="https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs"
                getuserdata =urllib.parse.urlencode({
                "REPEAT_SUBMIT_TOKEN":self.token,
                }).encode('utf-8')
                req8 = urllib.request.Request(getuserurl,getuserdata)
                req8.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3\
        6 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req8data=urllib.request.urlopen(req8).read().decode("utf-8","ignore")
                #获取用户信息
                #提取姓名
                namepat='"passenger_name":"(.*?)"'
                #提取身份证
                idpat='"passenger_id_no":"(.*?)"'
                #提取手机号
                mobilepat='"mobile_no":"(.*?)"'
                #提取对应乘客所在的国家
                countrypat='"country_code":"(.*?)"'
                self.nameall=re.compile(namepat).findall(req8data)
                self.idall=re.compile(idpat).findall(req8data)
                self.mobileall=re.compile(mobilepat).findall(req8data)
                countryall=re.compile(countrypat).findall(req8data)
                #选择乘客
                #输出乘客信息，由于可能有多位乘客，所以通过循环输出
                if self.chooseno == "":
                    for i in range(0,len(self.nameall)):
                        self.addMessage("第"+str(i+1)+"位用户,姓名:"+str(self.nameall[i]))
                    self.addMessage("请选择要订票的用户的序号，此处只能选择一位哦，如需选择多位，可以自行修改一下代码")
                self.step = 9
                if self.continueFlag == 1:
                    self.A(Dialog)
            elif self.step == 9:
                if self.continueFlag != 1:
                    self.chooseno=text
                    self.thisno=int(self.chooseno)-1
                if(self.trainzy[self.thiscode]=="无"):
                    self.addMessage("当前无票，继续监控…")
                    self.step = 8
                    self.continueFlag = 1
                    self.A(Dialog)
                #总请求1-点击提交后步骤1-确认订单(在此只定二等座，座位类型为1，如需选择多种类型座位，可
                #以自行修改一下代码使用if判断一下即可)
                checkOrderurl="https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo"
                checkdata=urllib.parse.urlencode({
                "cancel_flag":2,
                "bed_level_order_num":"000000000000000000000000000000",
                "passengerTicketStr":"M,0,1,"+str(self.nameall[self.thisno])+",1,"+str(self.idall[self.thisno])+",\
        "+str(self.mobileall[self.thisno])+",N",
                "oldPassengerStr":str(self.nameall[self.thisno])+",1,"+str(self.idall[self.thisno])+",1_",
                "tour_flag":"dc",
                "randCode":"",
                "whatsSelect":1,
                "_json_att":"",
                "REPEAT_SUBMIT_TOKEN":self.token,
                }).encode('utf-8')
                req9 = urllib.request.Request(checkOrderurl,checkdata)
                req9.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KH\
        TML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req9data=urllib.request.urlopen(req9).read().decode("utf-8","ignore")
                self.addMessage("确认订单完成，即将进行下一步")
                #总请求2-点击提交后步骤2-获取队列
                getqueurl="https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount"
                #checkdata=checkOrderdata.encode('utf-8')
                #将日期转为格林时间
                #先将字符串转为常规时间格式
                thisdatestr=self.date#需要的买票时间
                thisdate=datetime.datetime.strptime(thisdatestr,"%Y-%m-%d").date()
                #再转为对应的格林时间
                gmt='%a+%b+%d+%Y'
                thisgmtdate=thisdate.strftime(gmt)
                #将leftstr2转成指定格式
                leftstr2=self.leftTicketStr.replace("%","%25")
                getquedata="train_date="+str(thisgmtdate)+"+00%3A00%3A00+GMT%2B0800&train_no="+self.train_no+"&sta\
        tionTrainCode="+self.thiscode+"&seatType=M&fromStationTelecode="+self.fromStationTelecode+"&toStationTelecod\
        e="+self.toStationTelecode+"&leftTicket="+leftstr2+"&purpose_codes=00&train_location="+self.train_location+"&_j\
        son_att=&REPEAT_SUBMIT_TOKEN="+str(self.token)
                getdata=getquedata.encode('utf-8')
                req10 = urllib.request.Request(getqueurl,getdata)
                req10.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTM\
        L, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req10data=urllib.request.urlopen(req10).read().decode("utf-8","ignore")
                self.addMessage("获取订单队列完成，即将进行下一步")
                #总请求3-确认步骤1-配置确认提交
                confurl="https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue"
                confdata2=urllib.parse.urlencode({
                "passengerTicketStr":"M,0,1,"+str(self.nameall[self.thisno])+",1,"+str(self.idall[self.thisno])+",\
        "+str(self.mobileall[self.thisno])+",N",
                "oldPassengerStr":str(self.nameall[self.thisno])+",1,"+str(self.idall[self.thisno])+",1_",
                "randCode":"",
                "purpose_codes":"00",
                "key_check_isChange":self.key,
                "leftTicketStr":self.leftTicketStr,
                "train_location":self.train_location,
                "choose_seats":"",
                "seatDetailType":"000",
                "whatsSelect":"1",
                "roomType":"00",
                "dwAll":"N",
                "_json_att":"",
                "REPEAT_SUBMIT_TOKEN":self.token,
                }).encode('utf-8')
                req11 = urllib.request.Request(confurl,confdata2)
                req11.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3\
        6 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req11data=urllib.request.urlopen(req11).read().decode("utf-8","ignore")
                self.addMessage("配置确认提交完成，即将进行下一步")
                time1=time.time()
                while True:
                    #总请求4-确认步骤2-获取orderid
                    time2=time.time()
                    if((time2-time1)//60>5):
                        self.addMessage("获取orderid超时，正在进行新一次抢购")
                        break
                    getorderidurl="https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime?random="+str(int(time.time()*1000))+"&tourFlag=dc&_json_att=&REPEAT_SUBMIT_TOKEN="+str(self.token)
                    req12 = urllib.request.Request(getorderidurl)
                    req12.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                    req12data=urllib.request.urlopen(req12).read().decode("utf-8","ignore")
                    patorderid='"orderId":"(.*?)"'
                    orderidall=re.compile(patorderid).findall(req12data)
                    if(len(orderidall)==0):
                        self.addMessage("未获取到orderid，正在进行新一次的请求。")
                        continue
                    else:
                        orderid=orderidall[0]
                        break
                self.addMessage("获取orderid完成，即将进行下一步")
                #总请求5-确认步骤3-请求结果
                resulturl="https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue"
                resultdata="orderSequence_no="+orderid+"&_json_att=&REPEAT_SUBMIT_TOKEN="+str(self.token)
                resultdata2=resultdata.encode('utf-8')
                req13 = urllib.request.Request(resulturl,resultdata2)
                req13.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                req13data=urllib.request.urlopen(req13).read().decode("utf-8","ignore")
                self.addMessage("请求结果完成，即将进行下一步")
                try:
                    #总请求6-确认步骤4-支付接口页面
                    payurl="https://kyfw.12306.cn/otn//payOrder/init"
                    paydata="_json_att=&REPEAT_SUBMIT_TOKEN="+str(self.token)
                    paydata2=paydata.encode('utf-8')
                    req14 = urllib.request.Request(payurl,paydata2)
                    req14.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
                    req14data=urllib.request.urlopen(req14).read().decode("utf-8","ignore")
                    self.addMessage("订单已经完成提交，您可以登录后台进行支付了。")
                except Exception as err:
                    self.addMessage(err)
                self.step = 10
        self.textEdit.setText("")
        self.textEdit.setFocus()
        # self.textBrowser.verticalScrollBar().setFocus()
        if self.textBrowser.verticalScrollBar().maximum() > 0:
            # self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
            # time.sleep(1)
            self.textBrowser.verticalScrollBar().setSliderPosition(self.textBrowser.verticalScrollBar().maximum())
        # self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
        # self.addMessage(str(self.textBrowser.verticalScrollBar().value()))
        # self.addMessage(str(self.textBrowser.verticalScrollBar().maximum()))
        # text = self.textEdit.toPlainText()
            # print(text)
            # self.textEdit.setText("")
            # history = self.label.text()
            # self.label.setText(history + "\n" + text)
        # self.image = QtGui.QImage()
        # self.image.load("12306_yzm.jpg")

        # self.label.setPixmap(QtGui.QPixmap.fromImage(self.image).scaled(450,300))
        #读取图片文件
    def addMessage(self,text):
        history = self.textBrowser.toPlainText()
        self.textBrowser.setText(history + "\n" + text)
        
    def imreadex(filename):
        return cv2.imdecode(np.fromfile(filename, dtype=np.uint8), cv2.IMREAD_COLOR)
    # def imageOpenCv2ToQImage (self, cv_img):
    #     height, width, bytesPerComponent = cv_img.shape
    #     bytesPerLine = bytesPerComponent * width;
    #     cv2.cvtColor(cv_img, cv2.CV_BGR2RGB, cv_img)
    #     return QtGui.QImage(cv_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
if __name__=='__main__':

    app=QtWidgets.QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
   