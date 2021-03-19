+++
type = "question"
title = "Extract Packet arrival time and capture length of bytes at that instant"
description = '''From my test.cap file I need to extract the &quot;timestamp of packet arrival&quot; and &quot;capture length&quot; field What field parameter need to be given to tshark for extracting and saving as .txt or .csv'''
date = "2015-11-18T04:34:00Z"
lastmod = "2015-11-18T04:44:00Z"
weight = 47705
keywords = [ "tshark" ]
aliases = [ "/questions/47705" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Extract Packet arrival time and capture length of bytes at that instant](/questions/47705/extract-packet-arrival-time-and-capture-length-of-bytes-at-that-instant)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47705-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From my test.cap file I need to extract the "timestamp of packet arrival" and "capture length" field What field parameter need to be given to tshark for extracting and saving as .txt or .csv</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '15, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/f2daecc4e0588d9138ade2d50de19a37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hawa&#39;s gravatar image" /><p>hawa<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hawa has no accepted answers">0%</span></p></div></div><div id="comments-container-47705" class="comments-container"></div><div id="comment-tools-47705" class="comment-tools"></div><div class="clear"></div><div id="comment-47705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47707"></span>

<div id="answer-container-47707" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47707-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>'frame.time' and 'frame.cap_len' are your candidates (don't be surprised by frame.time's verbosity, maybe you'd prefer 'frame.time_epoch').</p><p>Hint: use the "graphic" Wireshark, choose a packet, and go to the dissection window. When you click on a line in expanded view, you'll see the matching protocol field name, if it exists, in the bottommost status line of the window.</p><p>So the parameters to tshark will be <code>-T fields -e frame.time -e frame.cap_len</code> .</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '15, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Nov '15, 04:46</p></div></div><div id="comments-container-47707" class="comments-container"><span id="47708"></span><div id="comment-47708" class="comment"><div id="post-47708-score" class="comment-score"></div><div class="comment-text"><p>thanks. it did the trick</p></div><div id="comment-47708-info" class="comment-info"><span class="comment-age">(18 Nov '15, 04:52)</span> hawa</div></div><span id="47709"></span><div id="comment-47709" class="comment"><div id="post-47709-score" class="comment-score"></div><div class="comment-text"><p>OK. Although it may seem weird, the "thumb up" icon is raising my karma (thank you), but the checkmark icon marks the answer as useful for the others (questions with accepted answers are marked with different colour in the list). While anyone can press "thumbs up", only the one who asked the question can mark the answer as accepted. Please take one more click.</p></div><div id="comment-47709-info" class="comment-info"><span class="comment-age">(18 Nov '15, 04:56)</span> sindy</div></div></div><div id="comment-tools-47707" class="comment-tools"></div><div class="clear"></div><div id="comment-47707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

