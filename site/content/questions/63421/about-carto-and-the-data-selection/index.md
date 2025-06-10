+++
type = "question"
title = "about carto and the data selection"
description = '''As you know, carto-css will ask questions to the database and associate the answers to appropriate css through layers. Is it possible to build a unique global layer with only one question to the database, subdivisions of the css doing the work ? or associate multiple layers to only one db question, ...'''
date = "2018-05-11T12:55:00Z"
lastmod = "2018-05-12T15:01:00Z"
weight = 63421
keywords = [ "openstreetmap-carto", "osm-carto", "carto", "postgres" ]
aliases = [ "/questions/63421" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [about carto and the data selection](/questions/63421/about-carto-and-the-data-selection)

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
<span id="post-63421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63421-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As you know, carto-css will ask questions to the database and associate the answers to appropriate css through layers.</p>
<p>Is it possible to build a unique global layer with only one question to the database, subdivisions of the css doing the work ? or associate multiple layers to only one db question, the layer being one column of the db answer ?</p>
<p>I know I can find the answer by understanding the way carto css works and then by reading the documentation and learning to use it. But if some kind people may answer, I'ld get a free we</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap-carto" rel="tag" title="see questions tagged &#39;openstreetmap-carto&#39;">openstreetmap-carto</span> <span class="post-tag tag-link-osm-carto" rel="tag" title="see questions tagged &#39;osm-carto&#39;">osm-carto</span> <span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '18, 12:55</strong></p>
<img src="https://secure.gravatar.com/avatar/1c90056dece0313061d8ce6edd94da8a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AntaC&#39;s gravatar image" />
<p><span>AntaC</span><br />
<span class="score" title="13 reputation points">13</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AntaC has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63421" class="comments-container">
&#10;</div>
<div id="comment-tools-63421" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63421-form-container" class="comment-form-container">
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

<span id="63427"></span>

<div id="answer-container-63427" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63427-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63427-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-63427-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AntaC has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The requests allow to organise the data in layers, and usually you'd like to render bridges over rivers, roads over forest,... See <a href="https://tilemill-project.github.io/tilemill/docs/guides/symbol-drawing-order/">https://tilemill-project.github.io/tilemill/docs/guides/symbol-drawing-order/</a></p>
<p>Also, if you take everything at once from the database, Im not sure how performance would be affected.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '18, 09:14</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-63427" class="comments-container">
<span id="63429"></span>
<div id="comment-63429" class="comment">
<div id="post-63429-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you !</p>
</div>
<div id="comment-63429-info" class="comment-info">
<span class="comment-age">(12 May '18, 15:01)</span> <span class="comment-user userinfo">AntaC</span>
</div>
</div>
</div>
<div id="comment-tools-63427" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63427-form-container" class="comment-form-container">
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

