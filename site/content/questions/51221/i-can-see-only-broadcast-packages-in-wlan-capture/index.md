+++
type = "question"
title = "I can see only BROADCAST packages in WLAN CAPTURE"
description = '''As the title says, i can capture only broadcast packages while capturing on wlan. That&#x27;s what i did:  sudo airmon-ng start wlan0 , airmon check kill (to kill the process that causes trouble), airmon-ng stop wlan0mon , airmon-ng start wlan0 , and the network adapter succesfully enter in monitor mode....'''
date = "2016-03-27T03:12:00Z"
lastmod = "2016-03-28T13:28:00Z"
weight = 51221
keywords = [ "broadcast", "capture", "packages", "wlan", "wireshark" ]
aliases = [ "/questions/51221" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I can see only BROADCAST packages in WLAN CAPTURE](/questions/51221/i-can-see-only-broadcast-packages-in-wlan-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51221-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As the title says, i can capture only broadcast packages while capturing on wlan. That's what i did: <code> sudo airmon-ng start wlan0 </code>, <code> airmon check kill </code> (to kill the process that causes trouble), <code> airmon-ng stop wlan0mon </code>, <code> airmon-ng start wlan0 </code>, and the network adapter succesfully enter in monitor mode. then i <code> sudo wireshark </code> , and start capturing on <code> wlan0mon </code>. But the only thing i can see is a lot of broadcast packages, and some other packages that i don't really care about. Actually i need to capture packages sent and received from my phone, connected by WiFi. What am i doing wrong? [ I tried with ARPspoof, but the phone loses connection (i can see only the DNS requests it send to the rounter. i can't connect e.g. to google.com). ]</p></div><div id="question-tags" class="tags-container tags">broadcast capture packages wlan wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '16, 03:12</strong></p><img src="https://secure.gravatar.com/avatar/775d98a2cfa3308c62a5c3d5169c3cc1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hikami&#39;s gravatar image" /><p>Hikami<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hikami has no accepted answers">0%</span></p></div></div><div id="comments-container-51221" class="comments-container"><span id="51244"></span><div id="comment-51244" class="comment"><div id="post-51244-score" class="comment-score"></div><div class="comment-text"><p>Several possibilities:</p><ul><li><p>you may be monitoring at a different frequency channel than your WLAN is using</p></li><li><p>your phone may use a more advanced modulation than your PC's wireless NIC is able to demodulate</p></li><li><p>you may be using WPA encryption on your network so those frames you "don't care about" may actually be the ones you're interested in but do not look like that due to encryption</p></li><li><p>your phone may be too far or too close from the monitoring wireless card, causing the signal to be too noisy to be demodulated (too weak signal if too far as well as too strong one if too close may both prevent the receiver from working properly).</p></li></ul><p>If you believe you are monitoring at the proper frequency channel, and your phone is about 2 meters / 7 ft away from your PC while capturing and you still cannot see anything useful, try to publish the resulting capture at cloudshark or at some login-free file sharing service (Google drive, MS OneDrive) and edit your question with a link to it.</p></div><div id="comment-51244-info" class="comment-info"><span class="comment-age">(28 Mar '16, 13:44)</span> sindy</div></div></div><div id="comment-tools-51221" class="comment-tools"></div><div class="clear"></div><div id="comment-51221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51241"></span>

<div id="answer-container-51241" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51241-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Can you try to do the following?</p><ol><li>Determine the Channel frequency, Channel bandwidth and Center 1 frequency. This can be done by connecting the WLAN adapter that will be used for the capture to the same SSID that is of interest. Then issue the command "wlan0 info".</li><li>Disassociate the WLAN adapter from the SSID.</li><li><p>Issue the commands:</p><p>ifconfig wlan0 down</p><p>iw dev wlan0 set type monitor</p><p>ifconfig wlan0 up</p><p>iw dev wlan1 set freq 5180 40 5190</p></li><li><p>Launch Wireshark</p></li><li>Select the mon0 interface</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '16, 13:28</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-51241" class="comments-container"></div><div id="comment-tools-51241" class="comment-tools"></div><div class="clear"></div><div id="comment-51241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

