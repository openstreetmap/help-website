+++
type = "question"
title = "What to do when changesets overlap"
description = '''Let&#x27;s say there are two users, &quot;M&quot; and &quot;N&quot;. User &quot;N&quot; downloads the data for an area (Which I&#x27;ll call &quot;A1&quot;) at T=0 and starts happily editing it. Some time after, user &quot;M&quot; downloads almost the same area (&quot;A2&quot;), at T=1, and edits it. At T=2, user &quot;M&quot; uploads the changes made (Changeset &quot;C1&quot;). At T=8 (...'''
date = "2012-10-18T23:48:00Z"
lastmod = "2012-10-19T07:52:00Z"
weight = 17006
keywords = [ "behaviour", "changeset", "stale", "quality", "overlapping" ]
aliases = [ "/questions/17006" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What to do when changesets overlap](/questions/17006/what-to-do-when-changesets-overlap)

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
<span id="post-17006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17006-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Let's say there are two users, "M" and "N".</p>
<p>User "N" downloads the data for an area (Which I'll call "A1") at T=0 and starts happily editing it.</p>
<p>Some time after, user "M" downloads almost the same area ("A2"), at T=1, and edits it. At T=2, user "M" uploads the changes made (Changeset "C1").</p>
<p>At T=8 (that is, 6 hours after "M" uploaded "C1"), user "N" uploads his changes, creating "C2".</p>
<p>However, "N" notes that a large part of the items he uploaded in "C2" were already uploaded in "C1" by "M". That is, the dataset used by "N" was stale and did not show "C1" changes until the moment "C2" was uploaded.</p>
<p>Assuming that the quality of the overlapping parts of "C1" and "C2" is equivalent (very similar tracing, similar tagging, etc.) and therefore it is not possible to rule based on the quality of the data, what is the expected behaviour of "M" and "N"?</p>
<p>If needed, I could provide the users and changeset IDs, but based only on what I wrote, what should be done?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-behaviour" rel="tag" title="see questions tagged &#39;behaviour&#39;">behaviour</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-stale" rel="tag" title="see questions tagged &#39;stale&#39;">stale</span> <span class="post-tag tag-link-quality" rel="tag" title="see questions tagged &#39;quality&#39;">quality</span> <span class="post-tag tag-link-overlapping" rel="tag" title="see questions tagged &#39;overlapping&#39;">overlapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Oct '12, 23:48</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-17006" class="comments-container">
<span id="17014"></span>
<div id="comment-17014" class="comment">
<div id="post-17014-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Editing for several hours without uploading is in general at not so good idea. I suggest to upload at latest an hour after having made changes, both to keep the changesets small and to minimize such conflicts as the one mentioned above.</p>
<p>This advice doesn't solve your current problem, but it helps avoiding the same kind of problem in the future. For a solution, please see cartinus' answer.</p>
</div>
<div id="comment-17014-info" class="comment-info">
<span class="comment-age">(19 Oct '12, 07:38)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-17006" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17006-form-container" class="comment-form-container">
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

<span id="17010"></span>

<div id="answer-container-17010" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17010-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-17010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MCPicoli has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Who downloaded the data first is completely irrelevant.</p>
<p>Depending on how much time "N" has he can either:</p>
<ul>
<li>simply revert C2</li>
<li>check all objects in C2 one by one to see if they are somehow better than the existing objects (including those from C1) and remove them if not.</li>
</ul>
<p>If you are using JOSM (looks like it as this workflow is (nearly?) impossible with Potlatch), then you should <a href="http://josm.openstreetmap.de/wiki/Help/Action/UpdateData">update the data</a> from the server just before you upload, if you have taken a long time to make your edits.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '12, 00:29</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Oct '12, 00:31</strong> </span></p>
</div>
</div>
<div id="comments-container-17010" class="comments-container">
&#10;</div>
<div id="comment-tools-17010" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17010-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17015"></span>

<div id="answer-container-17015" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17015-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just to make this clear, a problem only occurrs if both users have added new data (in which case it would be desirable for the "better" data to prevail, whatever that is). Had both users made modifications to the same existing data, the API would have reported a version conflict upon receiving C2, and user N would have to go through appropriate conflict resolution steps in his editor before the changes are accepted.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '12, 07:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17015" class="comments-container">
&#10;</div>
<div id="comment-tools-17015" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17015-form-container" class="comment-form-container">
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

