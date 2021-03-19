+++
type = "question"
title = "Identifying the IP/Subnet Mask in Attack Traffic"
description = '''Hey everyone - question for you: I have a VoIP switch that is the subject of frequent attacks (registration/login types). I am able to identify the source IP address of the attacker with Wireshark, and then block that address with our edge Cisco 2811 router using an access list. Simple enough. The p...'''
date = "2014-07-08T09:55:00Z"
lastmod = "2014-07-08T11:31:00Z"
weight = 34473
keywords = [ "subnet", "attack", "mask", "ip" ]
aliases = [ "/questions/34473" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Identifying the IP/Subnet Mask in Attack Traffic](/questions/34473/identifying-the-ipsubnet-mask-in-attack-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34473-score" class="post-score" title="current number of votes">0</div><span id="post-34473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey everyone - question for you: I have a VoIP switch that is the subject of frequent attacks (registration/login types). I am able to identify the source IP address of the attacker with Wireshark, and then block that address with our edge Cisco 2811 router using an access list. Simple enough.</p><p>The problem comes in when the attack changes IP addresses after the previous one has been blocked, ie: 162.130.100.5 gets blocked via an ACL, then the attack starts back up with 162.130.100.30, and so on.</p><p>If I could identify the subnet mask (CIDR notation) that is sent with the packet, I could effectively block the range that is associated with that IP without having to block on an almost classful boundary (ie: deny ip 162.130.x.x 0.0.255.255). I would prefer to be specific with the ACL and only block the IP range that is generating the attack.</p><p>I have not been able to find a way with Wireshark to identify BOTH the IP address and the associated mask length, which should be included with the packet. I am a novice Wireshark user, so I could be missing something very simple.<br />
</p><p>Is this possible? Any feedback/assistance would be appreciated.</p><p>Thank you!!</p><p>Twitch</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-subnet" rel="tag" title="see questions tagged &#39;subnet&#39;">subnet</span> <span class="post-tag tag-link-attack" rel="tag" title="see questions tagged &#39;attack&#39;">attack</span> <span class="post-tag tag-link-mask" rel="tag" title="see questions tagged &#39;mask&#39;">mask</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '14, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/ee649a8f5791d9348601b7a761ef4fdc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Twitch&#39;s gravatar image" /><p><span>Twitch</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Twitch has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-34473" class="comments-container"></div><div id="comment-tools-34473" class="comment-tools"></div><div class="clear"></div><div id="comment-34473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34474"></span>

<div id="answer-container-34474" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34474-score" class="post-score" title="current number of votes">1</div><span id="post-34474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>If I could identify the <strong>subnet mask</strong> (CIDR notation) <strong>that is sent</strong> with the packet,</p></blockquote><p>the netmask is just a logical construct to allow routing and other stuff done on every system with an IP stack. Hence, the netmask itself is never sent in an IP packet, unless any upper layer protocol includes the netmask in the payload for whatever reason.</p><p>In your case, there is no way to find the netmask in the traffic itself. All you can do is a WHOIS query for that IP address and then block either the whole registered range or only parts of it, if it is a large block.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '14, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34474" class="comments-container"></div><div id="comment-tools-34474" class="comment-tools"></div><div class="clear"></div><div id="comment-34474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

