+++
type = "question"
title = "Was does the leading space mean in word.word_token?"
description = '''I&#x27;m wondering why words appear to entered twice in the word table, once plain and once with a leading space. This table is part of Nominatim (or Gazetteer as it was called when i first installed it). Here are links for the create table statement.  https://trac.openstreetmap.org/browser/applications/...'''
date = "2012-05-05T15:26:00Z"
lastmod = "2012-05-06T14:39:00Z"
weight = 12561
keywords = [ "nominatim", "database" ]
aliases = [ "/questions/12561" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Was does the leading space mean in word.word_token?](/questions/12561/was-does-the-leading-space-mean-in-wordword_token)

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
<span id="post-12561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12561-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm wondering why words appear to entered twice in the word table, once plain and once with a leading space.</p>
<p>This table is part of Nominatim (or Gazetteer as it was called when i first installed it). Here are links for the create table statement.</p>
<ul>
<li><a href="https://trac.openstreetmap.org/browser/applications/utils/export/osm2pgsql/gazetteer/gazetteer-tables.sql#L70">https://trac.openstreetmap.org/browser/applications/utils/export/osm2pgsql/gazetteer/gazetteer-tables.sql#L70</a></li>
<li><a href="https://trac.openstreetmap.org/browser/applications/utils/nominatim/sql/tables.sql#L69">https://trac.openstreetmap.org/browser/applications/utils/nominatim/sql/tables.sql#L69</a></li>
<li><a href="https://github.com/twain47/Nominatim/blob/master/sql/tables.sql#L69">https://github.com/twain47/Nominatim/blob/master/sql/tables.sql#L69</a></li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 May '12, 15:26</strong></p>
<img src="https://secure.gravatar.com/avatar/dd655a7de48df0e3c15cd26c9fb33806?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brian_252&#39;s gravatar image" />
<p><span>brian_252</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brian_252 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 May '12, 00:08</strong> </span></p>
</div>
</div>
<div id="comments-container-12561" class="comments-container">
<span id="12563"></span>
<div id="comment-12563" class="comment">
<div id="post-12563-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Please tell us what word table you are talking about.</p>
</div>
<div id="comment-12563-info" class="comment-info">
<span class="comment-age">(05 May '12, 17:10)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-12561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12561-form-container" class="comment-form-container">
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

<span id="12578"></span>

<div id="answer-container-12578" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12578-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-12578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="brian_252 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Tokens with a leading space constitute full matches (names), while those with out spaces are simple words. To give an example: for 'swan lane rd', you will find ' swan lane rd' as the name and 'swan', 'lane' and 'rd' as partial words. Single word names have always two entries: 'london' will have ' london' for the full name and 'london' as a word match.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '12, 14:39</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-12578" class="comments-container">
&#10;</div>
<div id="comment-tools-12578" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12578-form-container" class="comment-form-container">
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

