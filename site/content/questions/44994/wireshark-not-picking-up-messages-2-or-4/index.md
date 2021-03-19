+++
type = "question"
title = "Wireshark not picking up Messages #2 or #4?"
description = '''Hi I&#x27;m trying to capture the 4-way handshake between my tablet in my room and my AP. Somehow, when I&#x27;m next to the tablet, I can only pickup Messages #1 and #3. Only if I move closer to the AP (with the tablet still in my room), I can pick up #1, #2 and #3. I don&#x27;t know why I can never pick up #4 th...'''
date = "2015-08-12T02:36:00Z"
lastmod = "2015-08-12T06:47:00Z"
weight = 44994
keywords = [ "wpa2" ]
aliases = [ "/questions/44994" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark not picking up Messages \#2 or \#4?](/questions/44994/wireshark-not-picking-up-messages-2-or-4)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44994-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I'm trying to capture the 4-way handshake between my tablet in my room and my AP. Somehow, when I'm next to the tablet, I can only pickup Messages #1 and #3. Only if I move closer to the AP (with the tablet still in my room), I can pick up #1, #2 and #3. I don't know why I can never pick up #4 though.</p><p>Is there any reason why #2 (or #4 for that matter) is more sensitive to signal strength/distance from router?</p><p>I'm using a Raspberry Pi - could it be too slow for the task? I'm using a TP-Link WN-722N.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">wpa2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '15, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/3c16c3b7b9d89a5736de02187a6253d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mun&#39;s gravatar image" /><p>mun<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mun has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Aug '15, 05:30</p></div></div><div id="comments-container-44994" class="comments-container"></div><div id="comment-tools-44994" class="comment-tools"></div><div class="clear"></div><div id="comment-44994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45001"></span>

<div id="answer-container-45001" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45001-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>EAPOL messages #2 and #4 are transmitted by the WiFi client - in this case the tablet. So distance from the tablet would be important. That also means being too close to the client may cause your RF receiver on the wireless adapter that you are using for the wireless capture (i.e., TP-Link WN-722N) to saturate. You might want to try the following:</p><ol><li>Reboot the machine you are using to perform the capture.</li><li>Ensure there are no other processes/applications running on the capture PC prior to beginning the capture. This includes background processes like antivirus programs, etc.</li><li>Try to keep a distance between the AP, tablet and sniffer around 10 feet. Best practices is not to exceed 12 feet, but not be less than 1 foot.</li></ol><p>Good luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '15, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-45001" class="comments-container"><span id="45002"></span><div id="comment-45002" class="comment"><div id="post-45002-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the advice. I'm doing it in a RPi, but could the processor/memory/disk speed be an issue? Is there a better adapter for the job?</p></div><div id="comment-45002-info" class="comment-info"><span class="comment-age">(12 Aug '15, 06:49)</span> mun</div></div><span id="45003"></span><div id="comment-45003" class="comment"><div id="post-45003-score" class="comment-score"></div><div class="comment-text"><p>The RPi could be a limiting component. Are you using the Wireshark GUI to try to capture? If so, you might want to try a command line capture like tshark or dumpcap which are tools provided within Wireshark.</p><p><a href="https://www.wireshark.org/docs/man-pages/tshark.html">https://www.wireshark.org/docs/man-pages/tshark.html</a></p><p><a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">https://www.wireshark.org/docs/man-pages/dumpcap.html</a></p><p>If you are running Linux, then you can also try tcpdump.</p><p><a href="http://www.tcpdump.org/tcpdump_man.html">http://www.tcpdump.org/tcpdump_man.html</a></p></div><div id="comment-45003-info" class="comment-info"><span class="comment-age">(12 Aug '15, 07:15)</span> Amato_C</div></div></div><div id="comment-tools-45001" class="comment-tools"></div><div class="clear"></div><div id="comment-45001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

