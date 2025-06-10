+++
type = "question"
title = "Version mismatch while updating node information"
description = '''I&#x27;ve written a PHP script that updates some tages of a previously retrieved node information. Before updating the node, I request a changeset and the current content of the node. I than make the required changes to the node&#x27;s tags. So far so good. When I try to upload the changes, I get the message:...'''
date = "2011-10-25T09:02:00Z"
lastmod = "2011-10-25T17:44:00Z"
weight = 8633
keywords = [ "version", "mismatch", "update" ]
aliases = [ "/questions/8633" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Version mismatch while updating node information](/questions/8633/version-mismatch-while-updating-node-information)

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
<span id="post-8633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8633-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've written a PHP script that updates some tages of a previously retrieved node information. Before updating the node, I request a changeset and the current content of the node. I than make the required changes to the node's tags. So far so good.</p>
<p>When I try to upload the changes, I get the message: "Version mismatch: Provided 7, server had: 8 of Node 1479973945"</p>
<p>I don't understand why this happened because the version number is in the node's XML which I request just before making the changes. I have also tried incrementing teh version number by 1 but that gave the same error. Does someone know what the problem might be?</p>
<p>Chris</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-mismatch" rel="tag" title="see questions tagged &#39;mismatch&#39;">mismatch</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '11, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/8bae72e0f8dc1ba5ce53a5e1bd831f04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris%20Peters&#39;s gravatar image" />
<p><span>Chris Peters</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris Peters has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8633" class="comments-container">
&#10;</div>
<div id="comment-tools-8633" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8633-form-container" class="comment-form-container">
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

<span id="8635"></span>

<div id="answer-container-8635" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8635-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-8635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I do not know what you mean by "requesting a changeset" but obviously you have changed this node 8 times in a row.</p>
<p>Each time you upload a changeset with a "modify" section concerning that node, the node's version ID is incremented, and if you want to make another change to the node, you need to use the new version number. Simply opening a changeset does not increment anything of course, but that isn't required for retrieving data anyway - so what you should do is</p>
<ol>
<li>retrieve node data</li>
<li>create changeset</li>
<li>update node(s) using the version numbers from step 1</li>
<li>close changeset</li>
</ol>
<p>You should never increase the version number manually as this might lead to accidental overwriting of someone else's changes.</p>
<p>And, another thing: If you want to test your editing software, please do that on <a href="http://api.dev.openstreetmap.org">api.dev.openstreetmap.org</a> and not on the main site. Your experiments are visible to all, forever, and take up space in our database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '11, 09:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-8635" class="comments-container">
<span id="8645"></span>
<div id="comment-8645" class="comment">
<div id="post-8645-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>especially the <a href="http://api.dev.openstreetmap.org">api.dev.openstreetmap.org</a> bit</p>
</div>
<div id="comment-8645-info" class="comment-info">
<span class="comment-age">(25 Oct '11, 17:44)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
</div>
<div id="comment-tools-8635" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8635-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8634"></span>

<div id="answer-container-8634" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8634-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-8634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think, requesting a changeset already increases the version number. Look at the nodes history: <a href="http://www.openstreetmap.org/browse/node/1479973945/history">http://www.openstreetmap.org/browse/node/1479973945/history</a></p>
<p>Try to get the nodes tags without requesting the changeset, make the changes locally and upload them. Have you added action="modify" before uploading?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '11, 09:15</strong></p>
<img src="https://secure.gravatar.com/avatar/baddeab22266e1533be4ba4c9f3deb49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajoessen&#39;s gravatar image" />
<p><span>ajoessen</span><br />
<span class="score" title="168 reputation points">168</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajoessen has one accepted answer">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Oct '11, 09:16</strong> </span></p>
</div>
</div>
<div id="comments-container-8634" class="comments-container">
&#10;</div>
<div id="comment-tools-8634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8634-form-container" class="comment-form-container">
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

