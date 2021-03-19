+++
type = "question"
title = "PLC tcp com to RFID Keepalive"
description = '''Hi everybody. I&#x27;m struggling to debug a communication between a AB plc and a feig RFID reader. I&#x27;m trying to monitor the keep alive communication frames from a computer with wire shark connected to a hub between the PLC and the reader. But I only see the Creation of the socket... If I communicate th...'''
date = "2016-08-23T13:45:00Z"
lastmod = "2016-08-24T01:21:00Z"
weight = 55082
keywords = [ "plc", "tcp", "keepalive" ]
aliases = [ "/questions/55082" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PLC tcp com to RFID Keepalive](/questions/55082/plc-tcp-com-to-rfid-keepalive)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55082-score" class="post-score" title="current number of votes">0</div><span id="post-55082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody.</p><p>I'm struggling to debug a communication between a AB plc and a feig RFID reader.</p><p>I'm trying to monitor the keep alive communication frames from a computer with wire shark connected to a hub between the PLC and the reader. But I only see the Creation of the socket...</p><p>If I communicate thru the pc interface where wire shark is recording to the reader I can see the keep alive frame. My aim is to determine which one of the Plc or the feig reader stops first to send the keep alive frames</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-plc" rel="tag" title="see questions tagged &#39;plc&#39;">plc</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-keepalive" rel="tag" title="see questions tagged &#39;keepalive&#39;">keepalive</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '16, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/830c333d9543fe3b12339be6f76904b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mikron&#39;s gravatar image" /><p><span>Mikron</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mikron has no accepted answers">0%</span></p></div></div><div id="comments-container-55082" class="comments-container"></div><div id="comment-tools-55082" class="comment-tools"></div><div class="clear"></div><div id="comment-55082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55087"></span>

<div id="answer-container-55087" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55087-score" class="post-score" title="current number of votes">0</div><span id="post-55087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your hub is not a hub, but a switch. Therefore, once it learns the MAC addresses of the nodes involved the Ethernet frames only go between these ports, not the one you capture on. Get a <a href="https://wiki.wireshark.org/SwitchReference">proper switch</a> with monitor port to capture this traffic, e.g. a network tap from dualcomm.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '16, 23:31</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55087" class="comments-container"><span id="55088"></span><div id="comment-55088" class="comment"><div id="post-55088-score" class="comment-score"></div><div class="comment-text"><p>i used Center COM MR820TR Multiport Micro hub/repeater witch is a HUB i assume? Can't i do this with a hub?</p></div><div id="comment-55088-info" class="comment-info"><span class="comment-age">(24 Aug '16, 00:48)</span> <span class="comment-user userinfo">Mikron</span></div></div><span id="55089"></span><div id="comment-55089" class="comment"><div id="post-55089-score" class="comment-score"></div><div class="comment-text"><p>Make a test - if you have a LAN connection to the internet, connect one PC to it via the maybe-hub, use another PC to capture, and generate some traffic (open a web page). If you can see many packets in both directions, your device is a real hub and your issue comes from something else; if you can see just a single packet in each direction, it is a switch and you'll have to use something else.</p><p>If you don't have a LAN connection to the internet, try two PCs talking to each other (if both run Windows, it should be possible so set up at least a remote desktop session between them, if there is linux on at least one of them, ssh, telnet, ftp, ... should be fine) and use a third PC to capture that traffic.</p></div><div id="comment-55089-info" class="comment-info"><span class="comment-age">(24 Aug '16, 01:21)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-55087" class="comment-tools"></div><div class="clear"></div><div id="comment-55087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

