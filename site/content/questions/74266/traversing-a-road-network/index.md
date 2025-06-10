+++
type = "question"
title = "Traversing a road network"
description = '''In my project, a driving app, I want to traverse the OSM road network as the user is driving. There&#x27;s no routing at all and I don&#x27;t need geometry. I just want to be able to display info about where the user is driving (road name and administrative area names like city, county, and state) and what th...'''
date = "2020-04-18T19:47:00Z"
lastmod = "2020-04-21T20:42:00Z"
weight = 74266
keywords = [ "network", "road" ]
aliases = [ "/questions/74266" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Traversing a road network](/questions/74266/traversing-a-road-network)

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
<span id="post-74266-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74266-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74266-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my project, a driving app, I want to traverse the OSM road network as the user is driving. There's no routing at all and I don't need geometry. I just want to be able to display info about where the user is driving (road name and administrative area names like city, county, and state) and what the max speed is for the current road segment. What's the best way to approach this without constantly reverse geocoding?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '20, 19:47</strong></p>
<img src="https://secure.gravatar.com/avatar/4413e5a84cc70727f83f6b80b47cdb16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbjb00&#39;s gravatar image" />
<p><span>jbjb00</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbjb00 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74266" class="comments-container">
&#10;</div>
<div id="comment-tools-74266" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74266-form-container" class="comment-form-container">
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

<span id="74280"></span>

<div id="answer-container-74280" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74280-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is effectively "map matching", where you take a GPS trace and work out the most likely route from it. Most routing engines, such as OSRM and Graphhopper, provide a map matching feature.</p>
<p>This does mean that you have to run an instance of a routing engine. Unfortunately, running a simple proximity search without a routing engine is less likely to work, because it won't know which road you're on at junctions or other situations where there's more than one road in the area. You could try building some logic which is "sticky" to the current road, but that's likely to be problematic in urban areas where the road network is dense, GPS reception is poor, and you might be making numerous turns.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '20, 09:31</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-74280" class="comments-container">
<span id="74319"></span>
<div id="comment-74319" class="comment">
<div id="post-74319-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the answer, Richard. Do you have any suggestions for implementing map matching in the way that I've described? An example to start with, that is. I've looked at OSRM, and it can easily provide snap-to-road functionality given a few GPS locations, but it doesn't give any administrative info or max speed, and there doesn't appear to be any way I could effectively cache results for "random" location inputs (e.g. I could drive the same road 1,000,000 times and never get the same set of GPS locations twice). I've also taken a cursory look at Graphhopper, but its map matching is buried in so much other stuff that I don't need.</p>
</div>
<div id="comment-74319-info" class="comment-info">
<span class="comment-age">(21 Apr '20, 18:18)</span> <span class="comment-user userinfo">jbjb00</span>
</div>
</div>
<span id="74320"></span>
<div id="comment-74320" class="comment">
<div id="post-74320-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Mapbox (who maintained OSRM until recently) have a "route annotator" which is designed to work with OSRM. You feed it the node ids returned from OSRM, and it supplied the OSM way properties. I don't have any experience with it but have seen reports that it works. <a href="https://github.com/mapbox/route-annotator">https://github.com/mapbox/route-annotator</a></p>
<p>For administrative areas, you <em>could</em> try doing just a simple polygon lookup - i.e. download boundary polygons and then just do a point-in-polygon lookup. This is much simpler than map matching.</p>
</div>
<div id="comment-74320-info" class="comment-info">
<span class="comment-age">(21 Apr '20, 20:42)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74280-form-container" class="comment-form-container">
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

