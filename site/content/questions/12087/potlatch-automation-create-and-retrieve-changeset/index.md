+++
type = "question"
title = "Potlatch automation: create and retrieve changeset"
description = '''Goal: direct user to potlatch where they specify a closed path. Then get the points of that closed path for later use. User will not know much about OSM. This is being driven from a phone, so I want a web solution. Interactively, I can accomplish this by creating the path; saving it; going to histor...'''
date = "2012-04-17T13:53:00Z"
lastmod = "2012-04-17T16:01:00Z"
weight = 12087
keywords = [ "potlatch2", "changesets", "paths" ]
aliases = [ "/questions/12087" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Potlatch automation: create and retrieve changeset](/questions/12087/potlatch-automation-create-and-retrieve-changeset)

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
<span id="post-12087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12087-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Goal: direct user to potlatch where they specify a closed path. Then get the points of that closed path for later use. User will not know much about OSM. This is being driven from a phone, so I want a web solution.</p>
<p>Interactively, I can accomplish this by creating the path; saving it; going to history; getting my changeset id and then use <a href="https://www.openstreetmap.org/browse/changeset/">https://www.openstreetmap.org/browse/changeset/</a>&lt;changesetid&gt;.</p>
<p>It feels like I need to setup my own potlatch server and modify it so I can pass a location and a changeset description in; then I can get changesets within a bounding box and look for my description.</p>
<p>Question: Am I using the right tool. Is there a better way.</p>
<p>Edit: Yes, I want to see the points. Here is a sample application: I want to have a phone scavenger hunt. The user is going to draw out the field/pitch/playspace on their phone; then I am going to scatter (electronically, not physically) prizes, clues or what not inside that field. Then they walk around and collect the prizes. I have the location of the phone and all my created items; I am looking for a way to allow a user to fence-in the application. I could do this on the phone; but I would rather do it on the web as the boundary they create could well be shared/re-used. (via OSM) Is that better?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-changesets" rel="tag" title="see questions tagged &#39;changesets&#39;">changesets</span> <span class="post-tag tag-link-paths" rel="tag" title="see questions tagged &#39;paths&#39;">paths</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Apr '12, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/1ee5f50115a779ed34c526cfbf0f88d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ts2000&#39;s gravatar image" />
<p><span>ts2000</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ts2000 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Apr '12, 17:23</strong> </span></p>
</div>
</div>
<div id="comments-container-12087" class="comments-container">
<span id="12088"></span>
<div id="comment-12088" class="comment">
<div id="post-12088-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you explain what you mean by "Then get the points of that closed path for later use". Is that for editing ? If not, do you just need the list of nodes for a special rendering on your phone app ? Edit and enhance your question, please. If it is not for editing, Potlach is not required and you have other means to retrieve the list of points.</p>
</div>
<div id="comment-12088-info" class="comment-info">
<span class="comment-age">(17 Apr '12, 15:19)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-12087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12087-form-container" class="comment-form-container">
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

<span id="12089"></span>

<div id="answer-container-12089" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12089-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question isn't very clear, but it seems unlikely that Potlatch is the tool you want.</p>
<p>Potlatch is the web-based Flash editor on the osm.org website (and several other places). As it's written in Flash and designed for desktop screen sizes, it is unlikely to function well on phones.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Apr '12, 16:01</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-12089" class="comments-container">
&#10;</div>
<div id="comment-tools-12089" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12089-form-container" class="comment-form-container">
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

