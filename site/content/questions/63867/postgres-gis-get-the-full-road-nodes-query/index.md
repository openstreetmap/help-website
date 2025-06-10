+++
type = "question"
title = "postgres gis get the full road nodes query"
description = '''I have OSM data using osm2pgsql (slim) with default style in PostgreSQL GIS DB. For my usage I&#x27;m trying to predict where the customer will go according to his current position on some way node. In order to do so I want to get the all way (road) data by its current partial way. I know how to do it by...'''
date = "2018-05-30T11:22:00Z"
lastmod = "2018-12-13T12:53:00Z"
weight = 63867
keywords = [ "query", "gis", "postgres", "road" ]
aliases = [ "/questions/63867" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [postgres gis get the full road nodes query](/questions/63867/postgres-gis-get-the-full-road-nodes-query)

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
<span id="post-63867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63867-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have OSM data using osm2pgsql (slim) with default style in PostgreSQL GIS DB. For my usage I'm trying to predict where the customer will go according to his current position on some way node.</p>
<p>In order to do so I want to get the all way (road) data by its current partial way.</p>
<p>I know how to do it by overpass using recursion up but can't find how to do it with SQL query (actually I done something but not so good by getting the way ref and then look for more ways with the same ref)</p>
<p>Tn'x for any help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '18, 11:22</strong></p>
<img src="https://secure.gravatar.com/avatar/53c4a40bd104f3de1bbc6ccb735e52eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="altopalo&#39;s gravatar image" />
<p><span>altopalo</span><br />
<span class="score" title="53 reputation points">53</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="altopalo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 May '18, 19:04</strong> </span></p>
</div>
</div>
<div id="comments-container-63867" class="comments-container">
<span id="63909"></span>
<div id="comment-63909" class="comment">
<div id="post-63909-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The answer is probably something with the relations between the data objects in the DB. So is there a good explanations of the data schema &amp; relations of the osm2postgress schema? (can't find a decent documentation on that)</p>
</div>
<div id="comment-63909-info" class="comment-info">
<span class="comment-age">(31 May '18, 10:42)</span> <span class="comment-user userinfo">altopalo</span>
</div>
</div>
</div>
<div id="comment-tools-63867" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63867-form-container" class="comment-form-container">
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

<span id="67164"></span>

<div id="answer-container-67164" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67164-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found the solution, so is someone will search for it.</p>
<p>Need to use planet_osm_rels table</p>
<p>Sample:</p>
<pre><code>select osm_id, ref, name, way 
FROM planet_osm_roads where ST_DWithin(ST_Transform(ST_SetSrid(ST_Point(-1.021076,51.714512), 4326), 3857), way,20000) 
and osm_id in( 
    SELECT distinct(unnest(parts)) as part 
    FROM planet_osm_rels 
    WHERE parts @&gt; ARRAY[147856382]::bigint[] and tags @&gt; ARRAY[&#39;M40&#39;]::text[]
)</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '18, 12:53</strong></p>
<img src="https://secure.gravatar.com/avatar/53c4a40bd104f3de1bbc6ccb735e52eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="altopalo&#39;s gravatar image" />
<p><span>altopalo</span><br />
<span class="score" title="53 reputation points">53</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="altopalo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Dec '18, 12:55</strong> </span></p>
</div>
</div>
<div id="comments-container-67164" class="comments-container">
&#10;</div>
<div id="comment-tools-67164" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67164-form-container" class="comment-form-container">
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

