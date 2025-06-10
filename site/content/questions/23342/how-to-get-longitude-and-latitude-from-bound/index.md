+++
type = "question"
title = "How to get longitude and latitude from bound?"
description = '''The below code will return the lat &amp;amp; lon values, when i click any where on the map.  The result is lon=8931183.8958044,lat=1456094.8596215 map.events.register(&#x27;click&#x27;, map, handleMapClick); function handleMapClick(e) { var lonlat = map.getLonLatFromViewPortPx(e.xy); alert(lonlat); }  how to get ...'''
date = "2013-06-13T16:06:00Z"
lastmod = "2013-06-15T07:29:00Z"
weight = 23342
keywords = [ "latitude", "bound", "longtitude" ]
aliases = [ "/questions/23342" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get longitude and latitude from bound?](/questions/23342/how-to-get-longitude-and-latitude-from-bound)

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
<span id="post-23342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23342-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The below code will return the lat &amp; lon values, when i click any where on the map. The result is <strong>lon=8931183.8958044,lat=1456094.8596215</strong></p>
<pre><code>map.events.register(&#39;click&#39;, map, handleMapClick);
function handleMapClick(e)
{
var lonlat = map.getLonLatFromViewPortPx(e.xy);
alert(lonlat);
}</code></pre>
<p>how to get the lat &amp; lon exactly when clicking on the map what is the extact format for lat and lon</p>
<p>Is this the correct lat &amp; lon? because I see that the Lat &amp; Lon comes in 2 digit (0-90) before can some one help me in converting the values?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-bound" rel="tag" title="see questions tagged &#39;bound&#39;">bound</span> <span class="post-tag tag-link-longtitude" rel="tag" title="see questions tagged &#39;longtitude&#39;">longtitude</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '13, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/c8b533bf899ec4204f39cfc04ad6f1a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gayathri&#39;s gravatar image" />
<p><span>gayathri</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gayathri has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jun '13, 05:42</strong> </span></p>
</div>
</div>
<div id="comments-container-23342" class="comments-container">
<span id="23377"></span>
<div id="comment-23377" class="comment">
<div id="post-23377-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This is an OpenLayers question not OpenStreetMap try GIS Stack Exchange, read a bit about projections, and this blog post might be useful <a href="http://macwright.org/2012/01/12/openlayers.html.">http://macwright.org/2012/01/12/openlayers.html.</a></p>
</div>
<div id="comment-23377-info" class="comment-info">
<span class="comment-age">(14 Jun '13, 15:14)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23342" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23342-form-container" class="comment-form-container">
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

<span id="23349"></span>

<div id="answer-container-23349" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23349-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>lonlat.lon, lonlat.lat</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '13, 19:42</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-23349" class="comments-container">
<span id="23355"></span>
<div id="comment-23355" class="comment">
<div id="post-23355-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is this the correct lat &amp; lon? because I see that the Lat &amp; Lon comes in 2 digit (0-90) before can some one help me in converting the values?</p>
</div>
<div id="comment-23355-info" class="comment-info">
<span class="comment-age">(14 Jun '13, 05:42)</span> <span class="comment-user userinfo">gayathri</span>
</div>
</div>
<span id="23379"></span>
<div id="comment-23379" class="comment">
<div id="post-23379-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess you have read this <a href="http://wiki.openstreetmap.org/wiki/Bounding_box">http://wiki.openstreetmap.org/wiki/Bounding_box</a> and noticed that it uses degrees and fractions in decimal format NOT degrees Minutes and Seconds so 45.5 deg= 45,30,00 DMS. If that does not help what lat lon were you expecting to get back from your code. Could you set it up so you know the result beforehand as a test?</p>
</div>
<div id="comment-23379-info" class="comment-info">
<span class="comment-age">(14 Jun '13, 19:46)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="23390"></span>
<div id="comment-23390" class="comment">
<div id="post-23390-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>thank for u kindly reply.... i got answer</p>
</div>
<div id="comment-23390-info" class="comment-info">
<span class="comment-age">(15 Jun '13, 07:26)</span> <span class="comment-user userinfo">gayathri</span>
</div>
</div>
<span id="23391"></span>
<div id="comment-23391" class="comment">
<div id="post-23391-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<pre><code>var fromProjection = new OpenLayers.Projection(&quot;EPSG:4326&quot;);  
var toProjection   = new OpenLayers.Projection(&quot;EPSG:900913&quot;);
var mapbounds = map.getExtent(); // to getting the bounds
var bound = mapbounds.transform(toProjection, fromProjection ); // converting the bounds to left, right, bottom &amp; top values.</code></pre>
</div>
<div id="comment-23391-info" class="comment-info">
<span class="comment-age">(15 Jun '13, 07:29)</span> <span class="comment-user userinfo">gayathri</span>
</div>
</div>
</div>
<div id="comment-tools-23349" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23349-form-container" class="comment-form-container">
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

