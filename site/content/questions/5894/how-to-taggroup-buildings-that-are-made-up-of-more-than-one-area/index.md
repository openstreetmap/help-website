+++
type = "question"
title = "How to tag/group buildings that are made up of more than one area"
description = '''I&#x27;ve been tracing buildings using separate areas for different roof levels as recommended on the wiki. How should I go about tagging them and signifying that they belong to the same structure? Here&#x27;s an example:  If I were to just paste the same tags onto each shape, it would look like there were mu...'''
date = "2011-06-20T00:43:00Z"
lastmod = "2021-04-22T17:31:00Z"
weight = 5894
keywords = [ "buildings", "relations", "tagging", "grouping" ]
aliases = [ "/questions/5894" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag/group buildings that are made up of more than one area](/questions/5894/how-to-taggroup-buildings-that-are-made-up-of-more-than-one-area)

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
<span id="post-5894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5894-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been tracing buildings using separate areas for different roof levels as recommended <a href="http://wiki.openstreetmap.org/wiki/Key:building">on the wiki</a>.</p>
<p>How should I go about tagging them and signifying that they belong to the same structure?</p>
<p><strong>Here's an example:</strong></p>
<p><img src="http://gyazo.com/3ea52159fc22c35b7077892ab1eaca77.png" alt="alt text" /></p>
<p>If I were to just paste the same tags onto each shape, it would look like there were multiples of the same building. What do I do? Should I be using some kind of relation?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-grouping" rel="tag" title="see questions tagged &#39;grouping&#39;">grouping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jun '11, 00:43</strong></p>
<img src="https://secure.gravatar.com/avatar/d35ac2d7ba52cccf2e2e41a5cf87c654?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sekai&#39;s gravatar image" />
<p><span>Sekai</span><br />
<span class="score" title="291 reputation points">291</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sekai has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jun '11, 00:44</strong> </span></p>
</div>
</div>
<div id="comments-container-5894" class="comments-container">
&#10;</div>
<div id="comment-tools-5894" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5894-form-container" class="comment-form-container">
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

<span id="5895"></span>

<div id="answer-container-5895" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5895-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-5895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sekai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That recommendation on the wiki is not necessarily widely accepted. I can see the interest in rendering different roof levels from those with an interest in 3-D rendering.<br />
</p>
<p>It is acceptable to draw a single outline for the collective building. Where it is attached you could reasonably call it one building, and tag it as such.<br />
</p>
<p>If you wish to show more detail, including the multiple roof levels, a multipolygon relation is the way to go.<br />
</p>
<ul>
<li>Draw the multiple, adjacent polygons.</li>
<li>Create a relation, type=multipolygon</li>
<li>building=yes</li>
<li>addr:housenumber=123</li>
<li>addr:street=Sesame Street</li>
<li>name=as appropriate</li>
<li>amenity=university; or other as appropriate</li>
<li>make each individual building outline a member of the relation, with role=outer</li>
</ul>
<p>That should do it.</p>
<p>Those interested in 3D rendering will probably suggest tags for the various roof levels as well. <a href="http://wiki.openstreetmap.org/wiki/Key:building:levels">Incomplete or contentious examples may be seen here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '11, 01:11</strong></p>
<img src="https://secure.gravatar.com/avatar/d90ea04df82d77f534659f08894dd889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Weait&#39;s gravatar image" />
<p><span>Richard Weait</span><br />
<span class="score" title="3044 reputation points"><span>3.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="34 badges"><span class="silver">●</span><span class="badgecount">34</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Weait has 8 accepted answers">17%</span> </br></br></p>
</div>
</div>
<div id="comments-container-5895" class="comments-container">
<span id="5907"></span>
<div id="comment-5907" class="comment">
<div id="post-5907-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the clear explanation! Am I correct in thinking that only the relation should be tagged and not the individual polygons? (as long as the tag relates to the building as a whole)</p>
</div>
<div id="comment-5907-info" class="comment-info">
<span class="comment-age">(20 Jun '11, 18:34)</span> <span class="comment-user userinfo">Sekai</span>
</div>
</div>
<span id="5908"></span>
<div id="comment-5908" class="comment">
<div id="post-5908-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, you do not need the tags on the building ways if you have them on the relation.</p>
</div>
<div id="comment-5908-info" class="comment-info">
<span class="comment-age">(20 Jun '11, 19:10)</span> <span class="comment-user userinfo">Gnonthgol ♦</span>
</div>
</div>
</div>
<div id="comment-tools-5895" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5895-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79812"></span>

<div id="answer-container-79812" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79812-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This multipolygon relation would be invalid because the outer rings must not share paths. See <a href="https://gis.stackexchange.com/questions/298307/invalid-multipolygon-of-valid-individual-polygons/298312">https://gis.stackexchange.com/questions/298307/invalid-multipolygon-of-valid-individual-polygons/298312</a></p>
<p>Map the building accordingly <a href="https://wiki.openstreetmap.org/wiki/Simple_3D_Buildings">https://wiki.openstreetmap.org/wiki/Simple_3D_Buildings</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '21, 17:31</strong></p>
<img src="https://secure.gravatar.com/avatar/3234045ddb86d06651c5e8046c1caa7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Robhubi&#39;s gravatar image" />
<p><span>Robhubi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Robhubi has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-79812" class="comments-container">
&#10;</div>
<div id="comment-tools-79812" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79812-form-container" class="comment-form-container">
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

