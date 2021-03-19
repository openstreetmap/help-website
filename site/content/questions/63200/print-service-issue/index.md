+++
type = "question"
title = "print service issue"
description = '''Hi Guys  We have a really strange situation since the last upgrade of our PALO ALTO (ACTIVE ACTIVE HA) firewalls. From time to time, randomly some users report printers offline (there is a print server). The architecture is like this: |USERS|==&amp;gt;|Router1|==&amp;gt;|PA1|==&amp;gt;|ROUTER2|==&amp;gt;|SRX2|==&amp;gt...'''
date = "2017-07-28T00:59:00Z"
lastmod = "2017-07-31T22:41:00Z"
weight = 63200
keywords = [ "print", "tcp-sporious", "rst-ack", "service" ]
aliases = [ "/questions/63200" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [print service issue](/questions/63200/print-service-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63200-score" class="post-score" title="current number of votes">0</div><span id="post-63200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys We have a really strange situation since the last upgrade of our PALO ALTO (ACTIVE ACTIVE HA) firewalls. From time to time, randomly some users report printers offline (there is a print server). The architecture is like this:</p><p>|USERS|==&gt;|Router1|==&gt;|PA1|==&gt;|ROUTER2|==&gt;|SRX2|==&gt;PrintSERVER The upgrade was done only on the Palo Alto Fw. Facts observed: - massive amount of "tcp spurious retransmission" followed by (RST,ACK )from the server - the issue is coming during the 3way Handshake (client sending a SYN , server-spourious, server sending the (RST,ACK) ) - is around the same hour - is just the printing server (not http flow, as we have a web server on the same machine-VM actually) - the other type of traffic is not affected - I have traces on the Server and also on the PA - routing wise -nothing is changed during the ISSUE (traceroute) - on the server side we don't see too manny logs related with the issue (2,3 when we have normally 30 users complaining) - on the Print server we don't see a massive number of connection during that hour that can cause somehow the communication to crush - there is no increasing in the latency dring that hour (same 6 ms RTT) - routing wise , the traffic is not asymmetric (interface wise it is sometimes as we have a portchannel between PA and routing devices) I would appreciate if I can have any thoughts from you, that can help me to solve this issue. Regards! server side captures:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Snap_2017-07-28_at_09.54.47_oTejccz.jpg" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Snap_2017-07-28_at_09.56.34.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-print" rel="tag" title="see questions tagged &#39;print&#39;">print</span> <span class="post-tag tag-link-tcp-sporious" rel="tag" title="see questions tagged &#39;tcp-sporious&#39;">tcp-sporious</span> <span class="post-tag tag-link-rst-ack" rel="tag" title="see questions tagged &#39;rst-ack&#39;">rst-ack</span> <span class="post-tag tag-link-service" rel="tag" title="see questions tagged &#39;service&#39;">service</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '17, 00:59</strong></p><img src="https://secure.gravatar.com/avatar/ef9a345192b7329057a740f6eed3ccdf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mariusG&#39;s gravatar image" /><p><span>mariusG</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mariusG has no accepted answers">0%</span></p></img></div></div><div id="comments-container-63200" class="comments-container"></div><div id="comment-tools-63200" class="comment-tools"></div><div class="clear"></div><div id="comment-63200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63203"></span>

<div id="answer-container-63203" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63203-score" class="post-score" title="current number of votes">0</div><span id="post-63203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In your situation, I would capture at both sides of the Palo Alto <strong>simultaneously</strong> until the issue happens and compare the traces. And if this would show that some packets didn't make it to the other side at all or got modified in a destructive way, I would open a support case with Palo Alto.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '17, 01:37</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></img></div></div><div id="comments-container-63203" class="comments-container"><span id="63268"></span><div id="comment-63268" class="comment"><div id="post-63268-score" class="comment-score"></div><div class="comment-text"><p>Thanks mate!! I've done a capture on the PaloAlto FW and there are packets that are dropped. I've open the ticket to the provider to see where is the issue. What I cannot explain is the fact that is random...is coming and going so in 10 min you have to be ready to capture what is necessary ! I will let you know about the result! Thanks!</p></div><div id="comment-63268-info" class="comment-info"><span class="comment-age">(31 Jul '17, 22:25)</span> <span class="comment-user userinfo">mariusG</span></div></div><span id="63270"></span><div id="comment-63270" class="comment"><div id="post-63270-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-63270-info" class="comment-info"><span class="comment-age">(31 Jul '17, 22:41)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-63203" class="comment-tools"></div><div class="clear"></div><div id="comment-63203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

