+++
type = "question"
title = "Ports Reused / TCP Out of Order"
description = '''Hi All, I have an issue with two servers across a DMVPN. Backup software i failing. ICMP and traces all look good between them. No aysmetric routing. I ran a capture on the Core switch at one of the sites capturing traffic between the two hosts and I have attached screenshot. Anything obvious standi...'''
date = "2015-10-30T03:25:00Z"
lastmod = "2015-11-09T13:54:00Z"
weight = 47084
keywords = [ "numbers", "reused", "out-of-order", "tcp", "port" ]
aliases = [ "/questions/47084" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Ports Reused / TCP Out of Order](/questions/47084/ports-reused-tcp-out-of-order)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47084-score" class="post-score" title="current number of votes">0</div><span id="post-47084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I have an issue with two servers across a DMVPN. Backup software i failing. ICMP and traces all look good between them. No aysmetric routing. I ran a capture on the Core switch at one of the sites capturing traffic between the two hosts and I have attached screenshot. Anything obvious standing out as it looks like something is wrong, but not entirely sure what.</p><p>Many Thanks<img src="https://osqa-ask.wireshark.org/upfiles/servercap.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-numbers" rel="tag" title="see questions tagged &#39;numbers&#39;">numbers</span> <span class="post-tag tag-link-reused" rel="tag" title="see questions tagged &#39;reused&#39;">reused</span> <span class="post-tag tag-link-out-of-order" rel="tag" title="see questions tagged &#39;out-of-order&#39;">out-of-order</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '15, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/a28bceae0effe0ec1130bab7cb87a4e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="exit12&#39;s gravatar image" /><p><span>exit12</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="exit12 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-47084" class="comments-container"></div><div id="comment-tools-47084" class="comment-tools"></div><div class="clear"></div><div id="comment-47084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47383"></span>

<div id="answer-container-47383" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47383-score" class="post-score" title="current number of votes">0</div><span id="post-47383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you look at the conversation between ports 52309 (client port) and 50008 (server port), starting from 4th packet, every time the client sent a SYN (don't worry about ECN CWR flags), it got a SYNACK packet and then TCP RST packet. What's funny is that the TCP RST packet has a strange sequence number (4274946776 or 0xfece82d8).</p><ul><li>It feels like something closer to the client side blocks either the SYNACK or ACK.</li><li>server side has something entity that sent TCP RST, with wrong sequence number.</li></ul><p>If there is time information, that could be helpful.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '15, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span> </br></p></div></div><div id="comments-container-47383" class="comments-container"><span id="47398"></span><div id="comment-47398" class="comment"><div id="post-47398-score" class="comment-score"></div><div class="comment-text"><p>Did you examine the "Port Reuse" fact?</p></div><div id="comment-47398-info" class="comment-info"><span class="comment-age">(08 Nov '15, 10:14)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="47418"></span><div id="comment-47418" class="comment"><div id="post-47418-score" class="comment-score"></div><div class="comment-text"><p>Yes, saw the "Port reuse" message by Wireshark. Unclear whether it's a true "Port reuse" because don't the timing information and the absolute sequence number on TCP SYN packet.</p></div><div id="comment-47418-info" class="comment-info"><span class="comment-age">(08 Nov '15, 16:18)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="47422"></span><div id="comment-47422" class="comment"><div id="post-47422-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@pktUser1001</span>: The Question was a little bit unclear. I originally meant <span></span><span>@exit12</span>. Apologize for that. But it is unclear to me, too. Because we can see a SYN/ACK. My expactation is to see only a SYN and a RST.</p></div><div id="comment-47422-info" class="comment-info"><span class="comment-age">(08 Nov '15, 22:25)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="47434"></span><div id="comment-47434" class="comment"><div id="post-47434-score" class="comment-score"></div><div class="comment-text"><p><span>@christian_r</span> That's fine. We are on the same page that the problem (pcap snapshot) could be a little clearer :-)</p></div><div id="comment-47434-info" class="comment-info"><span class="comment-age">(09 Nov '15, 09:50)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="47439"></span><div id="comment-47439" class="comment"><div id="post-47439-score" class="comment-score"></div><div class="comment-text"><p>After reviewing the picture. I think Port Reuse is there, but it happens only as a follow up. <span></span><span>@exit12</span>: Do you have an additional Layer4 device (Loadbalancer, Firewall,...) between the server and the capture point.</p></div><div id="comment-47439-info" class="comment-info"><span class="comment-age">(09 Nov '15, 13:54)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-47383" class="comment-tools"></div><div class="clear"></div><div id="comment-47383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

