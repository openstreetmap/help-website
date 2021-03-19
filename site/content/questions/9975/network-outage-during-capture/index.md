+++
type = "question"
title = "Network outage during capture"
description = '''I have been trying to diagnose a SQL timeout issue, and started a capture on one web server tonight. 10 minutes after starting we started receiving monitoring pages and customer calls that we were offline. This issue was affecting all subnets; crossing VLANs, Cisco ASA firewalls between subnets, and...'''
date = "2012-04-05T22:44:00Z"
lastmod = "2012-04-06T04:34:00Z"
weight = 9975
keywords = [ "network", "wireshark" ]
aliases = [ "/questions/9975" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Network outage during capture](/questions/9975/network-outage-during-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9975-score" class="post-score" title="current number of votes">0</div><span id="post-9975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been trying to diagnose a SQL timeout issue, and started a capture on one web server tonight. 10 minutes after starting we started receiving monitoring pages and customer calls that we were offline. This issue was affecting all subnets; crossing VLANs, Cisco ASA firewalls between subnets, and Cisco ACE load balancers fronting a dozen web services. Various applications were unable to connect to the backend web services (through the load balancers and firewalls, with services both in the same subnet/VLAN and crossing through routers/firewalls/load balancers). As soon as we stopped capturing all issues were resolved and not recurred.</p><p>Our application logs contain many connection errors across all services (all backend services were sporadically affected); there were no errors on any switch, firewall, or load balancer; no unusual packet errors at the switches; and no server had any OS level errors (all servers are Windows 2003/2008).<br />
</p><p>I am at a loss to explain what happened; my team and our hosting provider can not identify anything after several hours of investigation. We are hosted in a highly available datacenter with all Cisco equipment installed according to industry standards; I have no reason to believe that equipment is causing our issues (and not being logged). There are no spikes in inbound or outbound traffic to explain anything nefarious or unusual traffic. The timing is too coincidental to immediately dismiss the fact that the only time the issue occured a Wireshark capture was occurring.</p><p>There is a similar post at <a href="http://ask.wireshark.org/questions/8892/wireshark-causing-network-problems">http://ask.wireshark.org/questions/8892/wireshark-causing-network-problems</a> that identifies a similar problem. Has anyone else seen a similar problem ever? We are baffled and looking for any help that may be there. (I can't do any of the suggested test in the linked post until our next maintenance window in case the capture was the cause of the problem.)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '12, 22:44</strong></p><img src="https://secure.gravatar.com/avatar/54ac4d95bfd4127123af5c826a643d2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bdstark&#39;s gravatar image" /><p><span>bdstark</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bdstark has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-9975" class="comments-container"></div><div id="comment-tools-9975" class="comment-tools"></div><div class="clear"></div><div id="comment-9975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9979"></span>

<div id="answer-container-9979" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9979-score" class="post-score" title="current number of votes">2</div><span id="post-9979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is kinda hard to tell what happened without having a look at the captured data - and maybe even that won't help since it could be the capturing machine that caused the effect. Usually when someone says that the whole network got into trouble at the same time the first thing I ask about is the spanning tree - you could look for at topology change that could explain the drastic effect in the network (the switches should be able to tell you that).</p><p>The other, more important thing I keep telling the students in my network analysis classes is this: <strong>never</strong> capture on a system that is part of the problem you want to solve. <strong>Always</strong> use a third, completely <strong>passive</strong> capture device - an additional PC or appliance, with the capture card being <strong>read-only</strong>. It is something that professinal capture cards do anyway, but which you can simulate on a normal PC NIC by removing all protocol bindings from it. That way your capture device can't interfere with anything the network does. It just listens, just like a doctor using her/his stethoscope.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '12, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Apr '12, 04:34</strong> </span></p></div></div><div id="comments-container-9979" class="comments-container"></div><div id="comment-tools-9979" class="comment-tools"></div><div class="clear"></div><div id="comment-9979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

