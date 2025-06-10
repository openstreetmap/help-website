+++
type = "question"
title = "How to handle overlapping markers in a slippy map?"
description = '''Hello  I am displaying business on open street map. There are some businesses with same latitude and longitude. That is why some marker of business which have same lat and long are going to be overlapping with each other. In google map API there is spidered library through which we can handle this i...'''
date = "2013-07-26T04:32:00Z"
lastmod = "2013-07-29T07:23:00Z"
weight = 24588
keywords = [ "leaflet", "overlapping", "openlayers", "markers", "slippymap" ]
aliases = [ "/questions/24588" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to handle overlapping markers in a slippy map?](/questions/24588/how-to-handle-overlapping-markers-in-a-slippy-map)

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
<span id="post-24588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24588-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>I am displaying business on open street map. There are some businesses with same latitude and longitude. That is why some marker of business which have same lat and long are going to be overlapping with each other. In google map API there is spidered library through which we can handle this issue. Is there any solution for this issue in OSM ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-overlapping" rel="tag" title="see questions tagged &#39;overlapping&#39;">overlapping</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-markers" rel="tag" title="see questions tagged &#39;markers&#39;">markers</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jul '13, 04:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a9c5624c21474b043e8007d8724d67f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Saeed&#39;s gravatar image" />
<p><span>Saeed</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Saeed has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '13, 16:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-24588" class="comments-container">
&#10;</div>
<div id="comment-tools-24588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24588-form-container" class="comment-form-container">
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

<span id="24590"></span>

<div id="answer-container-24590" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24590-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-24590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That depends on your current setup which you didn't tell us. <a href="http://leafletjs.com/">Leaflet</a> has a really nice plugin called <a href="http://github.com/Leaflet/Leaflet.markercluster">MarkerCluster</a> (<a href="http://leaflet.github.io/Leaflet.markercluster/example/marker-clustering-realworld.388.html">example</a>) which makes it easy to handle lots of (overlapping) markers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '13, 06:33</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-24590" class="comments-container">
<span id="24667"></span>
<div id="comment-24667" class="comment">
<div id="post-24667-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I am using OpenLayers.js libaray. for example just like <a href="http://openlayers.org/dev/examples/markers.html">http://openlayers.org/dev/examples/markers.html</a></p>
</div>
<div id="comment-24667-info" class="comment-info">
<span class="comment-age">(29 Jul '13, 06:25)</span> <span class="comment-user userinfo">Saeed</span>
</div>
</div>
<span id="24672"></span>
<div id="comment-24672" class="comment">
<div id="post-24672-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There seems to be a similar plugin for OpenLayers described as <a href="http://acuriousanimal.com/blog/2012/08/19/animated-marker-cluster-strategy-for-openlayers/">AnimatedCluster strategy for OpenLayers</a> which is designed similar to the Leaflet plugin.</p>
</div>
<div id="comment-24672-info" class="comment-info">
<span class="comment-age">(29 Jul '13, 07:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24590-form-container" class="comment-form-container">
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

