+++
type = "question"
title = "[closed] How to get boundary points of different zoom levels through getBounds() method of leaftlet API?"
description = '''I have written this function to find the corner points according to the 3 different zoom levels. The problem is that for all the 3 zoom levels, the corner points that I get are &quot;same&quot;!!   function findCorners ()  {  var zoomLevel;  for (zoomLevel = 7; zoomLevel &amp;lt; 10; zoomLevel++)  {  map.setView ...'''
date = "2012-10-11T11:47:00Z"
lastmod = "2012-10-11T12:53:00Z"
weight = 16831
keywords = [ "openstreetmap", "leaflet", "qt" ]
aliases = [ "/questions/16831" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to get boundary points of different zoom levels through getBounds() method of leaftlet API?](/questions/16831/how-to-get-boundary-points-of-different-zoom-levels-through-getbounds-method-of-leaftlet-api)

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
<span id="post-16831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16831-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-16831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have written this function to find the corner points according to the 3 different zoom levels.<br />
<strong>The problem is that for all the 3 zoom levels, the corner points that I get are</strong> "same"<strong>!!</strong></p>
<hr />
<pre><code>    function findCorners ()
    {
        var zoomLevel;
        for (zoomLevel = 7; zoomLevel &lt; 10; zoomLevel++)
        {
            map.setView (centerPoint, zoomLevel);
&#10;            var corners        = map.getBounds ();
&#10;            // Extracting boundary points
            var northEast      = corners.getNorthEast ();
            var southWest      = corners.getSouthWest ();
            var topLeft        = new L.LatLng (southWest.lat, northEast.lng, true);
            var bottomRight    = new L.LatLng (northEast.lat, southWest.lng, true);
&#10;            // For boundary line equation
            var topLeftLng     = toFixedd (topLeft.lng);
            var topLeftLat     = toFixedd (topLeft.lat);
            var bottomRightLng = toFixedd (bottomRight.lng);
            var bottomRightLat = toFixedd (bottomRight.lat);
&#10;            var stringCat       = &quot;&quot;;
            stringCat           = stringCat.concat (toFixedd (centerPoint.lng) + &quot;,&quot; + toFixedd (centerPoint.lat) + &quot;,&quot; + zoomLevel + &quot;,&quot; + topLeftLng + &quot;,&quot;, topLeftLat + &quot;,&quot;, + bottomRightLng + &quot;,&quot; + bottomRightLat + &quot;,&quot;);
&#10;            // For map downloading.
            // Attach the northEast and southWest corners too to the above formed string. 
            var bottomLeftLng = toFixedd (southWest.lng);
            var bottomLeftLat = toFixedd (southWest.lat);
            var topRightLng   = toFixedd (northEast.lng);
            var topRightLat   = toFixedd (northEast.lat);
&#10;            stringCat         = stringCat.concat (bottomLeftLng + &quot;,&quot; + bottomLeftLat + &quot;,&quot; + topRightLng + &quot;,&quot; + topRightLat);
&#10;            arrayCorners.push (stringCat);
        }
        map.setView (centerPoint, 13);
    }</code></pre>
<hr />
<p><strong>The function for selecting center point is here:</strong></p>
<pre><code>        var map;
        var centerPoint;
        var arrayCenterPoints = new Array ();
        var arrayFileNames    = new Array ();
        var arrayCorners      = new Array ();
        var arrayList         = new Array ();
&#10;        function displayMapAndClick ()
        {
            map = L.map (&#39;map&#39;, 
                    {
                        dragging: true,
                        scrollWheelZoom: true
                    }).setView ([51.505, -0.09], 13, true);
&#10;            L.tileLayer(&#39;http://{s}.tile.cloudmade.com/24c8d683cff74bffa7f00e59cd858e00/997/256/{z}/{x}/{y}.png&#39;, 
                {
                    attribution: &#39;Map data &amp;copy; &lt;a href=&quot;http://openstreetmap.org&quot;&gt;OpenStreetMap&lt;/a&gt; contributors, &lt;a href=&quot;http://creativecommons.org/licenses/by-sa/2.0/&quot;&gt;CC-BY-SA&lt;/a&gt;, Imagery © &lt;a href=&quot;http://cloudmade.com&quot;&gt;CloudMade&lt;/a&gt;&#39;,
                    maxZoom: 13,
                }).addTo (map);
&#10;            selectCenterPoint ();
        }
&#10;        function selectCenterPoint ()
        {
            var popup = L.popup();
&#10;            function onMapClick (e) 
            {
                popup
                    .setLatLng  (e.latlng)
                    .setContent (&quot;You clicked the map at: &quot; + e.latlng.toString())
                    .openOn      (map);
&#10;                    map.panTo (e.latlng);
                    L.marker (e.latlng).addTo (map).bindPopup (&quot;&lt;b&gt;Center point: &lt;/b&gt;&quot; + &quot;&lt;br&gt;&quot; + e.latlng + &quot;&lt;br /&gt;&quot;).openPopup ();
                    centerPoint = e.latlng; 
            }
            map.on (&#39;click&#39;, onMapClick);
        }
&#10;       function toFixedd (value) 
       {
        var power         = Math.pow (10, 4 || 0);
        var returnValue = String (Math.round (value * power) / power);
        return returnValue;
       }</code></pre>
<p><strong>Am I on the right track?</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-qt" rel="tag" title="see questions tagged &#39;qt&#39;">qt</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Oct '12, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/0848a0cab04ba90c16abc4c8f32904d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anisha%20Kaul&#39;s gravatar image" />
<p><span>Anisha Kaul</span><br />
<span class="score" title="29 reputation points">29</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anisha Kaul has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>11 Oct '12, 23:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-16831" class="comments-container">
<span id="16833"></span>
<div id="comment-16833" class="comment">
<div id="post-16833-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Reason of the downvote? Not a mind reader am I. <span>@someoneelse</span></p>
</div>
<div id="comment-16833-info" class="comment-info">
<span class="comment-age">(11 Oct '12, 12:28)</span> <span class="comment-user userinfo">Anisha Kaul</span>
</div>
</div>
<span id="16836"></span>
<div id="comment-16836" class="comment">
<div id="post-16836-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Frederik</span> Is this off-topic too?</p>
</div>
<div id="comment-16836-info" class="comment-info">
<span class="comment-age">(11 Oct '12, 12:53)</span> <span class="comment-user userinfo">Anisha Kaul</span>
</div>
</div>
</div>
<div id="comment-tools-16831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16831-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "This is not an OpenLayers (or Leaflet) support forum, nor a Javascript support forum. Your problem is not OSM related in the least - your problem would be just the same whether you display OSM tiles or Google tiles or whatever. Please stop abusing this forum with questions that have nothing to do with OSM. If you feel unable to judge which specific forum to direct a question to, I recommed http://gis.stackexchange.com/ which is a general place for all GIS-related stuff." by Frederik Ramm 11 Oct '12, 23:29

</div>

</div>

</div>

