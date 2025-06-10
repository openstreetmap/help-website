+++
type = "question"
title = "Nominatim usage policy: HTTP Referers and User-Agents"
description = '''Hi all, I&#x27;ve got a question on the Nominatim Usage Policy that will probably sound stupid to many of you, but have very limited experience with APIs and just want to make sure to get it right. The policy states:  Provide a valid HTTP Referer or User-Agent identifying the application (stock User-Agen...'''
date = "2020-04-15T15:42:00Z"
lastmod = "2020-04-15T16:49:00Z"
weight = 74205
keywords = [ "policy", "python", "api", "nominatim" ]
aliases = [ "/questions/74205" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim usage policy: HTTP Referers and User-Agents](/questions/74205/nominatim-usage-policy-http-referers-and-user-agents)

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
<span id="post-74205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74205-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I've got a question on the <a href="https://operations.osmfoundation.org/policies/nominatim/">Nominatim Usage Policy</a> that will probably sound stupid to many of you, but have very limited experience with APIs and just want to make sure to get it right. The policy states:</p>
<blockquote>
<p>Provide a valid <strong>HTTP Referer</strong> or <strong>User-Agent</strong> identifying the application (stock User-Agents as set by http libraries will not do).</p>
</blockquote>
<p>and I simply don't know what this means - if I were to write a Python script using the <em>requests</em> library in combination with the API and do a simple requests.get(url), would that be OK (given I'll abide by the other rules, like the request limit), or would that exactly be what falls under "stock User-Agents as set by http libraries"? In the latter case, what would I have to change to make it comply?</p>
<p>Thanks for the help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-policy" rel="tag" title="see questions tagged &#39;policy&#39;">policy</span> <span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '20, 15:42</strong></p>
<img src="https://secure.gravatar.com/avatar/bd07b02a16af07c9d3e5f633c10e4c7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ratatoskr&#39;s gravatar image" />
<p><span>Ratatoskr</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ratatoskr has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '20, 15:42</strong> </span></p>
</div>
</div>
<div id="comments-container-74205" class="comments-container">
&#10;</div>
<div id="comment-tools-74205" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74205-form-container" class="comment-form-container">
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

<span id="74206"></span>

<div id="answer-container-74206" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74206-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-74206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How to set <code>user-agent</code> in python requests is document here: <a href="https://stackoverflow.com/questions/10606133/sending-user-agent-using-requests-library-in-python">https://stackoverflow.com/questions/10606133/sending-user-agent-using-requests-library-in-python</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '20, 16:49</strong></p>
<img src="https://secure.gravatar.com/avatar/e79628d44a15e95c607f8c5007d0ccd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Firefishy&#39;s gravatar image" />
<p><span>Firefishy ♦♦</span><br />
<span class="score" title="1296 reputation points"><span>1.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Firefishy has 14 accepted answers">29%</span></p>
</div>
</div>
<div id="comments-container-74206" class="comments-container">
&#10;</div>
<div id="comment-tools-74206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74206-form-container" class="comment-form-container">
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

