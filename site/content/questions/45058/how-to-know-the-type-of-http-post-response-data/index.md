+++
type = "question"
title = "how to know the type of HTTP-Post response data?"
description = '''I&#x27;m new to WireShark and want to know if there is a way to get out the type of received data as I&#x27;m getting a pretty weird data response:  ...`.......H.V.....H.V.............X(.............(D..........d.DeviceClass:VTO DeviceType:VTO6210B ...................................X............................'''
date = "2015-08-13T07:17:00Z"
lastmod = "2015-08-13T07:34:00Z"
weight = 45058
keywords = [ "http.response", "response" ]
aliases = [ "/questions/45058" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to know the type of HTTP-Post response data?](/questions/45058/how-to-know-the-type-of-http-post-response-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45058-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to WireShark and want to know if there is a way to get out the type of received data as I'm getting a pretty weird data response:</p><blockquote><p>...`.......H.V.....H.V.............X(.............(D..........d.DeviceClass:VTO DeviceType:VTO6210B</p><p>...................................X...............................................................X................................U...........................TransactionID:1 Method:GetParameterValues ParameterName:Dahua.Device.Decode.Cfg</p><p>...................................Xn...........................TransactionID:1 Method:GetParameterValuesResponse ParameterName:Dahua.Device.Decode.Cfg FaultCode:Error</p><p>...X............................FTP:1:Record,Snap&amp;&amp;SMTP:1:AlarmText,AlarmSnap&amp;&amp;NTP:2:AdjustSysTime&amp;&amp;VideoCover:1:MutiCover&amp;&amp;AutoRegister:1:Login&amp;&amp;AutoMaintain:1:Reboot,DeleteFiles,ShutDown&amp;&amp;UPNP:1:SearchDevice&amp;&amp;DHCP:1:RequestIP&amp;&amp;STORE POSITION:1:FTP&amp;&amp;DefaultQuery:1:DQuery&amp;&amp;ImportantRecID:1:RECID&amp;&amp;ACFControl:1:ACF&amp;&amp;DavinciModule:1:WorkSheetCFGApart,StandardGOP&amp;&amp;Dahua.Gps:1:Locate&amp;&amp;Dahua.a4.9:1:Login&amp;&amp;Dahua.Device.Record.General:1:General&amp;&amp;Log:1:PageForPageLog&amp;&amp;QueryURL:1:CONFIG....Y...........................TransactionID:2 Method:GetParameterValues ParameterName:Dahua.Device.Record.General</p><p>...X............................TransactionID:2 Method:GetParameterValuesResponse ParameterName:Dahua.Device.Record.General FaultCode:OK IsGeneralRecord:1 IsAlarmRecord:1 IsMoveDetectRecord:1 IsLocalStore:1 IsRemoteStore:1 IsRedunancyStore:0 IsLocalurgentStore:1</p><p>...................................................................................X................................a...+.......a.........(D....{ "id" : 1067, "method" : "accessControl.listMethod", "params" : null, "session" : 1143535103 } ....X....+.................(D....{ "params" : { "method" : [ "accessControl.factory.instance", "accessControl.destroy", "accessControl.openDoor", "accessControl.listMethod" ] }, "result" : true, "session" : 1143535103 } ....Z...+.......Z.........(D....{ "id" : 1323, "method" : "system.listMethod", "params" : null, "session" : 1143535103 } ....X....+.................(D....{ "id" : 1323, "params" : { "method" : [ "system.listMethod", "VideoTalkPhone.getCallState", "VideoTalkPhone.disconnect", "VideoTalkPhone.attachCallState", "VideoTalkPhone.detachCallState", "mobile.getCaps" ] }, "result" : true, "session" : 1143535103 } ....t...+.......t.........(D....{ "id" : 1579, "method" : "accessControl.factory.instance", "params" : { "Channel" : 0 }, "session" : 1143535103 } ....X9...+.......9.........(D....{ "id" : 1579, "result" : true, "session" : 1143535103 } ....m...+.......m.........(D....{ "id" : 1835, "method" : "accessControl.openDoor", "object" : 1, "params" : null, "session" : 1143535103 } ....X9...+.......9.........(D....{ "id" : 1835, "result" : true, "session" : 1143535103 } ....l...+.......l.........(D....{ "id" : 2091, "method" : "accessControl.destroy", "object" : 1, "params" : null, "session" : 1143535103 } ....X9...+.......9.........(D....{ "id" : 2091, "result" : true, "session" : 1143535103 } ...................................................................................X...............................................................X...............................................................X...............................................................X...............................................................X...............................................................X...............................................................X...............................................................X...............................................................X...............................................................X...............................................................X...............................................................X...............................................................X...............................................................................................................X............................................................................</p></blockquote></div><div id="question-tags" class="tags-container tags">http.response response</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '15, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/8696dfe0dcd3cc565df94068c349a255?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MuhammedRefaat&#39;s gravatar image" /><p>MuhammedRefaat<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MuhammedRefaat has no accepted answers">0%</span></p></div></div><div id="comments-container-45058" class="comments-container"></div><div id="comment-tools-45058" class="comment-tools"></div><div class="clear"></div><div id="comment-45058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45059"></span>

<div id="answer-container-45059" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45059-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It would appear that this is from a Dahua VTO6210B IP camera.</p><p>Seems to be a mix of some text and binary records and some json.</p><p>What are you expecting to see?</p><p>It would help if you posted the actual capture somewhere public, as the http headers might shed some more light and a paste of the text part of the http response body is difficult to make sense of on its own..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '15, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45059" class="comments-container"><span id="45062"></span><div id="comment-45062" class="comment"><div id="post-45062-score" class="comment-score"></div><div class="comment-text"><p>in fact I'm using the webservice of the camera and it works perfectly, so that I'm trying to capture and get the camera port commands to send it separately from my app that uses the camera but it only works for the first two commands, so I captured the mobile stream from the app that the camera company presented to know how they make the mobile app works although it can't just send the post commands like the webservice, and I'm getting the response I posted above, sorry for the long talk :)</p></div><div id="comment-45062-info" class="comment-info"><span class="comment-age">(13 Aug '15, 07:58)</span> MuhammedRefaat</div></div></div><div id="comment-tools-45059" class="comment-tools"></div><div class="clear"></div><div id="comment-45059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

