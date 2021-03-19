+++
type = "question"
title = "why does wireshark stop working when I open a file larger than 10MB?"
description = ''''''
date = "2015-02-04T09:56:00Z"
lastmod = "2015-02-04T10:11:00Z"
weight = 39644
keywords = [ "stopped", "filesize", "working" ]
aliases = [ "/questions/39644" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why does wireshark stop working when I open a file larger than 10MB?](/questions/39644/why-does-wireshark-stop-working-when-i-open-a-file-larger-than-10mb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39644-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/ScreenHunter_50_Feb._04_11.44.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">stopped filesize working</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '15, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/3857b1c0a2dd4fa4b96c06723ff2f97f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="opus&#39;s gravatar image" /><p>opus<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="opus has no accepted answers">0%</span></p></img></div></div><div id="comments-container-39644" class="comments-container"></div><div id="comment-tools-39644" class="comment-tools"></div><div class="clear"></div><div id="comment-39644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39645"></span>

<div id="answer-container-39645" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39645-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What version of wireshark, and is this 32 bit or 64 bit? The Help &gt;&gt; About box will give you all the details.</p><p>The problem is likely to be <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">out-of-memory</a>. If you have a 64 bit OS, you can try a 64 bit version of Wireshark if you haven't already, else you can use editcap to split the capture into smaller files.</p><p>There is also the possibility that the issue is a bug in a dissector. You would need to post the capture in a public spot to allow others to check that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '15, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39645" class="comments-container"><span id="39714"></span><div id="comment-39714" class="comment"><div id="post-39714-score" class="comment-score"></div><div class="comment-text"><p>Thanks for responding. The behavior is occurring in version 1.12.2 (64-bit) running on a 64-bit Windows 7 Machine with 4GB of RAM. I'll try using editcap; thanks for the suggestion.</p></div><div id="comment-39714-info" class="comment-info"><span class="comment-age">(09 Feb '15, 07:17)</span> opus</div></div><span id="39719"></span><div id="comment-39719" class="comment"><div id="post-39719-score" class="comment-score"></div><div class="comment-text"><p>For what it's worth, there's at least one report of 64-bit Wireshark on Windows acting as if it didn't have as much address space available as it should have if it's truly 64-bit; I'm not sure whether that's the result of not performing the appropriate ritual sacrifices over the MSVC linker to get the program to <em>really truly</em> be 64-bit or not.</p></div><div id="comment-39719-info" class="comment-info"><span class="comment-age">(09 Feb '15, 14:27)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-39645" class="comment-tools"></div><div class="clear"></div><div id="comment-39645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

