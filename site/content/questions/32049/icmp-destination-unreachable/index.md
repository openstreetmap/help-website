+++
type = "question"
title = "ICMP Destination Unreachable"
description = '''Hi, my first post in here. I made lots of search but couldn&#x27;t find useful info about how create ICMP Code-3 (dest. unreachable) error and capture it with Wireshark. I tried to ping a closed port in Linux machine and also used host command but nothing. Could anyone help me about this please?  Thank y...'''
date = "2014-04-22T04:10:00Z"
lastmod = "2014-04-22T05:40:00Z"
weight = 32049
keywords = [ "icmp" ]
aliases = [ "/questions/32049" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ICMP Destination Unreachable](/questions/32049/icmp-destination-unreachable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32049-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, my first post in here. I made lots of search but couldn't find useful info about how create ICMP Code-3 (dest. unreachable) error and capture it with Wireshark. I tried to ping a closed port in Linux machine and also used host command but nothing. Could anyone help me about this please? Thank you.</p></div><div id="question-tags" class="tags-container tags">icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '14, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/0e5cae167fcef0f3e33eeebfe13a5988?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erer&#39;s gravatar image" /><p>erer<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erer has no accepted answers">0%</span></p></div></div><div id="comments-container-32049" class="comments-container"></div><div id="comment-tools-32049" class="comment-tools"></div><div class="clear"></div><div id="comment-32049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32051"></span>

<div id="answer-container-32051" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32051-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need a router (Linux) that does not know how to forward a frame to a destination network (network unreachable), or that does not get an ARP reply (Host unreachable).</p><p><strong>Sample setup</strong>:</p><pre><code>client [10.1.1.20]  ---- [10.1.1.1] eth0 :: router :: eth1 [192.168.1.1]</code></pre><p>Set the following routes</p><p><strong>client</strong></p><ul><li>route add 192.168.1.0 mask 255.255.255.0 10.1.1.1</li><li>route add 192.168.5.0 mask 255.255.255.0 10.1.1.1</li></ul><p><strong>router</strong></p><ul><li>enable IP Forwarding: <code>sysctl net.ipv4.ip_forward=1</code></li><li><strong>don't set a default route!!</strong>: route delete default</li></ul><p>Now, ping the following IP addresses from the client:</p><ul><li>ping 192.168.1.5 :: you will get a <code>ICMP Destination unreachable (Host unreachable)</code></li><li>ping 192.168.5.5 :: you will get a <code>ICMP Destination unreachable (Network unreachable)</code></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '14, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Apr '14, 06:44</p></div></div><div id="comments-container-32051" class="comments-container"><span id="32055"></span><div id="comment-32055" class="comment"><div id="post-32055-score" class="comment-score"></div><div class="comment-text"><p>Big thanks Kurt. This is awesome and very straight forward answer. Cant wait to try it :)</p></div><div id="comment-32055-info" class="comment-info"><span class="comment-age">(22 Apr '14, 06:50)</span> erer</div></div><span id="32057"></span><div id="comment-32057" class="comment"><div id="post-32057-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-32057-info" class="comment-info"><span class="comment-age">(22 Apr '14, 07:31)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-32051" class="comment-tools"></div><div class="clear"></div><div id="comment-32051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

