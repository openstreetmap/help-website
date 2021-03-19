+++
type = "question"
title = "wireshark not signed"
description = '''why is wireshark not signed???'''
date = "2010-12-26T11:56:00Z"
lastmod = "2011-01-07T11:45:00Z"
weight = 1486
keywords = [ "not", "signed" ]
aliases = [ "/questions/1486" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark not signed](/questions/1486/wireshark-not-signed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1486-score" class="post-score" title="current number of votes">0</div><span id="post-1486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>why is wireshark not signed???</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-not" rel="tag" title="see questions tagged &#39;not&#39;">not</span> <span class="post-tag tag-link-signed" rel="tag" title="see questions tagged &#39;signed&#39;">signed</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Dec '10, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/e95d9270ae3cf8a460d1428ada052801?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="awgi&#39;s gravatar image" /><p><span>awgi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="awgi has no accepted answers">0%</span></p></div></div><div id="comments-container-1486" class="comments-container"></div><div id="comment-tools-1486" class="comment-tools"></div><div class="clear"></div><div id="comment-1486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1521"></span>

<div id="answer-container-1521" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1521-score" class="post-score" title="current number of votes">0</div><span id="post-1521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There was a discussion about this in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1086">bug 1086</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Dec '10, 19:21</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-1521" class="comments-container"></div><div id="comment-tools-1521" class="comment-tools"></div><div class="clear"></div><div id="comment-1521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1674"></span>

<div id="answer-container-1674" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1674-score" class="post-score" title="current number of votes">0</div><span id="post-1674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hashes for each release file can be found in a "SIGNATURES" file for each release. For example, the signature file for 1.4.2 is at <a href="http://www.wireshark.org/download/src/all-versions/SIGNATURES-1.4.2.txt">http://www.wireshark.org/download/src/all-versions/SIGNATURES-1.4.2.txt</a>. It is signed with my GPG key. The hashes can also be found in each <a href="http://www.wireshark.org/lists/wireshark-announce/201011/msg00000.html">release announcement</a>, which is also signed.</p><p>We don't sign the Windows packages with <a href="http://msdn.microsoft.com/en-us/library/ms537361.aspx">Authenticode signatures</a> but we should. I'll see if I can add that to the release process.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '11, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-1674" class="comments-container"></div><div id="comment-tools-1674" class="comment-tools"></div><div class="clear"></div><div id="comment-1674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

