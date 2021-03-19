+++
type = "question"
title = "labels in tshark?"
description = '''i do apologize for a question i&#x27;m sure everyone on here knows except me. i have been to 10 pages and still am in the dark. i know what BOOLEAN/UNSIGNED INT/FRAME NUMER/ all mean in the display codes for tshark, but what exactly is a LABEL? think about it. as a newbie, i could refrence that to mean a...'''
date = "2014-11-19T22:25:00Z"
lastmod = "2014-11-20T00:33:00Z"
weight = 37994
keywords = [ "syntaxed" ]
aliases = [ "/questions/37994" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [labels in tshark?](/questions/37994/labels-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37994-score" class="post-score" title="current number of votes">0</div><span id="post-37994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i do apologize for a question i'm sure everyone on here knows except me. i have been to 10 pages and still am in the dark. i know what BOOLEAN/UNSIGNED INT/FRAME NUMER/ all mean in the display codes for tshark, but what exactly is a LABEL? think about it. as a newbie, i could refrence that to mean anything! a port number, protocol, string. they tell me NOTHING. so i ask you, where is a label reference sheet? i keep getting this error</p><p>-o tcp.contiuation_to: (it wants a LABEL. so i cant put FALSE/TRUE/etc)</p><p>once again, sorry for the stupid question but i truly am at a loss here</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-syntaxed" rel="tag" title="see questions tagged &#39;syntaxed&#39;">syntaxed</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '14, 22:25</strong></p><img src="https://secure.gravatar.com/avatar/91879a16d398f907c691aa7d2e0edd31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="McKittrick&#39;s gravatar image" /><p><span>McKittrick</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="McKittrick has no accepted answers">0%</span></p></div></div><div id="comments-container-37994" class="comments-container"></div><div id="comment-tools-37994" class="comment-tools"></div><div class="clear"></div><div id="comment-37994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37996"></span>

<div id="answer-container-37996" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37996-score" class="post-score" title="current number of votes">0</div><span id="post-37996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's no such field type as a "label". The field tcp.continuation_to has type "frame number", so its value is an integer value.</p><p>A filter expression that has only a field name tests whether the field is present in the frame; if you want to test whether "tcp.continuation_to" is present, you want a display filter (<code>-Y</code>) of "tcp.continuation_to", with no colon.</p><p><code>-o</code> is for <em>preferences</em>; there is no such preference as "tcp.continuation_to", so there is <em>nothing</em> valid you can place after the colon in <code>-o tcp.continuation_to:</code>.</p><p>If you're trying to disable TCP reassembly, so that no frames will be marked as TCP continuations, you want the preference "tcp.desegment_tcp_streams", and it's a Boolean preference, so you'd specify <code>-o tcp.desegment_tcp_streams:false</code> to disable it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '14, 00:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-37996" class="comments-container"></div><div id="comment-tools-37996" class="comment-tools"></div><div class="clear"></div><div id="comment-37996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

