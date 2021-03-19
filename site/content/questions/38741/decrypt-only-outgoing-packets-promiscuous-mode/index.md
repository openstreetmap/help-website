+++
type = "question"
title = "Decrypt only outgoing packets - promiscuous mode."
description = '''I am using linux with airmon-ng. When I sniff in promiscuous mode I can only decrypt packets outgoing from sniffed devices (I can decrypt http requests but not resonses). When in monitor mode I can decrypt everything. I am very curious what is the cause. I am attaching dump from Wireshark ESSID:Open...'''
date = "2014-12-27T10:52:00Z"
lastmod = "2014-12-27T12:13:00Z"
weight = 38741
keywords = [ "sniffing", "decryption", "wpa2", "wlan", "wireshark" ]
aliases = [ "/questions/38741" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypt only outgoing packets - promiscuous mode.](/questions/38741/decrypt-only-outgoing-packets-promiscuous-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38741-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using linux with airmon-ng. When I sniff in promiscuous mode I can only decrypt packets outgoing from sniffed devices (I can decrypt http requests but not resonses). When in monitor mode I can decrypt everything. I am very curious what is the cause.</p><p>I am attaching dump from Wireshark ESSID:OpenWrt WPA-PWD:test_network <a href="https://www.dropbox.com/s/c43j0pr87x991ae/weird_packets.pcapng?dl=0">https://www.dropbox.com/s/c43j0pr87x991ae/weird_packets.pcapng?dl=0</a> Sniffed device:10.11.11.165 My laptop:10.11.11.129</p></div><div id="question-tags" class="tags-container tags">sniffing decryption wpa2 wlan wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Dec '14, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/eed1969cb8eb9f95031e0cdb697ff66e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sewci0&#39;s gravatar image" /><p>Sewci0<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sewci0 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Dec '14, 11:24</p></div></div><div id="comments-container-38741" class="comments-container"><span id="38745"></span><div id="comment-38745" class="comment"><div id="post-38745-score" class="comment-score"></div><div class="comment-text"><p>was that capture file taken in monitor mode or promiscuous mode?</p></div><div id="comment-38745-info" class="comment-info"><span class="comment-age">(27 Dec '14, 11:13)</span> Kurt Knochner ♦</div></div><span id="38746"></span><div id="comment-38746" class="comment"><div id="post-38746-score" class="comment-score"></div><div class="comment-text"><p>In promiscuous mode. In monitor mode everything is working perfectly.</p></div><div id="comment-38746-info" class="comment-info"><span class="comment-age">(27 Dec '14, 11:14)</span> Sewci0</div></div><span id="38747"></span><div id="comment-38747" class="comment"><div id="post-38747-score" class="comment-score"></div><div class="comment-text"><p>what's the mac address of your laptop and the other (sniffed) device?</p></div><div id="comment-38747-info" class="comment-info"><span class="comment-age">(27 Dec '14, 11:15)</span> Kurt Knochner ♦</div></div><span id="38748"></span><div id="comment-38748" class="comment"><div id="post-38748-score" class="comment-score"></div><div class="comment-text"><p>Laptop: 64:5a:04:64:36:88 Sniffed device: B4:18:D1:A6:0B:35 AP: 90:F6:52:5D:28:66</p></div><div id="comment-38748-info" class="comment-info"><span class="comment-age">(27 Dec '14, 11:21)</span> Sewci0</div></div></div><div id="comment-tools-38741" class="comment-tools"></div><div class="clear"></div><div id="comment-38741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38749"></span>

<div id="answer-container-38749" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38749-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If I select the option "<strong>Ignore the protection bit: Yes - with IV</strong>", I can decrypt your capture file and I'm able to see traffic from 10.11.12.129 (you posted the wrong IP address - 10.11.11.129) and also a broadcast from 10.11.12.165.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_q38741_screenshot.png" alt="alt text" /></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '14, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 27 Dec '14, 12:14</p></div></div><div id="comments-container-38749" class="comments-container"><span id="38750"></span><div id="comment-38750" class="comment"><div id="post-38750-score" class="comment-score"></div><div class="comment-text"><p>Are you able to decrypt packets going to 10.11.12.165 (http responses)?</p></div><div id="comment-38750-info" class="comment-info"><span class="comment-age">(27 Dec '14, 12:19)</span> Sewci0</div></div><span id="38751"></span><div id="comment-38751" class="comment"><div id="post-38751-score" class="comment-score"></div><div class="comment-text"><p>I can only see a single frame (#423), which is a broadcast to 224.0.0.251.</p><p>If you wonder why, please see the comments on promiscuous mode here:</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Monitor_mode">http://wiki.wireshark.org/CaptureSetup/WLAN#Monitor_mode</a></p></blockquote><p>To reliably be able to capture and decrypt the whole traffic, you should use monitor mode.</p></div><div id="comment-38751-info" class="comment-info"><span class="comment-age">(27 Dec '14, 12:26)</span> Kurt Knochner ♦</div></div><span id="38753"></span><div id="comment-38753" class="comment"><div id="post-38753-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I can only see a single frame (#423), which is a broadcast to 224.0.0.251.</p></blockquote><p>Just out of curious. How those packets affect capturing? Why are they important?</p></div><div id="comment-38753-info" class="comment-info"><span class="comment-age">(27 Dec '14, 12:40)</span> Sewci0</div></div><span id="38755"></span><div id="comment-38755" class="comment"><div id="post-38755-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, can you please add more information? Which frames are you referring to?</p></div><div id="comment-38755-info" class="comment-info"><span class="comment-age">(27 Dec '14, 12:57)</span> Kurt Knochner ♦</div></div><span id="38756"></span><div id="comment-38756" class="comment"><div id="post-38756-score" class="comment-score"></div><div class="comment-text"><p>You said that you only see one frame #423 I am curious why you choose this frame while I was asking about frames going from router to sniffed device for example #503. It seams like packets going from device to router are being properly decrypted while those coming from router to device aren't.</p></div><div id="comment-38756-info" class="comment-info"><span class="comment-age">(27 Dec '14, 13:18)</span> Sewci0</div></div><span id="38779"></span><div id="comment-38779" class="comment not_top_scorer"><div id="post-38779-score" class="comment-score"></div><div class="comment-text"><blockquote><p>You said that you only see one frame #423 I am curious why you choose this frame</p></blockquote><p>because you mentioned the IP address: 10.11.12.165</p></div><div id="comment-38779-info" class="comment-info"><span class="comment-age">(30 Dec '14, 03:48)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-38749" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-38749-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

