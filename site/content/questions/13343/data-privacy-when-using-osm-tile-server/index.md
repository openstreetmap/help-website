+++
type = "question"
title = "Data privacy when using OSM tile server"
description = '''My question is quite simple : when using OpenStreetMap tile server to display a map on a website, are informations like makers position and informations sent to OSM servers ? Or does OSM server just get informations about the area to render, and markers are added on &#x27;client&#x27; side by the browser (so ...'''
date = "2012-06-08T10:34:00Z"
lastmod = "2012-06-12T08:43:00Z"
weight = 13343
keywords = [ "marker", "critical", "data", "privacy" ]
aliases = [ "/questions/13343" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Data privacy when using OSM tile server](/questions/13343/data-privacy-when-using-osm-tile-server)

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
<span id="post-13343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13343-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My question is quite simple : when using OpenStreetMap tile server to display a map on a website, are informations like makers position and informations sent to OSM servers ? Or does OSM server just get informations about the area to render, and markers are added on 'client' side by the browser (so critical data are just shared by the server hosting the website and user's browser) ?</p>
<p>Thanks !</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-critical" rel="tag" title="see questions tagged &#39;critical&#39;">critical</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-privacy" rel="tag" title="see questions tagged &#39;privacy&#39;">privacy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '12, 10:34</strong></p>
<img src="https://secure.gravatar.com/avatar/da7ff7fedcd5fd0591fc8f6b3249ae66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Camille&#39;s gravatar image" />
<p><span>Camille</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Camille has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13343" class="comments-container">
&#10;</div>
<div id="comment-tools-13343" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13343-form-container" class="comment-form-container">
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

<span id="13344"></span>

<div id="answer-container-13344" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13344-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-13344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Camille has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are at all concerned about information being passed back to the OpenStreetMap servers, the answer is simple: <a href="http://switch2osm.org/serving-tiles/">use your own tile server</a>. This ensures that there is no chance anyone connected with OSM will be able to find out where you are showing maps of.</p>
<p>The technical answer is that if a map display library like OpenLayers or Leaflet shows a marker over a map, the location of the marker isn't explicitly passed back to the tile server, but some information does leak back should someone who has access to the server logs be trying to find this out. The list of tiles requested by each client on your site would be available, giving a very good idea of which area they were looking at and at which zoom level. Needless to say, none of the OSM server admins are even remotely interested in where your markers are.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '12, 10:49</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-13344" class="comments-container">
<span id="13346"></span>
<div id="comment-13346" class="comment">
<div id="post-13346-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Perfect, thx ! That's what I just figured out having a look at network traffic between my browser and OSM server : the only requests are thing like <a href="http://vmap0.tiles.osgeo.org/wms/vmap0?LAYERS=basic&amp;SERVICE=WMS&amp;VERSION=1.1.1&amp;REQUEST=GetMap&amp;STYLES=&amp;FORMAT=image%2Fjpeg&amp;SRS=EPSG%3A4326&amp;BBOX=0,0,90,90&amp;WIDTH=256&amp;HEIGHT=256,">http://vmap0.tiles.osgeo.org/wms/vmap0?LAYERS=basic&amp;SERVICE=WMS&amp;VERSION=1.1.1&amp;REQUEST=GetMap&amp;STYLES=&amp;FORMAT=image%2Fjpeg&amp;SRS=EPSG%3A4326&amp;BBOX=0,0,90,90&amp;WIDTH=256&amp;HEIGHT=256,</a> which are parts of map, sliced from parameters sent :</p>
<p>LAYERS:basic</p>
<p>SERVICE:WMS</p>
<p>VERSION:1.1.1</p>
<p>REQUEST:GetMap</p>
<p>STYLES:</p>
<p>FORMAT:image/jpeg</p>
<p>SRS:EPSG:4326</p>
<p>BBOX:0,0,90,90</p>
<p>WIDTH:256</p>
<p>HEIGHT:256</p>
<p>so nothing about my markers ! :)</p>
</div>
<div id="comment-13346-info" class="comment-info">
<span class="comment-age">(08 Jun '12, 11:21)</span> <span class="comment-user userinfo">Camille</span>
</div>
</div>
<span id="13347"></span>
<div id="comment-13347" class="comment">
<div id="post-13347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess that OSM server admins are not interested in my markers, and have certainly more important things to deal with, but my customer had just to be reassured, because geolocation can be quite a confidential issue... ;)</p>
<p>Thx again !</p>
<p>Best regards</p>
</div>
<div id="comment-13347-info" class="comment-info">
<span class="comment-age">(08 Jun '12, 11:27)</span> <span class="comment-user userinfo">Camille</span>
</div>
</div>
<span id="13448"></span>
<div id="comment-13448" class="comment">
<div id="post-13448-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>vmap0.tiles.osgeo.org is not an OpenStreetMap based service.</p>
</div>
<div id="comment-13448-info" class="comment-info">
<span class="comment-age">(12 Jun '12, 08:43)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-13344" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13344-form-container" class="comment-form-container">
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

