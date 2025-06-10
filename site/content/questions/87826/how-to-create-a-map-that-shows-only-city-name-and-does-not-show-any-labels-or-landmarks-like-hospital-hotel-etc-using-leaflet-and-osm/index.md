+++
type = "question"
title = "[closed] How to create a map that shows only city name and does not show any labels or landmarks like hospital, hotel, etc using leaflet and OSM?"
description = '''I&#x27;m new to OSM and want to create a leaflet map using OSM that shows only city names on the map and does not show any label or landmark like hotel, hospitals, etc. Kindly help me create this map. Here&#x27;s the sample code: // Create a Leaflet map centered at a specific location and zoom level  const ma...'''
date = "2023-09-09T09:20:00Z"
lastmod = "2023-09-09T10:04:00Z"
weight = 87826
keywords = [ "leaflet", "openstreetmap", "openstreetmaps", "osm", "#openstreetmap" ]
aliases = [ "/questions/87826" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to create a map that shows only city name and does not show any labels or landmarks like hospital, hotel, etc using leaflet and OSM?](/questions/87826/how-to-create-a-map-that-shows-only-city-name-and-does-not-show-any-labels-or-landmarks-like-hospital-hotel-etc-using-leaflet-and-osm)

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
<span id="post-87826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87826-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OSM and want to create a leaflet map using OSM that shows only city names on the map and does not show any label or landmark like hotel, hospitals, etc. Kindly help me create this map.</p>
<p>Here's the sample code:</p>
<pre><code>// Create a Leaflet map centered at a specific location and zoom level
  const map = L.map(&quot;leaflet-map-popup&quot;).setView([20.5937, 78.9629], 5);
&#10;  // Customize the map&#39;s appearance with a custom tile layer (HOT style)
  L.tileLayer(&quot;https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png&quot;, {
    maxZoom: 16,
    tileSize: 512,
    zoomOffset: -1,
  }).addTo(map);</code></pre>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-openstreetmaps" rel="tag" title="see questions tagged &#39;openstreetmaps&#39;">openstreetmaps</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-#openstreetmap" rel="tag" title="see questions tagged &#39;#openstreetmap&#39;">#openstreetmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Sep '23, 09:20</strong></p>
<img src="https://secure.gravatar.com/avatar/1cb590df556bee9f891ddcfd2ecd097a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aditya_07&#39;s gravatar image" />
<p><span>Aditya_07</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aditya_07 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>13 Sep '23, 09:12</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-87826" class="comments-container">
<span id="87827"></span>
<div id="comment-87827" class="comment">
<div id="post-87827-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>See also <a href="https://community.openstreetmap.org/t/how-to-create-a-map-that-shows-only-city-names-and-does-not-show-any-label-or-landmarks-like-hotel-hospital-etc-using-osm-and-leaflet/103639">https://community.openstreetmap.org/t/how-to-create-a-map-that-shows-only-city-names-and-does-not-show-any-label-or-landmarks-like-hotel-hospital-etc-using-osm-and-leaflet/103639</a></p>
</div>
<div id="comment-87827-info" class="comment-info">
<span class="comment-age">(09 Sep '23, 10:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-87826" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87826-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by SimonPoole 13 Sep '23, 09:12

</div>

</div>

</div>

