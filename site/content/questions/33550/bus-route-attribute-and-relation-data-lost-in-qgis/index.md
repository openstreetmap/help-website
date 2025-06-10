+++
type = "question"
title = "bus route attribute and relation data lost in QGIS"
description = '''I am currently trying to obtain bus routes in the shapefile data format. I have downloaded raw osm data for Nottingham from the Geofabrik website. I then queried for the bus route relations using osmosis (type=bus, route=bus). I can see the relations for the route data, with the bus number for each ...'''
date = "2014-05-29T09:55:00Z"
lastmod = "2014-06-02T15:18:00Z"
weight = 33550
keywords = [ "qgis", "bus", "busroute", "relations" ]
aliases = [ "/questions/33550" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [bus route attribute and relation data lost in QGIS](/questions/33550/bus-route-attribute-and-relation-data-lost-in-qgis)

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
<span id="post-33550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33550-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently trying to obtain bus routes in the shapefile data format. I have downloaded raw osm data for Nottingham from the Geofabrik website. I then queried for the bus route relations using osmosis (type=bus, route=bus). I can see the relations for the route data, with the bus number for each route in JOSM. However, after exporting to QGIS, all attribute data is lost. I can physically see the polyline segments that make up each route, but I have no information on what bus route number it belongs to. Is there a way to retain the reference tag/relation once its has been opened in GIS?</p>
<p>Thank you. Any help would be greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-busroute" rel="tag" title="see questions tagged &#39;busroute&#39;">busroute</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 May '14, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/33adffb1a0bb2191168299357a9a15ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fm144&#39;s gravatar image" />
<p><span>fm144</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fm144 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 May '14, 14:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-33550" class="comments-container">
<span id="33551"></span>
<div id="comment-33551" class="comment">
<div id="post-33551-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>How are you pulling data into QGIS? Are you aware of route_master relations for some Nottingham bus routes? (e.g., Indigo).</p>
</div>
<div id="comment-33551-info" class="comment-info">
<span class="comment-age">(29 May '14, 10:08)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="33553"></span>
<div id="comment-33553" class="comment">
<div id="post-33553-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have tried different data formats, GeoJSON, GPX, importing the OSM file etc. When I open the attribute table, the fields for each object display NULL.</p>
</div>
<div id="comment-33553-info" class="comment-info">
<span class="comment-age">(29 May '14, 11:03)</span> <span class="comment-user userinfo">fm144</span>
</div>
</div>
<span id="33555"></span>
<div id="comment-33555" class="comment">
<div id="post-33555-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I suspect that this is down to how you are filtering the data with Osmosis not anything to do with QGIS</p>
</div>
<div id="comment-33555-info" class="comment-info">
<span class="comment-age">(29 May '14, 16:41)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="33616"></span>
<div id="comment-33616" class="comment">
<div id="post-33616-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can see the attributes and route information from the osmosis filtered data when the osm file is opened in JOSM. The filtering appears to have worked fine, I just can't get the attributes in the shape file.</p>
</div>
<div id="comment-33616-info" class="comment-info">
<span class="comment-age">(02 Jun '14, 09:52)</span> <span class="comment-user userinfo">fm144</span>
</div>
</div>
<span id="33630"></span>
<div id="comment-33630" class="comment">
<div id="post-33630-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You are still not giving enough info to answer the question. How do you go from an OSM file to JSON or gpx? Which versions of Osmosis, QGIS etc are you using? How many nodes &amp; ways are present in your filtered OSM file? Which platform are you running on (Windows, Max, Linux etc.)? There are just too many potential places where the problem could arise. Lastly I just wouldnt try to get the data this way: I'd push the OSM extract into PostGIS with osm2pgsql &amp; pull that data into QGIS. It's fast &amp; it works.</p>
</div>
<div id="comment-33630-info" class="comment-info">
<span class="comment-age">(02 Jun '14, 15:18)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33550" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33550-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

