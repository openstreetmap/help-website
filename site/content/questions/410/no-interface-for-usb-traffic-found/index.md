+++
type = "question"
title = "No interface for USB traffic found"
description = '''I want to capture traffic from an USB scanner. But after starting wireshark I can&#x27;t see a proper interface for USB. Capturing network via eth0 works fine. Wireshark 1.2.8 openSUSE 11.3 with kernel 2.6.34.4-0.1 libpcap 1.1.1'''
date = "2010-10-04T11:45:00Z"
lastmod = "2010-10-06T11:26:00Z"
weight = 410
keywords = [ "interface", "usb" ]
aliases = [ "/questions/410" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [No interface for USB traffic found](/questions/410/no-interface-for-usb-traffic-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-410-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to capture traffic from an USB scanner. But after starting wireshark I can't see a proper interface for USB. Capturing network via eth0 works fine.</p><p>Wireshark 1.2.8 openSUSE 11.3 with kernel 2.6.34.4-0.1 libpcap 1.1.1</p></div><div id="question-tags" class="tags-container tags">interface usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '10, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/dbeba090e42c20071befe0719def822f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerd&#39;s gravatar image" /><p>Gerd<br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerd has one accepted answer">100%</span></p></div></div><div id="comments-container-410" class="comments-container"></div><div id="comment-tools-410" class="comment-tools"></div><div class="clear"></div><div id="comment-410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="441"></span>

<div id="answer-container-441" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-441-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>After performing a "modprobe usbmon" I can see the USB-Interfaces</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '10, 11:26</strong></p><img src="https://secure.gravatar.com/avatar/dbeba090e42c20071befe0719def822f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerd&#39;s gravatar image" /><p>Gerd<br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerd has one accepted answer">100%</span></p></div></div><div id="comments-container-441" class="comments-container"></div><div id="comment-tools-441" class="comment-tools"></div><div class="clear"></div><div id="comment-441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="422"></span>

<div id="answer-container-422" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-422-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm able to capture from <code>usbmon1</code> on Ubuntu 10.04 (Linux kernel 2.6.32-24) without having to do anything special. <code>dumpcap -D</code> says:</p><pre><code>1. eth0
2. usbmon1 (USB bus number 1)
3. any (Pseudo-device that captures on all interfaces)
4. lo</code></pre><p><code>strace</code> shows that dumpcap (libpcap, actually) opens <code>/dev/bus/usb</code> followed by <code>/dev/usbmon1</code>:</p><pre><code>4182  open(&quot;/dev/bus/usb&quot;, O_RDONLY|O_NONBLOCK|O_DIRECTORY|O_CLOEXEC) = 3
4182  fcntl(3, F_GETFD)                 = 0x1 (flags FD_CLOEXEC)
4182  getdents(3, /* 3 entries */, 32768) = 72
4182  open(&quot;/dev/usbmon1&quot;, O_RDONLY)    = 4
4182  ioctl(4, 0x9205, 0)               = 307200
4182  mmap(NULL, 307200, PROT_READ, MAP_SHARED, 4, 0) = 0x7f9a64c5f000
4182  close(4)                          = 0</code></pre><p>Do those exist on your system?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '10, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-422" class="comments-container"><span id="431"></span><div id="comment-431" class="comment"><div id="post-431-score" class="comment-score"></div><div class="comment-text"><p>dumpcap -D shows only eth0, any and lo. No usbmon available.</p></div><div id="comment-431-info" class="comment-info"><span class="comment-age">(06 Oct '10, 01:07)</span> Gerd</div></div><span id="432"></span><div id="comment-432" class="comment"><div id="post-432-score" class="comment-score"></div><div class="comment-text"><p>strace of dumpcap -D shows "No such file or directory" from /dev/usbmon1 to /dev/usbmon6</p></div><div id="comment-432-info" class="comment-info"><span class="comment-age">(06 Oct '10, 03:44)</span> Gerd</div></div></div><div id="comment-tools-422" class="comment-tools"></div><div class="clear"></div><div id="comment-422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="411"></span>

<div id="answer-container-411" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-411-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since you can't see the USB interface listed, then you can't capture from it.</p><p>There's some great information on setting up Wireshark for USB capture on Linux platforms at http://wiki.wireshark.org/CaptureSetup/USB. Hope that works for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '10, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-411" class="comments-container"><span id="417"></span><div id="comment-417" class="comment"><div id="post-417-score" class="comment-score"></div><div class="comment-text"><p>Sorry, but this is not helpful for me. I'm not new in using Wireshark and asked my question after I found the article "USB capture setup" in the wiki and tried the example without success. Instead of an USB network gadget I used a USB scanner Canon LIDE 50. I performed as Root "mount -t usbfs /dev/bus/usb /proc/bus/usb" and started Wireshark. But there were only the interfaces eth0, Pseudo and IO. The example says "8. On Linux, startup a USB-enabled version of Wireshark..." What is a USB-enabled version ? Are the used versions of Wireshark (1.2.8), Kernel(2.6.34.4-0.1), libpcap (1.1.1) ok ?</p></div><div id="comment-417-info" class="comment-info"><span class="comment-age">(05 Oct '10, 10:46)</span> Gerd</div></div><span id="434"></span><div id="comment-434" class="comment"><div id="post-434-score" class="comment-score"></div><div class="comment-text"><p>I'm a newbie to the list so please forgive me if I don't understand what you are trying to do. It sounds like you are trying to launch a wireshark scan using a usb scanner (quote:I used a USB scanner Canon LIDE 50)? That isn't really possible as far as I can see. Where did you get the idea? Am I reading your post wrong? If so again I apologize. Please clarify.</p></div><div id="comment-434-info" class="comment-info"><span class="comment-age">(06 Oct '10, 06:04)</span> blacknight</div></div><span id="442"></span><div id="comment-442" class="comment"><div id="post-442-score" class="comment-score"></div><div class="comment-text"><p>Hi blacknight, I hope my English is sufficient to explain my idea to you... My Scanner works well in Windows XP, but not in Linux. There is a ugly noise when I try to scan. As there is no trace option with the Canon XP driver and I found no suitable free usb sniffer for Windows XP, I use a VirtualBox client to perform scanning in a XP environment. Then I would capture the scanner USB traffic on my Linux box. Compared with trace data when scanning under linux maybe I see what goes wrong.</p></div><div id="comment-442-info" class="comment-info"><span class="comment-age">(06 Oct '10, 11:57)</span> Gerd</div></div><span id="453"></span><div id="comment-453" class="comment"><div id="post-453-score" class="comment-score"></div><div class="comment-text"><p>@blacknight Just to expand on @Gerd's comment, Wireshark can be used to analyze packet-based technologies that aren't traditionally used for networking such as USB, Bluetooth, and CAN-bus. It can also open MP3 and JPEG files.</p></div><div id="comment-453-info" class="comment-info"><span class="comment-age">(06 Oct '10, 16:43)</span> Gerald Combs ♦♦</div></div></div><div id="comment-tools-411" class="comment-tools"></div><div class="clear"></div><div id="comment-411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

