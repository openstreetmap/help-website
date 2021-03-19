+++
type = "question"
title = "NTP: uncalibrated local clock"
description = '''I have a Windows 2003 DC (NTP3) that has a Cisco router as its time source on the same LAN.  Recently, 2003 server stopped getting replies from the router, however if I change the time source to any external NTP server, the sync problem goes away. Filtering for NTP traffic wireshark sees (NTP symmet...'''
date = "2010-12-07T07:43:00Z"
lastmod = "2010-12-07T17:31:00Z"
weight = 1270
keywords = [ "windows", "ntp", "domain", "cisco" ]
aliases = [ "/questions/1270" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [NTP: uncalibrated local clock](/questions/1270/ntp-uncalibrated-local-clock)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1270-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Windows 2003 DC (NTP3) that has a Cisco router as its time source on the same LAN. Recently, 2003 server stopped getting replies from the router, however if I change the time source to any external NTP server, the sync problem goes away.</p><p>Filtering for NTP traffic wireshark sees (NTP symmetric active) requests from the server to the Cisco router, but nothing comes back. (assuming NTP symmetric passing should be seen)</p><p><img src="http://www.remontnetworks.com/ntp.jpg" alt="alt text" /></p><p>when it says "uncalibrated local clock", does it mean uncalibrated local clock used as a primary reference for a subnet without external means of synchronization ?</p><p><a href="http://www.faqs.org/rfcs/rfc2030.html">http://www.faqs.org/rfcs/rfc2030.html</a></p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">windows ntp domain cisco</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '10, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p>net_tech<br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 07 Dec '10, 07:50</p></div></div><div id="comments-container-1270" class="comments-container"></div><div id="comment-tools-1270" class="comment-tools"></div><div class="clear"></div><div id="comment-1270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1280"></span>

<div id="answer-container-1280" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1280-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think this is simply the current reference source of the server that is sending the ntp traffic. The Cisco may not respond if it is not synchronized, though it has nothing to do with the Reference ID in this packet (as you stated it is going from the windows server to the NTP server. Since it is the DC, there is some time function that the server is holding. Therefore it is "used as a primary reference fore a subnet" and since it is synchronized it is "uncalibrated and without external means of sync"</p><p>Take a look at the status of the NTP on the Cisco if you have access by issuing the following commands:</p><p>show ntp status</p><p>show ntp associations</p><p>show ntp associations detail</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '10, 17:31</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Dec '10, 17:32</p></div></div><div id="comments-container-1280" class="comments-container"></div><div id="comment-tools-1280" class="comment-tools"></div><div class="clear"></div><div id="comment-1280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

