+++
type = "question"
title = "Null or undefined error in AddPopup"
description = '''I get this error when I call AddPopup():  Unable to get value of the property &#x27;Left&#x27;; object is null or undefined http://www.openlayers.org/api/OpenLayers.js  The same error occurs in both Chrome and IE. The map works fine when I comment out that line, and the markers work fine as well. Later, icon0...'''
date = "2012-03-02T19:23:00Z"
lastmod = "2012-03-05T17:45:00Z"
weight = 10951
keywords = [ "openlayers", "popup", "osm" ]
aliases = [ "/questions/10951" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Null or undefined error in AddPopup](/questions/10951/null-or-undefined-error-in-addpopup)

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
<span id="post-10951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10951-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I get this error when I call AddPopup():</p>
<blockquote>
<p><em>Unable to get value of the property 'Left'; object is null or undefined</em></p>
<p><em><a href="http://www.openlayers.org/api/OpenLayers.js">http://www.openlayers.org/api/OpenLayers.js</a></em></p>
</blockquote>
<p>The same error occurs in both Chrome and IE. The map works fine when I comment out that line, and the markers work fine as well. Later, icon0 and lonLat0 will be several items in a loop, but I'll handle that. The end result should be a text box of some kind that would display on the marker.</p>
<p>The marker at lonLat0 displays, so it doesn't seem like a problem with the lonLat object.</p>
<p>Yes, I will end up displaying many markers with text on them all at once. I know, it seems silly, but that's the requirement.</p>
<p><strong>Why does addPopup give me this error?</strong></p>
<pre><code>&lt;html&gt;&lt;body&gt;   
&lt;div id=&#39;mapdiv&#39;&gt;&lt;/div&gt; &lt;script src=&#39;http://www.openlayers.org/api/OpenLayers.js&#39;&gt;&lt;/script&gt; 
&lt;script&gt;
  map = new OpenLayers.Map(&#39;mapdiv&#39;);
  map.addLayer(new OpenLayers.Layer.OSM());
  var lonLat = new OpenLayers.LonLat(-104.73,38.92).transform(new OpenLayers.Projection(&#39;EPSG:4326&#39;), map.getProjectionObject() );
  var markers = new OpenLayers.Layer.Markers( &#39;Markers&#39; );
  map.addLayer(markers);
  markers.addMarker(new OpenLayers.Marker(lonLat));     
  function onPopupClose(evt) {selectControl.unselect(this.feature); }
  var icon0 = new OpenLayers.Icon(&quot;pinMS.png&quot;, new OpenLayers.Size(32,32), new OpenLayers.Pixel(-16,-32));  
  var lonLat0 = new OpenLayers.LonLat(-104.73,38.92).transform(new OpenLayers.Projection(&#39;EPSG:4326&#39;), map.getProjectionObject());  
  markers.addMarker(new OpenLayers.Marker(lonLat0, icon0.clone()));  
  map.addPopup(new OpenLayers.Popup.FramedCloud(&quot;featurePopup&quot;, lonLat0, new OpenLayers.Size(10, 10), &quot;&lt;h2&gt;Title&lt;/h2&gt;description&quot;, null, true, onPopupClose)); 
  map.setCenter (lonLat, 1);    
&lt;/script&gt;&lt;/body&gt;&lt;/html&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-popup" rel="tag" title="see questions tagged &#39;popup&#39;">popup</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '12, 19:23</strong></p>
<img src="https://secure.gravatar.com/avatar/30d5456d1b71664feb5cda0233bf0d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tsilb&#39;s gravatar image" />
<p><span>tsilb</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tsilb has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Mar '12, 19:24</strong> </span></p>
</div>
</div>
<div id="comments-container-10951" class="comments-container">
&#10;</div>
<div id="comment-tools-10951" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10951-form-container" class="comment-form-container">
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

<span id="10967"></span>

<div id="answer-container-10967" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10967-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-10967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tsilb has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had a play around in firefox with your code. For me it gives an error '<code>extent is null</code>'</p>
<p>...which is easily fixed by swapping the last two lines around i.e. do <code>map.setCenter</code> before <code>map.addPopup</code>.</p>
<p>For me then it works apart from the size of the bubble popup is wrong and the close button doesn't work, so this would need more work.</p>
<p>You might find <a href="http://harrywood.co.uk/maps/examples/openlayers/marker-popups.html">my little popups example here</a> useful, except it's defining markers as vector features so it's a bit different.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '12, 21:44</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-10967" class="comments-container">
<span id="10977"></span>
<div id="comment-10977" class="comment">
<div id="post-10977-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That did it. Do you know of a way to make the popups smaller? My requirement is to have many of them with a small text blurb, visible all the time. Thanks.</p>
</div>
<div id="comment-10977-info" class="comment-info">
<span class="comment-age">(05 Mar '12, 17:45)</span> <span class="comment-user userinfo">tsilb</span>
</div>
</div>
</div>
<div id="comment-tools-10967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10967-form-container" class="comment-form-container">
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

