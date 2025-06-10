+++
type = "question"
title = "Using OSM for calculating distance in desktop application using java"
description = '''I would like make a simple desktop application that can calculate the distance between two cities given by the user. I know that there is no practical purpose for this but I would just like to build it as a programming exercise. I&#x27;m having a hard time however with finding the right documentation for...'''
date = "2016-09-25T15:04:00Z"
lastmod = "2016-09-28T18:45:00Z"
weight = 52219
keywords = [ "application", "java", "desktop" ]
aliases = [ "/questions/52219" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Using OSM for calculating distance in desktop application using java](/questions/52219/using-osm-for-calculating-distance-in-desktop-application-using-java)

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
<span id="post-52219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52219-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like make a simple desktop application that can calculate the distance between two cities given by the user. I know that there is no practical purpose for this but I would just like to build it as a programming exercise. I'm having a hard time however with finding the right documentation for this. I would like to do this through an API request and it should be street level routing.</p>
<p>Is there anybody that could help me out here by pointing me in the right direction?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-application" rel="tag" title="see questions tagged &#39;application&#39;">application</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-desktop" rel="tag" title="see questions tagged &#39;desktop&#39;">desktop</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Sep '16, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/5a5c75833d95234d8e367502f3b50049?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tezen&#39;s gravatar image" />
<p><span>Tezen</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tezen has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Sep '16, 14:37</strong> </span></p>
</div>
</div>
<div id="comments-container-52219" class="comments-container">
<span id="52253"></span>
<div id="comment-52253" class="comment">
<div id="post-52253-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please EDIT your question and tell us whether you want to have the needed routing data via online download / API request ... or via offline map files on your PC / device ... and then: do you want to know direct lien connection, or street level routing?</p>
</div>
<div id="comment-52253-info" class="comment-info">
<span class="comment-age">(27 Sep '16, 20:39)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-52219" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52219-form-container" class="comment-form-container">
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

<span id="52286"></span>

<div id="answer-container-52286" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52286-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tezen has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should have a look at the OSM wiki about <a href="https://wiki.openstreetmap.org/wiki/Routing">Routing</a> and its sub-page about <a href="https://wiki.openstreetmap.org/wiki/Routing/online_routers">online routing</a></p>
<p>Please try each online service listed there, and evaluate yourself whether the user interface comes near your aim, or that you can do some coding for your own.</p>
<p>Also pay attention to the age of each routing database ... some are outdated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '16, 18:45</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-52286" class="comments-container">
&#10;</div>
<div id="comment-tools-52286" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52286-form-container" class="comment-form-container">
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

