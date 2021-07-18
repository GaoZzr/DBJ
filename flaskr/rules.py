#coding=UTF-8
ruleDatas = {
###中间件
'Shiro':'(deleteMe)',
'Weblogic':'Hypertext Transfer Protocol -- HTTP/1.1',
'Jboss':'jboss.css ',
'Tomcat-默认页面':'(/manager/html|/manager/status)',
'ThinkPHP':'1165838194',
'Spring框架':'116323821',

###协同办公OA
'Tongda-通达OA':'(tongda.ico|onmouseover="this.focus()")',
'Seeyon-致远OA':'(/seeyon/USER-DATA/IMAGES/LOGIN/login.gif|/seeyon/common|SY8045|Seeyon-Server/1.0)',
'Ecology-泛微OA':'(/wui/theme|/js/ecology8/lang/weaver_lang_7_wev8.js|WVS)',
'e-Bridge-泛微云桥':'(/main/login/images/loginlogo.png|e-Bridge)',
'E-Mobile':'(weaver,e-mobile|E-Mobile&nbsp;)',
'Landray-蓝凌OA':'(kmss_onsubmit|sys/ui/extend/theme/default/style/icon.css)',
'用友NC':'(uclient.yonyou.com)',
'Zentao-禅道':'(zentaosid|/zentao/js|/zentao/theme/|/theme/default/images/main/zt-logo.png)',
'协众OA':'(CNOAOASESSID|Powered by 协众OA)',
'金蝶EAS':'(easSessionId)',
'金蝶政务GSiS':'(/kdgs/script/kdgs.js)',
'金和OA':'(金和协同管理平台)',

###内容管理CMS
'Typecho-博客':'(Typecho</a>)',
'微三云管理系统':'(WSY_logo|管理系统 MANAGEMENT SYSTEM)',
'WordPress':'wp-content',
'ThinkCMF':'(ThinkCMF|{Simple content manage Framework)',

###开发框架 接口文档
'ThinkPHP-3.x':'(Simple OOP PHP Framework)',
'ThinkPHP':'(ThinkPHP</a>|十年磨一剑-为API开发设计的高性能框架)|<h1>页面错误！请稍后再试～</h1>',
'Spring-Boot开发平台':'(<title>Spring Boot开发平台</title>)',
'Swagger UI':'(/swagger-ui.css|swagger-ui-bundle.js)',

###邮件服务器
'Exchange':'(/owa/auth.owa)',
'CoreMail':'(coremail/common)',

###网站管理 集群、监控、仓库、队列 
'Gitlab':'(assets/gitlab_logo|GitLab</title>)',
'宝塔-BT':'(app.bt.cn/static/app.png|安全入口校验失败)',
'phpMyAdmin':'(phpmyadmin.css|img/logo_right.png)',
'Zabbix':'(zbx_sessionid|images/general/zabbix.ico|Zabbix SIA)',
'Nagios':'(Nagios Access)',
'Nexus':'(Nexus Repository Manager|NX-ANTI-CSRF-TOKEN)',
'Harbor':'(harbor-lang|<title>Harbor</title>)',
'Jira':'(jira.webresources)',
'Jenkins':'(M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z)',
'RabbitMQ':'(<title>RabbitMQ Management</title>)',
'360主机卫士':'(zhuji.360.cn)',
'360网站卫士':'(360wzb)',
'360站长平台':'(360-site-verification)',


###网络设备
'Ruijie-锐捷':'(4008 111 000)',
'Inspur-浪潮服务器IPMI管理口':'(img/inspur_logo.png)',
'Huawei SMC':'(Script/SmcScript.js?version=)',
'网康下一代防火墙':'(网康下一代防火墙</title>|北京网康科技有限公司)',
'Sangfor-深信服VPN':'(login_psw.csp|loginPageSP/loginPrivacy.js)',
'Sangfor-深信服上网行为管理':'(utccjfaewjb)',
'Sangfor-深信服应用交付报表系统':'(report/js/prng4.js|/reportCenter/index.php?cls_mode=cluster_mode_others)',
'Sangfor-深信服WAF':'(commonFunction.js)',
'Sangfor-深信服防火墙':'(SANGFOR FW)',
'华为安全设备':'(sweb-lib/resource/)',
'华为_HUAWEI_SRG2220':'(HUAWEI SRG2220)',
'华为 NetOpen':'(/netopen/theme/css/inFrame.css)',
'华为 MCU':'(McuR5-min.js)',
'华为_HUAWEI_ASG2050':'(HUAWEI ASG2050)',
'华为_HUAWEI_SRG3250':'(HUAWEI SRG3250)',
'华为_HUAWEI_ASG2100':'(HUAWEI ASG2100)',
'华为_HUAWEI_SRG1220':'(HUAWEI SRG1220)',
'H3C公司产品':'(service@h3c.com)',
'H3C Router':'(/wnm/ssl/web/frame/login.html)',
'H3C-AM8000':'(AM8000)',
'H3C ICG 1000':'(ICG 1000系统管理)',
'H3C ER3200':'(ER3200系统管理)',
'H3C ER5100':'(ER5100系统管理)',
'H3C ER8300':'(ER8300系统管理)',
'H3C ER2100V2':'(ER2100V2系统管理)',
'H3C ER3108GW':'(ER3108GW系统管理)',
'H3C ER3260G2':'(ER3260G2系统管理)',
'H3C ICG1000':'(ICG1000系统管理)',
'H3C ER5200':'(ER5200系统管理)',
'H3C ER3100':'(ER3100系统管理)',
'H3C-SecBlade-FireWall':'(js/MulPlatAPI.js)',
'H3C ER6300G2':'(ER6300G2系统管理)',
'H3C ER3260':'(ER3260系统管理)',
'H3C ER3108G':'(ER3108G系统管理)',
'H3C ER5200G2':'(ER5200G2系统管理)',
'H3C ER6300':'(ER6300系统管理)',
'H3C ER2100':'(ER2100系统管理)',
'H3C ER2100n':'(ER2100n系统管理)',
'H3C ER8300G2':'(ER8300G2系统管理)',
'CISCO_EPC3925':'(Docsis_system)',
'CISCO ASR':'(CISCO ASR)',
'CISCO VPN':'(/+CSCOE+/logon.html)',
'CISCO-CX20':'(CISCO-CX20)',
'网御 VPN':'(vpn/common/js/leadsec.js|/vpn/user/common/custom/auth_home.css)',
'绿盟下一代防火墙':'(NSFOCUS NF)',
'启明星辰天清汉马USG防火墙':'(/cgi-bin/webui?op=get_product_model)',
'万户ezOFFICE':'(LocLan)',
'万户网络':'(css/css_whir.css)',
'TP-LINK Wireless WDR3600':'(TP-LINK Wireless WDR3600)',
'TP-Link 3600 DD-WRT':'(TP-Link 3600 DD-WRT)',
'Citrix-Metaframe':'(window.location=\\"/Citrix/MetaFrame)',
'Citrix-Web-PN-Server':'(Citrix Web PN Server)',
'Citrix-Access-Gateway':'(Citrix Access Gateway)',
'Citrix-XenServer':'(Citrix Systems|Inc. XenServer)',
'Juniper_vpn':'(welcome.cgi\\?p=logo|/images/logo_juniper_reversed.gif)',


###大数据相关
'Spark_Master':'(Spark Master at)',
'Spark_Worker':'(Spark Worker at)',

###其它
'xxl-job':'(分布式任务调度平台XXL-JOB)',
}