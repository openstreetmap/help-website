+++
type = "question"
title = "Revert a changeset with users permission"
description = '''Hi All, Could someone with more experience than me please revert a changeset for me? I have already contacted the user (cwarnock) regarding changeset #37668263 and he has agreed to the revert as I explained to him that I was in the middle of making multiple edits when he made his before I could save...'''
date = "2016-03-09T11:11:00Z"
lastmod = "2016-03-10T16:38:00Z"
weight = 48591
keywords = [ "changeset", "revert" ]
aliases = [ "/questions/48591" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Revert a changeset with users permission](/questions/48591/revert-a-changeset-with-users-permission)

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
<span id="post-48591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48591-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>Could someone with more experience than me please revert a changeset for me? I have already contacted the user (cwarnock) regarding changeset #37668263 and he has agreed to the revert as I explained to him that I was in the middle of making multiple edits when he made his before I could save mine, causing a conflict of versions (error status code 409).</p>
<p>My edits match his in any case so once his changeset is reverted and I save my edits, the result should be the same.</p>
<p>Many thanks, Gary</p>
<p>Edit: error message below -</p>
<p><img src="http://help.openstreetmap.org/upfiles/OSM_error.JPG" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '16, 11:11</strong></p>
<img src="https://secure.gravatar.com/avatar/e4d4559d0889de101611f786984e792e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gaz3434&#39;s gravatar image" />
<p><span>gaz3434</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gaz3434 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '16, 12:21</strong> </span></p>
</div>
</div>
<div id="comments-container-48591" class="comments-container">
<span id="48594"></span>
<div id="comment-48594" class="comment">
<div id="post-48594-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Just a quick note that reverting will increase the version numbers as the items are changed back to their previous state in a new version, not restore previous version numbers, so it probably won't help with the conflict of versions (as I understand it).</p>
</div>
<div id="comment-48594-info" class="comment-info">
<span class="comment-age">(09 Mar '16, 12:02)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="48595"></span>
<div id="comment-48595" class="comment">
<div id="post-48595-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks EdLoach, but I think it's more a case of the particular edit in question was where I combined several sections of an undefined line and changed it to a footpath, whereas the other user just changed the undefined sections to a footpath.</p>
<p>Perhaps I'm wrong but it would still be useful to have the changeset reverted to try as I have a lot of unsaved changes that I don't want to lose because of this error.</p>
</div>
<div id="comment-48595-info" class="comment-info">
<span class="comment-age">(09 Mar '16, 12:19)</span> <span class="comment-user userinfo">gaz3434</span>
</div>
</div>
<span id="48596"></span>
<div id="comment-48596" class="comment">
<div id="post-48596-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, cwarnock had already uploaded those paths a few days ago without tagging them as anything. To revert changeset #37668263 will still leave the untagged ways. Do you still want changeset #37668263 rebverted?</p>
</div>
<div id="comment-48596-info" class="comment-info">
<span class="comment-age">(09 Mar '16, 13:05)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="48597"></span>
<div id="comment-48597" class="comment">
<div id="post-48597-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To echo what EdLoach said, a revert won't avoid the 409 error. <a href="http://help.openstreetmap.org/users/12070/gaz3434"></a><a href="http://help.openstreetmap.org/users/12070/gaz3434">@gaz3434</a> what editor were you using? Maybe there's some other way around the problem?</p>
<p>EDIT: Looks like iD from user's edit history. I suspect that there's no easy workaround. From memory someone did once manage to intercept the changes sent to the OSM server (details are on this site; maybe try searching the tag "ideditor") but it's far from straightforward. It's probably quicker to redo your changes.</p>
<p>EDIT 2: Found it! See <a href="https://help.openstreetmap.org/questions/36044/error-saving-changes-version-mismatch">https://help.openstreetmap.org/questions/36044/error-saving-changes-version-mismatch</a> and <a href="https://help.openstreetmap.org/questions/34325/id-conflict-of-a-bigger-edit-not-resolvable-in-web-editor-because-of-changed-telephone-number?page=1&amp;focusedAnswerId=34340#34340">https://help.openstreetmap.org/questions/34325/id-conflict-of-a-bigger-edit-not-resolvable-in-web-editor-because-of-changed-telephone-number?page=1&amp;focusedAnswerId=34340#34340</a> . Still probably quicker to redo your edits though.</p>
</div>
<div id="comment-48597-info" class="comment-info">
<span class="comment-age">(09 Mar '16, 13:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48603"></span>
<div id="comment-48603" class="comment not_top_scorer">
<div id="post-48603-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the responses. Yes, I'm using iD editor. So reverting the changeset won't avoid the 409 error? Is it worth a try seeing the edits cwarnock made were fairly minor and mine are quite extensive? Even if it doesn't work I can still go back and re-do the edits that cwarnock made.</p>
<p>Let me know if someone is willing to revert the changeset for me, thanks.</p>
</div>
<div id="comment-48603-info" class="comment-info">
<span class="comment-age">(10 Mar '16, 11:17)</span> <span class="comment-user userinfo">gaz3434</span>
</div>
</div>
<span id="48614"></span>
<div id="comment-48614" class="comment">
<div id="post-48614-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As others said, it won't help. The iD editor compares the local version number of the object with the one in the database. Since that number is already higher, no matter which change you make to the entry in the database, the version number will be higher than the one in your editor. It does not compare the characteristics (tags) of nodes and ways, just the version field</p>
</div>
<div id="comment-48614-info" class="comment-info">
<span class="comment-age">(10 Mar '16, 16:38)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-48591" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-48591-form-container" class="comment-form-container">
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

<span id="48604"></span>

<div id="answer-container-48604" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48604-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A revert of <a href="http://www.openstreetmap.org/changeset/37668263">http://www.openstreetmap.org/changeset/37668263</a> is irrelevant, actually - there are no new objects in there.</p>
<p>If you can follow <a href="https://help.openstreetmap.org/questions/34325/id-conflict-of-a-bigger-edit-not-resolvable-in-web-editor-because-of-changed-telephone-number?page=1&amp;focusedAnswerId=34340#34340">https://help.openstreetmap.org/questions/34325/id-conflict-of-a-bigger-edit-not-resolvable-in-web-editor-because-of-changed-telephone-number?page=1&amp;focusedAnswerId=34340#34340</a> to work around the 409 error then good luck!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '16, 11:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-48604" class="comments-container">
&#10;</div>
<div id="comment-tools-48604" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48604-form-container" class="comment-form-container">
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

