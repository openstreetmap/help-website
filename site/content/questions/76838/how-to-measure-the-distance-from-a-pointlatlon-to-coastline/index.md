+++
type = "question"
title = "How to measure the distance from a point(lat,lon) to coastline"
description = '''I have a rather large dataset containing property data, and I want to find the distance from each property to the nearest coastline preferably using Python.'''
date = "2020-09-26T14:46:00Z"
lastmod = "2020-09-29T09:16:00Z"
weight = 76838
keywords = [ "property", "coastline", "sea" ]
aliases = [ "/questions/76838" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to measure the distance from a point(lat,lon) to coastline](/questions/76838/how-to-measure-the-distance-from-a-pointlatlon-to-coastline)

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
<span id="post-76838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76838-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a rather large dataset containing property data, and I want to find the distance from each property to the nearest coastline preferably using Python.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-property" rel="tag" title="see questions tagged &#39;property&#39;">property</span> <span class="post-tag tag-link-coastline" rel="tag" title="see questions tagged &#39;coastline&#39;">coastline</span> <span class="post-tag tag-link-sea" rel="tag" title="see questions tagged &#39;sea&#39;">sea</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Sep '20, 14:46</strong></p>
<img src="https://secure.gravatar.com/avatar/207c75a8f4a28e989bf866211b46b1db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sebastian&#39;s gravatar image" />
<p><span>Sebastian</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sebastian has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Sep '20, 16:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span></p>
</div>
</div>
<div id="comments-container-76838" class="comments-container">
<span id="76877"></span>
<div id="comment-76877" class="comment">
<div id="post-76877-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There has been done quite some research on finding places that have the largest distance to the nearest road/coast/settlement etc: <a href="https://en.wikipedia.org/wiki/Pole_of_inaccessibility">Pole of inaccessibility</a>. To do that you basically need to answer the same question you have. Maybe that gives you a hint on how to expand your search.</p>
</div>
<div id="comment-76877-info" class="comment-info">
<span class="comment-age">(29 Sep '20, 09:16)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-76838" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76838-form-container" class="comment-form-container">
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

<span id="76874"></span>

<div id="answer-container-76874" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76874-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This formula may help. But it can't find the nearest coast. Perhaps you could put the formula with set of coastal locations into a spread sheet along with the properties so set of distances for each property could be seen. <a href="https://en.wikipedia.org/wiki/Haversine_formula">https://en.wikipedia.org/wiki/Haversine_formula</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '20, 22:02</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-76874" class="comments-container">
&#10;</div>
<div id="comment-tools-76874" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76874-form-container" class="comment-form-container">
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

