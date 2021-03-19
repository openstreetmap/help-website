+++
type = "question"
title = "How to use proto_register_subtree_array / proto_item_add_subtree with repeating structures ?"
description = '''I am writing a dissector for a custom protocol with pdus containing repetitive structures (the number of each structure is determined by a previous field whose value can be &amp;gt; 2000), possibly composed of other structures (think as &quot;area descriptions&quot; containing polylines / polygons, circles, ...) ...'''
date = "2016-04-14T08:36:00Z"
lastmod = "2016-04-29T08:59:00Z"
weight = 51669
keywords = [ "proto_tree_add_item", "subtree" ]
aliases = [ "/questions/51669" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to use proto\_register\_subtree\_array / proto\_item\_add\_subtree with repeating structures ?](/questions/51669/how-to-use-proto_register_subtree_array-proto_item_add_subtree-with-repeating-structures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51669-score" class="post-score" title="current number of votes">0</div><span id="post-51669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a dissector for a custom protocol with pdus containing repetitive structures (the number of each structure is determined by a previous field whose value can be &gt; 2000), possibly composed of other structures (think as "area descriptions" containing polylines / polygons, circles, ...)</p><p>I need to display each of these structures as a subtree, containing other subtree if needed, and I understand that I must register a variable for each of them (&gt; 2000 variables) with <code>proto_register_subtree_array</code>. Am I right ?</p><p>I do not need to retain the state (expanded or collapsed) of the tree for these structures, I just need the same default behavior for them when I first look at a packet (all expanded or all collapsed). Is there a way to do it without creating a lot of variables (register "less" element in <code>proto_register_subtree_array</code> ? Use <code>proto_item_add_subtree</code> with a value that has not been registered before ?, ...) ?</p><p>How do you proceed when you need to dissect repeating structures ? Are there any best practices ?</p><p>Thank you all for your advice(s) !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-proto_tree_add_item" rel="tag" title="see questions tagged &#39;proto_tree_add_item&#39;">proto_tree_add_item</span> <span class="post-tag tag-link-subtree" rel="tag" title="see questions tagged &#39;subtree&#39;">subtree</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '16, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/dfd728dcc858e4bb45f3ea8804fe9ba1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hpa&#39;s gravatar image" /><p><span>hpa</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hpa has no accepted answers">0%</span></p></div></div><div id="comments-container-51669" class="comments-container"></div><div id="comment-tools-51669" class="comment-tools"></div><div class="clear"></div><div id="comment-51669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51671"></span>

<div id="answer-container-51671" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51671-score" class="post-score" title="current number of votes">0</div><span id="post-51671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hpa has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can re-use the same ett_xxx variable for each subtree, this just records the expanded\collapsed state of the subtree, so all that use the same variable will expand\collapse together.</p><p>This is quite common in telemetry protocols, e.g. where a field device contains lots of data objects representing physical values such as analog and digital values. One such dissector is packet-dnp.c, but that is a very complex protocol so might not be the best example. The code to look at there is in <code>dnp3_al_process_object()</code> around the <code>for()</code> loop which loops over each data object (or point) and adds a subtree for it (held in <code>point_tree</code>) along with the appropriate data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '16, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51671" class="comments-container"><span id="52080"></span><div id="comment-52080" class="comment"><div id="post-52080-score" class="comment-score"></div><div class="comment-text"><p>I did that (reusing the same ett for each subtree type), and it's ok.</p><p>Thank you !</p></div><div id="comment-52080-info" class="comment-info"><span class="comment-age">(29 Apr '16, 08:59)</span> <span class="comment-user userinfo">hpa</span></div></div></div><div id="comment-tools-51671" class="comment-tools"></div><div class="clear"></div><div id="comment-51671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

