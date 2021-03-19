+++
type = "question"
title = "Best way to catch all packets between two devices on local network ethernet/wifi"
description = '''Im facing problem that i have to catch packets between two devices on local network ethernet/ wifi : tv and iphone. Thats mean none of this devices is my computer. What is the most easy &amp;amp; effective solution ? '''
date = "2014-02-27T06:41:00Z"
lastmod = "2014-03-03T02:56:00Z"
weight = 30234
keywords = [ "ethernet", "wifi", "packets", "network", "wireshark" ]
aliases = [ "/questions/30234" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Best way to catch all packets between two devices on local network ethernet/wifi](/questions/30234/best-way-to-catch-all-packets-between-two-devices-on-local-network-ethernetwifi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30234-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im facing problem that i have to catch packets between two devices on local network ethernet/ wifi : tv and iphone. Thats mean none of this devices is my computer. What is the most easy &amp; effective solution ?</p></div><div id="question-tags" class="tags-container tags">ethernet wifi packets network wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '14, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/1d751c6a335be9fb0f1b9fab7f7ffbc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Osel%20Miko%20D%C5%99evorubec&#39;s gravatar image" /><p>Osel Miko Dř...<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Osel Miko Dřevorubec has one accepted answer">100%</span></p></div></div><div id="comments-container-30234" class="comments-container"></div><div id="comment-tools-30234" class="comment-tools"></div><div class="clear"></div><div id="comment-30234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30342"></span>

<div id="answer-container-30342" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30342-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Problem in catching packets between two devices is that they doesnt comming to pc becouse the packets going directly to second device...</p><p>I solved this problem with ARP poisoning tool <a href="http://www.oxid.it/index.html">Cain &amp; Abel</a> , then packets was going to my pc and i was able to catch any packets on local network...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '14, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/1d751c6a335be9fb0f1b9fab7f7ffbc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Osel%20Miko%20D%C5%99evorubec&#39;s gravatar image" /><p>Osel Miko Dř...<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Osel Miko Dřevorubec has one accepted answer">100%</span></p></div></div><div id="comments-container-30342" class="comments-container"></div><div id="comment-tools-30342" class="comment-tools"></div><div class="clear"></div><div id="comment-30342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30328"></span>

<div id="answer-container-30328" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30328-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What is the most easy &amp; effective solution ?</p></blockquote><p>well, that depends on your environment and your skills ;-))</p><p>I guess the TV is connected via ethernet and the iPhone is connected via wlan, like this:</p><pre><code>TV --- ethernet --- WLAN router --- Internet
                        |
iPhone --- wlan/wifi --- </code></pre><p>Now, you have two options:</p><ul><li>capture the ethernet traffic of the TV set</li><li>capture the wlan/wifi traffic of the iPhone</li></ul><p>Capturing the ethernet traffic is (sometimes) easier than wlan/wifi traffic, however, you would need additional equipment (a TAP, or a switch with port mirror functionality), see: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p>Capturing the wlan/wifi traffic on a Windows box requires additional hardware (AirPcap) or special capture software. If you don't have that, I suggest to use Linux to capture wlan/wifi traffic: <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">http://wiki.wireshark.org/CaptureSetup/WLAN</a> (see also numerous tutorials on <a href="http://www.youtube.com/results?search_query=linux%20wlan%20capture&amp;sm=12">youtube</a> and <a href="https://www.google.com/?q=linux+wlan+capture">google</a>).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '14, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30328" class="comments-container"><span id="30341"></span><div id="comment-30341" class="comment"><div id="post-30341-score" class="comment-score"></div><div class="comment-text"><p>Thanks for answer ! I found solution which is probably most easiest.. check my answer</p></div><div id="comment-30341-info" class="comment-info"><span class="comment-age">(03 Mar '14, 02:48)</span> Osel Miko Dř...</div></div></div><div id="comment-tools-30328" class="comment-tools"></div><div class="clear"></div><div id="comment-30328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

