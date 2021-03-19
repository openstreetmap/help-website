+++
type = "question"
title = "Custom Dissector How to Add Multiple TREEs in same protocol"
description = '''Hi, Iam new to this. Iam develoing custom dissector. I have one tree generated and inside that tree i have many sub trees. Now i have to generate a new tree (not a sub tree ) (which payload is from the first tree). How can i do this? ALso please advise how to get tvb buff back to 39 bytes (sub tree ...'''
date = "2014-05-28T20:06:00Z"
lastmod = "2014-05-29T06:48:00Z"
weight = 33146
keywords = [ "tree", "add", "dissector", "multiple", "custom" ]
aliases = [ "/questions/33146" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Custom Dissector How to Add Multiple TREEs in same protocol](/questions/33146/custom-dissector-how-to-add-multiple-trees-in-same-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33146-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Iam new to this. Iam develoing custom dissector. I have one tree generated and inside that tree i have many sub trees. Now i have to generate a new tree (not a sub tree ) (which payload is from the first tree).</p><p>How can i do this? ALso please advise how to get tvb buff back to 39 bytes (sub tree byte of first tree)</p><p>ANy exampe available??</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">tree add dissector multiple custom</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '14, 20:06</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p>umar<br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 May '14, 20:14</p></div></div><div id="comments-container-33146" class="comments-container"></div><div id="comment-tools-33146" class="comment-tools"></div><div class="clear"></div><div id="comment-33146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33166"></span>

<div id="answer-container-33166" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33166-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>+-tree1
  +-subtree1a
  +-subtree1b
+-tree2
  +-subtree2a</code></pre><p>Now you want in tree2 to be able to represent data as already shown in tree1/subtree1x</p><p>Assuming you've used a TVB while working on tree1, and making subsets when making subtree1a and subtree1b, the original TVB stays intact. So when you want to create tree2 you just can use the original TVB again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '14, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-33166" class="comments-container"><span id="33173"></span><div id="comment-33173" class="comment"><div id="post-33173-score" class="comment-score"></div><div class="comment-text"><p><code> tvb_get_guint8( tvb_b, offsetb ); offsetb-=39;</code></p><p><code></code></p><p><code>moto_item = proto_tree_add_item(tree_b, proto_moto, tvb_b, 0, -1, FALSE); moto_tree = proto_item_add_subtree(moto_item, ett_moto); moto_header_tree = proto_item_add_subtree(moto_item, ett_moto); offsetb++;</code></p><p>Hi whats wrong in this code? I have created parent tree 3 functions .. dissect, handoff, register</p><p>The same i did for this tree also. Tree 1's one of the subtree data is the input for this 2nd tree. How do i get that. Is there any sample code for me to understand . Could any one please send me.</p></div><div id="comment-33173-info" class="comment-info"><span class="comment-age">(29 May '14, 08:40)</span> umar</div></div><span id="33174"></span><div id="comment-33174" class="comment"><div id="post-33174-score" class="comment-score"></div><div class="comment-text"><p>You'll need to pass the top-level tree item from your first dissector into your second dissector so it can add its subtrees at the same level as the first one.</p></div><div id="comment-33174-info" class="comment-info"><span class="comment-age">(29 May '14, 09:19)</span> grahamb ♦</div></div><span id="33179"></span><div id="comment-33179" class="comment"><div id="post-33179-score" class="comment-score"></div><div class="comment-text"><p>Hi mr.graham and jaap,thanks for your valuable time . I could not get understand as iam new to this. Is there any similar protocol available i can sèe the code for reference. Thanks again.</p></div><div id="comment-33179-info" class="comment-info"><span class="comment-age">(29 May '14, 10:13)</span> umar</div></div><span id="33194"></span><div id="comment-33194" class="comment"><div id="post-33194-score" class="comment-score"></div><div class="comment-text"><p>The question seems to have moved on to <a href="http://ask.wireshark.org/questions/33188/tvb-reference-from-one-tree-to-another-crash-while-starting-wireshark">http://ask.wireshark.org/questions/33188/tvb-reference-from-one-tree-to-another-crash-while-starting-wireshark</a></p></div><div id="comment-33194-info" class="comment-info"><span class="comment-age">(30 May '14, 02:54)</span> grahamb ♦</div></div></div><div id="comment-tools-33166" class="comment-tools"></div><div class="clear"></div><div id="comment-33166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

