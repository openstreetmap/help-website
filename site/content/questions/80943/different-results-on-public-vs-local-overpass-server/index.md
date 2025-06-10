+++
type = "question"
title = "Different Results on Public vs Local Overpass Server"
description = '''I&#x27;ve installed an overpass server locally (following this guide) and everything is working, but very rarely there&#x27;s differences between the public server and my local one. So far this has exclusively been queries involving areas, with some areas just not existing on my local server while they do exi...'''
date = "2021-07-13T14:49:00Z"
lastmod = "2021-07-14T13:55:00Z"
weight = 80943
keywords = [ "overpassapi", "overpass", "areas", "area" ]
aliases = [ "/questions/80943" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Different Results on Public vs Local Overpass Server](/questions/80943/different-results-on-public-vs-local-overpass-server)

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
<span id="post-80943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80943-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've installed an overpass server locally (following <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Installation">this</a> guide) and everything is working, but very rarely there's differences between the public server and my local one. So far this has exclusively been queries involving areas, with some areas just not existing on my local server while they do exist on the public one.</p>
<p>As an example, the following query gives lots of results on <a href="https://overpass-turbo.eu/">https://overpass-turbo.eu/</a> with //overpass-api.de/api/ as the server, but running the same query on my local server gives nothing (because that area does not exist for me).</p>
<pre><code>rel(area:3601994077);
out tags;</code></pre>
<p>I don't know why this would be happening, any ideas on the cause / how to fix it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-areas" rel="tag" title="see questions tagged &#39;areas&#39;">areas</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jul '21, 14:49</strong></p>
<img src="https://secure.gravatar.com/avatar/90c1a2a6f8b3789f0622ae27f3d92bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nbreden&#39;s gravatar image" />
<p><span>nbreden</span><br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nbreden has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '21, 15:24</strong> </span></p>
</div>
</div>
<div id="comments-container-80943" class="comments-container">
&#10;</div>
<div id="comment-tools-80943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80943-form-container" class="comment-form-container">
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

<span id="80947"></span>

<div id="answer-container-80947" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80947-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nbreden has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The most recent <a href="https://www.openstreetmap.org/changeset/106746793">changeset</a> for that relation (21 days ago) indicates that it and some other relations had been in a broken state. Depending on the state of it at the time you downloaded the data, it may not have properly imported into your database. You could try updating your data to see if Overpass then creates the area as expected, now that the relation has been fixed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '21, 16:59</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-80947" class="comments-container">
<span id="80965"></span>
<div id="comment-80965" class="comment">
<div id="post-80965-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think this was the problem. I updated my data and some of the problem cases went away (not all of them though :/). Thanks!</p>
</div>
<div id="comment-80965-info" class="comment-info">
<span class="comment-age">(14 Jul '21, 13:55)</span> <span class="comment-user userinfo">nbreden</span>
</div>
</div>
</div>
<div id="comment-tools-80947" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80947-form-container" class="comment-form-container">
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

