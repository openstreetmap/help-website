+++
type = "question"
title = "Cannot capture crafted raw packet on Intel X540 T2 10G NIC"
description = '''I create and send Ethernet packet by SharpPcap, then I catch those packets by wireshark. When I send those packets to my Intel 82579LM gigabit NIC, I can catch those packets. But I cannot catch any single packet when I send those packets to my Intel X540 T2 10 GE NIC. I can catch packets such as ICM...'''
date = "2012-06-26T15:36:00Z"
lastmod = "2012-06-26T16:42:00Z"
weight = 12214
keywords = [ "10", "ge", "packets", "lost", "nic" ]
aliases = [ "/questions/12214" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot capture crafted raw packet on Intel X540 T2 10G NIC](/questions/12214/cannot-capture-crafted-raw-packet-on-intel-x540-t2-10g-nic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12214-score" class="post-score" title="current number of votes">0</div><span id="post-12214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I create and send Ethernet packet by SharpPcap, then I catch those packets by wireshark. When I send those packets to my Intel 82579LM gigabit NIC, I can catch those packets. But I cannot catch any single packet when I send those packets to my Intel X540 T2 10 GE NIC. I can catch packets such as ICMP, TCP but not my own packets. Is the problem on NIC or wireshark? Does wireshark support 10 GE NIC in promiscuous mode? How can I catch packets on my 10 GE NIC as like 1 GE NIC?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-10" rel="tag" title="see questions tagged &#39;10&#39;">10</span> <span class="post-tag tag-link-ge" rel="tag" title="see questions tagged &#39;ge&#39;">ge</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-lost" rel="tag" title="see questions tagged &#39;lost&#39;">lost</span> <span class="post-tag tag-link-nic" rel="tag" title="see questions tagged &#39;nic&#39;">nic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '12, 15:36</strong></p><img src="https://secure.gravatar.com/avatar/c233e461648582b4d3bd233e6f2d872a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="decula&#39;s gravatar image" /><p><span>decula</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="decula has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jun '12, 15:37</strong> </span></p></div></div><div id="comments-container-12214" class="comments-container"></div><div id="comment-tools-12214" class="comment-tools"></div><div class="clear"></div><div id="comment-12214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12216"></span>

<div id="answer-container-12216" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12216-score" class="post-score" title="current number of votes">0</div><span id="post-12216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The X540 T2 adapter has two ports. Are you sure you send the packet to the port where wireshark is capturing?<br />
</p><p>Wireshark &gt;= 1.7 is able to capture on multiple interfaces. Can you try that?</p><p>Do you see the packet off-box (at a mirror/monitor port of a switch)? If you do see the packet off-box it might be some driver problem.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 16:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-12216" class="comments-container"></div><div id="comment-tools-12216" class="comment-tools"></div><div class="clear"></div><div id="comment-12216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

