+++
type = "question"
title = "how can I precisely specify a USB device to capture with tshark?"
description = '''I have a USB instrument, and I want to capture packets on it.  I ran  .&#92;tshark.exe -D and the USB interface is number 6. then I ran the command: .&#92;tshark.exe -c 100 -i 6 it seemed to capture the USB traffic from my device. Then it occurred to me, that when this device is running, there may be multip...'''
date = "2016-07-07T17:21:00Z"
lastmod = "2016-07-08T15:41:00Z"
weight = 53919
keywords = [ "tshark" ]
aliases = [ "/questions/53919" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how can I precisely specify a USB device to capture with tshark?](/questions/53919/how-can-i-precisely-specify-a-usb-device-to-capture-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53919-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a USB instrument, and I want to capture packets on it. I ran <code>.\tshark.exe -</code>D and the USB interface is number 6. then I ran the command: <code>.\tshark.exe -c 100 -i 6</code> it seemed to capture the USB traffic from my device. Then it occurred to me, that when this device is running, there may be multiple USB devices, hooked up to the system, and just specifying might not be enough. I know the Device ID(0x0009), and Vendor ID(0x08f7) how can I specify the exact device I want to capture, via tshark?</p><p>I see a -f &lt;capture filter=""&gt; Set the capture filter expression option, and some <a href="https://wiki.wireshark.org/CaptureFilters">network examples</a> but this doesn't include any USB packet capture examples.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '16, 17:21</strong></p><img src="https://secure.gravatar.com/avatar/b997637a56fa3812bb5146b3786ee488?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eric%20Lovejoy&#39;s gravatar image" /><p>Eric Lovejoy<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eric Lovejoy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '16, 12:11</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-53919" class="comments-container"></div><div id="comment-tools-53919" class="comment-tools"></div><div class="clear"></div><div id="comment-53919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53947"></span>

<div id="answer-container-53947" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53947-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Simply put, there is no <strong>capture</strong> filter available for usb capturing, except the root hub (or "bus") number. This number translates into a capturing interface name if you use the extcap API to control the USBPcap, which is what you seem to be doing as you've provided a <code>tshark ...</code> command line rather than <code>USBPcap ...</code> command line. So in your case, as tsharks returns just a single USB interface to capture at, there is just a single root hub in the PC.</p><p>During USB enumeration phase, each USB device detected is assigned an ID like <code>m.n</code>, where <code>m</code> is the root hub number and <code>n</code> is the order number of the device to be identified. If you unplug a device and plug it again to the same physical port, it will keep the <code>m</code> but get a new <code>n</code>. In your case with a single root hub, <code>m</code> will always be 1.</p><p>The VID and PID (vendor ID and product ID) are only used to identify the device and choose a proper driver for it during the so-called enumeration phase. So unless you capture the enumeration phase (i.e. unless you start capturing on the proper root hub before plugging the device in), you won't capture the VID and PID at all.</p><p>So your only chance is to use a <strong>display</strong> filter. There, you can use the full usb addresses of the endpoints of the devices (<code>usb.addr == "m.n.e"</code> where <code>e</code> is the endpoint id) to see only the packets (actually, URBs, it is a difference!) to/from a particular endpoint of a particular device, or you can filter for <code>m</code> and <code>n</code> combination only (i.e. URBs to/from all endpoints of a device) using <code>usb.bus_id == m and usb.device_address == n</code>.</p><p>If you did capture the enumeration phase, a display filter <code>usb.idVendor and usb.idProduct</code> will show you all packets that contain the <code>VID:PID</code> pairs, and you can use these packets to map these <code>VID:PID</code> pairs to the <code>m.n</code> device addresses (the packets that contain the VID and PID always come from endpoint 0).</p><p>A display filter can be used already during capture, but it only prevents the non-matching URBs from being displayed, not from being captured. So in Wireshark, you have to use <code>File-&gt;Export Specified Packets-&gt;Displayed</code> to save only the packets matching the display filter expression to a new pcap file; in tshark, specifying the display filter expression using <code>-Y</code> and the output file using <code>-w</code> should do the trick (as with tshark, the display filter affects what is written to the output pcap file), but with tshark, you won't know the <code>m</code> and <code>n</code> in advance unless you first run tshark with <code>-Y "usb.idVendor and usb.idProduct"</code> and no <code>-w</code> before plugging the device in, to see the <code>VID:PID</code> to <code>m.n</code> mapping in the text form, followed by another tshark run with <code>-Y "usb.bus_id == m and usb.device_address == n"</code> and the <code>-w</code> causing the writing of the filtered captured data to a file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '16, 15:41</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '16, 12:10</p></div></div><div id="comments-container-53947" class="comments-container"></div><div id="comment-tools-53947" class="comment-tools"></div><div class="clear"></div><div id="comment-53947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

