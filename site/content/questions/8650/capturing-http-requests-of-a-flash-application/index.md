+++
type = "question"
title = "Capturing HTTP requests of a (flash) application"
description = '''Hi there.  I&#x27;m currently analysing a flash application. For that reason, I need to know what HTTP requests (such as POST and GET) are send by the application. For some reason only a very few HTTP requests are captured, even though I know for certain that there are many more requests. I have Wireshar...'''
date = "2012-01-27T04:08:00Z"
lastmod = "2012-04-20T01:30:00Z"
weight = 8650
keywords = [ "http" ]
aliases = [ "/questions/8650" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing HTTP requests of a (flash) application](/questions/8650/capturing-http-requests-of-a-flash-application)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8650-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there.</p><p>I'm currently analysing a flash application. For that reason, I need to know what HTTP requests (such as POST and GET) are send by the application. For some reason only a very few HTTP requests are captured, even though I know for certain that there are many more requests. I have Wireshark set to the default settings.</p><p>Which settings should I change to view this traffic?</p><p>Thanks in advance! Erwin</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '12, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/326b3576c39edcd427fef6037b434ef7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Erwin&#39;s gravatar image" /><p>Erwin<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Erwin has no accepted answers">0%</span></p></div></div><div id="comments-container-8650" class="comments-container"></div><div id="comment-tools-8650" class="comment-tools"></div><div class="clear"></div><div id="comment-8650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="8686"></span>

<div id="answer-container-8686" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8686-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ok... try this - use a display filter <strong>frame contains ".swf"</strong> - that should show you the request for the flash file. If the flash app traffic is available to Wireshark, it should capture it. Sometimes it is just a matter of finding it on the trace file.</p><p>Alternately, select File &gt; Export &gt; Objects &gt; HTTP and see if the flash download is in there - look at the file size. You can select the .swf-related line and choose save as to reassemble the flash file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '12, 00:49</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-8686" class="comments-container"></div><div id="comment-tools-8686" class="comment-tools"></div><div class="clear"></div><div id="comment-8686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8820"></span>

<div id="answer-container-8820" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8820-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Flash may also be using HTTP pipelining. Check your "very few" HTTP connections and see if multiple requests are being submitted over a single connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '12, 21:03</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-8820" class="comments-container"></div><div id="comment-tools-8820" class="comment-tools"></div><div class="clear"></div><div id="comment-8820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10331"></span>

<div id="answer-container-10331" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10331-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If any of the traffic from the flash application is HTTPS, you will not even see the HTTP packet type in Wireshark, since the HTTP packets are traveling as encrypted data over an SSL/TLS connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '12, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p>inetdog<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span></p></div></div><div id="comments-container-10331" class="comments-container"></div><div id="comment-tools-10331" class="comment-tools"></div><div class="clear"></div><div id="comment-10331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

