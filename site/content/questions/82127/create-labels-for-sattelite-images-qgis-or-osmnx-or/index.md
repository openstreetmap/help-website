+++
type = "question"
title = "Create labels for sattelite images, qgis or osmnx or?"
description = '''Hi all! I am new to OSM and GIS in general. I am trying to create labels for sattelite images I have to do building/road segmentation. I&#x27;ve now figured out how to do this with osmnx (phew!), now that I think about it a little more, I was wondering if there might be an easier (better, cleaner) way cr...'''
date = "2021-10-11T17:08:00Z"
lastmod = "2021-10-14T05:28:00Z"
weight = 82127
keywords = [ "overpassapi", "qgis", "osmnx" ]
aliases = [ "/questions/82127" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Create labels for sattelite images, qgis or osmnx or?](/questions/82127/create-labels-for-sattelite-images-qgis-or-osmnx-or)

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
<span id="post-82127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82127-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all!</p>
<p>I am new to OSM and GIS in general.</p>
<p>I am trying to create labels for sattelite images I have to do building/road segmentation. I've now figured out how to do this with osmnx (phew!), now that I think about it a little more, I was wondering if there might be an easier (better, cleaner) way creating it with open gis? Or would you know of some other way?</p>
<p>What I did with osmnx:</p>
<pre><code>graph = ox.graph.graph_from_bbox(north, south, east, west)
geometries = ox.geometries.geometries_from_bbox(north, south, east, west, tags = {&#39;building&#39;:True, &#39;amenity&#39;:True, &#39;landuse&#39;:[&#39;commercial&#39;, &#39;residential&#39;, &#39;industrial&#39;, &#39;mixed&#39;]})</code></pre>
<p>this creates a map for my corresponding sattelite image (with bbox north south east west)</p>
<p>Edit: this is an example of what I've been able to cook up for now: <img src="https://imgur.com/a/U48SViV" alt="image" /></p>
<p><a href="https://imgur.com/a/U48SViV">https://imgur.com/a/U48SViV</a> thanks in advance for any tips,</p>
<p>cheers!</p>
<p>oli</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-osmnx" rel="tag" title="see questions tagged &#39;osmnx&#39;">osmnx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Oct '21, 17:08</strong></p>
<img src="https://secure.gravatar.com/avatar/cdbcea9c4b54ebbd5c124713a663f464?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oliver&#39;s gravatar image" />
<p><span>oliver</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oliver has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Oct '21, 05:32</strong> </span></p>
</div>
</div>
<div id="comments-container-82127" class="comments-container">
<span id="82128"></span>
<div id="comment-82128" class="comment">
<div id="post-82128-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you try explaining that again, perhaps in your native language? I've no idea what you are trying to do.</p>
</div>
<div id="comment-82128-info" class="comment-info">
<span class="comment-age">(11 Oct '21, 17:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82129"></span>
<div id="comment-82129" class="comment">
<div id="post-82129-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> Hi, apologies, English sort of is my first language but I am bad at all of them (:-S), I have a reading disability, I know my writing can be incoherent sometimes.</p>
<p>I have images, I want the corresponding map from openstreetmap with buildings, roads etc. I have figured out how to do this with osmnx, I'll edit above and add a code snippet to illustrate.</p>
</div>
<div id="comment-82129-info" class="comment-info">
<span class="comment-age">(11 Oct '21, 17:38)</span> <span class="comment-user userinfo">oliver</span>
</div>
</div>
<span id="82155"></span>
<div id="comment-82155" class="comment">
<div id="post-82155-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is this for a static image or for a slippy map? What output formats do you want? (Basically, what are you actually hoping to get out of this?)</p>
<p>Are you using your own aerial imagery or another provider's?</p>
</div>
<div id="comment-82155-info" class="comment-info">
<span class="comment-age">(13 Oct '21, 19:44)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="82161"></span>
<div id="comment-82161" class="comment">
<div id="post-82161-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a> Hi, thanks, it's a static image, our (non-profits) own aerial imagery. I am attaching what I did with matplotlib above</p>
</div>
<div id="comment-82161-info" class="comment-info">
<span class="comment-age">(14 Oct '21, 05:28)</span> <span class="comment-user userinfo">oliver</span>
</div>
</div>
</div>
<div id="comment-tools-82127" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82127-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

