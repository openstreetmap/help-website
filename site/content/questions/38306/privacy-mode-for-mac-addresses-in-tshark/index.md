+++
type = "question"
title = "Privacy mode for MAC addresses in tshark?"
description = '''If I use airodump-ng mon0 -w myfile --output-format cap  to capture network traffic, it shows (among others) the MAC address and the SSID in real time, and I can see them in plaintext. For example: 11:11:11:11:11:11 Device1 22:22:22:22:22:22 Device2  It furthermore stores the information in myfile-0...'''
date = "2014-12-03T08:53:00Z"
lastmod = "2014-12-03T10:04:00Z"
weight = 38306
keywords = [ "privacy", "tshark", "mac-address" ]
aliases = [ "/questions/38306" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Privacy mode for MAC addresses in tshark?](/questions/38306/privacy-mode-for-mac-addresses-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38306-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I use</p><pre><code>airodump-ng mon0 -w myfile --output-format cap</code></pre><p>to capture network traffic, it shows (among others) the MAC address and the SSID in real time, and I can see them in plaintext. For example:</p><pre><code>11:11:11:11:11:11 Device1
22:22:22:22:22:22 Device2</code></pre><p>It furthermore stores the information in myfile-01.cap.</p><p>However, if I now use</p><pre><code>tshark -r myfile-01.cap</code></pre><p>to access the information stored in the file, for <em>some</em> MAC addresses the first part of it is "anonymized", like this:</p><pre><code>11:11:11:11:11:11 Device1
HonHaiPr_22:22:22 Device2</code></pre><p>Is this a privacy feature? If it is, according to which rules is this feature applied to a MAC address? Can I turn it off (or on for all MAC addresses)?</p></div><div id="question-tags" class="tags-container tags">privacy tshark mac-address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '14, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/39130ccc607910d16111c7bdee4898a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baukran&#39;s gravatar image" /><p>baukran<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baukran has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Dec '14, 08:54</p></div></div><div id="comments-container-38306" class="comments-container"></div><div id="comment-tools-38306" class="comment-tools"></div><div class="clear"></div><div id="comment-38306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38309"></span>

<div id="answer-container-38309" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38309-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The first part of the MAC address is the vendor code and Wireshark is helpfully replacing the numeric value with the textual equivalent if the vendor is known from the list installed along with Wireshark. This can be controlled by using the Name Resolution preferences "Resolve MAC addresses" option.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '14, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38309" class="comments-container"></div><div id="comment-tools-38309" class="comment-tools"></div><div class="clear"></div><div id="comment-38309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

