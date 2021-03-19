+++
type = "question"
title = "Wireshark 2.0.1 crash when performing file operations"
description = '''I have Wireshark 2.0.1 on Windows 7 64-bit on a Dell Latitude E5550. If I use the menu system to do Open, Save As... and several other operations in the File menu Wireshark quietly exits. I think the problem I have relates to Qt. I recreated the problem and used procmon to trace Wireshark exiting. I...'''
date = "2016-02-16T02:08:00Z"
lastmod = "2016-02-16T03:10:00Z"
weight = 50232
keywords = [ "wireshark-2.0.1", "crash" ]
aliases = [ "/questions/50232" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark 2.0.1 crash when performing file operations](/questions/50232/wireshark-201-crash-when-performing-file-operations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50232-score" class="post-score" title="current number of votes">0</div><span id="post-50232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Wireshark 2.0.1 on Windows 7 64-bit on a Dell Latitude E5550. If I use the menu system to do Open, Save As... and several other operations in the File menu Wireshark quietly exits.</p><p>I think the problem I have relates to Qt. I recreated the problem and used procmon to trace Wireshark exiting. I noticed Wireshark fiddling about with some Dell Backup stuff! It turns out that the Dell Backup program uses Qt5, but a different revision to Wireshark. I’m getting some sort of weird interaction between Wireshark and Dell Backup program, I think relating to two revisions of a DLL called Qt5Core.dll. It gets in a right old state; at one point Wireshark is executing code inside a Dell Backup Restore DLL! Thinking about it now I guess the Dell code might be a minifilter, although it looks as though the main thread stack has been corrupted.</p><p>I know – you want to know what the fix is, don’t you? So do I?</p><p>I'll do some more work on this later, but I thought I'd check if this is a known problem and if there is already a fix.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark-2.0.1" rel="tag" title="see questions tagged &#39;wireshark-2.0.1&#39;">wireshark-2.0.1</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '16, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-50232" class="comments-container"></div><div id="comment-tools-50232" class="comment-tools"></div><div class="clear"></div><div id="comment-50232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50235"></span>

<div id="answer-container-50235" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50235-score" class="post-score" title="current number of votes">1</div><span id="post-50235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="PaulOfford has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12036">bug 12036</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '16, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50235" class="comments-container"><span id="50236"></span><div id="comment-50236" class="comment"><div id="post-50236-score" class="comment-score"></div><div class="comment-text"><p>Great catch Graham. Cheers.</p></div><div id="comment-50236-info" class="comment-info"><span class="comment-age">(16 Feb '16, 03:10)</span> <span class="comment-user userinfo">PaulOfford</span></div></div></div><div id="comment-tools-50235" class="comment-tools"></div><div class="clear"></div><div id="comment-50235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

