+++
type = "question"
title = "Troubleshooting slow WiFi file transfer"
description = '''I am hopping to get some advice on where to look for a problem with a file transfer over WiFi. This is a somewhat simple office set up. Cable Modem -&amp;gt;10/100 Router-&amp;gt;10/100/1000 Switch with jumbo frames enabled. Wireless DWL-3200AP (D-Link) access point is connected to a router. Wired computer ...'''
date = "2011-03-09T07:32:00Z"
lastmod = "2011-03-25T12:43:00Z"
weight = 2724
keywords = [ "slow", "ibm", "d-link", "wifi" ]
aliases = [ "/questions/2724" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Troubleshooting slow WiFi file transfer](/questions/2724/troubleshooting-slow-wifi-file-transfer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2724-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am hopping to get some advice on where to look for a problem with a file transfer over WiFi. This is a somewhat simple office set up. Cable Modem -&gt;10/100 Router-&gt;10/100/1000 Switch with jumbo frames enabled. Wireless DWL-3200AP (D-Link) access point is connected to a router. Wired computer is connected to a switch over 1Gb. Wireless IBM X201 laptop has a b/g/n realtek (RTL8192SE) network card &amp; connects to D-Link access point over G and shows 54Mb connection spped. Both computers run windows 7 and average 70MB/s file transfer speeds when they are connected to the switch. Once IBM goes wireless file transfer speeds are anywhere from 2MB/s to 2.5MB/s, I was expecting to see at least 6MB/s watching a 1GB file being copied. Wireless signal strength is not an issue. I am sitting right next to the AccessPoint.</p><p>Do I need to purchase AirPcap to troubleshoot this problem?</p><p>If I filter for tcp.analysis.flags while transferring a file over wifi I don’t get any packets displayed. None of the Wireless card settings have been changed, everything is set to factory defaults. Access point settings have not been tweaked other than security.</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">slow ibm d-link wifi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '11, 07:32</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p>net_tech<br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div></div><div id="comments-container-2724" class="comments-container"></div><div id="comment-tools-2724" class="comment-tools"></div><div class="clear"></div><div id="comment-2724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="3130"></span>

<div id="answer-container-3130" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3130-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>problem was fixed by updating the network driver which was released one day after the original post</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '11, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p>net_tech<br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div></div><div id="comments-container-3130" class="comments-container"></div><div id="comment-tools-3130" class="comment-tools"></div><div class="clear"></div><div id="comment-3130-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2726"></span>

<div id="answer-container-2726" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2726-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you have a problem on the "physical" wireless level and need to beacon frames etc. you might have to buy an AirPCAP adapter if you want to use Wireshark on Windows to look at things. With Linux you should be able to activate monitor mode yourself and use the internal WiFi adapter instead. That way you could find out if there are problems on the radio transmission layer.</p><p>I have to say I'm just a bit surprised that you expect 6MB/s on a 54MBit WiFi connection. 6MB/s would mean 48MBit/s, and I doubt you'd ever get that much data over a 54MBit connection. 2.5MB/s doesn't sound that unrealistic to me - WiFi isn't exactly good at getting up to maximum speeds :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '11, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2726" class="comments-container"><span id="2732"></span><div id="comment-2732" class="comment"><div id="post-2732-score" class="comment-score">2</div><div class="comment-text"><p>Actually, 6MB/s goodput would be 6*1024*1024*8*(1514/1460)/1000/1000 = ~52 Mbit/s... And that's on a fullduplex link and wireless is half duplex.</p><p>Apart from the maximum good-put rate on a streaming protocol, it was mentioned that the file was copied. Windows copies files per block and there is an application turn (and thus a roundtrip) between each block that can add up pretty quickly too.</p></div><div id="comment-2732-info" class="comment-info"><span class="comment-age">(09 Mar '11, 08:45)</span> SYN-bit ♦♦</div></div><span id="2734"></span><div id="comment-2734" class="comment"><div id="post-2734-score" class="comment-score"></div><div class="comment-text"><p>Thx for the additional info, I was just too lazy to calculate as precise as you did, I just did 6 times 8 :-)</p></div><div id="comment-2734-info" class="comment-info"><span class="comment-age">(09 Mar '11, 09:06)</span> Jasper ♦♦</div></div><span id="2800"></span><div id="comment-2800" class="comment"><div id="post-2800-score" class="comment-score"></div><div class="comment-text"><p>Jasper, I went back and tested again. With a built-in realtek adapter I am only getting 800KB/s during a file transfer, however if I insert a USB adapter and disable the built in I am getting 2.8MB/s. I did not realize that WiFi is half duplex, so I guess 2.8 – 3 Mb/s is all I can wish for.</p><p>What would you look for in the wireshark capture that may be an indication of a slow throughput using the built in adapter? At this point it does not look like the problem is signal related. Driver or Nic configuration perhaps?</p></div><div id="comment-2800-info" class="comment-info"><span class="comment-age">(14 Mar '11, 07:04)</span> net_tech</div></div></div><div id="comment-tools-2726" class="comment-tools"></div><div class="clear"></div><div id="comment-2726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2742"></span>

<div id="answer-container-2742" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2742-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>here is the AP's config</p><p>D-Link Access Point wlan1 -&gt; get config</p><p>wlan1 revisions: mac 5.8 phy 4.4 analog 4.6</p><p>PCI Vendor ID: 0x168c, Device ID: 0x13</p><p>Sub Vendor ID: 0x168c, Sub Device ID: 0x13</p><p>chip is AR2312</p><p>Country Code: US</p><p>Operation Mode: Access Point</p><p>Wlan State: Enabled</p><p>Radio Frequency: 2437 MHz (IEEE 6)</p><p>Wireless LAN Mode: 802.11g</p><p>Auto Channel Select: Enabled</p><p>Extended Channel Mode: Enabled</p><p>Data Rate: best</p><p>Antenna: best</p><p>Login Username: admin</p><p>RADIUS address:</p><p>Name server IP address:</p><p>Name server domain suffix:</p><p>SSID: WL02</p><p>SSID Suppress Mode: Disabled</p><p>System Name: D-Link Access Point</p><p>Beacon Interval: 100</p><p>DTIM: 1</p><p>Fragmentation Threshold: 2346</p><p>RTS/CTS Threshold: 2346</p><p>Short Preamble: Enabled</p><p>11g Only Allowed: Disabled</p><p>CTS Mode: AUTO</p><p>CTS Rate: 11 Mbps</p><p>CTS Type: CTS-ONLY</p><p>11g Overlapping BSS Protection: Disabled</p><p>11g Beacon Rate: 1 Mbps</p><p>11g Draft 5.0 compatibility: Disabled</p><p>Short Slot Time: Enabled</p><p>Basic 11g Rate Set: (1, 2, 5.5, 11)</p><p>11g Optimization Level: 1</p><p>Burst Time: 2</p><p>Burst Sequence Threshold: 3</p><p>IP Address: 192.168.50.50</p><p>IP Mask: 255.255.255.0</p><p>Host IP Address: 0.0.0.0</p><p>Gateway IP Address: 192.168.50.1</p><p>SNTP/NTP Server IP Address: 192.168.50.5</p><p>Time Zone: 14</p><p>HW Transmit Retry Limit: 4</p><p>SW Transmit Retry Limit: 3</p><p>TransmitPower: full</p><p>Current Transmit Output Power 21.0 dBm</p><p>SuperG :Disabled</p><p>Encryption: Enabled</p><p>Cipher selection: AUTO</p><p>Authentication Type: WPA2-PSK</p><p>Default transmit key: 1</p><p>Shared Key 1, size 40, 0000000000</p><p>Access Check: Disabled</p><p>Key Entry Method: hexadecimal</p><p>Group Key Update Interval: 1800 seconds</p><p>Key Source: server</p><p>Aging Interval: 300 seconds</p><p>Telnet Access: Enabled</p><p>Telnet Timeout: 180 seconds</p><p>Minimum rate: 1 Mbps</p><p>XR Poll interval: 100 msec</p><p>XR Frame Limit: 25</p><p>XR Poll Rate String is 0.25 1 1 3 3 6 6 20</p><p>XR Fragmentation Threshold: 540</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '11, 18:14</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p>net_tech<br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div></div><div id="comments-container-2742" class="comments-container"></div><div id="comment-tools-2742" class="comment-tools"></div><div class="clear"></div><div id="comment-2742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2825"></span>

<div id="answer-container-2825" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2825-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just to nit pick - You should consider your RF environment. How many other radios are operating in your area on the same, or neighboring frequencies? Even if you're on a different SSID you STILL share the medium (is this case medium = radio frequency). If you're in the US you really only have 3 separate frequencies or "channels": 1, 6, and 11. If you have an android or iPhone run a wifi analyzer and see how many neighboring SSIDs you can see. Note which of the above channels is LEAST used and set your AP up to use that channel. Don't set yourself up to use the other channels: 2-3 bleed over into 1; 4,5,7,8 bleed into 6; 9, 10, 12<em>, 13</em> bleed into 11. It's a big ol' mess.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '11, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-2825" class="comments-container"><span id="2826"></span><div id="comment-2826" class="comment"><div id="post-2826-score" class="comment-score"></div><div class="comment-text"><p><strong>Auto Channel Select: Enabled</strong></p><p>Access Point monitors the environment and selects the best channel. Also all neighboring APs are added to the rogue AP list.</p></div><div id="comment-2826-info" class="comment-info"><span class="comment-age">(15 Mar '11, 06:41)</span> net_tech</div></div><span id="2828"></span><div id="comment-2828" class="comment"><div id="post-2828-score" class="comment-score"></div><div class="comment-text"><p>Just my 2 cents - don't let it self adjust and jump frequencies on you. I don't think there's really a standard for this, and you don't want your AP jumping frequencies in the middle of a transfer.</p></div><div id="comment-2828-info" class="comment-info"><span class="comment-age">(15 Mar '11, 08:02)</span> GeonJay</div></div></div><div id="comment-tools-2825" class="comment-tools"></div><div class="clear"></div><div id="comment-2825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

