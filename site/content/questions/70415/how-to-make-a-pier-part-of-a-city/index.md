+++
type = "question"
title = "How to make a pier part of a city?"
description = '''I apologize; I&#x27;m new and not really sure how to fix this.  https://www.openstreetmap.org/search?query=pacifica%20pier#map=18/37.63347/-122.49575  For some reason, this pier is not counting as part of the city beyond the city line. I&#x27;m guessing it has to do with the city line being on the shore, but ...'''
date = "2019-08-18T21:59:00Z"
lastmod = "2019-08-19T23:33:00Z"
weight = 70415
keywords = [ "city", "pier" ]
aliases = [ "/questions/70415" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to make a pier part of a city?](/questions/70415/how-to-make-a-pier-part-of-a-city)

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
<span id="post-70415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70415-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I apologize; I'm new and not really sure how to fix this.</p>
<p><a href="https://www.openstreetmap.org/search?query=pacifica%20pier#map=18/37.63347/-122.49575">https://www.openstreetmap.org/search?query=pacifica%20pier#map=18/37.63347/-122.49575</a></p>
<p>For some reason, this pier is not counting as part of the city beyond the city line. I'm guessing it has to do with the city line being on the shore, but I'm not sure how I can just include the pier in that instead of drawing around the pier to include it. I tried looking at how San Francisco included its piers, but I couldn't find their city line by the piers. (I guess it's somewhere in the bay?)</p>
<p>If anyone could fix this the proper way, or at least direct me how to fix it, I'd greatly appreciate it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-pier" rel="tag" title="see questions tagged &#39;pier&#39;">pier</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '19, 21:59</strong></p>
<img src="https://secure.gravatar.com/avatar/14fd3d6ee76d2bd3b959eae051fcb6dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BrittlesSkittles&#39;s gravatar image" />
<p><span>BrittlesSkit...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BrittlesSkittles has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70415" class="comments-container">
<span id="70431"></span>
<div id="comment-70431" class="comment">
<div id="post-70431-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you absolutely sure it is inside the city boundary? there are plenty of entities which protrude from the boundary: <a href="https://www.openstreetmap.org/way/8939633#map=17/37.63098/-122.47229">https://www.openstreetmap.org/way/8939633#map=17/37.63098/-122.47229</a></p>
</div>
<div id="comment-70431-info" class="comment-info">
<span class="comment-age">(19 Aug '19, 23:33)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-70415" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70415-form-container" class="comment-form-container">
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

<span id="70420"></span>

<div id="answer-container-70420" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70420-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <a href="https://wiki.openstreetmap.org/wiki/Relation:boundary">https://wiki.openstreetmap.org/wiki/Relation:boundary</a> A coastal town border can have 2 admin relations. One for the Land area where the border is the coastline, and one for the real boundary which is usually offshore. My state has not yet legally established official offshore town boundaries (they say they are working on it) so we just put them out there a ways. I think the state boundary is 12 miles offshore. Checking your link it looks like the Pacifica city border is set up as an area instead of a boundary relation. And its from a 2008 TIGER import so probably not accurate. I have to go to sleep right now or I would fix it. Maybe someone could find a state GIS border file just to check accuracy.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '19, 05:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a69c47928edc8d3686d5236d45f1f146?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rassilon&#39;s gravatar image" />
<p><span>Rassilon</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rassilon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70420" class="comments-container">
&#10;</div>
<div id="comment-tools-70420" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70420-form-container" class="comment-form-container">
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

