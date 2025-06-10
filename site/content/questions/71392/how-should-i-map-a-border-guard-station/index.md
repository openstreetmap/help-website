+++
type = "question"
title = "How should I map a border guard station?"
description = '''Currently, border guard units are marked as military areas, government offices, police, etc. In many countries, border guards and police are two different formations. We have tags for coast guard (amenity=coast_guard), but we don&#x27;t have tags for border guard. Maybe some new tag?'''
date = "2019-10-31T08:44:00Z"
lastmod = "2020-05-16T03:50:00Z"
weight = 71392
keywords = [ "amenity", "borders" ]
aliases = [ "/questions/71392" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How should I map a border guard station?](/questions/71392/how-should-i-map-a-border-guard-station)

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
<span id="post-71392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71392-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Currently, border guard units are marked as military areas, government offices, police, etc. In many countries, border guards and police are two different formations. We have tags for coast guard (amenity=coast_guard), but we don't have tags for <a href="https://en.wikipedia.org/wiki/Border_guard">border guard</a>. Maybe some new tag?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-borders" rel="tag" title="see questions tagged &#39;borders&#39;">borders</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '19, 08:44</strong></p>
<img src="https://secure.gravatar.com/avatar/4f1072d1edc9e4fba99f63bcb6b803ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RafalR&#39;s gravatar image" />
<p><span>RafalR</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RafalR has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71392" class="comments-container">
<span id="71413"></span>
<div id="comment-71413" class="comment">
<div id="post-71413-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to clarify, when you say "station", is that a small checkpoint at a border crossing, or a larger multi-building facility (like a military base)?</p>
</div>
<div id="comment-71413-info" class="comment-info">
<span class="comment-age">(01 Nov '19, 16:24)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-71392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71392-form-container" class="comment-form-container">
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

<span id="71406"></span>

<div id="answer-container-71406" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71406-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-71406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We don't have a tag for it just like we don't have a tag for regular guard boths like the ones you find in industrial facility entrances.</p>
<p>The closest (from what we have currently) is probably <code>amenity=police</code>, but this can vary depending on which is the enforcing organization. For checkpoints we have:</p>
<ul>
<li><code>barrier=border_control</code></li>
<li><code>police=checkpoint</code></li>
<li><code>military=checkpoint</code></li>
</ul>
<p>But for a border crossing only <code>barrier=border_control</code> makes sense, so following this logic we should have <code>amenity=border_control</code> for your needs or maybe a new amenity for <a href="https://en.wikipedia.org/wiki/Guardhouse">guardhouses</a> generally, like <code>amenity=guard_house</code> then add subtypes like <code>guard_house=border_control</code> or <code>guard_house=security</code> for commercial/industrial ones.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '19, 02:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a9715d60e31c91a442c2dacefdc1dae9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="UntaggedWay&#39;s gravatar image" />
<p><span>UntaggedWay</span><br />
<span class="score" title="576 reputation points">576</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="UntaggedWay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71406" class="comments-container">
<span id="74849"></span>
<div id="comment-74849" class="comment">
<div id="post-74849-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also note <a href="https://wiki.openstreetmap.org/wiki/Tag:office%3Dsecurity">https://wiki.openstreetmap.org/wiki/Tag:office%3Dsecurity</a></p>
</div>
<div id="comment-74849-info" class="comment-info">
<span class="comment-age">(16 May '20, 03:50)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
</div>
<div id="comment-tools-71406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71406-form-container" class="comment-form-container">
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

