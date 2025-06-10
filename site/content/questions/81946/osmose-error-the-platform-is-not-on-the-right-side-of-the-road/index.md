+++
type = "question"
title = "Osmose error &quot;The platform is not on the right side of the road&quot;"
description = '''Osmose gives me relations errors &quot;The platform is not on the right side of the road&quot;. A example is linked below. How is the &quot;right&quot; side of road determined? The correct side for the platform should on the right side of the street (because we drive on the right side here in Sweden). In the linked exa...'''
date = "2021-09-25T08:08:00Z"
lastmod = "2021-09-26T08:32:00Z"
weight = 81946
keywords = [ "osmose" ]
aliases = [ "/questions/81946" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Osmose error "The platform is not on the right side of the road"](/questions/81946/osmose-error-the-platform-is-not-on-the-right-side-of-the-road)

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
<span id="post-81946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81946-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Osmose gives me relations errors "The platform is not on the right side of the road". A example is linked below.</p>
<p>How is the "right" side of road determined? The correct side for the platform should on the right side of the street (because we drive on the right side here in Sweden). In the linked example the platform is on the right correct side, because the route is from north to south.</p>
<p>I don't see why this is marked as an error. Is this a false positive error?</p>
<p><a href="https://www.openstreetmap.org/node/4922608429">https://www.openstreetmap.org/node/4922608429</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmose" rel="tag" title="see questions tagged &#39;osmose&#39;">osmose</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Sep '21, 08:08</strong></p>
<img src="https://secure.gravatar.com/avatar/7fbbe44e24bdb695025fddb0879817a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Msiipola&#39;s gravatar image" />
<p><span>Msiipola</span><br />
<span class="score" title="227 reputation points">227</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Msiipola has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Sep '21, 10:49</strong> </span></p>
</div>
</div>
<div id="comments-container-81946" class="comments-container">
&#10;</div>
<div id="comment-tools-81946" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81946-form-container" class="comment-form-container">
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

<span id="81958"></span>

<div id="answer-container-81958" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81958-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Msiipola has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>hej Msiipola.</p>
<p>The platforms need to be added to the relation <a href="https://wiki.openstreetmap.org/wiki/Buses#Adding_bus_stops_to_the_relation">in the order in which the bus stops at them</a>. In this relation they are ordered south to north, i.e. in opposite direction of the bus traveling and the road segments. You need to reverse them to be in line with the Public Transport Version 2 scheme.</p>
<p>One more thing. The rout claims to run <code>from=Skinnskatteberg</code> <code>via=Köping;Kungsör</code> <code>to=Eskilstuna</code>. Yet the route ends in Köping. Is the route just not completely mapped yet or are the tags not correct?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '21, 19:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-81958" class="comments-container">
<span id="81960"></span>
<div id="comment-81960" class="comment">
<div id="post-81960-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer!</p>
<p>I'm new on osm editing, and these bus route relations have been mysterious to me. I understand that I have to add all the way segments, but I have never understood how the bus stops and platforms should be added.</p>
<p>Maybe the concept of bus route relations is explained in the Wiki, I have searched, but didn't find anything useful (for me).</p>
</div>
<div id="comment-81960-info" class="comment-info">
<span class="comment-age">(26 Sep '21, 07:20)</span> <span class="comment-user userinfo">Msiipola</span>
</div>
</div>
<span id="81962"></span>
<div id="comment-81962" class="comment">
<div id="post-81962-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have linked to the relevant Wiki page in my answer. The step by step guide there is quite comprehensive.</p>
<p>Public transport route editing is not so simple as you have discovered yourself. Better first get familiar with relation editing in general and routes in particular before starting mapping in that area.</p>
<p>You already got almost 1000 edits and you are using JOSM. I wouldn't call that "new". :-)</p>
</div>
<div id="comment-81962-info" class="comment-info">
<span class="comment-age">(26 Sep '21, 08:32)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-81958" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81958-form-container" class="comment-form-container">
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

