+++
type = "question"
title = "File -&gt; Save As function"
description = '''I currently have Wireshark version 1.10.1 and the File -&amp;gt; Save As funtion does not have the features of Selected Packets, Displayed Packets, Range, etc. in order to save filtered packets; it only has the most basic Save As dialog box. This forces me to save the entire array of packet captures to ...'''
date = "2013-09-14T23:02:00Z"
lastmod = "2013-09-14T23:29:00Z"
weight = 24704
keywords = [ "saveas" ]
aliases = [ "/questions/24704" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [File -&gt; Save As function](/questions/24704/file-save-as-function)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24704-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I currently have Wireshark version 1.10.1 and the File -&gt; Save As funtion does not have the features of Selected Packets, Displayed Packets, Range, etc. in order to save filtered packets; it only has the most basic Save As dialog box. This forces me to save the entire array of packet captures to a .pcap file, which may be much larger than what I want. Previous versions of wireshark did have these options.</p><p>How can I recover these options in 1.10.1 as I had in the prior version?</p></div><div id="question-tags" class="tags-container tags">saveas</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '13, 23:02</strong></p><img src="https://secure.gravatar.com/avatar/b3bd2fc506c49e5b95e4bdd2e93f4589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sharkwire1&#39;s gravatar image" /><p>Sharkwire1<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sharkwire1 has no accepted answers">0%</span></p></div></div><div id="comments-container-24704" class="comments-container"></div><div id="comment-tools-24704" class="comment-tools"></div><div class="clear"></div><div id="comment-24704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24705"></span>

<div id="answer-container-24705" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24705-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How can I recover these options in 1.10.1 as I had in the prior version?</p></blockquote><p>Use File -&gt; Export Specified Packets instead. Writing out a subset of the current capture to another file, which doesn't become the current file, is <em>not</em> really a "Save As" function, so it was moved to "Export Specified Packets" in 1.10 (especially given that in 1.10 Wireshark is an "editor" that can modify some capture files by editing packet comments, so that "Save" and "Save As" should function as editor-style save functions).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '13, 23:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Sep '13, 17:57</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-24705" class="comments-container"></div><div id="comment-tools-24705" class="comment-tools"></div><div class="clear"></div><div id="comment-24705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

