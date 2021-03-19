+++
type = "question"
title = "Recommended wireless adapter (USB) with Linux wireshark that reports mactime in Radiotap header"
description = '''I have tried with Dlink-DWA-160-A2 card with AR9170 but do not see mac timestamp and also TSFT flag is 0.'''
date = "2014-01-08T11:35:00Z"
lastmod = "2014-01-09T10:02:00Z"
weight = 28683
keywords = [ "mactime" ]
aliases = [ "/questions/28683" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Recommended wireless adapter (USB) with Linux wireshark that reports mactime in Radiotap header](/questions/28683/recommended-wireless-adapter-usb-with-linux-wireshark-that-reports-mactime-in-radiotap-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28683-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have tried with Dlink-DWA-160-A2 card with AR9170 but do not see mac timestamp and also TSFT flag is 0.</p></div><div id="question-tags" class="tags-container tags">mactime</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '14, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/43e2d9c38f7fe55143e0606580e503bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sudheer&#39;s gravatar image" /><p>Sudheer<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sudheer has no accepted answers">0%</span></p></div></div><div id="comments-container-28683" class="comments-container"></div><div id="comment-tools-28683" class="comment-tools"></div><div class="clear"></div><div id="comment-28683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28740"></span>

<div id="answer-container-28740" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28740-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I did a quick test with my <a href="http://www.tp-link.us/products/details/?categoryid=&amp;model=TL-WN822N">TP-Link TL-WN822N v2</a> on <a href="http://kali.org">Kali 1.0.4</a>. Here are the results.</p><pre><code>[email protected]:~# lsusb
Bus 001 Device 002: ID 0cf3:7015 Atheros Communications, Inc. TP-Link TL-WN821N v3 802.11n [Atheros AR7010+AR9287]

+++ HINT +++: lsusb is showing the wlan device as TL-WN821N, whereas it is in reality a TL-WN822N Ver. 2.0 (822 instead of 821)!!!

[email protected]:~# airmon-ng start wlan0
[email protected]:~# tcpdump -ni mon0 -w /tmp/k1.pcap

[email protected]:~# tshark -nr /tmp/k1.pcap -T fields -e frame.number -e radiotap.mactime  
1       43619545
2       43622799
3       43774362
4       43759542
5       43902905

[email protected]:~# lsb_release -a
No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux Kali Linux 1.0
Release:        Kali Linux 1.0
Codename:       n/a</code></pre><p>As you can see there is a <code>mactime</code> field in the radiotap header. If my understanding is right, this means the Atheros chipset (actually the driver) put that timestamp into the data structure. So, the <a href="http://www.tp-link.us/products/details/?categoryid=&amp;model=TL-WN822N">TP-Link TL-WN822N V2</a> might be the right tool for you (or any other wlan device with that Atheros chipset).</p><p><strong>++ UPDATE ++</strong></p><p>In the meantime I tried some of my other wlan devices.</p><ul><li>D-Link DWA 160 A2 (Atheros 9170)</li><li>Alfa AWUS036NHR V2 (RTL8192cu)</li></ul><p>So far none of them provided a mactime field, meaning <strong>no</strong> hardware timestamps (or not implemented in the driver). So, the TP Link device with AR9287 is currently the only chipset for which I can confirm hardware timestamps.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '14, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jan '14, 14:56</p></div></div><div id="comments-container-28740" class="comments-container"><span id="28745"></span><div id="comment-28745" class="comment"><div id="post-28745-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for the information. The wireless I have used is Dlink DWA-160 Rev A2 that has Atheros chipset - AR9170 + AR9104 (<a href="http://wikidevi.com/wiki/D-Link_DWA-160_rev_A2).">http://wikidevi.com/wiki/D-Link_DWA-160_rev_A2).</a></p><p>The driver that gets loaded when i use the above card is carl9170.ko. Can you please let me know the driver that gets laoded when you try with TP-Link TL-WN822N V2 ?</p><p>-Sudheer</p></div><div id="comment-28745-info" class="comment-info"><span class="comment-age">(09 Jan '14, 12:24)</span> Sudheer</div></div><span id="28748"></span><div id="comment-28748" class="comment"><div id="post-28748-score" class="comment-score"></div><div class="comment-text"><p>driver: ath9k_htc</p><p>See also the <strong>UPDATE</strong> in my answer for AR9170.</p></div><div id="comment-28748-info" class="comment-info"><span class="comment-age">(09 Jan '14, 14:47)</span> Kurt Knochner ♦</div></div><span id="28749"></span><div id="comment-28749" class="comment"><div id="post-28749-score" class="comment-score"></div><div class="comment-text"><p>Thnaks for the info. So looks like with Atheros chip sets the only ones that report mac time stamp is AR7010, AR9287 with ath9k_htc driver. The one I have does not work.</p><p>I will look for wireless adapter that has above chip set and get one of those.</p></div><div id="comment-28749-info" class="comment-info"><span class="comment-age">(09 Jan '14, 14:57)</span> Sudheer</div></div><span id="28750"></span><div id="comment-28750" class="comment"><div id="post-28750-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure if those are the <strong>only</strong> ones, as I currently don't have access to devices with other Atheros chipsets. But at least I can confirm that the AR9287 is generating some reasonable looking <code>mactime</code> values on my system.</p><p><strong>Hint</strong>: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-28750-info" class="comment-info"><span class="comment-age">(09 Jan '14, 15:02)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28740" class="comment-tools"></div><div class="clear"></div><div id="comment-28740-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

