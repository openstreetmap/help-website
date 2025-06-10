+++
type = "question"
title = "How to generate turn by turn instructions from OSM data"
description = '''Hi, I have extracted street data from OpenStreetMap and structured the data street by street. Is there any help on how I can write a simple routing algorithm based on the extracted data to generate turn-by-turn instructions if a user chooses one street as the starting point and then another street a...'''
date = "2023-06-01T00:28:00Z"
lastmod = "2023-06-02T02:01:00Z"
weight = 87328
keywords = [ "routing" ]
aliases = [ "/questions/87328" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to generate turn by turn instructions from OSM data](/questions/87328/how-to-generate-turn-by-turn-instructions-from-osm-data)

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
<span id="post-87328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87328-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have extracted street data from OpenStreetMap and structured the data street by street. Is there any help on how I can write a simple routing algorithm based on the extracted data to generate turn-by-turn instructions if a user chooses one street as the starting point and then another street as the destination?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '23, 00:28</strong></p>
<img src="https://secure.gravatar.com/avatar/d91bc4f974e22ffeb60227442e03aafa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Segunlakata&#39;s gravatar image" />
<p><span>Segunlakata</span><br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Segunlakata has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87328" class="comments-container">
&#10;</div>
<div id="comment-tools-87328" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87328-form-container" class="comment-form-container">
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

<span id="87329"></span>

<div id="answer-container-87329" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87329-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-87329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are ready-made algortihms out there on GitHub that do what you want - check out OSRM or GraphHopper. These are sophisticated routing engines where a lot of work has gone not into making them fast but also making the instructions good - which is more difficult than you might expect! Even if you decide to write your own routing engine for educational purposes, it might make sense to have a look at how these programs generate turn instructions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '23, 08:34</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-87329" class="comments-container">
<span id="87334"></span>
<div id="comment-87334" class="comment">
<div id="post-87334-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Frederik for your response always!</p>
</div>
<div id="comment-87334-info" class="comment-info">
<span class="comment-age">(02 Jun '23, 02:01)</span> <span class="comment-user userinfo">Segunlakata</span>
</div>
</div>
</div>
<div id="comment-tools-87329" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87329-form-container" class="comment-form-container">
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

