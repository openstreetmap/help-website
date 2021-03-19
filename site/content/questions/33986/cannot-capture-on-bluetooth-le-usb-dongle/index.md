+++
type = "question"
title = "Cannot capture on Bluetooth LE USB dongle"
description = '''I am using Wireshark 1.10.8 with WinPCap 4.1.3 I have a Bluetooth LE USB dongle, which is working without any problem, but I can&#x27;t capture it with wireshark : it is not listed in the list of interfaces. Note that I am able to see another bluetooth dongle I have. Same on Linux. I am using 1.10.8, wit...'''
date = "2014-06-20T04:38:00Z"
lastmod = "2014-06-22T07:20:00Z"
weight = 33986
keywords = [ "low-energer", "capture", "dongle", "usb", "bluetooth" ]
aliases = [ "/questions/33986" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot capture on Bluetooth LE USB dongle](/questions/33986/cannot-capture-on-bluetooth-le-usb-dongle)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33986-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark 1.10.8 with WinPCap 4.1.3 I have a Bluetooth LE USB dongle, which is working without any problem, but I can't capture it with wireshark : it is not listed in the list of interfaces. Note that I am able to see another bluetooth dongle I have.</p><p>Same on Linux. I am using 1.10.8, with libpcap 1.5.3. I am able to capture that other bluetooth dongle I have, but I cannot see that Bluetooth LE USB dongle.</p><p>Can you please assist on either OS?</p><p>Regards.</p></div><div id="question-tags" class="tags-container tags">low-energer capture dongle usb bluetooth</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '14, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/d5907520e4b8ef90c0d77d4e848e9cc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aaf&#39;s gravatar image" /><p>aaf<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aaf has no accepted answers">0%</span></p></div></div><div id="comments-container-33986" class="comments-container"><span id="33991"></span><div id="comment-33991" class="comment"><div id="post-33991-score" class="comment-score"></div><div class="comment-text"><p>In windows you can use netmon for USB Dongle capture and then u can open it in wireshark even i searched a lot but finally settled with netmon for USB Dongle capturing.For linux i have no idea.</p></div><div id="comment-33991-info" class="comment-info"><span class="comment-age">(20 Jun '14, 06:49)</span> kishan pandey</div></div><span id="33992"></span><div id="comment-33992" class="comment"><div id="post-33992-score" class="comment-score"></div><div class="comment-text"><p>yes, I know - but USB packets are "raw", more difficult to understand to me than Bluetooth packets.</p><p>NB. On Windows, USB capturing can be done with USBPcap. On Linux too, with usbmon (kernel module to load).</p></div><div id="comment-33992-info" class="comment-info"><span class="comment-age">(20 Jun '14, 07:28)</span> aaf</div></div></div><div id="comment-tools-33986" class="comment-tools"></div><div class="clear"></div><div id="comment-33986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34034"></span>

<div id="answer-container-34034" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34034-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>it is not listed in the list of interfaces.</p></blockquote><p>WinPcap will only be able to capture on supported devices (obviously). As there is no native Bluetooth support in WinPcap, it will only work, if the Bluetooth device driver makes the device look like a network interface to the OS and WinPcap. So, if the dongle does not appear on the list of devices, there are two possible reasons:</p><ul><li>It is not detected and thus not support by WinPcap. Not much you can do about that, except adding Bluetooth support to WinPcap yourself.</li><li>You started the WinPcap NPF driver <strong>before</strong> you inserted the USB dongle. In that case WinPcap won't see it either. Please run the following commands</li></ul><blockquote><p>sc stop npf<br />
remove and then insert the USB dongle<br />
sc start npf<br />
dumpcap -D -M</p></blockquote><p>If you don't see the device in the output of dumpcap, it's not supported by WinPcap.</p><blockquote><p>Same on Linux. I am able to capture that other bluetooth dongle I have, but <strong>I cannot see that Bluetooth LE USB dongle</strong>.</p></blockquote><p>Similar problem as on Windows. How does your kernel detected that dongle? Is it a network device?</p><p>What is the output of the following commands, after you have inserted the dongle.</p><blockquote><p>ifconfig -a<br />
dumpcap -D -M<br />
lsusb dmesg | egrep -i '(usb|bluetooth)'</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '14, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-34034" class="comments-container"><span id="34058"></span><div id="comment-34058" class="comment"><div id="post-34058-score" class="comment-score"></div><div class="comment-text"><p>My device is seen in dmesg, lsusb, but not by tcpdump, dumpcap, ifconfig or hcitool.</p><p>lsusb:</p><pre><code>Bus 001 Device 003: ID 2687:fb01</code></pre><p>dmesg:</p><pre><code>[503386.469496] usb 1-1.3: new full-speed USB device number 3 using ehci-pci
[503386.568329] usb 1-1.3: New USB device found, idVendor=2687, idProduct=fb01</code></pre><p>but nothing elsewhere:</p><p>ifconfig -a only lists eth0 and lo in my case.</p><p>dumpcap:</p><pre><code>$ dumpcap -D -M
1. eth0                 0       my IP       network
2. nflog                        0               network
3. nfqueue                      0               network
4. any                  0               network
5. lo           Loopback        0       127.0.0.1,::1   loopback</code></pre><p>tcpdump:</p><pre><code>$ sudo tcpdump -D
1.eth0
2.any (Pseudo-device that captures on all interfaces)
3.lo</code></pre><p>hcitool:</p><pre><code>$ sudo hcitool dev
Devices:</code></pre><p>Do you know how I can have it recognized by the system? (Linux Mint)</p></div><div id="comment-34058-info" class="comment-info"><span class="comment-age">(23 Jun '14, 02:50)</span> aaf</div></div><span id="34064"></span><div id="comment-34064" class="comment"><div id="post-34064-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Do you know how I can have it recognized by the system? (Linux Mint)</p></blockquote><p>that's a linux kernel/driver question and you will (most certainly) get a better answer in a Linux/Bluetooth forum. Furthermore you did not mention the brand of the Bluetooth dongle. I could search for the vendor ID, but as I said: A linux forum might be the better place for you to get the dongle recognized by the kernel. As soon as that works, tcpdump/wireshark should be able to detect it as well.</p></div><div id="comment-34064-info" class="comment-info"><span class="comment-age">(23 Jun '14, 04:12)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-34034" class="comment-tools"></div><div class="clear"></div><div id="comment-34034-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

