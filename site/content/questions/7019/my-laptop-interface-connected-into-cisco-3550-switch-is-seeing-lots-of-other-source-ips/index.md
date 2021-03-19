+++
type = "question"
title = "My Laptop interface connected into Cisco 3550 switch is seeing lots of other Source IP&#x27;s"
description = '''I ran a 2 minute capture and I see many other IP&#x27;s TCP traffic (source &amp;amp; destination). My understanding is I should only see my own laptops IP traffic and maybe broadcast traffic. We have 12 switches all plugged into a Cisco 6506 backbone. When I plug directly into other switches I also see othe...'''
date = "2011-10-21T05:36:00Z"
lastmod = "2011-10-22T21:58:00Z"
weight = 7019
keywords = [ "interface", "seeing", "other", "traffic", "source" ]
aliases = [ "/questions/7019" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [My Laptop interface connected into Cisco 3550 switch is seeing lots of other Source IP's](/questions/7019/my-laptop-interface-connected-into-cisco-3550-switch-is-seeing-lots-of-other-source-ips)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7019-score" class="post-score" title="current number of votes">0</div><span id="post-7019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I ran a 2 minute capture and I see many other IP's TCP traffic (source &amp; destination). My understanding is I should only see my own laptops IP traffic and maybe broadcast traffic. We have 12 switches all plugged into a Cisco 6506 backbone. When I plug directly into other switches I also see other IP's TCP traffic. Any help would be appreciated. One thing I have read is mac address table may be full. I have checked the switch I am in and it had only 147 addresses. Maybe the backbones mac address table is full??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-seeing" rel="tag" title="see questions tagged &#39;seeing&#39;">seeing</span> <span class="post-tag tag-link-other" rel="tag" title="see questions tagged &#39;other&#39;">other</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '11, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/87809dc43debeb1ce0293833498029d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Forst&#39;s gravatar image" /><p><span>Forst</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Forst has no accepted answers">0%</span></p></div></div><div id="comments-container-7019" class="comments-container"></div><div id="comment-tools-7019" class="comment-tools"></div><div class="clear"></div><div id="comment-7019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7020"></span>

<div id="answer-container-7020" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7020-score" class="post-score" title="current number of votes">0</div><span id="post-7020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To see other IP's as source should not be alarming, as long as they send broadcast and multicast traffic. If you see the IP of other systems as destination in a unicast packet, that indicates flooding.</p><p>Flooding occurs when a switch does not know where to send the traffic. That can be caused by a full table, which is not the case in your case. It could also be caused by asymmetric routing. Also Microsoft Network Loadbalancing is a notorious source for flooding.</p><p>So have a good look at the mac and ip addresses of the traffic you did not expect to find out the cause.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '11, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7020" class="comments-container"><span id="7034"></span><div id="comment-7034" class="comment"><div id="post-7034-score" class="comment-score"></div><div class="comment-text"><p>I do see that a lot of the traffic is MS-NLB_VirtServer_0a:00,etc. And we do have 2 sets of servers running unicast load balancing with dual nics plugged directly into the Cisco 6506 Switch. Could this be the cause and what recommendations? I have read to put load balanced servers into a hub and plug the hub into the switch...</p></div><div id="comment-7034-info" class="comment-info"><span class="comment-age">(21 Oct '11, 13:22)</span> <span class="comment-user userinfo">Forst</span></div></div><span id="7045"></span><div id="comment-7045" class="comment"><div id="post-7045-score" class="comment-score"></div><div class="comment-text"><p>That MS-NLB_VirtServer is simply the probe/heartbeat packets used by the load-balancing drive to make sure the which interfaces are working, and to allow load-balancing not to break the network. I don't see any reason why MS load-balancing shouldn't work with a switch directly - people don't make hubs these days.</p><p>That said, I assume you know that almost no real people actually use MS load-balancing in the enterprise? Most that I have heard that implement it regret it (though not sure of the real reasons to be honest) I would strongly recommend something like a F5 LTM instead</p></div><div id="comment-7045-info" class="comment-info"><span class="comment-age">(22 Oct '11, 21:58)</span> <span class="comment-user userinfo">martyvis</span></div></div></div><div id="comment-tools-7020" class="comment-tools"></div><div class="clear"></div><div id="comment-7020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

