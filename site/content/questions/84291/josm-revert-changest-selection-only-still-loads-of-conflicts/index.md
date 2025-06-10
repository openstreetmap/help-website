+++
type = "question"
title = "JOSM Revert Changest - &#x27;Selection Only&#x27; - Still loads of Conflicts"
description = '''Hi I want to revert just one entity amended in a changset using JOSM&#x27;s &#x27;reverter&#x27; plugin. I have to download the whole changeset as the other options are greyed out. It gives a warning dialog about 22 conflicts. I select the one object I want to revert. I go back to the &#x27;Revert Changset&#x27; command &amp;am...'''
date = "2022-04-27T17:00:00Z"
lastmod = "2023-04-29T15:22:00Z"
weight = 84291
keywords = [ "conflicts", "josm", "selection", "revert" ]
aliases = [ "/questions/84291" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM Revert Changest - 'Selection Only' - Still loads of Conflicts](/questions/84291/josm-revert-changest-selection-only-still-loads-of-conflicts)

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
<span id="post-84291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84291-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I want to revert just one entity amended in a changset using JOSM's 'reverter' plugin.</p>
<p>I have to download the whole changeset as the other options are greyed out.</p>
<p>It gives a warning dialog about 22 conflicts.</p>
<p>I select the one object I want to revert.</p>
<p>I go back to the 'Revert Changset' command &amp; select 'Revert selection only' which is now ungreyed, &amp; click revert.</p>
<p>I then click the 'upload changeset' command, but it won't allow it as it says there are still 22 conflicts to be resolved which have no association with the object I want to revert &amp; about which I have no knowledge.</p>
<p>How do I ignore/resolve these conflicts so they don't get uploaded?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-conflicts" rel="tag" title="see questions tagged &#39;conflicts&#39;">conflicts</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-selection" rel="tag" title="see questions tagged &#39;selection&#39;">selection</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '22, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-84291" class="comments-container">
&#10;</div>
<div id="comment-tools-84291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84291-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="84295"></span>

<div id="answer-container-84295" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84295-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The revert changeset command just loads the changes object in a layer and undoes any changes in the changeset, upload still happens separately. I've done partial reverts and I don't think I've ever used the revert selection feature.</p>
<p>If you have downloaded the old version of all of the data and just want to revert some of it then you can select that and just "upload selection" in the usual way.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Reverter#Partial_reverts">Description of this in the wiki</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '22, 20:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-84295" class="comments-container">
&#10;</div>
<div id="comment-tools-84295" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84295-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84297"></span>

<div id="answer-container-84297" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84297-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If I want to do this I first download the area in question in the usual way, then select the object that I want to revert and only then call the reverter plugin. Then I'm always able to chose the "revert selection only" option. Usually, I leave the "Downlaod as new layer" option unticked. Does that work for you?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '22, 22:47</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-84297" class="comments-container">
&#10;</div>
<div id="comment-tools-84297" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84297-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87189"></span>

<div id="answer-container-87189" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87189-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Check <a href="https://help.openstreetmap.org/questions/74915/how-can-i-revert-an-edit">https://help.openstreetmap.org/questions/74915/how-can-i-revert-an-edit</a> and <a href="https://community.openstreetmap.org/t/josm-want-to-review-changes-before-upload/81549/2">https://community.openstreetmap.org/t/josm-want-to-review-changes-before-upload/81549/2</a></p>
<blockquote>
<p>You should be able to select the modified objects with a search (CTRL+F) for "modifed" and upload just those objects via File&gt;Upload selection (CTRL+ALT+SHIFT+U).</p>
</blockquote>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '23, 15:22</strong></p>
<img src="https://secure.gravatar.com/avatar/09f491ff872d3ed578d7e246d1bf30cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xerusf&#39;s gravatar image" />
<p><span>xerusf</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xerusf has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87189" class="comments-container">
&#10;</div>
<div id="comment-tools-87189" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87189-form-container" class="comment-form-container">
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

