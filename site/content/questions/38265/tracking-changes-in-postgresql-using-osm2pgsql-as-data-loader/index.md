+++
type = "question"
title = "Tracking Changes in Postgresql using osm2pgsql as data loader"
description = '''Hello, I am maintaining my postgresql database using osm2pgsql to maintain my database. I want to track the changes made by the daily replication files. I was thinking of creating triggers that fired after delete, update and insert. But I have concerns that is might slow down the daily update proces...'''
date = "2014-11-02T20:53:00Z"
lastmod = "2014-11-06T01:03:00Z"
weight = 38265
keywords = [ "openstreetmap", "postgresql", "osm2pgsql", "sql" ]
aliases = [ "/questions/38265" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tracking Changes in Postgresql using osm2pgsql as data loader](/questions/38265/tracking-changes-in-postgresql-using-osm2pgsql-as-data-loader)

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
<span id="post-38265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38265-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am maintaining my postgresql database using osm2pgsql to maintain my database. I want to track the changes made by the daily replication files.</p>
<p>I was thinking of creating triggers that fired after delete, update and insert. But I have concerns that is might slow down the daily update process. Has anyone done this?</p>
<p>Can you export the change files to polygons in another table? or to a shapefile?</p>
<p>Thank you</p>
<p>Andrew</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Nov '14, 20:53</strong></p>
<img src="https://secure.gravatar.com/avatar/728321acc3469682288102302efc6341?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajc2014&#39;s gravatar image" />
<p><span>ajc2014</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajc2014 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38265" class="comments-container">
&#10;</div>
<div id="comment-tools-38265" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38265-form-container" class="comment-form-container">
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

<span id="38287"></span>

<div id="answer-container-38287" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38287-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I did something along such lines for a map I produced during the licence change (slightly over two years ago).</p>
<p>It is slightly tricky in particular, except if something has changed, osm2pgsql will not update any objects, it deletes and then inserts a new copy. This is relevant if you have added additional columns to the schema and want to retain the information (essentially you have to copy the extra information on delete and then re-add on insert). I would not have any concerns performance wise if you are running this on a reasonably fast machine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '14, 17:08</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-38287" class="comments-container">
<span id="38344"></span>
<div id="comment-38344" class="comment">
<div id="post-38344-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you post how you made it work?</p>
</div>
<div id="comment-38344-info" class="comment-info">
<span class="comment-age">(06 Nov '14, 01:03)</span> <span class="comment-user userinfo">ajc2014</span>
</div>
</div>
</div>
<div id="comment-tools-38287" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38287-form-container" class="comment-form-container">
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

