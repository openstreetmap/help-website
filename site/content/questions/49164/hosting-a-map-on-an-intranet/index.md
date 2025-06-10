+++
type = "question"
title = "Hosting a map on an intranet"
description = '''I am working on a project in which i&#x27;ll need to use openstreetmaps and leafletjs. We&#x27;ll be needing the full map details of a specific country (cities, roads, etc..), along with the a general drawing of rest of the world (country borders, etc..). Since this project should only be accessed within the ...'''
date = "2016-04-11T06:03:00Z"
lastmod = "2016-11-30T04:33:00Z"
weight = 49164
keywords = [ "leaflet", "intranet", "server" ]
aliases = [ "/questions/49164" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Hosting a map on an intranet](/questions/49164/hosting-a-map-on-an-intranet)

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
<span id="post-49164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49164-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am working on a project in which i'll need to use openstreetmaps and leafletjs. We'll be needing the full map details of a specific country (cities, roads, etc..), along with the a general drawing of rest of the world (country borders, etc..). Since this project should only be accessed within the organization, we can't use links to add an osm layer, and so one possible solution is to download the map. I've found a few downloads, yet I'm not sure they're what I am looking for, and since I'm using leaflet, GeoJSON format gave me great results, I couldn't find a GeoJSON download. With all this in mind, is it possible for me to download the full details of a country, along with a general drawing of the rest of the world (and possibly) in GeoJSON?</p>
<p>I am new to maps, so I apologize for anything out of the ordinary in my questions!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-intranet" rel="tag" title="see questions tagged &#39;intranet&#39;">intranet</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '16, 06:03</strong></p>
<img src="https://secure.gravatar.com/avatar/334977ae4f916c5fb022e26234c3fb4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mabuodeh&#39;s gravatar image" />
<p><span>mabuodeh</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mabuodeh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '16, 21:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-49164" class="comments-container">
&#10;</div>
<div id="comment-tools-49164" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49164-form-container" class="comment-form-container">
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

<span id="49169"></span>

<div id="answer-container-49169" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49169-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-49169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you most likely want to do is to set up a tile server along the lines of the instructions in <a href="http://www.switch2osm.org/">http://www.switch2osm.org/</a> - this will let you download raw OSM data and serve it internally in the form of ready-made map tiles. No GeoJSON involved. You will download the country you're interested in and load that into your database, and you will get a couple of shape files from naturalearthdata.com to cover the world at low zoom levels. You will have to modify the default map style ("OSM Carto") slightly, to make use of these shape files - earlier versions of OSM Carto did that by default (use shapefiles for low-zoom country boundaries and place names) but meanwhile OSM Carto relies more on OSM data, and you're not going to load OSM data for the whole world (that would require an unnecessarily big server).</p>
<p>You might also want to look at other map styles like "OSM Bright" that might come with more shape files "built in".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '16, 06:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '16, 06:45</strong> </span></p>
</div>
</div>
<div id="comments-container-49169" class="comments-container">
&#10;</div>
<div id="comment-tools-49169" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49169-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49175"></span>

<div id="answer-container-49175" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49175-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In addition to Frederik's doityourself approach, there are companies who can sell you a set of prerendered tiles to your liking. Depending on how frequently you want to get map updates, this can end up being cheaper than the employee time and server cost to maintain your own deployment.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '16, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-49175" class="comments-container">
&#10;</div>
<div id="comment-tools-49175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49175-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53176"></span>

<div id="answer-container-53176" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53176-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am working on similar requirement, may help someone.</p>
<p><a href="https://github.com/gagan-bansal/osm-for-my-country">https://github.com/gagan-bansal/osm-for-my-country</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '16, 04:33</strong></p>
<img src="https://secure.gravatar.com/avatar/39d75f04e1a21ba653b41ac75ec1b026?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gagan&#39;s gravatar image" />
<p><span>Gagan</span><br />
<span class="score" title="305 reputation points">305</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gagan has 2 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-53176" class="comments-container">
&#10;</div>
<div id="comment-tools-53176" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53176-form-container" class="comment-form-container">
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

