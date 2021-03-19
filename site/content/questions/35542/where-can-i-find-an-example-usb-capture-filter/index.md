+++
type = "question"
title = "where can I find an example usb capture filter"
description = '''Hi, there are lot of examples for capture filtering at http://wiki.wireshark.org/CaptureFilters but unfortunately none of them is referred to usb. Shall you give me an example, please?'''
date = "2014-08-18T10:41:00Z"
lastmod = "2014-08-25T16:04:00Z"
weight = 35542
keywords = [ "usb" ]
aliases = [ "/questions/35542" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [where can I find an example usb capture filter](/questions/35542/where-can-i-find-an-example-usb-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35542-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, there are lot of examples for capture filtering at <a href="http://wiki.wireshark.org/CaptureFilters">http://wiki.wireshark.org/CaptureFilters</a> but unfortunately none of them is referred to usb. Shall you give me an example, please?</p></div><div id="question-tags" class="tags-container tags">usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '14, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/8c8be422bf878b6e489fb2cf79f1c5ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="uhum2004&#39;s gravatar image" /><p>uhum2004<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="uhum2004 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Aug '14, 10:42</p></div></div><div id="comments-container-35542" class="comments-container"></div><div id="comment-tools-35542" class="comment-tools"></div><div class="clear"></div><div id="comment-35542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35734"></span>

<div id="answer-container-35734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35734-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't use a <strong>capture</strong> filter on USB data, as that's not implemented by libpcap (and/or usbmon), the capture library of Wireshark. The reason: libpcap uses BPF (Berkely Packet Filter) to implement <strong>capture</strong> filters and that works mainly for network protocols. So, no USB data <strong>capture</strong> filtering without a a massive rewrite of libpcap.</p><p>As a result, you can use <strong>display</strong> filters for USB traffic in Wireshark and/or tshark, but not <strong>capture</strong> filters.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '14, 16:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35734" class="comments-container"><span id="35740"></span><div id="comment-35740" class="comment"><div id="post-35740-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Kurt! But how can I capture the registering traffic? I guess I have to have my device disconnected, then start Wireshark to see registering progress. However, at the moment of starting Wireshark it is not known what address will be given by operating system. What capture filter can be used then?</p></div><div id="comment-35740-info" class="comment-info"><span class="comment-age">(25 Aug '14, 19:02)</span> uhum2004</div></div><span id="35741"></span><div id="comment-35741" class="comment"><div id="post-35741-score" class="comment-score"></div><div class="comment-text"><p>Perhaps the Wireshark <a href="http://wiki.wireshark.org/CaptureSetup/USB">USB capture setup</a> wiki page will be of use to you?</p></div><div id="comment-35741-info" class="comment-info"><span class="comment-age">(25 Aug '14, 19:32)</span> cmaynard ♦♦</div></div><span id="35743"></span><div id="comment-35743" class="comment"><div id="post-35743-score" class="comment-score"></div><div class="comment-text"><blockquote><p>However, at the moment of starting Wireshark it is not known what address will be given by operating system.</p></blockquote><p>correct.</p><p>I don't believe you will be able to do what you are trying to with a standard PC and Wireshark. That's what special USB capture devices are made for, especially if you want to monitor the phase while the USB device is connected to the PC.</p></div><div id="comment-35743-info" class="comment-info"><span class="comment-age">(26 Aug '14, 02:36)</span> Kurt Knochner ♦</div></div><span id="35748"></span><div id="comment-35748" class="comment"><div id="post-35748-score" class="comment-score">1</div><div class="comment-text"><p>if you are using Windows, you can follow the USBPcap guide found here: <a href="http://desowin.org/usbpcap/tour.html">http://desowin.org/usbpcap/tour.html</a> . As the device will always connect to the same root hub, you will be able to see the enumeration. I guess you should be able to do more or less the same thing with usbmon (as I already saw some Linux captures with the device enumeration).</p></div><div id="comment-35748-info" class="comment-info"><span class="comment-age">(26 Aug '14, 03:28)</span> Pascal Quantin</div></div></div><div id="comment-tools-35734" class="comment-tools"></div><div class="clear"></div><div id="comment-35734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

