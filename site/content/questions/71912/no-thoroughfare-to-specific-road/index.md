+++
type = "question"
title = "No thoroughfare to specific road"
description = '''How can I specify that a certain road is not to be used as a thoroughfare to reach another specific road? In Norway there are signs prohibiting cars from using a road as a short-cut to another road(usually a small road through a residential area leading to a major road).  I cannot use &quot;access=design...'''
date = "2019-12-01T04:34:00Z"
lastmod = "2019-12-01T16:22:00Z"
weight = 71912
keywords = [ "thoroughfare", "no" ]
aliases = [ "/questions/71912" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [No thoroughfare to specific road](/questions/71912/no-thoroughfare-to-specific-road)

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
<span id="post-71912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71912-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I specify that a certain road is not to be used as a thoroughfare to reach another specific road? In Norway there are signs prohibiting cars from using a road as a short-cut to another road(usually a small road through a residential area leading to a major road). I cannot use "access=designated" since the road can be used for all other destinations except that specific road. I have tried to illustrate this with a drawing<img src="https://help.openstreetmap.org/upfiles/thoroughfare_CZARLmM.jpg" alt="alt text" />. A car from the bottom passes a sign indicating that it cannot not continue to the major road(in red) but is allowed to take any of the blue roads. People living in that area(past the sign) are allowed to drive onto the red road.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-thoroughfare" rel="tag" title="see questions tagged &#39;thoroughfare&#39;">thoroughfare</span> <span class="post-tag tag-link-no" rel="tag" title="see questions tagged &#39;no&#39;">no</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '19, 04:34</strong></p>
<img src="https://secure.gravatar.com/avatar/4f3e51f970b94e6dee1da86ccb30d1b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Odiz&#39;s gravatar image" />
<p><span>Odiz</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Odiz has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Dec '19, 04:36</strong> </span></p>
</div>
</div>
<div id="comments-container-71912" class="comments-container">
&#10;</div>
<div id="comment-tools-71912" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71912-form-container" class="comment-form-container">
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

<span id="71915"></span>

<div id="answer-container-71915" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71915-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-71915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Odiz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the closed tagging OSM has for this is the <a href="https://wiki.openstreetmap.org/wiki/Relation:restriction">turn restrictions</a> schema. While this can encode the relevant information it might be considered a bit of an "off label use". The description below is closest to the second example of a prohibitory restriction on the wiki page.</p>
<p>Steps:</p>
<ol>
<li>Split the road at at the sign and the relevant points where the drivers might turn onto the main road.</li>
<li>Add a <code>no_left_turn</code> restriction with: the road before the sign as <code>from</code>, the road(s) traversed to reach the main road as <code>via</code>, and the relevant portion of the main road/sliproad as <code>to</code>.</li>
<li>Add a <code>no_right_turn</code> restriction with: the road before the sign as <code>from</code>, the road(s) traversed to reach the main road as <code>via</code>, and the relevant portion of the main road/sliproad as <code>to</code>.</li>
<li>Repeat for any other approaches with the same restriction.</li>
</ol>
<p>As some might consider this to be stretching the definition of a turn restriction it might be useful to add a <a href="https://wiki.openstreetmap.org/wiki/Key:note"><code>note=*</code></a> tag to the new relations to help future mappers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '19, 11:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-71915" class="comments-container">
<span id="71918"></span>
<div id="comment-71918" class="comment">
<div id="post-71918-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Never thought of turn restrictions that way. Will give it a try and see if it works. Thanks.</p>
</div>
<div id="comment-71918-info" class="comment-info">
<span class="comment-age">(01 Dec '19, 12:27)</span> <span class="comment-user userinfo">Odiz</span>
</div>
</div>
</div>
<div id="comment-tools-71915" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71915-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71914"></span>

<div id="answer-container-71914" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71914-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First access=designation is not a thing and is always wrong, what you were thinking of is access=destination</p>
<p>Outside of using *=destination I don't see a way of exactly modelling this with the the currently available tags, as, if I understood you correctly, through traffic is actually allowed for most destinations just not to the main road.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '19, 10:43</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-71914" class="comments-container">
<span id="71916"></span>
<div id="comment-71916" class="comment">
<div id="post-71916-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think it is just about possible if you consider it a pair of overgrown turn restrictions. The required '<code>via</code>' ways are larger than you would usually expect though. I have no idea if existing software will parse it correctly.</p>
</div>
<div id="comment-71916-info" class="comment-info">
<span class="comment-age">(01 Dec '19, 11:12)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="71928"></span>
<div id="comment-71928" class="comment">
<div id="post-71928-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A dedicated 'multi-<code>from</code>' and 'multi-<code>to</code>' relation type would be better though.</p>
</div>
<div id="comment-71928-info" class="comment-info">
<span class="comment-age">(01 Dec '19, 16:22)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-71914" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71914-form-container" class="comment-form-container">
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

