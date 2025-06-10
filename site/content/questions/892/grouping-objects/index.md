+++
type = "question"
title = "Grouping objects"
description = '''What is the philosophy on map objects? For example, I realized that a local river in a place where I live is split into couple of parts. The river is about 50 km long and it has some 5-10 parts, I did not count them exactly. Can I join these parts into a single entity. I guess there are not tag conf...'''
date = "2010-09-21T16:58:00Z"
lastmod = "2010-09-21T17:19:00Z"
weight = 892
keywords = [ "objects", "grouping", "tags" ]
aliases = [ "/questions/892" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Grouping objects](/questions/892/grouping-objects)

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
<span id="post-892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-892-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the philosophy on map objects? For example, I realized that a local river in a place where I live is split into couple of parts. The river is about 50 km long and it has some 5-10 parts, I did not count them exactly. Can I join these parts into a single entity. I guess there are not tag conflicts between those parts. The reason I am asking is following - it would be nice to have rivers, roads and other entities as single entities, so that they could be nicely linked from somewhere else (e.g. relevant Wikipedia page).</p>
<p>Given there were tag conflicts between different parts of one geographical object (e.g. maximum allowed speed on a road) - is there a way to group such parts into higher type of object?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-objects" rel="tag" title="see questions tagged &#39;objects&#39;">objects</span> <span class="post-tag tag-link-grouping" rel="tag" title="see questions tagged &#39;grouping&#39;">grouping</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '10, 16:58</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-892" class="comments-container">
&#10;</div>
<div id="comment-tools-892" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-892-form-container" class="comment-form-container">
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

<span id="893"></span>

<div id="answer-container-893" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-893-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kozuch has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="http://wiki.openstreetmap.org/wiki/API_v0.6">API</a> limits the number of nodes a single way can have to 2.000 (this has been introduced with <a href="http://wiki.openstreetmap.org/wiki/API_changes_between_v0.5_and_v0.6#Ways">API version 0.6</a>). Therefore you probably won't be able to join a long river to one single way.</p>
<p>There seems to be also a rather old <a href="http://wiki.openstreetmap.org/wiki/Relations/Proposed/Collected_Ways">proposal</a> for grouping streets, rivers, railways etc. with the help of a <a href="http://wiki.openstreetmap.org/wiki/Relations">relation</a>. A newer one for rivers can be found <a href="http://wiki.openstreetmap.org/wiki/Relations/Proposed/Waterway">here</a> or just take a look at this <a href="http://wiki.openstreetmap.org/wiki/Relations#Composition_and_sectioning_of_ways_and_tags">list</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '10, 17:12</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Sep '10, 17:21</strong> </span></p>
</div>
</div>
<div id="comments-container-893" class="comments-container">
&#10;</div>
<div id="comment-tools-893" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-893-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="894"></span>

<div id="answer-container-894" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-894-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For your example, the ways and polygons of a river may be placed into a <a href="http://wiki.openstreetmap.org/wiki/Relations/Proposed/Collected_Ways">Collected Way</a> relation to indicate that the river is composed of those separate parts.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '10, 17:19</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-894" class="comments-container">
&#10;</div>
<div id="comment-tools-894" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-894-form-container" class="comment-form-container">
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

