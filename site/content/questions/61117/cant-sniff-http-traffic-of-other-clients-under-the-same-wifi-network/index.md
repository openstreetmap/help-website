+++
type = "question"
title = "Can&#x27;t sniff http traffic of other clients under the same wifi network"
description = '''Hello! This is my setup A.  VMWare with Kali Linux under a Win10 pc Wireshark Alfa Wireless USB Adapter  B.  My Win 10 connects to our home wifi My VMWare receives traffic through the Win10 connection(this means that its wired connected) Alfa USB is on monitor mode(wlan0mon) Wireshark runs with defa...'''
date = "2017-04-29T10:30:00Z"
lastmod = "2017-04-29T22:02:00Z"
weight = 61117
keywords = [ "sniffing", "http.request", "http" ]
aliases = [ "/questions/61117" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can't sniff http traffic of other clients under the same wifi network](/questions/61117/cant-sniff-http-traffic-of-other-clients-under-the-same-wifi-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61117-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! This is my setup</p><p>A.</p><ul><li>VMWare with Kali Linux under a Win10 pc</li><li>Wireshark</li><li>Alfa Wireless</li><li>USB Adapter</li></ul><p>B.</p><ul><li>My Win 10 connects to our home wifi</li><li>My VMWare receives traffic through the Win10 connection(this means that its wired connected)</li><li>Alfa USB is on monitor mode(wlan0mon)</li><li>Wireshark runs with default option for wlan0mon(Monitor mode unchecked and Promiscuous checked)</li><li>Wireshark filter: http</li></ul><p>C.</p><ul><li>My mobile phone is connected to the same wifi network</li></ul><p>No matter what I do I can't seem to capture the http traffic from my mobile phone. I'd appreciate any help or advice.</p></div><div id="question-tags" class="tags-container tags">sniffing http.request http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '17, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/958665b5d3ab07f5789f8e6d6d6d9bf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="parevale&#39;s gravatar image" /><p>parevale<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="parevale has no accepted answers">0%</span></p></div></div><div id="comments-container-61117" class="comments-container"></div><div id="comment-tools-61117" class="comment-tools"></div><div class="clear"></div><div id="comment-61117-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61123"></span>

<div id="answer-container-61123" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61123-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's likely encrypted, but we have no idea what traffic you do get to see to know if the issue might be something else, such as modulation issues.</p><p>Some places to start - to decrypt:</p><p><a href="https://wiki.wireshark.org/HowToDecrypt802.11">https://wiki.wireshark.org/HowToDecrypt802.11</a></p><p>Not seeing all the traffic you expect:</p><p><a href="https://ask.wireshark.org/questions/53260/cannot-capture-frames-other-than-broadcast-or-multicast-over-wlan">https://ask.wireshark.org/questions/53260/cannot-capture-frames-other-than-broadcast-or-multicast-over-wlan</a></p><p>...and search on this site as this type of issues comes up routinely.</p><p>If none of this works, post a link to a short capture and we can have a look and check to be sure you are observing data frames for the devices in question and go from there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '17, 22:02</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-61123" class="comments-container"><span id="61131"></span><div id="comment-61131" class="comment"><div id="post-61131-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your reply :)</p><p>I will check the links you provided later on, in the meantime I have create a .cap file with airodump-ng where I have used my other pc(which is on the same network) to log into an ftp account(using Win7 cmd). Then I used Wireshark to view the .cap file where I noticed that it only showed 802.11 protocol requests.</p></div><div id="comment-61131-info" class="comment-info"><span class="comment-age">(30 Apr '17, 15:56)</span> parevale</div></div><span id="61269"></span><div id="comment-61269" class="comment"><div id="post-61269-score" class="comment-score"></div><div class="comment-text"><p>Thank you Bob. Your answer helped to me to find my way to the solution of this issue. I didn't know I had to de-crypt wireshark monitoring while I also didnt know that I would have to wait until the client pc reconnects to the network while wireshark was running.</p></div><div id="comment-61269-info" class="comment-info"><span class="comment-age">(06 May '17, 16:10)</span> parevale</div></div></div><div id="comment-tools-61123" class="comment-tools"></div><div class="clear"></div><div id="comment-61123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

