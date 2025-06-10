+++
type = "question"
title = "How can I revert an edit?"
description = '''Alright, so I was mapping on JOSM, and I accidently deleted something by mistake. Normally, this wouldn&#x27;t be a big issue. However, I made a lot of edits afterwards that if I undoed the deletion of the building, the edits made afterward would dissapear. I&#x27;ve heard a lot about reverting edits in JOSM,...'''
date = "2020-05-19T21:59:00Z"
lastmod = "2020-05-22T10:21:00Z"
weight = 74915
keywords = [ "josm", "edits", "revert" ]
aliases = [ "/questions/74915" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I revert an edit?](/questions/74915/how-can-i-revert-an-edit)

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
<span id="post-74915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74915-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Alright, so I was mapping on JOSM, and I accidently deleted something by mistake. Normally, this wouldn't be a big issue. However, I made a lot of edits afterwards that if I undoed the deletion of the building, the edits made afterward would dissapear. I've heard a lot about reverting edits in JOSM, but I'm not entirely sure how to do it. Any help would be appricated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-edits" rel="tag" title="see questions tagged &#39;edits&#39;">edits</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 May '20, 21:59</strong></p>
<img src="https://secure.gravatar.com/avatar/b3c43e68353fb119848cbad80c687109?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheAdventurer64&#39;s gravatar image" />
<p><span>TheAdventurer64</span><br />
<span class="score" title="139 reputation points">139</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheAdventurer64 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74915" class="comments-container">
&#10;</div>
<div id="comment-tools-74915" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74915-form-container" class="comment-form-container">
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

<span id="74917"></span>

<div id="answer-container-74917" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74917-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<h3 id="if-you-have-already-uploaded">If you have already uploaded</h3>
<p>JOSM has a <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Reverter">reverter plugin</a> for this. I think the <em>Partial reverts</em> section on the wiki page has what you're after.</p>
<p>If you only do a selective upload of the building (and nodes) you had deleted (via <em>File</em>&gt;<em>Upload selection</em>), then delete the data layer, you should end up with the building restored and the rest of the edit intact.</p>
<h3 id="if-you-have-not-uploaded">If you have not uploaded</h3>
<p>You should be able to select the modified objects with a search (<code>CTRL+F</code>) for "modifed" and upload just those objects via <em>File</em>&gt;<em>Upload selection</em> (<code>CTRL+ALT+SHIFT+U</code>).</p>
<p>Alternatively, you can re-download the area as a new layer and selectively merge (<em>Edit</em>&gt;<em>Merge Selection</em>) the changes you do want to upload across to the new layer leaving the deletion behind in the original layer. You can then upload the new layer as normal.</p>
<p>In both of these options (especially the first), you should be weary of leaving orphaned nodes (ones without tags or "parent" objects) if you have changed the geometry of existing ways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '20, 01:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 May '20, 10:36</strong> </span></p>
</div>
</div>
<div id="comments-container-74917" class="comments-container">
<span id="74918"></span>
<div id="comment-74918" class="comment">
<div id="post-74918-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, but I am confused onto how to use the modified tool. Could I send you a DM via OSM?</p>
</div>
<div id="comment-74918-info" class="comment-info">
<span class="comment-age">(20 May '20, 01:24)</span> <span class="comment-user userinfo">TheAdventurer64</span>
</div>
</div>
<span id="74950"></span>
<div id="comment-74950" class="comment">
<div id="post-74950-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Better try to solve it here so that others can profit from the resolution, too.<br />
Could you share the changeset and the id of the deleted building?</p>
</div>
<div id="comment-74950-info" class="comment-info">
<span class="comment-age">(22 May '20, 10:07)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="74951"></span>
<div id="comment-74951" class="comment">
<div id="post-74951-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is no separate modified tool, it is a search term within the search tool. I will try to edit for clarity.</p>
<p>It wasn't clear to me from your initial post whether you had uploaded the edits yet or not. Have you?</p>
</div>
<div id="comment-74951-info" class="comment-info">
<span class="comment-age">(22 May '20, 10:21)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-74917" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74917-form-container" class="comment-form-container">
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

