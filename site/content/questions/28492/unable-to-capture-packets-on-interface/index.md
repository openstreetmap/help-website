+++
type = "question"
title = "Unable to capture packets on interface."
description = '''Hi I have following 3 interfaces  hduser@dn1:~$ ifconfig eth0 Link encap:Ethernet HWaddr 00:11:43:e1:79:03  inet addr:155.98.39.121 Bcast:155.98.39.255 Mask:255.255.252.0  UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1  RX packets:225209 errors:0 dropped:0 overruns:0 frame:0  TX packets:212227 err...'''
date = "2013-12-30T21:05:00Z"
lastmod = "2013-12-31T00:00:00Z"
weight = 28492
keywords = [ "traffic-analysis", "ubuntu", "networkinterfaces", "wireshark" ]
aliases = [ "/questions/28492" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to capture packets on interface.](/questions/28492/unable-to-capture-packets-on-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28492-score" class="post-score" title="current number of votes">0</div><span id="post-28492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have following 3 interfaces</p><p><span class="__cf_email__" data-cfemail="650d011016001725010b54">[email protected]</span>:~$ ifconfig eth0 Link encap:Ethernet HWaddr 00:11:43:e1:79:03 inet addr:155.98.39.121 Bcast:155.98.39.255 Mask:255.255.252.0 UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1 RX packets:225209 errors:0 dropped:0 overruns:0 frame:0 TX packets:212227 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:1000 RX bytes:211193409 (211.1 MB) TX bytes:41723043 (41.7 MB)</p><p>eth4 Link encap:Ethernet HWaddr 00:04:23:a8:fc:0e inet addr:10.10.1.1 Bcast:10.10.1.255 Mask:255.255.255.0 UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1 RX packets:14 errors:0 dropped:0 overruns:0 frame:0 TX packets:15 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:1000 RX bytes:1068 (1.0 KB) TX bytes:1266 (1.2 KB)</p><p>lo Link encap:Local Loopback inet addr:127.0.0.1 Mask:255.0.0.0 UP LOOPBACK RUNNING MTU:16436 Metric:1 RX packets:55140 errors:0 dropped:0 overruns:0 frame:0 TX packets:55140 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:0 RX bytes:14918354 (14.9 MB) TX bytes:14918354 (14.9 MB)</p><p><span class="__cf_email__" data-cfemail="90f8f4e5e3f5e2d0f4fea1">[email protected]</span>:~$</p><p>But when i start wireshark using</p><p><span class="__cf_email__" data-cfemail="2b434f5e584e596b4f451a">[email protected]</span>:~$ wireshark &amp;</p><p>A wireshark network analyser window opens , but it is not showing any interfaces to capture the traffic.</p><p>I am not running this on my local machine. This is GENI resources which i can access through ssh.</p><p>I want to capture the network traffic in eth4 . Can anyone help me on this ?</p><p>Thanks Navaz</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic-analysis" rel="tag" title="see questions tagged &#39;traffic-analysis&#39;">traffic-analysis</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-networkinterfaces" rel="tag" title="see questions tagged &#39;networkinterfaces&#39;">networkinterfaces</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '13, 21:05</strong></p><img src="https://secure.gravatar.com/avatar/7ebc4294ff0928fd4def898edda41aae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="navaz&#39;s gravatar image" /><p><span>navaz</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="navaz has no accepted answers">0%</span></p></div></div><div id="comments-container-28492" class="comments-container"></div><div id="comment-tools-28492" class="comment-tools"></div><div class="clear"></div><div id="comment-28492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28496"></span>

<div id="answer-container-28496" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28496-score" class="post-score" title="current number of votes">1</div><span id="post-28496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It seems you don't have the necessary privileges to start traces. Did you check the steps listed here <a href="http://ask.wireshark.org/questions/7523/ubuntu-machine-no-interfaces-listed">http://ask.wireshark.org/questions/7523/ubuntu-machine-no-interfaces-listed</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '13, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-28496" class="comments-container"></div><div id="comment-tools-28496" class="comment-tools"></div><div class="clear"></div><div id="comment-28496-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

