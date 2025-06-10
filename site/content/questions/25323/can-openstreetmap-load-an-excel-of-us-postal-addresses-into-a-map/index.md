+++
type = "question"
title = "Can OpenStreetMap load an excel of US postal addresses into a map?"
description = '''We have a use case where customers give us large numbers of postal addresses (Canada, US and Europe), and we need to sit and examine these addresses to ascertain the logistics of covering these areas from a support perspective (emergency support, etc). Sometimes we get these addresses as KML/KMZ fil...'''
date = "2013-08-13T15:47:00Z"
lastmod = "2013-08-13T18:36:00Z"
weight = 25323
keywords = [ "import", "postal", "addresses", "kml", "kmz" ]
aliases = [ "/questions/25323" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Can OpenStreetMap load an excel of US postal addresses into a map?](/questions/25323/can-openstreetmap-load-an-excel-of-us-postal-addresses-into-a-map)

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
<span id="post-25323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25323-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have a use case where customers give us large numbers of postal addresses (Canada, US and Europe), and we need to sit and examine these addresses to ascertain the logistics of covering these areas from a support perspective (emergency support, etc).</p>
<p>Sometimes we get these addresses as KML/KMZ files. About half or more of the time, we get these addresses as Excel files.</p>
<p>We have one guy who loads these into MS Streets and Maps and produces a map with push-pin markers in them. But, we cannot get approval to purchase this software for everyone who would like to generate a map like this.</p>
<p>From reading the forums and spending some time on the software, I don't see a way to bulk import postal addresses to generate this kind of map in OpenStreetMap. This can be done...can't it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-postal" rel="tag" title="see questions tagged &#39;postal&#39;">postal</span> <span class="post-tag tag-link-addresses" rel="tag" title="see questions tagged &#39;addresses&#39;">addresses</span> <span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span> <span class="post-tag tag-link-kmz" rel="tag" title="see questions tagged &#39;kmz&#39;">kmz</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '13, 15:47</strong></p>
<img src="https://secure.gravatar.com/avatar/729f81ca59f8eca9a51bd589c9445e92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alta-Mapper1&#39;s gravatar image" />
<p><span>Alta-Mapper1</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alta-Mapper1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25323" class="comments-container">
&#10;</div>
<div id="comment-tools-25323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25323-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="25328"></span>

<div id="answer-container-25328" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25328-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want a professional solution by a company who seems to be quite up to date in visualizing data and map graphics, have a look at <a href="http://www.mapbox.com">Mapbox</a>.</p>
<p>They are only one among others according to <a href="http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">Commercial_OSM_Software_and_Services</a></p>
<p>Or try frameworks like <a href="http://cartodb.com">CartoDB</a> or <a href="http://kartograph.org">kartograph.org</a></p>
<p>In general, you can display maps as tile graphics via <a href="http://leafletjs.com">leaflet</a> or <a href="http://openlayers.org">openlayers</a> ... I assume (not sure) they have some example code to display markers loaded from a CSV file. But maybe you would have to process too many markers?</p>
<p>Tell us about success or failure.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '13, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Aug '13, 17:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-25328" class="comments-container">
&#10;</div>
<div id="comment-tools-25328" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25328-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25329"></span>

<div id="answer-container-25329" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25329-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is an OpenData plugin for JOSM, the Java based editor. This plugin allows you to import csv files with longitude and latitude and in different projections. (see <a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/OpenData)">http://wiki.openstreetmap.org/wiki/JOSM/Plugins/OpenData)</a></p>
<p>I assume the data does not have the right license to be uploaded to the central OSM database. but from JOSM, you can write a GeoJSON file which can be displayed with Leaflet or OpenLayers (links see stephan75's answer)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '13, 17:19</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Aug '13, 17:20</strong> </span></p>
</div>
</div>
<div id="comments-container-25329" class="comments-container">
&#10;</div>
<div id="comment-tools-25329" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25329-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25334"></span>

<div id="answer-container-25334" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25334-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are many solutions for creating maps with push-pins, but if your Excel files don't include longitude and latitude, then your main problem is <a href="http://en.wikipedia.org/wiki/Geocoding">geocoding</a>.</p>
<p>Try googleing "batch geocoding"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '13, 18:36</strong></p>
<img src="https://secure.gravatar.com/avatar/b9a8b8a3b1418b4b0bb41041555b18a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dymo12&#39;s gravatar image" />
<p><span>Dymo12</span><br />
<span class="score" title="796 reputation points">796</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dymo12 has 2 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-25334" class="comments-container">
&#10;</div>
<div id="comment-tools-25334" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25334-form-container" class="comment-form-container">
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

