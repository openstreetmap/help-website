+++
type = "question"
title = "Export capture file as hex dump"
description = '''I saw, that i can export my traffic capture as plain text, c array, .csv [...] and so on. But i didn&#x27;t found a way to export my whole capture as a hex dump. Like this 000000 00 e0 1e a7 05 6f 00 10 ........ 000008 5a a0 b9 12 08 00 46 00 ........ 000010 03 68 00 00 00 00 0a 2e ........ 000018 ee 33 ...'''
date = "2017-06-20T04:07:00Z"
lastmod = "2017-06-20T05:40:00Z"
weight = 62161
keywords = [ "hexdump", "export" ]
aliases = [ "/questions/62161" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Export capture file as hex dump](/questions/62161/export-capture-file-as-hex-dump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62161-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I saw, that i can export my traffic capture as plain text, c array, .csv [...] and so on. But i didn't found a way to export my whole capture as a hex dump. Like this</p><pre><code>000000 00 e0 1e a7 05 6f 00 10 ........
000008 5a a0 b9 12 08 00 46 00 ........
000010 03 68 00 00 00 00 0a 2e ........
000018 ee 33 0f 19 08 7f 0f 19 ........
000020 03 80 94 04 00 00 10 01 ........
000028 16 a2 0a 00 03 50 00 0c ........
000030 01 01 0f 19 03 80 11 01 ........</code></pre><p>or even this</p><pre><code>000000 00 e0 1e a7 05 6f 00 10
000008 5a a0 b9 12 08 00 46 00
000010 03 68 00 00 00 00 0a 2e
000018 ee 33 0f 19 08 7f 0f 19
000020 03 80 94 04 00 00 10 01
000028 16 a2 0a 00 03 50 00 0c
000030 01 01 0f 19 03 80 11 01</code></pre></div><div id="question-tags" class="tags-container tags">hexdump export</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '17, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/99aa7bab1317487e17831ff692a6cf19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="whateverever&#39;s gravatar image" /><p>whateverever<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="whateverever has no accepted answers">0%</span></p></div></div><div id="comments-container-62161" class="comments-container"></div><div id="comment-tools-62161" class="comment-tools"></div><div class="clear"></div><div id="comment-62161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62166"></span>

<div id="answer-container-62166" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62166-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>File | Export Packet Dissections | As Plain Text...</p><p>Then in the dialog select for Packet Format the Bytes checkbox only (uncheck the other two)</p><p>Select a filename and save.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '17, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62166" class="comments-container"><span id="62174"></span><div id="comment-62174" class="comment"><div id="post-62174-score" class="comment-score"></div><div class="comment-text"><p>Well - thanks. Thats the trick.</p></div><div id="comment-62174-info" class="comment-info"><span class="comment-age">(20 Jun '17, 08:18)</span> whateverever</div></div><span id="62177"></span><div id="comment-62177" class="comment"><div id="post-62177-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-62177-info" class="comment-info"><span class="comment-age">(20 Jun '17, 09:02)</span> Jaap ♦</div></div></div><div id="comment-tools-62166" class="comment-tools"></div><div class="clear"></div><div id="comment-62166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

