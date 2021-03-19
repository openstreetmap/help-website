+++
type = "question"
title = "how to give offset of 24 bits in dissector code"
description = '''proto_tree_add_uint(tree, hf_id,tvb,offset,4,(tvb_get_ntoh24( tvb,offset &amp;amp; 0xFFFFF000))); This is the function i gave for dissecting 24 bits in my dissector code.But it not giving the correct result.'''
date = "2015-04-08T06:06:00Z"
lastmod = "2015-04-08T06:29:00Z"
weight = 41280
keywords = [ "proto_tree_add_uint" ]
aliases = [ "/questions/41280" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to give offset of 24 bits in dissector code](/questions/41280/how-to-give-offset-of-24-bits-in-dissector-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41280-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>proto_tree_add_uint(tree, hf_id,tvb,offset,4,(tvb_get_ntoh24( tvb,offset &amp; 0xFFFFF000)));</p><p>This is the function i gave for dissecting 24 bits in my dissector code.But it not giving the correct result.</p></div><div id="question-tags" class="tags-container tags">proto_tree_add_uint</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '15, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/4175e12d54c0b11b1d8a5fb592555a63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lucky15&#39;s gravatar image" /><p>lucky15<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lucky15 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Apr '15, 06:21</p></div></div><div id="comments-container-41280" class="comments-container"></div><div id="comment-tools-41280" class="comment-tools"></div><div class="clear"></div><div id="comment-41280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41283"></span>

<div id="answer-container-41283" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41283-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wrong.</p><p>Use proto_tree_add_item() and setup your hf entry using FT_UINT24 or FT_INT24.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '15, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41283" class="comments-container"><span id="41307"></span><div id="comment-41307" class="comment"><div id="post-41307-score" class="comment-score"></div><div class="comment-text"><p>thanks, it worked.</p></div><div id="comment-41307-info" class="comment-info"><span class="comment-age">(08 Apr '15, 22:21)</span> lucky15</div></div><span id="41331"></span><div id="comment-41331" class="comment"><div id="post-41331-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-41331-info" class="comment-info"><span class="comment-age">(09 Apr '15, 12:44)</span> Jaap ♦</div></div></div><div id="comment-tools-41283" class="comment-tools"></div><div class="clear"></div><div id="comment-41283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

