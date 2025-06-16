+++
type = "question"
title = "Speeding up OpenStreetMap PostGIS querying"
description = '''I asked this question on gis.stackexchange.com as well, but hope to catch some more expertise here. I have OpenStreetMap data for the Netherlands loaded into a PostGIS database (PostgreSQL 8.3 / PostGIS 1.3.3) using the osmosis schema. This means all tags are stored in a hstore field. In addition to...'''
date = "2011-03-22T16:06:00Z"
lastmod = "2014-12-15T14:14:00Z"
weight = 3988
keywords = [ "query", "postgresql", "postgis" ]
aliases = [ "/questions/3988" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Speeding up OpenStreetMap PostGIS querying](/questions/3988/speeding-up-openstreetmap-postgis-querying)

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
<span id="post-3988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3988-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I asked this question <a href="http://gis.stackexchange.com/questions/7574/speeding-up-openstreetmap-postgis-querying">on</a> <a href="http://gis.stackexchange.com"></a><a href="http://gis.stackexchange.com">gis.stackexchange.com</a> as well, but hope to catch some more expertise here.</p>
<p>I have OpenStreetMap data for the Netherlands loaded into a PostGIS database (PostgreSQL 8.3 / PostGIS 1.3.3) using the <a href="https://wiki.openstreetmap.org/wiki/Osmosis/PostGIS_Setup">osmosis schema</a>. This means all tags are stored in a <a href="http://www.postgresql.org/docs/8.3/interactive/hstore.html">hstore</a> field. In addition to the GIST index that osmosis creates on the geometry field, I created an additional GIST index on the tags field.</p>
<p>Trying to query using both a spatial constraint and a constraint on the tags field, I find that it is slower than I would like. A query like this one:</p>
<pre><code>SELECT n.geom,n.tags,n.tstamp,u.name FROM nodes AS n 
  INNER JOIN users AS u ON n.user_id = u.id 
  WHERE tags-&gt;&#39;man_made&#39;=&#39;surveillance&#39; 
  AND ST_Within(geom, ST_GeomFromText(&#39;POLYGON((4.0 52.0,5.0 52.0,5.0 53.0,4.0 53.0,4.0 52.0))&#39;,4326));</code></pre>
<p>takes 22 seconds to return 78 records.</p>
<p>There are around 53 million records in this table.</p>
<p>Is there a way to significantly speed this up? I've heard that hstore is implemented significantly better in PostgreSQL 9, would upgrading help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '11, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/acea3c9fd5908d7ff09596d16b8724d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mvexel&#39;s gravatar image" />
<p><span>mvexel</span><br />
<span class="score" title="762 reputation points">762</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mvexel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3988" class="comments-container">
&#10;</div>
<div id="comment-tools-3988" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3988-form-container" class="comment-form-container">
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

<span id="39497"></span>

<div id="answer-container-39497" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39497-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've never optimised a hstore column, so I can't speak to that. If you split out the <code>man_made</code> value into a separate column, you can add a <code>WHERE</code> clause to the geom index. I've seen big speed ups from that. i.e. <code>CREATE INDEX blah ON nodes using gist (geom) WHERE man_made = 'surveillance'</code>. You'll now have 2 geometry indexes, one on the <code>geom</code>, and a subset that only has rows where <code>man_made = surveillance</code>. IME PostgreSQL is smart enough to know to use the smaller index, which means scanning the index will be faster.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '14, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-39497" class="comments-container">
&#10;</div>
<div id="comment-tools-39497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39497-form-container" class="comment-form-container">
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

