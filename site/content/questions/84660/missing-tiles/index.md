+++
type = "question"
title = "Missing Tiles?"
description = '''I&#x27;ve just started using OpenStreetMap in a C# project. It&#x27;s great! Occasionally I notice, when retrieving tiles, that some of them don&#x27;t seem to exist...even though &quot;nearby&quot; tiles do. For example, https://tile.openstreetmap.org/13/665/1580.png returns a 404 error, but https://tile.openstreetmap.org/...'''
date = "2022-06-01T19:09:00Z"
lastmod = "2022-06-04T20:04:00Z"
weight = 84660
keywords = [ "missing" ]
aliases = [ "/questions/84660" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Missing Tiles?](/questions/84660/missing-tiles)

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
<span id="post-84660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84660-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've just started using OpenStreetMap in a C# project. It's great!</p>
<p>Occasionally I notice, when retrieving tiles, that some of them don't seem to exist...even though "nearby" tiles do. For example, <a href="https://tile.openstreetmap.org/13/665/1580.png">https://tile.openstreetmap.org/13/665/1580.png</a> returns a 404 error, but <a href="https://tile.openstreetmap.org/13/665/1579.png">https://tile.openstreetmap.org/13/665/1579.png</a> and <a href="https://tile.openstreetmap.org/13/665/1581.png">https://tile.openstreetmap.org/13/665/1581.png</a> both exist.</p>
<p>Are there some regions/tiles that just aren't in the database? If so, I'd love to know why. Just curious!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '22, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/4e60e64904304c8a59d810b254400fd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Motorcycle%20Mayor&#39;s gravatar image" />
<p><span>Motorcycle M...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Motorcycle Mayor has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84660" class="comments-container">
<span id="84663"></span>
<div id="comment-84663" class="comment">
<div id="post-84663-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Fascinating! The missing tile now shows up on my iPhone browser. I guess the server cache was invalid earlier today</p>
</div>
<div id="comment-84663-info" class="comment-info">
<span class="comment-age">(02 Jun '22, 01:26)</span> <span class="comment-user userinfo">Motorcycle M...</span>
</div>
</div>
<span id="84698"></span>
<div id="comment-84698" class="comment">
<div id="post-84698-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Bear in mind that if you're accessing tiles programmatically, you need to set a distinct User-Agent header that identifies your application. If you use the stock C# one you're at risk of being blocked.</p>
</div>
<div id="comment-84698-info" class="comment-info">
<span class="comment-age">(04 Jun '22, 10:57)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="84700"></span>
<div id="comment-84700" class="comment">
<div id="post-84700-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanx, Richard. I am supplying a User-Agent identifier (based on my program's FQ name). Just to be clear, you don't mean I need to supply a unique identifier for each request? That's not how I read the docs. If I need to do that I'd have to tweak the program.</p>
</div>
<div id="comment-84700-info" class="comment-info">
<span class="comment-age">(04 Jun '22, 18:32)</span> <span class="comment-user userinfo">Motorcycle M...</span>
</div>
</div>
<span id="84701"></span>
<div id="comment-84701" class="comment">
<div id="post-84701-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, it has to be unique for your application, not for each individual request of your application. So all your requests should have to same UA which is unique for your application.</p>
</div>
<div id="comment-84701-info" class="comment-info">
<span class="comment-age">(04 Jun '22, 20:04)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-84660" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84660-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

