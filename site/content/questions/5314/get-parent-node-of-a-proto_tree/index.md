+++
type = "question"
title = "Get parent node of a proto_tree"
description = '''Is there a way to grab a child proto_tree&#x27;s parent proto_tree? Thank you for your time, Brandon'''
date = "2011-07-27T07:51:00Z"
lastmod = "2011-07-27T08:03:00Z"
weight = 5314
keywords = [ "node", "traverse", "proto_tree", "parent", "child" ]
aliases = [ "/questions/5314" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Get parent node of a proto\_tree](/questions/5314/get-parent-node-of-a-proto_tree)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5314-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to grab a child proto_tree's parent proto_tree?</p><p>Thank you for your time,</p><p>Brandon</p></div><div id="question-tags" class="tags-container tags">node traverse proto_tree parent child</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '11, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/b65eb296474b8a4c664c8f7bc0ba2234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="officialhopsof&#39;s gravatar image" /><p>officialhopsof<br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="officialhopsof has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jul '11, 07:52</p></div></div><div id="comments-container-5314" class="comments-container"></div><div id="comment-tools-5314" class="comment-tools"></div><div class="clear"></div><div id="comment-5314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5316"></span>

<div id="answer-container-5316" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5316-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>See <code>proto_item_get_parent()</code> in <code>proto.h</code></p><p>Update: Upon doing some research: I think that the code to get the <code>parent_proto_tree</code> is as follows:</p><pre><code>subtree_item = proto_tree_get_parent(subtree);  // returns (proto_item *)subtree
parent_item  = proto_item_get_parent(subtree_item);
parent_tree  = proto_item_get_subtree(parent_item);</code></pre><p>AFAIKT there are no instances of this usage in the current Wireshark source.</p><p>What I do see in a number of dissectors is code like the following:</p><pre><code>proto_item_append_text(proto_item_get_parent(proto_tree_get_parent(tree)), &quot;...&quot;);</code></pre><p>which appends text to the item "1 level up" from the item for the current tree.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '11, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jul '11, 14:02</p></div></div><div id="comments-container-5316" class="comments-container"></div><div id="comment-tools-5316" class="comment-tools"></div><div class="clear"></div><div id="comment-5316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

