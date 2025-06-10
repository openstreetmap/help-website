+++
type = "question"
title = "show user location by lat and lon"
description = '''hi, i show user current location in map.i need after show location by receive lat and lon via user show location on map. thanks for help.  &amp;lt;!DOCTYPE html&amp;gt; &amp;lt;html&amp;gt; &amp;lt;head&amp;gt;   &amp;lt;title&amp;gt;view&amp;lt;/title&amp;gt;   &amp;lt;meta charset=&quot;utf-8&quot; /&amp;gt;  &amp;lt;meta name=&quot;viewport&quot; content=&quot;width=devic...'''
date = "2019-11-24T09:55:00Z"
lastmod = "2019-11-24T10:40:00Z"
weight = 71791
keywords = [ "location" ]
aliases = [ "/questions/71791" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [show user location by lat and lon](/questions/71791/show-user-location-by-lat-and-lon)

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
<span id="post-71791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71791-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi, i show user current location in map.i need after show location by receive lat and lon via user show location on map. thanks for help.</p>
<pre><code>    &lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&#10;    &lt;title&gt;view&lt;/title&gt;
&#10;    &lt;meta charset=&quot;utf-8&quot; /&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
&#10;
&#10;    &lt;link rel=&quot;stylesheet&quot; href=&quot;leaflet/leaflet.css&quot; /&gt;
    &lt;script src=&quot;leaflet/leaflet.js&quot;&gt;&lt;/script&gt;
&#10;
    &lt;style&gt;
        html, body {
            height: 100%;
            margin: 0;
        }
        #map {
            width: 600px;
            height: 400px;
        }       
        div#lat-lon {
            padding-top: 10px;
        }
    &lt;/style&gt;
&#10;    &lt;style&gt;body { padding: 0; margin: 0; } &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div id=&quot;main-content&quot;&gt;
    &lt;div id=&#39;map&#39;&gt;&lt;/div&gt;
    &lt;div id=&quot;lat-lon&quot;&gt;
        &lt;input type=&quot;text&quot; id=&quot;frmLat&quot;&gt;
        &lt;input type=&quot;text&quot; id=&quot;frmLon&quot;&gt;
        &lt;button onclick=&quot;getLocation()&quot;&gt;show lat and lon&lt;/button&gt;
        &lt;button onclick=&quot;setLocation()&quot;&gt;set location&lt;/button&gt;
    &lt;/div&gt;
&lt;/div&gt;
&#10;
&lt;script&gt;
    var map = L.map(&#39;map&#39;).fitWorld();
&#10;    L.tileLayer(&#39;https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=token&#39;, {
        maxZoom: 18,
&#10;        id: &#39;mapbox.streets&#39;
    }).addTo(map);
&#10;    function onLocationFound(e) {
        var radius = e.accuracy / 2;
&#10;        L.marker(e.latlng).addTo(map)
            .bindPopup(&quot;You are within &quot; + radius + &quot; meters from this point&quot;).openPopup();
&#10;        L.circle(e.latlng, radius).addTo(map);
    }
&#10;    function onLocationError(e) {
        alert(e.message);
    }
&#10;    map.on(&#39;locationfound&#39;, onLocationFound);
    map.on(&#39;locationerror&#39;, onLocationError);
&#10;    map.locate({setView: true, maxZoom: 16});
&#10;&lt;/script&gt;
&#10;&lt;script&gt;
var x = document.getElementById(&quot;map&quot;);
&#10;function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    x.innerHTML = &quot;Geolocation is not supported by this browser.&quot;;
  }
}
&#10;function showPosition(position) {
    document.getElementById(&quot;frmLat&quot;).value = position.coords.latitude;
    document.getElementById(&quot;frmLon&quot;).value = position.coords.longitude;            
}
&lt;/script&gt;</code></pre>
<p>&lt;/body&gt; &lt;/html&gt;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Nov '19, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/d32cbb1eecaaae86fd35140149b49f6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eurus&#39;s gravatar image" />
<p><span>eurus</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eurus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Nov '19, 10:12</strong> </span></p>
</div>
</div>
<div id="comments-container-71791" class="comments-container">
<span id="71792"></span>
<div id="comment-71792" class="comment">
<div id="post-71792-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you explain in a bit more detail what you are trying to do and how it is related to OpenStreetMap?</p>
<p>What sort of platform are you asking about (on the web, on a phone, something else?) and what sort of map (tile-based, vector based, something else again?)</p>
<p>Questions such as "how do I find the user's location from a web page" (which may be part of what you are asking) are general web technology questions - you'll find answers at this help site but much more in-depth answers elsewhere.</p>
</div>
<div id="comment-71792-info" class="comment-info">
<span class="comment-age">(24 Nov '19, 10:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="71793"></span>
<div id="comment-71793" class="comment">
<div id="post-71793-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>now can help me ?</p>
</div>
<div id="comment-71793-info" class="comment-info">
<span class="comment-age">(24 Nov '19, 10:13)</span> <span class="comment-user userinfo">eurus</span>
</div>
</div>
<span id="71794"></span>
<div id="comment-71794" class="comment">
<div id="post-71794-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>er - not really, since it's unclear what "navigator" is in your code snippet. I can show you an example of web-based geolocation that works, though - see <a href="https://github.com/SomeoneElseOSM/SomeoneElse-map/blob/master/map/Scripts/leaflet_embed_small.js#L139">here</a>. That's using leaflet (as you seem to be doing also). Pressing the "centre" button <a href="https://map.atownsend.org.uk/maps/map/map.html">here</a> will invoke it.</p>
</div>
<div id="comment-71794-info" class="comment-info">
<span class="comment-age">(24 Nov '19, 10:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="71795"></span>
<div id="comment-71795" class="comment">
<div id="post-71795-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>solved, thanks</p>
</div>
<div id="comment-71795-info" class="comment-info">
<span class="comment-age">(24 Nov '19, 10:29)</span> <span class="comment-user userinfo">eurus</span>
</div>
</div>
<span id="71796"></span>
<div id="comment-71796" class="comment not_top_scorer">
<div id="post-71796-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>can set marker to center location ?</p>
</div>
<div id="comment-71796-info" class="comment-info">
<span class="comment-age">(24 Nov '19, 10:37)</span> <span class="comment-user userinfo">eurus</span>
</div>
</div>
<span id="71797"></span>
<div id="comment-71797" class="comment">
<div id="post-71797-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There's a ton of examples at the leaflet site <a href="https://leafletjs.com/">here</a> - including setting markers.</p>
</div>
<div id="comment-71797-info" class="comment-info">
<span class="comment-age">(24 Nov '19, 10:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71791" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-71791-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

