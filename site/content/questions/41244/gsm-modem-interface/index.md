+++
type = "question"
title = "GSM Modem Interface"
description = '''Hi i have Ublox Leon G100 i would like to find out how to get a interface for it i am running Kali Linux. the ublox has a Serial port and usb i can send sms and receive sms i can make voice calls and receive voice calls but i cant analyze any of it with out a interface'''
date = "2015-04-07T03:56:00Z"
lastmod = "2015-04-09T03:22:00Z"
weight = 41244
keywords = [ "interface", "modem", "gsm" ]
aliases = [ "/questions/41244" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [GSM Modem Interface](/questions/41244/gsm-modem-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41244-score" class="post-score" title="current number of votes">0</div><span id="post-41244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi i have Ublox Leon G100 i would like to find out how to get a interface for it i am running Kali Linux. the ublox has a Serial port and usb i can send sms and receive sms i can make voice calls and receive voice calls but i cant analyze any of it with out a interface</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-modem" rel="tag" title="see questions tagged &#39;modem&#39;">modem</span> <span class="post-tag tag-link-gsm" rel="tag" title="see questions tagged &#39;gsm&#39;">gsm</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '15, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/a0d9c4677ec1a7895b11dd7dee4d83bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BadBoy&#39;s gravatar image" /><p><span>BadBoy</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BadBoy has no accepted answers">0%</span></p></div></div><div id="comments-container-41244" class="comments-container"></div><div id="comment-tools-41244" class="comment-tools"></div><div class="clear"></div><div id="comment-41244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41249"></span>

<div id="answer-container-41249" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41249-score" class="post-score" title="current number of votes">0</div><span id="post-41249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If I understand you correctly, you are trying to capture the 2G GSM/GPRS protocol messages as define in 3GPP specifications, right? If yes it requires some specific logging function inside your modem and you will not be able to capture them with a standard Linux interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '15, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-41249" class="comments-container"><span id="41252"></span><div id="comment-41252" class="comment"><div id="post-41252-score" class="comment-score"></div><div class="comment-text"><p>Thanks so much for the replay. I have a program called M-Center from UBlox that works 100% on any windows system my goal is to see what information i can pick up from sending a text message (SMS) to a mobile device and see if i can identify its cell id from a force return message i know i can find the LAC but i am not sure about the cell id do you have any suggested interface for me</p></div><div id="comment-41252-info" class="comment-info"><span class="comment-age">(07 Apr '15, 08:30)</span> <span class="comment-user userinfo">BadBoy</span></div></div><span id="41261"></span><div id="comment-41261" class="comment"><div id="post-41261-score" class="comment-score"></div><div class="comment-text"><p>If you have access to a serial port allowing you to send AT commands, you can look at the ouput of CREG command when using n=2:</p><p>AT+CEREG=2</p><p>then do</p><p>AT+CEREG?</p><p>And the ouput should be</p><p>+CREG: &lt;stat&gt;[,[&lt;lac&gt;],[&lt;ci&gt;],[&lt;act&gt;]]</p><p>See 3GPP 27.007 specification for details.</p></div><div id="comment-41261-info" class="comment-info"><span class="comment-age">(07 Apr '15, 11:26)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="41273"></span><div id="comment-41273" class="comment"><div id="post-41273-score" class="comment-score"></div><div class="comment-text"><p>the AT+CEREG=2 gives me a Error =(</p></div><div id="comment-41273-info" class="comment-info"><span class="comment-age">(08 Apr '15, 01:14)</span> <span class="comment-user userinfo">BadBoy</span></div></div><span id="41275"></span><div id="comment-41275" class="comment"><div id="post-41275-score" class="comment-score"></div><div class="comment-text"><p>Sorry I did a typo and wanted to type AT+CREG=2; AT+CREG? and not AT+CEREG (that is used for LTE modems). According to <a href="https://www.u-blox.com/images/downloads/Product_Docs/u-blox-ATCommands_Manual_%28UBX-13002752%29.pdf">https://www.u-blox.com/images/downloads/Product_Docs/u-blox-ATCommands_Manual_%28UBX-13002752%29.pdf</a> this command is supported so it should give you the GSM cell identity.</p></div><div id="comment-41275-info" class="comment-info"><span class="comment-age">(08 Apr '15, 01:33)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="41279"></span><div id="comment-41279" class="comment"><div id="post-41279-score" class="comment-score"></div><div class="comment-text"><p>Seriously ! ! ! OMG your haven sent ! lol i been thru that site a good number of times got a lot of PDF's but i its the 1st time seeing this one THANKS a Billion</p></div><div id="comment-41279-info" class="comment-info"><span class="comment-age">(08 Apr '15, 05:50)</span> <span class="comment-user userinfo">BadBoy</span></div></div><span id="41294"></span><div id="comment-41294" class="comment not_top_scorer"><div id="post-41294-score" class="comment-score"></div><div class="comment-text"><p>i have all the codes i would ever need but i don't have any idea how to send them to a mobile device for example</p><p>AT+CREG=2 OK AT+CREG=? +CREG: (0-2)</p><p>The manual does not give any clear examples where do we in put the cell phone number and how will it return what am i missing ?</p></div><div id="comment-41294-info" class="comment-info"><span class="comment-age">(08 Apr '15, 09:00)</span> <span class="comment-user userinfo">BadBoy</span></div></div><span id="41295"></span><div id="comment-41295" class="comment not_top_scorer"><div id="post-41295-score" class="comment-score"></div><div class="comment-text"><p>You must type "AT+CREG?", not "AT+CREG=?"</p></div><div id="comment-41295-info" class="comment-info"><span class="comment-age">(08 Apr '15, 09:36)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="41312"></span><div id="comment-41312" class="comment not_top_scorer"><div id="post-41312-score" class="comment-score"></div><div class="comment-text"><p>I must be doing some thing wrong i cant send any commands it keeps sending them to the ublox and it only replays with OK or ERROR i am looking in to PDU and APDU right now maybe i can send and request it thru HEX messages</p></div><div id="comment-41312-info" class="comment-info"><span class="comment-age">(09 Apr '15, 01:06)</span> <span class="comment-user userinfo">BadBoy</span></div></div><span id="41317"></span><div id="comment-41317" class="comment not_top_scorer"><div id="post-41317-score" class="comment-score"></div><div class="comment-text"><p>I have a USRP can i scan GSM packets with it in airprobe and scan airprobe with wireshark for example <a href="https://www.youtube.com/watch?v=FqtJ-TvtLTQ">https://www.youtube.com/watch?v=FqtJ-TvtLTQ</a> but how will i get a fixed signal on the ublox ?</p></div><div id="comment-41317-info" class="comment-info"><span class="comment-age">(09 Apr '15, 03:22)</span> <span class="comment-user userinfo">BadBoy</span></div></div></div><div id="comment-tools-41249" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-41249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

