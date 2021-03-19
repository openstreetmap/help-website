+++
type = "question"
title = "How to to understand TCP/IP packets output?"
description = '''Hello, i hope i can find some help here. I´m working at the moment on a school project. As you can see its a TCP/IP packets output from Wireshark but i need help from you to understand the meaning, structure &amp;amp; contents. Can anyone assist? I appreciate it! Here is the output:  13:12:49.751403 arp...'''
date = "2014-11-17T03:08:00Z"
lastmod = "2014-11-17T13:35:00Z"
weight = 37898
keywords = [ "output", "packets", "tcp", "ip" ]
aliases = [ "/questions/37898" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to to understand TCP/IP packets output?](/questions/37898/how-to-to-understand-tcpip-packets-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37898-score" class="post-score" title="current number of votes">0</div><span id="post-37898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, i hope i can find some help here. I´m working at the moment on a school project. As you can see its a TCP/IP packets output from Wireshark but i need help from you to understand the meaning, structure &amp; contents. Can anyone assist? I appreciate it!</p><p>Here is the output:</p><ol><li>13:12:49.751403 arp who-has 192.168.246.13(Broadcast) tell 192.168.246.128</li><li>13:12:49.751602 arp reply 192.168.246.13is-at 00:00:01:0f:2e:7e</li><li>13:12:50.441259 IP 192.168.246.13.137 &gt; 192.168.246.128.137: UDP, length 50</li><li>13:12:50.441632 IP 192.168.246.128 &gt; 192.168.246.13: ICMP 192.168.246.128 udp port 137 unreachable, length 86</li><li>13:12:51.942563 IP 192.168.246.13.137 &gt; 192.168.246.128.137: UDP, length 50</li><li>13:12:51.943277 IP 192.168.246.128 &gt; 192.168.246.13: ICMP 192.168.246.128 udp port 137 unreachable, length 86</li><li>13:12:53.444627 IP 192.168.246.13.137 &gt; 192.168.246.128.137: UDP, length 50</li><li>13:12:53.445343 IP 192.168.246.128 &gt; 192.168.246.13: ICMP 192.168.246.128 udp port 137 unreachable, length 86</li><li>13:13:02.738990 IP 192.168.246.128.39886 &gt; 192.168.246.13.80: . ack 1611053795 win 3072</li><li>13:13:02.739053 IP 192.168.246.13.80 &gt; 192.168.246.128.39886: R 1611053795:1611053795(0) win 0</li><li>13:13:22.407445 IP 192.168.246.128.54955 &gt; 192.168.246.13.80: S 2910497703:2910497703(0) win 5840 &lt;mss 1460,sackok,timestamp="" 518611="" 0,nop,wscale="" 6=""&gt;</li><li>13:13:22.407560 IP 192.168.246.13.80 &gt; 192.168.246.128.54955: S 3762608065:3762608065(0) ack 2910497704 win 64240 &lt;mss 1460,nop,wscale="" 0,nop,nop,timestamp="" 0="" 0,nop,nop,sackok=""&gt;</li><li>13:13:22.407963 IP 192.168.246.128.54955 &gt; 192.168.246.13.80: . ack 1 win 92 &lt;nop,nop,timestamp 518611="" 0=""&gt;</li><li>13:13:22.408321 IP 192.168.246.128.54955 &gt; 192.168.246.13.80: R 1:1(0) ack 1 win 92 &lt;nop,nop,timestamp 518611="" 0=""&gt;</li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-output" rel="tag" title="see questions tagged &#39;output&#39;">output</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '14, 03:08</strong></p><img src="https://secure.gravatar.com/avatar/cb7634e4c879c2726a631cf06b124f39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kell90&#39;s gravatar image" /><p><span>Kell90</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kell90 has no accepted answers">0%</span></p></div></div><div id="comments-container-37898" class="comments-container"><span id="37904"></span><div id="comment-37904" class="comment"><div id="post-37904-score" class="comment-score"></div><div class="comment-text"><p>ok i found out to point 8 is there anyone who can help with point 9?</p></div><div id="comment-37904-info" class="comment-info"><span class="comment-age">(17 Nov '14, 10:06)</span> <span class="comment-user userinfo">Kell90</span></div></div></div><div id="comment-tools-37898" class="comment-tools"></div><div class="clear"></div><div id="comment-37898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37915"></span>

<div id="answer-container-37915" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37915-score" class="post-score" title="current number of votes">0</div><span id="post-37915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>#9 is linux sending a packet on a tcp connection that does not (no longer) exist at the server.<br />
#10 is the server sending a RST in reaction of #9 as no socket is open for this connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '14, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-37915" class="comments-container"></div><div id="comment-tools-37915" class="comment-tools"></div><div class="clear"></div><div id="comment-37915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

