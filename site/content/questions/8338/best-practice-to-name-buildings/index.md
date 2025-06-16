+++
type = "question"
title = "Best-practice to name buildings"
description = '''Hi, I am a newbie in OSM and started to name some public buildings (eg. Townhall, Supermarkets etc.) in my home town. I tried it in two different ways  1. I draw the building and added some key tags to that drawing eg. building, operator, shop  2. I only take a point from the list (eg. Supermarket) ...'''
date = "2011-10-07T16:51:00Z"
lastmod = "2013-09-10T17:19:00Z"
weight = 8338
keywords = [ "building", "best-practice", "name" ]
aliases = [ "/questions/8338" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Best-practice to name buildings](/questions/8338/best-practice-to-name-buildings)

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
<span id="post-8338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8338-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am a newbie in OSM and started to name some public buildings (eg. Townhall, Supermarkets etc.) in my home town. I tried it in two different ways 1. I draw the building and added some key tags to that drawing eg. building, operator, shop 2. I only take a point from the list (eg. Supermarket) and place this point into my drawing of the building and add the key tags eg. addr., name, shop</p>
<p>What is recommended, 1st, 2nd or both?</p>
<p>thx thomas</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-best-practice" rel="tag" title="see questions tagged &#39;best-practice&#39;">best-practice</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '11, 16:51</strong></p>
<img src="https://secure.gravatar.com/avatar/2fcf54e7ebb710bcec94ed6e1f38fa92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlenhard&#39;s gravatar image" />
<p><span>tlenhard</span><br />
<span class="score" title="60 reputation points">60</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlenhard has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8338" class="comments-container">
<span id="26257"></span>
<div id="comment-26257" class="comment">
<div id="post-26257-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here's another more detailed explaination given to another similar question: <a href="/questions/22962/should-i-use-pois-or-areas-to-identify-shops">https://help.openstreetmap.org/questions/22962/should-i-use-pois-or-areas-to-identify-shops</a></p>
</div>
<div id="comment-26257-info" class="comment-info">
<span class="comment-age">(10 Sep '13, 17:19)</span> <span class="comment-user userinfo">MagicFab</span>
</div>
</div>
</div>
<div id="comment-tools-8338" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8338-form-container" class="comment-form-container">
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

<span id="8345"></span>

<div id="answer-container-8345" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8345-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-8345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A common style of mapping is to add tags to the building outline if they apply to the entire building, but to place a node within the building if the feature does not use the whole building (e.g. if there are multiple shops within the same building).</p>
<p>You <a href="https://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element">should avoid creating duplicates</a>, so choose either a node or tags on the building outline, but not both.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '11, 19:30</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Oct '11, 19:33</strong> </span></p>
</div>
</div>
<div id="comments-container-8345" class="comments-container">
&#10;</div>
<div id="comment-tools-8345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8345-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8339"></span>

<div id="answer-container-8339" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8339-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-8339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally, people map objects as points until they have better sources which allow them to map them as areas (buildings in your examples). There is also a clear guideline <a href="https://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element">in the wiki</a> which suggests you shouldn't use both.</p>
<p>So if you can map something as an area, the 1st method you mention is best, but if you can't the 2nd is still better than neither. Just try and avoid both.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '11, 17:27</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-8339" class="comments-container">
&#10;</div>
<div id="comment-tools-8339" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8339-form-container" class="comment-form-container">
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

