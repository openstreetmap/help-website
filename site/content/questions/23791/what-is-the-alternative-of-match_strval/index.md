+++
type = "question"
title = "What is the alternative of match_strval?"
description = '''Hi experts, I fail to build my plugin for wireshark 1.10.1. it report match_strval function undefined. Is there any alternative solution for this. my plugin call this function like: if(!match_strval(tvb_get_bits8(tvb, bit_offset, 8),xxx_type)); Take Care'''
date = "2013-08-15T01:19:00Z"
lastmod = "2013-08-15T01:47:00Z"
weight = 23791
keywords = [ "match_strval" ]
aliases = [ "/questions/23791" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is the alternative of match\_strval?](/questions/23791/what-is-the-alternative-of-match_strval)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23791-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi experts, I fail to build my plugin for wireshark 1.10.1. it report match_strval function undefined. Is there any alternative solution for this.</p><p>my plugin call this function like: if(!match_strval(tvb_get_bits8(tvb, bit_offset, 8),xxx_type));</p><p>Take Care</p></div><div id="question-tags" class="tags-container tags">match_strval</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Aug '13, 01:19</strong></p><img src="https://secure.gravatar.com/avatar/816ce305386a60ddd1b13bf850712092?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gaobrian&#39;s gravatar image" /><p>gaobrian<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gaobrian has no accepted answers">0%</span></p></div></div><div id="comments-container-23791" class="comments-container"></div><div id="comment-tools-23791" class="comment-tools"></div><div class="clear"></div><div id="comment-23791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23792"></span>

<div id="answer-container-23792" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23792-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think it's been renamed to try_val_to_str() see epan/value_string.[ch]</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '13, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-23792" class="comments-container"><span id="23793"></span><div id="comment-23793" class="comment"><div id="post-23793-score" class="comment-score"></div><div class="comment-text"><p>It works well. Thanks</p></div><div id="comment-23793-info" class="comment-info"><span class="comment-age">(15 Aug '13, 02:46)</span> gaobrian</div></div></div><div id="comment-tools-23792" class="comment-tools"></div><div class="clear"></div><div id="comment-23792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

