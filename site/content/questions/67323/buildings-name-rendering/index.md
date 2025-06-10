+++
type = "question"
title = "Building&#x27;s name rendering"
description = '''Hi, The building I am asking about has a shape of two plus signs merged side by side. After I added its name I expected it would appear roughly in the middle but instead, the name is shifted to the left, like it was over one of the &#x27;plus signs&#x27;. What is the reason for that? Am I missing something im...'''
date = "2018-12-22T18:53:00Z"
lastmod = "2018-12-22T23:57:00Z"
weight = 67323
keywords = [ "rendering", "name" ]
aliases = [ "/questions/67323" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Building's name rendering](/questions/67323/buildings-name-rendering)

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
<span id="post-67323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67323-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>The building I am asking about has a shape of two plus signs merged side by side. After I added its name I expected it would appear roughly in the middle but instead, the name is shifted to the left, like it was over one of the 'plus signs'. What is the reason for that? Am I missing something important?</p>
<p><a href="https://www.openstreetmap.org/#map=19/55.95024/-3.24121">https://www.openstreetmap.org/#map=19/55.95024/-3.24121</a></p>
<p>Thanks, Michal</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Dec '18, 18:53</strong></p>
<img src="https://secure.gravatar.com/avatar/cde755e8ab6fcc1c37864170c84f98db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="michau&#39;s gravatar image" />
<p><span>michau</span><br />
<span class="score" title="71 reputation points">71</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="michau has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67323" class="comments-container">
&#10;</div>
<div id="comment-tools-67323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67323-form-container" class="comment-form-container">
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

<span id="67328"></span>

<div id="answer-container-67328" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67328-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-67328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is how the Mapnik works with "interior" algorithm. It tries to find the point which is the most distant from all the borders and then adds a bit of gravity towards geometric center. I was involved in the process of changing this algorithm, because the old one had some flaws, which resulted in showing labels outside the area, which was a problem that was bugging me, because for example Lake Victoria was rendered somewhere on the ground.</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/issues/1465">https://github.com/gravitystorm/openstreetmap-carto/issues/1465</a></p>
<p>Finding centroid is not trivial task and it depends on the shape heavily. What works better on some of them, is just strange in some other cases. I have reviewed about 100 of different shapes when giving a feedback to the developer, and there was no clear winner and this algorithm was just sane enough.</p>
<p><a href="https://github.com/mapnik/mapnik/issues/3550">https://github.com/mapnik/mapnik/issues/3550</a></p>
<p><a href="https://github.com/mapnik/mapnik/pull/3780">https://github.com/mapnik/mapnik/pull/3780</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Dec '18, 23:57</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-67328" class="comments-container">
&#10;</div>
<div id="comment-tools-67328" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67328-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67325"></span>

<div id="answer-container-67325" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67325-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While I don't know how the renderer works, my guess is that it is searching for the biggest square area to place the label in. And this happens to be at the center of the western cross.</p>
<p><img src="https://help.openstreetmap.org/upfiles/osm_qFOxPAx.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Dec '18, 20:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2f19e3a960bbc861e85b69c9c13a8e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pbb&#39;s gravatar image" />
<p><span>pbb</span><br />
<span class="score" title="621 reputation points">621</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pbb has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-67325" class="comments-container">
&#10;</div>
<div id="comment-tools-67325" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67325-form-container" class="comment-form-container">
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

