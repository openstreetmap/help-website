+++
type = "question"
title = "JOSM -  Adding admin_centre in relation"
description = '''I&#x27;d like to add a node (city centre) as a relation (admin_centre) to an administrative boundary, with JOSM, but how? This question was previously asked (and answered) here, but that only answered the part for the online website editor.'''
date = "2021-09-14T22:33:00Z"
lastmod = "2021-09-15T16:04:00Z"
weight = 81747
keywords = [ "josm", "nodes", "admin_centre", "relations" ]
aliases = [ "/questions/81747" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM - Adding admin_centre in relation](/questions/81747/josm-adding-admin_centre-in-relation)

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
<span id="post-81747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81747-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to add a node (city centre) as a relation (admin_centre) to an administrative boundary, with JOSM, but how?</p>
<p>This question was previously asked (and answered) <a href="/questions/71724/missing-admin_centre-in-relation">here</a>, but that only answered the part for the online website editor.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-admin_centre" rel="tag" title="see questions tagged &#39;admin_centre&#39;">admin_centre</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '21, 22:33</strong></p>
<img src="https://secure.gravatar.com/avatar/acd37670cb9754ec79d0ae8418893317?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Seb&#39;s gravatar image" />
<p><span>Seb</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Seb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81747" class="comments-container">
&#10;</div>
<div id="comment-tools-81747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81747-form-container" class="comment-form-container">
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

<span id="81748"></span>

<div id="answer-container-81748" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81748-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This should be relatively straightforward in JOSM:</p>
<ol>
<li>Select a way that forms part of the existing relation. You should then see the boundary relation under "Member of" in the Tags/Memberships pane.</li>
<li>Right clicking on the boundary relation listing you should be able to select an option to <em>Edit</em> the relation. This should open a window with the title "Edit relation #...".</li>
<li>Select the node to be designated the admin centre in the main window it will appear in the selection list at the bottom right of the Relation window.</li>
<li>Select the node in the selection list in the relations window.</li>
<li>Use the top button immediately to the left of the selection list to push the node onto the list of elements for the relation at the left and manually enter <code>admin_centre</code> as the role.</li>
</ol>
<p>More information on the relation editor can be found in the <a href="https://josm.openstreetmap.de/wiki/Help/Dialog/RelationEditor">online help</a>. There is also a completely different workflow using the <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Relation_Toolbox">Relation Toolbox</a> Plugin if you have that installed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '21, 01:55</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-81748" class="comments-container">
<span id="81751"></span>
<div id="comment-81751" class="comment">
<div id="post-81751-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Excellent extensive explanation, thank you!</p>
<p>On my system the "Edit Relation" window of JOSM opens and replaces the content of the main window, so I had to use a workaround. I had to select both the boundary and the admin_centre and then open the edit relation mode. Then I can add 'all' relations (no possibility of selecting just one), then JOSM gives a circular dependency warning and skips adding the boundary (which is great), and then it adds the admin_centre and then I can give it the proper role. If you have a way to get JOSM running as you describe, I'm interested (since it sounds more useful).</p>
</div>
<div id="comment-81751-info" class="comment-info">
<span class="comment-age">(15 Sep '21, 09:57)</span> <span class="comment-user userinfo">Seb</span>
</div>
</div>
<span id="81756"></span>
<div id="comment-81756" class="comment">
<div id="post-81756-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't think I did anything to get JOSM to do this in multiple windows. I think you may be experiencing a bug.</p>
<p>The only workaround I can suggest is to use the Relation Toolbox plugin which only occupies a single pane on the same side menu as the tags. The steps are broadly similar, but once a relation is selected you add the new element with the plus button in the pane and select the role from a dropdown menu.</p>
</div>
<div id="comment-81756-info" class="comment-info">
<span class="comment-age">(15 Sep '21, 12:27)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="81759"></span>
<div id="comment-81759" class="comment">
<div id="post-81759-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, got it :)</p>
</div>
<div id="comment-81759-info" class="comment-info">
<span class="comment-age">(15 Sep '21, 16:04)</span> <span class="comment-user userinfo">Seb</span>
</div>
</div>
</div>
<div id="comment-tools-81748" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81748-form-container" class="comment-form-container">
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

