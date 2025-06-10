+++
type = "question"
title = "Renderd across multiple machines"
description = '''I&#x27;m looking into running multiple renderd instances across multiple machines to load balance the rendering of tiles. It seems like renderd supports this with the [renderd01] and [renderd02] options in the config files. If anyone has any experience, I was hoping to ask a few questions since I&#x27;ve had ...'''
date = "2018-07-27T00:43:00Z"
lastmod = "2018-07-28T15:00:00Z"
weight = 64958
keywords = [ "renderd" ]
aliases = [ "/questions/64958" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Renderd across multiple machines](/questions/64958/renderd-across-multiple-machines)

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
<span id="post-64958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64958-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking into running multiple renderd instances across multiple machines to load balance the rendering of tiles. It seems like renderd supports this with the [renderd01] and [renderd02] options in the config files. If anyone has any experience, I was hoping to ask a few questions since I've had trouble finding resources online about it:</p>
<ol>
<li>Is this possible?</li>
<li>Is there a limit to how many instances you can run? e.g. Can you add [renderd03], etc.?</li>
<li>Does the master instance act as the single point of contact to clients and it distributes requests to its worker instances on different machines?</li>
<li>Is there any explanation of the configuration required on the master and worker instances? The config file on the master looks like it needs IPs of the workers. How do the workers know where the master is located on the network?</li>
<li>Are there any other gotchas that would be helpful to know about?</li>
</ol>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '18, 00:43</strong></p>
<img src="https://secure.gravatar.com/avatar/7594614ba848fdde8ac9feb3d91253f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coderunner&#39;s gravatar image" />
<p><span>coderunner</span><br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coderunner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64958" class="comments-container">
&#10;</div>
<div id="comment-tools-64958" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64958-form-container" class="comment-form-container">
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

<span id="64982"></span>

<div id="answer-container-64982" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64982-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>It seems like renderd supports this with the [renderd01] and [renderd02] options in the config files.</p>
</blockquote>
<p>Just to be clear, which config file are you talking about? If you mean <code>renderd.conf</code>, then you can define multiple styles in one file, but that's the opposite of what you want I think.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '18, 14:25</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-64982" class="comments-container">
&#10;</div>
<div id="comment-tools-64982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64982-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64983"></span>

<div id="answer-container-64983" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64983-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes sorry. Didn't specify but I meant renderd.conf. It looks like you set the IP for the worker machines in those sections and the master load balances requests across all the workers listed (even if they are on separate machines on the same network?</p>
<p>Also if you are the owner of the someoneelseosm mod_tile fork, thanks for doing that!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '18, 14:55</strong></p>
<img src="https://secure.gravatar.com/avatar/7594614ba848fdde8ac9feb3d91253f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coderunner&#39;s gravatar image" />
<p><span>coderunner</span><br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coderunner has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jul '18, 14:56</strong> </span></p>
</div>
</div>
<div id="comments-container-64983" class="comments-container">
<span id="64984"></span>
<div id="comment-64984" class="comment">
<div id="post-64984-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>It looks like you set the IP for the worker machines in those sections and the master load balances requests across all the workers</p>
</blockquote>
<p>If you can get all that working it'd be great if you could write up a diary entry or similar about it - I'm sure that it'd be useful to lots of other people.</p>
</div>
<div id="comment-64984-info" class="comment-info">
<span class="comment-age">(28 Jul '18, 15:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64983" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64983-form-container" class="comment-form-container">
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

