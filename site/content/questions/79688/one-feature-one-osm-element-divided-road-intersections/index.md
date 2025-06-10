+++
type = "question"
title = "&quot;One feature, one OSM element&quot; &amp; divided road intersections"
description = '''https://www.openstreetmap.org/#map=19/40.71498/-74.01331 Divided roads like West Street in NYC seem to always be mapped as 2 separate one-way roads. When the divider ends, the 2 roads merge into one. I always thought this was a bit odd because it seems to contradict the &quot;one feature, one OSM element...'''
date = "2021-04-17T08:46:00Z"
lastmod = "2021-04-20T00:30:00Z"
weight = 79688
keywords = [ "divided", "traffic", "signal", "highway" ]
aliases = [ "/questions/79688" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# ["One feature, one OSM element" & divided road intersections](/questions/79688/one-feature-one-osm-element-divided-road-intersections)

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
<span id="post-79688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79688-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="https://www.openstreetmap.org/#map=19/40.71498/-74.01331">https://www.openstreetmap.org/#map=19/40.71498/-74.01331</a></p>
<p>Divided roads like West Street in NYC seem to always be mapped as 2 separate one-way roads. When the divider ends, the 2 roads merge into one. I always thought this was a bit odd because it seems to contradict the "one feature, one OSM element" rule. In the case of a road it probably doesn't matter much, but it could for traffic signals. I've been thinking about how navigation software determines the best route to the destination. If it counts the traffic lights along the route, having 2 intersections with a divided road, each tagged as a traffic signal, would probably cause issues. Since the divided road is only divided between intersections and not through them, shouldn't the 2 halves of the road join at a single intersection node?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-divided" rel="tag" title="see questions tagged &#39;divided&#39;">divided</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-signal" rel="tag" title="see questions tagged &#39;signal&#39;">signal</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Apr '21, 08:46</strong></p>
<img src="https://secure.gravatar.com/avatar/6203fe5d1e41fd2c3f1c1354049b3efc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tguen&#39;s gravatar image" />
<p><span>tguen</span><br />
<span class="score" title="141 reputation points">141</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tguen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79688" class="comments-container">
&#10;</div>
<div id="comment-tools-79688" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79688-form-container" class="comment-form-container">
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

<span id="79690"></span>

<div id="answer-container-79690" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79690-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tguen has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>West Street is mapped as a dual carriage way since it is physically not possible to cross from one direction lane onto the other. Neither can pedestrians easily cross from one side to the other here.</p>
<p>There are different ways of mapping traffic lights. In your example an easy approach has been chosen. To map more accurately one could set the lights only on the incoming ways and/or use <code>direction</code> tags to indicate which direction the light is valid for. You can read up on this in the wiki, which gives a lot of <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dtraffic_signals#How_to_map">different examples</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Apr '21, 10:26</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-79690" class="comments-container">
<span id="79755"></span>
<div id="comment-79755" class="comment">
<div id="post-79755-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the link. I had checked the Key:traffic_signals page but not that one. The way it's mapped seems to be an approved method, however...</p>
<p>"Add traffic signals to the common nodes in the junction. It is up to the routing software to count nearby signals as one for timing purposes."</p>
<p>This seems like a bad idea to me, but I'll bring this up in the wiki page's discussion section.</p>
</div>
<div id="comment-79755-info" class="comment-info">
<span class="comment-age">(20 Apr '21, 00:30)</span> <span class="comment-user userinfo">tguen</span>
</div>
</div>
</div>
<div id="comment-tools-79690" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79690-form-container" class="comment-form-container">
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

