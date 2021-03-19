+++
type = "question"
title = "same field name different columns?"
description = '''In IEC61850 sampled values frames we have the same field repeated several times (for example sv.meas_value). the first one is for the current of phase A, 2º for current in phase B... How can i display as a column the 2º, 3º... sv.meas_value?? if i try to apply as column always appears the first valu...'''
date = "2011-04-07T07:52:00Z"
lastmod = "2011-04-08T04:18:00Z"
weight = 3386
keywords = [ "columns" ]
aliases = [ "/questions/3386" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [same field name different columns?](/questions/3386/same-field-name-different-columns)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3386-score" class="post-score" title="current number of votes">0</div><span id="post-3386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In IEC61850 sampled values frames we have the same field repeated several times (for example sv.meas_value). the first one is for the current of phase A, 2º for current in phase B... How can i display as a column the 2º, 3º... sv.meas_value?? if i try to apply as column always appears the first value (current pahase A).</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-columns" rel="tag" title="see questions tagged &#39;columns&#39;">columns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '11, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/5a4573c4fb6c149e3bc05d6b1c2ae7e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="azs&#39;s gravatar image" /><p><span>azs</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="azs has no accepted answers">0%</span></p></div></div><div id="comments-container-3386" class="comments-container"></div><div id="comment-tools-3386" class="comment-tools"></div><div class="clear"></div><div id="comment-3386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3389"></span>

<div id="answer-container-3389" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3389-score" class="post-score" title="current number of votes">1</div><span id="post-3389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You don't mention which version of Wireshark you're using, but with the latest development release (v1.5.0 as of this writing) or later, this is now possible to do when you create a custom column by specifying the <em>field occurrence</em>. By default, this will be set to 0, but as the tooltip indicates, set it to 1, 2, ..., n, to display the 1st, 2nd, ..., nth occurrence of the field. Use -1 to display the last occurrence.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '11, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3389" class="comments-container"><span id="3405"></span><div id="comment-3405" class="comment"><div id="post-3405-score" class="comment-score"></div><div class="comment-text"><p>Thank you, I am using 1.4.4. I will try 1.5</p></div><div id="comment-3405-info" class="comment-info"><span class="comment-age">(08 Apr '11, 04:18)</span> <span class="comment-user userinfo">azs</span></div></div></div><div id="comment-tools-3389" class="comment-tools"></div><div class="clear"></div><div id="comment-3389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

