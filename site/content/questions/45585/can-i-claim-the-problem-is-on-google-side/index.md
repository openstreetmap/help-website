+++
type = "question"
title = "Can I claim the problem is on google side?"
description = '''My communication with google has some problems. I even saw some ICMP TTL expired packet (see pcap packet 37). Since my network appears to be ok (HTTP transactions to other sites), can I claim Google server is at fault? Thanks.'''
date = "2015-09-01T21:28:00Z"
lastmod = "2015-09-02T09:43:00Z"
weight = 45585
keywords = [ "wireshark" ]
aliases = [ "/questions/45585" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can I claim the problem is on google side?](/questions/45585/can-i-claim-the-problem-is-on-google-side)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45585-score" class="post-score" title="current number of votes">0</div><span id="post-45585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My communication with google has some problems. I even saw some ICMP TTL expired packet (see <a href="https://www.cloudshark.org/captures/502240438462">pcap</a> packet 37).</p><p>Since my network appears to be ok (HTTP transactions to other sites), can I claim Google server is at fault? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '15, 21:28</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-45585" class="comments-container"><span id="45591"></span><div id="comment-45591" class="comment"><div id="post-45591-score" class="comment-score"></div><div class="comment-text"><p>Can you add a traceroute to the 'offending Google host' 173.194.115.6 ?</p></div><div id="comment-45591-info" class="comment-info"><span class="comment-age">(02 Sep '15, 04:04)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-45585" class="comment-tools"></div><div class="clear"></div><div id="comment-45585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45600"></span>

<div id="answer-container-45600" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45600-score" class="post-score" title="current number of votes">0</div><span id="post-45600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Here is it (change the IP for ATT gateway for a little privacy)</p><pre><code>traceroute 173.194.115.6 
traceroute to 173.194.115.6 (173.194.115.6), 30 hops max, 60 byte packets
 1  10.0.0.1 (10.0.0.1)  1.180 ms  1.677 ms  1.671 ms
 2  192.168.1.254 (192.168.1.254)  168.293 ms  168.341 ms  168.396 ms
 3  x.y.z.w.lightspeed.austtx.sbcglobal.net (x.y.z.w)  268.932 ms  273.867 ms  283.483 ms
 4  71.149.77.146 (71.149.77.146)  168.345 ms  168.374 ms  168.497 ms
 5  * * *
 6  12.83.68.145 (12.83.68.145)  168.440 ms  24.725 ms  190.800 ms
 7  12.122.139.209 (12.122.139.209)  190.753 ms  190.808 ms  190.803 ms
 8  * * *
 9  209.85.244.162 (209.85.244.162)  190.772 ms  191.311 ms  191.427 ms
10  209.85.254.127 (209.85.254.127)  190.788 ms  190.305 ms  190.338 ms
11  dfw06s39-in-f6.1e100.net (173.194.115.6)  190.651 ms  190.679 ms  203.090 ms
[email protected]:~/Downloads$ ping 173.194.115.6
PING 173.194.115.6 (173.194.115.6) 56(84) bytes of data.
64 bytes from 173.194.115.6: icmp_req=1 ttl=53 time=10.0 ms
64 bytes from 173.194.115.6: icmp_req=2 ttl=53 time=12.8 ms
^C
--- 173.194.115.6 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 10.051/11.472/12.893/1.421 ms</code></pre><p>My laptop is connected to wireshark router (10.0.0.1) which is in turn connected to AT&amp;T residential gateway 192.168.1.254. Traceroute to 192.168.1.254 is slow (168.293 ms), but pinging it is very fast. Not sure why.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '15, 09:43</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-45600" class="comments-container"></div><div id="comment-tools-45600" class="comment-tools"></div><div class="clear"></div><div id="comment-45600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

