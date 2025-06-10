+++
type = "question"
title = "Matching level in nominatim"
description = '''When I search for a specific housenumber that isn`t matched yet, nominatim will only return a location somewhere on this street. Is there something like a &#x27;matching level&#x27; to help me indicate those results?'''
date = "2015-11-02T10:12:00Z"
lastmod = "2015-11-02T15:36:00Z"
weight = 46293
keywords = [ "matching" ]
aliases = [ "/questions/46293" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Matching level in nominatim](/questions/46293/matching-level-in-nominatim)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46293-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I search for a specific housenumber that isn`t matched yet, nominatim will only return a location somewhere on this street. Is there something like a 'matching level' to help me indicate those results?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-matching" rel="tag" title="see questions tagged &#39;matching&#39;">matching</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Nov '15, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/c2aedb5d7966ad8d9da5c83a807ef655?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmyers&#39;s gravatar image" />
<p><span>mmyers</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmyers has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46293" class="comments-container">
&#10;</div>
<div id="comment-tools-46293" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46293-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46294"></span>

<div id="answer-container-46294" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46294-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mmyers has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, if you request a <code>format=jsonv2</code> response there will be a <code>place_rank</code> element and if that has a value of 30, you've struck a house number.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '15, 10:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46294" class="comments-container">
<span id="46297"></span>
<div id="comment-46297" class="comment">
<div id="post-46297-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, but this rank is not related to my search query. I am looking for a criteria to determine the results quality according to the address I entered.</p>
<p>I am processing many requests automatically and want only to use exact matches.</p>
</div>
<div id="comment-46297-info" class="comment-info">
<span class="comment-age">(02 Nov '15, 11:40)</span> <span class="comment-user userinfo">mmyers</span>
</div>
</div>
<span id="46300"></span>
<div id="comment-46300" class="comment">
<div id="post-46300-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If your query contains a house number and you get a <code>place_rank</code> of 30 then it is an exact match, and if you get a different place rank then it is not. -- If your query is less precise, i.e. you are only <em>asking</em> for a road in the first place, then you have to analyse your queries before (i.e. you have to know what place_rank your query is asking for) and then compare the rank you got with what you expected.</p>
</div>
<div id="comment-46300-info" class="comment-info">
<span class="comment-age">(02 Nov '15, 13:32)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="46301"></span>
<div id="comment-46301" class="comment">
<div id="post-46301-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, that is the problem.</p>
<p>I am getting queries as non-structured requests (at least street + housenumber) and have problems to decide if a street or a house is meant. For example: There are streetnames including numbers, like 'portstreet 4', where the number is not a housenumber.</p>
<p>I was thinking nominatim could identify that the result is not matching the whole query and presenting this in some kind of quality.</p>
<p>Guess I have to solve this by forcing structured requests.</p>
</div>
<div id="comment-46301-info" class="comment-info">
<span class="comment-age">(02 Nov '15, 15:36)</span> <span class="comment-user userinfo">mmyers</span>
</div>
</div>
</div>
<div id="comment-tools-46294" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46294-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

