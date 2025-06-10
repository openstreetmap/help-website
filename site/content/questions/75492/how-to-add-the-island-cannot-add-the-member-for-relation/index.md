+++
type = "question"
title = "How to add the island (cannot add the member for relation)"
description = '''I&#x27;m very sorry for stupid question. I try to add some islands at the lake to the map.  lake; island 0; island 1; island 2.  And I try to add the relations for islands (because without relation the lake&#x27;s border is invalid and the islands are rendered invalid). I use the browser editor &#x27;iD&#x27;.  When I ...'''
date = "2020-07-01T12:13:00Z"
lastmod = "2020-07-01T14:02:00Z"
weight = 75492
keywords = [ "member", "island", "relation" ]
aliases = [ "/questions/75492" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add the island (cannot add the member for relation)](/questions/75492/how-to-add-the-island-cannot-add-the-member-for-relation)

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
<span id="post-75492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75492-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm very sorry for stupid question. I try to add some islands at the lake to the map.</p>
<ul>
<li><a href="https://www.openstreetmap.org/way/75888963">lake</a>;</li>
<li><a href="https://www.openstreetmap.org/way/821530452">island 0</a>;</li>
<li><a href="https://www.openstreetmap.org/way/821530453">island 1</a>;</li>
<li><a href="https://www.openstreetmap.org/way/821530454">island 2</a>.</li>
</ul>
<p>And I try to add the relations for islands (because without relation the lake's border is invalid and the islands are rendered invalid).</p>
<p>I use the browser editor 'iD'. When I click to '+' (add relation) I cannot see or type the lake as the parent relation at the editor combo box. How can i set the lake as the parent relation for islands?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-member" rel="tag" title="see questions tagged &#39;member&#39;">member</span> <span class="post-tag tag-link-island" rel="tag" title="see questions tagged &#39;island&#39;">island</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jul '20, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/4c2ea933480b0ef1eba7293b5d9225e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Taras&#39;s gravatar image" />
<p><span>Taras</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Taras has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '20, 12:14</strong> </span></p>
</div>
</div>
<div id="comments-container-75492" class="comments-container">
&#10;</div>
<div id="comment-tools-75492" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75492-form-container" class="comment-form-container">
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

<span id="75494"></span>

<div id="answer-container-75494" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75494-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>2 methods:</p>
<ol>
<li><p>Create the multipolygon at one of its member, (add its name, or a temporary tag as a trick for ease of recognition), then add it to other members.</p></li>
<li><p>Select all of them, then press "merge" in the right-click menu ("+" button). (be careful if this removes any tags from them)</p></li>
</ol>
<p>Check that they have correct <code>outer</code> (lake border) and <code>inner</code> (the islands) roles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '20, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '20, 14:04</strong> </span></p>
</div>
</div>
<div id="comments-container-75494" class="comments-container">
&#10;</div>
<div id="comment-tools-75494" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75494-form-container" class="comment-form-container">
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

