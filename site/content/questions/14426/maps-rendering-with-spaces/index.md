+++
type = "question"
title = "Maps rendering with spaces"
description = '''When i display a map in a div called venuemap, the map is displayed with gaps. Example: http://www.diigo.com/item/image/1w8bo/ck4u This is the code i use for displaying the map  /* Open map */  map = new OpenLayers.Map(&quot;venuemap&quot;);  map.addLayer(new OpenLayers.Layer.OSM());   var lonLat = new OpenLa...'''
date = "2012-07-20T12:40:00Z"
lastmod = "2012-07-20T13:26:00Z"
weight = 14426
keywords = [ "maps", "wrong", "javascript", "display" ]
aliases = [ "/questions/14426" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Maps rendering with spaces](/questions/14426/maps-rendering-with-spaces)

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
<span id="post-14426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14426-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When i display a map in a div called venuemap, the map is displayed with gaps.</p>
<p>Example:</p>
<p><a href="http://www.diigo.com/item/image/1w8bo/ck4u">http://www.diigo.com/item/image/1w8bo/ck4u</a></p>
<p>This is the code i use for displaying the map</p>
<pre><code>        /* Open map */
            map = new OpenLayers.Map(&quot;venuemap&quot;);
            map.addLayer(new OpenLayers.Layer.OSM());
&#10;            var lonLat = new OpenLayers.LonLat( venue.location.lng ,venue.location.lat )
                  .transform(
                    new OpenLayers.Projection(&quot;EPSG:4326&quot;), // transform from WGS 1984
                    map.getProjectionObject() // to Spherical Mercator Projection
                  );
&#10;            var zoom=16;
&#10;            var markers = new OpenLayers.Layer.Markers( &quot;Markers&quot; );
            map.addLayer(markers);
&#10;            markers.addMarker(new OpenLayers.Marker(lonLat));
&#10;            map.setCenter (lonLat, zoom);
            /* end open map */</code></pre>
<p>What is wrong with my code? Kind regards brantje</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maps" rel="tag" title="see questions tagged &#39;maps&#39;">maps</span> <span class="post-tag tag-link-wrong" rel="tag" title="see questions tagged &#39;wrong&#39;">wrong</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jul '12, 12:40</strong></p>
<img src="https://secure.gravatar.com/avatar/b617881083b5b8ea49d3fc517fb5a2e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brantje&#39;s gravatar image" />
<p><span>brantje</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brantje has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14426" class="comments-container">
<span id="14431"></span>
<div id="comment-14431" class="comment">
<div id="post-14431-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The example url seems wrong : no map there.</p>
</div>
<div id="comment-14431-info" class="comment-info">
<span class="comment-age">(20 Jul '12, 13:23)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-14426" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14426-form-container" class="comment-form-container">
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

<span id="14432"></span>

<div id="answer-container-14432" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14432-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Probably your JS code is right, but your HTML style is wrong ? Make sure you set margin and padding to 0 on your map div and the tag surrounding the div.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jul '12, 13:26</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-14432" class="comments-container">
&#10;</div>
<div id="comment-tools-14432" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14432-form-container" class="comment-form-container">
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

