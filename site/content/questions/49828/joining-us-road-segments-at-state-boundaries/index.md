+++
type = "question"
title = "Joining US Road Segments at State Boundaries"
description = '''I am attempting to generate drive time polygons that span state lines. Is there a way to join road segments that span the state boundary - e.g. how do I create a national road network whereby a rural road the crosses the NC-VA border is recognized as one road segment.'''
date = "2016-05-25T14:31:00Z"
lastmod = "2016-05-28T22:31:00Z"
weight = 49828
keywords = [ "roads", "drivetimes", "join", "drive", "road" ]
aliases = [ "/questions/49828" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Joining US Road Segments at State Boundaries](/questions/49828/joining-us-road-segments-at-state-boundaries)

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
<span id="post-49828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49828-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am attempting to generate drive time polygons that span state lines. Is there a way to join road segments that span the state boundary - e.g. how do I create a national road network whereby a rural road the crosses the NC-VA border is recognized as one road segment.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-drivetimes" rel="tag" title="see questions tagged &#39;drivetimes&#39;">drivetimes</span> <span class="post-tag tag-link-join" rel="tag" title="see questions tagged &#39;join&#39;">join</span> <span class="post-tag tag-link-drive" rel="tag" title="see questions tagged &#39;drive&#39;">drive</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '16, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/c5184f7be0a23779e60710e92a3002d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ARM2020&#39;s gravatar image" />
<p><span>ARM2020</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ARM2020 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49828" class="comments-container">
&#10;</div>
<div id="comment-tools-49828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49828-form-container" class="comment-form-container">
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

<span id="49829"></span>

<div id="answer-container-49829" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49829-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general, such roads should be connected in OSM (which just means that they share a node). There is a possibility that your data processing is somehow dropping these connections. One way this could happen is converting several OSM extracts into whatever format you are using for processing.</p>
<p>So if you are seeing many missing connections you may want to investigate whether your pipeline is setup to preserve the connections.</p>
<p>If it is only a few missing connections, check to see if the modeling is correct in the main OSM database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '16, 14:38</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-49829" class="comments-container">
<span id="49830"></span>
<div id="comment-49830" class="comment">
<div id="post-49830-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems that the roads are connected, but on different ways (i.e. sharing the connecting node, which sometimes also lies on the state border): e.g. here, the roads are obviously mapped as different types on each side of the border: <a href="http://www.openstreetmap.org/relation/224045#map=16/36.5444/-78.1401">http://www.openstreetmap.org/relation/224045#map=16/36.5444/-78.1401</a></p>
</div>
<div id="comment-49830-info" class="comment-info">
<span class="comment-age">(25 May '16, 15:57)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
<span id="49887"></span>
<div id="comment-49887" class="comment">
<div id="post-49887-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It appears on the Virginia of the example that is a state highway while on the North Carolina side, it is just a regular ol' county road. This is typical when crossing state lines. Often times when you're riding along at the state border, you'll feel quite a thunderous bump and the road will either be much better or worse depending on the side you're on.</p>
</div>
<div id="comment-49887-info" class="comment-info">
<span class="comment-age">(28 May '16, 22:31)</span> <span class="comment-user userinfo">Longhorn256</span>
</div>
</div>
</div>
<div id="comment-tools-49829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49829-form-container" class="comment-form-container">
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

