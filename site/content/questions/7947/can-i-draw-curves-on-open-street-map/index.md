+++
type = "question"
title = "Can I draw curves on Open Street Map?"
description = '''Is there any way to draw curves (e.g. Bézier curves) on Open Street Map or is straight lines the only way to draw paths?'''
date = "2011-09-16T17:25:00Z"
lastmod = "2019-03-26T20:22:00Z"
weight = 7947
keywords = [ "path", "editing" ]
aliases = [ "/questions/7947" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can I draw curves on Open Street Map?](/questions/7947/can-i-draw-curves-on-open-street-map)

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
<span id="post-7947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7947-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there any way to draw curves (e.g. <a href="http://en.wikipedia.org/wiki/B%C3%A9zier_curve">Bézier curves</a>) on Open Street Map or is straight lines the only way to draw paths?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '11, 17:25</strong></p>
<img src="https://secure.gravatar.com/avatar/b1d217a3a6e04cf4654372068beef20d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonas_&#39;s gravatar image" />
<p><span>Jonas_</span><br />
<span class="score" title="662 reputation points">662</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonas_ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Sep '11, 17:29</strong> </span></p>
</div>
</div>
<div id="comments-container-7947" class="comments-container">
&#10;</div>
<div id="comment-tools-7947" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7947-form-container" class="comment-form-container">
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

<span id="7948"></span>

<div id="answer-container-7948" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7948-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-7948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jonas_ has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The only way to draw curves in the OpenStreetMap data model is using many short straight sections. You can't draw true curves such as Béziers. This is a deliberate design choice to keep the data model as simple as possible.</p>
<p>You may be able to convert OpenStreetMap data to true curves after exporting it to a graphics or GIS package, but that would require extra work on your part.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '11, 17:31</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-7948" class="comments-container">
<span id="7950"></span>
<div id="comment-7950" class="comment">
<div id="post-7950-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Note that some renderers, for example osmarender, smoothe the angles more than mapnik, making them look curvyer.</p>
</div>
<div id="comment-7950-info" class="comment-info">
<span class="comment-age">(16 Sep '11, 18:30)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7948-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68500"></span>

<div id="answer-container-68500" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68500-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These sidewalks near my house seem to be rendered as bezier-like curves. In the ID editor, they are straight lines with right angles.</p>
<p><a href="https://www.openstreetmap.org/#map=20/44.03628/-92.46942&amp;layers=C">https://www.openstreetmap.org/#map=20/44.03628/-92.46942&amp;layers=C</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Mar '19, 20:16</strong></p>
<img src="https://secure.gravatar.com/avatar/b2507d479af955f05ee995b8d5daa6ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JHartley&#39;s gravatar image" />
<p><span>JHartley</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JHartley has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68500" class="comments-container">
<span id="68501"></span>
<div id="comment-68501" class="comment">
<div id="post-68501-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The cyclemap layer does attempt to render paths as curves. But because OSM itself does not actually support curves in the data, the renderer has to guess – which it does extremely aggressively, as your map shows.</p>
</div>
<div id="comment-68501-info" class="comment-info">
<span class="comment-age">(26 Mar '19, 20:22)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-68500" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68500-form-container" class="comment-form-container">
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

