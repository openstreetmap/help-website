+++
type = "question"
title = "Unable to handle timestamp output in Excel"
description = '''Hello, I have the following command, and the problem is that I cannot operate in Excel with the date. Can anybody give a clue? thanks tshark -r /home/javier/Documents/capture -i -T fields -e frame.time -e col.info -e wlan.sa -e ip.src -E header=y -E separator=, -E quote=d -E occurrence=f &amp;gt; /home/...'''
date = "2014-10-23T16:09:00Z"
lastmod = "2014-10-25T02:43:00Z"
weight = 37323
keywords = [ "timestamp", "excel", "tshark" ]
aliases = [ "/questions/37323" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to handle timestamp output in Excel](/questions/37323/unable-to-handle-timestamp-output-in-excel)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37323-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have the following command, and the problem is that I cannot operate in Excel with the date. Can anybody give a clue?</p><p>thanks</p><p>tshark -r /home/javier/Documents/capture -i -T fields -e frame.time -e col.info -e wlan.sa -e ip.src -E header=y -E separator=, -E quote=d -E occurrence=f &gt; /home/javier/Documents/capture.csv</p><p>BR</p></div><div id="question-tags" class="tags-container tags">timestamp excel tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '14, 16:09</strong></p><img src="https://secure.gravatar.com/avatar/52f8d63ea874c7a4a7eb7608ce8ce221?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escalanterj&#39;s gravatar image" /><p>escalanterj<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escalanterj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 24 Oct '14, 00:51</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-37323" class="comments-container"></div><div id="comment-tools-37323" class="comment-tools"></div><div class="clear"></div><div id="comment-37323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37344"></span>

<div id="answer-container-37344" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37344-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi BR,</p><p>Format the cells in the time column with the Custom format hh:mm:ss.000</p><p>So in Excel do Right Click -&gt; Format Cells... -&gt; Number -&gt; Custom -&gt; Type: and then enter the above format. Unfortunately Excel will only support 3 digits after the decimal place i.e. down to milliseconds.</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '14, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-37344" class="comments-container"></div><div id="comment-tools-37344" class="comment-tools"></div><div class="clear"></div><div id="comment-37344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

