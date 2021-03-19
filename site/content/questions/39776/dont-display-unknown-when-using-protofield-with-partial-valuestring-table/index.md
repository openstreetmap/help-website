+++
type = "question"
title = "Don&#x27;t display Unknown when using ProtoField with partial valuestring table"
description = '''There is a field in my protocol that I would like to display as base.DEC_HEX, except when it is a reserved value, in which case I would like to display a string (with a dec or hex value in parentheses). I do NOT want the values to show as Unknown (value), which is what happens when I create a string...'''
date = "2015-02-10T10:00:00Z"
lastmod = "2015-02-11T06:04:00Z"
weight = 39776
keywords = [ "unknown", "protofield", "value_string", "valuestring" ]
aliases = [ "/questions/39776" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Don't display Unknown when using ProtoField with partial valuestring table](/questions/39776/dont-display-unknown-when-using-protofield-with-partial-valuestring-table)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39776-score" class="post-score" title="current number of votes">0</div><span id="post-39776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>There is a field in my protocol that I would like to display as base.DEC_HEX, except when it is a reserved value, in which case I would like to display a string (with a dec or hex value in parentheses).</p><p>I do NOT want the values to show as <code>Unknown (value)</code>, which is what happens when I create a string table with just the reserved value and reference it in the ProtoField.new call.</p><p>What is the best way to accomplish this? I know I can use an <code>if</code> statement and assign a label when calling <code>tree:add()</code> but this seems less than ideal, and would be a pain if I had several reserved values instead of just one.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unknown" rel="tag" title="see questions tagged &#39;unknown&#39;">unknown</span> <span class="post-tag tag-link-protofield" rel="tag" title="see questions tagged &#39;protofield&#39;">protofield</span> <span class="post-tag tag-link-value_string" rel="tag" title="see questions tagged &#39;value_string&#39;">value_string</span> <span class="post-tag tag-link-valuestring" rel="tag" title="see questions tagged &#39;valuestring&#39;">valuestring</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '15, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/c0e1d8fa360f3ed1d0eb32459c4eda98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chojiao&#39;s gravatar image" /><p><span>chojiao</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chojiao has no accepted answers">0%</span></p></div></div><div id="comments-container-39776" class="comments-container"></div><div id="comment-tools-39776" class="comment-tools"></div><div class="clear"></div><div id="comment-39776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39794"></span>

<div id="answer-container-39794" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39794-score" class="post-score" title="current number of votes">0</div><span id="post-39794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="chojiao has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Extract the value and decide what code path to follow to represent it in the tree. That's how you can divide the complexity into existing functions. Yes there's some duplication of data points, unfortunately.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '15, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-39794" class="comments-container"></div><div id="comment-tools-39794" class="comment-tools"></div><div class="clear"></div><div id="comment-39794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

