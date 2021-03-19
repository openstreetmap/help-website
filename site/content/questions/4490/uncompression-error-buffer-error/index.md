+++
type = "question"
title = "Uncompression error : buffer error"
description = '''An error occurred while reading the capture file : Uncompression error :buffer error. =&amp;gt; It means that I cannot read data fully?? that is, some data is missing when wireshark reading the capture file, right? What should I do to overcome this error??? I have to read data fully. I am trying to read...'''
date = "2011-06-10T03:14:00Z"
lastmod = "2011-06-10T12:36:00Z"
weight = 4490
keywords = [ "error" ]
aliases = [ "/questions/4490" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Uncompression error : buffer error](/questions/4490/uncompression-error-buffer-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4490-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>An error occurred while reading the capture file : Uncompression error :buffer error.</p><p>=&gt; It means that I cannot read data fully?? that is, some data is missing when wireshark reading the capture file, right?</p><p>What should I do to overcome this error??? I have to read data fully. I am trying to read DARPA 1999 dataset. Please, help me~~!! It's my term project.~~~ please somebody, anybody~</p></div><div id="question-tags" class="tags-container tags">error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '11, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/d5790231d11e06a7eea505c6fc6b714b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pauline%20Koh&#39;s gravatar image" /><p>Pauline Koh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pauline Koh has no accepted answers">0%</span></p></div></div><div id="comments-container-4490" class="comments-container"></div><div id="comment-tools-4490" class="comment-tools"></div><div class="clear"></div><div id="comment-4490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4498"></span>

<div id="answer-container-4498" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4498-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The error exists in zlib (compression library), not Wireshark itself. While processing your file, zlib failed with a buffer error (specifically when trying to inflate a particular chunk), which was passed back to the wiretap file handler, which does not have a capability to correct such an error. You should check to see if your file is malformed, corrupted, or too large to handle. Can you verify your data set against the original?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '11, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-4498" class="comments-container"></div><div id="comment-tools-4498" class="comment-tools"></div><div class="clear"></div><div id="comment-4498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4513"></span>

<div id="answer-container-4513" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4513-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try using gunzip, if you have it, on the capture file. If it fails, the capture file somehow got damaged.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '11, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4513" class="comments-container"></div><div id="comment-tools-4513" class="comment-tools"></div><div class="clear"></div><div id="comment-4513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

