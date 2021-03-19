+++
type = "question"
title = "WireShark crashes on save when not stopped"
description = '''WireShark 1.6.2, including WinPcap. Also happens with 1.6.1. When I close the program, and answer the prompt to save, it appears to save, and then throws a Run-Time library exception. If I stop the capture and then exit/save, it works. This used to work fine. Any ideas? Thank you. Alex'''
date = "2011-09-18T18:49:00Z"
lastmod = "2011-09-19T08:14:00Z"
weight = 6440
keywords = [ "onsave", "nostop", "crash", "wireshark" ]
aliases = [ "/questions/6440" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WireShark crashes on save when not stopped](/questions/6440/wireshark-crashes-on-save-when-not-stopped)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6440-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>WireShark 1.6.2, including WinPcap. Also happens with 1.6.1. When I close the program, and answer the prompt to save, it appears to save, and then throws a Run-Time library exception. If I stop the capture and then exit/save, it works. This used to work fine. Any ideas? Thank you.</p><p>Alex</p></div><div id="question-tags" class="tags-container tags">onsave nostop crash wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '11, 18:49</strong></p><img src="https://secure.gravatar.com/avatar/9ed2deec46b7fe9da734109d50869674?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="awinguru&#39;s gravatar image" /><p>awinguru<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="awinguru has no accepted answers">0%</span></p></div></div><div id="comments-container-6440" class="comments-container"><span id="6444"></span><div id="comment-6444" class="comment"><div id="post-6444-score" class="comment-score"></div><div class="comment-text"><p>ERROR:file.c:376:cf_reset_state: assertion failed: (cf-&gt;state != FILE_READ_IN_PROGRESS) Aborted (core dumped) yes this is the error that we get</p></div><div id="comment-6444-info" class="comment-info"><span class="comment-age">(19 Sep '11, 04:57)</span> flashkicker</div></div></div><div id="comment-tools-6440" class="comment-tools"></div><div class="clear"></div><div id="comment-6440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6447"></span>

<div id="answer-container-6447" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6447-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have encountered <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5776">bug 5776</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '11, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-6447" class="comments-container"><span id="6451"></span><div id="comment-6451" class="comment"><div id="post-6451-score" class="comment-score"></div><div class="comment-text"><p>Is there a solution ??</p></div><div id="comment-6451-info" class="comment-info"><span class="comment-age">(19 Sep '11, 21:46)</span> flashkicker</div></div><span id="6452"></span><div id="comment-6452" class="comment"><div id="post-6452-score" class="comment-score"></div><div class="comment-text"><p>I think in GTk if we make the save hidden until unless we stop then the work is completed..........</p></div><div id="comment-6452-info" class="comment-info"><span class="comment-age">(19 Sep '11, 21:57)</span> flashkicker</div></div><span id="6461"></span><div id="comment-6461" class="comment"><div id="post-6461-score" class="comment-score"></div><div class="comment-text"><p>The bug is still open so there's no resolution yet.</p></div><div id="comment-6461-info" class="comment-info"><span class="comment-age">(20 Sep '11, 06:18)</span> cmaynard ♦♦</div></div><span id="6464"></span><div id="comment-6464" class="comment"><div id="post-6464-score" class="comment-score"></div><div class="comment-text"><p>ohk ok .....</p></div><div id="comment-6464-info" class="comment-info"><span class="comment-age">(20 Sep '11, 07:55)</span> flashkicker</div></div></div><div id="comment-tools-6447" class="comment-tools"></div><div class="clear"></div><div id="comment-6447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

