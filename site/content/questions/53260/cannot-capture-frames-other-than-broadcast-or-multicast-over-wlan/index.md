+++
type = "question"
title = "Cannot Capture Frames Other Than Broadcast or Multicast over WLAN"
description = '''I have searched almost every forum on this topic but couldn&#x27;t find a correct answer so I hope you can help. My problem is I cannot capture any frames other than broadcast or multicast over wireshark on my WLAN interface (eg. no ICMP packets, no HTTP packets, etc.) Please follow details below:  OS: L...'''
date = "2016-06-06T23:18:00Z"
lastmod = "2016-06-07T02:56:00Z"
weight = 53260
keywords = [ "sniffing", "kali", "wifi" ]
aliases = [ "/questions/53260" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot Capture Frames Other Than Broadcast or Multicast over WLAN](/questions/53260/cannot-capture-frames-other-than-broadcast-or-multicast-over-wlan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53260-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have searched almost every forum on this topic but couldn't find a correct answer so I hope you can help.</p><p>My problem is I cannot capture any frames other than broadcast or multicast over wireshark on my WLAN interface (eg. no ICMP packets, no HTTP packets, etc.)</p><p>Please follow details below:</p><ul><li>OS: Linux KALI 2016.1 Rolling Release 64bit (u#1 SMP Debian 4.3.3-5kali4)</li><li>NIC: Linksys WUSB600Nv2 Dual-Band (RaLink RT3572 - Driver: rt2800usb - mac80211: capable - Assigned as WLAN0)</li><li>WLAN0 put to monitor mode (using airmon-ng start wlan0) therefore listening on <strong>wlan0mon</strong> Channel 01 on Wireshark</li><li>Test AP: Linksys E3000 on Channel 01 - Open security no encryption</li><li>Second Client: Win7 Laptop pinging the AP (ICMPv4) &amp; Surfing web</li><li>Wireshark version 2.0.3</li></ul><p>However cannot capture any UNICAST frames, please tell me what I am missing, Thanks</p></div><div id="question-tags" class="tags-container tags">sniffing kali wifi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '16, 23:18</strong></p><img src="https://secure.gravatar.com/avatar/955aef8cc9cd1e8c48503b52fa56c60e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bahmanthegreat&#39;s gravatar image" /><p>bahmanthegreat<br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bahmanthegreat has no accepted answers">0%</span></p></div></div><div id="comments-container-53260" class="comments-container"><span id="53261"></span><div id="comment-53261" class="comment"><div id="post-53261-score" class="comment-score"></div><div class="comment-text"><p>Not an authoritative answer - you may be missing a proper driver which would let through all frames captured in monitoring mode, regardless their destination MAC address. This seems obvious but some drivers' authors think otherwise so monitoring mode doesn't automatically mean promiscuous mode, and there is currently no chance to ask the driver for both simultaneously.</p><p>Alternatively, the driver may be OK but you forgot about WPA security - Wireshark cannot recognize any packets as ICMP, HTTP etc. without decrypting them first.</p><p>So to choose the right possibility: can you see any other destination <strong>MAC</strong> addresses than broadcast and multicast (and your own one) in the captured frames?</p></div><div id="comment-53261-info" class="comment-info"><span class="comment-age">(07 Jun '16, 00:56)</span> sindy</div></div><span id="53262"></span><div id="comment-53262" class="comment"><div id="post-53262-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick reply Sindy,</p><p>To clarify: 1. No encryption is applied to the SSID, it's open. 2. I do not receive any frames for destinations other than Broadcast/Multicast. 3. I do not receive frames destined to my own station unless I am connected to the AP (which beats the purpose if I do because I have to change out of monitor mode) 4. I have tried filtering out the broadcast/multicast frames from the capture and the output showed no frames at all. 5. No firewall is running, no antiviruses. 6. I can see ARP requests, SSDP, NBNS, IGMP, etc. but no unicast traffic.</p><p>How can I make sure I have the correct driver?</p></div><div id="comment-53262-info" class="comment-info"><span class="comment-age">(07 Jun '16, 01:29)</span> bahmanthegreat</div></div><span id="53267"></span><div id="comment-53267" class="comment"><div id="post-53267-score" class="comment-score"></div><div class="comment-text"><p>I'm afraid that only by reading the driver's code, and patching it if necessary.</p></div><div id="comment-53267-info" class="comment-info"><span class="comment-age">(07 Jun '16, 02:36)</span> sindy</div></div></div><div id="comment-tools-53260" class="comment-tools"></div><div class="clear"></div><div id="comment-53260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53269"></span>

<div id="answer-container-53269" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53269-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That Kernel, if I recall, has a regression for monitor mode with RT chipsets:</p><p><a href="http://marc.info/?l=linux-wireless&amp;m=145311668331789&amp;w=2">http://marc.info/?l=linux-wireless&amp;m=145311668331789&amp;w=2</a></p><p>On Kali Rolling, try to get to this kernel or later:</p><pre><code>4.4.0-kali1-amd64 #1 SMP Debian 4.4.6-1kali1 (2016-03-18) x86_64 GNU/Linux</code></pre><p>I capture regularly with RT chipsets but had to work around that driver issue by upgrading kernels.<br />
</p><p>To upgrade the kernel, try</p><pre><code>apt-get upgrade linux-image</code></pre><p>You can see what kernels are available with:</p><pre><code>/home/admin/horst-git# apt-cache search linux-image
linux-headers-4.4.0-kali1-amd64 - Header files for Linux 4.4.0-kali1-amd64
linux-image-4.4.0-kali1-amd64 - Linux 4.4 for 64-bit PCs
linux-image-4.4.0-kali1-amd64-dbg - Debugging symbols for Linux 4.4.0-kali1-amd64
linux-image-amd64 - Linux for 64-bit PCs (meta-package)
linux-image-amd64-dbg - Debugging symbols for Linux amd64 configuration (meta-package)
nvidia-kernel-4.4.0-kali1-amd64 - NVIDIA binary kernel module for Linux 4.4.0-kali1-amd64
linux-image-4.3.0-kali1-amd64 - Linux 4.3 for 64-bit PCs</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '16, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></p></div></div><div id="comments-container-53269" class="comments-container"><span id="53274"></span><div id="comment-53274" class="comment"><div id="post-53274-score" class="comment-score"></div><div class="comment-text"><p>Bob you are a genius! Upgrading the kernel solved the problem.</p><p>Many thanks.</p></div><div id="comment-53274-info" class="comment-info"><span class="comment-age">(07 Jun '16, 04:47)</span> bahmanthegreat</div></div><span id="53276"></span><div id="comment-53276" class="comment"><div id="post-53276-score" class="comment-score">1</div><div class="comment-text"><p>I note your very detailed question. Most just put 'It doesn't work' and rarely provide a capture file. With the detail you provided it was possible to go right to work and figure out what is wrong. Technically, this isn't a Wireshark issue but rather a hardware/driver problem.<br />
</p><p>OK, I get why people won't put kernel versions and such, even though it can be important, but this is a Wireshark site, and some of the other people here <em>really</em> know what they are doing. So why people won't put up a capture file for those experts to look at until it is practically ripped out of them is beyond me...</p></div><div id="comment-53276-info" class="comment-info"><span class="comment-age">(07 Jun '16, 06:02)</span> Bob Jones</div></div></div><div id="comment-tools-53269" class="comment-tools"></div><div class="clear"></div><div id="comment-53269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

