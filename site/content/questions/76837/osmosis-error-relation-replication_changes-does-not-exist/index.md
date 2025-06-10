+++
type = "question"
title = "Osmosis ERROR: relation &quot;replication_changes&quot; does not exist"
description = '''I upgraded Osmosis to 0.48 did a full planet import to Postgres and started the syncing process. I used the same command I used with Osmosis 0.47; however, I am getting an error.  org.postgresql.util.PSQLException: ERROR: relation &quot;replication_changes&quot; does not exist  This is the command I executed:...'''
date = "2020-09-26T14:44:00Z"
lastmod = "2021-10-23T19:18:00Z"
weight = 76837
keywords = [ "postgresql", "postgis", "osmosis" ]
aliases = [ "/questions/76837" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis ERROR: relation "replication_changes" does not exist](/questions/76837/osmosis-error-relation-replication_changes-does-not-exist)

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
<span id="post-76837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76837-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I upgraded Osmosis to 0.48 did a full planet import to Postgres and started the syncing process. I used the same command I used with Osmosis 0.47; however, I am getting an error.</p>
<pre><code>org.postgresql.util.PSQLException: ERROR: relation &quot;replication_changes&quot; does not exist</code></pre>
<p>This is the command I executed:</p>
<pre><code>/usr/share/osmosis-0.48.2/bin/osmosis --read-replication-interval workingDirectory=. --simc --write-pgsql-change host=&quot;127.0.0.1&quot; database=&quot;osm&quot; user=&quot;my_user&quot; password=&#39;my_pass&#39;</code></pre>
<p>I never got this error before (I've been doing the syncing for the past 2-3 years.) Couldn't find any information regarding a table called replication_changes when googled. This is the table fields reported by the error:</p>
<pre><code>replication_changes (nodes_added, nodes_modified, nodes_deleted, ways_added, ways_modified, ways_deleted, relations_added, relations_modified
, relations_deleted, changesets_applied, earliest_timestamp, latest_timestamp)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Sep '20, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/3fa98831cef96f8b9fb7530160338da7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="picmate&#39;s gravatar image" />
<p><span>picmate</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="picmate has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-76837" class="comments-container">
&#10;</div>
<div id="comment-tools-76837" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76837-form-container" class="comment-form-container">
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

<span id="82321"></span>

<div id="answer-container-82321" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82321-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to apply .../osmosis/script/pgsnapshot_schema_0.6_changes.sql by psql command. This will create a TABLE replication_changes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '21, 19:18</strong></p>
<img src="https://secure.gravatar.com/avatar/e14371f8e23cbf844f27d8eef7c9ab99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nichtgedacht&#39;s gravatar image" />
<p><span>nichtgedacht</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nichtgedacht has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82321" class="comments-container">
&#10;</div>
<div id="comment-tools-82321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82321-form-container" class="comment-form-container">
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

