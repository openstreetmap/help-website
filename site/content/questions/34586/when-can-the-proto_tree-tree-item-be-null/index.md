+++
type = "question"
title = "When can the proto_tree *tree item be NULL?"
description = '''According to the WSDG, proto_tree *tree params can be NULL when &quot;asked for a summary of a packet instead of the details&quot;. How should I decide whether something is a detail? Where is this difference exactly visible? In the example, the column data seems to be the summary while the filterable protocol...'''
date = "2014-07-10T14:49:00Z"
lastmod = "2014-07-11T02:03:00Z"
weight = 34586
keywords = [ "null", "proto_tree" ]
aliases = [ "/questions/34586" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [When can the proto\_tree \*tree item be NULL?](/questions/34586/when-can-the-proto_tree-tree-item-be-null)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34586-score" class="post-score" title="current number of votes">0</div><span id="post-34586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>According to the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html">WSDG</a>, proto_tree *tree params can be NULL when "asked for a summary of a packet instead of the details". How should I decide whether something is a detail? Where is this difference exactly visible?</p><p>In the example, the column data seems to be the summary while the filterable protocol tree are the details. Wouldn't skipping <code>proto_tree_add_item()</code> make all fields unfilterable?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-null" rel="tag" title="see questions tagged &#39;null&#39;">null</span> <span class="post-tag tag-link-proto_tree" rel="tag" title="see questions tagged &#39;proto_tree&#39;">proto_tree</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '14, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Jul '14, 14:50</strong> </span></p></div></div><div id="comments-container-34586" class="comments-container"></div><div id="comment-tools-34586" class="comment-tools"></div><div class="clear"></div><div id="comment-34586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34592"></span>

<div id="answer-container-34592" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34592-score" class="post-score" title="current number of votes">2</div><span id="post-34592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Lekensteyn has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Basically if(tree) can be used to make the first pass faster (when all packets are read in sequence) by omitting puting details in the tree which will not be vissible in the GUI/Tshark output any way. Writing to columns and calling of subdissectors must be done outside of if(tree) to ensure it allways hapens as would reassembly.</p><p>If dissection is run with filter tree is not NULL, as you noted filtering wouldn't work otherwise.</p><p>A simple dissector would just put the proto name in the tree and write to the proto and info columns outside of if(tree).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '14, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-34592" class="comments-container"><span id="34593"></span><div id="comment-34593" class="comment"><div id="post-34593-score" class="comment-score"></div><div class="comment-text"><p>Note that expert info and call to subdissectors should not be inside a if(tree) statement.</p></div><div id="comment-34593-info" class="comment-info"><span class="comment-age">(11 Jul '14, 02:03)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-34592" class="comment-tools"></div><div class="clear"></div><div id="comment-34592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

