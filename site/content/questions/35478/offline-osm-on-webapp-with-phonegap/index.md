+++
type = "question"
title = "Offline OSM on Webapp with Phonegap"
description = '''I want to integrate the OpenStreetMap to my WebApp. Now I&#x27;ve download a shp.zip for a region. After extract the Zip-File i have 71 .map files. How can I use the Files for showing the Map Offline?'''
date = "2014-08-03T19:40:00Z"
lastmod = "2017-01-03T11:22:00Z"
weight = 35478
keywords = [ "phonegap", "webapp", "offline", "development", "usage" ]
aliases = [ "/questions/35478" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Offline OSM on Webapp with Phonegap](/questions/35478/offline-osm-on-webapp-with-phonegap)

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
<span id="post-35478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35478-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to integrate the OpenStreetMap to my WebApp. Now I've download a shp.zip for a region. After extract the Zip-File i have 71 .map files. How can I use the Files for showing the Map Offline?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-phonegap" rel="tag" title="see questions tagged &#39;phonegap&#39;">phonegap</span> <span class="post-tag tag-link-webapp" rel="tag" title="see questions tagged &#39;webapp&#39;">webapp</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '14, 19:40</strong></p>
<img src="https://secure.gravatar.com/avatar/6c5b7fd327a74eda5ae74bf467d04fc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vital1985&#39;s gravatar image" />
<p><span>vital1985</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vital1985 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Aug '14, 23:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-35478" class="comments-container">
<span id="35482"></span>
<div id="comment-35482" class="comment">
<div id="post-35482-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think some more details and description would help. What is "integrate the OpenStreetMap to my WebApp" for you? Why did you think that shp.zip is the right download?</p>
</div>
<div id="comment-35482-info" class="comment-info">
<span class="comment-age">(03 Aug '14, 23:09)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="35512"></span>
<div id="comment-35512" class="comment">
<div id="post-35512-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I simply want to display a OSM map offline using JavaScript. I don't know which download is the right but in the shp.zip file are *.map files which i can open with the JSOM Editor and see streets with some data.</p>
</div>
<div id="comment-35512-info" class="comment-info">
<span class="comment-age">(04 Aug '14, 15:57)</span> <span class="comment-user userinfo">vital1985</span>
</div>
</div>
<span id="35515"></span>
<div id="comment-35515" class="comment">
<div id="post-35515-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What sort of map do you want to display? One that looks like the maps that you see on the OpenStreetMap website (which are made up of <a href="http://wiki.osm.org/wiki/Tiles">map tiles</a>), or a vector-drawn map (like you see in JOSM, but presumably with a different style)? If you do want map tiles, do you want ones that look like an existing OSM style, or different?</p>
<p>How much of the world do you want to display and at what level of detail? How much size are you willing to allocate to map data in your application? How much time do you have to spend writing it? Are you targeting just one platform supported by PhoneGap or several?</p>
<p>At one end of the range of possible answers would be a <a href="https://github.com/SomeoneElseOSM/OSMembedded">quick-and-dirty</a> use of something like <a href="http://leafletjs.com/">Leaflet</a> to display embedded map tiles - simple to do, but impractical for all but very small areas. At the other end would be writing a full-blown renderer in JavaScript. In between are lots of other options.</p>
</div>
<div id="comment-35515-info" class="comment-info">
<span class="comment-age">(04 Aug '14, 19:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="35530"></span>
<div id="comment-35530" class="comment">
<div id="post-35530-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To display a Map looks like OpenStreetMap will be enough. I don't know what is better to use on a mobile device (vector or tiles).</p>
<p>I only want to display Germany on the map. The decision for using PhoneGap is because i want to support ios and android devices.</p>
<p>An other question: is it possible to extract the maxspeed-values from the map and show this on map?</p>
</div>
<div id="comment-35530-info" class="comment-info">
<span class="comment-age">(05 Aug '14, 15:41)</span> <span class="comment-user userinfo">vital1985</span>
</div>
</div>
</div>
<div id="comment-tools-35478" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35478-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="53821"></span>

<div id="answer-container-53821" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53821-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try <strong>Offy Data DLR</strong> for Windows</p>
<p><a href="https://github.com/OffyGIS/Offy-Data-DLR/releases/tag/v1.0">Latest release</a></p>
<p><a href="https://github.com/OffyGIS/Offy-Data-DLR#offy-data-dlr">Getting started</a> (how to download data &amp; how to use it)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '17, 10:50</strong></p>
<img src="https://secure.gravatar.com/avatar/1638dfb4bbd6c90cefa57e6d847354c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="offygis&#39;s gravatar image" />
<p><span>offygis</span><br />
<span class="score" title="25 reputation points">25</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="offygis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53821" class="comments-container">
<span id="53822"></span>
<div id="comment-53822" class="comment">
<div id="post-53822-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That just looks like a tile scraper - how is that related to Phonegap / Cordova?</p>
<p>Note that tile usage must abide by <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">https://wiki.openstreetmap.org/wiki/Tile_usage_policy</a> .</p>
</div>
<div id="comment-53822-info" class="comment-info">
<span class="comment-age">(03 Jan '17, 11:10)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53824"></span>
<div id="comment-53824" class="comment">
<div id="post-53824-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>:) yes I know. Take a look at the last section of the readme page : <a href="https://github.com/OffyGIS/Offy-Data-DLR#important">https://github.com/OffyGIS/Offy-Data-DLR#important</a> . In addition, there is a tuto explaining how to use downloaded tiles within different GIS clients (but respecting the server Usage policy).</p>
</div>
<div id="comment-53824-info" class="comment-info">
<span class="comment-age">(03 Jan '17, 11:22)</span> <span class="comment-user userinfo">offygis</span>
</div>
</div>
</div>
<div id="comment-tools-53821" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53821-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35941"></span>

<div id="answer-container-35941" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35941-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-35941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello, Its is something new for me but thanks for posting this question by this i am able to know about something new which i dont know .</p>
<p><a href="http://www.mobilepundits.com/PhoneGap_Development.html">PhoneGap Development</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '14, 09:08</strong></p>
<img src="https://secure.gravatar.com/avatar/e697879fe1f5c8a5f7ed73cb636dee79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mobilepundits&#39;s gravatar image" />
<p><span>Mobilepundits</span><br />
<span class="score" title="-1 reputation points">-1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mobilepundits has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35941" class="comments-container">
<span id="35942"></span>
<div id="comment-35942" class="comment">
<div id="post-35942-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Link is on-topic, but almost entirely content-free.</p>
</div>
<div id="comment-35942-info" class="comment-info">
<span class="comment-age">(18 Aug '14, 09:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="35943"></span>
<div id="comment-35943" class="comment">
<div id="post-35943-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Smells like spam :\</p>
</div>
<div id="comment-35943-info" class="comment-info">
<span class="comment-age">(18 Aug '14, 09:16)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-35941" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35941-form-container" class="comment-form-container">
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

