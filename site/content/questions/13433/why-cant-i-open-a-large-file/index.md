+++
type = "question"
title = "Why can&#x27;t I open a large file?"
description = '''I am using Wireshark version 1.8, newly installed. Wireshark is crashing when trying to open a 400MB file. It gets to roughly 47%, then dies. I get a Microsoft Visual C++ Runtime library error.'''
date = "2012-08-07T10:37:00Z"
lastmod = "2012-08-07T10:58:00Z"
weight = 13433
keywords = [ "crash", "error" ]
aliases = [ "/questions/13433" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why can't I open a large file?](/questions/13433/why-cant-i-open-a-large-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13433-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark version 1.8, newly installed. Wireshark is crashing when trying to open a 400MB file. It gets to roughly 47%, then dies.</p><p>I get a Microsoft Visual C++ Runtime library error.</p></div><div id="question-tags" class="tags-container tags">crash error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '12, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/843009f25221dda304d6b04c760effbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="drumhrd&#39;s gravatar image" /><p>drumhrd<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="drumhrd has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Aug '12, 14:02</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-13433" class="comments-container"></div><div id="comment-tools-13433" class="comment-tools"></div><div class="clear"></div><div id="comment-13433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13434"></span>

<div id="answer-container-13434" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13434-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use the command line tool <em>editcap</em> to split the large file into smaller files. Editcap was installed when you installed Wireshark. Even if you could open the 400 MB file, you would find it difficult to work with because of its size. In particular, applying and clearing display filters would take a very long time.</p><p>You can find the editcap syntax by clicking on Help &gt; Manual Pages &gt; Editcap from within Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '12, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-13434" class="comments-container"><span id="13470"></span><div id="comment-13470" class="comment"><div id="post-13470-score" class="comment-score"></div><div class="comment-text"><p>Wireshark is /probably/ dying because it's running out of memory. See <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">OutOfMemory</a>.</p><p>Note that it's not uncommon for me to analyze 400 Mb capture files but I have a 64-bit OS (and 64-bit Wireshark) and lots of RAM. (Note here too that there have been reports that 64-bit Wireshark on 64-bit Windows is NOT able to actually take advantage of lots of RAM; I think there's a bug report about that.)</p></div><div id="comment-13470-info" class="comment-info"><span class="comment-age">(08 Aug '12, 06:45)</span> JeffMorriss ♦</div></div><span id="13472"></span><div id="comment-13472" class="comment"><div id="post-13472-score" class="comment-score"></div><div class="comment-text"><p>Bug mentioned: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5979">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5979</a></p></div><div id="comment-13472-info" class="comment-info"><span class="comment-age">(08 Aug '12, 07:25)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13434" class="comment-tools"></div><div class="clear"></div><div id="comment-13434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

