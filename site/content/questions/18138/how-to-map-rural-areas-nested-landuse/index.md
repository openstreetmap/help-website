+++
type = "question"
title = "How to map rural areas / nested landuse"
description = '''I am mapping some rural areas. Basically there are 90% farmland, on some spots farm yards and even residential areas. I would no simply make the whole area farmland and put inside the farm yards and residential areas. Is this okay? Should I go even further and put natural wood on top of this landuse...'''
date = "2012-12-01T17:55:00Z"
lastmod = "2012-12-06T15:22:00Z"
weight = 18138
keywords = [ "landuse", "mapping" ]
aliases = [ "/questions/18138" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to map rural areas / nested landuse](/questions/18138/how-to-map-rural-areas-nested-landuse)

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
<span id="post-18138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18138-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am mapping some rural areas.</p>
<p>Basically there are 90% farmland, on some spots farm yards and even residential areas.</p>
<p>I would no simply make the whole area farmland and put inside the farm yards and residential areas.</p>
<p>Is this okay?</p>
<p>Should I go even further and put natural wood on top of this landuse=farmland as they are quite small compared to the area of farmland?</p>
<p>On which point should we start to make disjunct areas of landuse and when is it okay to nest them?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '12, 17:55</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Dec '12, 17:55</strong> </span></p>
</div>
</div>
<div id="comments-container-18138" class="comments-container">
&#10;</div>
<div id="comment-tools-18138" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18138-form-container" class="comment-form-container">
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

<span id="18139"></span>

<div id="answer-container-18139" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18139-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-18139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You shouldn't stack them on top of each other. Use a <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">multipolygon</a> for the farmland, so the other landuses are holes in it. Go to <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon#Potlatch_2_example">the bottom of the page</a> for a practical example.</p>
<hr />
<p>Reply to the first comment:</p>
<p>If you have one big area of farmland and inside it are ten farmyards and twenty little patches of wood, then however you are going to map it, this requires you to draw 31 polygons. The multipolygon adds 1 (one) relation to it. One relation does not constitute a huge amount of data compared to the 31 other objects you have to map anyway.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '12, 19:59</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '12, 19:05</strong> </span></p>
</div>
</div>
<div id="comments-container-18139" class="comments-container">
<span id="18253"></span>
<div id="comment-18253" class="comment">
<div id="post-18253-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is this really necessary? I think this would create a huge amount of additional data were I do not see the use.</p>
</div>
<div id="comment-18253-info" class="comment-info">
<span class="comment-age">(06 Dec '12, 15:22)</span> <span class="comment-user userinfo">AddisMap_Ale...</span>
</div>
</div>
</div>
<div id="comment-tools-18139" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18139-form-container" class="comment-form-container">
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

