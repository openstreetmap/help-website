+++
type = "question"
title = "Extracting bus routes as a sequence of street intersections"
description = '''Dear friends,  I have a question regarding extracting bus routes as a sequence of street intersections. I used the following query in Overpass turbo  area[&quot;name&quot;=&quot;London&quot;]; (  rel(area)[&quot;route&quot;=&quot;bus&quot;] )-&amp;gt;.routes; ( node(r.routes:&quot;stop&quot;); )-&amp;gt;.stations; .routes out meta; .stations out center qt;...'''
date = "2017-02-10T19:02:00Z"
lastmod = "2017-02-10T19:02:00Z"
weight = 54602
keywords = [ "overpass-bus", "route" ]
aliases = [ "/questions/54602" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting bus routes as a sequence of street intersections](/questions/54602/extracting-bus-routes-as-a-sequence-of-street-intersections)

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
<span id="post-54602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54602-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear friends, I have a question regarding extracting bus routes as a sequence of street intersections. I used the following query in Overpass turbo area["name"="London"]; ( rel(area)["route"="bus"] )-&gt;.routes; ( node(r.routes:"stop"); )-&gt;.stations;</p>
<p>.routes out meta; .stations out center qt;</p>
<p>To extract the bus route based on a sequence of ways. It returned each bus route as a sequence of ways. Each way was indicated as the roles "Forward or Backward or without any role". But actually when I plotted the routes in Matlab, the resulted routes is a complete mass. If there is any one who knows how to solve this problem. Thank you Eli</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-bus" rel="tag" title="see questions tagged &#39;overpass-bus&#39;">overpass-bus</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '17, 19:02</strong></p>
<img src="https://secure.gravatar.com/avatar/ea2fb719f0b12aec9969605906be82b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ElhamAHM&#39;s gravatar image" />
<p><span>ElhamAHM</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ElhamAHM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54602" class="comments-container">
&#10;</div>
<div id="comment-tools-54602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54602-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

