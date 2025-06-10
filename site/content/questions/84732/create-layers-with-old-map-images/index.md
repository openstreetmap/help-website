+++
type = "question"
title = "Create layers with old map images"
description = '''Hello, I&#x27;m looking for a solution to put 400 old map images, as layers that can be turned on and off, on a current OSM type map background. I know how to geo-reference old map images, but I can&#x27;t find a solution to create layers with these images. I would like to know if OSM, via open layer or umap ...'''
date = "2022-06-08T09:22:00Z"
lastmod = "2022-06-08T09:45:00Z"
weight = 84732
keywords = [ "layer", "image" ]
aliases = [ "/questions/84732" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Create layers with old map images](/questions/84732/create-layers-with-old-map-images)

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
<span id="post-84732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84732-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm looking for a solution to put 400 old map images, as layers that can be turned on and off, on a current OSM type map background. I know how to geo-reference old map images, but I can't find a solution to create layers with these images. I would like to know if OSM, via open layer or umap can do this, please?</p>
<p>Thank you in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '22, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/930dcbade72f4c23920bab165928d89d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PhilBdN&#39;s gravatar image" />
<p><span>PhilBdN</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PhilBdN has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84732" class="comments-container">
&#10;</div>
<div id="comment-tools-84732" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84732-form-container" class="comment-form-container">
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

<span id="84733"></span>

<div id="answer-container-84733" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84733-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM would only be a small component in what you are doing. You would not solve your problem "with OSM" but rather "with OpenLayers" or "with Leaflet" - both of which exist independently of OSM - and OSM map tiles would just be one layer you're showing.</p>
<p>To show your georeferenced images in an OpenLayers or Leaflet map, one possible avenue is setting up a map server - utilizing e.g. the open Source products MapServer or Geoserver - which load your images and serve them as tiles, WMTS, or WMS which can then be loaded by OpenLayers or Leaflet.</p>
<p>There might be plugins for OpenLayers or Leaflet to consume georeferenced images directly, but even if there are, there's a danger of overloading the browser when you load 400 maps into it. The server solution would make the browser only load what the user currently needs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '22, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-84733" class="comments-container">
<span id="84734"></span>
<div id="comment-84734" class="comment">
<div id="post-84734-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Frederik,</p>
<p>Thank you for this detailed answer. I had some doubts about the quantity of images. I don't know if the solution is not going to be a bit oversized for this project, but I'm going to follow your advice and look at Leaflet and OpenLayers. I'll drop a little note to say what will be decided.</p>
<p>Phil</p>
</div>
<div id="comment-84734-info" class="comment-info">
<span class="comment-age">(08 Jun '22, 09:45)</span> <span class="comment-user userinfo">PhilBdN</span>
</div>
</div>
</div>
<div id="comment-tools-84733" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84733-form-container" class="comment-form-container">
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

