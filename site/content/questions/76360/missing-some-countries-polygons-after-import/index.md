+++
type = "question"
title = "Missing some countries polygons after import"
description = '''Hello, A few days ago I updated my database with the latest planet file. Everything looks ok but I&#x27;m missing the Russia entry in planet_osm_polygon. It is found in both planet_osm_roads: osm=&amp;gt; osm=&amp;gt; select admin_level, name osm-&amp;gt; from planet_osm_roads osm-&amp;gt; where osm_id = -60189 and boun...'''
date = "2020-08-30T18:04:00Z"
lastmod = "2020-08-30T18:04:00Z"
weight = 76360
keywords = [ "missing", "planet_osm_polygon", "osm2pgsql" ]
aliases = [ "/questions/76360" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Missing some countries polygons after import](/questions/76360/missing-some-countries-polygons-after-import)

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
<span id="post-76360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76360-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>A few days ago I updated my database with the latest planet file. Everything looks ok but I'm missing the Russia entry in planet_osm_polygon.</p>
<p>It is found in both planet_osm_roads:</p>
<pre><code>osm=&gt;
osm=&gt; select admin_level, name
osm-&gt; from planet_osm_roads
osm-&gt; where osm_id = -60189 and boundary = &#39;administrative&#39;
osm-&gt; limit 1;
 admin_level |  name
-------------+--------
 2           | Россия
(1 row)</code></pre>
<p>and planet_osm_line:</p>
<pre><code>osm=&gt; select admin_level, name
osm-&gt; from planet_osm_line
osm-&gt; where osm_id = -60189 and boundary = &#39;administrative&#39;
osm-&gt; limit 1;
 admin_level |  name
-------------+--------
 2           | Россия
(1 row)</code></pre>
<p>But not in planet_osm_polygon:</p>
<pre><code>osm=&gt; select admin_level, name
osm-&gt; from planet_osm_polygon
osm-&gt; where osm_id = -60189 and boundary = &#39;administrative&#39;
osm-&gt; limit 1;
 admin_level | name
-------------+------
(0 rows)</code></pre>
<p>On my production server using an older planet.pbf file, it is in planet_osm_polygon as well.</p>
<p>What could be wrong?</p>
<p>Edit: I'm missing multiple other countries as well: Brazil, Argentina, Chile...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span> <span class="post-tag tag-link-planet_osm_polygon" rel="tag" title="see questions tagged &#39;planet_osm_polygon&#39;">planet_osm_polygon</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Aug '20, 18:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a711e0129f307399a857a6f9b4bfd0e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="timautin&#39;s gravatar image" />
<p><span>timautin</span><br />
<span class="score" title="151 reputation points">151</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="timautin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Aug '20, 20:31</strong> </span></p>
</div>
</div>
<div id="comments-container-76360" class="comments-container">
&#10;</div>
<div id="comment-tools-76360" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76360-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

