+++
type = "question"
title = "Monitoring Group Policy Traffic on Windows while PC shuts down"
description = '''Hello, is there a way to monitor Windows Group Policy Client traffic with Wireshark, while a Windows 7 workstation is shutting down? For the past week or so, my PC has been taking a long time to shut down. A blue screen with a cursor appears after ten minutes or so, then the mysterious &quot;Please wait ...'''
date = "2015-08-27T01:56:00Z"
lastmod = "2015-08-27T04:23:00Z"
weight = 45390
keywords = [ "policy", "windows7", "client", "group" ]
aliases = [ "/questions/45390" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Monitoring Group Policy Traffic on Windows while PC shuts down](/questions/45390/monitoring-group-policy-traffic-on-windows-while-pc-shuts-down)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45390-score" class="post-score" title="current number of votes">0</div><span id="post-45390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, is there a way to monitor Windows Group Policy Client traffic with Wireshark, while a Windows 7 workstation is shutting down?</p><p>For the past week or so, my PC has been taking a long time to shut down. A blue screen with a cursor appears after ten minutes or so, then the mysterious "Please wait for the Group Policy Client..." message.</p><p>Any help would be much appreciated.</p><p>PS</p><p>This article on Internet gave me the idea of monitoring Group Policy traffic to try to pinpoint the issue causing the shutdown delay.</p><p><a href="http://trentent.blogspot.fr/2013/03/slow-group-policy-client-side.html">http://trentent.blogspot.fr/2013/03/slow-group-policy-client-side.html</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-policy" rel="tag" title="see questions tagged &#39;policy&#39;">policy</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-client" rel="tag" title="see questions tagged &#39;client&#39;">client</span> <span class="post-tag tag-link-group" rel="tag" title="see questions tagged &#39;group&#39;">group</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '15, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/efbc0d09feb29ab9c97874ef82f6b7ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phiroc&#39;s gravatar image" /><p><span>phiroc</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phiroc has no accepted answers">0%</span></p></div></div><div id="comments-container-45390" class="comments-container"></div><div id="comment-tools-45390" class="comment-tools"></div><div class="clear"></div><div id="comment-45390-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45394"></span>

<div id="answer-container-45394" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45394-score" class="post-score" title="current number of votes">0</div><span id="post-45394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately when a shutdown is commenced, user space applications get the chop first, so I don't know how long into the shutdown the capture will keep running. Maybe you could try that and report back. There are also other capturing mechanism, e.g. <a href="http://blogs.technet.com/b/yongrhee/archive/2012/12/01/network-tracing-packet-sniffing-built-in-to-windows-server-2008-r2-and-windows-server-2012.aspx">netsh trace</a> that may run a little longer. You'll have to use NetMon or Message Analyzer to convert the netsh captures to a format Wireshark can read.</p><p>Maybe you could capture the traffic externally to the machine, maybe on the DC it's communicating with, or via a mirror or span port on a switch.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '15, 04:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45394" class="comments-container"></div><div id="comment-tools-45394" class="comment-tools"></div><div class="clear"></div><div id="comment-45394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45396"></span>

<div id="answer-container-45396" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45396-score" class="post-score" title="current number of votes">0</div><span id="post-45396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, add a sniffer to your network and go ahead. See <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Capture Setup</a> instructions in the Wiki how to go about it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '15, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-45396" class="comments-container"></div><div id="comment-tools-45396" class="comment-tools"></div><div class="clear"></div><div id="comment-45396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

