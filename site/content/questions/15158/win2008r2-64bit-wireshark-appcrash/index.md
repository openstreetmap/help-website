+++
type = "question"
title = "Win2008R2 64bit WireShark APPCRASH"
description = '''I cannot get any version of WireShark v1.8.3 (32bit or 64bit) to run on a Win2008R2. The error below occurs when the WireShark is starting, how can I get it to work??? I also tried to go back a version and still it wouldn&#x27;t work... Problem signature:  Problem Event Name: APPCRASH  Application Name: ...'''
date = "2012-10-22T07:16:00Z"
lastmod = "2012-10-22T09:03:00Z"
weight = 15158
keywords = [ "appcrash" ]
aliases = [ "/questions/15158" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Win2008R2 64bit WireShark APPCRASH](/questions/15158/win2008r2-64bit-wireshark-appcrash)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15158-score" class="post-score" title="current number of votes">0</div><span id="post-15158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I cannot get any version of WireShark v1.8.3 (32bit or 64bit) to run on a Win2008R2. The error below occurs when the WireShark is starting, how can I get it to work??? I also tried to go back a version and still it wouldn't work...</p><p>Problem signature: Problem Event Name: APPCRASH Application Name: wireshark.exe Application Version: 1.8.3.45256 Application Timestamp: 506b148f Fault Module Name: StackHash_3184 Fault Module Version: 6.1.7601.17725 Fault Module Timestamp: 4ec4aa8e Exception Code: c0000374 Exception Offset: 00000000000c40f2 OS Version: 6.1.7601.2.1.0.272.7 Locale ID: 1033 Additional Information 1: 3184 Additional Information 2: 31843cf121481c946ab29ceb8ed6d936 Additional Information 3: 9983 Additional Information 4: 9983a7843ed160e25bc3c9f876f45c8f<br />
<br />
</p><p>Log Name: Application<br />
Source: Application Error<br />
Date: 10/22/2012 9:19:24 AM<br />
Event ID: 1000<br />
Task Category: (100)<br />
Level: Error<br />
Keywords: Classic<br />
User: N/A<br />
Computer:<br />
Description:<br />
Faulting application name: wireshark.exe, version: 1.8.3.45256, time stamp: 0x506b148f<br />
Faulting module name: ntdll.dll, version: 6.1.7601.17725, time stamp: 0x4ec4aa8e<br />
Exception code: 0xc0000374<br />
Fault offset: 0x00000000000c40f2<br />
Faulting process id: 0x39fc<br />
Faulting application start time: 0x01cdb0603bbba52c<br />
Faulting application path: C:\Program Files\Wireshark\wireshark.exe<br />
Faulting module path: C:\Windows\SYSTEM32\ntdll.dll<br />
Report Id: 7a0e6f0d-1c53-11e2-a35f-6431504ae268<br />
Event Xml: &lt;event xmlns="http://schemas.microsoft.com/win/2004/08/events/event"&gt; &lt;system&gt; &lt;provider name="Application Error"/&gt; &lt;eventid qualifiers="0"&gt;1000&lt;/eventid&gt; &lt;level&gt;2&lt;/level&gt; &lt;task&gt;100&lt;/task&gt; &lt;keywords&gt;0x80000000000000&lt;/keywords&gt; &lt;timecreated systemtime="2012-10-22T14:19:24.000000000Z"/&gt; &lt;eventrecordid&gt;16734&lt;/eventrecordid&gt; &lt;channel&gt;Application&lt;/channel&gt; &lt;computer&gt;&lt;/computer&gt; &lt;security/&gt; &lt;/system&gt; &lt;eventdata&gt; &lt;data&gt;wireshark.exe&lt;/data&gt; &lt;data&gt;1.8.3.45256&lt;/data&gt; &lt;data&gt;506b148f&lt;/data&gt; &lt;data&gt;ntdll.dll&lt;/data&gt; &lt;data&gt;6.1.7601.17725&lt;/data&gt; &lt;data&gt;4ec4aa8e&lt;/data&gt; &lt;data&gt;c0000374&lt;/data&gt; &lt;data&gt;00000000000c40f2&lt;/data&gt; &lt;data&gt;39fc&lt;/data&gt; &lt;data&gt;01cdb0603bbba52c&lt;/data&gt; &lt;data&gt;C:\Program Files\Wireshark\wireshark.exe&lt;/data&gt; &lt;data&gt;C:\Windows\SYSTEM32\ntdll.dll&lt;/data&gt; &lt;data&gt;7a0e6f0d-1c53-11e2-a35f-6431504ae268&lt;/data&gt; &lt;/eventdata&gt; &lt;/event&gt;</p><p>Version=1<br />
EventType=APPCRASH<br />
EventTime=129953891640935850<br />
ReportType=2<br />
Consent=1<br />
ReportIdentifier=7a0e6f0e-1c53-11e2-a35f-6431504ae268<br />
IntegratorReportIdentifier=7a0e6f0d-1c53-11e2-a35f-6431504ae268<br />
Response.type=4<br />
Sig[0].Name=Application Name<br />
Sig[0].Value=wireshark.exe<br />
Sig[1].Name=Application Version<br />
Sig[1].Value=1.8.3.45256<br />
Sig[2].Name=Application Timestamp<br />
Sig[2].Value=506b148f<br />
Sig[3].Name=Fault Module Name<br />
Sig[3].Value=StackHash_3184<br />
Sig[4].Name=Fault Module Version<br />
Sig[4].Value=6.1.7601.17725<br />
Sig[5].Name=Fault Module Timestamp<br />
Sig[5].Value=4ec4aa8e<br />
Sig[6].Name=Exception Code<br />
Sig[6].Value=c0000374<br />
Sig[7].Name=Exception Offset<br />
Sig[7].Value=00000000000c40f2<br />
DynamicSig[1].Name=OS Version<br />
DynamicSig[1].Value=6.1.7601.2.1.0.272.7<br />
DynamicSig[2].Name=Locale ID<br />
DynamicSig[2].Value=1033<br />
DynamicSig[22].Name=Additional Information 1<br />
DynamicSig[22].Value=3184<br />
DynamicSig[23].Name=Additional Information 2<br />
DynamicSig[23].Value=31843cf121481c946ab29ceb8ed6d936<br />
DynamicSig[24].Name=Additional Information 3<br />
DynamicSig[24].Value=9983<br />
DynamicSig[25].Name=Additional Information 4<br />
DynamicSig[25].Value=9983a7843ed160e25bc3c9f876f45c8f<br />
UI[2]=C:\Program Files\Wireshark\wireshark.exe<br />
UI[3]=Wireshark has stopped working<br />
UI[4]=Windows can check online for a solution to the problem.<br />
UI[5]=Check online for a solution and close the program<br />
UI[6]=Check online for a solution later and close the program<br />
UI[7]=Close the program<br />
LoadedModule[0]=C:\Program Files\Wireshark\wireshark.exe<br />
LoadedModule[1]=C:\Windows\SYSTEM32\ntdll.dll<br />
LoadedModule[2]=C:\Windows\system32\kernel32.dll<br />
LoadedModule[3]=C:\Windows\system32\KERNELBASE.dll<br />
LoadedModule[4]=C:\Program Files\Wireshark\wiretap-1.8.0.dll<br />
LoadedModule[5]=C:\Program Files\Wireshark\libglib-2.0-0.dll<br />
LoadedModule[6]=C:\Windows\system32\ADVAPI32.dll<br />
LoadedModule[7]=C:\Windows\system32\msvcrt.dll<br />
LoadedModule[8]=C:\Windows\SYSTEM32\sechost.dll<br />
LoadedModule[9]=C:\Windows\system32\RPCRT4.dll<br />
LoadedModule[10]=C:\Program Files\Wireshark\libintl-8.dll<br />
LoadedModule[11]=C:\Windows\system32\ole32.dll<br />
LoadedModule[12]=C:\Windows\system32\GDI32.dll<br />
LoadedModule[13]=C:\Windows\system32\USER32.dll<br />
LoadedModule[14]=C:\Windows\system32\LPK.dll<br />
LoadedModule[15]=C:\Windows\system32\USP10.dll<br />
LoadedModule[16]=C:\Windows\system32\SHELL32.dll<br />
LoadedModule[17]=C:\Windows\system32\SHLWAPI.dll<br />
LoadedModule[18]=C:\Windows\system32\WINMM.dll<br />
LoadedModule[19]=C:\Windows\system32\WS2_32.dll<br />
LoadedModule[20]=C:\Windows\system32\NSI.dll<br />
LoadedModule[21]=C:\Program Files\Wireshark\libwsutil.dll<br />
LoadedModule[22]=C:\Program Files\Wireshark\libgmodule-2.0-0.dll<br />
LoadedModule[23]=C:\Windows\system32\MSVCR100.dll<br />
LoadedModule[24]=C:\Program Files\Wireshark\zlib1.dll<br />
LoadedModule[25]=C:\Program Files\Wireshark\libwireshark.dll<br />
LoadedModule[26]=C:\Program Files\Wireshark\libcares-2.dll<br />
LoadedModule[27]=C:\Program Files\Wireshark\libgcrypt-11.dll<br />
LoadedModule[28]=C:\Program Files\Wireshark\libgpg-error-0.dll<br />
LoadedModule[29]=C:\Program Files\Wireshark\libgnutls-26.dll<br />
LoadedModule[30]=C:\Program Files\Wireshark\libtasn1-3.dll<br />
LoadedModule[31]=C:\Program Files\Wireshark\libsmi-2.dll<br />
LoadedModule[32]=C:\Program Files\Wireshark\libGeoIP-1.dll<br />
LoadedModule[33]=C:\Program Files\Wireshark\lua5.1.dll<br />
LoadedModule[34]=C:\Windows\system32\COMDLG32.dll<br />
LoadedModule[35]=C:\Windows\WinSxS\amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.7601.17514_none_fa396087175ac9ac\COMCTL32.dll<br />
LoadedModule[36]=C:\Program Files\Wireshark\libgtk-win32-2.0-0.dll<br />
LoadedModule[37]=C:\Program Files\Wireshark\libgdk-win32-2.0-0.dll<br />
LoadedModule[38]=C:\Program Files\Wireshark\libcairo-2.dll<br />
LoadedModule[39]=C:\Program Files\Wireshark\libfontconfig-1.dll<br />
LoadedModule[40]=C:\Program Files\Wireshark\libfreetype-6.dll<br />
LoadedModule[41]=C:\Program Files\Wireshark\libxml2-2.dll<br />
LoadedModule[42]=C:\Windows\system32\MSIMG32.dll<br />
LoadedModule[43]=C:\Program Files\Wireshark\libpixman-1-0.dll<br />
LoadedModule[44]=C:\Program Files\Wireshark\libpng15-15.dll<br />
LoadedModule[45]=C:\Program Files\Wireshark\libgdk_pixbuf-2.0-0.dll<br />
LoadedModule[46]=C:\Program Files\Wireshark\libgio-2.0-0.dll<br />
LoadedModule[47]=C:\Program Files\Wireshark\libgobject-2.0-0.dll<br />
LoadedModule[48]=C:\Program Files\Wireshark\libffi-5.dll<br />
LoadedModule[49]=C:\Windows\system32\DNSAPI.dll<br />
LoadedModule[50]=C:\Program Files\Wireshark\libjasper-1.dll<br />
LoadedModule[51]=C:\Program Files\Wireshark\libjpeg-8.dll<br />
LoadedModule[52]=C:\Program Files\Wireshark\libtiff-5.dll<br />
LoadedModule[53]=C:\Program Files\Wireshark\liblzma-5.dll<br />
LoadedModule[54]=C:\Windows\system32\IMM32.dll<br />
LoadedModule[55]=C:\Windows\system32\MSCTF.dll<br />
LoadedModule[56]=C:\Program Files\Wireshark\libpango-1.0-0.dll<br />
LoadedModule[57]=C:\Program Files\Wireshark\libpangocairo-1.0-0.dll<br />
LoadedModule[58]=C:\Program Files\Wireshark\libpangoft2-1.0-0.dll<br />
LoadedModule[59]=C:\Program Files\Wireshark\libpangowin32-1.0-0.dll<br />
LoadedModule[60]=C:\Program Files\Wireshark\libatk-1.0-0.dll<br />
LoadedModule[61]=C:\Windows\system32\WINSPOOL.DRV<br />
LoadedModule[62]=C:\Windows\system32\riched20.dll<br />
LoadedModule[63]=C:\Windows\system32\wpcap.dll<br />
LoadedModule[64]=C:\Windows\system32\packet.dll<br />
LoadedModule[65]=C:\Windows\system32\VERSION.dll<br />
LoadedModule[66]=C:\Windows\system32\iphlpapi.dll<br />
LoadedModule[67]=C:\Windows\system32\WINNSI.DLL<br />
LoadedModule[68]=C:\Windows\system32\CRYPTBASE.dll<br />
LoadedModule[69]=C:\Windows\system32\SspiCli.dll<br />
LoadedModule[70]=C:\Program Files\Wireshark\lib\gtk-2.0\2.10.0\engines\libwimp.dll<br />
LoadedModule[71]=C:\Windows\system32\uxtheme.dll<br />
LoadedModule[72]=C:\Windows\system32\CRYPTSP.dll<br />
LoadedModule[73]=C:\Windows\system32\NETAPI32.DLL<br />
LoadedModule[74]=C:\Windows\system32\netutils.dll<br />
LoadedModule[75]=C:\Windows\system32\srvcli.dll<br />
LoadedModule[76]=C:\Windows\system32\wkscli.dll<br />
LoadedModule[77]=C:\Program Files\Wireshark\plugins\1.8.3\asn1.dll<br />
LoadedModule[78]=C:\Program Files\Wireshark\plugins\1.8.3\docsis.dll<br />
LoadedModule[79]=C:\Program Files\Wireshark\plugins\1.8.3\ethercat.dll<br />
LoadedModule[80]=C:\Program Files\Wireshark\plugins\1.8.3\gryphon.dll<br />
LoadedModule[81]=C:\Program Files\Wireshark\plugins\1.8.3\irda.dll<br />
LoadedModule[82]=C:\Program Files\Wireshark\plugins\1.8.3\m2m.dll<br />
LoadedModule[83]=C:\Program Files\Wireshark\plugins\1.8.3\mate.dll<br />
LoadedModule[84]=C:\Program Files\Wireshark\plugins\1.8.3\opcua.dll<br />
LoadedModule[85]=C:\Program Files\Wireshark\plugins\1.8.3\profinet.dll<br />
LoadedModule[86]=C:\Program Files\Wireshark\plugins\1.8.3\stats_tree.dll<br />
LoadedModule[87]=C:\Program Files\Wireshark\plugins\1.8.3\unistim.dll<br />
LoadedModule[88]=C:\Program Files\Wireshark\plugins\1.8.3\wimax.dll<br />
LoadedModule[89]=C:\Program Files\Wireshark\plugins\1.8.3\wimaxasncp.dll<br />
LoadedModule[90]=C:\Windows\system32\dhcpcsvc.DLL<br />
LoadedModule[91]=C:\Windows\system32\dhcpcsvc6.DLL<br />
FriendlyEventName=Stopped working<br />
ConsentKey=APPCRASH<br />
AppName=Wireshark<br />
AppPath=C:\Program Files\Wireshark\wireshark.exe<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-appcrash" rel="tag" title="see questions tagged &#39;appcrash&#39;">appcrash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '12, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/a0ffe6c7ba65bf64b5dec8a8b12affdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mgh1472&#39;s gravatar image" /><p><span>mgh1472</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mgh1472 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Oct '12, 07:40</strong> </span></p></div></div><div id="comments-container-15158" class="comments-container"></div><div id="comment-tools-15158" class="comment-tools"></div><div class="clear"></div><div id="comment-15158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15165"></span>

<div id="answer-container-15165" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15165-score" class="post-score" title="current number of votes">0</div><span id="post-15165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, you should not just post tons of debug lines here. This is a Q&amp;A Site, and not the bug tracker (where this would indeed help in some cases). So you should probably open a bug there: <a href="http://bugs.wireshark.org"></a><a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a></p><p>If the problem you have is actually not just happening at the start of Wireshark but after capturing for a while you might just have encountered the good old out-of-memory trouble, see <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">http://wiki.wireshark.org/KnownBugs/OutOfMemory</a>. In that case you do not need to open a bug report.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '12, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></br></p></div></div><div id="comments-container-15165" class="comments-container"><span id="15169"></span><div id="comment-15169" class="comment"><div id="post-15169-score" class="comment-score"></div><div class="comment-text"><p>Alrighty then...</p></div><div id="comment-15169-info" class="comment-info"><span class="comment-age">(22 Oct '12, 09:03)</span> <span class="comment-user userinfo">mgh1472</span></div></div></div><div id="comment-tools-15165" class="comment-tools"></div><div class="clear"></div><div id="comment-15165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

