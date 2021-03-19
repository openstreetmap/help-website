+++
type = "question"
title = "Configure Wireshark to generate a file in a specific format every day"
description = '''I would like to configure Wireshark to generate a file in Visual Networks format every day. Is it possible? I just plan to launch Wireshark one time. Thanks.'''
date = "2016-05-12T14:26:00Z"
lastmod = "2016-05-13T03:55:00Z"
weight = 52483
keywords = [ "file-format", "time" ]
aliases = [ "/questions/52483" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Configure Wireshark to generate a file in a specific format every day](/questions/52483/configure-wireshark-to-generate-a-file-in-a-specific-format-every-day)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52483-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to configure Wireshark to generate a file in Visual Networks format every day. Is it possible? I just plan to launch Wireshark one time.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">file-format time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '16, 14:26</strong></p><img src="https://secure.gravatar.com/avatar/3494becea1bec248958f4608019f1b5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="puertas12&#39;s gravatar image" /><p>puertas12<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="puertas12 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 May '16, 14:26</p></div></div><div id="comments-container-52483" class="comments-container"><span id="52485"></span><div id="comment-52485" class="comment"><div id="post-52485-score" class="comment-score"></div><div class="comment-text"><p>You mean start Wireshark once, and for it to create a new capture file every day?</p></div><div id="comment-52485-info" class="comment-info"><span class="comment-age">(12 May '16, 15:16)</span> grahamb ♦</div></div><span id="52499"></span><div id="comment-52499" class="comment"><div id="post-52499-score" class="comment-score"></div><div class="comment-text"><p>That is exactly what I mean</p></div><div id="comment-52499-info" class="comment-info"><span class="comment-age">(13 May '16, 03:41)</span> puertas12</div></div></div><div id="comment-tools-52483" class="comment-tools"></div><div class="clear"></div><div id="comment-52483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52501"></span>

<div id="answer-container-52501" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52501-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Firstly, for long term captures use dumpcap, as Wireshark will run out of memory at some point.</p><p>Next, have a look at dumpcap's <code>-b duration:86400</code> ring buffer option to write a new file every day. note that this won't be synchronised to the exact start of the day, instead it will be 86400 seconds from when dumpcap is started.</p><p>Finally, dumpcap won't write the capture in the format you've requested "Visual Networks", use editcap to post process the capture file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '16, 03:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-52501" class="comments-container"><span id="52508"></span><div id="comment-52508" class="comment"><div id="post-52508-score" class="comment-score"></div><div class="comment-text"><p>A more in-depth discussion, written by Jeremy Stretch, of what @grahamb suggests is at <a href="http://packetlife.net/blog/2011/mar/9/long-term-traffic-capture-wireshark/.">http://packetlife.net/blog/2011/mar/9/long-term-traffic-capture-wireshark/.</a></p></div><div id="comment-52508-info" class="comment-info"><span class="comment-age">(13 May '16, 06:55)</span> coloncm</div></div></div><div id="comment-tools-52501" class="comment-tools"></div><div class="clear"></div><div id="comment-52501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

