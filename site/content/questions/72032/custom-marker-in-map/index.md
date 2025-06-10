+++
type = "question"
title = "custom marker in map"
description = '''hi i use web map and i need to show current location like https://www.openstreetmap.org/ blue svg icon can help me ? thanks. my script:   &amp;lt;script&amp;gt;  var map = L.map(&#x27;map&#x27;).fitWorld();  L.tileLayer(&#x27;https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=token&#x27;, {  maxZoom: 18,   id: &#x27;...'''
date = "2019-12-07T13:15:00Z"
lastmod = "2019-12-07T13:15:00Z"
weight = 72032
keywords = [ "marker" ]
aliases = [ "/questions/72032" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [custom marker in map](/questions/72032/custom-marker-in-map)

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
<span id="post-72032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72032-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi i use web map and i need to show current location like <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> blue svg icon can help me ? thanks.</p>
<p>my script:</p>
<pre><code>    &lt;script&gt;
    var map = L.map(&#39;map&#39;).fitWorld();
    L.tileLayer(&#39;https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=token&#39;, {
        maxZoom: 18,
&#10;        id: &#39;mapbox.streets&#39;
    }).addTo(map);
&#10;    function onLocationFound(e) {
        var radius = e.accuracy / 2;
&#10;        L.marker(e.latlng).addTo(map);              ;
        map.setZoom( 18 );
        L.circle(e.latlng, radius).addTo(map);
    }
&#10;    function onLocationError(e) {
        alert(e.message);
    }
&#10;    map.on(&#39;locationfound&#39;, onLocationFound);
    map.on(&#39;locationerror&#39;, onLocationError);
&#10;    map.locate({setView: true, maxZoom: 16});
&#10;&lt;/script&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Dec '19, 13:15</strong></p>
<img src="https://secure.gravatar.com/avatar/d32cbb1eecaaae86fd35140149b49f6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eurus&#39;s gravatar image" />
<p><span>eurus</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eurus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Dec '19, 06:50</strong> </span></p>
</div>
</div>
<div id="comments-container-72032" class="comments-container">
&#10;</div>
<div id="comment-tools-72032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72032-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

