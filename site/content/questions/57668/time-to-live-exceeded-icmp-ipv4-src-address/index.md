+++
type = "question"
title = "Time-to-live exceeded - ICMP IPv4 SRC address"
description = '''Hi, I&#x27;m analysing pcap with traceroute and noticed that ICMP packets with Time-to-live exceeded are having under &quot;original&quot; packet that was sent source IP address not NATed i mean private from 192.168. I thought that when host on the internet discards packet then it send TTL exceeded but as source i...'''
date = "2016-11-27T20:30:00Z"
lastmod = "2016-11-29T07:38:00Z"
weight = 57668
keywords = [ "exceeded", "ttl" ]
aliases = [ "/questions/57668" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Time-to-live exceeded - ICMP IPv4 SRC address](/questions/57668/time-to-live-exceeded-icmp-ipv4-src-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57668-score" class="post-score" title="current number of votes">0</div><span id="post-57668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm analysing pcap with traceroute and noticed that ICMP packets with Time-to-live exceeded are having under "original" packet that was sent source IP address not NATed i mean private from 192.168. I thought that when host on the internet discards packet then it send TTL exceeded but as source it will see my public address. Are you able to put some light on this?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-exceeded" rel="tag" title="see questions tagged &#39;exceeded&#39;">exceeded</span> <span class="post-tag tag-link-ttl" rel="tag" title="see questions tagged &#39;ttl&#39;">ttl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '16, 20:30</strong></p><img src="https://secure.gravatar.com/avatar/0299fc71c94626d93ceeb9c4043c773c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="j202433&#39;s gravatar image" /><p><span>j202433</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="j202433 has no accepted answers">0%</span></p></div></div><div id="comments-container-57668" class="comments-container"></div><div id="comment-tools-57668" class="comment-tools"></div><div class="clear"></div><div id="comment-57668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57671"></span>

<div id="answer-container-57671" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57671-score" class="post-score" title="current number of votes">0</div><span id="post-57671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="j202433 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming this capture is done on your private address node, the following scenario takes place.</p><p>Your private address node sends an ICMP echo towards an internet host. It sees that the address is outside the locally attached network(s), so consults the routing table for the router to use. This is probably your home gateway (including the NAT). The Home Gateway gets the packet, sees that it needs to forward it through the NAT, so applies NATing and forwards the packet (decrementing TTL) to the next router. There the process repeats, without the NAT.</p><p>Once the TTL runs out the ICMP TTL-exceeded is send back, indeed addressed to your public address, with the original header with your public address. This gets back to your router, which NATs the packet to your local address. It can do that for both the normal IPv4 header as well as the ICMP TTL-exceeded payload, which it knows is the original header.</p><p>So the thing is, your NAT function is ICMP aware, and thus knows how to translate addresses in those type of packets.</p><p>If you want to know your public IP address you'll need something like <a href="https://en.wikipedia.org/wiki/STUN">STUN</a> which is specifically designed for this purpose.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '16, 21:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-57671" class="comments-container"><span id="57691"></span><div id="comment-57691" class="comment"><div id="post-57691-score" class="comment-score"></div><div class="comment-text"><p>Thank you.</p></div><div id="comment-57691-info" class="comment-info"><span class="comment-age">(29 Nov '16, 01:29)</span> <span class="comment-user userinfo">j202433</span></div></div><span id="57706"></span><div id="comment-57706" class="comment"><div id="post-57706-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-57706-info" class="comment-info"><span class="comment-age">(29 Nov '16, 07:38)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-57671" class="comment-tools"></div><div class="clear"></div><div id="comment-57671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

