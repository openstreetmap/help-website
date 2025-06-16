+++
type = "question"
title = "Why does my PostGIS load of Geofabrik Australian extract look different from www.openstreetmap.org?"
description = '''I have downloaded the Geofabrik Australia.osm.pbf extract dated 8/10/12 and loaded into a PostGIS database with osm2pgsql with no errors. However, when I display this data (using OpenLayers and MapServer), I see quite a different picture from what I see when I look at the same area on www.openstreet...'''
date = "2012-10-09T07:07:00Z"
lastmod = "2012-10-11T13:21:00Z"
weight = 16747
keywords = [ "excerpts", "geofabrik" ]
aliases = [ "/questions/16747" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Why does my PostGIS load of Geofabrik Australian extract look different from www.openstreetmap.org?](/questions/16747/why-does-my-postgis-load-of-geofabrik-australian-extract-look-different-from-wwwopenstreetmaporg)

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
<span id="post-16747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16747-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have downloaded the Geofabrik Australia.osm.pbf extract dated 8/10/12 and loaded into a PostGIS database with osm2pgsql with no errors.</p>
<p>However, when I display this data (using OpenLayers and MapServer), I see quite a different picture from what I see when I look at the same area on www.openstreetmap.org.</p>
<p>At <a href="https://www.openstreetmap.org/?lat=-34.932&amp;lon=138.574&amp;zoom=10&amp;layers=M">www.openstreetmap.org lat=-34.932, lon=138.574, zoom=10</a>, I see red, orange and green streets, green park names and quite a few parks, lakes and streams.</p>
<p>The same area in my map shows no green streets, no park names and only a couple of parks and lakes: generally much less detail.</p>
<p>Yesterday, I loaded the extract dated 7/10/12 and compared it with www.openstreetmap.org and saw much the same differences so it is not just a matter of missing a few updates.</p>
<p>How can I best get the more detailed data?</p>
<p>Cheers and thanks, Stephen</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-excerpts" rel="tag" title="see questions tagged &#39;excerpts&#39;">excerpts</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '12, 07:07</strong></p>
<img src="https://secure.gravatar.com/avatar/91bfd1591ae1c53100f55da985cb3c7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stephen%20C%20Davies&#39;s gravatar image" />
<p><span>Stephen C Da...</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stephen C Davies has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Oct '12, 11:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-16747" class="comments-container">
&#10;</div>
<div id="comment-tools-16747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16747-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="16825"></span>

<div id="answer-container-16825" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16825-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Today I trashed my PostGIS database and created a new one using imposm (instead of osm2pgsql).</p>
<p>I also recreated my map file using a new download of the mapserver-utils in "default" mode.</p>
<p>The result is significantly closer to the OSM original but still has less detail.</p>
<p>I have searched through the database and confirmed that there are a lot of features in the database that fail to meet any of the criteria in the map file so the bottom line seems to be that I need to manually edit the generated map file to include the ones that I want/need.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Oct '12, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/91bfd1591ae1c53100f55da985cb3c7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stephen%20C%20Davies&#39;s gravatar image" />
<p><span>Stephen C Da...</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stephen C Davies has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16825" class="comments-container">
&#10;</div>
<div id="comment-tools-16825" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16825-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16843"></span>

<div id="answer-container-16843" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16843-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap's default "mapnik" map layer is generated rendered using Mapnik and not Mapserver. The mapnik styles are here: <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/">http://svn.openstreetmap.org/applications/rendering/mapnik/</a></p>
<p>And extended guide on how to setup mapnik for OSM is available on <a href="http://www.switch2osm.org">http://www.switch2osm.org</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Oct '12, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/e79628d44a15e95c607f8c5007d0ccd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Firefishy&#39;s gravatar image" />
<p><span>Firefishy ♦♦</span><br />
<span class="score" title="1296 reputation points"><span>1.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Firefishy has 14 accepted answers">29%</span></p>
</div>
</div>
<div id="comments-container-16843" class="comments-container">
&#10;</div>
<div id="comment-tools-16843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16843-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16749"></span>

<div id="answer-container-16749" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16749-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While it is always possible that there's a bug in the extraction process, the Geofabrik .osm.pbf extracts will normally contain every object that is in OpenStreetMap. Are you sure that your import and rendering process is working correctly? You could verify that by loading a small amount of data from the region in question through the "export" tab on openstreetmap.org. Can you post a screenshot of how the rendering looks on your machine?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '12, 08:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-16749" class="comments-container">
&#10;</div>
<div id="comment-tools-16749" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16749-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16753"></span>

<div id="answer-container-16753" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16753-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Zoom level 10 is quite a way out - depending on its specification, your server may take a while to render those tiles.</p>
<p>Perhaps instead look at the differences between <a href="http://b.tile.openstreetmap.org/18/231975/158248.png">this tile</a> on your server and the OSM server.<br />
</p>
<p>EDIT - extraneous mod_tile-specific stuff removed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '12, 11:54</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Oct '12, 14:42</strong> </span></p>
</div>
</div>
<div id="comments-container-16753" class="comments-container">
<span id="16757"></span>
<div id="comment-16757" class="comment">
<div id="post-16757-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The original post says he's using MapServer, not mod_tile.</p>
</div>
<div id="comment-16757-info" class="comment-info">
<span class="comment-age">(09 Oct '12, 14:06)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="16782"></span>
<div id="comment-16782" class="comment">
<div id="post-16782-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have put screen shots at www.sdc.com.au/osm/osm.png and www.sdc.com.au/osm/mapserver.png.</p>
<p>I have also done an export of a small subset of the osm data and will load it into PostGIS ASAP.</p>
</div>
<div id="comment-16782-info" class="comment-info">
<span class="comment-age">(10 Oct '12, 02:43)</span> <span class="comment-user userinfo">Stephen C Da...</span>
</div>
</div>
</div>
<div id="comment-tools-16753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16753-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16783"></span>

<div id="answer-container-16783" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16783-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have loaded the small set of data exported from osm.org and again the results displayed by MapServer are quite different. (See www.sdc.com.au/osm/osm2.png and www.sdc.com.au/osm/mapserver2.png.)</p>
<p>The obvious conclusion is that there is something wrong with my map file.</p>
<p>I am using a map file generated by osm-mapserver-utils as documented in the MapServer "RenderingOsmData" section.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '12, 03:14</strong></p>
<img src="https://secure.gravatar.com/avatar/91bfd1591ae1c53100f55da985cb3c7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stephen%20C%20Davies&#39;s gravatar image" />
<p><span>Stephen C Da...</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stephen C Davies has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16783" class="comments-container">
&#10;</div>
<div id="comment-tools-16783" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16783-form-container" class="comment-form-container">
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

