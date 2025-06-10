+++
type = "question"
title = "Scanned Maps and OpenLayers"
description = '''I&#x27;ve scanned an old map from around 1912 and created a tile set. The set contains tiles for zoomlevels 11-16 and covers only a small area. When using it with OpenLayers I get error messages in the log for the not coverd parts around the map – not suprising but not necessary. So how to tell OpenLayer...'''
date = "2013-08-15T13:21:00Z"
lastmod = "2013-08-20T20:54:00Z"
weight = 25419
keywords = [ "tiles", "scanned" ]
aliases = [ "/questions/25419" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Scanned Maps and OpenLayers](/questions/25419/scanned-maps-and-openlayers)

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
<span id="post-25419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25419-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-25419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've scanned an old map from around 1912 and created a tile set. The set contains tiles for zoomlevels 11-16 and covers only a small area. When using it with OpenLayers I get error messages in the log for the not coverd parts around the map – not suprising but not necessary.</p>
<p>So how to tell OpenLayers for wich area tiles should be available and for which not. Same with the zoom levels. Setting numZoomLevels to 6 makes the Layer available for level 1-6 but how to to that for 11 to 16?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-scanned" rel="tag" title="see questions tagged &#39;scanned&#39;">scanned</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Aug '13, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef3a3c25492438c9f0e5a548a36fa07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ogmios&#39;s gravatar image" />
<p><span>Ogmios</span><br />
<span class="score" title="766 reputation points">766</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ogmios has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-25419" class="comments-container">
&#10;</div>
<div id="comment-tools-25419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25419-form-container" class="comment-form-container">
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

<span id="25441"></span>

<div id="answer-container-25441" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25441-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Set (max|restricted)Extent on the map, see <a href="http://dev.openlayers.org/releases/OpenLayers-2.13.1/doc/apidocs/files/OpenLayers/Map-js.html#OpenLayers.Map.restrictedExtent">http://dev.openlayers.org/releases/OpenLayers-2.13.1/doc/apidocs/files/OpenLayers/Map-js.html#OpenLayers.Map.restrictedExtent</a> . Experiment with those, I don't know which one you'd need.</p>
<p>For the zoom level restrictions see the example from openlayers. <a href="http://dev.openlayers.org/releases/OpenLayers-2.13.1/examples/bing-tiles-restrictedzoom.html">http://dev.openlayers.org/releases/OpenLayers-2.13.1/examples/bing-tiles-restrictedzoom.html</a></p>
<p>Generally those examples are a very good source of information and guidance on how to do things.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '13, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-25441" class="comments-container">
<span id="25442"></span>
<div id="comment-25442" class="comment">
<div id="post-25442-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The example doesnt fit. With numZoomLevels i can Use zoom level 1-5 not 11-16 as I want.</p>
</div>
<div id="comment-25442-info" class="comment-info">
<span class="comment-age">(15 Aug '13, 15:38)</span> <span class="comment-user userinfo">Ogmios</span>
</div>
</div>
<span id="25445"></span>
<div id="comment-25445" class="comment">
<div id="post-25445-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Whats with the other examples tagged zoom? <a href="http://openlayers.org/dev/examples/?q=zoom">http://openlayers.org/dev/examples/?q=zoom</a> . I'd guess you have to play around with the <code>scales</code> parameter.</p>
</div>
<div id="comment-25445-info" class="comment-info">
<span class="comment-age">(15 Aug '13, 16:02)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="25611"></span>
<div id="comment-25611" class="comment">
<div id="post-25611-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I did but I can't get it working – at least not completely. I can add it as a whole layer and hide the error-tiles via css, at the moment thats the best way. But I can't get it to show the layer only within the given borders and especially not limited to the given zoom levels. That seems to be much easyer with leaflet. But I'm not an experienced web developer so It's very likely that I'm doing something completely wrong.</p>
</div>
<div id="comment-25611-info" class="comment-info">
<span class="comment-age">(20 Aug '13, 20:54)</span> <span class="comment-user userinfo">Ogmios</span>
</div>
</div>
</div>
<div id="comment-tools-25441" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25441-form-container" class="comment-form-container">
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

