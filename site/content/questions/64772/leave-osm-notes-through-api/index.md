+++
type = "question"
title = "Leave OSM notes through API"
description = '''Is it possible to leave notes by using the API? When I need local mapper help I&#x27;ve noticed, that nobody cares for my FIXMEs, but that notes instead are quickly fixed. So I would like to write a JOSM tool which converts my FIXMEs into notes.'''
date = "2018-07-17T19:30:00Z"
lastmod = "2018-07-19T20:56:00Z"
weight = 64772
keywords = [ "josm", "notes", "api" ]
aliases = [ "/questions/64772" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Leave OSM notes through API](/questions/64772/leave-osm-notes-through-api)

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
<span id="post-64772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64772-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to leave <a href="https://wiki.openstreetmap.org/wiki/Notes">notes</a> by using the API?</p>
<p>When I need local mapper help I've noticed, that nobody cares for my FIXMEs, but that notes instead are quickly fixed. So I would like to write a JOSM tool which converts my FIXMEs into notes.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-notes" rel="tag" title="see questions tagged &#39;notes&#39;">notes</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jul '18, 19:30</strong></p>
<img src="https://secure.gravatar.com/avatar/c1d822e9922f602162e979f9fbde9187?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OpenTopoMap&#39;s gravatar image" />
<p><span>OpenTopoMap</span><br />
<span class="score" title="40 reputation points">40</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OpenTopoMap has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64772" class="comments-container">
<span id="64775"></span>
<div id="comment-64775" class="comment">
<div id="post-64775-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just for curiosity: Can I create an anonymous note by using the API like it's possible for anonymous users on the OSM webpage?</p>
<pre><code>curl -X POST https://apis.openstreetmap.org/api/0.6/notes?lat=52.51861&amp;lon=113.40833&amp;text=ExampleNote</code></pre>
</div>
<div id="comment-64775-info" class="comment-info">
<span class="comment-age">(17 Jul '18, 23:49)</span> <span class="comment-user userinfo">OpenTopoMap</span>
</div>
</div>
<span id="64806"></span>
<div id="comment-64806" class="comment">
<div id="post-64806-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For the benefit of future readers: JOSM has a <a href="https://josm.openstreetmap.de/wiki/Help/Dialog/Notes">built-in dialog for creating and updating OSM notes</a>. It doesn't convert FIXMEs, but is still convenient for many typical use-cases.</p>
</div>
<div id="comment-64806-info" class="comment-info">
<span class="comment-age">(19 Jul '18, 20:56)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-64772" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64772-form-container" class="comment-form-container">
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

<span id="64774"></span>

<div id="answer-container-64774" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64774-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the wikipage you link to, there's a link to the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Map_Notes_API">Map_Notes_API</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '18, 21:12</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-64774" class="comments-container">
&#10;</div>
<div id="comment-tools-64774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64774-form-container" class="comment-form-container">
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

