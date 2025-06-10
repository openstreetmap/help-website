+++
type = "question"
title = "find points that are a certain distance from another point"
description = '''Hi I have a java program which I want to query my PostGIS databaes and return those nodes that are a certain distance from a given centre point. I am not sure how to pass the centre point into the query. I have the following so far:  public ArrayList&amp;lt;Node&amp;gt; getOsmPoiNodes(Point centrePoint) thr...'''
date = "2012-12-03T16:30:00Z"
lastmod = "2012-12-22T22:13:00Z"
weight = 18168
keywords = [ "osm", "java", "postgis", "sql" ]
aliases = [ "/questions/18168" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [find points that are a certain distance from another point](/questions/18168/find-points-that-are-a-certain-distance-from-another-point)

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
<span id="post-18168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18168-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I have a java program which I want to query my PostGIS databaes and return those nodes that are a certain distance from a given centre point.</p>
<p>I am not sure how to pass the centre point into the query. I have the following so far:</p>
<pre><code> public ArrayList&lt;Node&gt; getOsmPoiNodes(Point centrePoint) throws SQLException {
&#10;        /* 
         * Create a statement and execute a select query. 
         */ 
        Statement s = conn.createStatement(); 
        String sql = &quot;select ST_Distance(&quot; + centrePoint + &quot;,way), ST_AsGeoJSON(ST_Transform(way,94326) from planet_osm_point;&quot;;</code></pre>
<p>How could I pass the PostGis Point object in properly?</p>
<p>Also, when I am defining the distance from the centre point. Can I simply do a <code>HAVING(ST_Distance(centrePoint, way) &lt;= '100'</code> where 100 would be in metres?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '12, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/8f19a0a6b0afe902c224e03a8eb38ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srose&#39;s gravatar image" />
<p><span>srose</span><br />
<span class="score" title="161 reputation points">161</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18168" class="comments-container">
&#10;</div>
<div id="comment-tools-18168" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18168-form-container" class="comment-form-container">
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

<span id="18668"></span>

<div id="answer-container-18668" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18668-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="srose has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use ST_GeomFromText:</p>
<p>Example: select st_geomfromtext('point(-23.4 -46.2)'::text, 93426); -- Lat/Lon/SRID</p>
<p>I would say that, unless some other optimizations are made, that this way of querying the database would - most likely - be <em>VERY</em> slow.</p>
<p>See: <a href="http://www.postgis.org/docs/ST_Distance.html">ST_Distance</a> and <a href="http://www.postgis.org/docs/ST_GeomFromText.html">ST_GeomFromText</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Dec '12, 22:13</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-18668" class="comments-container">
&#10;</div>
<div id="comment-tools-18668" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18668-form-container" class="comment-form-container">
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

