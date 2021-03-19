+++
type = "question"
title = "&#x27;How do I set the capture to auto save periodically?"
description = '''How do I set the capture to auto save periodically so WireShark doesn&#x27;t crash?'''
date = "2011-04-02T13:29:00Z"
lastmod = "2011-04-02T13:52:00Z"
weight = 3291
keywords = [ "capture", "save", "auto" ]
aliases = [ "/questions/3291" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# ['How do I set the capture to auto save periodically?](/questions/3291/how-do-i-set-the-capture-to-auto-save-periodically)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3291-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I set the capture to auto save periodically so WireShark doesn't crash?</p></div><div id="question-tags" class="tags-container tags">capture save auto</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '11, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/09bc8744dad36b7148613ecf15680d2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bkready&#39;s gravatar image" /><p>bkready<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bkready has no accepted answers">0%</span></p></div></div><div id="comments-container-3291" class="comments-container"></div><div id="comment-tools-3291" class="comment-tools"></div><div class="clear"></div><div id="comment-3291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3295"></span>

<div id="answer-container-3295" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3295-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Open up the capture options dialog (second button on the toolbar, or "Capture" -&gt; "Options" in the main menu) and set a file name. Then check "Use multiple files" and select a good file size for "Next file every ... megabytes". You could also go for "Next file every ... minutes" but I only recommend doing that when the amount of traffic is very consistent, otherwise the megabyte limits make more sense.</p><p>Finally, to stop your disk from running out of space you might consider to use the "Ring buffer with..." feature. The way it works is that as soon as Wireshark has written the number of files you set it will replace the oldest and continue to capture, overwriting files as needed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '11, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3295" class="comments-container"><span id="3302"></span><div id="comment-3302" class="comment"><div id="post-3302-score" class="comment-score">2</div><div class="comment-text"><p>But keep in mind that Wireshark is a very memory intensive application, so even with using multiple files and ring buffering as <a href="http://ask.wireshark.org/users/145/jasper/">Jasper</a> mentions, it might still crash if it <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">runs out of memory</a>. The recommended solution in that case, especially when performing long-term capturing, is to use <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> instead, which also supports writing to multiple files and ring buffers, but whose memory usage is much lower.</p></div><div id="comment-3302-info" class="comment-info"><span class="comment-age">(03 Apr '11, 08:01)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-3295" class="comment-tools"></div><div class="clear"></div><div id="comment-3295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

