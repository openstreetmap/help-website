+++
type = "question"
title = "[closed] Openlayers - adding POI with description"
description = '''Hi, I want to read some POIs from text file, so I looked at Openlayers example how to do it and its great. But now I need to add new POI manually (when user clicks on the map). It can be done with map.addMarker and it works great, but this marker is different from one I get from text file. Marker fr...'''
date = "2012-02-08T15:06:00Z"
lastmod = "2012-02-08T16:23:00Z"
weight = 10488
keywords = [ "marker", "openlayers", "poi" ]
aliases = [ "/questions/10488" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Openlayers - adding POI with description](/questions/10488/openlayers-adding-poi-with-description)

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
<span id="post-10488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10488-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-10488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I want to read some POIs from text file, so I looked at Openlayers example how to do it and its great. But now I need to add new POI manually (when user clicks on the map). It can be done with map.addMarker and it works great, but this marker is different from one I get from text file.</p>
<p>Marker from text file has a popup when I click on it, with description. But I cant find any way how to add new marker with description to map. So how can I do this?</p>
<p>I load POIs like this:</p>
<pre><code>markers = new OpenLayers.Layer.Text( &quot;My Points&quot;,
                    { location:&quot;poi.txt&quot;,
                      projection: map.displayProjection
                    });
map.addLayer(markers);</code></pre>
<p>Content of <a href="http://poi.txt">poi.txt</a>:</p>
<pre><code>lat lon title   description icon    iconSize    iconOffset
48.9459301  9.6075669   Title One   Description one&lt;br&gt;Second line.&lt;br&gt;&lt;br&gt;(click again to close)   Ol/img/marker-green.png 24,24   0,-24
48.9899851  9.5382032   Title Two   Description two.    Ol/img/marker-green.png 16,16   -8,-8</code></pre>
<p>And I add new marker after click like this:</p>
<pre><code>var size = new OpenLayers.Size(21,25);
var offset = new OpenLayers.Pixel(-(size.w/2), -size.h);
var icon = new OpenLayers.Icon(&#39;http://www.openlayers.org/dev/img/marker.png&#39;,size,offset);
markers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(lon,lat),icon));</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '12, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/474930251481c461e1bfe0bfb803a80a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pirozek&#39;s gravatar image" />
<p><span>Pirozek</span><br />
<span class="score" title="35 reputation points">35</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pirozek has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>20 Dec '12, 12:30</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-10488" class="comments-container">
&#10;</div>
<div id="comment-tools-10488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10488-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "This is not an OpenLayers help site and your question is not about anything OSM-specific." by Frederik Ramm 20 Dec '12, 12:30

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10490"></span>

<div id="answer-container-10490" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10490-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not an OpenLayers help system and especially not a coding site. You will probably get more help from an OpenLayers forum or OpenLayers mailing list.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '12, 16:23</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-10490" class="comments-container">
&#10;</div>
<div id="comment-tools-10490" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10490-form-container" class="comment-form-container">
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

