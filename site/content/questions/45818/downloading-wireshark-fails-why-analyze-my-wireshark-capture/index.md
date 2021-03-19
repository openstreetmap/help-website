+++
type = "question"
title = "Downloading WireShark Fails - Why? Analyze my WireShark Capture"
description = '''I wanted to download the latest stable version for 64-bit Win. The download failed. I tried the Beta/Dev version links, both 32 and 64-bit, and tried 32-bit Win. ALL FAILED. I obtained and installed the latest version of WireShark for 64-bit Windows and installed it on the same machine that the down...'''
date = "2015-09-12T20:04:00Z"
lastmod = "2015-09-13T02:41:00Z"
weight = 45818
keywords = [ "download", "failed", "wireshark.org", "firefox" ]
aliases = [ "/questions/45818" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Downloading WireShark Fails - Why? Analyze my WireShark Capture](/questions/45818/downloading-wireshark-fails-why-analyze-my-wireshark-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45818-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wanted to download the latest stable version for 64-bit Win. The download failed. I tried the Beta/Dev version links, both 32 and 64-bit, and tried 32-bit Win.</p><p>ALL FAILED.</p><p>I obtained and installed the latest version of WireShark for 64-bit Windows and installed it on the same machine that the downloads had failed. All other internet and network activity seems normal.</p><p>I started the capture and then started FireFox and went directly to wireshark.org, then the download page, and tried to download the latest stable version for 64-bit Windows.</p><p>The capture shows the failed download, and I stopped the capture as the "hourglass" (or whatever they call the icon nowadays) was displayed and the download never started.</p><p>Why? Why do all the download attempts fail?</p><p>I think I see the "conversation" at about Frame #47</p><p>I can capture more attempts, if needed. Thank you, in advance, for any insight anyone can provide on this.</p><p>[* LINK TO CAPTURE.... --REMOVED][1]</p></div><div id="question-tags" class="tags-container tags">download failed wireshark.org firefox</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '15, 20:04</strong></p><img src="https://secure.gravatar.com/avatar/9b9b8e32ead1717b0ccc959d75ef9ad0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddfoye&#39;s gravatar image" /><p>ddfoye<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddfoye has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Sep '15, 11:34</p></div></div><div id="comments-container-45818" class="comments-container"></div><div id="comment-tools-45818" class="comment-tools"></div><div class="clear"></div><div id="comment-45818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45820"></span>

<div id="answer-container-45820" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45820-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From your capture (tcp streams 69, 70 &amp; 71) it appears that you were trying to download from the eu Wireshark mirror (1.eu.dl.wireshark.org) and for some reason your browser was unable to connect to that site.</p><p>You were able to connect to the main Wireshark site (tcp stream 55), so it's likely there was a temporary issue with the eu download mirror. On the <a href="https://www.wireshark.org/download.html">download</a> page there is a list of other mirrors so if you still can't get to the eu mirror (it works for me now) try another site.</p><p>On a side note your capture contains a lot of traffic that's not relevant to your question and although it doesn't seem to be the case this time, you could be leaving sensitive information about your network to the world. You should review capture contents before making them public.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '15, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45820" class="comments-container"></div><div id="comment-tools-45820" class="comment-tools"></div><div class="clear"></div><div id="comment-45820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

