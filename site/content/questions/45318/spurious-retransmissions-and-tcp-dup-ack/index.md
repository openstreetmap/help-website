+++
type = "question"
title = "spurious retransmissions and TCP dup ack"
description = '''Hello, I am experiencing stability issues with a connection from a windows PC to a embedded Linux using LWIP. One thing I can reproduce is that I get numerous Spurious Retransmissions and TCP Dup Acks. Maybe someone can check my tcp dump uploaded to  CloudShark Spurious Retransmissions Thank you for...'''
date = "2015-08-23T23:28:00Z"
lastmod = "2015-08-25T07:40:00Z"
weight = 45318
keywords = [ "spurious", "dup", "retransmissiond", "ack", "tcp" ]
aliases = [ "/questions/45318" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [spurious retransmissions and TCP dup ack](/questions/45318/spurious-retransmissions-and-tcp-dup-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45318-score" class="post-score" title="current number of votes">0</div><span id="post-45318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am experiencing stability issues with a connection from a windows PC to a embedded Linux using LWIP.</p><p>One thing I can reproduce is that I get numerous Spurious Retransmissions and TCP Dup Acks.</p><p>Maybe someone can check my tcp dump uploaded to <a href="https://www.cloudshark.org/captures/04977e87fbf2">CloudShark Spurious Retransmissions</a></p><p>Thank you for your support.</p><p>Regards, Chris</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-spurious" rel="tag" title="see questions tagged &#39;spurious&#39;">spurious</span> <span class="post-tag tag-link-dup" rel="tag" title="see questions tagged &#39;dup&#39;">dup</span> <span class="post-tag tag-link-retransmissiond" rel="tag" title="see questions tagged &#39;retransmissiond&#39;">retransmissiond</span> <span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '15, 23:28</strong></p><img src="https://secure.gravatar.com/avatar/010b61d67e57804ff8903e80d998f76b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="christofb&#39;s gravatar image" /><p><span>christofb</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="christofb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Aug '15, 04:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-45318" class="comments-container"></div><div id="comment-tools-45318" class="comment-tools"></div><div class="clear"></div><div id="comment-45318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45345"></span>

<div id="answer-container-45345" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45345-score" class="post-score" title="current number of votes">0</div><span id="post-45345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The trace was taken at the windows machine and it shows that lots of packets from linux get droppoed on their way to the trace point. As linux increments the ip.id per tcp session we can determine that 5 packets at the end of batch get lost (ip.id 7070-7074) between frame 36 and frame 40 and ipids 707a and 707b between frame 48 and frame 50.<br />
Why this happens is not clear to me but I doubt it is the Cisco router dropping those packets. Maybe it has to do with too tiny transmit queue-sizes in the linux stack.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-4.png" alt="alt text" /><br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '15, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div></div><div id="comments-container-45345" class="comments-container"></div><div id="comment-tools-45345" class="comment-tools"></div><div class="clear"></div><div id="comment-45345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

