+++
type = "question"
title = "Getting information of terrain with bounding box"
description = '''Hi, I&#x27;m pretty new to OpenStreetMap and i&#x27;m sorry for my bad english. I&#x27;m trying to get terrain information from a specific bounding box. I tried it with overpass turbo but had no success. It would be nice if i could get informations like forrest, grassland, desert, snow or if the location in the bb...'''
date = "2020-02-03T14:23:00Z"
lastmod = "2020-02-04T04:11:00Z"
weight = 72829
keywords = [ "overpassapi", "overpass", "overpass-turbo" ]
aliases = [ "/questions/72829" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting information of terrain with bounding box](/questions/72829/getting-information-of-terrain-with-bounding-box)

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
<span id="post-72829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72829-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm pretty new to OpenStreetMap and i'm sorry for my bad english. I'm trying to get terrain information from a specific bounding box. I tried it with overpass turbo but had no success. It would be nice if i could get informations like forrest, grassland, desert, snow or if the location in the bbx is ocean (maybe also temperature).</p>
<p>I found the 'natural' key/tag but im not sure if this contains all the information i'm looking for</p>
<p>In the end my plan is to make a python script that gets these informations from multiple locations(bbx's)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Feb '20, 14:23</strong></p>
<img src="https://secure.gravatar.com/avatar/3ba64f8d6fbc982930996ffd72aba585?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fliens&#39;s gravatar image" />
<p><span>Fliens</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fliens has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72829" class="comments-container">
<span id="72843"></span>
<div id="comment-72843" class="comment">
<div id="post-72843-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please note OSM has no information on temperature.</p>
</div>
<div id="comment-72843-info" class="comment-info">
<span class="comment-age">(04 Feb '20, 04:11)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-72829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72829-form-container" class="comment-form-container">
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

<span id="72830"></span>

<div id="answer-container-72830" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72830-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your first place to look is in the wiki to find the correct 'key' for each entity you wish to locate: <a href="https://wiki.openstreetmap.org/wiki/Forest">https://wiki.openstreetmap.org/wiki/Forest</a></p>
<p>To get different boundary boxes use: <a href="https://osm.duschmarke.de/bbox.html">https://osm.duschmarke.de/bbox.html</a> (Press Alt &amp; drag with mouse left button)</p>
<p>To find single entity types:</p>
<pre><code>nwr [natural=wood](51.4649882,-0.089,51.5457077,0.079);
out geom;</code></pre>
<p>To find multiple entities types:</p>
<pre><code>[bbox:51.4649882,-0.089,51.5457077,0.079];
nwr [landuse=forest];
nwr [leisure=park];
out geom;</code></pre>
<p>Unsure if ocean is an OSM type - look up <code>coastline</code></p>
<p>Also <code>seasonal</code> but unsure how widely it's used.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '20, 15:01</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-72830" class="comments-container">
<span id="72831"></span>
<div id="comment-72831" class="comment">
<div id="post-72831-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>is it possible to get all tags or keys that the current boundary box has? for example i want to get all keys or tags from this boundary box: [bbox:54.4438,7.1249,54.6032,7.4435]</p>
</div>
<div id="comment-72831-info" class="comment-info">
<span class="comment-age">(03 Feb '20, 15:08)</span> <span class="comment-user userinfo">Fliens</span>
</div>
</div>
<span id="72832"></span>
<div id="comment-72832" class="comment">
<div id="post-72832-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just remove the tags, but be careful not to make the area too large, especially over land. It'll return large amounts of data.</p>
</div>
<div id="comment-72832-info" class="comment-info">
<span class="comment-age">(03 Feb '20, 16:12)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-72830" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72830-form-container" class="comment-form-container">
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

