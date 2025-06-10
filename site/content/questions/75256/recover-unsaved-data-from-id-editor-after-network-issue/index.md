+++
type = "question"
title = "Recover unsaved data from iD editor after network issue"
description = '''After a network or authentication issue while saving my changes, the iD editor is stuck in the &quot;saving&quot; state with no way to cancel and try again. How can I recover or at least see my changes? I&#x27;m hoping there&#x27;s a way to reset the UI so that I can at least see the tags that I added, either through t...'''
date = "2020-06-09T19:49:00Z"
lastmod = "2020-06-09T22:03:00Z"
weight = 75256
keywords = [ "ideditor" ]
aliases = [ "/questions/75256" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Recover unsaved data from iD editor after network issue](/questions/75256/recover-unsaved-data-from-id-editor-after-network-issue)

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
<span id="post-75256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75256-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After a network or authentication issue while saving my changes, the iD editor is stuck in the "saving" state with no way to cancel and try again. How can I recover or at least see my changes? I'm hoping there's a way to reset the UI so that I can at least see the tags that I added, either through the UI or by manipulating the window.iD object through the console. Or perhaps someone can point me to the variable that contains my changes.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jun '20, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a4bce9529d90de62f48bfd28bb7cab3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maskedwanderer&#39;s gravatar image" />
<p><span>maskedwanderer</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maskedwanderer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75256" class="comments-container">
&#10;</div>
<div id="comment-tools-75256" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75256-form-container" class="comment-form-container">
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

<span id="75258"></span>

<div id="answer-container-75258" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75258-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-75258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="maskedwanderer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Fist of all you should check if your changes might already have been saved into the OSM database: <a href="https://www.openstreetmap.org/user/maskedwanderer/history">your changesets</a>.</p>
<p>If not you can try re-loading the page. Usually, when reloaded, you will be asked if you want to restore your unsaved changes. Of course I cannot guarantee this is working in your case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '20, 21:32</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-75258" class="comments-container">
<span id="75259"></span>
<div id="comment-75259" class="comment">
<div id="post-75259-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you! That did the trick. I was hesitant to do it at first since when I opened the editor in a new tab it did not ask to restore my unsaved changes. But reloading the tab worked. I also managed to leave the stuck "saving" state by searching for a feature, clicking on a result and waiting a few seconds. At that point I was still unable to upload the changes, but at least I was able to download an OSM changes file.</p>
</div>
<div id="comment-75259-info" class="comment-info">
<span class="comment-age">(09 Jun '20, 22:03)</span> <span class="comment-user userinfo">maskedwanderer</span>
</div>
</div>
</div>
<div id="comment-tools-75258" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75258-form-container" class="comment-form-container">
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

