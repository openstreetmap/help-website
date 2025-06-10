+++
type = "question"
title = "Getting segments between crossroads?"
description = '''I search on google but nothing so far, i want to make a map with colored segments between the crossroads around me. I didn&#x27;t find this on the documentation so I&#x27;m ask here, is it even possible to trace multiple colored segment on OSM? So my first step is to get all crossroads around me. The second s...'''
date = "2016-10-18T11:43:00Z"
lastmod = "2016-10-19T13:45:00Z"
weight = 52588
keywords = [ "segments" ]
aliases = [ "/questions/52588" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting segments between crossroads?](/questions/52588/getting-segments-between-crossroads)

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
<span id="post-52588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52588-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I search on google but nothing so far, i want to make a map with colored segments between the crossroads around me. I didn't find this on the documentation so I'm ask here, is it even possible to trace multiple colored segment on OSM?</p>
<p>So my first step is to get all crossroads around me.</p>
<p>The second step is to trace the segment between all this crossroads.</p>
<p>Thanks in advance for the help</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-segments" rel="tag" title="see questions tagged &#39;segments&#39;">segments</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Oct '16, 11:43</strong></p>
<img src="https://secure.gravatar.com/avatar/36f813c31ff8d8559b59f2d54bd12c74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tagazok&#39;s gravatar image" />
<p><span>tagazok</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tagazok has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52588" class="comments-container">
<span id="52591"></span>
<div id="comment-52591" class="comment">
<div id="post-52591-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>cross-posted: <a href="https://gis.stackexchange.com/questions/214587/getting-segments-between-crossroads-of-openstreetmap">https://gis.stackexchange.com/questions/214587/getting-segments-between-crossroads-of-openstreetmap</a></p>
</div>
<div id="comment-52591-info" class="comment-info">
<span class="comment-age">(18 Oct '16, 13:59)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52588-form-container" class="comment-form-container">
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

<span id="52608"></span>

<div id="answer-container-52608" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52608-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52608-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52608-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think your first step would be to get the roads. <a href="http://overpass-turbo.eu/s/jto">For example, using Overpass</a>. Then you want to split the ways at every crossroads (and possibly join ways that are split for some other reason than a crossroad). This is a pretty straightforward thing to do in GIS software. Then you will want to draw them in different colors. Depending on what you want to achieve (a static image, a worldwide always up to date service) there are very many ways to approach this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '16, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-52608" class="comments-container">
&#10;</div>
<div id="comment-tools-52608" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52608-form-container" class="comment-form-container">
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

