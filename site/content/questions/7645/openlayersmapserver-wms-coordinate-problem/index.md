+++
type = "question"
title = "OpenLayers+MapServer (WMS) - coordinate-problem"
description = '''Hello community, I got a bad problem with coordinates. I tried to setup a raw MapServer WMS with OpenLayers frontend. My aim is to show measurement data from a database as a single tile with OpenLayers. Some facts: OpenLayers:  - Background-Map: OSM (new OpenLayers.Layer.OSM();)  - requesting my Map...'''
date = "2011-09-05T16:29:00Z"
lastmod = "2011-09-07T11:59:00Z"
weight = 7645
keywords = [ "wms", "mapserver", "openlayers", "coordinates" ]
aliases = [ "/questions/7645" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OpenLayers+MapServer (WMS) - coordinate-problem](/questions/7645/openlayersmapserver-wms-coordinate-problem)

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
<span id="post-7645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7645-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello community,</p>
<p>I got a bad problem with coordinates. I tried to setup a raw MapServer WMS with OpenLayers frontend. My aim is to show measurement data from a database as a single tile with OpenLayers.</p>
<p>Some facts: OpenLayers: - Background-Map: OSM (new OpenLayers.Layer.OSM();) - requesting my MapServer WMS (new OpenLayers.Layer.WMS) with Single-Tile-Mode</p>
<p>MapServer: - Raw WMS - means I'm fetching the querystring by myself and trying to apply it to the map - No mapfile used - all settings in map-generating file itself</p>
<p>My problem is, that OpenLayers creates a querystring like that...</p>
<p>LAYERS-&gt;basic<br />
FORMAT-&gt;image/png<br />
PROJECTION-&gt;EPSG:4326<br />
UNITS-&gt;m<br />
SERVICE-&gt;WMS<br />
VERSION-&gt;1.1.1<br />
REQUEST-&gt;GetMap<br />
STYLES-&gt;<br />
EXCEPTIONS-&gt;application/vnd.ogc.se_inimage<br />
BBOX-&gt;-11231962.682325,-2416633.0858313,19763558.029875,12161436.946106<br />
WIDTH-&gt;1584<br />
HEIGHT-&gt;745<br />
</p>
<p>...and mapserver has a method to set the bounding box from OpenLayers...</p>
<p>$Map-&gt;setExtent(lat1,lon1,lat2,lon2);</p>
<p>but the coordinates have a different format. OpenLayers provides coordinates in UTM(?) while setExtent expects decimal values as I often saw them in example scripts.</p>
<p>My question is: How can I create a map which fits perfectly with the OSM map, but without using a mapfile and tilemode since I need singletile-mode? I couldn't figure out to set the bounding box correctly or even convert the coordinates. Additionally I suppose that something is wrong with my projections.</p>
<p>I hope someone can help me.:)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wms" rel="tag" title="see questions tagged &#39;wms&#39;">wms</span> <span class="post-tag tag-link-mapserver" rel="tag" title="see questions tagged &#39;mapserver&#39;">mapserver</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '11, 16:29</strong></p>
<img src="https://secure.gravatar.com/avatar/2565cdf414e726ce463e1dc87bd7d620?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sannifrosch&#39;s gravatar image" />
<p><span>Sannifrosch</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sannifrosch has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-7645" class="comments-container">
<span id="7647"></span>
<div id="comment-7647" class="comment">
<div id="post-7647-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Using leaflet causes the same problem. Coordinates look like bbox-&gt;1878516.4071364915,5635549.221409475,2504688.5428486555,6261721.35712164 while setExtent() needs decimal values (lat/lon)</p>
</div>
<div id="comment-7647-info" class="comment-info">
<span class="comment-age">(05 Sep '11, 18:29)</span> <span class="comment-user userinfo">Sannifrosch</span>
</div>
</div>
</div>
<div id="comment-tools-7645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7645-form-container" class="comment-form-container">
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

<span id="7712"></span>

<div id="answer-container-7712" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7712-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your coordinates seem to be in spherical mercator (900913, EPSG 3857) but you need them in lat/lon. You have to transform them for the querystring. Openlayers offers functions for this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '11, 11:59</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span> </br></br></p>
</div>
</div>
<div id="comments-container-7712" class="comments-container">
&#10;</div>
<div id="comment-tools-7712" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7712-form-container" class="comment-form-container">
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

