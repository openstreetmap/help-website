+++
type = "question"
title = "How do you make the osm2pgsql diff imports run faster than molasses on postgres 8.4?"
description = '''Using postgres 8.4 diff imports seem to run as slow as a license change. I&#x27;ve hear that it&#x27;s better to use postgres 8.3. Is there any other way?'''
date = "2010-06-25T16:34:00Z"
lastmod = "2012-01-17T13:02:00Z"
weight = 1
keywords = [ "diff", "rendering", "osm2pgsql", "postgres" ]
aliases = [ "/questions/1" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do you make the osm2pgsql diff imports run faster than molasses on postgres 8.4?](/questions/1/how-do-you-make-the-osm2pgsql-diff-imports-run-faster-than-molasses-on-postgres-84)

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
<span id="post-1-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using postgres 8.4 diff imports seem to run as slow as a license change. I've hear that it's better to use postgres 8.3. Is there any other way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jun '10, 16:34</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jul '10, 17:21</strong> </span></p>
</div>
</div>
<div id="comments-container-1" class="comments-container">
&#10;</div>
<div id="comment-tools-1" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="55"></span>

<div id="answer-container-55" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-55-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Frederik Ramm mentioned this in <a href="http://wiki.openstreetmap.org/wiki/SotM_2010_session:Tuning_the_Mapnik_Rendering_Chain">his SOTM10 presentation</a> and he has had a chance to try Postgres 9.0 (with Postgis 1.5) and that apparently no longer suffers from this slowdown - in fact it is apparently faster than Postgres 8.3 in his benchmarks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '10, 16:53</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Sep '10, 08:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-55" class="comments-container">
<span id="10016"></span>
<div id="comment-10016" class="comment">
<div id="post-10016-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Meanwhile PostgreSQL 9.1 is available</p>
</div>
<div id="comment-10016-info" class="comment-info">
<span class="comment-age">(17 Jan '12, 13:02)</span> <span class="comment-user userinfo">saerdnaer</span>
</div>
</div>
</div>
<div id="comment-tools-55" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5"></span>

<div id="answer-container-5" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-5-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problems seem to relate to GIN index updates. In the case of osm2pgsql this seems to be particularly updates to planet_osm_ways_nodes, which is the index on the list of nodes for a way.</p>
<p>Given the the imminent release of postgresql 9.0 it seems likely that this problem won't get resolved and will probably be reinvestigated once 9.0 is out.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '10, 17:40</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-5" class="comments-container">
&#10;</div>
<div id="comment-tools-5" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5-form-container" class="comment-form-container">
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

