+++
type = "question"
title = "Keep pipe in interface list"
description = '''I am capturing from &#92;&#92;.&#92;pipe&#92;wireshark using a utility program. Right now, I go to Capture Options-&amp;gt;Manage Interfaces and add the new pipe. Capturing here is no problem. However, the next time I open Wireshark, the pipe has gone from the list and I need to go through the same procedure to add the...'''
date = "2014-07-11T06:41:00Z"
lastmod = "2014-07-15T03:39:00Z"
weight = 34601
keywords = [ "pipe", "capture" ]
aliases = [ "/questions/34601" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Keep pipe in interface list](/questions/34601/keep-pipe-in-interface-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34601-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am capturing from <code>\\.\pipe\wireshark</code> using a utility program. Right now, I go to Capture Options-&gt;Manage Interfaces and add the new pipe. Capturing here is no problem.</p><p>However, the next time I open Wireshark, the pipe has gone from the list and I need to go through the same procedure to add the pipe again.</p><p>Is there any way that I can make the pipe persist in the interface list? Doing this every time I open Wireshark is very inconvenient.</p></div><div id="question-tags" class="tags-container tags">pipe capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '14, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/2973b6be28bed95434b4ee70047a5735?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="burwell&#39;s gravatar image" /><p>burwell<br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="burwell has one accepted answer">100%</span></p></div></div><div id="comments-container-34601" class="comments-container"></div><div id="comment-tools-34601" class="comment-tools"></div><div class="clear"></div><div id="comment-34601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34654"></span>

<div id="answer-container-34654" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34654-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please start Wireshark like this:</p><blockquote><p>wireshark -ni <code>\\.\pipe\wireshark</code></p></blockquote><p>You will then see the pipe in the list of interfaces.</p><p>If you want to start capturing immediately, you can run</p><blockquote><p>wireshark -ni <code>\\.\pipe\wireshark</code> -k</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '14, 03:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jul '14, 03:40</p></div></div><div id="comments-container-34654" class="comments-container"><span id="34678"></span><div id="comment-34678" class="comment"><div id="post-34678-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply, Kurt. Is there any way to do this without starting from the command line?</p></div><div id="comment-34678-info" class="comment-info"><span class="comment-age">(15 Jul '14, 12:39)</span> burwell</div></div><span id="34685"></span><div id="comment-34685" class="comment"><div id="post-34685-score" class="comment-score"></div><div class="comment-text"><p>I don't think so. I believe it would require a code change.</p></div><div id="comment-34685-info" class="comment-info"><span class="comment-age">(15 Jul '14, 12:57)</span> Kurt Knochner ♦</div></div><span id="34691"></span><div id="comment-34691" class="comment"><div id="post-34691-score" class="comment-score"></div><div class="comment-text"><p>Okay. I'll accept your answer since I didn't specify that I needed it to be non-command line and there doesn't seem to be another way. Thanks!</p></div><div id="comment-34691-info" class="comment-info"><span class="comment-age">(15 Jul '14, 14:04)</span> burwell</div></div><span id="45839"></span><div id="comment-45839" class="comment"><div id="post-45839-score" class="comment-score"></div><div class="comment-text"><p>As the form of the pipe name you gave suggests you run Wireshark on Windows, have you noticed that application "shortcuts" (on the desktop, in the Start menu, or anywhere where you create it) are actually command line wrappers? If you open properties of the shortcut, you'll see that there is a command line starting the application. Modify it the way Kurt has suggested and the next time you click the shortcut, your pipe will be in the interface list.</p></div><div id="comment-45839-info" class="comment-info"><span class="comment-age">(14 Sep '15, 22:17)</span> sindy</div></div></div><div id="comment-tools-34654" class="comment-tools"></div><div class="clear"></div><div id="comment-34654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

