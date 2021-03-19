+++
type = "question"
title = "how can i make a nested protocol tree in dissector"
description = '''I want to make a multiple and nested subtrees in my protocol dissector tree. I am not able to add another tree in my protocol subtree. I tried to add a new item in the subtree of the protocol by proto_tree_add_item()and proto_item_add_subtree(). But it doesn&#x27;t worked.'''
date = "2014-05-14T00:22:00Z"
lastmod = "2014-05-14T05:16:00Z"
weight = 32779
keywords = [ "proto_tree_add_item", "dissector", "tree", "plugin" ]
aliases = [ "/questions/32779" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how can i make a nested protocol tree in dissector](/questions/32779/how-can-i-make-a-nested-protocol-tree-in-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32779-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to make a multiple and nested subtrees in my protocol dissector tree. I am not able to add another tree in my protocol subtree.</p><p>I tried to add a new item in the subtree of the protocol by proto_tree_add_item()and proto_item_add_subtree(). But it doesn't worked.</p></div><div id="question-tags" class="tags-container tags">proto_tree_add_item dissector tree plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '14, 00:22</strong></p><img src="https://secure.gravatar.com/avatar/3bd1cf7096b417e3b2be586527ec8002?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Balpreet%20Singh&#39;s gravatar image" /><p>Balpreet Singh<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Balpreet Singh has no accepted answers">0%</span></p></div></div><div id="comments-container-32779" class="comments-container"></div><div id="comment-tools-32779" class="comment-tools"></div><div class="clear"></div><div id="comment-32779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32793"></span>

<div id="answer-container-32793" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32793-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you following the instructions in README.dissector, section 1.5.2 "Adding Items and Values to the Protocol Tree"?</p><p>Have you got an "ett" variable for your subtree and registered it with <code>proto_register_subtree_array()</code>?</p><p>Can you show the relevant portions of your code, e.g. ett_xxx declaration and registration, and the code around <code>proto_item_add_subtree()</code> ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '14, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-32793" class="comments-container"></div><div id="comment-tools-32793" class="comment-tools"></div><div class="clear"></div><div id="comment-32793-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

