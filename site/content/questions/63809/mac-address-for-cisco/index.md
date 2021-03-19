+++
type = "question"
title = "MAC-address for Cisco"
description = '''So I&#x27;m trying to ping Cisco to get the MAC-address. In the Destination section I get OpenWrt.lan and a MAC-address, but in the video below it shows Ciscospv_cd instead of OpenWrt.lan. Am I doing something wrong here? The same thing happened when I tried to ping Yahoo. https://www.youtube.com/watch?v...'''
date = "2017-10-11T08:30:00Z"
lastmod = "2017-10-11T11:27:00Z"
weight = 63809
keywords = [ "ping" ]
aliases = [ "/questions/63809" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MAC-address for Cisco](/questions/63809/mac-address-for-cisco)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63809-score" class="post-score" title="current number of votes">0</div><span id="post-63809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I'm trying to ping Cisco to get the MAC-address. In the Destination section I get OpenWrt.lan and a MAC-address, but in the video below it shows Ciscospv_cd instead of OpenWrt.lan. Am I doing something wrong here? The same thing happened when I tried to ping Yahoo.</p><p><a href="https://www.youtube.com/watch?v=xVwFjH0sQUI">https://www.youtube.com/watch?v=xVwFjH0sQUI</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '17, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/8abe64dac77628fb2dd3ef96e3822589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="captainpancake133&#39;s gravatar image" /><p><span>captainpanca...</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="captainpancake133 has no accepted answers">0%</span></p></div></div><div id="comments-container-63809" class="comments-container"></div><div id="comment-tools-63809" class="comment-tools"></div><div class="clear"></div><div id="comment-63809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63815"></span>

<div id="answer-container-63815" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63815-score" class="post-score" title="current number of votes">0</div><span id="post-63815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You are about 16 minutes into this video and are asked to ping yahoo.com and cisco.com. The next question is 'what is significant about this information' and the answer is 'All MAC addresses are the same'. Now why is that? That comes from the fact that yahoo.com and cisco.com are resolving to IP addresses outside of your local network. Therefore all this ICMP packets go to your router first, and therefore it's the router MAC address you'll see.</p><p>In the presenters case, he has some Cisco device as his router, therefore sees the manufacturer name Ciscospv_cd in the MAC address, while you have a LinkSys router of some kind, therefore you see the OpenWrt.lan name.</p><p>So in short, he doesn't see the cisco.com MAC address, he sees the MAC address of his router, which happens to be a Cisco device.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '17, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-63815" class="comments-container"><span id="63816"></span><div id="comment-63816" class="comment"><div id="post-63816-score" class="comment-score"></div><div class="comment-text"><p>Got it. So in short: Pinging local IP addresses will give you the MAC-address, but pinging remote hosts won't. Am I correct on that?</p></div><div id="comment-63816-info" class="comment-info"><span class="comment-age">(11 Oct '17, 10:23)</span> <span class="comment-user userinfo">captainpanca...</span></div></div><span id="63819"></span><div id="comment-63819" class="comment"><div id="post-63819-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Pinging local IP addresses will give you the MAC-address, but pinging remote hosts won't.</p></blockquote><p>Correct, with "local" meaning "on the same LAN". If you're on a network segment that uses MAC addresses, pinging an IP address will give you the MAC address of the first host on the route to that IP address, which would be the host with that IP address if they're on the same network segment and would be a router if they're not on the same network segment.</p></div><div id="comment-63819-info" class="comment-info"><span class="comment-age">(11 Oct '17, 11:27)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-63815" class="comment-tools"></div><div class="clear"></div><div id="comment-63815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

