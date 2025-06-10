+++
type = "question"
title = "seasonal lanes"
description = '''Hi, Please, how can I set a seasonal cycle lane? In my city, there are permanent cycle tracks and cycle lanes, but every Sunday and holiday, only from 7 h to 16 h, the prefecture expands the net creating temporary cycle lanes for that day. Those new lanes are delimited with transit cones over once t...'''
date = "2021-12-10T21:10:00Z"
lastmod = "2021-12-14T01:52:00Z"
weight = 82807
keywords = [ "variablelanes", "lanes", "cycle_infrastructure", "cycleway" ]
aliases = [ "/questions/82807" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [seasonal lanes](/questions/82807/seasonal-lanes)

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
<span id="post-82807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82807-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Please, how can I set a seasonal cycle lane?</p>
<p>In my city, there are permanent cycle tracks and cycle lanes, but every Sunday and holiday, only from 7 h to 16 h, the prefecture expands the net creating temporary cycle lanes for that day.</p>
<p>Those new lanes are delimited with transit cones over once there are car lanes and connect the permanent cycle lanes. They are several kilometers and many people run on their bikes only and because of those temporary lanes, so they are very important.</p>
<p>But after 16 h, the transit cones are collected and everything comes to normal until the next Sunday or holiday.</p>
<p>So, how can I set up this on the OpenStreetMap?</p>
<p>The answer could help also in those streets where some lanes are inverted in the rush hours.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-variablelanes" rel="tag" title="see questions tagged &#39;variablelanes&#39;">variablelanes</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-cycle_infrastructure" rel="tag" title="see questions tagged &#39;cycle_infrastructure&#39;">cycle_infrastructure</span> <span class="post-tag tag-link-cycleway" rel="tag" title="see questions tagged &#39;cycleway&#39;">cycleway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Dec '21, 21:10</strong></p>
<img src="https://secure.gravatar.com/avatar/2ab52f8d32547389632cbe0d05792ead?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="planilhador&#39;s gravatar image" />
<p><span>planilhador</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="planilhador has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82807" class="comments-container">
&#10;</div>
<div id="comment-tools-82807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82807-form-container" class="comment-form-container">
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

<span id="82829"></span>

<div id="answer-container-82829" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82829-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Conditional lane access.</p>
<p>Something like:</p>
<pre><code>access:lanes:forward @ 07:00-16:00 = yes|no
bicycle:lanes:forward @ 07:00-16:00 = yes|designated</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '21, 01:52</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-82829" class="comments-container">
&#10;</div>
<div id="comment-tools-82829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82829-form-container" class="comment-form-container">
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

