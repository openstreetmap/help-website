+++
type = "question"
title = "thousands of markers, pop-up on click"
description = '''I&#x27;m looking to use openstreetmap. I&#x27;m wrting a program in java, with most likely the sprintboot framework and I will be using the OpenStreetMap API. I have a database with roughly 6000 locations(consisting of longitude and latitude coordinates) at which species of animals were observed. I would like...'''
date = "2021-02-22T10:43:00Z"
lastmod = "2021-02-22T12:06:00Z"
weight = 78982
keywords = [ "information", "popup", "markers" ]
aliases = [ "/questions/78982" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [thousands of markers, pop-up on click](/questions/78982/thousands-of-markers-pop-up-on-click)

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
<span id="post-78982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78982-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking to use openstreetmap. I'm wrting a program in java, with most likely the sprintboot framework and I will be using the OpenStreetMap API. I have a database with roughly 6000 locations(consisting of longitude and latitude coordinates) at which species of animals were observed. I would like to plot all these locations and if a user click a marker, I want to show additional information, maybe in a pop-up box (location name, species, date, etc.). Is this all possible with OpenStreetMap?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-information" rel="tag" title="see questions tagged &#39;information&#39;">information</span> <span class="post-tag tag-link-popup" rel="tag" title="see questions tagged &#39;popup&#39;">popup</span> <span class="post-tag tag-link-markers" rel="tag" title="see questions tagged &#39;markers&#39;">markers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '21, 10:43</strong></p>
<img src="https://secure.gravatar.com/avatar/7fb27608b60c3cb650b676b2348dc6c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mapijs&#39;s gravatar image" />
<p><span>mapijs</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mapijs has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78982" class="comments-container">
&#10;</div>
<div id="comment-tools-78982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78982-form-container" class="comment-form-container">
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

<span id="78986"></span>

<div id="answer-container-78986" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78986-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This has nothing to do with OpenStreetMap (which you would only use as a background map). If this were a web project I'd say you need some sort of clustering, WMS or vectortile technology for the browser to handle that number of elements but if you do it in Java it might be possible to actually show all locations. You will want to use some sort of library so that you don't need to reinvent the wheel. Check out <a href="https://wiki.openstreetmap.org/wiki/JMapViewer">https://wiki.openstreetmap.org/wiki/JMapViewer</a> (including the alternative links at the bottom).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '21, 12:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78986" class="comments-container">
&#10;</div>
<div id="comment-tools-78986" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78986-form-container" class="comment-form-container">
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

