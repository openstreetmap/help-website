+++
type = "question"
title = "URL parameters to open uMap with marker on given coordinates"
description = '''With OSM I can use mLat and mLon to create a link that opens a map with a marker on the given coordinates: https://www.openstreetmap.org/?mlat=39.9155&amp;amp;mlon=4.1745 How can I do the same with a map that I created with uMap? I tried several combinations like: http://umap.openstreetmap.fr/en/map/dum...'''
date = "2021-01-18T01:16:00Z"
lastmod = "2021-01-21T14:33:00Z"
weight = 78390
keywords = [ "url", "umap", "coordinates", "marker", "parameters" ]
aliases = [ "/questions/78390" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [URL parameters to open uMap with marker on given coordinates](/questions/78390/url-parameters-to-open-umap-with-marker-on-given-coordinates)

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
<span id="post-78390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78390-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>With OSM I can use mLat and mLon to create a link that opens a map with a marker on the given coordinates:</p>
<p><a href="https://www.openstreetmap.org/?mlat=39.9155&amp;mlon=4.1745">https://www.openstreetmap.org/?mlat=39.9155&amp;mlon=4.1745</a></p>
<p>How can I do the same with a map that I created with uMap?</p>
<p>I tried several combinations like:</p>
<p><a href="http://umap.openstreetmap.fr/en/map/dummy-map_123456/?mlat=39.9155&amp;mlon=4.1745">http://umap.openstreetmap.fr/en/map/dummy-map_123456/?mlat=39.9155&amp;mlon=4.1745</a></p>
<p>but nothing seems to work.</p>
<p>Any suggestions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-parameters" rel="tag" title="see questions tagged &#39;parameters&#39;">parameters</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jan '21, 01:16</strong></p>
<img src="https://secure.gravatar.com/avatar/2a43518266c8fd4b14f73c75624d0850?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Palthe&#39;s gravatar image" />
<p><span>Palthe</span><br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Palthe has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78390" class="comments-container">
&#10;</div>
<div id="comment-tools-78390" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78390-form-container" class="comment-form-container">
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

<span id="78394"></span>

<div id="answer-container-78394" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78394-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think it works that way. What you could do is to create a marker in a data layer and then specify that data layer and/or feature in the URL. Go to the share panel and explore the iframe export options there to see how it is done.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '21, 11:53</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-78394" class="comments-container">
<span id="78397"></span>
<div id="comment-78397" class="comment">
<div id="post-78397-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply. Do you mean I could add my custom uMap as a data-layer to OSM and then use the OSM-URL with mLat and mLon? I will have a look at it.</p>
<p>let me explain the background of my question:</p>
<p>I have on-line photo-albums and I have custom uMaps where you can see the GPS-tracks of the walks I made during which I took the photo's.</p>
<p>With a script I extract the GPS-data from a photo and then construct the URL to a mapping website. This link is presented to the user as a button next to the photo. When the user clicks on the button he gets a map with a marker on the position where the photo was taken.</p>
<p>This works fine with OSM (and OpenTopoMap and Google maps), but not with my custom uMaps. I can create a link to my custom uMap where the map is initially centered on the photo-location, but there is no visual indication. So when you pan or zoom on the map you loose track of the location. Compare these two links:</p>
<p><a href="https://www.openstreetmap.org/?mlat=39.57989&amp;mlon=3.39616#map=17/39.57989/3.39616">https://www.openstreetmap.org/?mlat=39.57989&amp;mlon=3.39616#map=17/39.57989/3.39616</a></p>
<p><a href="http://umap.openstreetmap.fr/en/map/2020-08-mallorca_498917#17/39.57989/3.39616">http://umap.openstreetmap.fr/en/map/2020-08-mallorca_498917#17/39.57989/3.39616</a></p>
</div>
<div id="comment-78397-info" class="comment-info">
<span class="comment-age">(18 Jan '21, 15:05)</span> <span class="comment-user userinfo">Palthe</span>
</div>
</div>
<span id="78402"></span>
<div id="comment-78402" class="comment">
<div id="post-78402-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><em>Do you mean I could add my custom uMap as a data-layer to OSM and then use the OSM-URL with mLat and mLon? I will have a look at it.</em></p>
<p>No, I was suggesting to create a data object in uMap (similar to your GPS tracks) and link to them. You'd have to create a data point for every image location and then point to it with the url parameter <code>feature=</code> and the view area at the end of the url. It could look like this: <a href="http://umap.openstreetmap.fr/de/map/flondor_1?scaleControl=false&amp;miniMap=false&amp;scrollWheelZoom=false&amp;zoomControl=true&amp;allowEdit=false&amp;moreControl=true&amp;searchControl=null&amp;tilelayersControl=null&amp;embedControl=null&amp;datalayersControl=true&amp;onLoadPanel=caption&amp;captionBar=false&amp;feature=t3#10/50.9054/3.4477">umap.openstreetmap.fr/de/map/flondor_1?scaleControl=false&amp;...&amp;feature=t3#10/50.9054/3.4477</a></p>
<p>If you have many photos this would become a bit cumbersome I guess. Maybe it's easier to forget uMap and build your map with Leaflet or OpenLayers.</p>
</div>
<div id="comment-78402-info" class="comment-info">
<span class="comment-age">(18 Jan '21, 16:04)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="78403"></span>
<div id="comment-78403" class="comment">
<div id="post-78403-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK. Maybe I will send a feature request to uMap to add the mLat/mLon option. But I think I can make a script in my photo-album software that exports all GPS-data from the photo's to a GPX-file, which I can import in my uMap. But then my uMap will be cluttered with photo-markers... So this could indeed be a good time to start with Leaflet, which I already downloaded some time ago. Thanks anyway for your help and suggestions!</p>
</div>
<div id="comment-78403-info" class="comment-info">
<span class="comment-age">(18 Jan '21, 16:41)</span> <span class="comment-user userinfo">Palthe</span>
</div>
</div>
</div>
<div id="comment-tools-78394" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78394-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78437"></span>

<div id="answer-container-78437" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78437-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You just need to put online you pictures and create a list (tipically csv) that contains something like:</p>
<p><code>lat,lon,url</code><br />
<code>40.33,13.2,</code><a href="http://myphotobucket.org/pic0010.jpg"><code>http://myphotobucket.org/pic0010.jpg</code></a><br />
<code>40.32,13.3,</code><a href="http://myphotobucket.org/pic0011.jpg"><code>http://myphotobucket.org/pic0011.jpg</code></a></p>
<p>then, when import the above list in umap. To create automatically the list, consider there are some utilities like imagemagik.</p>
<p>If you named at least the columns "lat" and "lon", you should get the map populated with markers; then, if you appropriately compile popup content (see inline help) you can create links to pictures and display at full or lower sizes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '21, 13:26</strong></p>
<img src="https://secure.gravatar.com/avatar/d33efa30f05d8f3604e7210c48b24a8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cascafico&#39;s gravatar image" />
<p><span>Cascafico</span><br />
<span class="score" title="283 reputation points">283</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cascafico has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-78437" class="comments-container">
<span id="78441"></span>
<div id="comment-78441" class="comment">
<div id="post-78441-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for your suggestion, but that is not what I want. See my comment on the first answer ("let me explain the background of my question:"). I need to create a link to my custom uMap that opens the map and shows just one, temporary marker on the coordinates as given in the URL. Your suggestion works the other way around: when I click on a marker on my uMap, it opens a popup with the photo. I already created a script that exports such a file (in GEOJASON format) from my online photo-album. But most of the time I don't want to have permanent markers for all my photos on the map. But I appreciate your answer: I did not know that uMap can also import csv-files. That will make my script much easier.</p>
</div>
<div id="comment-78441-info" class="comment-info">
<span class="comment-age">(21 Jan '21, 14:33)</span> <span class="comment-user userinfo">Palthe</span>
</div>
</div>
</div>
<div id="comment-tools-78437" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78437-form-container" class="comment-form-container">
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

