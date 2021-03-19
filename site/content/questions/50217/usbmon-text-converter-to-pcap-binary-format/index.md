+++
type = "question"
title = "? &quot;usbmon text&quot; converter to PCAP binary format"
description = '''I&#x27;m designing with an embedded USB Host that isn&#x27;t linux (STM32F4 with 196Kram) and looking for a format for implementing a dump of the USB wirelevel transaction that can be transferred through a UART interface to a host for analysis by wireshark. The primary purpose is to debug USB device enumerati...'''
date = "2016-02-15T13:52:00Z"
lastmod = "2016-02-15T16:22:00Z"
weight = 50217
keywords = [ "pcap", "usbmon" ]
aliases = [ "/questions/50217" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [? "usbmon text" converter to PCAP binary format](/questions/50217/usbmon-text-converter-to-pcap-binary-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50217-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm designing with an embedded USB Host that isn't linux (STM32F4 with 196Kram) and looking for a format for implementing a dump of the USB wirelevel transaction that can be transferred through a UART interface to a host for analysis by wireshark. The primary purpose is to debug USB device enumerations and compare them against a linux hosts enumeration.</p><p>The embedded system has a well buffered UART @115Kbaud, so the simplest, assuming a relatively low speed USB Host interface, is to capture USB transactions on the UART ASCII output sending to a slower ram buffer and then when they are send to the console capture them via a terminal logger.</p><p>The "usbmon text" interface is well defined, but I haven't found anyway of converting this to a wireshark (PCAP?) format. I'm just wondering if anybody knows of a converter that can take "usbmon text" format and convert to a PCAP format, or anyother ASCII format/converter to PCAP. Many thanks.</p></div><div id="question-tags" class="tags-container tags">pcap usbmon</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '16, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/801e862c3ecabc06b20c55469ec3d6c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neilh&#39;s gravatar image" /><p>neilh<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neilh has no accepted answers">0%</span></p></div></div><div id="comments-container-50217" class="comments-container"><span id="50218"></span><div id="comment-50218" class="comment"><div id="post-50218-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The "usbmon text" interface is well defined</p></blockquote><p>Are you referring to the <a href="https://github.com/torvalds/linux/blob/master/Documentation/usb/usbmon.txt">Linux usbmon text format</a>, or to something else?</p></div><div id="comment-50218-info" class="comment-info"><span class="comment-age">(15 Feb '16, 13:56)</span> Guy Harris ♦♦</div></div><span id="50221"></span><div id="comment-50221" class="comment"><div id="post-50221-score" class="comment-score"></div><div class="comment-text"><p>Hello Guy, yes the "Linux usbmon text format" outputs a text string, which would work well over an ASCII UART console interface.</p><p>However as far as I can see there isn't a way of capturing this and inputting it into wireshark? Maybe I've missed something?</p><p>Hence, I'm wondering if there is a way of converting it into a format that wireshark accepts?</p><p>thanks</p></div><div id="comment-50221-info" class="comment-info"><span class="comment-age">(15 Feb '16, 16:09)</span> neilh</div></div></div><div id="comment-tools-50217" class="comment-tools"></div><div class="clear"></div><div id="comment-50217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50222"></span>

<div id="answer-container-50222" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50222-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know of any converter program that exists now, <em>but</em> libpcap 1) can capture on Linux USB if it only gets the text format (the binary format is better, but it does handle the text format) and 2) libpcap obviously handles pcap, so somebody could start with the <code>usb_read_linux()</code> routine in libpcap's <code>pcap-usb-linux.c</code> and turn it into something that reads the text format and writes out a pcap file with a <a href="http://www.tcpdump.org/linktypes.html">link-layer header type</a> of <code>LINKTYPE_USB_LINUX</code>.</p><p>Other possibilities are:</p><ul><li>write a module for libpcap that duplicates what <code>pcap-usb-linux.c</code> does, but does it reading from a text file rather than reading from the Linux text USB capture device, and build Wireshark using that version of libpcap - that'd allow you to directly capture from the serial port in Wireshark (or any other program built with that version of libpcap);</li><li>write an "extcap" program that does much the same, and have Wireshark use that to capture.</li></ul><p>Unfortunately, there's not much in the way of documentation for either of those two processes; the first doesn't let you do that as a plugin (libpcap currently doesn't support plugin modules, so you'd need to build libpcap from scratch and link programs with it), and the latter does but isn't well documented (and requires Wireshark 2.x).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '16, 16:22</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-50222" class="comments-container"><span id="50223"></span><div id="comment-50223" class="comment"><div id="post-50223-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy, many thanks for the quick response. I was just checking to see if I had missed anything for an easy solution. Thanks for the pointers, I'm also looking at another couple of options. If I can figure out a way through the ASCII stream (Zmodem) then maybe I can also make the binary pcap work. Thanks again.</p></div><div id="comment-50223-info" class="comment-info"><span class="comment-age">(15 Feb '16, 16:56)</span> neilh</div></div></div><div id="comment-tools-50222" class="comment-tools"></div><div class="clear"></div><div id="comment-50222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

