+++
type = "question"
title = "monitoring the WAN port of a router"
description = '''I have the following setup: a router connected to a few wireless and wired computer a hub:  connected to the modem on port1 connected to the WAN port of the router on port2 connected to a PC running wireshark on port3.  I was expecting to see the traffic of my internet connection on the PC running w...'''
date = "2012-03-05T10:21:00Z"
lastmod = "2012-03-06T05:51:00Z"
weight = 9364
keywords = [ "router", "monitoring" ]
aliases = [ "/questions/9364" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [monitoring the WAN port of a router](/questions/9364/monitoring-the-wan-port-of-a-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9364-score" class="post-score" title="current number of votes">0</div><span id="post-9364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the following setup: a router connected to a few wireless and wired computer a hub:</p><ul><li>connected to the modem on port1</li><li>connected to the WAN port of the router on port2</li><li>connected to a PC running wireshark on port3.</li></ul><p>I was expecting to see the traffic of my internet connection on the PC running wireshark, but instead all I see is a bunch of DHCP protocol packets... is my setup wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span> <span class="post-tag tag-link-monitoring" rel="tag" title="see questions tagged &#39;monitoring&#39;">monitoring</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '12, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/26beadcd7dc41269e2ef7dd0116069e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gamba&#39;s gravatar image" /><p><span>gamba</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gamba has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Mar '12, 10:23</strong> </span></p></div></div><div id="comments-container-9364" class="comments-container"></div><div id="comment-tools-9364" class="comment-tools"></div><div class="clear"></div><div id="comment-9364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9366"></span>

<div id="answer-container-9366" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9366-score" class="post-score" title="current number of votes">2</div><span id="post-9366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gamba has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A couple of possibilities come to mind:</p><p>First, make sure you're capturing in promiscuous mode. That setting is found in the Capture Options dialog.</p><p>Second, your "hub" might really be a switch. Some devices marketed as hubs are really switches. If you have a switch, find out if your switch does port mirroring, and if so, mirror either port 1 or port 2 to port 3. If your switch does not do port mirroring, replace it with one that does.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '12, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-9366" class="comments-container"><span id="9392"></span><div id="comment-9392" class="comment"><div id="post-9392-score" class="comment-score"></div><div class="comment-text"><p>thank you. turns out the device marked as "hub" wa not a hub after all.</p></div><div id="comment-9392-info" class="comment-info"><span class="comment-age">(06 Mar '12, 05:51)</span> <span class="comment-user userinfo">gamba</span></div></div></div><div id="comment-tools-9366" class="comment-tools"></div><div class="clear"></div><div id="comment-9366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

