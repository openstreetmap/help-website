+++
type = "question"
title = "Problems with Wiki (Internal Error on registration and ConfirmEmail)"
description = '''I just registered on the wiki and got an Internal error. I haven&#x27;t received a email on registration. Now J try to confirm my mail adress but got also an Internal error (on Special:ConfirmEmail). Notice text was:  Internal error Set $wgShowExceptionDetails = true; at the bottom of LocalSettings.php t...'''
date = "2012-04-05T19:42:00Z"
lastmod = "2012-04-13T23:21:00Z"
weight = 11753
keywords = [ "wiki", "email", "error" ]
aliases = [ "/questions/11753" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Problems with Wiki (Internal Error on registration and ConfirmEmail)](/questions/11753/problems-with-wiki-internal-error-on-registration-and-confirmemail)

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
<span id="post-11753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11753-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just registered on the wiki and got an Internal error. I haven't received a email on registration. Now J try to confirm my mail adress but got also an Internal error (on Special:ConfirmEmail).</p>
<p>Notice text was:</p>
<blockquote>
<p>Internal error</p>
<p>Set $wgShowExceptionDetails = true; at the bottom of LocalSettings.php to show detailed debugging information.</p>
</blockquote>
<p>registration here at help.openstreetmap.org works and also get the registration email for it. So I think there is a problem with the mail configuration in the wiki.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wiki" rel="tag" title="see questions tagged &#39;wiki&#39;">wiki</span> <span class="post-tag tag-link-email" rel="tag" title="see questions tagged &#39;email&#39;">email</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Apr '12, 19:42</strong></p>
<img src="https://secure.gravatar.com/avatar/7f7ba79b500339855f4258629da6e740?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="se4598&#39;s gravatar image" />
<p><span>se4598</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="se4598 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11753" class="comments-container">
&#10;</div>
<div id="comment-tools-11753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11753-form-container" class="comment-form-container">
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

<span id="11996"></span>

<div id="answer-container-11996" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11996-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-11996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="se4598 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Fixed. Problem was due to a bug in Mediawiki 1.17.3 (used by wiki.openstreetmap.org ) and resolved by patch: <a href="https://bugzilla.wikimedia.org/show_bug.cgi?id=35441">https://bugzilla.wikimedia.org/show_bug.cgi?id=35441</a></p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '12, 23:21</strong></p>
<img src="https://secure.gravatar.com/avatar/e79628d44a15e95c607f8c5007d0ccd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Firefishy&#39;s gravatar image" />
<p><span>Firefishy ♦♦</span><br />
<span class="score" title="1296 reputation points"><span>1.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Firefishy has 14 accepted answers">29%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> wikified <strong>13 Apr '12, 23:22</strong> </span></p>
</div>
</div>
<div id="comments-container-11996" class="comments-container">
&#10;</div>
<div id="comment-tools-11996" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11996-form-container" class="comment-form-container">
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

