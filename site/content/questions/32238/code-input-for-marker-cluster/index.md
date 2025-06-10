+++
type = "question"
title = "Code input for marker cluster"
description = '''I have a basic map created by mapbox with the code below and want input markercluster function, anybody can complete the code for me.Thanks a ton! &amp;lt;!DOCTYPE html&amp;gt; &amp;lt;html&amp;gt; &amp;lt;head&amp;gt; &amp;lt;meta charset=utf-8 /&amp;gt; &amp;lt;title&amp;gt;&amp;lt;/title&amp;gt;  &amp;lt;script src=&#x27;http://api.tiles.mapbox.com/map...'''
date = "2014-04-09T19:30:00Z"
lastmod = "2014-04-09T20:56:00Z"
weight = 32238
keywords = [ "openstreetmap", "leaflet", "mapbox" ]
aliases = [ "/questions/32238" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Code input for marker cluster](/questions/32238/code-input-for-marker-cluster)

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
<span id="post-32238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32238-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a basic map created by mapbox with the code below and want input markercluster function, anybody can complete the code for me.Thanks a ton!</p>
<pre><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;meta charset=utf-8 /&gt;
&lt;title&gt;&lt;/title&gt;
  &lt;script src=&#39;http://api.tiles.mapbox.com/mapbox.js/v1.6.2/mapbox.js&#39;&gt;&lt;/script&gt;
  &lt;link href=&#39;http://api.tiles.mapbox.com/mapbox.js/v1.6.2/mapbox.css&#39; rel=&#39;stylesheet&#39; /&gt;
  &lt;!--[if lte IE 8]&gt;
    &lt;link href=&#39;//api.tiles.mapbox.com/mapbox.js/v1.6.2/mapbox.ie.css&#39; rel=&#39;stylesheet&#39;&gt;
  &lt;![endif]--&gt;
  &lt;style&gt;
    body { margin:0; padding:0; }
    #map { position:absolute; top:0; bottom:0; width:100%; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div id=&#39;map&#39;&gt;&lt;/div&gt;
&lt;script type=&#39;text/javascript&#39;&gt;
var map = L.mapbox.map(&#39;map&#39;, &#39;zjmu916.map-47p7qt6u&#39;);
&#10;var featureLayer = L.mapbox.featureLayer(&#39;zjmu916.map-47p7qt6u&#39;,{ 
  sanitizer: function(x) { 
    return x; }
  }).addTo(map);
&#10;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Apr '14, 19:30</strong></p>
<img src="https://secure.gravatar.com/avatar/642f3d87ae674e0dade8063c685e7147?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zjmu916&#39;s gravatar image" />
<p><span>zjmu916</span><br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zjmu916 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Apr '14, 07:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-32238" class="comments-container">
<span id="32244"></span>
<div id="comment-32244" class="comment">
<div id="post-32244-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This portal is focused on OSM only. You might want to repost your question over at gis.stackoverflow.com as more devs lurk there. But before you do so, you might want to give it a try on your own: <a href="https://www.mapbox.com/mapbox.js/example/v1.0.0/leaflet-markercluster/">https://www.mapbox.com/mapbox.js/example/v1.0.0/leaflet-markercluster/</a> and then post where you fail.</p>
</div>
<div id="comment-32244-info" class="comment-info">
<span class="comment-age">(09 Apr '14, 20:56)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-32238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32238-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

