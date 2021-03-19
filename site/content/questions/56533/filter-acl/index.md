+++
type = "question"
title = "filter ACL"
description = '''Hi dear, i am having some kind of troubling to figure out a solution, i cannot identify in which equipment my network is allowing some desktop to access another network, so probably the other technichian did an ACL in some device, i was wondering if i can capture the packet goes to another network a...'''
date = "2016-10-20T05:15:00Z"
lastmod = "2016-10-20T12:58:00Z"
weight = 56533
keywords = [ "filter", "acl" ]
aliases = [ "/questions/56533" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [filter ACL](/questions/56533/filter-acl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56533-score" class="post-score" title="current number of votes">0</div><span id="post-56533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi dear,</p><p>i am having some kind of troubling to figure out a solution, i cannot identify in which equipment my network is allowing some desktop to access another network, so probably the other technichian did an ACL in some device, i was wondering if i can capture the packet goes to another network and find where the ACL is being allowing it by wireshark.</p><p>Att,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-acl" rel="tag" title="see questions tagged &#39;acl&#39;">acl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '16, 05:15</strong></p><img src="https://secure.gravatar.com/avatar/712e9fe6833029010906fabad50e7cb9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bruno%20trombim&#39;s gravatar image" /><p><span>bruno trombim</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bruno trombim has no accepted answers">0%</span></p></div></div><div id="comments-container-56533" class="comments-container"></div><div id="comment-tools-56533" class="comment-tools"></div><div class="clear"></div><div id="comment-56533-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56541"></span>

<div id="answer-container-56541" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56541-score" class="post-score" title="current number of votes">0</div><span id="post-56541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on two things:</p><ul><li><p>how verbose the firewall device is,</p></li><li><p>how easy it is for you to capture at different points of your network topology.</p></li></ul><p>Assuming we talk about protocols using TCP as transport (http, https, telnet, ssh, ...):</p><p>If the firewall device sends back to the desktop an ICMP "destination unreachable" when it bans the SYN packet, it is easier for you because the ICMP packet's source IP address identifies the firewalling box.</p><p>So try to capture at the desktop's LAN interface and see whether there are ICMP packets coming back to your SYN attempts towards the ACLed network. If they are, you've got it.</p><p>If the firewall device imitates a no response situation, you cannot identify it by capturing traffic at the desktop which has been banned access to the other network because the firewall won't send anything back in response to the TCP SYN packet sent by the desktop. So in this case, you would have to know the complete route from the desktop to your site uplink and capture at the "inner" and "outer" side of each box along that route to see whether the SYN packet make it from the inner side to the outer side of the box. The box which did not let the SYN through is the firewall. But if you have access rights to the routers and understand their configuration, it is usually a lot easier to check the configurations than to run all over the site capturing.</p><p>If we talk about other transports, the situation is essentially the same, except that you look for handling of some other initial packet whose role in that connection protocol is similar to that of TCP SYN.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '16, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56541" class="comments-container"><span id="56543"></span><div id="comment-56543" class="comment"><div id="post-56543-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sindy,</p><p>i got your ideia, thinking out the box !!! for example if wanna a full package information such as (IP,GW, and also which acl was applied on it is that possible through wireshark )?</p><p>THanks</p></div><div id="comment-56543-info" class="comment-info"><span class="comment-age">(20 Oct '16, 10:45)</span> <span class="comment-user userinfo">bruno trombim</span></div></div><span id="56545"></span><div id="comment-56545" class="comment"><div id="post-56545-score" class="comment-score"></div><div class="comment-text"><blockquote><p>if I wanna a full package information such as (IP, GW, and also which acl was applied on it) is that possible through wireshark ?</p></blockquote><p>Wireshark only shows you information from the packets which were physically sent over the network.</p><p>So if the firewall device sends back an ICMP packet "destination unreachable":</p><ul><li><p>you would see the IP of the firewall device, it would be the source address of that ICMP packet.</p></li><li><p>you wouldn't see the IP address of the GW anywhere because it is somehow completely out of the context. The firewall may be in another IP subnet than the desktop from which the banned packet was sent, and you have to consult the desktop's routing table to find out which gateway is used when sending packets to the final destination. The firewall is somewhere on the path between that gateway and the final destination, and it is even possible that the gateway towards the firewall's own IP is a different one than the gateway towards the final destination if the desktop has more than one gateway configured.</p></li><li><p>you won't see which ACL inside the firewall was the reason of the packet rejection because it is an internal matter of the firewall and no information field of the ICMP protocol is foreseen to convey such information.</p></li></ul><p>If the firewall device does not send back any ICMP and drops the packets silently, you won't see even its IP in the capture taken at the desktop and you will have to capture hop by hop as I've already written before.</p></div><div id="comment-56545-info" class="comment-info"><span class="comment-age">(20 Oct '16, 12:58)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-56541" class="comment-tools"></div><div class="clear"></div><div id="comment-56541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

