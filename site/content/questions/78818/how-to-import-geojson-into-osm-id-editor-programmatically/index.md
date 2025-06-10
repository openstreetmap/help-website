+++
type = "question"
title = "How to import GeoJSON  into OSM ID Editor programmatically?"
description = '''Is there an OSM ID API that I can use to push GeoJSON data into an OSM ID editor? I have a leaflet map where users can draw markers. I was thinking of the feature to export drawn markers to the OSM editor. Is it possible?'''
date = "2021-02-12T13:38:00Z"
lastmod = "2021-02-14T19:53:00Z"
weight = 78818
keywords = [ "ideditor", "api" ]
aliases = [ "/questions/78818" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to import GeoJSON into OSM ID Editor programmatically?](/questions/78818/how-to-import-geojson-into-osm-id-editor-programmatically)

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
<span id="post-78818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78818-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there an OSM ID API that I can use to push GeoJSON data into an OSM ID editor?</p>
<p>I have a leaflet map where users can draw markers. I was thinking of the feature to export drawn markers to the OSM editor. Is it possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '21, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/eee470773c9c88880afc69682fb3f481?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sabirmostofa&#39;s gravatar image" />
<p><span>sabirmostofa</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sabirmostofa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78818" class="comments-container">
&#10;</div>
<div id="comment-tools-78818" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78818-form-container" class="comment-form-container">
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

<span id="78850"></span>

<div id="answer-container-78850" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78850-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The OSMF fork of iD supports the display of vector tiles in Mapboxs format, (Rap)iD supports 3rd party data from ESRI (format unknown), it might be possible to shoehorn GeoJSON support on to that, see <a href="https://wiki.openstreetmap.org/wiki/RapiD#ESRI_GIS">https://wiki.openstreetmap.org/wiki/RapiD#ESRI_GIS</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '21, 19:53</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-78850" class="comments-container">
&#10;</div>
<div id="comment-tools-78850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78850-form-container" class="comment-form-container">
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

