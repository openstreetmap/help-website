+++
type = "question"
title = "Trying to ID data within packets."
description = '''Hello! We use a product called Deepfreeze to restart and shutdown PC&#x27;s. There are 1200 PC&#x27;s reporting to the Deepfreeze server / console. I have a test environment with one PC reporting to a test server that mirrors our current configuration. We have an issue where workstations are restarting / shut...'''
date = "2013-04-05T09:09:00Z"
lastmod = "2013-04-06T09:06:00Z"
weight = 20118
keywords = [ "hex", "data", "string" ]
aliases = [ "/questions/20118" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to ID data within packets.](/questions/20118/trying-to-id-data-within-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20118-score" class="post-score" title="current number of votes">0</div><span id="post-20118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! We use a product called Deepfreeze to restart and shutdown PC's. There are 1200 PC's reporting to the Deepfreeze server / console. I have a test environment with one PC reporting to a test server that mirrors our current configuration.</p><p>We have an issue where workstations are restarting / shutting down "on their own". Unfortunately due to the nature of workplace (us vs them) and the finger pointing has started. So on to my question;</p><p>In my test environment I have done a capture of the restart / shutdown command between server and client PC. 8 TCP packets were captured.</p><p>server -&gt; client: psh, ack</p><p>client -&gt; server: ack</p><p>server -&gt; client: psh, ack</p><p>client -&gt; server: psh, ack</p><p>server -&gt; client: ack</p><p>client -&gt; server: psh, ack</p><p>server -&gt; client: ack</p><p>client -&gt; server: rst, ack</p><p>Somewhere in there is the data that triggers the restart / shutdown. How do I go about finding that "string" so that I can filter on it in the production environment?</p><p>Thank you! Giles</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hex" rel="tag" title="see questions tagged &#39;hex&#39;">hex</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-string" rel="tag" title="see questions tagged &#39;string&#39;">string</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '13, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/c930039151390b09e729f0879f44a29d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Malarky&#39;s gravatar image" /><p><span>Malarky</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Malarky has no accepted answers">0%</span></p></div></div><div id="comments-container-20118" class="comments-container"></div><div id="comment-tools-20118" class="comment-tools"></div><div class="clear"></div><div id="comment-20118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20125"></span>

<div id="answer-container-20125" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20125-score" class="post-score" title="current number of votes">2</div><span id="post-20125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The list of packets you quoted doesn't help much since there is no payload to examine <strong>and</strong> the capture is incomplete since there is no handshake - I'd have to be a techno-psychic to tell you that it is "in THAT packet". But even if you provide a trace file it is probably difficult to spot the command unless the deep freeze protocol is simple to reverse engineer.</p><p>If I were you I'd try to contact the vendor support to ask them how to determine that a shutdown command was issued. Maybe they'll be able to tell you how the protocol works - otherwise, you'll have to do a lot of research to find out yourself. I would probably try to do a differential analysis where I compare traces of "normal" deep freeze operations to traces where I am certain that a shutdown command is sent. With enough trace data it should be possible to determine how a shutdown command looks like - unless the protocol is using encryption, in which case you'd be out of luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '13, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20125" class="comments-container"><span id="20128"></span><div id="comment-20128" class="comment"><div id="post-20128-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply.</p><p>The handshake is established when the PC first checks in with the server, so you if the PC has been up for 4 hours that handshake would have taken place then.</p><p>In my test environment;</p><p>1 client PC. 1 Server.</p><p>I started a capture and observed traffic for an hour and noticed that an 8 packet exchange sequence occurs every 30 seconds that I assume is a polling of online PC's that registered with the server when powered on.</p><p>At the end of one of those exchanges I issued the restart command so I can be confident that what I captured is specific to the aformentioned restart issued command.</p><p>re- differential analysis. I am willing to do that. Just looking for suggestions on how to dive deeper and if wireshark has the capability to help me differentiate between the data of normal polling data and command issued data?</p><p>Thank you! Giles</p></div><div id="comment-20128-info" class="comment-info"><span class="comment-age">(06 Apr '13, 06:16)</span> <span class="comment-user userinfo">Malarky</span></div></div><span id="20129"></span><div id="comment-20129" class="comment"><div id="post-20129-score" class="comment-score"></div><div class="comment-text"><p>Wireshark has no special capabilities to help you with differentiation, you'll have to do it yourself. I would load two conversations (or partial conversations) into separate Wireshark instances and compare them manually, which is why my workstation setup always has at least two monitors as an absolute minimum. You could also double click packets in the packet list to open additional decode views if you need to compare packets within the same trace. I guess you can ignore everything including the TCP/UDP headers and concentrate on the payload.</p><p>If I'd already know that some parts of the trace contain normal polling events I would compare one of them with the one where I know I issued a restart command to see where the difference in the payload is. This may also involve using hex editors and/or scientific calculators to determine what payload byte/word is a command code and what is a parameter. I have to admit that a lot of that comes down to intuition and lots of experience, so if this is the first time you do this it'll take a while.</p><p><em>BTW i converted your answer to a comment to keep things clean.</em></p></div><div id="comment-20129-info" class="comment-info"><span class="comment-age">(06 Apr '13, 06:34)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-20125" class="comment-tools"></div><div class="clear"></div><div id="comment-20125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20133"></span>

<div id="answer-container-20133" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20133-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20133-score" class="post-score" title="current number of votes">1</div><span id="post-20133-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Somewhere in there is the data that triggers the restart / shutdown. How do I go about finding that "string" so that I can filter on it in the production environment?</p></blockquote><p>I don't think there is any <strong>cleartext magic string</strong> that triggers a restart/shutdown. After all this is an enterprise solution and I'm pretty confident, that they use some form of authentication (OTP according to their web site) and/or encryption to authorize any action on the target. If they don't protect the communication, everybody in your network would be able to capture that <strong>magic string</strong> and restart/shutdown any PC at will.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '13, 09:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20133" class="comments-container"></div><div id="comment-tools-20133" class="comment-tools"></div><div class="clear"></div><div id="comment-20133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

