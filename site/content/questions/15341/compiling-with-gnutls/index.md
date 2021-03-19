+++
type = "question"
title = "Compiling with gnutls"
description = '''Can Wireshark be compiled with libgnutls version greater than 3? I&#x27;m trying to compile on OpenSuSE 12.1, which has libgnutls 3.0.3 and am getting errors when I run configure. If it can be compiled with libgnutls version greater than 3, how can I force configure to accept the version?'''
date = "2012-10-29T11:46:00Z"
lastmod = "2012-10-30T08:55:00Z"
weight = 15341
keywords = [ "libgnutls" ]
aliases = [ "/questions/15341" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Compiling with gnutls](/questions/15341/compiling-with-gnutls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15341-score" class="post-score" title="current number of votes">0</div><span id="post-15341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can Wireshark be compiled with libgnutls version greater than 3? I'm trying to compile on OpenSuSE 12.1, which has libgnutls 3.0.3 and am getting errors when I run configure. If it can be compiled with libgnutls version greater than 3, how can I force configure to accept the version?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-libgnutls" rel="tag" title="see questions tagged &#39;libgnutls&#39;">libgnutls</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '12, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/0069f852a157ef656a0aaf630027a0b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swadlow&#39;s gravatar image" /><p><span>swadlow</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swadlow has no accepted answers">0%</span></p></div></div><div id="comments-container-15341" class="comments-container"></div><div id="comment-tools-15341" class="comment-tools"></div><div class="clear"></div><div id="comment-15341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15367"></span>

<div id="answer-container-15367" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15367-score" class="post-score" title="current number of votes">1</div><span id="post-15367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="swadlow has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It seems like gnutls is GPLv3 which poses a problem for Wireshark see <a href="http://www.wireshark.org/lists/wireshark-dev/201205/msg00186.html">http://www.wireshark.org/lists/wireshark-dev/201205/msg00186.html</a> and the links in that tread.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '12, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-15367" class="comments-container"><span id="15371"></span><div id="comment-15371" class="comment"><div id="post-15371-score" class="comment-score"></div><div class="comment-text"><p>Bleh. I sort of expected something like this, but was hoping it wasn't so. Thanks for the information.</p></div><div id="comment-15371-info" class="comment-info"><span class="comment-age">(30 Oct '12, 08:55)</span> <span class="comment-user userinfo">swadlow</span></div></div></div><div id="comment-tools-15367" class="comment-tools"></div><div class="clear"></div><div id="comment-15367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

