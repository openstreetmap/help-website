+++
type = "question"
title = "ActionView::Template::Error: couldn&#x27;t find file &#x27;settings.local.yml&#x27;"
description = '''I&#x27;m trying to setup a Openstreetmap Website (old The Rails Port) following the instructions at https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md but got stuck in the last step before running the server. When I run the command &quot;bundle exec rake db:create&quot; it makes a long t...'''
date = "2019-07-05T00:07:00Z"
lastmod = "2019-07-05T09:24:00Z"
weight = 69887
keywords = [ "website", "railsport" ]
aliases = [ "/questions/69887" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [ActionView::Template::Error: couldn't find file 'settings.local.yml'](/questions/69887/actionviewtemplateerror-couldnt-find-file-settingslocalyml)

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
<span id="post-69887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69887-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to setup a Openstreetmap Website (old The Rails Port) following the instructions at <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md">https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md</a> but got stuck in the last step before running the server. When I run the command "bundle exec rake db:create" it makes a long test with several lines of messages (thousands of lines I think) but most of them are very similar with repeated messages and an error that repeats among all of them: ActionView::Template::Error: couldn't find file 'settings.local.yml' A copy of part of the error is at this link: <a href="https://gist.github.com/caduguedess/ccf911088775eaf644893352be23e865">https://gist.github.com/caduguedess/ccf911088775eaf644893352be23e865</a> I would appreciate if somebody knows how to adress this issue. When I browse for localhost:3000 this is what I get: <img src="/upfiles/Screenshot_from_2019-07-04_13-20-18_rQq01MY.png" alt="alt text" /></p>
<p>I'm on Ubuntu 18.04 Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jul '19, 00:07</strong></p>
<img src="https://secure.gravatar.com/avatar/5f1f061e7e81f0e885227d27d95752f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlosguedes&#39;s gravatar image" />
<p><span>carlosguedes</span><br />
<span class="score" title="91 reputation points">91</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlosguedes has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-69887" class="comments-container">
&#10;</div>
<div id="comment-tools-69887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69887-form-container" class="comment-form-container">
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

<span id="69889"></span>

<div id="answer-container-69889" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69889-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="carlosguedes has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a bug in the way that the codebase works right now. You need to create a blank file in the <code>config</code> directory called <code>settings.local.yml</code>, for example by running</p>
<p><code>$ touch config/settings.local.yml</code></p>
<p>See <a href="https://github.com/openstreetmap/openstreetmap-website/issues/2185">https://github.com/openstreetmap/openstreetmap-website/issues/2185</a> for more information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '19, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-69889" class="comments-container">
&#10;</div>
<div id="comment-tools-69889" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69889-form-container" class="comment-form-container">
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

