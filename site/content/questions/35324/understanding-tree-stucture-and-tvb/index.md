+++
type = "question"
title = "Understanding tree stucture and tvb"
description = '''I&#x27;m very newbie to writing Wireshark code for plugin dissectors, I&#x27;ve read the documentation, but I still have some problem to understand the general environnement. 1) What are exactly trees, what do they do, and why should be useful to add tree for dissecting? Do I have to instance at least one tre...'''
date = "2014-08-08T04:04:00Z"
lastmod = "2014-08-08T05:29:00Z"
weight = 35324
keywords = [ "tree" ]
aliases = [ "/questions/35324" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Understanding tree stucture and tvb](/questions/35324/understanding-tree-stucture-and-tvb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35324-score" class="post-score" title="current number of votes">0</div><span id="post-35324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm very newbie to writing Wireshark code for plugin dissectors, I've read the documentation, but I still have some problem to understand the general environnement.</p><p>1) What are exactly trees, what do they do, and why should be useful to add tree for dissecting? Do I have to instance at least one tree in my dissector, or could I completely avoid using them?</p><p>2)Are subtrees just trees linked to a "father" tree ore something more? When should I use proto_item_add_subtree instead of proto_tree_add_item?</p><p>3)Aren't all the information of the packet in the tvbuff? Why I can't just read there to perform the dissection?</p><p>4)What is the difference between proto_tree and proto_item</p><p>5)How does the statement if(tree) work? What does it mean that I go into this function if I am being asked for details? Referring to that, what kind of code should I put inside this if() statement, and what else outside?</p><p>Sorry for these basic questions</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tree" rel="tag" title="see questions tagged &#39;tree&#39;">tree</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '14, 04:04</strong></p><img src="https://secure.gravatar.com/avatar/e1fba327ed394306c1606291dedfd698?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="francesco_bigotto&#39;s gravatar image" /><p><span>francesco_bi...</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="francesco_bigotto has no accepted answers">0%</span></p></div></div><div id="comments-container-35324" class="comments-container"></div><div id="comment-tools-35324" class="comment-tools"></div><div class="clear"></div><div id="comment-35324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35325"></span>

<div id="answer-container-35325" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35325-score" class="post-score" title="current number of votes">1</div><span id="post-35325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="francesco_bigotto has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>The tree is displayed in the packet details pane. No tree == no details, so yes you probably should add items to the tree.</li><li>Sub-trees are somewhat stylistic, but generally are used for protocol sub-elements that have multiple elements of their own. Without sub-trees, every element in your protocol would be in a flat list under the protocol tree.</li><li>The tvb is the data handed to your dissector from the preceding layer. You use the data in the tvb to construct your tree. This is the fundamental basis of dissection.</li><li>Well a tree is a tree and an item is an item in the tree. I think an item is always associated with data (possibly synthetic) so can be used in a filter.</li><li>In some circumstances dissectors can be called with a null tree pointer so they don't need to carry out any processing that was only for tree display, however the dissector should still carry out all other dissection processing.</li></ol><p>Are you sure you've read the Developers Guide and all the items in the docs directory of the source code? Most of these questions are answered there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '14, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35325" class="comments-container"><span id="35326"></span><div id="comment-35326" class="comment"><div id="post-35326-score" class="comment-score"></div><div class="comment-text"><p>I've read the Developers Guide, but not yet the items in the docs directory, sorry. Anyway thanks for the good explanation</p></div><div id="comment-35326-info" class="comment-info"><span class="comment-age">(08 Aug '14, 05:29)</span> <span class="comment-user userinfo">francesco_bi...</span></div></div></div><div id="comment-tools-35325" class="comment-tools"></div><div class="clear"></div><div id="comment-35325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

