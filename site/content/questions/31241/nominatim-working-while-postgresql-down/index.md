+++
type = "question"
title = "Nominatim working while postgreSQL down"
description = '''Something happened to my postgres and the database is currently down on my server, but strangely, Nominatim is still able to reverse geocode locations. I&#x27;m a bit confused here, doesn&#x27;t Nominatim&#x27;s reverse geocoding use postgres database to find locations? Or is my postgres actually half-working?'''
date = "2014-03-03T22:35:00Z"
lastmod = "2015-06-15T14:06:00Z"
weight = 31241
keywords = [ "nominatim", "postgresql" ]
aliases = [ "/questions/31241" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim working while postgreSQL down](/questions/31241/nominatim-working-while-postgresql-down)

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
<span id="post-31241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31241-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Something happened to my postgres and the database is currently down on my server, but strangely, Nominatim is still able to reverse geocode locations. I'm a bit confused here, doesn't Nominatim's reverse geocoding use postgres database to find locations? Or is my postgres actually half-working?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '14, 22:35</strong></p>
<img src="https://secure.gravatar.com/avatar/61de868d7785f30711497cecbdddf5f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baekacaek&#39;s gravatar image" />
<p><span>baekacaek</span><br />
<span class="score" title="176 reputation points">176</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baekacaek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31241" class="comments-container">
&#10;</div>
<div id="comment-tools-31241" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31241-form-container" class="comment-form-container">
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

<span id="31336"></span>

<div id="answer-container-31336" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31336-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim cannot work without a PostgreSQL connection.</p>
<p>One of the following is probably happening:</p>
<ul>
<li>Nominatim is not working. You are looking at cached results.</li>
<li>Nominatim is not working. You are accidentally accessing a different server.</li>
<li>Nominatim is working; the database is down; but Nominatim is configured to access a different database, possible even</li>
<li>Nominatim is working; the database is not down; it just appears down to you because you tried to connect through a different route (e.g. Nominatim connects via Unix domain socket which works, you try to connect via TCP which doesn't, and assume the database is down)</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '14, 21:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-31336" class="comments-container">
<span id="31339"></span>
<div id="comment-31339" class="comment">
<div id="post-31339-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A nice list. Add this ;-)</p>
<ul>
<li>Nominatim is working, the database is down and up at random times and Nominatim was lucky while you were were unlucky when trying to access.</li>
</ul>
</div>
<div id="comment-31339-info" class="comment-info">
<span class="comment-age">(05 Mar '14, 22:04)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="43571"></span>
<div id="comment-43571" class="comment">
<div id="post-43571-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you please help me steps to install Nominatim and PostgreSQ?</p>
</div>
<div id="comment-43571-info" class="comment-info">
<span class="comment-age">(15 Jun '15, 13:35)</span> <span class="comment-user userinfo">vinay Kumar M B</span>
</div>
</div>
<span id="43572"></span>
<div id="comment-43572" class="comment">
<div id="post-43572-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11111/vinay-kumar-m-b"></a><a href="http://help.openstreetmap.org/users/11111/vinay-kumar-m-b">@vinay</a>-kumar-m-b Please ask a separate question and provide clear details why the <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">installation instructions</a> don't work for you.</p>
</div>
<div id="comment-43572-info" class="comment-info">
<span class="comment-age">(15 Jun '15, 14:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31336-form-container" class="comment-form-container">
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

