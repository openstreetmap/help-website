+++
type = "question"
title = "Get village names with lat lon coords without duplicate village names"
description = '''I used this query to extract all village names with lat lon coords: SELECT name, st_astext(st_transform(way, 4326)) FROM planet_osm_point WHERE place=&#x27;village&#x27; ORDER BY name;  Example: Abertamy | POINT(12.8182600982157 50.3687442948073) Adamov | POINT(15.4089128978551 49.8578161948231) Adamov | POIN...'''
date = "2021-09-27T14:59:00Z"
lastmod = "2021-09-28T10:32:00Z"
weight = 81980
keywords = [ "coordinates", "postgres", "postgis", "village" ]
aliases = [ "/questions/81980" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Get village names with lat lon coords without duplicate village names](/questions/81980/get-village-names-with-lat-lon-coords-without-duplicate-village-names)

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
<span id="post-81980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81980-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I used this query to extract all village names with lat lon coords:</p>
<pre><code>SELECT name, st_astext(st_transform(way, 4326)) FROM planet_osm_point WHERE place=&#39;village&#39; ORDER BY name;</code></pre>
<p>Example:</p>
<pre><code>Abertamy | POINT(12.8182600982157 50.3687442948073)
Adamov   | POINT(15.4089128978551 49.8578161948231)
Adamov   | POINT(14.5395935979761 49.0005116948522)
Adamov   | POINT(15.9781534977758 50.5416186948022)
Adolfov  | POINT(13.9049393980644 50.7353921947967)</code></pre>
<p>As you can see name Adamov listed 3 times. How to get all village names with lat lon coords without duplicate village names? Even if lat lon of the same village name are significantly different</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-village" rel="tag" title="see questions tagged &#39;village&#39;">village</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Sep '21, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/1aeb86ca63b3378f4f80751ca910ec2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="akulin&#39;s gravatar image" />
<p><span>akulin</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="akulin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81980" class="comments-container">
<span id="81982"></span>
<div id="comment-81982" class="comment">
<div id="post-81982-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you mean that where several different villages have the same name, you only want to extract one of them? But then which lat/lon do you want to extract?</p>
</div>
<div id="comment-81982-info" class="comment-info">
<span class="comment-age">(27 Sep '21, 15:38)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="81983"></span>
<div id="comment-81983" class="comment">
<div id="post-81983-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I need the first available coordinates, just ignore the others. Like for Adamov will be used only first point from my "Example"</p>
</div>
<div id="comment-81983-info" class="comment-info">
<span class="comment-age">(27 Sep '21, 15:44)</span> <span class="comment-user userinfo">akulin</span>
</div>
</div>
<span id="81984"></span>
<div id="comment-81984" class="comment">
<div id="post-81984-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess it shoud be something with DISTINCT(name)</p>
</div>
<div id="comment-81984-info" class="comment-info">
<span class="comment-age">(27 Sep '21, 16:55)</span> <span class="comment-user userinfo">akulin</span>
</div>
</div>
</div>
<div id="comment-tools-81980" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81980-form-container" class="comment-form-container">
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

<span id="81989"></span>

<div id="answer-container-81989" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81989-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-81989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="akulin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not familiar with PostgreSQL and PostGIS specifics but in general SQL you could do that with an aggregate function. Something like this:</p>
<pre><code>SELECT name, FIRST(st_astext(st_transform(way, 4326))) AS unique_coord
FROM planet_osm_point 
WHERE place=&#39;village&#39;
GROUP BY name 
ORDER BY name;</code></pre>
<p><code>FIRST()</code> is not available in all dialects. <code>MIN()</code> might do the trick if you only look at one column.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '21, 09:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-81989" class="comments-container">
<span id="81992"></span>
<div id="comment-81992" class="comment">
<div id="post-81992-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Agreed this is a standard SQL problem, solvable using Window functions. The Postgres reference is here <a href="https://www.postgresql.org/docs/9.1/functions-window.html">https://www.postgresql.org/docs/9.1/functions-window.html</a></p>
</div>
<div id="comment-81992-info" class="comment-info">
<span class="comment-age">(28 Sep '21, 09:43)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="81993"></span>
<div id="comment-81993" class="comment">
<div id="post-81993-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Works ok with MIN()</p>
</div>
<div id="comment-81993-info" class="comment-info">
<span class="comment-age">(28 Sep '21, 10:32)</span> <span class="comment-user userinfo">akulin</span>
</div>
</div>
</div>
<div id="comment-tools-81989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81989-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81986"></span>

<div id="answer-container-81986" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81986-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>SELECT DISTINCT ON (name) name, st_astext(st_transform(way, 4326)) FROM planet_osm_point WHERE place=&#39;village&#39; ORDER BY name;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Sep '21, 17:01</strong></p>
<img src="https://secure.gravatar.com/avatar/1aeb86ca63b3378f4f80751ca910ec2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="akulin&#39;s gravatar image" />
<p><span>akulin</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="akulin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81986" class="comments-container">
<span id="81990"></span>
<div id="comment-81990" class="comment">
<div id="post-81990-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I doubt that works since the coordinates are not DISTINCT and as such the query would still return all lines. But maybe DISTINCT is handled differently in PostgreSQL/PostGIS than in other SQL dialects.</p>
</div>
<div id="comment-81990-info" class="comment-info">
<span class="comment-age">(28 Sep '21, 09:06)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="81991"></span>
<div id="comment-81991" class="comment">
<div id="post-81991-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10133/tzorn">@TZorn</a> I believe it is DISTINCT ON (name) that makes this different from a standard SQL DISTINCT query.</p>
</div>
<div id="comment-81991-info" class="comment-info">
<span class="comment-age">(28 Sep '21, 09:34)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-81986" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81986-form-container" class="comment-form-container">
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

