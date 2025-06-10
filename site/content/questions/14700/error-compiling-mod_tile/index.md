+++
type = "question"
title = "Error compiling mod_tile"
description = '''I&#x27;m attempting to compile mod_tile on Ubuntu 12:04, per the instructions. Autogen fails with the error below. Anyone have any thoughts on fixing this? configure.ac:35: error: possibly undefined macro: AC_CHECK_FT2  If this token and others are legitimate, please use m4_pattern_allow.  See the Autoco...'''
date = "2012-07-30T13:29:00Z"
lastmod = "2012-08-29T08:27:00Z"
weight = 14700
keywords = [ "compile", "compilation", "error", "renderd", "mod_tile" ]
aliases = [ "/questions/14700" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Error compiling mod_tile](/questions/14700/error-compiling-mod_tile)

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
<span id="post-14700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14700-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm attempting to compile mod_tile on Ubuntu 12:04, per the <a href="http://wiki.openstreetmap.org/wiki/Mod_tile#Install_mod_tile_From_Source">instructions</a>. Autogen fails with the error below. Anyone have any thoughts on fixing this?</p>
<pre><code>configure.ac:35: error: possibly undefined macro: AC_CHECK_FT2
     If this token and others are legitimate, please use m4_pattern_allow.
     See the Autoconf documentation.
autoreconf: /usr/bin/autoconf failed with exit status: 1</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-compilation" rel="tag" title="see questions tagged &#39;compilation&#39;">compilation</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '12, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/737f9e0f502db153ed024192d3e1cfc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keith_uk&#39;s gravatar image" />
<p><span>keith_uk</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keith_uk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14700" class="comments-container">
&#10;</div>
<div id="comment-tools-14700" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14700-form-container" class="comment-form-container">
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

<span id="15623"></span>

<div id="answer-container-15623" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15623-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try with:</p>
<p>$ sudo apt-get install libfreetype6-dev</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '12, 08:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0e065e3d0a38c5286c8c0e84bb2e303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jorge%20Piera%20Llodr%C3%A1&#39;s gravatar image" />
<p><span>Jorge Piera ...</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jorge Piera Llodrá has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15623" class="comments-container">
&#10;</div>
<div id="comment-tools-15623" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15623-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14870"></span>

<div id="answer-container-14870" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14870-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have you installed Freetype 2? This appears to refer to it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '12, 16:17</strong></p>
<img src="https://secure.gravatar.com/avatar/5eea0a101ed06779f56546479dcc80b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcw&#39;s gravatar image" />
<p><span>mcw</span><br />
<span class="score" title="416 reputation points">416</span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcw has one accepted answer">6%</span></p>
</div>
</div>
<div id="comments-container-14870" class="comments-container">
&#10;</div>
<div id="comment-tools-14870" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14870-form-container" class="comment-form-container">
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

