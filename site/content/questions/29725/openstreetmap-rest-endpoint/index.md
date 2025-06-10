+++
type = "question"
title = "OpenStreetMap rest endpoint?"
description = '''I have a service that consumes mapping services and renders the basemaps, I can&#x27;t however figure out how to incorporate OpenStreetMap into my service. We have a number endpoints stored in the DB of basemaps that we can flip between on the fly.  Not sure how OSM will work in that framework, it seems ...'''
date = "2014-01-09T15:58:00Z"
lastmod = "2014-01-09T19:28:00Z"
weight = 29725
keywords = [ "basemap", "osm", "rest", "service" ]
aliases = [ "/questions/29725" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OpenStreetMap rest endpoint?](/questions/29725/openstreetmap-rest-endpoint)

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
<span id="post-29725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29725-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a service that consumes mapping services and renders the basemaps, I can't however figure out how to incorporate OpenStreetMap into my service. We have a number endpoints stored in the DB of basemaps that we can flip between on the fly.<br />
</p>
<p>Not sure how OSM will work in that framework, it seems like it's all done in config files or with external javascript libraries</p>
<p>Any help on how to consume and render an OpenStreetMap like I would an ESRI basemap?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-basemap" rel="tag" title="see questions tagged &#39;basemap&#39;">basemap</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-rest" rel="tag" title="see questions tagged &#39;rest&#39;">rest</span> <span class="post-tag tag-link-service" rel="tag" title="see questions tagged &#39;service&#39;">service</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '14, 15:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f211c8cc30b1aae2d45c2ecd88bb8cc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gdrower&#39;s gravatar image" />
<p><span>Gdrower</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gdrower has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jan '14, 22:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-29725" class="comments-container">
<span id="29730"></span>
<div id="comment-29730" class="comment">
<div id="post-29730-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This question is difficult to understand for someone who does not know how you consume ESRI basemaps. Can you give an example of such an "endpoint" that you are looking for?</p>
</div>
<div id="comment-29730-info" class="comment-info">
<span class="comment-age">(09 Jan '14, 16:46)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="29733"></span>
<div id="comment-29733" class="comment">
<div id="post-29733-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://services.arcgisonline.com/ArcGIS/rest/services/ESRI_StreetMap_World_2D/MapServer">http://services.arcgisonline.com/ArcGIS/rest/services/ESRI_StreetMap_World_2D/MapServer</a></p>
<p>Would be an example of a rest endpoint for a basemap service</p>
</div>
<div id="comment-29733-info" class="comment-info">
<span class="comment-age">(09 Jan '14, 19:08)</span> <span class="comment-user userinfo">Gdrower</span>
</div>
</div>
<span id="29734"></span>
<div id="comment-29734" class="comment">
<div id="post-29734-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Same for me, I don't understand the question :( Is it something like this?<br />
<a href="https://gis.stackexchange.com/questions/37507/how-to-serve-openstreetmap-tiles-locally-using-arcgis-server-10">https://gis.stackexchange.com/questions/37507/how-to-serve-openstreetmap-tiles-locally-using-arcgis-server-10</a></p>
</div>
<div id="comment-29734-info" class="comment-info">
<span class="comment-age">(09 Jan '14, 19:28)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-29725" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29725-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

