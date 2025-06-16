+++
type = "question"
title = "Converting for WMS"
description = '''What format, or what process, do I need to do with the planet.osm file in order to serve it out with an OGC compliant WMS server? I&#x27;m reading a lot about converting ot to a database, but is that format OGC compliant or is that for some other type of serving? Thanks! Jon'''
date = "2013-06-27T02:07:00Z"
lastmod = "2013-06-27T15:08:00Z"
weight = 23740
keywords = [ "wms", "ogc" ]
aliases = [ "/questions/23740" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Converting for WMS](/questions/23740/converting-for-wms)

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
<span id="post-23740-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23740-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23740-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What format, or what process, do I need to do with the planet.osm file in order to serve it out with an OGC compliant WMS server? I'm reading a lot about converting ot to a database, but is that format OGC compliant or is that for some other type of serving? Thanks!</p>
<p>Jon</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wms" rel="tag" title="see questions tagged &#39;wms&#39;">wms</span> <span class="post-tag tag-link-ogc" rel="tag" title="see questions tagged &#39;ogc&#39;">ogc</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '13, 02:07</strong></p>
<img src="https://secure.gravatar.com/avatar/43a9c8a6e33c0ac041744f174523d59d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jjmil03&#39;s gravatar image" />
<p><span>jjmil03</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jjmil03 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23740" class="comments-container">
&#10;</div>
<div id="comment-tools-23740" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23740-form-container" class="comment-form-container">
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

<span id="23743"></span>

<div id="answer-container-23743" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23743-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to import your data into a database, most likely with osm2pgsql or imposm, and then set up a WMS with a suitable map style definition. The map style definition is key here, and it must match both your WMS software and the import program you're using. The map style of course controls how your map looks like and it is very likely that it it will <strong>not</strong> look like the map on www.openstreetmap.org.</p>
<p>Possible configurations include:</p>
<ul>
<li>UMN Mapserver as the WMS, imposm for importing, styles from <a href="https://github.com/mapserver/basemaps">https://github.com/mapserver/basemaps</a></li>
<li>GeoServer as the WMS, read <a href="http://osgeo-org.1560.x6.nabble.com/OSM-style-SLD-files-for-GeoServer-td5015615.html">http://osgeo-org.1560.x6.nabble.com/OSM-style-SLD-files-for-GeoServer-td5015615.html</a></li>
<li>Mapnik OGC Server (<a href="https://github.com/mapnik/OGCServer),">https://github.com/mapnik/OGCServer),</a> then use standard OSM Mapnik styles</li>
<li>mod_mapnik_wms (<a href="https://wiki.openstreetmap.org/wiki/Mod_mapnik_wms),">https://wiki.openstreetmap.org/wiki/Mod_mapnik_wms),</a> then use standard OSM Mapnik styles</li>
</ul>
<p>The Mapnik-based solutions will allow you to come closest to the "standard OSM" look but the UMN Mapserver solution is the most widely used for WMS.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '13, 07:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-23743" class="comments-container">
<span id="23748"></span>
<div id="comment-23748" class="comment">
<div id="post-23748-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So you need a three-tier architecture:</p>
<ul>
<li>OSM data in a database, which has to be synchronized to the main OSM Db (if you want current OSM data and not a static "OSM as of 2013-06-27" snapshot)</li>
<li>a rendering engine that generates images from the OSM data in the Db</li>
<li>a WMS server software that stitches the images together and serves them according to OGC request/response rules</li>
</ul>
</div>
<div id="comment-23748-info" class="comment-info">
<span class="comment-age">(27 Jun '13, 15:08)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-23743" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23743-form-container" class="comment-form-container">
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

