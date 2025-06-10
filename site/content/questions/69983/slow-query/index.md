+++
type = "question"
title = "Slow query"
description = '''Hello,  I have a very slow query,  if I remove the  WHERE active is null  Its work great (there is an index on that field of course) Query: SELECT data_gis.id, ex_data.title, ex_data.description, ex_data.ex_text,   ST_Y(ST_Transform(way, 4326)) as lat, ST_X(ST_Transform(way, 4326)) as lon, active  F...'''
date = "2019-07-11T07:35:00Z"
lastmod = "2019-07-11T08:32:00Z"
weight = 69983
keywords = [ "query", "slow", "postgis" ]
aliases = [ "/questions/69983" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Slow query](/questions/69983/slow-query)

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
<span id="post-69983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69983-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-69983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have a very slow query,</p>
<p>if I remove the</p>
<pre><code>WHERE active is null</code></pre>
<p>Its work great (there is an index on that field of course)</p>
<p>Query:</p>
<pre><code>SELECT data_gis.id, ex_data.title, ex_data.description, ex_data.ex_text,  
    ST_Y(ST_Transform(way, 4326)) as lat, ST_X(ST_Transform(way, 4326)) as lon, active 
FROM ex_data join data_gis 
    on ex_data.data_gis_id = data_gis.id 
WHERE 
    active is null 
    and ST_DWithin(ST_Transform(ST_SetSrid(ST_Point(51.758783,-1.152665), 4326), 3857), way, 5000.0)  
ORDER BY 
    way &lt;-&gt; ST_Transform(ST_SetSrid(ST_Point(51.758783,-1.152665), 4326), 3857)  
LIMIT 25;</code></pre>
<p>Query plan:</p>
<pre><code> Limit  (cost=60141.06..60143.98 rows=25 width=269)
   -&gt;  Gather Merge  (cost=60141.06..60175.13 rows=292 width=269)
         Workers Planned: 2
         -&gt;  Sort  (cost=59141.04..59141.40 rows=146 width=269)
               Sort Key: ((data_gis.way &lt;-&gt; &#39;010100....&#39;::geometry))
               -&gt;  Nested Loop  (cost=285.26..59135.79 rows=146 width=269)
                     -&gt;  Parallel Bitmap Heap Scan on ex_data  (cost=284.82..28888.62 rows=10972 width=148)
                           Recheck Cond: (active IS NULL)
                           -&gt;  Bitmap Index Scan on ex_data_org_lang_pkey  (cost=0.00..278.24 rows=26334 width=0)
                                 Index Cond: (org_lang IS NULL)
                     -&gt;  Index Scan using data_gis_pkey on data_gis  (cost=0.44..2.76 rows=1 width=137)
                           Index Cond: (id = ex_data.data_gis_id)
                           Filter: ((way &amp;&amp; &#39;010300002......&#39;::geometry) AND (&#39;010100002011.....&#39;::geometry &amp;&amp; st_expand(way, &#39;5000&#39;::double precision)) AND _st_dwithin(&#39;01010...&#39;::geometry, way, &#39;5000&#39;::double precision))
(13 rows)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '19, 07:35</strong></p>
<img src="https://secure.gravatar.com/avatar/53c4a40bd104f3de1bbc6ccb735e52eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="altopalo&#39;s gravatar image" />
<p><span>altopalo</span><br />
<span class="score" title="53 reputation points">53</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="altopalo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jul '19, 07:35</strong> </span></p>
</div>
</div>
<div id="comments-container-69983" class="comments-container">
&#10;</div>
<div id="comment-tools-69983" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69983-form-container" class="comment-form-container">
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

<span id="69984"></span>

<div id="answer-container-69984" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69984-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This question is off-topic here since it has nothing to do with OSM. Assuming that "acive" is in the same table as data_gis then you can likely fix the issue by creating a conditional index (<code>create index foo on table on data_gis using gist(way) where active is null</code>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '19, 08:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-69984" class="comments-container">
<span id="69985"></span>
<div id="comment-69985" class="comment">
<div id="post-69985-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>tn'x but active field is in ex_data table and way is in data_gis table.</p>
</div>
<div id="comment-69985-info" class="comment-info">
<span class="comment-age">(11 Jul '19, 08:32)</span> <span class="comment-user userinfo">altopalo</span>
</div>
</div>
</div>
<div id="comment-tools-69984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69984-form-container" class="comment-form-container">
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

