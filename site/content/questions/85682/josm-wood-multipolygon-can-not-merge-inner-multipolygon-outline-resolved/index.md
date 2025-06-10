+++
type = "question"
title = "JOSM Wood multipolygon can not merge inner multipolygon outline. [Resolved]"
description = '''Scenario: Map a large wood and map the inner areas. One inside area is large and comprises different parts of farmland, orchard meadow using the. The outline is mapped then cut up to use outline members as member parts of the farming lands. Problem: AFTER, select the inner outline member and the woo...'''
date = "2022-09-22T11:40:00Z"
lastmod = "2022-11-23T08:54:00Z"
weight = 85682
keywords = [ "multipolygon" ]
aliases = [ "/questions/85682" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM Wood multipolygon can not merge inner multipolygon outline. \[Resolved\]](/questions/85682/josm-wood-multipolygon-can-not-merge-inner-multipolygon-outline-resolved)

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
<span id="post-85682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85682-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Scenario:</strong> Map a large wood and map the inner areas. One inside area is large and comprises different parts of farmland, orchard meadow using the. The outline is mapped then cut up to use outline members as member parts of the farming lands.</p>
<p><strong>Problem:</strong> AFTER, select the inner outline member and the woodland outline to update the multipolygon relation with Crt+Shft+B. Does not work. Only after removing the large inner outline members from the farming relations could the could the large inner outline be made part of the woodland MP as inner.</p>
<p>Example of wood area: <a href="https://www.openstreetmap.org/relation/14608182">https://www.openstreetmap.org/relation/14608182</a> Inside multipolygon farmland relation that could not be made inner afterwards: <a href="https://www.openstreetmap.org/relation/14608176">https://www.openstreetmap.org/relation/14608176</a></p>
<p>It's well conceivable the a large enveloping woodland is mapped around an already existing farming area to the point where mapping an enveloping outline of it all is truly uninviting highly laborious.</p>
<p><strong>Question:</strong> How is this achievable without having to resort to having to remove all the inside MP relations before making the inner outline members of the enveloping wood multipolygon relation.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '22, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ed39ace8cbefe3b5c45da98f60f5e34c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SekeRob&#39;s gravatar image" />
<p><span>SekeRob</span><br />
<span class="score" title="211 reputation points">211</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SekeRob has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Nov '22, 08:38</strong> </span></p>
</div>
</div>
<div id="comments-container-85682" class="comments-container">
&#10;</div>
<div id="comment-tools-85682" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85682-form-container" class="comment-form-container">
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

<span id="86207"></span>

<div id="answer-container-86207" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86207-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To close off this topic, the resolution for me was after much discovery to add the relation toolbox plugin and using the middle mouse button AKA mouse wheel click-hold and ctrl button to select the target multipolygon (MP) relation in the pop-up list, then double click the MP line in the tags sidepanel box to open the relation toolbox edit window, select the object(s) in the map that need adding to the MP, which get listed in the right half of the relation edit box add them to the active MP member list at left and assign the roles, individual or by selectiong multiple and using the Apply role function at bottom of the relation edit window.</p>
<p>NB It's important to first hit the S(elect) on keyboard before doing these steps as when the toolbox is open the A(dd)/S(elect) keys don't work.</p>
<p>Trial, error and lots of play, now it's the routine that works for me and of course the ctrl B to start the MP and Ctrl+Shift+B to add objects that are not themselves already an MP.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '22, 08:54</strong></p>
<img src="https://secure.gravatar.com/avatar/ed39ace8cbefe3b5c45da98f60f5e34c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SekeRob&#39;s gravatar image" />
<p><span>SekeRob</span><br />
<span class="score" title="211 reputation points">211</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SekeRob has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86207" class="comments-container">
&#10;</div>
<div id="comment-tools-86207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86207-form-container" class="comment-form-container">
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

