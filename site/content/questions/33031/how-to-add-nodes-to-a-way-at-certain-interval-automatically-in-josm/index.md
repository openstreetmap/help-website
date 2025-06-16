+++
type = "question"
title = "How to add nodes to a way at certain interval  automatically in JOSM?"
description = '''I need to get coordinates at certain interval from a way. This is only possible when there are continous nodes from a way. Now I just can put the nodes manually to a way. Is there any possibility to draw nodes/coordinates automatically at certain interval(i.e. every 10 meters) to a way?'''
date = "2014-05-09T12:21:00Z"
lastmod = "2014-05-09T13:42:00Z"
weight = 33031
keywords = [ "josm", "nodes", "automatically", "way" ]
aliases = [ "/questions/33031" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add nodes to a way at certain interval automatically in JOSM?](/questions/33031/how-to-add-nodes-to-a-way-at-certain-interval-automatically-in-josm)

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
<span id="post-33031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33031-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to get coordinates at certain interval from a way. This is only possible when there are continous nodes from a way. Now I just can put the nodes manually to a way. Is there any possibility to draw nodes/coordinates automatically at certain interval(i.e. every 10 meters) to a way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-automatically" rel="tag" title="see questions tagged &#39;automatically&#39;">automatically</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '14, 12:21</strong></p>
<img src="https://secure.gravatar.com/avatar/f2226c49b999898aead44f47532228bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lovindair&#39;s gravatar image" />
<p><span>lovindair</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lovindair has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33031" class="comments-container">
<span id="33032"></span>
<div id="comment-33032" class="comment">
<div id="post-33032-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This sounds odd. For what do you need those nodes exactly?</p>
</div>
<div id="comment-33032-info" class="comment-info">
<span class="comment-age">(09 May '14, 12:25)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33033"></span>
<div id="comment-33033" class="comment">
<div id="post-33033-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>indeed, this looks a lot like tagging/mapping for the data consumer</p>
</div>
<div id="comment-33033-info" class="comment-info">
<span class="comment-age">(09 May '14, 12:39)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="33034"></span>
<div id="comment-33034" class="comment not_top_scorer">
<div id="post-33034-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the fast answer.</p>
<p>I need actually the coordinates of ways for speed limit App, so that I can compare the coordinates from GPS with the coordinates from the road to determine the speed limit of the road. Until now, the coordinates are only available where the nodes are drawed, Thats why I want to draw nodes or coordinates at certain interval, so I can get continous info of the speed limit from the road.</p>
</div>
<div id="comment-33034-info" class="comment-info">
<span class="comment-age">(09 May '14, 13:05)</span> <span class="comment-user userinfo">lovindair</span>
</div>
</div>
<span id="33035"></span>
<div id="comment-33035" class="comment">
<div id="post-33035-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please don't change the data solely because of your app. Computing these intermediate nodes within your app is a fairly easy task and the only sensible solution. Otherwise you would pollute OSM's database with lots of unnecessary information.</p>
</div>
<div id="comment-33035-info" class="comment-info">
<span class="comment-age">(09 May '14, 13:14)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33036"></span>
<div id="comment-33036" class="comment">
<div id="post-33036-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Of course I use it offline. I will not upload my modified map to OSM database, I just ask if thers is any possibility to draw it automatically in JOSM.</p>
</div>
<div id="comment-33036-info" class="comment-info">
<span class="comment-age">(09 May '14, 13:22)</span> <span class="comment-user userinfo">lovindair</span>
</div>
</div>
<span id="33038"></span>
<div id="comment-33038" class="comment">
<div id="post-33038-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Even if you do it for your own app, in your own database, it's an insane job to do that for every road. As scai said, let de software compute the nearest (the one you are driving on) road for your current GPS position.</p>
</div>
<div id="comment-33038-info" class="comment-info">
<span class="comment-age">(09 May '14, 13:32)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-33031" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-33031-form-container" class="comment-form-container">
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

<span id="33037"></span>

<div id="answer-container-33037" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33037-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-33037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are already opensource apps that are able to evaluate maxspedd values from vector data maps and do a compare with current position when going in the field with a device gps enabled.</p>
<p>For example, have a look at <a href="https://wiki.openstreetmap.org/wiki/OsmAnd">Osmand</a></p>
<p>So your solution by creating artificial nodes (even internally and offline) sound a bit easy, but it is not a clear solution.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '14, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-33037" class="comments-container">
<span id="33040"></span>
<div id="comment-33040" class="comment">
<div id="post-33040-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks, I'll look into it.</p>
</div>
<div id="comment-33040-info" class="comment-info">
<span class="comment-age">(09 May '14, 13:42)</span> <span class="comment-user userinfo">lovindair</span>
</div>
</div>
</div>
<div id="comment-tools-33037" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33037-form-container" class="comment-form-container">
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

