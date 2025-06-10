+++
type = "question"
title = "OSM and 4326 projection"
description = '''In my application I use several layers with 4326 projection. I would like to use as basemap OSM. Do you know any services that implement OSM with 4326 projection ? '''
date = "2013-07-03T14:20:00Z"
lastmod = "2013-07-19T15:49:00Z"
weight = 23934
keywords = [ "wms", "wgs84", "projection" ]
aliases = [ "/questions/23934" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [OSM and 4326 projection](/questions/23934/osm-and-4326-projection)

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
<span id="post-23934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23934-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my application I use several layers with 4326 projection. I would like to use as basemap OSM. Do you know any services that implement OSM with 4326 projection ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wms" rel="tag" title="see questions tagged &#39;wms&#39;">wms</span> <span class="post-tag tag-link-wgs84" rel="tag" title="see questions tagged &#39;wgs84&#39;">wgs84</span> <span class="post-tag tag-link-projection" rel="tag" title="see questions tagged &#39;projection&#39;">projection</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '13, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/278cbf1cc439901141f0de3796f03ebf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexander81&#39;s gravatar image" />
<p><span>alexander81</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexander81 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jul '13, 16:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span></p>
</div>
</div>
<div id="comments-container-23934" class="comments-container">
<span id="24376"></span>
<div id="comment-24376" class="comment">
<div id="post-24376-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i am having a problem with the same projection. which i have drawn in OSm and exported to QGIS and i got the error of +-10m now i am stuck how to correct it... i have converted my map to the same coordinate via Coordinate Reference System (CRS). what to do?</p>
</div>
<div id="comment-24376-info" class="comment-info">
<span class="comment-age">(19 Jul '13, 15:49)</span> <span class="comment-user userinfo">Bhagawat Urb...</span>
</div>
</div>
</div>
<div id="comment-tools-23934" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23934-form-container" class="comment-form-container">
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

<span id="23939"></span>

<div id="answer-container-23939" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23939-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a couple of - mostly commercial - WMS services that support various projections, 4326 among them. See the <a href="http://wiki.openstreetmap.org/wiki/WMS">WMS page on the wiki</a> for details. You can also set up your own WMS or tile server using the 4326 projection (more work), or use a tool like MapProxy to re-project existing tiles into 4326 (sub-standard image quality).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '13, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-23939" class="comments-container">
<span id="24338"></span>
<div id="comment-24338" class="comment">
<div id="post-24338-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Frederik, I imported the pbf file in postgis with a specific bounding box. I used mapnik-stylesheet to create a valid mapnik xml. However the generate_tiles.py make only tiles with sperical mercator projection. Exist any script like generate_tiles.py to generate tiles with 4326 projection?</p>
</div>
<div id="comment-24338-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 10:27)</span> <span class="comment-user userinfo">alexander81</span>
</div>
</div>
<span id="24351"></span>
<div id="comment-24351" class="comment">
<div id="post-24351-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>generate_tiles.py has Sperical Mercator hardcoded, can probably be rewritten to use 4326, though. See <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/generate_tiles.py">http://svn.openstreetmap.org/applications/rendering/mapnik/generate_tiles.py</a> , near the top there's a "GoogleProjection" class. This could probably be rewritten using pyproj to support other EPSGs.</p>
</div>
<div id="comment-24351-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 13:27)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-23939" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23939-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23951"></span>

<div id="answer-container-23951" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23951-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have very limited experience with GIS in general (a very green newbie, so please excuse me if I'm barking up the wrong tree). I have learned that <a href="http://www.qgis.org/">Qantum GIS</a> can reproject layers on the fly. It also has an OSM plugin that can either use the raw data or pull in rendered data. I have been able to use Bing imagery, OSM data and elevation data together using 4326 projection. Not sure if this will meet your needs though, but you may want to look into it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '13, 06:05</strong></p>
<img src="https://secure.gravatar.com/avatar/e466cf295ae880686a4b809362f931b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rovingmedic&#39;s gravatar image" />
<p><span>rovingmedic</span><br />
<span class="score" title="1060 reputation points"><span>1.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rovingmedic has one accepted answer">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '13, 06:09</strong> </span></p>
</div>
</div>
<div id="comments-container-23951" class="comments-container">
&#10;</div>
<div id="comment-tools-23951" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23951-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24353"></span>

<div id="answer-container-24353" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24353-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you using OpenLayers? OL should theoretically be able to reproject 4326-based layers to 900913/3857, see for example <a href="http://www.peterrobins.co.uk/it/olchangingprojection.html">http://www.peterrobins.co.uk/it/olchangingprojection.html</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '13, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-24353" class="comments-container">
&#10;</div>
<div id="comment-tools-24353" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24353-form-container" class="comment-form-container">
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

