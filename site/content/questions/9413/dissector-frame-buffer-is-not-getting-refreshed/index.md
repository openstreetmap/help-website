+++
type = "question"
title = "dissector frame buffer is not getting refreshed"
description = '''Hello  I have added a .CSV parser and a dissector. It is observed that if my .CSV file is opened as the first file in wireshark, tvb buffer contents is proper. But if an other file is opened first and then my .CSV file is opened then packet dump is of the previous data. This is not the behaviour wit...'''
date = "2012-03-06T22:02:00Z"
lastmod = "2012-03-11T22:27:00Z"
weight = 9413
keywords = [ "development", "dissector", "wireshark" ]
aliases = [ "/questions/9413" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [dissector frame buffer is not getting refreshed](/questions/9413/dissector-frame-buffer-is-not-getting-refreshed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9413-score" class="post-score" title="current number of votes">0</div><span id="post-9413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I have added a .CSV parser and a dissector. It is observed that if my .CSV file is opened as the first file in wireshark, tvb buffer contents is proper.</p><p>But if an other file is opened first and then my .CSV file is opened then packet dump is of the previous data. This is not the behaviour with other sample files.</p><p>Can anyone help me to resolve my issue?</p><p>thanks in advance krithiga</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '12, 22:02</strong></p><img src="https://secure.gravatar.com/avatar/58a0b723193dca931ba99c422c8a0e74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krithiga&#39;s gravatar image" /><p><span>krithiga</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krithiga has no accepted answers">0%</span></p></div></div><div id="comments-container-9413" class="comments-container"></div><div id="comment-tools-9413" class="comment-tools"></div><div class="clear"></div><div id="comment-9413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9482"></span>

<div id="answer-container-9482" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9482-score" class="post-score" title="current number of votes">1</div><span id="post-9482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>issue resolved by doing changes in XXX_seek() w.r.t to offset handling</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '12, 22:27</strong></p><img src="https://secure.gravatar.com/avatar/58a0b723193dca931ba99c422c8a0e74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krithiga&#39;s gravatar image" /><p><span>krithiga</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krithiga has no accepted answers">0%</span></p></div></div><div id="comments-container-9482" class="comments-container"></div><div id="comment-tools-9482" class="comment-tools"></div><div class="clear"></div><div id="comment-9482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

