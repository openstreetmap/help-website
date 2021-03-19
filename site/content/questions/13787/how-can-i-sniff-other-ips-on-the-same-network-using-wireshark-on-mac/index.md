+++
type = "question"
title = "how can i sniff other IPs on the same network using WireSHARK on mac"
description = '''how can i sniff other IPs on the same network using WireSHARK on mac... i can see for example my mobile IP address in the interfaces but i can&#x27;t start capturing the packets '''
date = "2012-08-20T20:23:00Z"
lastmod = "2012-08-21T13:44:00Z"
weight = 13787
keywords = [ "macbook" ]
aliases = [ "/questions/13787" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [how can i sniff other IPs on the same network using WireSHARK on mac](/questions/13787/how-can-i-sniff-other-ips-on-the-same-network-using-wireshark-on-mac)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13787-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how can i sniff other IPs on the same network using WireSHARK on mac... i can see for example my mobile IP address in the interfaces but i can't start capturing the packets</p></div><div id="question-tags" class="tags-container tags">macbook</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '12, 20:23</strong></p><img src="https://secure.gravatar.com/avatar/b4b68ca771679d4280f0cc8e243f34ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mazen&#39;s gravatar image" /><p>Mazen<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mazen has no accepted answers">0%</span></p></div></div><div id="comments-container-13787" class="comments-container"></div><div id="comment-tools-13787" class="comment-tools"></div><div class="clear"></div><div id="comment-13787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="13796"></span>

<div id="answer-container-13796" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13796-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Refer to the Wireshark <a href="http://wiki.wireshark.org/CaptureSetup">Capture Setup</a> wiki page. Note that this is a general capture setup page, but there are other related pages referred to in the "<a href="http://wiki.wireshark.org/CaptureSetup#See_Also">See Also</a>" section for additional information specific to capturing on certain types of networks, such as <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet</a>, <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">802.11</a>, <a href="http://wiki.wireshark.org/CaptureSetup/TokenRing">Token Ring</a>, etc.</p><p>If you're having trouble using Wireshark itself in order to initiate capturing, then you might find the Wireshark <a href="http://www.wireshark.org/docs/wsug_html_chunked/">User Guide</a> helpful, in particular the section on <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChapterCapture.html">Capturing</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '12, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Aug '12, 11:53</p></div></div><div id="comments-container-13796" class="comments-container"></div><div id="comment-tools-13796" class="comment-tools"></div><div class="clear"></div><div id="comment-13796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13802"></span>

<div id="answer-container-13802" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13802-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From "mobile IP address" I'm guessing the network is a Wi-Fi network. If so, then, given that this is presumably OS X, if you're running Wireshark 1.6 or later, there should be an option to select "monitor mode"; you'll need to run the Wi-Fi adapter in monitor mode in order to capture other hosts' traffic. If your network is "protected", i.e. using WEP or WPA encryption, you'll have to supply the password for the network to Wireshark to decrypt the traffic, and, for WPA/WPA2 personal mode, to decrypt traffic to or from a given host, you'd have to capture the traffic in which the host in question establishes a connection to the network (the whole point of WPA/WPA2 is, after all, to make it harder to sniff wireless networks...).</p><p>See <a href="http://wiki.wireshark.org/HowToDecrypt802.11">the Wireshark Wiki page on decrypting 802.11 traffic</a> for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '12, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-13802" class="comments-container"></div><div id="comment-tools-13802" class="comment-tools"></div><div class="clear"></div><div id="comment-13802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13791"></span>

<div id="answer-container-13791" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13791-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First you need admin privileges, Second you either need a TAP device to sniff others packets, or you need to execute an ARP Spoof attack, in order for you to see the packets of others (if you're on a switched environment).</p><p>OR Use a HUB device to connect your network and monitor/sniff them all.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '12, 04:05</strong></p><img src="https://secure.gravatar.com/avatar/0ce931f077e091c7dc397bda5e106b99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sha8e&#39;s gravatar image" /><p>sha8e<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sha8e has no accepted answers">0%</span></p></div></div><div id="comments-container-13791" class="comments-container"></div><div id="comment-tools-13791" class="comment-tools"></div><div class="clear"></div><div id="comment-13791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

