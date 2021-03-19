+++
type = "question"
title = "SSL request hangs intermittently with Amazon LB SSL (Capture Included)"
description = '''Greetings, I&#x27;ve been trying very desperately to track down the source of an issue I&#x27;m having with a large SSL request to my Apache server (75K-100K). Every 20 requests or so, when issuing the request in FF, the request hangs. The server is Apache running in Amazon EC2 behind a LB that handles the SS...'''
date = "2014-01-03T06:42:00Z"
lastmod = "2014-01-04T06:41:00Z"
weight = 28548
keywords = [ "load", "ssl", "balancer", "intermittent" ]
aliases = [ "/questions/28548" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SSL request hangs intermittently with Amazon LB SSL (Capture Included)](/questions/28548/ssl-request-hangs-intermittently-with-amazon-lb-ssl-capture-included)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28548-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings,</p><p>I've been trying very desperately to track down the source of an issue I'm having with a large SSL request to my Apache server (75K-100K). Every 20 requests or so, when issuing the request in FF, the request hangs. The server is Apache running in Amazon EC2 behind a LB that handles the SSL. (us-east-1)</p><p>I'm able to capture the wireshark trace (see <a href="http://cloudshark.org/captures/b9425eb191fc">http://cloudshark.org/captures/b9425eb191fc</a> ) and I believe what I'm seeing is that the LB becomes unresponsive possibly under load? I see slowness in other browsers but in Firefox, the request often hangs indefinitely.</p><p>Notes on the trace file.</p><ul><li>I'm issuing the request about once every 16 seconds, starting at 6891,7601, 8150, 9110</li><li>9110 is the start of a failed (or hung) request. TCP stream 155</li><li>Looking at the ACK in 9188 or 9351 you can see delays in the ACK receipt from RTT.</li><li>As far as decoding, attempts to add the private key fail with "using server decoder" -&gt; "no decoder available".</li><li>Keep-alive is enabled on the server.</li></ul><p>Any input on this would be greatly appreciated. Original ideas were issues with the cipher or encryption issues, but I don't see errors in the trace other than normal terminations.</p><p>Chris</p></div><div id="question-tags" class="tags-container tags">load ssl balancer intermittent</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '14, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/a3b34a7941537365d1114d79b2132212?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris%20in%20Ottawa&#39;s gravatar image" /><p>Chris in Ottawa<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris in Ottawa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jan '14, 10:34</p></div></div><div id="comments-container-28548" class="comments-container"></div><div id="comment-tools-28548" class="comment-tools"></div><div class="clear"></div><div id="comment-28548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28567"></span>

<div id="answer-container-28567" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28567-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've been looking at a hung session (tcp.port==64544) in the trace and I think the problem is due to your windows client not retransmitting "in time". In the example below, its retransmission timer increases from 300ms all the way up to 48 secs.</p><p>A few observations.</p><ul><li>The client is using Segmentation offload</li><li>Both client and server agreed upon SACK</li><li>The server never sends the SACK option reporting a gap</li></ul><p>So this behaviour might be a combination of SACK and LSO not working together well. You could try truning it off as described here <a href="http://www.peerwisdom.org/2013/04/25/disabling-large-send-offload-windows/">http://www.peerwisdom.org/2013/04/25/disabling-large-send-offload-windows/</a></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_026.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '14, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-28567" class="comments-container"><span id="28598"></span><div id="comment-28598" class="comment"><div id="post-28598-score" class="comment-score"></div><div class="comment-text"><p>Thank you for spending the time to go through this. I'll read up on these protocols, try your suggestion and run more tests from alternate clients, networks, etc. I'll post back. - Chris</p></div><div id="comment-28598-info" class="comment-info"><span class="comment-age">(06 Jan '14, 05:54)</span> Chris in Ottawa</div></div></div><div id="comment-tools-28567" class="comment-tools"></div><div class="clear"></div><div id="comment-28567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28557"></span>

<div id="answer-container-28557" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28557-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I couldn't get the capture from the link. In any case did you try to run capture on both side (server and client)? what about fiddler?<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '14, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/94630d1ea1108afeafb344e884044d15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Boaz%20Galil&#39;s gravatar image" /><p>Boaz Galil<br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Boaz Galil has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-28557" class="comments-container"><span id="28558"></span><div id="comment-28558" class="comment"><div id="post-28558-score" class="comment-score"></div><div class="comment-text"><p>Fixed up the link to the capture above. Not really sure how to go about getting the trace from the Load Balancer side of things (I have requests in to Amazon) Good idea about Fiddler, it might reveal something as well. Chris</p></div><div id="comment-28558-info" class="comment-info"><span class="comment-age">(03 Jan '14, 10:37)</span> Chris in Ottawa</div></div></div><div id="comment-tools-28557" class="comment-tools"></div><div class="clear"></div><div id="comment-28557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

