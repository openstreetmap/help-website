+++
type = "question"
title = "iSCSI troubleshooting help"
description = '''Currently, I am troubleshooting a iSCSI performance issue which looks like is a buffer capacity issue on my switches. I see messages on my captures which have &quot;TCP Dup ACK&quot; and &quot;TCP Previous segment not captured&quot;. My environment consists of vmware hypervisor using software iscsi initiators connectin...'''
date = "2013-04-05T11:30:00Z"
lastmod = "2013-04-11T14:21:00Z"
weight = 20120
keywords = [ "iscsi" ]
aliases = [ "/questions/20120" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [iSCSI troubleshooting help](/questions/20120/iscsi-troubleshooting-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20120-score" class="post-score" title="current number of votes">0</div><span id="post-20120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Currently, I am troubleshooting a iSCSI performance issue which looks like is a buffer capacity issue on my switches. I see messages on my captures which have "TCP Dup ACK" and "TCP Previous segment not captured". My environment consists of vmware hypervisor using software iscsi initiators connecting over a low-end catalyst 2960S switch to VNX SAN.</p><p>What I would like to determine from my captures is getting a metric of when packets start to drop. Are there any good guidelines when troubleshooting iSCSI connectivity to determine this. Cisco does not publish buffer sizes for their low-end switches but I can see from snmp monitoring that there are huge buffer misses and a lot of output drops on the interfaces connected to the SAN.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iscsi" rel="tag" title="see questions tagged &#39;iscsi&#39;">iscsi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '13, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/fa31430640237bf40c559c5bc4a3efee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ytek&#39;s gravatar image" /><p><span>ytek</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ytek has no accepted answers">0%</span></p></div></div><div id="comments-container-20120" class="comments-container"></div><div id="comment-tools-20120" class="comment-tools"></div><div class="clear"></div><div id="comment-20120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20219"></span>

<div id="answer-container-20219" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20219-score" class="post-score" title="current number of votes">0</div><span id="post-20219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>"TCP Dup ACK" and "TCP Previous segment not captured".</p></blockquote><p>That might be a sign for dropped packets. However, to be sure where the packet loss takes place, you need to capture in front of the server <strong>and</strong> in front of the client at the same time (two capturing machines). After that you can compare the two capture files to find any differences (packet loss).</p><p>However, as a first start you could use this display filter:</p><blockquote><p><code>tcp.analysis.lost_segment or tcp.analysis.duplicate_ack</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '13, 16:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-20219" class="comments-container"><span id="20341"></span><div id="comment-20341" class="comment"><div id="post-20341-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the advice Kurt. I actually can see that there are duplicate acks and lost segements. Given my current setup I'm only able to span the two ports to a single mirror port and then separate the captures based on source mac address. I'm exporting this view of the packets as two separate captures to compare.</p></div><div id="comment-20341-info" class="comment-info"><span class="comment-age">(11 Apr '13, 10:00)</span> <span class="comment-user userinfo">ytek</span></div></div><span id="20352"></span><div id="comment-20352" class="comment"><div id="post-20352-score" class="comment-score"></div><div class="comment-text"><blockquote><p>only able to span the two ports to a single mirror port</p></blockquote><p>well, then the packet loss might also be caused by flooding of the monitor port as too much traffic is coming from the two mirrored ports. With that setup, you will never know for sure what is causing the problem.</p><p>I would mirror just one port and then check if there is still packet loss.</p></div><div id="comment-20352-info" class="comment-info"><span class="comment-age">(11 Apr '13, 14:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20219" class="comment-tools"></div><div class="clear"></div><div id="comment-20219-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

