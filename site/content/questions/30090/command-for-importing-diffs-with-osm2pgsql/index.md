+++
type = "question"
title = "Command for importing diffs with osm2pgsql"
description = '''Does anyone have a sample/tutorial command call on how I can import diffs from planet osm using osm2pgsql? I know you use the osm2pgsql -c --slim ...other stuff to import osm data to the database initially. Do you use the -a (append) to import the diffs?  The help documents are rather sparse on this...'''
date = "2014-01-22T15:06:00Z"
lastmod = "2014-01-22T17:04:00Z"
weight = 30090
keywords = [ "postgresql", "osm", "osm2pgsql", "postgres" ]
aliases = [ "/questions/30090" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Command for importing diffs with osm2pgsql](/questions/30090/command-for-importing-diffs-with-osm2pgsql)

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
<span id="post-30090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30090-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Does anyone have a sample/tutorial command call on how I can import diffs from planet osm using osm2pgsql?</p>
<p>I know you use the osm2pgsql -c --slim ...other stuff to import osm data to the database initially.<br />
Do you use the -a (append) to import the diffs?<br />
</p>
<p>The help documents are rather sparse on this topic.</p>
<p>Thank you</p>
<p>A</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '14, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/1df0b0daef7049f4aa8561e4c29fd7de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fisherman12i&#39;s gravatar image" />
<p><span>Fisherman12i</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fisherman12i has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-30090" class="comments-container">
&#10;</div>
<div id="comment-tools-30090" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30090-form-container" class="comment-form-container">
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

<span id="30094"></span>

<div id="answer-container-30094" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30094-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's some info on <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">this switch2osm page</a> (go down to "updating") and also <a href="https://wiki.openstreetmap.org/wiki/Minutely_Mapnik">in the wiki here</a>. The last time I set this up (with no prior experience) I was able to follow a combination of those two. That was on Ubuntu though - I've no idea if anyone's ever tried Windows.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '14, 16:05</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-30094" class="comments-container">
<span id="30097"></span>
<div id="comment-30097" class="comment">
<div id="post-30097-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>so when you pull the replication files say from here: <a href="http://planet.osm.ch/replication/.">http://planet.osm.ch/replication/.</a> You would point to the state.txt file using osmosis?</p>
</div>
<div id="comment-30097-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 16:21)</span> <span class="comment-user userinfo">Fisherman12i</span>
</div>
</div>
</div>
<div id="comment-tools-30094" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30094-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30109"></span>

<div id="answer-container-30109" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30109-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can update your osm data using osm2pgsql by doing the following:</p>
<hr />
<p>osm2pgsql --append [my customized arguments] changes.osc.gz</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '14, 17:04</strong></p>
<img src="https://secure.gravatar.com/avatar/1df0b0daef7049f4aa8561e4c29fd7de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fisherman12i&#39;s gravatar image" />
<p><span>Fisherman12i</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fisherman12i has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30109" class="comments-container">
&#10;</div>
<div id="comment-tools-30109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30109-form-container" class="comment-form-container">
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

