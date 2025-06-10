+++
type = "question"
title = "WMS vectors on top of TMS?"
description = '''Hi, this is probably a stupid question, but I want to have a TMS (raster) as the base layer in my Leaflet map and then overlay vectors from a WMS on top. Is this possible? I thought I had this working but it appears as though the WMS layer completely covers the TMS. I realize that both TMS and WMS a...'''
date = "2019-10-25T23:44:00Z"
lastmod = "2019-10-26T22:01:00Z"
weight = 71334
keywords = [ "wms", "leaflet", "tms", "osm" ]
aliases = [ "/questions/71334" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [WMS vectors on top of TMS?](/questions/71334/wms-vectors-on-top-of-tms)

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
<span id="post-71334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71334-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, this is probably a stupid question, but I want to have a TMS (raster) as the base layer in my Leaflet map and then overlay vectors from a WMS on top. Is this possible? I thought I had this working but it appears as though the WMS layer completely covers the TMS. I realize that both TMS and WMS are raster but I thought that somehow the TMS layer would show through and not be completely covered by the WMS. Here is my code</p>
<pre><code>         var map = L.map(&#39;mapContainer&#39;,
             {
                 maxZoom: 15,
                 minZoom: 9
             }).setView([47.58, -122.35], 9);
&#10;        L.tileLayer(&#39;http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&#39;, {
            attribution: &#39;&amp;copy; &lt;a href=&quot;http://openstreetmap.org&quot;&gt;OpenStreetMap&lt;/a&gt; contributors&#39;
            }).addTo(map);
&#10;        L.tileLayer.wms(&#39;https://carto.nationalmap.gov:443/arcgis/services/geonames/MapServer/WmsServer?&#39;, {
            layers: &#39;7&#39;
        }).addTo(map);</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wms" rel="tag" title="see questions tagged &#39;wms&#39;">wms</span> <span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-tms" rel="tag" title="see questions tagged &#39;tms&#39;">tms</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '19, 23:44</strong></p>
<img src="https://secure.gravatar.com/avatar/41a7fedf2793f657dcef6efefeb10b49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SeattleHeather&#39;s gravatar image" />
<p><span>SeattleHeather</span><br />
<span class="score" title="220 reputation points">220</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SeattleHeather has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71334" class="comments-container">
<span id="71335"></span>
<div id="comment-71335" class="comment">
<div id="post-71335-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This may not be what you're trying to do, and apologies if I'm stating the bleeding obvious here, but one raster overlay over another will work if the overlay has a transparent background. See <a href="https://www.openstreetmap.org/user/SomeoneElse/diary/47027">this</a> diary entry.</p>
</div>
<div id="comment-71335-info" class="comment-info">
<span class="comment-age">(26 Oct '19, 00:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71334" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71334-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="71340"></span>

<div id="answer-container-71340" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71340-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can add</p>
<pre><code>transparent: &#39;true&#39;</code></pre>
<p>to your WMS options (where you currently only have "layers: '7'") and this will tell the WMS that you would like tiles with a transparent background. Not all WMS servers will honour this request, however (yours seems not to, sadly). In which case you might try</p>
<pre><code>opacity: &#39;0.5&#39;</code></pre>
<p>which will at least make the WMS layer semi-transparent so while the underlying OSM map will lose contrast it is still visible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '19, 22:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-71340" class="comments-container">
&#10;</div>
<div id="comment-tools-71340" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71340-form-container" class="comment-form-container">
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

