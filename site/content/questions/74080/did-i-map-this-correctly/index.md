+++
type = "question"
title = "Did I map this correctly?"
description = '''Did I map the destinations correctly: destination:lanes:forward=George J. Bean Parkway|George J. Bean Parkway;Economy Parking Garage turn:lanes:backward=left|left;through (It&#x27;s a two lane, one way road)'''
date = "2020-04-10T07:12:00Z"
lastmod = "2020-04-11T15:30:00Z"
weight = 74080
keywords = [ "question" ]
aliases = [ "/questions/74080" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Did I map this correctly?](/questions/74080/did-i-map-this-correctly)

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
<span id="post-74080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74080-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Did I map the destinations correctly:</p>
<p>destination:lanes:forward=George J. Bean Parkway|George J. Bean Parkway;Economy Parking Garage turn:lanes:backward=left|left;through</p>
<p>(It's a two lane, one way road)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-question" rel="tag" title="see questions tagged &#39;question&#39;">question</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Apr '20, 07:12</strong></p>
<img src="https://secure.gravatar.com/avatar/b5868b476e46281d48855dc281357d01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Timbot4x4&#39;s gravatar image" />
<p><span>Timbot4x4</span><br />
<span class="score" title="101 reputation points">101</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Timbot4x4 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Apr '20, 18:29</strong> </span></p>
</div>
</div>
<div id="comments-container-74080" class="comments-container">
<span id="74081"></span>
<div id="comment-74081" class="comment">
<div id="post-74081-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That URL seems invalid.</p>
</div>
<div id="comment-74081-info" class="comment-info">
<span class="comment-age">(10 Apr '20, 07:30)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-74080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74080-form-container" class="comment-form-container">
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

<span id="74087"></span>

<div id="answer-container-74087" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74087-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Timbot4x4 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If it's a one-way road (oneway=yes), you do not have to use forward/backward. then the tags should be</p>
<ul>
<li>highway=...</li>
<li>lanes=2</li>
<li>destination:lanes=George J. Bean Parkway|George J. Bean Parkway;Economy Parking Garage</li>
<li>turn:lanes=left|left;through</li>
</ul>
<p>It's also weird that you used forward for the destination lanes and backward for the turn:lanes.</p>
<p>note that cycle lanes should be counted in destination:lanes and turn:lanes, but not in lanes=</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '20, 07:02</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '20, 07:02</strong> </span></p>
</div>
</div>
<div id="comments-container-74087" class="comments-container">
<span id="74088"></span>
<div id="comment-74088" class="comment">
<div id="post-74088-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Didn't notice the forward/backward part. Much better to use software with a decent validator.</p>
</div>
<div id="comment-74088-info" class="comment-info">
<span class="comment-age">(11 Apr '20, 08:37)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="74089"></span>
<div id="comment-74089" class="comment">
<div id="post-74089-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>AFAIK, there is no validator that does the lane count correctly.</p>
</div>
<div id="comment-74089-info" class="comment-info">
<span class="comment-age">(11 Apr '20, 15:30)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-74087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74087-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74086"></span>

<div id="answer-container-74086" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74086-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That seems about right <a href="https://wiki.openstreetmap.org/wiki/Lanes#Motorway_with_lanes_and_destinations">according to the wiki</a>, assuming it has a <code>lanes=2</code>tag too.</p>
<p>If you use JOSM, the <a href="https://josm.openstreetmap.de/wiki/Styles/Lane_and_Road_Attributes">lane and road attributes</a> style is quite good for checking if you've created what you intended.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '20, 20:08</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-74086" class="comments-container">
&#10;</div>
<div id="comment-tools-74086" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74086-form-container" class="comment-form-container">
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

