+++
type = "question"
title = "Problem render EPSG 4326"
description = '''Hi! I am using openlayers to get map with openstreetmap with projection: &#x27;EPSG:4326&#x27;, but always, In the same position I see the map badly (as you can see in the photo). I am not sure how I can solve this. '''
date = "2019-10-15T08:55:00Z"
lastmod = "2019-10-16T16:46:00Z"
weight = 71179
keywords = [ "openstreetmap", "rendering", "openlayers", "data" ]
aliases = [ "/questions/71179" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem render EPSG 4326](/questions/71179/problem-render-epsg-4326)

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
<span id="post-71179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71179-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I am using openlayers to get map with openstreetmap with projection: 'EPSG:4326', but always, In the same position I see the map badly (as you can see in the photo). I am not sure how I can solve this.</p>
<p><img src="/upfiles/openlayers.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Oct '19, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/24b1fae623982c3afb0d9eb2b76105a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marina&#39;s gravatar image" />
<p><span>Marina</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marina has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-71179" class="comments-container">
&#10;</div>
<div id="comment-tools-71179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71179-form-container" class="comment-form-container">
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

<span id="71180"></span>

<div id="answer-container-71180" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71180-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like you are displaying in epsg 4326, but using an underlying tile source that is in epsg 3857. OpenLayers is probably choosing whichever tiles require the least distortion or rescaling, and this changes based on the latitude. So your picture shows zoom level 4 tiles in the south, and zoom level 3 tiles further north.</p>
<p>The two solutions are to either display the tiles in their native projection (i.e. change display to 3857) or to find a tile source in your display projection (i.e. tiles in 4326).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '19, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-71180" class="comments-container">
<span id="71206"></span>
<div id="comment-71206" class="comment">
<div id="post-71206-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>Thanks for the answer. I thought that openstreetmap has all the kinds of projection or funtions to manage them.</p>
<p>I solved it using useGeometries() function in openlayers(v 6.x), and it gives me other problems as raster render, but It allows to see the map correctly</p>
</div>
<div id="comment-71206-info" class="comment-info">
<span class="comment-age">(16 Oct '19, 16:46)</span> <span class="comment-user userinfo">Marina</span>
</div>
</div>
</div>
<div id="comment-tools-71180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71180-form-container" class="comment-form-container">
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

