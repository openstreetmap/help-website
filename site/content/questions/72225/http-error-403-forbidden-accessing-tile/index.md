+++
type = "question"
title = "HTTP error 403 (Forbidden) accessing tile"
description = '''I&#x27;m trying to fetch a tile https://b.tile.openstreetmap.org/16/35672/23381.png from a Go script, and the server is returning a 403/Forbidden error. Go is using HTTP/2 by default (instead of more common HTTP/1.1) so it might be a configuration error? Other headers indicate the error was generated by ...'''
date = "2019-12-27T01:52:00Z"
lastmod = "2019-12-27T23:11:00Z"
weight = 72225
keywords = [ "tiles", "tileserver" ]
aliases = [ "/questions/72225" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP error 403 (Forbidden) accessing tile](/questions/72225/http-error-403-forbidden-accessing-tile)

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
<span id="post-72225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72225-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to fetch a tile <a href="https://b.tile.openstreetmap.org/16/35672/23381.png">https://b.tile.openstreetmap.org/16/35672/23381.png</a> from a Go script, and the server is returning a 403/Forbidden error.</p>
<p>Go is using HTTP/2 by default (instead of more common HTTP/1.1) so it might be a configuration error? Other headers indicate the error was generated by the Squid proxy.</p>
<p>Who can I talk to to resolve this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Dec '19, 01:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ff34020e0a05e5f3b45e4e3825bf7c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivoras&#39;s gravatar image" />
<p><span>ivoras</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivoras has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Dec '19, 01:53</strong> </span></p>
</div>
</div>
<div id="comments-container-72225" class="comments-container">
&#10;</div>
<div id="comment-tools-72225" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72225-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="72243"></span>

<div id="answer-container-72243" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72243-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It was about the user-agent: the tile servers require non-browsers to have user-agent strings which identify applications, to be able to enforce tile download policy.</p>
<p>If someone encounters this problem in the future: you need to set the User-Agent HTTP header to identify your application. More information is available at the <a href="https://operations.osmfoundation.org/policies/tiles/">Tile usage policy page</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '19, 23:11</strong></p>
<img src="https://secure.gravatar.com/avatar/ff34020e0a05e5f3b45e4e3825bf7c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivoras&#39;s gravatar image" />
<p><span>ivoras</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivoras has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72243" class="comments-container">
&#10;</div>
<div id="comment-tools-72243" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72243-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72227"></span>

<div id="answer-container-72227" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72227-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are probably hitting one of the limit explained here : <a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a> In particular, using a script to access tiles is most probably beyond acceptable usage.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '19, 07:21</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-72227" class="comments-container">
<span id="72231"></span>
<div id="comment-72231" class="comment">
<div id="post-72231-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nope, never tried it before, I just wrote the script.</p>
<p>Additionally, loading the tile from a web browser works, both with HTTPS and HTTP, but loading it with the script doesn't - maybe there's a blanket ban for Go's user-agent?</p>
</div>
<div id="comment-72231-info" class="comment-info">
<span class="comment-age">(27 Dec '19, 11:26)</span> <span class="comment-user userinfo">ivoras</span>
</div>
</div>
<span id="72234"></span>
<div id="comment-72234" class="comment">
<div id="post-72234-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please don't respond to answers with further answers, add a comment or amend your original question.</p>
<p>In general generic user agents will sooner or later be blocked, adhere to the tou and you should be fine.</p>
</div>
<div id="comment-72234-info" class="comment-info">
<span class="comment-age">(27 Dec '19, 15:58)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-72227" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72227-form-container" class="comment-form-container">
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

