+++
type = "question"
title = "Multinetted Topology Question"
description = '''Load Balancer port is connected to a switch and switch in turn connected to 3 servers in 3 VLANS(VlanX,VlanY,VlanZ).The port on the loadbalancer connected to switch is multinetted(hosting all 3 subnets of Servers and a tagged port which is member of all three VLANs). If a server in VLANX needs to pi...'''
date = "2013-05-30T15:15:00Z"
lastmod = "2013-05-30T16:13:00Z"
weight = 21624
keywords = [ "topology" ]
aliases = [ "/questions/21624" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Multinetted Topology Question](/questions/21624/multinetted-topology-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21624-score" class="post-score" title="current number of votes">0</div><span id="post-21624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Load Balancer port is connected to a switch and switch in turn connected to 3 servers in 3 VLANS(VlanX,VlanY,VlanZ).The port on the loadbalancer connected to switch is multinetted(hosting all 3 subnets of Servers and a tagged port which is member of all three VLANs).</p><p>If a server in VLANX needs to ping server in VLANY then packet needs to come to loadbalancer(As LB is configured as the default gateway )and LB will route it to destination system which is in VLANY.</p><p>My Doubt is What ever port the packet came on will be send out on the same port from load balancer as all macs of VLANX,VLANY and VLANZ were learned on same port.Is there any switching/routing rule that says ingress and egress needs to be on different port.</p><p>Please clarify.Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-topology" rel="tag" title="see questions tagged &#39;topology&#39;">topology</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '13, 15:15</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-21624" class="comments-container"></div><div id="comment-tools-21624" class="comment-tools"></div><div class="clear"></div><div id="comment-21624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21625"></span>

<div id="answer-container-21625" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21625-score" class="post-score" title="current number of votes">0</div><span id="post-21625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="krishnayeddula has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A switch won't normally forward packets out the same port as it ingressed. But only if the vlan ID is the same.</p><p>In your case, you should look at the LB configuration. Some LB's (like F5 BigIP) will not forward traffic between vlans unless you set up it up yourself (forwarding virtuals on a F5 BigIP)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '13, 15:47</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21625" class="comments-container"><span id="21626"></span><div id="comment-21626" class="comment"><div id="post-21626-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sake.In this case LB supports packet forwarding between vlans.Will this configuration valid if vlan forwarding is enabled on LB?</p></div><div id="comment-21626-info" class="comment-info"><span class="comment-age">(30 May '13, 16:08)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="21627"></span><div id="comment-21627" class="comment"><div id="post-21627-score" class="comment-score">1</div><div class="comment-text"><p>Yes, this is a very common setup. A LB one-armed connected with several vlans. You might want to consider bundling two ethernet interfaces for redundancy.</p></div><div id="comment-21627-info" class="comment-info"><span class="comment-age">(30 May '13, 16:13)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-21625" class="comment-tools"></div><div class="clear"></div><div id="comment-21625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

