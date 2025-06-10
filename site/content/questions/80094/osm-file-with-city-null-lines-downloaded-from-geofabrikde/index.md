+++
type = "question"
title = "OSM file with city null lines (downloaded from geofabrik.de)"
description = '''Hello, I downloaded an OSM file from my area (Italy islands) to process it with Java and present an application to my organization. The purpose is, given a point on the map where a criminal activity is in progress, to find in the vicinity (e.g. 500 meters or 1 Km) all the POIs that represent sensiti...'''
date = "2021-05-10T05:07:00Z"
lastmod = "2021-05-10T10:03:00Z"
weight = 80094
keywords = [ "city", "null", ".osm", "geofabrik" ]
aliases = [ "/questions/80094" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OSM file with city null lines (downloaded from geofabrik.de)](/questions/80094/osm-file-with-city-null-lines-downloaded-from-geofabrikde)

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
<span id="post-80094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80094-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I downloaded an OSM file from my area (Italy islands) to process it with Java and present an application to my organization. The purpose is, given a point on the map where a criminal activity is in progress, to find in the vicinity (e.g. 500 meters or 1 Km) all the POIs that represent sensitive targets (banks, schools, jewelers, etc.) that can become secondary targets for crimes. For now, I need this information in data format and not as a map. The problem is that in the OSM file I have the city field is often null and from the geographic coordinates of the city limits I cannot make an initial list of all the POIs present. At this point I thought about changing cities hoping that there is one that has a more complete OSM file.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-null" rel="tag" title="see questions tagged &#39;null&#39;">null</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 May '21, 05:07</strong></p>
<img src="https://secure.gravatar.com/avatar/4f344de5970d6d8d291e78c4f27c7847?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lorenzopandolfo&#39;s gravatar image" />
<p><span>Lorenzopandolfo</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lorenzopandolfo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80094" class="comments-container">
<span id="80097"></span>
<div id="comment-80097" class="comment">
<div id="post-80097-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which "city field" is null? Is this about the <code>addr:city</code> tag?</p>
</div>
<div id="comment-80097-info" class="comment-info">
<span class="comment-age">(10 May '21, 08:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="80100"></span>
<div id="comment-80100" class="comment">
<div id="post-80100-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>exactly I am referring to that tag.</p>
</div>
<div id="comment-80100-info" class="comment-info">
<span class="comment-age">(10 May '21, 08:38)</span> <span class="comment-user userinfo">Lorenzopandolfo</span>
</div>
</div>
<span id="80107"></span>
<div id="comment-80107" class="comment">
<div id="post-80107-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What tool, or library, are you using to read the OSM file ? You probably can search around a point and don't care about the city limits.</p>
<p>If you need to reduce the size of the file, I pretty sure osmium, or osmconvert, can crop an OSM file based on a geoJSON, which you could get from overpass-turbo.</p>
<p>Regards.</p>
</div>
<div id="comment-80107-info" class="comment-info">
<span class="comment-age">(10 May '21, 10:03)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-80094" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80094-form-container" class="comment-form-container">
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

<span id="80103"></span>

<div id="answer-container-80103" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80103-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-80103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Lorenzopandolfo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot count on the addr:city field being set. You have to work, as you say, with the geographic coordinates of the city boundary which will often be present in OSM. If you load the OSM data into a PostgreSQL database with osm2pgsql, creating the list of POIs in a city is trivial. First, find the relation ID of the city,</p>
<pre><code>select osm_id,name 
from planet_osm_polygon 
where boundary=&#39;administrative&#39; and admin_level=8;</code></pre>
<p>(Add an "and name like '%something%' to reduce the list to certain names only. In some countries cities might have a different admin_level; sometimes this also depends on the city size. Check the boundary=administrative wiki page for details.)</p>
<p>Once you have the ID of the boundary (let's say it was -41485 which is the city of Rome), you can do something like</p>
<pre><code>select * from planet_osm_point p,     
   planet_osm_polygon q
where q.id=-41485 and st_contains(q.way, p.way);</code></pre>
<p>You could also add something like "and amenity in ('bank','post_office', ...)" to that query to limit the results.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 May '21, 09:43</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-80103" class="comments-container">
&#10;</div>
<div id="comment-tools-80103" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80103-form-container" class="comment-form-container">
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

