+++
type = "question"
title = "Keep doing TCP Retransmission with ACK, PSH"
description = '''Hello everyone, here is my situation: I got two servers, a loadbalancer (prowered by softlayer) and a web server running apache 2.2 and php 5.4. My web application only serve android mobile device. I was tested 2 set of server setting: Setting A: traffic directly point to web server Setting B: web s...'''
date = "2014-04-15T00:21:00Z"
lastmod = "2014-04-15T00:21:00Z"
weight = 31819
keywords = [ "apache", "tcpflags", "tcp" ]
aliases = [ "/questions/31819" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Keep doing TCP Retransmission with ACK, PSH](/questions/31819/keep-doing-tcp-retransmission-with-ack-psh)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31819-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone, here is my situation: I got two servers, a loadbalancer (prowered by softlayer) and a web server running apache 2.2 and php 5.4. My web application only serve android mobile device. I was tested 2 set of server setting: Setting A: traffic directly point to web server Setting B: web server as a node of the loadbalancer, and traffic is pointed to the loadbalancer</p><p>For Setting A, everything seems alright, packet have not lost and 3 way hand shark and connection close is done properly. However, for setting B, connection seems unstable, some request have [TCP Retransmission] with ACK + PSH flag. After 4-5 time TCP Retransmision (average took 40 second), the connection establish and data are sent.</p><p>What possible makes the client keep sending ACK + PSH? Please help.</p></div><div id="question-tags" class="tags-container tags">apache tcpflags tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '14, 00:21</strong></p><img src="https://secure.gravatar.com/avatar/4f0d0d50b4ca6652f6c4f9fb410aa1a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chrislaw&#39;s gravatar image" /><p>chrislaw<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chrislaw has no accepted answers">0%</span></p></div></div><div id="comments-container-31819" class="comments-container"></div><div id="comment-tools-31819" class="comment-tools"></div><div class="clear"></div><div id="comment-31819-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

