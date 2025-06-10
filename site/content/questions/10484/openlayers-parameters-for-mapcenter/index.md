+++
type = "question"
title = "openlayers - parameters for mapCenter"
description = '''Hi, I am trying to run this very simple code: var map;  function init() {  map = new OpenLayers.Map(&#x27;map&#x27;);   layerMapnik = new OpenLayers.Layer.OSM.Mapnik(&quot;Mapnik&quot;, {buffer: 4});  map.addLayer(layerMapnik);   map.setCenter(new OpenLayers.LonLat(16.5, 49.2), 5); }  $(function(){  init(); });  Everyt...'''
date = "2012-02-08T12:05:00Z"
lastmod = "2012-02-08T12:20:00Z"
weight = 10484
keywords = [ "mapcenter", "openlayers" ]
aliases = [ "/questions/10484" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [openlayers - parameters for mapCenter](/questions/10484/openlayers-parameters-for-mapcenter)

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
<span id="post-10484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10484-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am trying to run this very simple code:</p>
<pre><code>var map;
&#10;function init()
{
    map = new OpenLayers.Map(&#39;map&#39;);
&#10;    layerMapnik = new OpenLayers.Layer.OSM.Mapnik(&quot;Mapnik&quot;, {buffer: 4});
    map.addLayer(layerMapnik);
&#10;    map.setCenter(new OpenLayers.LonLat(16.5, 49.2), 5);
}
&#10;$(function(){
    init();
});</code></pre>
<p>Everything is ok, map is displayed but it is still centered here <a href="http://img35.imageshack.us/img35/5333/6e03cfcd14e24b2c9e6c32e.png">http://img35.imageshack.us/img35/5333/6e03cfcd14e24b2c9e6c32e.png</a> instead of here <a href="http://img338.imageshack.us/img338/4448/a501b38ec63e4da494b68da.png">http://img338.imageshack.us/img338/4448/a501b38ec63e4da494b68da.png</a></p>
<p>Any thoughts what I am doing wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapcenter" rel="tag" title="see questions tagged &#39;mapcenter&#39;">mapcenter</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '12, 12:05</strong></p>
<img src="https://secure.gravatar.com/avatar/474930251481c461e1bfe0bfb803a80a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pirozek&#39;s gravatar image" />
<p><span>Pirozek</span><br />
<span class="score" title="35 reputation points">35</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pirozek has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Feb '12, 12:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-10484" class="comments-container">
&#10;</div>
<div id="comment-tools-10484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10484-form-container" class="comment-form-container">
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

<span id="10485"></span>

<div id="answer-container-10485" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10485-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Pirozek has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your map is in spherical Mercator coordinates and you're setting it to a centre given in degrees. Try this:</p>
<pre><code>var proj4326 = new OpenLayers.Projection(&quot;EPSG:4326&quot;);
var projmerc = new OpenLayers.Projection(&quot;EPSG:900913&quot;);
var lonlat = new OpenLayers.LonLat(16.5, 49.2);
lonlat.transform(proj4326, projmerc);
map.setCenter(lonlat, 5);</code></pre>
<p>The problem you are seeing is a general OpenLayers issue when dealing with projections, and not limited to OpenStreetMap. Using a simpler toolbox like Leaflet would help you avoid these issues.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '12, 12:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-10485" class="comments-container">
<span id="10486"></span>
<div id="comment-10486" class="comment">
<div id="post-10486-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It works like a charm! Thanks man</p>
</div>
<div id="comment-10486-info" class="comment-info">
<span class="comment-age">(08 Feb '12, 12:20)</span> <span class="comment-user userinfo">Pirozek</span>
</div>
</div>
</div>
<div id="comment-tools-10485" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10485-form-container" class="comment-form-container">
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

