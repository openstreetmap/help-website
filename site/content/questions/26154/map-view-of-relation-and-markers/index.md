+++
type = "question"
title = "map view of relation and markers"
description = '''Dear OpenStreetMap users, today I need your help, cause I want to view a relation and two (or more) markers onto the same map, how can I archieve this?  relation: hanseatic city of Lübeck. marker 1: airport. marker 2: central railway station.  Thanks for your help. best regards'''
date = "2013-09-06T10:58:00Z"
lastmod = "2013-09-06T11:33:00Z"
weight = 26154
keywords = [ "map", "relation", "markers", "view" ]
aliases = [ "/questions/26154" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [map view of relation and markers](/questions/26154/map-view-of-relation-and-markers)

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
<span id="post-26154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26154-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear OpenStreetMap users,</p>
<p>today I need your help, cause I want to view a relation and two (or more) markers onto the same map, how can I archieve this?</p>
<ul>
<li>relation: <a href="http://www.openstreetmap.org/?relation=62463">hanseatic city of Lübeck</a>.</li>
<li>marker 1: <a href="http://www.openstreetmap.org/?mlon=10.714526174019&amp;mlat=53.803372409097">airport</a>.</li>
<li>marker 2: <a href="http://www.openstreetmap.org/?mlon=10.669926402531&amp;mlat=53.867539782056">central railway station</a>.</li>
</ul>
<p>Thanks for your help.</p>
<p>best regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-markers" rel="tag" title="see questions tagged &#39;markers&#39;">markers</span> <span class="post-tag tag-link-view" rel="tag" title="see questions tagged &#39;view&#39;">view</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '13, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/c4ae5b39c38e04b05bc48ba9aff2a5b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dragon&#39;s gravatar image" />
<p><span>dragon</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dragon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26154" class="comments-container">
&#10;</div>
<div id="comment-tools-26154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26154-form-container" class="comment-form-container">
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

<span id="26155"></span>

<div id="answer-container-26155" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26155-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This could be achieved with e.g. the overpass API, see query <a href="http://overpass-turbo.eu/s/YE">http://overpass-turbo.eu/s/YE</a> This is only a small step in the complete solution.</p>
<p>You could export this data as GeoJSON, and upload this in <a href="http://umap.openstreetmap.fr">http://umap.openstreetmap.fr</a> and style it there. Or you could set up your own server displaying tiles and overlaying them via Leaflet or OpenLayers</p>
<p>I realize that there are still a few hurdles to be taken, but hope this sets you on the right (or possible) track</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '13, 11:33</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-26155" class="comments-container">
&#10;</div>
<div id="comment-tools-26155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26155-form-container" class="comment-form-container">
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

