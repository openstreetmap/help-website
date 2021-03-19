+++
type = "question"
title = "TCP package loss? via VPN connection"
description = '''I am testing connecting a outside computer via vpn to my network and log in a softphone software. The connection is made through port 1500 on the server (172.24.7.12).  When you do the vpn connection the router gives you a fixed internal ip (configurable on the router).  Weird problem when i log int...'''
date = "2015-11-19T06:21:00Z"
lastmod = "2015-11-19T09:32:00Z"
weight = 47747
keywords = [ "vpn", "wireshark", "tcp", "packetloss" ]
aliases = [ "/questions/47747" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP package loss? via VPN connection](/questions/47747/tcp-package-loss-via-vpn-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47747-score" class="post-score" title="current number of votes">0</div><span id="post-47747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am testing connecting a outside computer via vpn to my network and log in a softphone software. The connection is made through port 1500 on the server (172.24.7.12).</p><p>When you do the vpn connection the router gives you a fixed internal ip (configurable on the router).</p><p>Weird problem when i log into the vpn with the ip 172.24.4.2 (and only this ip) the host packets get lost somewhere in the network , i see in wireshark that it doesn't receive all the ACK and etc necessary for the connection. Sometimes it doesn't receive anything at all even though i can ping with no problem (i see the ICMP in wireshark) but it doesn't show anything in port 1500. And other times it just connects OK with no problems it seems completely random..</p><p>This only happens when i use this specific ip if i use per example 172.24.4.3 all works fine.</p><p>Anyone has any ideia what it might be? If you need i can try to collect and share the wireshark entries of several tries.</p><p>If it's to complicated it's ok i've already busted my head trying to figuring this out i think i'm just going to ignore this problem and never use that IP :,D</p><p>EDIT: btw i've checked every place the packets go through and they should get the same "treatement" if they come from 172.24.4.2 or 172.24.4.3</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-packetloss" rel="tag" title="see questions tagged &#39;packetloss&#39;">packetloss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '15, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/36cb692941623bcbdcc3caad04392af2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mike3645&#39;s gravatar image" /><p><span>mike3645</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mike3645 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Nov '15, 06:23</strong> </span></p></div></div><div id="comments-container-47747" class="comments-container"></div><div id="comment-tools-47747" class="comment-tools"></div><div class="clear"></div><div id="comment-47747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47762"></span>

<div id="answer-container-47762" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47762-score" class="post-score" title="current number of votes">0</div><span id="post-47762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Weird problem when i log into the vpn with the ip 172.24.4.2<br />
This only happens when i use this specific ip if i use per example 172.24.4.3 all works fine.</p></blockquote><p>Sounds like there is a route on either your VPN gateway or on the internal system for <strong>172.24.4.2</strong>, or either one of these two (internal system or VPN gateway) has this IP address configured as secondary or on a second interface. Did you check that?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '15, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-47762" class="comments-container"></div><div id="comment-tools-47762" class="comment-tools"></div><div class="clear"></div><div id="comment-47762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

