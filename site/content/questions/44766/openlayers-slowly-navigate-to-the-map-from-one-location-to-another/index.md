+++
type = "question"
title = "OpenLayers: Slowly navigate to the map from one location to another"
description = '''Hello Guys, Please help me on this, I searched lot but didnt found solution. first of all I am setting my map at one point suppose my lat long are 19.151568,41.872330 so I am using following code to set my map on load to this points.. var val1 = &quot;19.151568&quot;; var val2 = &quot;41.872330&quot;; var lonLat = new ...'''
date = "2015-08-14T06:00:00Z"
lastmod = "2015-08-19T05:14:00Z"
weight = 44766
keywords = [ "openlayers" ]
aliases = [ "/questions/44766" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OpenLayers: Slowly navigate to the map from one location to another](/questions/44766/openlayers-slowly-navigate-to-the-map-from-one-location-to-another)

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
<span id="post-44766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44766-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Guys,</p>
<p>Please help me on this, I searched lot but didnt found solution.</p>
<p>first of all I am setting my map at one point suppose my lat long are <code>19.151568,41.872330</code></p>
<p>so I am using following code to set my map on load to this points..</p>
<pre><code>var val1 = &quot;19.151568&quot;;
var val2 = &quot;41.872330&quot;;
var lonLat = new OpenLayers.LonLat(val1,val2).transform(epsg4326, projectTo);
var zoom=18;
map.setCenter(lonLat, zoom);</code></pre>
<p>Now in my js code I am calling one function i.e. <code>changeLocation(var1,var2);</code> where var1 and var2 are my new lat and long for example : <code>18.950367,41.553726</code></p>
<p>so my code for <code>changeLocation(var1,var2)</code> is as follows</p>
<pre><code>function changeLocation(var1,var2) {
var zoomlvl = map.zoom;
var lonLat = new OpenLayers.LonLat(val1,val2).transform(epsg4326, projectTo);
map.setCenter(lonLat, zoomlvl);
}</code></pre>
<p>after this function my map immediately goes to that location. where want it to go slowly from previous location to my new location.</p>
<p>Please help me on this.. Thank you guys..:)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '15, 06:00</strong></p>
<img src="https://secure.gravatar.com/avatar/0ae2f284895c331bd9b5bd1e8f96ba88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="akaAni&#39;s gravatar image" />
<p><span>akaAni</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="akaAni has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Aug '15, 06:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-44766" class="comments-container">
&#10;</div>
<div id="comment-tools-44766" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44766-form-container" class="comment-form-container">
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

<span id="44775"></span>

<div id="answer-container-44775" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44775-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-44775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="akaAni has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here are a few examples for <strong>animated panning / fly to:</strong></p>
<ul>
<li>OL3: <a href="http://openlayers.org/en/v3.1.0/examples/animation.html">http://openlayers.org/en/v3.1.0/examples/animation.html</a></li>
<li>OL2: <a href="http://dev.openlayers.org/examples/animated_panning.html">http://dev.openlayers.org/examples/animated_panning.html</a></li>
<li>Mapbox: <a href="https://www.mapbox.com/mapbox-gl-js/example/flyto/">https://www.mapbox.com/mapbox-gl-js/example/flyto/</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '15, 10:40</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Aug '15, 10:42</strong> </span></p>
</div>
</div>
<div id="comments-container-44775" class="comments-container">
<span id="44776"></span>
<div id="comment-44776" class="comment">
<div id="post-44776-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>about the mapbox solution (or even the OL or leafletjs solution):</p>
<p>is there any software (except GoogleEarth!) or webservice that can display this smooth zoom out and zoom in on an OSM based map, and that can capture or render a video clip from this?</p>
</div>
<div id="comment-44776-info" class="comment-info">
<span class="comment-age">(15 Aug '15, 13:38)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="44812"></span>
<div id="comment-44812" class="comment">
<div id="post-44812-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much......</p>
</div>
<div id="comment-44812-info" class="comment-info">
<span class="comment-age">(19 Aug '15, 05:14)</span> <span class="comment-user userinfo">akaAni</span>
</div>
</div>
</div>
<div id="comment-tools-44775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44775-form-container" class="comment-form-container">
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

