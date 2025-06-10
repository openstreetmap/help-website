+++
type = "question"
title = "get the longitude and latitud and show on the inputbox"
description = '''hi, i show the user current location in map, i need to show user longitude and latitud on input box.tnx for help myscript:  &amp;lt;script&amp;gt;  var map = L.map(&#x27;map&#x27;).fitWorld();   L.tileLayer(&#x27;https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=token&#x27;, {  maxZoom: 18,  attribution: &#x27;Map d...'''
date = "2019-11-16T13:31:00Z"
lastmod = "2019-11-19T08:13:00Z"
weight = 71669
keywords = [ "latitude", "longitude" ]
aliases = [ "/questions/71669" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [get the longitude and latitud and show on the inputbox](/questions/71669/get-the-longitude-and-latitud-and-show-on-the-inputbox)

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
<span id="post-71669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71669-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi, i show the user current location in map, i need to show user longitude and latitud on input box.tnx for help</p>
<p>myscript:</p>
<pre><code>&lt;script&gt;
    var map = L.map(&#39;map&#39;).fitWorld();
&#10;    L.tileLayer(&#39;https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=token&#39;, {
        maxZoom: 18,
        attribution: &#39;Map data &amp;copy; &lt;a href=&quot;https://www.openstreetmap.org/&quot;&gt;OpenStreetMap&lt;/a&gt; contributors, &#39; +
            &#39;&lt;a href=&quot;https://creativecommons.org/licenses/by-sa/2.0/&quot;&gt;CC-BY-SA&lt;/a&gt;, &#39; +
            &#39;Imagery © &lt;a href=&quot;https://www.mapbox.com/&quot;&gt;Mapbox&lt;/a&gt;&#39;,
        id: &#39;mapbox.streets&#39;
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
&lt;/script&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '19, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/d32cbb1eecaaae86fd35140149b49f6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eurus&#39;s gravatar image" />
<p><span>eurus</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eurus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '19, 13:32</strong> </span></p>
</div>
</div>
<div id="comments-container-71669" class="comments-container">
<span id="71712"></span>
<div id="comment-71712" class="comment">
<div id="post-71712-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>See <a href="https://www.w3.org/TR/geolocation-API/">https://www.w3.org/TR/geolocation-API/</a> and <a href="https://www.w3schools.com/html/html5_geolocation.asp">https://www.w3schools.com/html/html5_geolocation.asp</a></p>
</div>
<div id="comment-71712-info" class="comment-info">
<span class="comment-age">(19 Nov '19, 08:13)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71669" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71669-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

