+++
type = "question"
title = "Geo-location on HTML page"
description = '''Hi there I&#x27;m looking for an easy solution how to add to my OpenStreetMap the icon to get my current position and retrive latitude and longitude. Thanks in advance for your help. Please keep ion mind when relying that I&#x27;m a nook. best regards Ossy'''
date = "2020-10-13T10:28:00Z"
lastmod = "2020-10-13T10:49:00Z"
weight = 77066
keywords = [ "geolocation", "openlayers" ]
aliases = [ "/questions/77066" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Geo-location on HTML page](/questions/77066/geo-location-on-html-page)

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
<span id="post-77066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77066-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there</p>
<p>I'm looking for an easy solution how to add to my OpenStreetMap the icon to get my current position and retrive latitude and longitude.</p>
<p>Thanks in advance for your help. Please keep ion mind when relying that I'm a nook.</p>
<p>best regards</p>
<p>Ossy</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geolocation" rel="tag" title="see questions tagged &#39;geolocation&#39;">geolocation</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Oct '20, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/702849b0e8a60c349d49cda5361c4285?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ossy01&#39;s gravatar image" />
<p><span>Ossy01</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ossy01 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Oct '20, 10:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-77066" class="comments-container">
<span id="77067"></span>
<div id="comment-77067" class="comment">
<div id="post-77067-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain in a bit more detail what you mean by "my OpenStreetMap"? If a generic website, try one of <a href="https://duckduckgo.com/?t=ffsb&amp;q=html+geolocation&amp;ia=web">https://duckduckgo.com/?t=ffsb&amp;q=html+geolocation&amp;ia=web</a> .</p>
</div>
<div id="comment-77067-info" class="comment-info">
<span class="comment-age">(13 Oct '20, 10:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="77068"></span>
<div id="comment-77068" class="comment">
<div id="post-77068-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry about not being clear. Here is my Page. &lt;html&gt;&lt;body&gt;</p>
<div>
&#10;</div>
<p>&lt;script src="http://www.openlayers.org/api/OpenLayers.js"&gt;&lt;/script&gt; &lt;script&gt; var mylat = 46.9 var mylon = 6.6833 map = new OpenLayers.Map("mapdiv"); map.addLayer(new OpenLayers.Layer.OSM());</p>
<pre><code>var lonLat = new OpenLayers.LonLat( mylon,mylat )
      .transform(
        new OpenLayers.Projection(&quot;EPSG:4326&quot;), // transform from WGS 1984
        map.getProjectionObject() // to Spherical Mercator Projection
      );
var zoom=17;
var markers = new OpenLayers.Layer.Markers( &quot;Markers&quot; );
map.addLayer(markers);
markers.addMarker(new OpenLayers.Marker(lonLat));
map.setCenter (lonLat, zoom);</code></pre>
<p>&lt;/script&gt; &lt;/body&gt;&lt;/html&gt;</p>
<p>I would lite to add under the zoom the icon for geo-location, center the map to this location and retrieve the information in my javascript. I have seen some script, but I didn't work for me. Perhars not used corretly.</p>
<p>++ Ossy</p>
</div>
<div id="comment-77068-info" class="comment-info">
<span class="comment-age">(13 Oct '20, 10:49)</span> <span class="comment-user userinfo">Ossy01</span>
</div>
</div>
</div>
<div id="comment-tools-77066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77066-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

