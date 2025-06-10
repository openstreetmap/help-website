+++
type = "question"
title = "splitting tiles directory ?"
description = '''hello  im trying to pre render tiles for a country z0 to Z18  i used only half of disk space but find myself with 0 free Inodes is there a way to split the directory /var/lib/mod_tile/default/ to 2 or more hard drives ? '''
date = "2018-12-12T07:56:00Z"
lastmod = "2018-12-12T17:56:00Z"
weight = 67140
keywords = [ "render_list", "pre-built", "mod_tile" ]
aliases = [ "/questions/67140" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [splitting tiles directory ?](/questions/67140/splitting-tiles-directory)

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
<span id="post-67140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67140-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello</p>
<p>im trying to pre render tiles for a country z0 to Z18 i used only half of disk space but find myself with 0 free Inodes is there a way to split the directory /var/lib/mod_tile/default/ to 2 or more hard drives ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-render_list" rel="tag" title="see questions tagged &#39;render_list&#39;">render_list</span> <span class="post-tag tag-link-pre-built" rel="tag" title="see questions tagged &#39;pre-built&#39;">pre-built</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Dec '18, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/8524afbaa2cb261296c620ea044952de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="do-d&#39;s gravatar image" />
<p><span>do-d</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="do-d has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67140" class="comments-container">
&#10;</div>
<div id="comment-tools-67140" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67140-form-container" class="comment-form-container">
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

<span id="67146"></span>

<div id="answer-container-67146" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67146-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Prerendering tiles down to z18 is probably not what you want to do, for exactly the reason that you've found. At the Unix level you have the opportunity to create mount points within <code>/var/lib/mod_tile</code> and having files below there elsewhere, but that's like dealing with a leaky roof with a bucket rather than fixing the leak.</p>
<p>What problem are you actually trying to solve by pre-rendering tiles down to z18 (most of which will never be accessed)?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '18, 17:56</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-67146" class="comments-container">
&#10;</div>
<div id="comment-tools-67146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67146-form-container" class="comment-form-container">
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

