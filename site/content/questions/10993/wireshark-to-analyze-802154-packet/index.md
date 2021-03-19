+++
type = "question"
title = "Wireshark to analyze 802.15.4 packet"
description = '''Hi, I want to analyze 802.15.4 packet using wireshark. I am encapsulating 802.15.4 packet into udp and sending it to my pc. But anyhow I am unable to decode packet as a 802.15.4. Does any know in what format I should send this packet so that wireshark can decode it easily. Is there any significance ...'''
date = "2012-05-15T07:02:00Z"
lastmod = "2012-05-16T13:53:00Z"
weight = 10993
keywords = [ "802.15.4", "zigbee", "6lowpan", "wireshark" ]
aliases = [ "/questions/10993" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark to analyze 802.15.4 packet](/questions/10993/wireshark-to-analyze-802154-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10993-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to analyze 802.15.4 packet using wireshark. I am encapsulating 802.15.4 packet into udp and sending it to my pc. But anyhow I am unable to decode packet as a 802.15.4.</p><p>Does any know in what format I should send this packet so that wireshark can decode it easily. Is there any significance of ether type(809a) while sending in udp? This is my setup: Wireshark&lt;-ethernet-&gt;My 802.15.4 hardwere.</p><p>Regards, Mahesh Sutariya</p></div><div id="question-tags" class="tags-container tags">802.15.4 zigbee 6lowpan wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '12, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/a877f5fbd8fcd0f096db3476e08ffada?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maheshsutariya&#39;s gravatar image" /><p>maheshsutariya<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maheshsutariya has no accepted answers">0%</span></p></div></div><div id="comments-container-10993" class="comments-container"><span id="10996"></span><div id="comment-10996" class="comment"><div id="post-10996-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><ol><li>did you enable IEEE 802.15.4 dissection (Analyze -&gt; Enabled Protocols -&gt; IEEE 802.15.4)?</li><li>how did you create the encapsulating udp packet/header?</li><li>can you see any data in the udp packet?</li><li>can you post 3-4 packets on <a href="http://cloudshark.org">cloudshark.org</a> for further analysis?</li></ol><p>BTW: Here is an interesting article about 802.15.4 sniffing using a pipe.</p><blockquote><p><code>http://freaklabs.org/index.php/Tutorials/Software/Feeding-the-Shark-Turning-the-Freakduino-into-a-Realtime-Wireless-Protocol-Analyzer-with-Wireshark.html</code></p></blockquote><p>Regards<br />
Kurt</p></div><div id="comment-10996-info" class="comment-info"><span class="comment-age">(15 May '12, 07:47)</span> Kurt Knochner ♦</div></div><span id="11015"></span><div id="comment-11015" class="comment"><div id="post-11015-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, I am using default wireshark and all the protocol including 802.15.4, Zep, 6Lowpan is enabled. I can see sent data in UDP packet I receive in wireshark, but they are not decoded.</p><p>I checked out that freaklabs article by akiba, I am not using any kind of piping, I am sending udp packet just like a syslog message from external Ethernet hardware to a normal Ethernet interface of my PC.</p><p>I am sending pcap capture on cloudshark.. please check it. I am sending beacon request to wireshark as provided in pcap capture on 802.15.4 wiki page to port 17754.</p><p>Regards, Mahesh</p></div><div id="comment-11015-info" class="comment-info"><span class="comment-age">(15 May '12, 20:25)</span> maheshsutariya</div></div><span id="11017"></span><div id="comment-11017" class="comment"><div id="post-11017-score" class="comment-score"></div><div class="comment-text"><p>This is a capture url:<a href="http://cloudshark.org/captures/70714d83a585">http://cloudshark.org/captures/70714d83a585</a> apply this filter udp.port==17754</p></div><div id="comment-11017-info" class="comment-info"><span class="comment-age">(15 May '12, 20:37)</span> maheshsutariya</div></div></div><div id="comment-tools-10993" class="comment-tools"></div><div class="clear"></div><div id="comment-10993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="11053"></span>

<div id="answer-container-11053" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11053-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>O.K. there is 802.15.4 beacon data in the UDP packet (bytes: 030806ffffffff070507).</p><p><code>http://cloudshark.org/captures/70714d83a585</code><br />
</p><p>However, I believe your UDP encapsulation is broken, as you only have the 802.15.4 data in the UDP packet (beacon frame), while you need it in the format of <strong>ZEP (ZigBee Encapsulation Protocol)</strong>, for Wireshark to be able to dissect it. See packet-zep.c</p><blockquote><p><code>*      ZEP Packets must be received in the following format:</code><br />
<code>*      |UDP Header|  ZEP Header |IEEE 802.15.4 Packet|</code><br />
<code>*      | 8 bytes  | 16/32 bytes |    &lt;= 127 bytes    |</code><br />
</p></blockquote><p>Apparently, the <strong>ZEP header is missing</strong> in your UDP packet.</p><p>I was able to create two correct UDP encapsulated 802.15.4 packets with a HEX editor. See here:</p><p><strong>Beacon</strong><br />
<code>http://cloudshark.org/captures/1e46dea88db0</code></p><p><strong>Some sample from internet</strong><br />
<code>http://cloudshark.org/captures/18efd3ef7114</code></p><p><strong>SUMMARY</strong>: I believe the tool that did the UDP encapsulation did it wrong. It used the ZEP port, however it did not add the ZEP header (ZigBee Encapsulation Protocol) to the UDP packet. So, please check that tool.</p><p>To answer your question:</p><blockquote><p><code>Does any know in what format I should send this packet so that wireshark can decode it easily.</code></p></blockquote><p>Please use ZEP (ZigBee Encapsulation Protocol).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '12, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 May '12, 11:15</p></div></div><div id="comments-container-11053" class="comments-container"><span id="11078"></span><div id="comment-11078" class="comment"><div id="post-11078-score" class="comment-score"></div><div class="comment-text"><p>Hey I got it working.. We can send 802.15.4 packet in udp..</p><p>Kurt, you are right, we need to encapsulate 802.15.4 packet in ZEP to be detected by wireshark. check this capture to see 802.15.4/Zigbee/6LowPan packet received in wireshark <a href="http://cloudshark.org/captures/36822505d7ab">http://cloudshark.org/captures/36822505d7ab</a></p><p>Anyway, I like cloud shark - How long this capture stay there.</p><p>I am using lwip to encapsulate 802.15.4 packet in udp..</p><p><strong>For others,</strong> To analyze 802.15.4 in wireshark Just send Normal udp packet with a payload as [ZEPv2 Header(32 byte for data) + 802.15.4 packet] and send it to port 17754. Length in ZEP header must be set to length of 802.15.4 packet.</p><p>There is also other way to send 802.15.4 packet in Raw Ethernet frame without udp using magic packet header(0xa1b2c3d4) with DLT type of 195. not tried..many pipe lining example available for that..one is by akiba <a href="http://freaklabs.org/index.php/Tutorials/Software/Feeding-the-Shark-Turning-the-Freakduino-into-a-Realtime-Wireless-Protocol-Analyzer-with-Wireshark.html">freaklabs</a> as mentioned by kurt.</p><p>Regards, Mahesh Sutariya <a href="http://www.energycloud.co.in"></a><a href="http://www.energycloud.co.in">www.energycloud.co.in</a></p></div><div id="comment-11078-info" class="comment-info"><span class="comment-age">(16 May '12, 21:51)</span> maheshsutariya</div></div><span id="11086"></span><div id="comment-11086" class="comment"><div id="post-11086-score" class="comment-score"></div><div class="comment-text"><p>I converted your answer to a comment (see FAQ of this site). It's easier for other to find the relevant information.</p></div><div id="comment-11086-info" class="comment-info"><span class="comment-age">(17 May '12, 00:44)</span> Kurt Knochner ♦</div></div><span id="11087"></span><div id="comment-11087" class="comment"><div id="post-11087-score" class="comment-score"></div><div class="comment-text"><p>If you upload a capture anonymously, it will stay online until they delete it (possibly "forever"). However, I don't know their policy regarding deletion of public uploads.</p></div><div id="comment-11087-info" class="comment-info"><span class="comment-age">(17 May '12, 00:55)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11053" class="comment-tools"></div><div class="clear"></div><div id="comment-11053-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11065"></span>

<div id="answer-container-11065" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11065-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think that if the data is encapsulated in zep, then it is only decoded as zigbee. If you strip off the Ethernet-&gt;IP-&gt;UDP encapsulation and then set the encapsulation type to wpan it decodes cleanly. The sequence of editcap commands I used was:</p><pre><code>editcap -r 802_15_4.pcap 802_14_4_1.pcap 5 9
editcap -T wpan C 42 802_15_4_1.pcap 802_15_4_2.pcap
editcap -C -8 802_5_4_2.pcap 802_15_4_3.pcap</code></pre><p>The first line isolates the packets of interest, the second changes the encapsulation type an chops off the encapsulation bytes at the front of the packets and the third chops off the trailing encapsulation bytes. There might be a more efficient way to do this, but that's left as an exercise for the reader.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '12, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-11065" class="comments-container"><span id="11073"></span><div id="comment-11073" class="comment"><div id="post-11073-score" class="comment-score"></div><div class="comment-text"><p>that's also possible.</p><p>Did you check the cloudshark samples? They were not decoded as zigbee, just as zigbee encapsulated. However, the rest looks O.K.</p></div><div id="comment-11073-info" class="comment-info"><span class="comment-age">(16 May '12, 15:50)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11065" class="comment-tools"></div><div class="clear"></div><div id="comment-11065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10994"></span>

<div id="answer-container-10994" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10994-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See the Wiki page on 802.15.4 <a href="http://wiki.wireshark.org/IEEE_802.15.4">here</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '12, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-10994" class="comments-container"><span id="11016"></span><div id="comment-11016" class="comment"><div id="post-11016-score" class="comment-score"></div><div class="comment-text"><p>Hi Grahamb,</p><p>I came across that wiki page for 802.15.4 but does not much info on encapsulating protocol and about hardware side interface.</p><p>Regards, Mahesh</p></div><div id="comment-11016-info" class="comment-info"><span class="comment-age">(15 May '12, 20:25)</span> maheshsutariya</div></div><span id="11043"></span><div id="comment-11043" class="comment"><div id="post-11043-score" class="comment-score"></div><div class="comment-text"><p>I don't think that Wireshark handles 802.15.4 encapsulated in udp. The dissector expects to see 802.15.4 as a top level protocol in the capture file.</p></div><div id="comment-11043-info" class="comment-info"><span class="comment-age">(16 May '12, 05:26)</span> grahamb ♦</div></div><span id="11080"></span><div id="comment-11080" class="comment"><div id="post-11080-score" class="comment-score"></div><div class="comment-text"><p>also edited wiki 802.15.4 page for answer :)</p></div><div id="comment-11080-info" class="comment-info"><span class="comment-age">(16 May '12, 22:25)</span> maheshsutariya</div></div></div><div id="comment-tools-10994" class="comment-tools"></div><div class="clear"></div><div id="comment-10994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

