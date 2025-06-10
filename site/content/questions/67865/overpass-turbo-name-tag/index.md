+++
type = "question"
title = "overpass turbo name tag"
description = '''I&#x27;m trying to add just the names of parking lots to a names data set for our university. Using Overpass Turbo, I can extract a geojson file using the wizard by having it look for &quot;amenity=parking and name=&quot; This identifies the parking lots I need and I run the Overpass query and export the resulting...'''
date = "2019-02-04T19:35:00Z"
lastmod = "2019-02-09T11:02:00Z"
weight = 67865
keywords = [ "overpass-turbo", "name", "geojson", "parking" ]
aliases = [ "/questions/67865" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [overpass turbo name tag](/questions/67865/overpass-turbo-name-tag)

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
<span id="post-67865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67865-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to add just the names of parking lots to a names data set for our university. Using Overpass Turbo, I can extract a geojson file using the wizard by having it look for "amenity=parking and name=<em>" This identifies the parking lots I need and I run the Overpass query and export the resulting geojson file. When I import the geojson file into the dataset in Mapbox, it imports the parking lots as polygons, where each polygon has a tag "amenity=parking" and "name=</em>" However I'd like the parking lots to be represented only by its name in the center of the polygon. Is there a way to convert a polygon to a point in Mapbox or in the geojson file, or is there a way to have Overpass Turbo identify a lot, but only export it's name and location?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '19, 19:35</strong></p>
<img src="https://secure.gravatar.com/avatar/6f197a6bc17c8c55f68a1102707b7247?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="URcommunications&#39;s gravatar image" />
<p><span>URcommunicat...</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="URcommunications has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67865" class="comments-container">
&#10;</div>
<div id="comment-tools-67865" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67865-form-container" class="comment-form-container">
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

<span id="67869"></span>

<div id="answer-container-67869" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67869-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-67869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This outputs the centre of each parking place.</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  // query part for: “amenity=parking and name=*”
  node[&quot;amenity&quot;=&quot;parking&quot;][&quot;name&quot;]({{bbox}});
  way[&quot;amenity&quot;=&quot;parking&quot;][&quot;name&quot;]({{bbox}});
  relation[&quot;amenity&quot;=&quot;parking&quot;][&quot;name&quot;]({{bbox}});
);
// print results
out center;</code></pre>
<p>Disclaimer - not tried importing it into mapbox, apologies if this is a red herring.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '19, 23:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ba18d96cf193429ae1a16c30828ef58d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrewblack&#39;s gravatar image" />
<p><span>andrewblack</span><br />
<span class="score" title="365 reputation points">365</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrewblack has 4 accepted answers">57%</span></p>
</div>
</div>
<div id="comments-container-67869" class="comments-container">
<span id="67882"></span>
<div id="comment-67882" class="comment">
<div id="post-67882-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It worked perfectly! Thanks. Funny, I had generated almost exactly the same thing using the wizard but instead of "out center;" it had "out body;" That made all the difference. Thanks!</p>
</div>
<div id="comment-67882-info" class="comment-info">
<span class="comment-age">(05 Feb '19, 14:49)</span> <span class="comment-user userinfo">URcommunicat...</span>
</div>
</div>
<span id="67946"></span>
<div id="comment-67946" class="comment">
<div id="post-67946-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I generated this using the wizard then edited the bit at the botton. I often use "out center" a lot (UK readers note the spelling!). E.g. if I want to know where POIs are but am not interested in layout of the building.</p>
</div>
<div id="comment-67946-info" class="comment-info">
<span class="comment-age">(09 Feb '19, 11:02)</span> <span class="comment-user userinfo">andrewblack</span>
</div>
</div>
</div>
<div id="comment-tools-67869" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67869-form-container" class="comment-form-container">
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

