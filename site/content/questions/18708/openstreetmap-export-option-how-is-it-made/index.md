+++
type = "question"
title = "Openstreetmap export option: how is it made?"
description = '''I&#x27;m running my own mapserver with OpenStreetMap and i&#x27;d like to add an export function like on OpenStreetMap Where can i find an example (html / javascript / ...) I can&#x27;t find any information about the export functionality other then links to the OpenStreetMap home page.'''
date = "2012-12-26T10:57:00Z"
lastmod = "2012-12-27T06:31:00Z"
weight = 18708
keywords = [ "development", "export", "railsport" ]
aliases = [ "/questions/18708" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Openstreetmap export option: how is it made?](/questions/18708/openstreetmap-export-option-how-is-it-made)

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
<span id="post-18708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18708-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm running my own mapserver with OpenStreetMap and i'd like to add an export function like on <a href="https://www.openstreetmap.org/export/">OpenStreetMap</a></p>
<p>Where can i find an example (html / javascript / ...)</p>
<p>I can't find any information about the export functionality other then links to the OpenStreetMap home page.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Dec '12, 10:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c90a1bf3b56ac07ada8d0918e394a2da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Robertico&#39;s gravatar image" />
<p><span>Robertico</span><br />
<span class="score" title="66 reputation points">66</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Robertico has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Apr '15, 21:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-18708" class="comments-container">
&#10;</div>
<div id="comment-tools-18708" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18708-form-container" class="comment-form-container">
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

<span id="18711"></span>

<div id="answer-container-18711" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18711-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-18711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can find the Ruby code for the export tab itself <a href="http://git.openstreetmap.org/rails.git/tree/HEAD:/app/views/export">here</a>. When you push the export button <a href="https://trac.openstreetmap.org/browser/sites/tile.openstreetmap.org/cgi-bin/export">this Python script</a> is executed or an api call is made, as can be found <a href="http://git.openstreetmap.org/rails.git/blob/HEAD:/app/controllers/export_controller.rb">here</a>.</p>
<p>(There might be a newer version of the Python script somewhere.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Dec '12, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-18711" class="comments-container">
<span id="18712"></span>
<div id="comment-18712" class="comment">
<div id="post-18712-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@cartinus</span>: Thank you very much !! I'll give it a try.</p>
</div>
<div id="comment-18712-info" class="comment-info">
<span class="comment-age">(27 Dec '12, 06:31)</span> <span class="comment-user userinfo">Robertico</span>
</div>
</div>
</div>
<div id="comment-tools-18711" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18711-form-container" class="comment-form-container">
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

