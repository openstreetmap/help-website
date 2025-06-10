+++
type = "question"
title = "One way for bicycles only, 2 way for vehicles"
description = '''I&#x27;m trying to tag a section of road as one-way, but only for bicycles. Washington Ave, between its northern end (where it turns into I295 on/off ramps) and the intersection with Eastern Promenade is one-way south only for bicycles. I can&#x27;t figure out how to properly mark this. https://www.openstreet...'''
date = "2021-04-01T18:19:00Z"
lastmod = "2021-04-01T20:50:00Z"
weight = 79475
keywords = [ "bicycle", "oneway" ]
aliases = [ "/questions/79475" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [One way for bicycles only, 2 way for vehicles](/questions/79475/one-way-for-bicycles-only-2-way-for-vehicles)

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
<span id="post-79475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79475-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to tag a section of road as one-way, but only for bicycles.</p>
<p>Washington Ave, between its northern end (where it turns into I295 on/off ramps) and the intersection with Eastern Promenade is one-way south only for bicycles. I can't figure out how to properly mark this.</p>
<p><a href="https://www.openstreetmap.org/#map=18/43.67138/-70.25508">https://www.openstreetmap.org/#map=18/43.67138/-70.25508</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '21, 18:19</strong></p>
<img src="https://secure.gravatar.com/avatar/3544a16d87f1a8a38477ace55a5cee1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scotteaton92&#39;s gravatar image" />
<p><span>scotteaton92</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scotteaton92 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79475" class="comments-container">
<span id="79476"></span>
<div id="comment-79476" class="comment">
<div id="post-79476-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And I also have the opposite question. Nevens St between Concord St and Saunders St is 2-ways for bicycles, and 1-way for vehicles.</p>
<p><a href="https://www.openstreetmap.org/#map=18/43.67236/-70.28647">https://www.openstreetmap.org/#map=18/43.67236/-70.28647</a></p>
</div>
<div id="comment-79476-info" class="comment-info">
<span class="comment-age">(01 Apr '21, 19:08)</span> <span class="comment-user userinfo">scotteaton92</span>
</div>
</div>
</div>
<div id="comment-tools-79475" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79475-form-container" class="comment-form-container">
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

<span id="79477"></span>

<div id="answer-container-79477" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79477-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="scotteaton92 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Key:oneway:bicycle">https://wiki.openstreetmap.org/wiki/Key:oneway:bicycle</a></p>
<p>"but only for bicycles."</p>
<p>oneway:bicycle=yes</p>
<p>This give oneway direction for bicycles.</p>
<p>"opposite"</p>
<p>oneway:bicycle=no</p>
<p>This give two way direction for bicycles, when oneway=yes is set.</p>
<p>Look at the drawing direction of the wayline. oneway=yes is the forward direction, oneway:bicycle=yes is also forward direction.</p>
<p>There is also oneway:mofa and oneway:moped possible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '21, 20:50</strong></p>
<img src="https://secure.gravatar.com/avatar/6c5dc0fc3be6786b643d15ec99ba3e3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Allroads&#39;s gravatar image" />
<p><span>Allroads</span><br />
<span class="score" title="222 reputation points">222</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Allroads has one accepted answer">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Apr '21, 20:52</strong> </span></p>
</div>
</div>
<div id="comments-container-79477" class="comments-container">
&#10;</div>
<div id="comment-tools-79477" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79477-form-container" class="comment-form-container">
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

