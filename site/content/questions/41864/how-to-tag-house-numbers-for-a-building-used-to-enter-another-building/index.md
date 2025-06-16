+++
type = "question"
title = "How to tag house numbers for a building used to enter another building?"
description = '''Hi, Out of curiosity question, I’m not sure there’s a practical use to this, but I’m getting fascinated by the tagging system of OSM and the way everything in the world is described by keys and values. But can this be tagged? This is where I live:  My home address is number 26 and I’m located in num...'''
date = "2015-03-23T18:21:00Z"
lastmod = "2015-03-23T19:51:00Z"
weight = 41864
keywords = [ "housenumbers", "address" ]
aliases = [ "/questions/41864" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag house numbers for a building used to enter another building?](/questions/41864/how-to-tag-house-numbers-for-a-building-used-to-enter-another-building)

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
<span id="post-41864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41864-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Out of curiosity question, I’m not sure there’s a practical use to this, but I’m getting fascinated by the tagging system of OSM and the way everything in the world is described by keys and values. But can this be tagged?</p>
<p>This is where I live:<br />
<img src="/upfiles/24-26.png" alt="24-26" /></p>
<p>My home address is number 26 and I’m located in number 26 building. However, the entrance door to number 26, and the mailboxes for number 26, are located at number 24. That’s two different buildings with a corridor dug in-between at some point. Now the street level at number 26 does not have a door, the space is the entrance to a nightclub (located underground). The door at number 24 has a sign saying ‘24–26’.</p>
<p>Is there any way to tag this (‘24 is the entrance to 26’)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '15, 18:21</strong></p>
<img src="https://secure.gravatar.com/avatar/834d570d7a91436154754db55059b3d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nclm&#39;s gravatar image" />
<p><span>nclm</span><br />
<span class="score" title="136 reputation points">136</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nclm has no accepted answers">0%</span> </br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '15, 18:31</strong> </span></p>
</div>
</div>
<div id="comments-container-41864" class="comments-container">
&#10;</div>
<div id="comment-tools-41864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41864-form-container" class="comment-form-container">
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

<span id="41866"></span>

<div id="answer-container-41866" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41866-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would add a node for the entrance of 24. building with tags:</p>
<ul>
<li>entrance=main</li>
<li>addr:housenumber=24;26</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '15, 19:51</strong></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RM87 has 20 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-41866" class="comments-container">
&#10;</div>
<div id="comment-tools-41866" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41866-form-container" class="comment-form-container">
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

