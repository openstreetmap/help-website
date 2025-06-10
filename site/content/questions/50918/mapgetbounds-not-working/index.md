+++
type = "question"
title = "[closed] map.getBounds() Not Working..."
description = '''How to get map corner latlong in OSM. i have many tried to solve it but i did not solve it. i have use below example. =================================================== &amp;lt;html&amp;gt; &amp;lt;head&amp;gt;  &amp;lt;title&amp;gt;OpenLayers Demo&amp;lt;/title&amp;gt;  &amp;lt;style type=&quot;text/css&quot;&amp;gt;  html, body, #basicMap  {  wi...'''
date = "2016-07-15T08:30:00Z"
lastmod = "2016-07-16T07:13:00Z"
weight = 50918
keywords = [ "getview", "getbounds" ]
aliases = [ "/questions/50918" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] map.getBounds() Not Working...](/questions/50918/mapgetbounds-not-working)

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
<span id="post-50918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50918-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How to get map corner latlong in OSM. i have many tried to solve it but i did not solve it.</p>
<p>i have use below example.</p>
<p>===================================================</p>
<p>&lt;html&gt; &lt;head&gt; &lt;title&gt;OpenLayers Demo&lt;/title&gt; &lt;style type="text/css"&gt; html, body, #basicMap { width: 100%; height: 100%; margin: 0; } &lt;/style&gt;</p>
<pre><code>&lt;script src=&quot;http://www.openlayers.org/api/OpenLayers.js&quot; type=&quot;text/javascript&quot;&gt;&lt;/script&gt;
&#10;&lt;script type=&quot;text/javascript&quot;&gt;
    function init() {
        var marker_layer = new OpenLayers.Layer.Markers(&quot;Markers&quot;);
&#10;        var map = new OpenLayers.Map(&quot;basicMap&quot;);
        var mapnik = new OpenLayers.Layer.OSM();
        var fromProjection = new OpenLayers.Projection(&quot;EPSG:4326&quot;);   // Transform from WGS 1984
        var toProjection = new OpenLayers.Projection(&quot;EPSG:900913&quot;); // to Spherical Mercator Projection
&#10;        var position1 = new OpenLayers.LonLat(78.9629, 20.5937).transform(fromProjection, toProjection);
        var position2 = new OpenLayers.LonLat(79.2629, 20.9937).transform(fromProjection, toProjection);
        var zoom = 8;
&#10;        map.addLayer(mapnik);
        map.setCenter(position1, zoom);
&#10;
        debugger;
&#10;        var bounds = map.getBounds();       //Error : map.getBounds is not a function
&#10;        var vv1 = map.getView().calculateExtent();  //Error : map.getView is not a function
&#10;    }
&lt;/script&gt;</code></pre>
<p>&lt;/head&gt; &lt;body onload="init();"&gt;</p>
<div>
&#10;</div>
&lt;/body&gt; &lt;/html&gt;
<p>===================================================</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-getview" rel="tag" title="see questions tagged &#39;getview&#39;">getview</span> <span class="post-tag tag-link-getbounds" rel="tag" title="see questions tagged &#39;getbounds&#39;">getbounds</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jul '16, 08:30</strong></p>
<img src="https://secure.gravatar.com/avatar/fc38080d9e980459bc64bf221f56bc62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jatin%20Patel&#39;s gravatar image" />
<p><span>Jatin Patel</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jatin Patel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>16 Jul '16, 07:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-50918" class="comments-container">
<span id="50929"></span>
<div id="comment-50929" class="comment">
<div id="post-50929-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Isn't this a duplicate of <a href="https://help.openstreetmap.org/questions/50696/how-to-get-map-corner-latlong-using-open-layer">https://help.openstreetmap.org/questions/50696/how-to-get-map-corner-latlong-using-open-layer</a> ?</p>
</div>
<div id="comment-50929-info" class="comment-info">
<span class="comment-age">(15 Jul '16, 17:52)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="50936"></span>
<div id="comment-50936" class="comment">
<div id="post-50936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If possible then write a solution for above query...</p>
<p>Thanks in advance.</p>
</div>
<div id="comment-50936-info" class="comment-info">
<span class="comment-age">(16 Jul '16, 07:13)</span> <span class="comment-user userinfo">Jatin Patel</span>
</div>
</div>
</div>
<div id="comment-tools-50918" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50918-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question, see https://help.openstreetmap.org/questions/50696/how-to-get-map-corner-latlong-using-open-layer" by scai 16 Jul '16, 07:47

</div>

</div>

</div>

