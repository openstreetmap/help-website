+++
type = "question"
title = "regarding capture probe request"
description = '''I have a question regarding capture probe request on a single specific channel between access point and client'''
date = "2013-11-09T01:55:00Z"
lastmod = "2013-11-10T03:10:00Z"
weight = 26798
keywords = [ "packet-capture", "wireshark" ]
aliases = [ "/questions/26798" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [regarding capture probe request](/questions/26798/regarding-capture-probe-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26798-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a question regarding capture probe request on a single specific channel between access point and client</p></div><div id="question-tags" class="tags-container tags">packet-capture wireshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '13, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/16470d60489924a990d46b89a72b585c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manish26&#39;s gravatar image" /><p>manish26<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manish26 has no accepted answers">0%</span></p></div></div><div id="comments-container-26798" class="comments-container"><span id="26806"></span><div id="comment-26806" class="comment"><div id="post-26806-score" class="comment-score"></div><div class="comment-text"><p>and your question is...?</p></div><div id="comment-26806-info" class="comment-info"><span class="comment-age">(09 Nov '13, 14:46)</span> Kurt Knochner ♦</div></div><span id="26814"></span><div id="comment-26814" class="comment"><div id="post-26814-score" class="comment-score"></div><div class="comment-text"><p>how to capture??</p></div><div id="comment-26814-info" class="comment-info"><span class="comment-age">(10 Nov '13, 00:18)</span> manish26</div></div></div><div id="comment-tools-26798" class="comment-tools"></div><div class="clear"></div><div id="comment-26798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26817"></span>

<div id="answer-container-26817" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26817-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>O.K. I understand it like this:</p><blockquote><p>You want to <strong>capture probe requests in a wireless network</strong>, on a certain channel</p></blockquote><p>If that is true, you should read the WLAN Capturing Wiki first</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/WLAN">http://wiki.wireshark.org/CaptureSetup/WLAN</a></p></blockquote><p>Basically</p><ul><li>If you want to capture traffic on Windows, you need special hardware (<a href="http://www.riverbed.com/products-solutions/products/network-performance-management/wireshark-enhancement-products/Wireless-Traffic-Packet-Capture.html">AirPcap</a>), as WinPcap (the capture library) on Windows does not support wlan/wifi very well</li><li>If you want to capture on a Unix 'like' system (e.g. Linux), you need a kernel with support for your wlan/wifi card and some additional tools to enable '<a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Monitor_mode">monitor mode</a>'. Those tools (and others) will also allow you to set your wlan/wifi card to a certain channel.</li></ul><p>See also the answer to the following question</p><blockquote><p><a href="http://ask.wireshark.org/questions/26347/unable-to-capture-wireless-traffic-on-monitor-mode-on-ubuntu-1004-version">http://ask.wireshark.org/questions/26347/unable-to-capture-wireless-traffic-on-monitor-mode-on-ubuntu-1004-version</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '13, 03:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Nov '13, 03:28</p></div></div><div id="comments-container-26817" class="comments-container"></div><div id="comment-tools-26817" class="comment-tools"></div><div class="clear"></div><div id="comment-26817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

