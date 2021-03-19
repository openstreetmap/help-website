+++
type = "question"
title = "Viewing RSSI value using wireshark windows version"
description = '''I try to view RSSI value in wireshark windows version (v1.8.5). So what is the first thing that I should do? Thx'''
date = "2013-02-12T15:57:00Z"
lastmod = "2013-02-12T17:23:00Z"
weight = 18568
keywords = [ "qwe" ]
aliases = [ "/questions/18568" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Viewing RSSI value using wireshark windows version](/questions/18568/viewing-rssi-value-using-wireshark-windows-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18568-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I try to view RSSI value in wireshark windows version (v1.8.5). So what is the first thing that I should do? Thx</p></div><div id="question-tags" class="tags-container tags">qwe</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '13, 15:57</strong></p><img src="https://secure.gravatar.com/avatar/0a3865cbc361c1abb797fdc4062f3dd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="awi216&#39;s gravatar image" /><p>awi216<br />
<span class="score" title="10 reputation points">10</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="awi216 has no accepted answers">0%</span></p></div></div><div id="comments-container-18568" class="comments-container"></div><div id="comment-tools-18568" class="comment-tools"></div><div class="clear"></div><div id="comment-18568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18569"></span>

<div id="answer-container-18569" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18569-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The first thing that you should do is either</p><ul><li>download and install <a href="http://www.microsoft.com/en-us/download/details.aspx?id=4865">Microsoft Network Monitor</a>, use it to capture traffic, and either read its captures in Network Monitor or save them and read them in Wireshark;</li><li>buy an <a href="http://www.riverbed.com/us/products/cascade/wireshark_enhancements/airpcap.php">AirPcap</a> adapter and use it to capture traffic in Wireshark</li></ul><p>WinPcap doesn't support capturing in monitor mode, or capturing with any radio information such as signal strength, with regular 802.11 adapters, and Wireshark uses WinPcap for traffic capture on Windows, so Wireshark doesn't support getting radio information when capturing on Windows unless you have an AirPcap adapter.</p><p>(I guess a third thing you could do is "download some version of Linux or *BSD and install it on your machine", but that's probably a less convenient alternative. :-))</p><p>Note, by the way, that the "RSSI" value might not show up in a column in the packet list, and, in the packet details, might be a <em>signed</em> value, either in decibels from some arbitrary reference point (dB) or in decibels from 1 milliwatt (dBm), rather than the unsigned "RSSI" values referred to by some places in the IEEE 802.11 specification. Those unsigned values might not be available on many platforms (and are not, as far as I know, any more useful than the decibel values).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '13, 17:23</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-18569" class="comments-container"><span id="18618"></span><div id="comment-18618" class="comment"><div id="post-18618-score" class="comment-score"></div><div class="comment-text"><p>Thx for reply</p><p>Actually, right now I already doing what u have suggested, exclude the AirPcap adapter. And will choose what is the best method, to get the best result. I have seen someone from google using Wireshark and get the RSSI value, and it look neat and proper :)</p></div><div id="comment-18618-info" class="comment-info"><span class="comment-age">(13 Feb '13, 15:21)</span> awi216</div></div><span id="18620"></span><div id="comment-18620" class="comment"><div id="post-18620-score" class="comment-score"></div><div class="comment-text"><p>They might have gotten it either by capturing on Linux or OS X or *BSD, or by reading a capture file from some other application.</p></div><div id="comment-18620-info" class="comment-info"><span class="comment-age">(13 Feb '13, 16:51)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-18569" class="comment-tools"></div><div class="clear"></div><div id="comment-18569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

