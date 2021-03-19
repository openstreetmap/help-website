+++
type = "question"
title = "Beacons Intervals"
description = '''I am new to wireshark. To be honest, this is an assignment I have to do using Wireshark. Anyway, I have a pcap file which has the content of more than 4000 entries. I need to find the Beacons Interval. Is there a filter I need to use? '''
date = "2017-04-15T13:42:00Z"
lastmod = "2017-04-15T16:19:00Z"
weight = 60849
keywords = [ "intervals" ]
aliases = [ "/questions/60849" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Beacons Intervals](/questions/60849/beacons-intervals)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60849-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to wireshark. To be honest, this is an assignment I have to do using Wireshark. Anyway, I have a pcap file which has the content of more than 4000 entries. I need to find the Beacons Interval. Is there a filter I need to use?</p></div><div id="question-tags" class="tags-container tags">intervals</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '17, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/13b9874ded6ad7d47c50d9b0551d88b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cyberchaos&#39;s gravatar image" /><p>cyberchaos<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cyberchaos has no accepted answers">0%</span></p></div></div><div id="comments-container-60849" class="comments-container"></div><div id="comment-tools-60849" class="comment-tools"></div><div class="clear"></div><div id="comment-60849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60852"></span>

<div id="answer-container-60852" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60852-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, a display filter will help quantify the beacon interval. Google shows this page with something very close:</p><p><a href="https://wiki.wireshark.org/Wi-Fi">https://wiki.wireshark.org/Wi-Fi</a></p><p>As this is an assignment, I leave it to you to determine the specific syntax to get the filter you need. If you have difficulty, show the filters you have come up and someone can provide more guidance.</p><p>Do you know what to expect from an AP as it relates to beacons, i.e. the TBTT? Use this expectation to help determine if you might have the correct filter as you work on the filter syntax.<br />
</p><p>This all assumes that you have a packet trace that actually includes beacons. It would be very difficult to infer TBTT from a trace without beacons. This usually requires that an 802.11 capture be obtained, but there can be alternatives from some vendors that may send wireless capture from an AP over a tunneled wired connection and these may or may not include beacons. Cisco, Aruba, Ruckus, Mikrotik, and many others support this in one way or another through various mechanisms and software packages.<br />
</p><p>To capture wireless traffic, which, if done correctly, will show beacons, review this information:</p><p><a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a></p><p>If wireless traffic comes from the AP vendor through some mechanism, check with them to see what is included. It may take some configuration to understand the encapsulation so that the wireless information can be decoded properly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '17, 16:19</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Apr '17, 06:26</p></div></div><div id="comments-container-60852" class="comments-container"><span id="60856"></span><div id="comment-60856" class="comment"><div id="post-60856-score" class="comment-score"></div><div class="comment-text"><p>Bob, Thanks for your help. Now, I used wlan display filter yesterday and it didn't show me anything. Part of the assignment is the pcap was captured on the router. I don't know if that gonna make any difference. I tried every possible (Wi-Fi filters) and all of the filters were blank.</p></div><div id="comment-60856-info" class="comment-info"><span class="comment-age">(15 Apr '17, 18:19)</span> cyberchaos</div></div><span id="60857"></span><div id="comment-60857" class="comment"><div id="post-60857-score" class="comment-score"></div><div class="comment-text"><p>I updated the answer to clarify the assumption that you have a wireless trace with beacons in it, and need only find them.</p><blockquote><blockquote><p>pcap was captured on the router</p></blockquote></blockquote><p>I don't know exactly what this means, so cannot advise on how to show what you need. This could mean:</p><ol><li><p>802.11 capture sitting next to the device</p></li><li><p>You took a wired capture of the traffic crossing the router that was created by wireless clients</p></li><li><p>The router is really an AP and has a mechanism for collecting capture files and forwarding them to a device on the LAN, encapsulated</p></li><li><p>And others...</p></li></ol><p>You could upload a trace in a publicly accessible location (i.e. cloudshark, drive, etc) so we can see what you are dealing with. Or try to obtain another capture per a different technique.</p></div><div id="comment-60857-info" class="comment-info"><span class="comment-age">(16 Apr '17, 06:32)</span> Bob Jones</div></div><span id="60868"></span><div id="comment-60868" class="comment"><div id="post-60868-score" class="comment-score"></div><div class="comment-text"><p>Bob, in the assignment, it says the traffic in the pcap was captured on the network router. attackers used protocol buffers. I need to find the beaconing interval in this pcap. I don't know what filter to use. I used wlan display filter and it didn't give me any results.</p></div><div id="comment-60868-info" class="comment-info"><span class="comment-age">(17 Apr '17, 12:59)</span> cyberchaos</div></div></div><div id="comment-tools-60852" class="comment-tools"></div><div class="clear"></div><div id="comment-60852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

