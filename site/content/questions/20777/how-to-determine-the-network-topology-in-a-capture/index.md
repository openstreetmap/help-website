+++
type = "question"
title = "how to determine the network topology in a capture"
description = '''Hi guys, I&#x27;m new to wireshark and I need to know how figure out the network topology from a wireshark capture, please can someone shed some light on the subject many thanks  H'''
date = "2013-04-24T12:26:00Z"
lastmod = "2013-04-24T12:44:00Z"
weight = 20777
keywords = [ "network", "topology" ]
aliases = [ "/questions/20777" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to determine the network topology in a capture](/questions/20777/how-to-determine-the-network-topology-in-a-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20777-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I'm new to wireshark and I need to know how figure out the network topology from a wireshark capture, please can someone shed some light on the subject</p><p>many thanks</p><p>H</p></div><div id="question-tags" class="tags-container tags">network topology</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '13, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/ba098a871f62a184f74eb61b16b9abc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harry82&#39;s gravatar image" /><p>harry82<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harry82 has no accepted answers">0%</span></p></div></div><div id="comments-container-20777" class="comments-container"><span id="20783"></span><div id="comment-20783" class="comment"><div id="post-20783-score" class="comment-score"></div><div class="comment-text"><p>what do you mean (exactly) by 'network topology'?</p></div><div id="comment-20783-info" class="comment-info"><span class="comment-age">(24 Apr '13, 14:29)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20777" class="comment-tools"></div><div class="clear"></div><div id="comment-20777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20778"></span>

<div id="answer-container-20778" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20778-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no general method to do this. I usually look at the ip.ttl of inbound packets. Most platforms send with a default initial TTL so you can guess how far away (in terms of L3 hops) they are if you know the initial TTL. 3-way handshake tcp options can be used to determine the sending OS (p0f). MAC addresses and ARP packets give an idea of the local topology ...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '13, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p>mrEEde2<br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div></div><div id="comments-container-20778" class="comments-container"></div><div id="comment-tools-20778" class="comment-tools"></div><div class="clear"></div><div id="comment-20778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

