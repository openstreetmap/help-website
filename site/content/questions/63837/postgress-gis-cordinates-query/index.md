+++
type = "question"
title = "postgress gis cordinates query"
description = '''I imported OSM data using osm2pgsql osm (slim) to gis posetgres Now I want to get all roads close to a point. I use this query: SELECT * FROM planet_osm_line ORDER BY ST_SetSrid(way, 4326) &amp;lt;-&amp;gt; ST_SetSrid(ST_Point(48.8523,2.3466), 4326) LIMIT 20;  Its give me results but from a point much south...'''
date = "2018-05-29T11:56:00Z"
lastmod = "2018-05-30T11:14:00Z"
weight = 63837
keywords = [ "query", "gis", "postgress", "osm2pgsql" ]
aliases = [ "/questions/63837" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [postgress gis cordinates query](/questions/63837/postgress-gis-cordinates-query)

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
<span id="post-63837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63837-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I imported OSM data using osm2pgsql osm (slim) to gis posetgres Now I want to get all roads close to a point. I use this query:</p>
<pre><code>SELECT * FROM planet_osm_line
ORDER BY ST_SetSrid(way, 4326) &lt;-&gt; ST_SetSrid(ST_Point(48.8523,2.3466), 4326) LIMIT 20;</code></pre>
<p>Its give me results but from a point much southeast then the point I asked (center of Paris) I think that something with the SRID but can't find the problem.</p>
<p>Any ideas? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span> <span class="post-tag tag-link-postgress" rel="tag" title="see questions tagged &#39;postgress&#39;">postgress</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 May '18, 11:56</strong></p>
<img src="https://secure.gravatar.com/avatar/53c4a40bd104f3de1bbc6ccb735e52eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="altopalo&#39;s gravatar image" />
<p><span>altopalo</span><br />
<span class="score" title="53 reputation points">53</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="altopalo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 May '18, 11:57</strong> </span></p>
</div>
</div>
<div id="comments-container-63837" class="comments-container">
&#10;</div>
<div id="comment-tools-63837" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63837-form-container" class="comment-form-container">
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

<span id="63840"></span>

<div id="answer-container-63840" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63840-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63840-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63840-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="altopalo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You want to</p>
<pre><code>SELECT * FROM planet_osm_line
ORDER BY way &lt;-&gt; ST_Transform(ST_SetSrid(ST_Point(48.8523,2.3466), 4326), 3857) LIMIT 20;</code></pre>
<p>Your query would only work if you had used -l (ell) during import.</p>
<p>Caveat: Your query does not necessarily give you the results in the order "nearest to farthest" because you are using a projected coordinate system; you can experiment by having PostGIS give you the ST_Distance of <code>st_transform(way,4326)::geography</code> and <code>ST_Point(48.8523,2.3466)::geography</code> to see this. It is possible that a way that is exactly 50.1 metres north of your point is displayed before a way that is exactly 49.9 metres east.</p>
<p>(edit: removed a suggestion to use ST_DWITHIN, as I see that the KNN operator is already index-aware.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '18, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 May '18, 13:07</strong> </span></p>
</div>
</div>
<div id="comments-container-63840" class="comments-container">
<span id="63865"></span>
<div id="comment-63865" class="comment">
<div id="post-63865-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Tn'x, great help. For what I need, I don't really need the nearest order , just some roads around a point. I think I'll use the ST_DWITHIN as you suggest to get all roars in some distance from point instead.</p>
</div>
<div id="comment-63865-info" class="comment-info">
<span class="comment-age">(30 May '18, 11:14)</span> <span class="comment-user userinfo">altopalo</span>
</div>
</div>
</div>
<div id="comment-tools-63840" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63840-form-container" class="comment-form-container">
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

