+++
type = "question"
title = "Should i use revert or undelete to restore deleted data?"
description = '''I have to revert a changeset, 16464958, where a user deleted some of the objects. we have agreed on reverting the change.  I see i have two options of reverting or undeleting using JOSM plugins. I want to understand what is the difference in these two. As i understand, reverter will create a new cha...'''
date = "2013-07-24T08:57:00Z"
lastmod = "2013-07-25T10:26:00Z"
weight = 24513
keywords = [ "undelete", "version", "revert" ]
aliases = [ "/questions/24513" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Should i use revert or undelete to restore deleted data?](/questions/24513/should-i-use-revert-or-undelete-to-restore-deleted-data)

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
<span id="post-24513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24513-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have to revert a changeset, 16464958, where a user deleted some of the objects. we have agreed on reverting the change.</p>
<p>I see i have two options of reverting or undeleting using JOSM plugins. I want to understand what is the difference in these two. As i understand, reverter will create a new change which is opposite of the change. So i get the old object id and new version. Since it is like normal editing i also get to handle conflicts and review changes before updating.</p>
<p>On trying to revert in JOSM, i am using the Modified object renderer to track the objects to be changed. i see that in buildings the nodes are marked to be reverted by the way is not, whereas the roads are marked to be reverted. Will be buildings be reverted or is it a bug? i have not uploaded yet.</p>
<p>I don't know much about undelete, will it use new version or restore older version? and since it works directly with objects, do i need to restore deleted nodes of a way to restore the way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-undelete" rel="tag" title="see questions tagged &#39;undelete&#39;">undelete</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jul '13, 08:57</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jul '13, 10:59</strong> </span></p>
</div>
</div>
<div id="comments-container-24513" class="comments-container">
<span id="24514"></span>
<div id="comment-24514" class="comment">
<div id="post-24514-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please explain which tool you are talking about that offers "reverting" and "undeleting". These actions are not directly implemented in the API, so what exactly the difference is depends on which tool you are using.</p>
</div>
<div id="comment-24514-info" class="comment-info">
<span class="comment-age">(24 Jul '13, 09:27)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="24515"></span>
<div id="comment-24515" class="comment">
<div id="post-24515-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(just in case future readers of this question aren't aware of it) there's an API that can be used for testing and development purposes at <a href="http://api06.dev.openstreetmap.org/">http://api06.dev.openstreetmap.org/</a> which you can use for testing the impact of whatever method it is that you're considering using.</p>
</div>
<div id="comment-24515-info" class="comment-info">
<span class="comment-age">(24 Jul '13, 10:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="24516"></span>
<div id="comment-24516" class="comment">
<div id="post-24516-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span></span><span>@Frederik Ramm</span>: Both are JOSM plugins.</p>
<p><span></span><span>@SomeoneElse</span>: I have tried that, but it failed. maybe because there are no objects with the given ids. Deleted objects should be created, and in history browser in josm i can see negative id on them. But they fail on upload. I'll try uploading individual objects (partial revert), see if it works .</p>
</div>
<div id="comment-24516-info" class="comment-info">
<span class="comment-age">(24 Jul '13, 11:04)</span> <span class="comment-user userinfo">amritkarma</span>
</div>
</div>
<span id="24523"></span>
<div id="comment-24523" class="comment">
<div id="post-24523-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes - with the dev api you'll need to create test data there before you can test deleting it :)</p>
</div>
<div id="comment-24523-info" class="comment-info">
<span class="comment-age">(24 Jul '13, 12:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="24527"></span>
<div id="comment-24527" class="comment">
<div id="post-24527-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i tried uploading individual objects in the dev server and found that JOSM is trying to modify them, instead of create. I saved the changed file before uploading and opened it in a text editor. There are objects for which actions for modify and delete are recorded but not for create.</p>
</div>
<div id="comment-24527-info" class="comment-info">
<span class="comment-age">(24 Jul '13, 13:08)</span> <span class="comment-user userinfo">amritkarma</span>
</div>
</div>
</div>
<div id="comment-tools-24513" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24513-form-container" class="comment-form-container">
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

<span id="24528"></span>

<div id="answer-container-24528" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24528-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What I tend to do, if a new mapper has made a complete horlicks of something but has added some genuine new stuff that should be kept, is (after appropriate discussion with the the new mapper) to revert the original changeset but then look at the deletions in that reversion changeset and then undelete those (and fix and join as appropriate - with a new mapper a bit of tidying is to be expected). I'd tend to use Potlatch 1 or rawedit for undeletes, but "other editors are available".</p>
<p>Re the create vs modify point, you'd expect the reversion plugin to be only doing deletes and modifies because the data either already was there and shouldn't be or already was there but was deleted.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '13, 13:13</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-24528" class="comments-container">
<span id="24552"></span>
<div id="comment-24552" class="comment">
<div id="post-24552-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the data was there( my edits) then it was deleted (other's edit). Now i need it to be in state i left. Since it is not there now, shouldn't it be created again (maybe with new id)?</p>
</div>
<div id="comment-24552-info" class="comment-info">
<span class="comment-age">(25 Jul '13, 06:15)</span> <span class="comment-user userinfo">amritkarma</span>
</div>
</div>
<span id="24560"></span>
<div id="comment-24560" class="comment">
<div id="post-24560-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i read the josm_file_format <a href="https://wiki.openstreetmap.org/wiki/JOSM_file_format">https://wiki.openstreetmap.org/wiki/JOSM_file_format</a> which states that create is done by giving negaive id and does not use the action attribute.</p>
</div>
<div id="comment-24560-info" class="comment-info">
<span class="comment-age">(25 Jul '13, 10:20)</span> <span class="comment-user userinfo">amritkarma</span>
</div>
</div>
<span id="24561"></span>
<div id="comment-24561" class="comment">
<div id="post-24561-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well, "deleted" doesn't mean "gone away for ever"; it just means "marked as deleted and not currently appearing in the data". To take an example from one of my recent changesets, <a href="https://www.openstreetmap.org/browse/way/231022984/history">way 231022984</a> was deleted in <a href="https://www.openstreetmap.org/browse/changeset/17065699">changeset 17065699</a>. If I was to revert that changeset, the way would be "undeleted" and appear in the data again. Using the same ID (rather than creating a new one) is much more traceable.</p>
</div>
<div id="comment-24561-info" class="comment-info">
<span class="comment-age">(25 Jul '13, 10:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24528" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24528-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24556"></span>

<div id="answer-container-24556" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24556-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have had trials, and i found the undelete plugin more useful. It is lengthy as we have to list out the id and type of object.</p>
<p>I have not thoroughly tested reverter on modified object, but i suppose it works well looking at some of the instances where it was applied during this trial. As for the deleted objects, it restores the nodes, but closed ways are converted to linear feature (maybe the end node is not added).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '13, 09:13</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-24556" class="comments-container">
&#10;</div>
<div id="comment-tools-24556" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24556-form-container" class="comment-form-container">
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

