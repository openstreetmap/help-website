+++
type = "question"
title = "PNODE_FINFO returning NULL?"
description = '''i am working on my current project using wireshark lib, after calling dissector run on the data buffer, i get the &#x27;edt&#x27; tree but when i call PNODE_FINFO on the node where (&#x27;node = edt.tree&#x27;) PNODE_FINFO returns NULL what is the problem? any help. thanks!! '''
date = "2012-01-23T23:09:00Z"
lastmod = "2012-01-25T02:12:00Z"
weight = 8576
keywords = [ "proto_node", "wireshark" ]
aliases = [ "/questions/8576" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [PNODE\_FINFO returning NULL?](/questions/8576/pnode_finfo-returning-null)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8576-score" class="post-score" title="current number of votes">0</div><span id="post-8576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i am working on my current project using wireshark lib,</p><p>after calling dissector run on the data buffer, i get the 'edt' tree but when i call PNODE_FINFO on the node where ('node = edt.tree')</p><p>PNODE_FINFO returns NULL what is the problem? any help.</p><p>thanks!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-proto_node" rel="tag" title="see questions tagged &#39;proto_node&#39;">proto_node</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '12, 23:09</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p><span>Sanny_D</span><br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-8576" class="comments-container"></div><div id="comment-tools-8576" class="comment-tools"></div><div class="clear"></div><div id="comment-8576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8598"></span>

<div id="answer-container-8598" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8598-score" class="post-score" title="current number of votes">1</div><span id="post-8598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sanny_D has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You are looking at the root of the tree, that has no field info (ref <code>epan/epan.c:epan_dissect_init()</code> and <code>/epan/proto.c:proto_tree_create_root()</code>). Look further down into the tree to find the items, those have field info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '12, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8598" class="comments-container"></div><div id="comment-tools-8598" class="comment-tools"></div><div class="clear"></div><div id="comment-8598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

