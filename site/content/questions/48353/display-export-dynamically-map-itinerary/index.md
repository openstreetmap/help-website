+++
type = "question"
title = "[closed] Display &amp; export dynamically map itinerary"
description = '''Hello I want to generate instantly an image showing a route between two points that I&#x27;ve chosen (this image will then be inserted in a video). On my computer, I&#x27;ve been using Mapbox JS API to display a set of directions, in particular their Directions API which is neat! But now I need a route from a...'''
date = "2016-02-25T12:28:00Z"
lastmod = "2016-02-26T10:24:00Z"
weight = 48353
keywords = [ "api", "maperitive", "google_maps", "mapbox" ]
aliases = [ "/questions/48353" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Display & export dynamically map itinerary](/questions/48353/display-export-dynamically-map-itinerary)

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
<span id="post-48353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48353-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello I want to generate instantly an image showing a route between two points that I've chosen (this image will then be inserted in a video).</p>
<p>On my computer, I've been using Mapbox JS API to display a set of directions, in particular their Directions API which is neat! But now I need a route from a user geolocation retrieved on the fly. With Mapbox URL API, this URL will show the two points, but no itinerary.</p>
<p><a href="https://api.mapbox.com/v4/mapbox.dark/pin-l-star+482(%s,%s),pin-l-hairdresser+482(%s,%s)/%s,%s,17/1280x800.png?access_token=%s">https://api.mapbox.com/v4/mapbox.dark/pin-l-star+482(%s,%s),pin-l-hairdresser+482(%s,%s)/%s,%s,17/1280x800.png?access_token=%s</a></p>
<p>The Direction API via URL sends a JSON, but I need the itinerary to be shown on the map.</p>
<p><a href="https://api.mapbox.com/v4/directions/mapbox.walking/2.345732,48.893782;2.353325,48.878329.json?access_token=...">https://api.mapbox.com/v4/directions/mapbox.walking/2.345732,48.893782;2.353325,48.878329.json?access_token=..."</a> I've been looking to OpenStreetMap, Mapquest, ... Maperitive is interesting: it's a Desktop app with Python API; you can import a GPX itinerary and then saves the image.</p>
<p>I wonder if anyone has another option to say instantly "export an image with itinerary from Point A to Point B". Can't use Google Maps as they don't allow commercial use of the maps from their API.</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span> <span class="post-tag tag-link-google_maps" rel="tag" title="see questions tagged &#39;google_maps&#39;">google_maps</span> <span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '16, 12:28</strong></p>
<img src="https://secure.gravatar.com/avatar/8d3d52778adbc93a9443060f8ca88afc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Charlie18&#39;s gravatar image" />
<p><span>Charlie18</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Charlie18 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>26 Feb '16, 16:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-48353" class="comments-container">
<span id="48354"></span>
<div id="comment-48354" class="comment">
<div id="post-48354-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Related question: <a href="https://help.openstreetmap.org/questions/48283/create-image-of-map-and-route-on-a-mac-view-osm-data-and-import-kml-file.">https://help.openstreetmap.org/questions/48283/create-image-of-map-and-route-on-a-mac-view-osm-data-and-import-kml-file.</a> Maybe it already contains an useful answer for you.</p>
</div>
<div id="comment-48354-info" class="comment-info">
<span class="comment-age">(25 Feb '16, 12:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="48356"></span>
<div id="comment-48356" class="comment">
<div id="post-48356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai">@scai</a>: thanks for your answer!</p>
</div>
<div id="comment-48356-info" class="comment-info">
<span class="comment-age">(25 Feb '16, 13:46)</span> <span class="comment-user userinfo">Charlie18</span>
</div>
</div>
<span id="48365"></span>
<div id="comment-48365" class="comment">
<div id="post-48365-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/12028/charlie18">@Charlie18</a>: do you still have questions or is everything fine now?</p>
</div>
<div id="comment-48365-info" class="comment-info">
<span class="comment-age">(25 Feb '16, 19:58)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="48367"></span>
<div id="comment-48367" class="comment">
<div id="post-48367-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> I'd say it's ok for now. Thanks!</p>
</div>
<div id="comment-48367-info" class="comment-info">
<span class="comment-age">(26 Feb '16, 10:24)</span> <span class="comment-user userinfo">Charlie18</span>
</div>
</div>
</div>
<div id="comment-tools-48353" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48353-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "See the linked "related question" above - answers there." by aseerel4c26 26 Feb '16, 16:44

</div>

</div>

</div>

