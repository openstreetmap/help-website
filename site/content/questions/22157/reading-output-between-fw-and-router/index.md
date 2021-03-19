+++
type = "question"
title = "Reading output between FW and router"
description = '''We have a server looking to communicate through both a firewall and a router set up with a VPN to a remote public address on a certain port. The opposite end complains that they can send and receive traffic successfully when they initiate the connection from their end but cannot see traffic when we ...'''
date = "2013-06-19T06:54:00Z"
lastmod = "2013-06-19T10:49:00Z"
weight = 22157
keywords = [ "firewall", "source", "vpn", "destination", "nat" ]
aliases = [ "/questions/22157" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reading output between FW and router](/questions/22157/reading-output-between-fw-and-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22157-score" class="post-score" title="current number of votes">0</div><span id="post-22157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a server looking to communicate through both a firewall and a router set up with a VPN to a remote public address on a certain port. The opposite end complains that they can send and receive traffic successfully when they initiate the connection from their end but cannot see traffic when we initiate. The setup is as follows:</p><p>Server &gt; Firewall &gt; router (with IPsec VPN tunnel) &gt; Internet &lt; router (with IPsec VPN tunnel) &lt; RemoteServer</p><p>We do not have access to the local VPN router's configs so we want to make sure traffic is getting to it from our firewall properly for it to then transmit across the net to the remote end.</p><p>Lets say our server at 192.168.aaa.aa2/24 initiates the communication by sending a request to the end IP of 157.xxx.xxx.xx5 on port 32xxx. The packet's first checkpoint is the firewall, where it gets translated from the internal interface of the firewall (192.168.aaa.aa1/24) to the external interface (192.168.bbb.bb2/30) which faces the internal interface of the VPN router (192.168.bbb.bb1/30). So, with Wireshark sitting between the firewall's external interface and the VPN router's internal interface, we see traffic with a source address of 192.168.bbb.bb2 and destination address of 157.xxx.xxx.xx5, but then it gets confusing as far as ports go when we see this: 49xxx &gt; 32xxx. It's a SYN packet with the source port as 49xxx and destination port as the intended target port of the remote end which is 32xxx.</p><p>The question is, what does this mean and what should the VPN router see coming from the firewall? Is there a NAT that is not happening properly? The 49xxx number varies and I'm not sure where that number is coming from. Any assistance would help. Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-firewall" rel="tag" title="see questions tagged &#39;firewall&#39;">firewall</span> <span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span> <span class="post-tag tag-link-nat" rel="tag" title="see questions tagged &#39;nat&#39;">nat</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '13, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/728e08a274f7dbc9acfe5111f5faf55f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnnybiggles&#39;s gravatar image" /><p><span>johnnybiggles</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnnybiggles has no accepted answers">0%</span></p></div></div><div id="comments-container-22157" class="comments-container"></div><div id="comment-tools-22157" class="comment-tools"></div><div class="clear"></div><div id="comment-22157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22163"></span>

<div id="answer-container-22163" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22163-score" class="post-score" title="current number of votes">0</div><span id="post-22163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>The opposite end complains that they can send and receive traffic successfully when they initiate the connection from their end but cannot see traffic when we initiate.</p></blockquote><p>That's because of the NAT on your firewall.</p><p>Eplanation:</p><p>They connect:</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '13, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Jun '13, 07:45</strong> </span></p></div></div><div id="comments-container-22163" class="comments-container"><span id="22166"></span><div id="comment-22166" class="comment"><div id="post-22166-score" class="comment-score"></div><div class="comment-text"><p>When we spoke with them, we had them configure the VPN router to communicate with our external interface of the firewall instead of the server so it should expect traffic from that address already translated as the source. So could you explain more in detail what you mean and a possible workaround if what we have is not correct?</p></div><div id="comment-22166-info" class="comment-info"><span class="comment-age">(19 Jun '13, 07:54)</span> <span class="comment-user userinfo">johnnybiggles</span></div></div><span id="22181"></span><div id="comment-22181" class="comment"><div id="post-22181-score" class="comment-score"></div><div class="comment-text"><p>When we spoke with them, we had them configure the VPN router to communicate with our external interface of the firewall instead of the server so it should expect traffic from that address already translated as the source. So could you explain more in detail what you mean and a possible workaround if what we have is not correct?</p></div><div id="comment-22181-info" class="comment-info"><span class="comment-age">(19 Jun '13, 10:49)</span> <span class="comment-user userinfo">johnnybiggles</span></div></div></div><div id="comment-tools-22163" class="comment-tools"></div><div class="clear"></div><div id="comment-22163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

