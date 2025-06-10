+++
type = "question"
title = "build openPOImap"
description = '''Can I build something similar to the openPOImap for myself? I want to show a map that will only display certain things, similar to how in openPOImap is allowing users to choose one of the amenities. I basically want to show important infrastructure elements on the map such as roads, railways, school...'''
date = "2017-06-19T01:10:00Z"
lastmod = "2017-06-19T07:38:00Z"
weight = 56671
keywords = [ "openpoimap", "osm", "query" ]
aliases = [ "/questions/56671" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [build openPOImap](/questions/56671/build-openpoimap)

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
<span id="post-56671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56671-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can I build something similar to the <a href="http://openpoimap.org/">openPOImap</a> for myself? I want to show a map that will only display certain things, similar to how in openPOImap is allowing users to choose one of the amenities. I basically want to show important infrastructure elements on the map such as roads, railways, schools, hospitals, police, post offices, etc.</p>
<p>I want to be able to query the OSM data similar to how openPOImap is doing from Overpass Turbo. I am certain that I won't need to query too much data at a time so I won't put too much pressure on the server.</p>
<p>It'd be great If anyone could guide me on how where I should begin. I have some experience with Javascript Programming and web development. I already have an app where I have used downloaded data (from OSM in kml or geoJSON format) and tried displaying them on a plain map using Google Maps API. Google maps API is very restrictive so I'd like to build something like the openPOImap, but at the end I'd like to display this data on top of a plain Google Maps. I need to have Google maps because I have another database with spatial points and features that I need to display on the map too.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openpoimap" rel="tag" title="see questions tagged &#39;openpoimap&#39;">openpoimap</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '17, 01:10</strong></p>
<img src="https://secure.gravatar.com/avatar/4d41865031ca35133ece228ee66bcc8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sudbasnet&#39;s gravatar image" />
<p><span>sudbasnet</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sudbasnet has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56671" class="comments-container">
&#10;</div>
<div id="comment-tools-56671" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56671-form-container" class="comment-form-container">
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

<span id="56672"></span>

<div id="answer-container-56672" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56672-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sudbasnet has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While bulding it from scratch is not too difficult, if you simply want the ability to show the results of an OverPass API query on a map, you can do that (for example) with <a href="http://emap.openstreetmap.fr/">umap</a>.</p>
<p>If you want to roll your own, you should have a look at <a href="http://leaflet.org/">leaflet</a> or <a href="http://openlayers.org">OpenLayers</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '17, 07:38</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '17, 07:39</strong> </span></p>
</div>
</div>
<div id="comments-container-56672" class="comments-container">
&#10;</div>
<div id="comment-tools-56672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56672-form-container" class="comment-form-container">
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

