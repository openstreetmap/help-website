+++
type = "question"
title = "How to get the parent dissector information?"
description = '''I wish to conditionally call col_set_str or col_append_str depends on the parent dissector information. But I was stuck by getting the parent dissector information. Anyone could help me to do this?  Thanks!'''
date = "2011-07-22T01:50:00Z"
lastmod = "2011-07-26T05:03:00Z"
weight = 5172
keywords = [ "development", "dissector" ]
aliases = [ "/questions/5172" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get the parent dissector information?](/questions/5172/how-to-get-the-parent-dissector-information)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5172-score" class="post-score" title="current number of votes">0</div><span id="post-5172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wish to conditionally call <code>col_set_str</code> or <code>col_append_str</code> depends on the parent dissector information. But I was stuck by getting the parent dissector information. Anyone could help me to do this? Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '11, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/41a2049e9b3abbe6ea9576d112a8ceeb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="piao&#39;s gravatar image" /><p><span>piao</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="piao has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Oct '11, 17:10</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-5172" class="comments-container"></div><div id="comment-tools-5172" class="comment-tools"></div><div class="clear"></div><div id="comment-5172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5173"></span>

<div id="answer-container-5173" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5173-score" class="post-score" title="current number of votes">2</div><span id="post-5173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="piao has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is supposed to be handled the other way around. The parent sets the column non-writable, using col_set_writable(), then calls the subdissector, then restores the previous writable state of the column.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '11, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5173" class="comments-container"><span id="5253"></span><div id="comment-5253" class="comment"><div id="post-5253-score" class="comment-score"></div><div class="comment-text"><p>This way does not solve my problem. So I just let it be since not a big problem for me. Thanks anyway!</p></div><div id="comment-5253-info" class="comment-info"><span class="comment-age">(26 Jul '11, 05:03)</span> <span class="comment-user userinfo">piao</span></div></div></div><div id="comment-tools-5173" class="comment-tools"></div><div class="clear"></div><div id="comment-5173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

