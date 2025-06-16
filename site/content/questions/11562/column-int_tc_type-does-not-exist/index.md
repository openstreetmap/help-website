+++
type = "question"
title = "column &quot;int_tc_type&quot; does not exist"
description = '''Hey guys! When rendering from PostgreSQL/PostGIS database by Python/Mapnik I receice the following ERROR: http://dpaste.org/s8zIZ/  Traceback (most recent call last): File &quot;C:&#92;0A&#92;11&#92;generate_image.py&quot;, line 71, in &amp;lt;module&amp;gt; mapnik.render(m, im) RuntimeError: Postgis Plugin: PSQL error: ERROR: c...'''
date = "2012-03-28T15:44:00Z"
lastmod = "2012-03-29T10:17:00Z"
weight = 11562
keywords = [ "column", "rendering", "postgis", "mapnik", "int_tc_type" ]
aliases = [ "/questions/11562" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [column "int_tc_type" does not exist](/questions/11562/column-int_tc_type-does-not-exist)

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
<span id="post-11562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11562-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys! When rendering from PostgreSQL/PostGIS database by Python/Mapnik I receice the following ERROR: <a href="http://dpaste.org/s8zIZ/">http://dpaste.org/s8zIZ/</a></p>
<hr />
<pre><code>Traceback (most recent call last):
File &quot;C:\0A\11\generate_image.py&quot;, line 71, in &lt;module&gt;
mapnik.render(m, im)
RuntimeError: Postgis Plugin: PSQL error:
ERROR: column &quot;int_tc_type&quot; does not exist
LINE 1: SELECT ST_AsBinary(&quot;way&quot;) AS geom,&quot;int_tc_type&quot; from planet_...
^
Full sql was: &#39;SELECT ST_AsBinary(&quot;way&quot;) AS geom,&quot;int_tc_type&quot; from planet_osm_roads WHERE &quot;way&quot; &amp;&amp; SetSRID(&#39;BOX3D(1127187.934825658 7229086.56980958,1134824.118093661 7236722.753077583)&#39;::box3d, 900913)&#39;</code></pre>
<hr />
<p>I took the steps like in <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server/</a></p>
<p>My OS is Windows.</p>
<p>I imported my africa.osm by osm2pgsql to my database.</p>
<p>Is it possible, that the whole thing only works with the whole planet_latest.osm?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-column" rel="tag" title="see questions tagged &#39;column&#39;">column</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-int_tc_type" rel="tag" title="see questions tagged &#39;int_tc_type&#39;">int_tc_type</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Mar '12, 15:44</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0198a02af3c41ad04b61e028c3b126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MHein&#39;s gravatar image" />
<p><span>MHein</span><br />
<span class="score" title="141 reputation points">141</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MHein has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11562" class="comments-container">
&#10;</div>
<div id="comment-tools-11562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11562-form-container" class="comment-form-container">
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

<span id="11577"></span>

<div id="answer-container-11577" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11577-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MHein has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most likely the version of osm2psql is too old to work with the current mapnik stylesheet you are using. Try an older stylesheet eg: <a href="https://trac.openstreetmap.org/browser/applications/rendering/mapnik?rev=20000">https://trac.openstreetmap.org/browser/applications/rendering/mapnik?rev=20000</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '12, 21:57</strong></p>
<img src="https://secure.gravatar.com/avatar/e79628d44a15e95c607f8c5007d0ccd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Firefishy&#39;s gravatar image" />
<p><span>Firefishy ♦♦</span><br />
<span class="score" title="1296 reputation points"><span>1.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Firefishy has 14 accepted answers">29%</span></p>
</div>
</div>
<div id="comments-container-11577" class="comments-container">
<span id="11586"></span>
<div id="comment-11586" class="comment">
<div id="post-11586-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, but I don't find any stylesheet "default.style" there (maybe because the server</p>
<p>seems to be kind of down..) or did you think of the osm.xml?</p>
<p>Yesterday I downloaded a newer "default.style" to fix another Error</p>
<p><a href="/questions/11542/error-column-generatorsource-does-not-exist">https://help.openstreetmap.org/questions/11542/error-column-generatorsource-does-not-exist</a></p>
<p>How can I fix both of them? Is there any possibility to fill in the missing column by hand/manually? .. column "length" is also missing ..</p>
</div>
<div id="comment-11586-info" class="comment-info">
<span class="comment-age">(29 Mar '12, 10:17)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
</div>
<div id="comment-tools-11577" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11577-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

