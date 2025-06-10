+++
type = "question"
title = "[closed] Overpass: user clause"
description = '''Does the user clause select all elements that have been last touched or ever touched by a specified user? I made this clause with an &#x27;out meta&#x27; action and there are many other users listed.'''
date = "2013-02-26T13:36:00Z"
lastmod = "2013-02-27T11:49:00Z"
weight = 20304
keywords = [ "overpass", "user", "query" ]
aliases = [ "/questions/20304" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Overpass: user clause](/questions/20304/overpass-user-clause)

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
<span id="post-20304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20304-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Does the user clause select all elements that have been <strong>last</strong> touched or <strong>ever</strong> touched by a specified user? I made this clause with an 'out meta' action and there are many other users listed.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-user" rel="tag" title="see questions tagged &#39;user&#39;">user</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '13, 13:36</strong></p>
<img src="https://secure.gravatar.com/avatar/2c52393df51ceb5327c1e19e3b0efbfe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mattes_tili&#39;s gravatar image" />
<p><span>Mattes_tili</span><br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mattes_tili has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>01 Mar '13, 14:09</strong> </span></p>
</div>
</div>
<div id="comments-container-20304" class="comments-container">
&#10;</div>
<div id="comment-tools-20304" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20304-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Mattes_tili 01 Mar '13, 14:09

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20333"></span>

<div id="answer-container-20333" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20333-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-20333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It does only select elements that have been <em>last</em> touched by a specific user. In particular, a query of the form</p>
<pre><code>node(user:&quot;Roland Olbricht&quot;);out meta;</code></pre>
<p>should only show the mentioned person in the meta attributes.</p>
<p>If you see more than one user, then there is a bug and I would be happy to get details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '13, 08:43</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-20333" class="comments-container">
<span id="20337"></span>
<div id="comment-20337" class="comment">
<div id="post-20337-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I tried to reproduce the output data, but it seems that I just messed up my data. Thank you for your answer and sorry for my wrong informations :).</p>
</div>
<div id="comment-20337-info" class="comment-info">
<span class="comment-age">(27 Feb '13, 11:49)</span> <span class="comment-user userinfo">Mattes_tili</span>
</div>
</div>
</div>
<div id="comment-tools-20333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20333-form-container" class="comment-form-container">
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

