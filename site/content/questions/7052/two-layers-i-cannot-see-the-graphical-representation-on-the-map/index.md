+++
type = "question"
title = "two layers - I cannot see the graphical representation on the map"
description = '''People, I need a Help. I have one layer on the Geoserver, called Comp5 into a var wmms (it is a point map) I want to put this layer together with a map from Openstreetmap into a var mapnik. I&#x27;m not seeing both map, but just the Openstreetmap (Mapnik). Why? I would like to see the Map of city (from O...'''
date = "2011-08-12T02:37:00Z"
lastmod = "2011-08-12T09:17:00Z"
weight = 7052
keywords = [ "openlayers" ]
aliases = [ "/questions/7052" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [two layers - I cannot see the graphical representation on the map](/questions/7052/two-layers-i-cannot-see-the-graphical-representation-on-the-map)

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
<span id="post-7052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7052-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>People, I need a Help. I have one layer on the Geoserver, called Comp5 into a var wmms (it is a point map) I want to put this layer together with a map from Openstreetmap into a var mapnik.</p>
<p>I'm not seeing both map, but just the Openstreetmap (Mapnik). Why? I would like to see the Map of city (from Openstreetmmap) and the points over the city map.</p>
<p>The code I'm using is the following:</p>
<pre><code>&lt;script type=&quot;text/javascript&quot; src=&quot;js/OpenLayers/OpenLayers.js&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/javascript&quot;&gt;
var map;
&#10;function init() {
&#10;    map = new OpenLayers.Map(&quot;basicMap&quot;,{projection: new OpenLayers.Projection(&quot;EPSG:900913&quot;),
    displayProjection: new OpenLayers.Projection(&quot;EPSG:4326&quot;),isBaseLayer:false,visibility: true
    });
&#10;    var mapnik = new OpenLayers.Layer.OSM();
&#10;    var wms = new OpenLayers.Layer.WMS(
            &quot;Marble Blue&quot;,
            &quot;http://localhost:9999/geoserver/wms&quot;,
            {layers: &#39;comp5&#39;, transparent:true}//,
    );
&#10;     map.addLayer(wms);
     map.addLayer(mapnik);
&#10;    map.setCenter(new OpenLayers.LonLat(-46.69320,-23.64665) // Center of the map
&#10;        .transform(
&#10;      new OpenLayers.Projection(&quot;EPSG:4326&quot;), // transform from WGS 1984
&#10;      new OpenLayers.Projection(&quot;EPSG:900913&quot;) // to Spherical Mercator Projection
&#10;     ), 11 // Zoom level
&#10;   );
&#10;  }
&lt;/script&gt;</code></pre>
<p>Thanks in advance for any help.</p>
<p>Vernei</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Aug '11, 02:37</strong></p>
<img src="https://secure.gravatar.com/avatar/19b2736f9f75fa463688aded9c6b6182?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vernei&#39;s gravatar image" />
<p><span>vernei</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vernei has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Aug '11, 09:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span></p>
</div>
</div>
<div id="comments-container-7052" class="comments-container">
&#10;</div>
<div id="comment-tools-7052" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7052-form-container" class="comment-form-container">
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

<span id="7055"></span>

<div id="answer-container-7055" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7055-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This question is OpenLayers realted and should go to OpenLayers mailing <a href="http://lists.osgeo.org/mailman/listinfo/openlayers-users">list</a> or asked on IRC: <a href="irc://irc.freenode.net/#openlayers">irc://irc.freenode.net/#openlayers</a> . You have a higher chance to get help from there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '11, 09:17</strong></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RM87 has 20 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Aug '11, 09:20</strong> </span></p>
</div>
</div>
<div id="comments-container-7055" class="comments-container">
&#10;</div>
<div id="comment-tools-7055" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7055-form-container" class="comment-form-container">
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

