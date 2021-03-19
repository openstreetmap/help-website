+++
type = "question"
title = "How can I capture, on a switched network, unicast packets to a specific IP address ?"
description = '''The network environment is a common star network with network switch (not hub). I need to capture the packets that to a specific IP address from anywhere (e.g. any PC to PC01) I&#x27;ve a computer that connected to a normal switch port (not management port) has wireshark installed (e.g. PC02) What I need...'''
date = "2015-10-06T20:47:00Z"
lastmod = "2015-10-06T21:58:00Z"
weight = 46384
keywords = [ "unicast", "capture", "packet", "switchednetwork" ]
aliases = [ "/questions/46384" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I capture, on a switched network, unicast packets to a specific IP address ?](/questions/46384/how-can-i-capture-on-a-switched-network-unicast-packets-to-a-specific-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46384-score" class="post-score" title="current number of votes">0</div><span id="post-46384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The network environment is a common star network with network switch (not hub). I need to capture the packets that to a specific IP address from anywhere (e.g. any PC to PC01) I've a computer that connected to a normal switch port (not management port) has wireshark installed (e.g. PC02)</p><p>What I need is use this PC02 to capture all traffic that the destination is PC01 and the source is from anywhere. How can I make it ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unicast" rel="tag" title="see questions tagged &#39;unicast&#39;">unicast</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-switchednetwork" rel="tag" title="see questions tagged &#39;switchednetwork&#39;">switchednetwork</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '15, 20:47</strong></p><img src="https://secure.gravatar.com/avatar/533f79d69c580af147a7526f8e821f50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DHL&#39;s gravatar image" /><p><span>DHL</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DHL has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Oct '15, 23:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-46384" class="comments-container"></div><div id="comment-tools-46384" class="comment-tools"></div><div class="clear"></div><div id="comment-46384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46385"></span>

<div id="answer-container-46385" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46385-score" class="post-score" title="current number of votes">0</div><span id="post-46385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If I were you, I would start here:<br />
<a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '15, 21:18</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></p></div></div><div id="comments-container-46385" class="comments-container"><span id="46386"></span><div id="comment-46386" class="comment"><div id="post-46386-score" class="comment-score"></div><div class="comment-text"><p>hello Christian, I read that page before. And seems that the most feasible way is Switch + Monitor port. But not every switch has monitor port.</p></div><div id="comment-46386-info" class="comment-info"><span class="comment-age">(06 Oct '15, 21:36)</span> <span class="comment-user userinfo">DHL</span></div></div><span id="46387"></span><div id="comment-46387" class="comment"><div id="post-46387-score" class="comment-score"></div><div class="comment-text"><p>Yes, that is right. It is a special function of a switch. The alternative is to use a tap. For more precision you need a tap.</p></div><div id="comment-46387-info" class="comment-info"><span class="comment-age">(06 Oct '15, 21:58)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-46385" class="comment-tools"></div><div class="clear"></div><div id="comment-46385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

