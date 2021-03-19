+++
type = "question"
title = "Need help reviewing a wireshark log and find out why a SIP call was dropped"
description = '''Hello, I do not the expertise to properly analyze a wireshar log- I hope someone could please help reviewing a WireShark log and find out why a SIP call was dropped: We have an application that uses Dialogic/HMP. This application requests outbound SIP calls to an Asterisk server. Suddenly, our HMP/a...'''
date = "2015-11-10T10:04:00Z"
lastmod = "2015-11-10T19:40:00Z"
weight = 47475
keywords = [ "asterisk", "sip", "call", "iperr" ]
aliases = [ "/questions/47475" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Need help reviewing a wireshark log and find out why a SIP call was dropped](/questions/47475/need-help-reviewing-a-wireshark-log-and-find-out-why-a-sip-call-was-dropped)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47475-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I do not the expertise to properly analyze a wireshar log- I hope someone could please help reviewing a WireShark log and find out why a SIP call was dropped: We have an application that uses Dialogic/HMP. This application requests outbound SIP calls to an Asterisk server. Suddenly, our HMP/app receives this message: IPERR_INVALID_PHONE_NUMBER and we have to reboot.</p><p>Could someone please, take a quick look ate the Wiresharlog and analyze why and who dropped a particular outbound call? I can supply the log and further info if needed. Thanks a lot</p></div><div id="question-tags" class="tags-container tags">asterisk sip call iperr</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '15, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/78d99cc915d443c347e5e3d9f915e9ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="saveriobaq&#39;s gravatar image" /><p>saveriobaq<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="saveriobaq has no accepted answers">0%</span></p></div></div><div id="comments-container-47475" class="comments-container"><span id="47487"></span><div id="comment-47487" class="comment"><div id="post-47487-score" class="comment-score"></div><div class="comment-text"><p>Can you upload the packet capture online and post a link? Dropbox for example.</p></div><div id="comment-47487-info" class="comment-info"><span class="comment-age">(10 Nov '15, 15:13)</span> Quadratic</div></div><span id="47488"></span><div id="comment-47488" class="comment"><div id="post-47488-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot sindy and quadratic. Please download the pcapng file from <a href="https://drive.google.com/file/d/0B45IDDeIjT2edHpvXzIzdE5nRFU/view?usp=sharing">https://drive.google.com/file/d/0B45IDDeIjT2edHpvXzIzdE5nRFU/view?usp=sharing</a></p><p>Please search from the bottom up for the number I was calling: 60999839104 you will see a 487 Request terminated message. Need to know what happen to this call.</p><p>Regards Saverio</p></div><div id="comment-47488-info" class="comment-info"><span class="comment-age">(10 Nov '15, 16:38)</span> saveriobaq</div></div></div><div id="comment-tools-47475" class="comment-tools"></div><div class="clear"></div><div id="comment-47475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47476"></span>

<div id="answer-container-47476" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47476-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, I can have a look at the SIP message exchange, but don't expect too much: Wireshark shows you <strong>what</strong> has happened but not <strong>why</strong> it has happened. To know why exactly the HMP's SIP stack has dropped the call, you'll need to see its logs, even if I eventually tell you what was wrong with some SIP message.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '15, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-47476" class="comments-container"><span id="47506"></span><div id="comment-47506" class="comment"><div id="post-47506-score" class="comment-score"></div><div class="comment-text"><p>I've checked too and I agree with <a href="https://ask.wireshark.org/users/5283/rooster_50">Rooster_50</a> that there is nothing odd in this particular call as compared to those calls in the capture which have the same calling and called and have not crashed your application.</p><p>So as I wrote initially, dive yourself into the HMP's log files which should explain you why HMP has sent to your application the exception (which, I agree, doesn't seem logical in combination with those totally harmless SIP messages).</p><p>If you use the HMP together with an E1 card and the SIP calls to Asterisk are triggered by incoming TDM calls, you might want to trace the TDM side simultaneously with running the wireshark to see whether something ugly does not come from the TDM side, as the last step before taking the adventure of reading HMP's logs.</p></div><div id="comment-47506-info" class="comment-info"><span class="comment-age">(11 Nov '15, 00:45)</span> sindy</div></div><span id="47537"></span><div id="comment-47537" class="comment"><div id="post-47537-score" class="comment-score"></div><div class="comment-text"><p>Hi Saverio,<br />
part of your capture is useful to illustrate a Wireshark bug I want to file. I cannot use my own capture which shows the same issue because is taken in production environment at a customer. Would you mind if I use part of your capture to file the bug? It would be the SIP message exchange of the crashed call and the RTP streams which use the same UDP port on the Dialogic side, i.e. the RTP of the crashed call itself and of two other ones.<br />
</p><p>Thank you<br />
Pavel</p></div><div id="comment-47537-info" class="comment-info"><span class="comment-age">(12 Nov '15, 02:11)</span> sindy</div></div></div><div id="comment-tools-47476" class="comment-tools"></div><div class="clear"></div><div id="comment-47476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47494"></span>

<div id="answer-container-47494" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47494-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The 487 Request Terminated is in response to the CANCEL request sent by the Client (10.5.232.150) terminating the session before a 200 response was received.</p><p>The finger is pointed at 10.5.232.150. Check your application logs for further details as to what happened.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '15, 19:40</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-47494" class="comments-container"></div><div id="comment-tools-47494" class="comment-tools"></div><div class="clear"></div><div id="comment-47494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

