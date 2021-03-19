+++
type = "question"
title = "How to add source ,destination and protocol info into the tree"
description = '''I would like to know the functions which help us in adding the information of source destination and protocol into pane2 ...as clicking on them in pane 3 is making the wireshark to quit  I encountered the following error (lt-wireshark:9103): Gtk-CRITICAL **: gtk_tree_store_get_path: assertion `iter-...'''
date = "2011-09-23T01:16:00Z"
lastmod = "2011-09-23T02:54:00Z"
weight = 6503
keywords = [ "dissector" ]
aliases = [ "/questions/6503" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to add source ,destination and protocol info into the tree](/questions/6503/how-to-add-source-destination-and-protocol-info-into-the-tree)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6503-score" class="post-score" title="current number of votes">0</div><span id="post-6503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to know the functions which help us in adding the information of source destination and protocol into pane2 ...as clicking on them in pane 3 is making the wireshark to quit I encountered the following error (lt-wireshark:9103): Gtk-CRITICAL **: gtk_tree_store_get_path: assertion `iter-&gt;user_data != NULL' failed</p><p>(lt-wireshark:9103): Gtk-CRITICAL **: IA__gtk_tree_view_expand_row: assertion `path != NULL' failed</p><p>(lt-wireshark:9103): Gtk-CRITICAL **: gtk_tree_store_get_value: assertion `VALID_ITER (iter, tree_store)' failed</p><p>(lt-wireshark:9103): GLib-GObject-WARNING **: gtype.c:4181: type id `0' is invalid</p><p>(lt-wireshark:9103): GLib-GObject-WARNING **: can't peek value table for type `&lt;invalid&gt;' which is not currently referenced Segmentation fault (core dumped)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '11, 01:16</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p><span>flashkicker</span><br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div></div><div id="comments-container-6503" class="comments-container"></div><div id="comment-tools-6503" class="comment-tools"></div><div class="clear"></div><div id="comment-6503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6509"></span>

<div id="answer-container-6509" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6509-score" class="post-score" title="current number of votes">0</div><span id="post-6509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flashkicker has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>removing PROTO_ITEM_SET_HIDDEN in packet-eth.c which was used before resolved the issue</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '11, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p><span>flashkicker</span><br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div></div><div id="comments-container-6509" class="comments-container"></div><div id="comment-tools-6509" class="comment-tools"></div><div class="clear"></div><div id="comment-6509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6506"></span>

<div id="answer-container-6506" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6506-score" class="post-score" title="current number of votes">0</div><span id="post-6506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First make sure you have a clean build of a released source before adding your own changes.</p><p>Adding items to the protocol tree is do by <code>proto_tree_add_item()</code> calls. All this can be found in <code>doc/README.developer</code> in the source tree.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '11, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6506" class="comments-container"><span id="6508"></span><div id="comment-6508" class="comment"><div id="post-6508-score" class="comment-score"></div><div class="comment-text"><p>Ohk thanks...actually i have hidden the Ethernet tree so that i have only the tree presented by my dissector</p></div><div id="comment-6508-info" class="comment-info"><span class="comment-age">(23 Sep '11, 02:51)</span> <span class="comment-user userinfo">flashkicker</span></div></div></div><div id="comment-tools-6506" class="comment-tools"></div><div class="clear"></div><div id="comment-6506-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

