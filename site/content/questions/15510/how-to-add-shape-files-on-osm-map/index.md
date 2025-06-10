+++
type = "question"
title = "How to add Shape files on OSM Map"
description = '''I want to add Shape files on OSM Map. I have searched for it, but cannot find any solution. Please suggest any solution for this'''
date = "2012-08-25T14:01:00Z"
lastmod = "2012-08-26T11:47:00Z"
weight = 15510
keywords = [ "jsp" ]
aliases = [ "/questions/15510" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add Shape files on OSM Map](/questions/15510/how-to-add-shape-files-on-osm-map)

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
<span id="post-15510-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15510-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-15510-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to add Shape files on OSM Map. I have searched for it, but cannot find any solution. Please suggest any solution for this</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-jsp" rel="tag" title="see questions tagged &#39;jsp&#39;">jsp</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '12, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/4103ee989b09b034a93eac604cdbdca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Niki%20Kallurwar&#39;s gravatar image" />
<p><span>Niki Kallurwar</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Niki Kallurwar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15510" class="comments-container">
<span id="15512"></span>
<div id="comment-15512" class="comment">
<div id="post-15512-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you want to display them on top of a map or use them to add new data?</p>
</div>
<div id="comment-15512-info" class="comment-info">
<span class="comment-age">(25 Aug '12, 14:50)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="15513"></span>
<div id="comment-15513" class="comment">
<div id="post-15513-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>A bit more information about what you're trying to do here would help. Are you talking about a web map, or on a phone, or something else? What sort of rendering are you talking about - tiles, or a vector map? What sort of information do you want to show?</p>
</div>
<div id="comment-15513-info" class="comment-info">
<span class="comment-age">(25 Aug '12, 14:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="15514"></span>
<div id="comment-15514" class="comment">
<div id="post-15514-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to add shape file of India roadways on OSM web map and I want to add it as a layer map.</p>
</div>
<div id="comment-15514-info" class="comment-info">
<span class="comment-age">(26 Aug '12, 10:48)</span> <span class="comment-user userinfo">Niki Kallurwar</span>
</div>
</div>
<span id="15516"></span>
<div id="comment-15516" class="comment">
<div id="post-15516-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So you probably want to display a shapefile using OpenLayers. What about cartinus' answer?</p>
</div>
<div id="comment-15516-info" class="comment-info">
<span class="comment-age">(26 Aug '12, 11:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15510" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15510-form-container" class="comment-form-container">
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

<span id="15511"></span>

<div id="answer-container-15511" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15511-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>An OSM-map on the web is typically displayed using <a href="http://openlayers.org/">OpenLayers</a> or <a href="http://leaflet.cloudmade.com/">Leaflet</a>.</p>
<p>A quick Google search on "openlayers shapefile example" gives <a href="https://indicatrix.wordpress.com/2011/12/13/shapefiles-in-openlayers/">this blog</a> as a first hit.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '12, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Aug '12, 19:34</strong> </span></p>
</div>
</div>
<div id="comments-container-15511" class="comments-container">
&#10;</div>
<div id="comment-tools-15511" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15511-form-container" class="comment-form-container">
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

