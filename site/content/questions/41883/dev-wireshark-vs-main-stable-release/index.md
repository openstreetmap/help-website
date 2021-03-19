+++
type = "question"
title = "Dev wireshark vs main stable release"
description = '''Are any of the code changes submitted to the development wireshark (1.99) submitted or merged into the 1.12 or 1.10 versions of wireshark? Is there a way to submit code for the main version versus the development only version? thanks'''
date = "2015-04-27T06:00:00Z"
lastmod = "2015-04-27T06:16:00Z"
weight = 41883
keywords = [ "development", "code" ]
aliases = [ "/questions/41883" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Dev wireshark vs main stable release](/questions/41883/dev-wireshark-vs-main-stable-release)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41883-score" class="post-score" title="current number of votes">0</div><span id="post-41883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Are any of the code changes submitted to the development wireshark (1.99) submitted or merged into the 1.12 or 1.10 versions of wireshark? Is there a way to submit code for the main version versus the development only version?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-code" rel="tag" title="see questions tagged &#39;code&#39;">code</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '15, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/e43b7f1ad5c73c7a40e9a94c0c3180f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jorge&#39;s gravatar image" /><p><span>jorge</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jorge has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Apr '15, 06:04</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-41883" class="comments-container"></div><div id="comment-tools-41883" class="comment-tools"></div><div class="clear"></div><div id="comment-41883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41885"></span>

<div id="answer-container-41885" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41885-score" class="post-score" title="current number of votes">2</div><span id="post-41885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jorge has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <a href="https://wiki.wireshark.org/Development/ReleasePolicy">Release Policy</a> page on the wiki details how we proceed. The normal route is to submit for master, then backport only bug-fixes to the stable and old-stable releases as required.</p><p>There are plenty of bug-fixes backported, the release notes for stable and old-stable releases list the changes made to them.</p><p>It would be possible to submit changes only for stable or old-stable if it were for a serious bug-fix for code that no longer exists in master.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '15, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-41885" class="comments-container"></div><div id="comment-tools-41885" class="comment-tools"></div><div class="clear"></div><div id="comment-41885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

