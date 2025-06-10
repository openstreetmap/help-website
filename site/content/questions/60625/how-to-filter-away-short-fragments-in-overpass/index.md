+++
type = "question"
title = "How to filter away short fragments in Overpass?"
description = '''I want to show all long stretches of cycleway in a certain area, as to do some quality checks. However, I don&#x27;t care about the small cycleways (e.g. &amp;lt;5m length) and want to remove them from the rendering of overpass. Is this possible?'''
date = "2017-11-15T01:40:00Z"
lastmod = "2017-11-16T15:59:00Z"
weight = 60625
keywords = [ "overpass" ]
aliases = [ "/questions/60625" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter away short fragments in Overpass?](/questions/60625/how-to-filter-away-short-fragments-in-overpass)

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
<span id="post-60625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60625-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to show all long stretches of cycleway in a certain area, as to do some quality checks. However, I don't care about the small cycleways (e.g. &lt;5m length) and want to remove them from the rendering of overpass.</p>
<p>Is this possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '17, 01:40</strong></p>
<img src="https://secure.gravatar.com/avatar/5aa76ca348911cce8f3ce7337f117d46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieter%20Vander%20Vennet&#39;s gravatar image" />
<p><span>Pieter Vande...</span><br />
<span class="score" title="241 reputation points">241</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieter Vander Vennet has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-60625" class="comments-container">
&#10;</div>
<div id="comment-tools-60625" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60625-form-container" class="comment-form-container">
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

<span id="60626"></span>

<div id="answer-container-60626" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60626-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Pieter Vander Vennet has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, there is no length operator in the Overpass query language.</p>
<p>If you use JOSM you could use Overpass API to fetch just the cycleways and then use the search to find and purge the short ways. Add a tile layer showing OpenStreetMap and the visualization is similar.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '17, 02:03</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-60626" class="comments-container">
<span id="60652"></span>
<div id="comment-60652" class="comment">
<div id="post-60652-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>According to the devs, it'll be added in the next release :)</p>
</div>
<div id="comment-60652-info" class="comment-info">
<span class="comment-age">(16 Nov '17, 15:59)</span> <span class="comment-user userinfo">Pieter Vande...</span>
</div>
</div>
</div>
<div id="comment-tools-60626" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60626-form-container" class="comment-form-container">
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

