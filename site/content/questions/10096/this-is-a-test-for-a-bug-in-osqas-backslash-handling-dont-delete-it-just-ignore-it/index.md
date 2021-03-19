+++
type = "question"
title = "This is a test for a bug in OSQA&#x27;s backslash handling - don&#x27;t delete it, just ignore it"
description = '''If, in a question:   I type &quot;UN&quot; {backslash} {asterisk} &quot;X&quot;, it comes out as UN&#92;*X, with a backslash before the asterisk.   I type {backquote} &quot;C&quot; &quot;:&quot; {backslash} &quot;Program Files&quot; {backslash} &quot;Wireshark&quot; {backquote}, it comes out as C:&#92;&#92;Program Files&#92;&#92;Wireshark, with both backslashes doubled.  '''
date = "2012-04-12T15:48:00Z"
lastmod = "2012-04-19T13:35:00Z"
weight = 10096
keywords = [ "osqa" ]
aliases = [ "/questions/10096" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [This is a test for a bug in OSQA's backslash handling - don't delete it, just ignore it](/questions/10096/this-is-a-test-for-a-bug-in-osqas-backslash-handling-dont-delete-it-just-ignore-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10096-score" class="post-score" title="current number of votes">0</div><span id="post-10096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If, in a question:</p><ul><li><p>I type "UN" {backslash} {asterisk} "X", it comes out as UN\*X, with a backslash before the asterisk.</p></li><li><p>I type {backquote} "C" ":" {backslash} "Program Files" {backslash} "Wireshark" {backquote}, it comes out as <code>C:\\Program Files\\Wireshark</code>, with both backslashes doubled.</p></li></ul></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osqa" rel="tag" title="see questions tagged &#39;osqa&#39;">osqa</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '12, 15:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Apr '12, 19:39</strong> </span></p></div></div><div id="comments-container-10096" class="comments-container"><span id="10097"></span><div id="comment-10097" class="comment"><div id="post-10097-score" class="comment-score"></div><div class="comment-text"><p>If, in a comment:</p><ul><li><p>I type "UN" {backslash} {star} "X", it comes out as UN\*X, with a backslash before the asterisk.</p></li><li><p>I type {backquote} "C" ":" {backslash} "Program Files" {backslash} "Wireshark" {backquote}, it comes out as <code>C:\\Program Files\\Wireshark</code>, with both backslashes doubled.</p></li></ul></div><div id="comment-10097-info" class="comment-info"><span class="comment-age">(12 Apr '12, 15:51)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="10304"></span><div id="comment-10304" class="comment"><div id="post-10304-score" class="comment-score"></div><div class="comment-text"><p>Seemed to work (after I changed the trailing backslash to a trailing backquote).</p></div><div id="comment-10304-info" class="comment-info"><span class="comment-age">(19 Apr '12, 13:29)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="10305"></span><div id="comment-10305" class="comment"><div id="post-10305-score" class="comment-score"></div><div class="comment-text"><p>If I type {backquote} "C" ":" {backslash} "Program Files" {backslash} "Wireshark" {backquote} after manually applying the fix for <a href="http://jira.osqa.net/browse/OSQA-739">OSQA bug 739</a> I get</p><p><code>C:\Program Files\Wireshark</code></p></div><div id="comment-10305-info" class="comment-info"><span class="comment-age">(19 Apr '12, 13:35)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div></div><div id="comment-tools-10096" class="comment-tools"></div><div class="clear"></div><div id="comment-10096-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10098"></span>

<div id="answer-container-10098" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10098-score" class="post-score" title="current number of votes">0</div><span id="post-10098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Guy Harris has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If, in an answer:</p><ul><li><p>I type "UN" {backslash} {star} "X", it comes out as UN\*X, with a backslash before the asterisk.</p></li><li><p>I type {backquote} "C" ":" {backslash} "Program Files" {backslash} "Wireshark" {backquote}, it comes out as <code>C:\\Program Files\\Wireshark</code>, with both backslashes doubled.</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '12, 15:51</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Apr '12, 19:41</strong> </span></p></div></div><div id="comments-container-10098" class="comments-container"></div><div id="comment-tools-10098" class="comment-tools"></div><div class="clear"></div><div id="comment-10098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

