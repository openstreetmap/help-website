+++
type = "question"
title = "Adding multiple items to a tree"
description = '''We have a temporary packet that we we&#x27;re trying to do some quick dissecting on. basically we read a field and its value determines what the next 10 or so fields are. Is there a way to overlay text for those next 10 fields, something like this: some string  {  &quot;first&quot;,  &quot;second&quot;, .... } proto_tree_ad...'''
date = "2013-02-11T09:59:00Z"
lastmod = "2013-02-11T14:38:00Z"
weight = 18490
keywords = [ "items", "add", "multiple", "tree" ]
aliases = [ "/questions/18490" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Adding multiple items to a tree](/questions/18490/adding-multiple-items-to-a-tree)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18490-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a temporary packet that we we're trying to do some quick dissecting on.</p><p>basically we read a field and its value determines what the next 10 or so fields are. Is there a way to overlay text for those next 10 fields, something like this:</p><p>some string { "first", "second", ....</p><p>}</p><p>proto_tree_add_item(some_tree, next_ten_fields, tvb, offset, 10, TRUE);</p><p>and have the following appear in the tree:</p><p>first: value second: value .... ten: value</p><p>If so the next question is probably how to adjust the size of each field (1 byte or 4 bytes).</p><p>Thanks, Brian</p></div><div id="question-tags" class="tags-container tags">items add multiple tree</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '13, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/ca4d08b00778143dab07e2cde30f653c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brwiese&#39;s gravatar image" /><p>brwiese<br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brwiese has one accepted answer">50%</span></p></div></div><div id="comments-container-18490" class="comments-container"></div><div id="comment-tools-18490" class="comment-tools"></div><div class="clear"></div><div id="comment-18490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18512"></span>

<div id="answer-container-18512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18512-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>tvb_get_guint8() / tvb_ntohs() / tvb_ntohl() and tvb_letohs() / tvb_letohl()</code> are your friends here. Get that first fields value and branch based on that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '13, 14:38</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-18512" class="comments-container"></div><div id="comment-tools-18512" class="comment-tools"></div><div class="clear"></div><div id="comment-18512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

