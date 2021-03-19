+++
type = "question"
title = "TCP Out of Order packets"
description = '''We have sites that homed to the hub for resources and users are experiencing slowness. Captured traffic on both end hosts and receiver is getting lots of out of order packets based on the Wireshark analysis. However, UDP traffic such as VTC is not affected. Captured the UDP traffic from both ends an...'''
date = "2016-05-03T13:31:00Z"
lastmod = "2016-05-03T13:41:00Z"
weight = 52191
keywords = [ "of", "tcp-out-of-order", "out" ]
aliases = [ "/questions/52191" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Out of Order packets](/questions/52191/tcp-out-of-order-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52191-score" class="post-score" title="current number of votes">0</div><span id="post-52191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have sites that homed to the hub for resources and users are experiencing slowness. Captured traffic on both end hosts and receiver is getting lots of out of order packets based on the Wireshark analysis. However, UDP traffic such as VTC is not affected. Captured the UDP traffic from both ends and the IP ID numbers all matched. From info provided from the network group, no load balancer is in place, routing, LAN and QOS checks out. There is firewall used in the network and traffic is GRE. Not sure why TCP traffic is affected and not UDP.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-of" rel="tag" title="see questions tagged &#39;of&#39;">of</span> <span class="post-tag tag-link-tcp-out-of-order" rel="tag" title="see questions tagged &#39;tcp-out-of-order&#39;">tcp-out-of-order</span> <span class="post-tag tag-link-out" rel="tag" title="see questions tagged &#39;out&#39;">out</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '16, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/9d629f265392eaf7b61f921e25f9f730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws2006&#39;s gravatar image" /><p><span>ws2006</span><br />
<span class="score" title="1 reputation points">1</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws2006 has no accepted answers">0%</span></p></div></div><div id="comments-container-52191" class="comments-container"></div><div id="comment-tools-52191" class="comment-tools"></div><div class="clear"></div><div id="comment-52191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52192"></span>

<div id="answer-container-52192" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52192-score" class="post-score" title="current number of votes">0</div><span id="post-52192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Could it be that the UDP packets are shorter then the TCP packets? So maybe the firewall blocks the ICMP packets for the Path MTU Discovery process?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '16, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-52192" class="comments-container"></div><div id="comment-tools-52192" class="comment-tools"></div><div class="clear"></div><div id="comment-52192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

