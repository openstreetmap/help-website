+++
type = "question"
title = "mac behind a router"
description = '''I have data captured from the WAN port of my router. is it possible to filter the data based on the MAC addresses of the computers using the router? is that information present in the packet? obviously, all the packets now have the MAC of the router itself.'''
date = "2012-03-06T06:37:00Z"
lastmod = "2012-03-07T05:12:00Z"
weight = 9393
keywords = [ "router", "monitoring", "mac-address" ]
aliases = [ "/questions/9393" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [mac behind a router](/questions/9393/mac-behind-a-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9393-score" class="post-score" title="current number of votes">0</div><span id="post-9393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have data captured from the WAN port of my router. is it possible to filter the data based on the MAC addresses of the computers using the router? is that information present in the packet? obviously, all the packets now have the MAC of the router itself.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span> <span class="post-tag tag-link-monitoring" rel="tag" title="see questions tagged &#39;monitoring&#39;">monitoring</span> <span class="post-tag tag-link-mac-address" rel="tag" title="see questions tagged &#39;mac-address&#39;">mac-address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '12, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/26beadcd7dc41269e2ef7dd0116069e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gamba&#39;s gravatar image" /><p><span>gamba</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gamba has no accepted answers">0%</span></p></div></div><div id="comments-container-9393" class="comments-container"></div><div id="comment-tools-9393" class="comment-tools"></div><div class="clear"></div><div id="comment-9393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="9399"></span>

<div id="answer-container-9399" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9399-score" class="post-score" title="current number of votes">2</div><span id="post-9399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, the MAC address of a computer on the LAN side of the router is not present in the packets on the WAN side. If your router is doing NAT, then the LAN side IP address is not present either.</p><p>Some port-mirroring switches will allow you to mirror multiple source ports to a single destination port, so you could consider mirroring all the LAN ports to your Wireshark port, instead of the WAN port.</p><p>Obviously if you mirror four source ports to a single destination port, you can overwhelm the destination port if all of the source ports are passing traffic at or near their maximum rate, but this may not be a problem, depending on the traffic levels in your LAN. You could also mirror one LAN port at a time, and then change the mirroring as needed, although this will not allow simultaneous capture from all the LAN PCs.</p><p>Using this setup, you will capture local LAN traffic as well as traffic to and from the Internet, but you could filter on the router's MAC address to limit the capture, or display, to only traffic to or from the Internet.</p><p>This will show you all traffic <em>through</em> the router, but it will not show traffic arriving on the WAN side that gets dropped by the router, which may be the case if your router has firewall capabilities.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '12, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-9399" class="comments-container"></div><div id="comment-tools-9399" class="comment-tools"></div><div class="clear"></div><div id="comment-9399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9398"></span>

<div id="answer-container-9398" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9398-score" class="post-score" title="current number of votes">0</div><span id="post-9398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, it's not present in the packet; you'd have to capture on the LAN side of the router, or filter based on the IP (or other network-layer) address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '12, 09:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9398" class="comments-container"></div><div id="comment-tools-9398" class="comment-tools"></div><div class="clear"></div><div id="comment-9398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9419"></span>

<div id="answer-container-9419" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9419-score" class="post-score" title="current number of votes">0</div><span id="post-9419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Router is a Layer 3 it would only pass IP packets and would not pass any Layer 2 info(MAC) on the other side (WAN-to-LAN).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '12, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/8201e27177d7d4c609adb9a62e18ea6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pfu&#39;s gravatar image" /><p><span>pfu</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pfu has no accepted answers">0%</span></p></div></div><div id="comments-container-9419" class="comments-container"></div><div id="comment-tools-9419" class="comment-tools"></div><div class="clear"></div><div id="comment-9419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

