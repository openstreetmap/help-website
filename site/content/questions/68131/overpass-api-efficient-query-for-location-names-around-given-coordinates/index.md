+++
type = "question"
title = "Overpass API: efficient query for location names around given coordinates"
description = '''Hi there, currently I&#x27;m searching for 4 types of features along a certain path (e.g. a point every 20 meters on a given track). I want to query for location names (e.g. mountains, rivers, huts, cities) around these coordinates. Currently my queries look like this: [out:json][timeout:30]; (  node(aro...'''
date = "2019-02-24T20:35:00Z"
lastmod = "2019-02-25T16:30:00Z"
weight = 68131
keywords = [ "overpass", "osm", "locations", "query" ]
aliases = [ "/questions/68131" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: efficient query for location names around given coordinates](/questions/68131/overpass-api-efficient-query-for-location-names-around-given-coordinates)

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
<span id="post-68131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68131-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>currently I'm searching for 4 types of features along a certain path (e.g. a point every 20 meters on a given track). I want to query for location names (e.g. mountains, rivers, huts, cities) around these coordinates.</p>
<p>Currently my queries look like this:</p>
<pre><code>[out:json][timeout:30];
(
 node(around:50,46.512,7.827) [&quot;natural&quot;];
 node(around:50,46.512,7.827) [&quot;highway&quot;];
 node(around:1500,46.512,7.827) [&quot;place&quot;];
 node(around:50,46.512,7.827) [&quot;tourism&quot;];
&#10; node(around:50,46.512,7.827) [&quot;natural&quot;];
 node(around:50,46.512,7.827) [&quot;highway&quot;];
 node(around:1500,46.512,7.827) [&quot;place&quot;];
 node(around:50,46.512,7.827) [&quot;tourism&quot;];
); 
out body;</code></pre>
<p>The block inside (4 types) is repeated for each coordinate.</p>
<p>Because I'm querying several hundred coordinates for features at once: Is there a more efficient way doing this? Or can I combine all the queries around 50 meters for "natural", "highway" and "tourism"?</p>
<p>Thank you! Jens</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-locations" rel="tag" title="see questions tagged &#39;locations&#39;">locations</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '19, 20:35</strong></p>
<img src="https://secure.gravatar.com/avatar/b3c6b0ce539881c7f94758a2f63c5541?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lukey78&#39;s gravatar image" />
<p><span>Lukey78</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lukey78 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '19, 20:40</strong> </span></p>
</div>
</div>
<div id="comments-container-68131" class="comments-container">
<span id="68143"></span>
<div id="comment-68143" class="comment">
<div id="post-68143-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Passing the track as a linestring to around might be an improvement, see <a href="https://help.openstreetmap.org/questions/65796/querying-the-osm-data-for-peaks-or-other-features-which-are-nearby-a-gpx-track/65904">https://help.openstreetmap.org/questions/65796/querying-the-osm-data-for-peaks-or-other-features-which-are-nearby-a-gpx-track/65904</a></p>
</div>
<div id="comment-68143-info" class="comment-info">
<span class="comment-age">(25 Feb '19, 16:30)</span> <span class="comment-user userinfo">ikonor</span>
</div>
</div>
</div>
<div id="comment-tools-68131" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68131-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

