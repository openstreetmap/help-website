+++
type = "question"
title = "Tile server stopped updating private OSM changes"
description = '''I have a diff.osc file with a changeset #40293631 in a private OSM server. This is apparently one of the successful updates sent to a tile server. In the part of the file I have following, specifically related to a node id 4269514246: &amp;lt;create&amp;gt;  &amp;lt;node id=&quot;4269514246&quot; version=&quot;1&quot; timestamp=&quot;2...'''
date = "2018-08-03T11:21:00Z"
lastmod = "2018-08-03T11:21:00Z"
weight = 65098
keywords = [ "diff", "api", ".osc", "tileserver" ]
aliases = [ "/questions/65098" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tile server stopped updating private OSM changes](/questions/65098/tile-server-stopped-updating-private-osm-changes)

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
<span id="post-65098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65098-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a diff.osc file with a changeset #40293631 in a private OSM server. This is apparently one of the successful updates sent to a tile server. In the part of the file I have following, specifically related to a node id 4269514246:</p>
<pre><code>&lt;create&gt;
   &lt;node id=&quot;4269514246&quot; version=&quot;1&quot; timestamp=&quot;2018-07-13T03:40:33Z&quot; uid=&quot;4170915&quot; user=&quot;ABC&quot; changeset=&quot;40293631&quot; lat=&quot;43.1734836&quot; lon=&quot;77.0276441&quot;/&gt;
&lt;/create&gt;
&lt;modify&gt;
   &lt;way id=&quot;238131937&quot; version=&quot;6&quot; timestamp=&quot;2018-07-13T03:40:35Z&quot; uid=&quot;4170915&quot; user=&quot;ABC&quot; changeset=&quot;40293631&quot;&gt;
      &lt;nd ref=&quot;4269514246&quot;/&gt;
   &lt;/way&gt;
&lt;/modify&gt;
&lt;create&gt;
   &lt;way id=&quot;428143996&quot; version=&quot;1&quot; timestamp=&quot;2018-07-13T03:40:34Z&quot; uid=&quot;4170915&quot; user=&quot;ABC&quot; changeset=&quot;40293631&quot;&gt;
      &lt;nd ref=&quot;4269514246&quot;/&gt;
   &lt;tag .../&gt;
&lt;/create&gt;</code></pre>
<p>Now I would like to locate those updates in PostgreSQL database. In it I searched following:</p>
<pre><code> gis=# select * from planet_osm_nodes where id=4269514246;
         id     |    lat    |    lon    | tags
    ------------+-----------+-----------+------ 
    4269514246 | 533841521 | 857467812 | (1 row)</code></pre>
<p>I found that the coordinates need to be converted to decimal format, so I did:</p>
<pre><code>gis=# select id,ST_X(ST_AsText(st_transform(st_geomfromtext(&#39;POINT (&#39;||lon/100||&#39; &#39;||lat/100||&#39;)&#39;,900913),4326))) as lon, ST_Y(ST_AsText(st_transform(st_geomfromtext(&#39;POINT (&#39;||lon/100||&#39; &#39;||lat/100||&#39;)&#39;,900913),4326))) as lat from planet_osm_nodes where id=4269514246;
     id     |       lon        |       lat
------------+------------------+------------------  
4269514246 | 77.0276430380341 | 43.1734822268193 (1 row)</code></pre>
<p>But I realised that the coordinates in the database and diff.osc file are not the same. The diff file's and the database's lon,lat respectively are<br />
[43.1734836, 77.0276441]<br />
[43.1734822268193, 77.0276430380341]<br />
</p>
<p>Could there be conversion mistake or something else is causing it? Please, also advise on better troubleshooting methods, if they exist? Is there a way to get the last update on the tile server, if it does not save timestamps?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-.osc" rel="tag" title="see questions tagged &#39;.osc&#39;">.osc</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '18, 11:21</strong></p>
<img src="https://secure.gravatar.com/avatar/5536b85874cbcefafb22f75e03e91003?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khassen&#39;s gravatar image" />
<p><span>khassen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khassen has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Aug '18, 11:25</strong> </span></p>
</div>
</div>
<div id="comments-container-65098" class="comments-container">
&#10;</div>
<div id="comment-tools-65098" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65098-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

