+++
type = "question"
title = "Nearest point on a planet_osm_roads"
description = '''I have a query that give me the nearest roads to a point SELECT osm_id, ref, name, way, ST_AsText(ST_Transform(way, 4326)), * FROM planet_osm_roads where  ST_DWithin(ST_Transform(ST_SetSrid(ST_Point(-1.28779, 51.78976), 4326), 3857), way, 20) ORDER BY way &amp;lt;-&amp;gt; ST_Transform(ST_SetSrid(ST_Point(-...'''
date = "2018-12-05T08:48:00Z"
lastmod = "2018-12-05T08:48:00Z"
weight = 67071
keywords = [ "psql", "planet_osm_roads", "postgis" ]
aliases = [ "/questions/67071" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nearest point on a planet_osm_roads](/questions/67071/nearest-point-on-a-planet_osm_roads)

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
<span id="post-67071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67071-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a query that give me the nearest roads to a point</p>
<pre><code>SELECT osm_id, ref, name, way, ST_AsText(ST_Transform(way, 4326)), *
FROM planet_osm_roads
where 
ST_DWithin(ST_Transform(ST_SetSrid(ST_Point(-1.28779, 51.78976), 4326), 3857), way, 20)
ORDER BY way &lt;-&gt; ST_Transform(ST_SetSrid(ST_Point(-1.28779, 51.78976), 4326), 3857) LIMIT 5;</code></pre>
<p>Now I want in the same query to get for each road the nearest point(node) for my original point (-1.28779, 51.78976) I know how to do it in separate queries, but for less DB access I want it in the same query.</p>
<p>Tn;x for any help</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-psql" rel="tag" title="see questions tagged &#39;psql&#39;">psql</span> <span class="post-tag tag-link-planet_osm_roads" rel="tag" title="see questions tagged &#39;planet_osm_roads&#39;">planet_osm_roads</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Dec '18, 08:48</strong></p>
<img src="https://secure.gravatar.com/avatar/53c4a40bd104f3de1bbc6ccb735e52eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="altopalo&#39;s gravatar image" />
<p><span>altopalo</span><br />
<span class="score" title="53 reputation points">53</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="altopalo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67071" class="comments-container">
&#10;</div>
<div id="comment-tools-67071" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67071-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

