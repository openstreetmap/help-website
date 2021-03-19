+++
type = "question"
title = "Out of Order packets"
description = '''Hello, I know that out of order packets have been discussed many times, but I still think there should be some way to reorder packets based on sequence and ack numbers only to make it easier to see if all packets were sent and received, and then how many were retransmitted. Yes, looking at the FINs,...'''
date = "2015-11-08T05:36:00Z"
lastmod = "2015-11-09T14:47:00Z"
weight = 47379
keywords = [ "out-of-order" ]
aliases = [ "/questions/47379" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Out of Order packets](/questions/47379/out-of-order-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47379-score" class="post-score" title="current number of votes">0</div><span id="post-47379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I know that out of order packets have been discussed many times, but I still think there should be some way to reorder packets based on sequence and ack numbers only to make it easier to see if all packets were sent and received, and then how many were retransmitted. Yes, looking at the FINs, the following ACKs, and RSTs can be a quick way to see if all packets were sent and received, but it is sometimes painfully difficult to go up and down looking at each packet's sequence and ack numbers.</p><p>Tcpdumps from firewalls and loadbalancers are always saved out of order, and worse, the orders do not match each other. This makes large captures difficult to troubleshoot by having to ignore the Wireshark warning messages about previous segment lost and acking unseen segment. Then, look at each packet up and down trying to piece together what was sent and received.</p><p>A wireshark menu option to reorder packets from the display filter based on sequence and ack numbers would be the best improvement ever.</p><p>Thanks, Tom</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-out-of-order" rel="tag" title="see questions tagged &#39;out-of-order&#39;">out-of-order</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '15, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/099d20d1756a5cbc605c8270200b6026?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomF&#39;s gravatar image" /><p><span>TomF</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomF has no accepted answers">0%</span></p></div></div><div id="comments-container-47379" class="comments-container"><span id="47381"></span><div id="comment-47381" class="comment"><div id="post-47381-score" class="comment-score"></div><div class="comment-text"><p>Do you want to be able to save a pcap with out-of-order packets into a new pcap with the packets in order (timestamp of packets may not be in order as a result) and all retransmitted packets removed?</p></div><div id="comment-47381-info" class="comment-info"><span class="comment-age">(08 Nov '15, 05:50)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-47379" class="comment-tools"></div><div class="clear"></div><div id="comment-47379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47392"></span>

<div id="answer-container-47392" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47392-score" class="post-score" title="current number of votes">1</div><span id="post-47392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Tcpdumps from firewalls and loadbalancers are always saved out of order, and worse, the orders do not match each other.</p></blockquote><p>I know that problem well and as you said, sometimes it makes troubleshooting harder.</p><blockquote><p>Then, look at each packet up and down trying to piece together what was sent and received.</p></blockquote><p>You can add a column for the IP ID (ip.id) and/or SEQ (tcp.seq) and sort the capture file according to the values of one of these columns. It will break the 'flow' of a session (req/resp), but at least it will help to compare two capture files (taken on the firewall and/or the loadbalancer).</p><blockquote><p>A wireshark menu option to reorder packets from the display filter based on sequence and ack numbers would be the best improvement ever.</p></blockquote><p>Please add a feature request to the Wireshark bug tracker.</p><blockquote><p><a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '15, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-47392" class="comments-container"><span id="47419"></span><div id="comment-47419" class="comment"><div id="post-47419-score" class="comment-score"></div><div class="comment-text"><p>Hello Kurt, Many thanks. Adding a column for Custom(tcp.seq) is a good workaround and will help.</p><p>Thanks, Tom</p></div><div id="comment-47419-info" class="comment-info"><span class="comment-age">(08 Nov '15, 19:37)</span> <span class="comment-user userinfo">TomF</span></div></div><span id="47441"></span><div id="comment-47441" class="comment"><div id="post-47441-score" class="comment-score"></div><div class="comment-text"><p>good!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-47441-info" class="comment-info"><span class="comment-age">(09 Nov '15, 14:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-47392" class="comment-tools"></div><div class="clear"></div><div id="comment-47392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

