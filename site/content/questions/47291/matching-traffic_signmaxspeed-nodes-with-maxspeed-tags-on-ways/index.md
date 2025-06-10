+++
type = "question"
title = "matching traffic_sign=maxspeed Nodes with maxspeed tags on Ways"
description = '''I&#x27;ve started to notice speed limit signs on the side of the road. I&#x27;ve been adding these to OSM as Nodes with the tags traffic_sign=maxspeed, maxspeed=[the speed limit], direction=[the cardinal direction the sign is facing]. Ideally, I would also like to update the maxspeed tag on the Way. However, ...'''
date = "2015-12-26T19:06:00Z"
lastmod = "2015-12-28T19:39:00Z"
weight = 47291
keywords = [ "quality_assurance" ]
aliases = [ "/questions/47291" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [matching traffic_sign=maxspeed Nodes with maxspeed tags on Ways](/questions/47291/matching-traffic_signmaxspeed-nodes-with-maxspeed-tags-on-ways)

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
<span id="post-47291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47291-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've started to notice speed limit signs on the side of the road. I've been adding these to OSM as Nodes with the tags <a href="http://wiki.openstreetmap.org/wiki/Key:traffic_sign">traffic_sign</a>=maxspeed, maxspeed=[<em>the speed limit</em>], <a href="http://wiki.openstreetmap.org/wiki/Key:direction">direction</a>=[<em>the cardinal direction the sign is facing</em>].</p>
<p>Ideally, I would also like to update the <a href="http://wiki.openstreetmap.org/wiki/Key:maxspeed">maxspeed</a> tag on the Way. However, by just looking at a single speed limit sign, I don't have enough information to update the maxspeed tag on the road. When I'm walking it is also not always practical to walk to the end of the road (or to the next speed limit sign that is different).</p>
<p>Are there any OSM analysis tools that check for maxspeed traffic_sign Nodes next to road to see if the maxspeed tag on the road matches?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-quality_assurance" rel="tag" title="see questions tagged &#39;quality_assurance&#39;">quality_assurance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Dec '15, 19:06</strong></p>
<img src="https://secure.gravatar.com/avatar/22748312961cdceb5419decc3cc5faad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Dobratz&#39;s gravatar image" />
<p><span>Peter Dobratz</span><br />
<span class="score" title="311 reputation points">311</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Dobratz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47291" class="comments-container">
&#10;</div>
<div id="comment-tools-47291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47291-form-container" class="comment-form-container">
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

<span id="47292"></span>

<div id="answer-container-47292" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47292-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>in general maxspeed -is- an attribute of the road, and while the signs themselves are not uninteresting they are relatively seldom actually mapped and as such QA based on them is problematic. In any case mapillary has automatic sign recognition and my be of some help to you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Dec '15, 22:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-47292" class="comments-container">
<span id="47302"></span>
<div id="comment-47302" class="comment">
<div id="post-47302-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The Helsinki OSM community have been mapping signs as well as applying speed limits to roads for quite while.</p>
</div>
<div id="comment-47302-info" class="comment-info">
<span class="comment-age">(28 Dec '15, 19:39)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47292" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47292-form-container" class="comment-form-container">
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

