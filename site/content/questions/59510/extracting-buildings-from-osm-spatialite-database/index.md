+++
type = "question"
title = "extracting buildings from osm spatialite database"
description = '''Hi, I downloaded OSM data from Geofabrik and saved it in a Spatialite database. Now I want to select all the buildings from my region and save it in a separate table. Is there a way to do this in Spatialite with a Inner Join between the osm nodes id/tags tables and the way id/tags tables? '''
date = "2017-09-10T18:42:00Z"
lastmod = "2017-09-10T19:11:00Z"
weight = 59510
keywords = [ "sqlite", "osm", "database" ]
aliases = [ "/questions/59510" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [extracting buildings from osm spatialite database](/questions/59510/extracting-buildings-from-osm-spatialite-database)

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
<span id="post-59510-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59510-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59510-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I downloaded OSM data from Geofabrik and saved it in a Spatialite database. Now I want to select all the buildings from my region and save it in a separate table. Is there a way to do this in Spatialite with a Inner Join between the osm nodes id/tags tables and the way id/tags tables?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sqlite" rel="tag" title="see questions tagged &#39;sqlite&#39;">sqlite</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Sep '17, 18:42</strong></p>
<img src="https://secure.gravatar.com/avatar/d578f9b44b4a19a09dc3be982fe15a0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="terra03032006&#39;s gravatar image" />
<p><span>terra03032006</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="terra03032006 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59510" class="comments-container">
<span id="59511"></span>
<div id="comment-59511" class="comment">
<div id="post-59511-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>How did you convert from .osm.pbf (or .osm.bz2) to Spatialite? The software used for that will determine the options you have.</p>
</div>
<div id="comment-59511-info" class="comment-info">
<span class="comment-age">(10 Sep '17, 18:48)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="59512"></span>
<div id="comment-59512" class="comment">
<div id="post-59512-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I used the spatial_osm_raw tool like this: spatial_osm_raw -o region.osm.pbf -d my_data.sqlite</p>
</div>
<div id="comment-59512-info" class="comment-info">
<span class="comment-age">(10 Sep '17, 18:52)</span> <span class="comment-user userinfo">terra03032006</span>
</div>
</div>
<span id="59513"></span>
<div id="comment-59513" class="comment">
<div id="post-59513-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you really sure you want to go down this (hard) route which would require that you manually collect the nodes for building ways (as well as the ways and nodes for building relations!) when using <code>spatialite_osm_map</code> (instead of <code>spatialite_osm_raw</code>) promises to handle all this for you automatically?</p>
</div>
<div id="comment-59513-info" class="comment-info">
<span class="comment-age">(10 Sep '17, 18:56)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="59515"></span>
<div id="comment-59515" class="comment">
<div id="post-59515-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am not using these tools myself but when searching for the name of the tool on the web, I found <a href="https://www.gaia-gis.it/fossil/spatialite-tools/wiki?name=OSM+tools">https://www.gaia-gis.it/fossil/spatialite-tools/wiki?name=OSM+tools</a> which seems to explain that <code>spatialite_osm_map</code> already gives you tables for the individual feature types, including (I suppose) buildings!</p>
</div>
<div id="comment-59515-info" class="comment-info">
<span class="comment-age">(10 Sep '17, 19:00)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="59516"></span>
<div id="comment-59516" class="comment">
<div id="post-59516-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ya but I want to work with the raw data, are there some links which can help me to achieve my goal?</p>
</div>
<div id="comment-59516-info" class="comment-info">
<span class="comment-age">(10 Sep '17, 19:11)</span> <span class="comment-user userinfo">terra03032006</span>
</div>
</div>
</div>
<div id="comment-tools-59510" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59510-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

