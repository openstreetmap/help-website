+++
type = "question"
title = "Why Wireshark 2.0.1 cannot open a named pipe?"
description = '''I created a pipe &quot;&#92;.&#92;pipe&#92;wireshark&quot; with VB.net and tried to add and open it in Wireshark, but get &quot;The capture session on &quot;&#92;.pipe&#92;wireshark&quot;could not be started due to error on pipe open: The system cannot find the file specified. (error 2). I&#x27;ve test the pipe with command line pipe tool(NamedPipe...'''
date = "2016-01-11T17:20:00Z"
lastmod = "2016-01-12T10:15:00Z"
weight = 49107
keywords = [ "josh117" ]
aliases = [ "/questions/49107" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why Wireshark 2.0.1 cannot open a named pipe?](/questions/49107/why-wireshark-201-cannot-open-a-named-pipe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49107-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I created a pipe "\.\pipe\wireshark" with VB.net and tried to add and open it in Wireshark, but get "The capture session on "\.pipe\wireshark"could not be started due to error on pipe open: The system cannot find the file specified. (error 2).</p><p>I've test the pipe with command line pipe tool(NamedPipeClient.exe) and VB.net pipe client tool I created, and "\.\pipe\wireshark" pipe can be connected and works fine with both tools.</p><p>Why Wireshark 2.0.1 cannot open a named pipe?</p><p>Thanks, Josh</p></div><div id="question-tags" class="tags-container tags">josh117</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '16, 17:20</strong></p><img src="https://secure.gravatar.com/avatar/b8478b0c92d05d2409726bed5e32c0b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="josh117&#39;s gravatar image" /><p>josh117<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="josh117 has one accepted answer">100%</span></p></div></div><div id="comments-container-49107" class="comments-container"><span id="49113"></span><div id="comment-49113" class="comment"><div id="post-49113-score" class="comment-score"></div><div class="comment-text"><ol><li><p>Are you sure that it is a specific issue of 2.0.1 or you simply haven't tried with any other Wireshark version? Because I have tested it (but not with VB!) with other versions of Wireshark before and it worked, and Wireshark's extcap mechanism also relies on named pipes, so it should work.</p></li><li><p>What method exactly have you used to tell Wireshark that it should read from the named pipe?</p></li></ol></div><div id="comment-49113-info" class="comment-info"><span class="comment-age">(12 Jan '16, 02:09)</span> sindy</div></div></div><div id="comment-tools-49107" class="comment-tools"></div><div class="clear"></div><div id="comment-49107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49132"></span>

<div id="answer-container-49132" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49132-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I figured it out. Wireshark 2.0.1 is fine. I should use NamedPipeServerStream("wireshark", PipeDirection.Out) instead of NamedPipeServerStream("\\.\pipe\wireshark", PipeDirection.Out) in my code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '16, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/b8478b0c92d05d2409726bed5e32c0b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="josh117&#39;s gravatar image" /><p>josh117<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="josh117 has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jan '16, 10:17</p></div></div><div id="comments-container-49132" class="comments-container"></div><div id="comment-tools-49132" class="comment-tools"></div><div class="clear"></div><div id="comment-49132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

