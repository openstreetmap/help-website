+++
type = "question"
title = "[closed] Why is the sequence number &quot;7&quot; on latest state.txt"
description = '''I&#x27;ve setup the replication process using osmosis, based on the hourly diffs, and it was running fine until today. Now, it does nothing, like there wasn&#x27;t anything else to update. But my database is not up-to-date, there are more than 2 months of diffs still to be applied. No errors output as well. A...'''
date = "2013-07-14T19:16:00Z"
lastmod = "2013-07-15T00:50:00Z"
weight = 24235
keywords = [ "state.txt", "replication", "sequence", "osmosis", "hourly" ]
aliases = [ "/questions/24235" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Why is the sequence number "7" on latest state.txt](/questions/24235/why-is-the-sequence-number-7-on-latest-statetxt)

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
<span id="post-24235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24235-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've setup the replication process using osmosis, based on the hourly diffs, and it was running fine until today. Now, it does nothing, like there wasn't anything else to update. But my database is not up-to-date, there are more than 2 months of diffs still to be applied. No errors output as well.</p>
<p>Acessing link:<a href="http://planet.openstreetmap.org/replication/hour/state.txt">Latest state.txt</a>, I found that (as of now) the sequence number is listed as "7":</p>
<p>#Sun Jul 14 18:02:07 UTC 2013<br />
sequenceNumber=7<br />
timestamp=2013-07-14T18\:00\:00Z<br />
</p>
<p>And it should be "7322" (as of now), as per the latest historic hourly diff link:<a href="http://planet.openstreetmap.org/replication/hour/000/007/322.state.txt">000/007/322</a></p>
<p>#Sun Jul 14 09:02:10 UTC 2013<br />
sequenceNumber=7322<br />
timestamp=2013-07-14T09\:00\:00Z</p>
<p>Am I doing something wrong? Did something changed (nothing on the osmosis documentation)? Is it a bug?</p>
<p>The command used is:</p>
<p>osmosis -v --rri workingDirectory=m:\OSM\osmosis\work --write-apidb-change host=<em>myserver</em>:<em>myport</em> password=<em>password</em> database=<em>database</em> user=<em>username</em> validateSchemaVersion=yes allowIncorrectSchemaVersion=no populateCurrentTables=yes</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-state.txt" rel="tag" title="see questions tagged &#39;state.txt&#39;">state.txt</span> <span class="post-tag tag-link-replication" rel="tag" title="see questions tagged &#39;replication&#39;">replication</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-hourly" rel="tag" title="see questions tagged &#39;hourly&#39;">hourly</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jul '13, 19:16</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>19 Sep '13, 21:49</strong> </span></p>
</div>
</div>
<div id="comments-container-24235" class="comments-container">
<span id="24239"></span>
<div id="comment-24239" class="comment">
<div id="post-24239-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>For info, this is also being discussed on the dev list - <a href="http://lists.openstreetmap.org/pipermail/dev/2013-July/027168.html">http://lists.openstreetmap.org/pipermail/dev/2013-July/027168.html</a> .</p>
</div>
<div id="comment-24239-info" class="comment-info">
<span class="comment-age">(14 Jul '13, 23:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24235" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24235-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Problem is not reproducible or outdated" by MCPicoli 19 Sep '13, 21:49

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24240"></span>

<div id="answer-container-24240" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24240-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Seems to be fixed, but no one (here or on the email list) gave an explanation. Maybe some kind of "leftover" of the redaction period?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '13, 00:50</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span> </br></br></p>
</div>
</div>
<div id="comments-container-24240" class="comments-container">
&#10;</div>
<div id="comment-tools-24240" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24240-form-container" class="comment-form-container">
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

