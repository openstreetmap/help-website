+++
type = "question"
title = "All re-transmissions coming from a single source going in one direction."
description = '''WE have a very large enterprise application located in a data-center in Boston. Users are all over the State (WAN MPLS). In analyzing a WireSherk Trace at several clients, the source of all of the transmissions was a load balancer (software CISCO 6509) that front end three Apache servers that distri...'''
date = "2013-10-02T16:52:00Z"
lastmod = "2013-10-02T16:52:00Z"
weight = 25563
keywords = [ "retransmissions" ]
aliases = [ "/questions/25563" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [All re-transmissions coming from a single source going in one direction.](/questions/25563/all-re-transmissions-coming-from-a-single-source-going-in-one-direction)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25563-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>WE have a very large enterprise application located in a data-center in Boston. Users are all over the State (WAN MPLS). In analyzing a WireSherk Trace at several clients, the source of all of the transmissions was a load balancer (software CISCO 6509) that front end three Apache servers that distribute the database request into a multi-tier environment. All the re-transmission are indeed retransmissions from this one load balance device (Cisco 6509E). The re-transmissions coming from this load-balancer represent about 1.5% of all the traffic in this capture. Does the fact that all these re-transmission are coming from a single device only and not coming back the other way mean that its the device itself rather than something along the way? If there was congestion along the way then then it would be seen in both directions.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/10-2-2013_4-24-22_PM.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '13, 16:52</strong></p><img src="https://secure.gravatar.com/avatar/16c80ca493c77f3486cbb7ff38cc5d3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoberist&#39;s gravatar image" /><p>Zoberist<br />
<span class="score" title="0 reputation points">0</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoberist has no accepted answers">0%</span></p></img></div></div><div id="comments-container-25563" class="comments-container"><span id="25573"></span><div id="comment-25573" class="comment"><div id="post-25573-score" class="comment-score">1</div><div class="comment-text"><p>Have you traced each leg between the 6509 and an example client? Does the client get the initial TCP message (and if not, between what two points in the network is it lost)? Does the client send an acknowledgement? Does the acknowledgement get to the 6509 (and if not, at what point is it lost)?</p><p>The fact that it is the one load balancer that is sending the retransmissions doesn't necessarily place the blame on the load balancer. I had a similar scenario recently actually where the cause was TCP sessions which would be completely idle without keepalives for hours, causing their sessions to clear from the state table of a firewall in between (causing retransmissions on one side when its mid-session packets were silently dropped in the middle, meanwhile the receiver never saw them).</p><p>That's just an example but the point is no, the fact that the 6509 is retransmitting doesn't mean it's the source of the problem. You need to trace it out and apply your understanding of the network topology at hand.</p></div><div id="comment-25573-info" class="comment-info"><span class="comment-age">(02 Oct '13, 21:12)</span> Quadratic</div></div><span id="25612"></span><div id="comment-25612" class="comment"><div id="post-25612-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much .... this is an excellent answer.</p></div><div id="comment-25612-info" class="comment-info"><span class="comment-age">(03 Oct '13, 16:13)</span> Zoberist</div></div></div><div id="comment-tools-25563" class="comment-tools"></div><div class="clear"></div><div id="comment-25563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

