+++
type = "question"
title = "Missing diagonal tiles when rendering"
description = '''I followed the directions here https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/ to set up my own tile server. When rendering tiles now, diagonal tiles are always missing when displayed in a browser (regardless of zoom level) like shown here:  https://imgur.com/a/QK6gozY I&#x27;m not ge...'''
date = "2018-05-21T19:16:00Z"
lastmod = "2018-05-21T22:31:00Z"
weight = 63601
keywords = [ "renderd", "mod_tile" ]
aliases = [ "/questions/63601" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Missing diagonal tiles when rendering](/questions/63601/missing-diagonal-tiles-when-rendering)

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
<span id="post-63601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63601-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I followed the directions here <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> to set up my own tile server. When rendering tiles now, diagonal tiles are always missing when displayed in a browser (regardless of zoom level) like shown here:</p>
<p><a href="https://imgur.com/a/QK6gozY">https://imgur.com/a/QK6gozY</a></p>
<p>I'm not getting any errors when going through the guide linked above. Any ideas on what I could be doing wrong? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 May '18, 19:16</strong></p>
<img src="https://secure.gravatar.com/avatar/7594614ba848fdde8ac9feb3d91253f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coderunner&#39;s gravatar image" />
<p><span>coderunner</span><br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coderunner has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '18, 19:46</strong> </span></p>
</div>
</div>
<div id="comments-container-63601" class="comments-container">
&#10;</div>
<div id="comment-tools-63601" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63601-form-container" class="comment-form-container">
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

<span id="63603"></span>

<div id="answer-container-63603" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63603-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="coderunner has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm guessing that only 2 requests in 3 are getting through to a working tile server. Are you using something like switcheroo to redirect? If so, with what rule?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '18, 20:05</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-63603" class="comments-container">
<span id="63605"></span>
<div id="comment-63605" class="comment">
<div id="post-63605-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You were right. I was missing a forward slash at the end of the source url in one of the rules. That fixed it. Thanks!</p>
</div>
<div id="comment-63605-info" class="comment-info">
<span class="comment-age">(21 May '18, 22:31)</span> <span class="comment-user userinfo">coderunner</span>
</div>
</div>
</div>
<div id="comment-tools-63603" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63603-form-container" class="comment-form-container">
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

