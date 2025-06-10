+++
type = "question"
title = "Get all points of a street."
description = '''Hi friends! I have a address already geocoded, and i need draw entire street in the map. I think to get the first and the last point of this street and pass to GoogleDirections to calculate this route. How can i get this points or do some like that? Thanks, Andre Silva'''
date = "2012-08-07T13:05:00Z"
lastmod = "2012-08-09T09:41:00Z"
weight = 14885
keywords = [ "street", "drawing" ]
aliases = [ "/questions/14885" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Get all points of a street.](/questions/14885/get-all-points-of-a-street)

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
<span id="post-14885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14885-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi friends!</p>
<p>I have a address already geocoded, and i need draw entire street in the map. I think to get the first and the last point of this street and pass to GoogleDirections to calculate this route. How can i get this points or do some like that?</p>
<p>Thanks, Andre Silva</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-drawing" rel="tag" title="see questions tagged &#39;drawing&#39;">drawing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '12, 13:05</strong></p>
<img src="https://secure.gravatar.com/avatar/aa9f909370ea8e7a8ce33d8745ee9877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ALMSRJ&#39;s gravatar image" />
<p><span>ALMSRJ</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ALMSRJ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14885" class="comments-container">
<span id="14891"></span>
<div id="comment-14891" class="comment">
<div id="post-14891-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can i do that only with OSM? I mean, from a point, get the begining and the and of a street?</p>
</div>
<div id="comment-14891-info" class="comment-info">
<span class="comment-age">(07 Aug '12, 15:52)</span> <span class="comment-user userinfo">ALMSRJ</span>
</div>
</div>
<span id="14917"></span>
<div id="comment-14917" class="comment">
<div id="post-14917-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Here we help people using OSM, not Google....</p>
</div>
<div id="comment-14917-info" class="comment-info">
<span class="comment-age">(09 Aug '12, 09:41)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-14885" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14885-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="14906"></span>

<div id="answer-container-14906" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14906-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-14906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To highlight a street, you can use <a href="http://overpass-api.de">Overpass API</a>.</p>
<p>The link</p>
<p><a href="http://overpass-api.de/api/convert?data=%28way%5Bname~%22Im%20Tannenbusch%22%5D%2850.6%2C7.0%2C50.8%2C7.3%29%3B%3E%3B%29%3Bout+skel%3B%0D%0A&amp;target=openlayers">http://overpass-api.de/api/convert?data=(way[name~"Im Tannenbusch"](50.6,7.0,50.8,7.3);&gt;;);out skel;target=openlayers</a></p>
<p>for example, highlights the street "Im Tannenbusch" within the rough bounding box north 50.6, east 7.0, north 50.8, east 7.3.</p>
<p>The link also shows that the question about the first and last point of a street is not so simple: there are three ends to that street. Other streets may have much more endings or even none at all if the street is circular. So a search for the first and the last point cannot be more than heuristics.</p>
<p>In general, you can get the raw data for a street with a link similar to the above</p>
<p><a href="http://overpass-api.de/api/interpreter?data=%28way%5Bname~%22Im%20Tannenbusch%22%5D%2850.6%2C7.0%2C50.8%2C7.3%29%3B%3E%3B%29%3Bout%3B">http://overpass-api.de/api/interpreter?data=(way[name~"Im Tannenbusch"](50.6,7.0,50.8,7.3);&gt;;);out;</a></p>
<p>This raw data consists of the ways that comprise the street within the "way" tags. The "nd" tags correspond to the referred nodes (points). In this raw data you can look which of the first or last lines starting with "&lt;nd" within a way-tag appears only once. These ids are the nodes at all the possibly multiple ends of a street.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '12, 07:47</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-14906" class="comments-container">
&#10;</div>
<div id="comment-tools-14906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14906-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14896"></span>

<div id="answer-container-14896" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14896-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Any basic frameworks about routing with OSM data can be found in the OSM wiki about <a href="http://wiki.openstreetmap.org/wiki/Routing">Routing</a></p>
<p>But you have to define first how you will find the start and end node of a street, because one street can consist of several ways.</p>
<p>So tell us by adding a COMMENT here how you will define this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '12, 17:22</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-14896" class="comments-container">
&#10;</div>
<div id="comment-tools-14896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14896-form-container" class="comment-form-container">
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

