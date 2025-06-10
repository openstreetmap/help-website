+++
type = "question"
title = "index returns relation &quot;search_name_0&quot; does not exist in &quot;Starting rank 2&quot;"
description = '''Hello! I have generated nominatim database before and never faced such an issue. Please tell me which &quot;setup.php&quot; command generates the &quot;search_name_0&quot; and such tables? Full error output is: -bash-4.2$ ./utils/setup.php --index --threads 8 --osm2pgsql-cache 24000 nominatim version 2.5.1  Starting in...'''
date = "2017-09-12T10:20:00Z"
lastmod = "2017-09-13T22:43:00Z"
weight = 59567
keywords = [ "setup.php", "index", "setup", "indexing", "database" ]
aliases = [ "/questions/59567" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [index returns relation "search_name_0" does not exist in "Starting rank 2"](/questions/59567/index-returns-relation-search_name_0-does-not-exist-in-starting-rank-2)

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
<span id="post-59567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59567-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello!</p>
<p>I have generated nominatim database before and never faced such an issue.</p>
<p>Please tell me which "setup.php" command generates the "search_name_0" and such tables?</p>
<p>Full error output is:</p>
<pre><code>-bash-4.2$ ./utils/setup.php --index --threads 8 --osm2pgsql-cache 24000
nominatim version 2.5.1
&#10;Starting indexing rank (0 to 4) using 8 threads
Starting rank 0
  Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 1
  Done 0 in 0 @ 0.000000 per second - FINISHED
&#10;Starting rank 2
index_placex: UPDATE failed: ERROR:  relation &quot;search_name_0&quot; does not exist
LINE 1: DELETE from search_name_0 WHERE place_id = in_place_id
                    ^
QUERY:  DELETE from search_name_0 WHERE place_id = in_place_id
CONTEXT:  PL/pgSQL function deletesearchname(integer,bigint) line 1260 at SQL statement
PL/pgSQL function placex_update() line 75 at assignment
index_placex: UPDATE failed: ERROR:  relation &quot;search_name_0&quot; does not exist
LINE 1: DELETE from search_name_0 WHERE place_id = in_place_id
                    ^
QUERY:  DELETE from search_name_0 WHERE place_id = in_place_id
CONTEXT:  PL/pgSQL function deletesearchname(integer,bigint) line 1260 at SQL statement
PL/pgSQL function placex_update() line 75 at assignment
index_placex: UPDATE failed: ERROR:  relation &quot;search_name_0&quot; does not exist
LINE 1: DELETE from search_name_0 WHERE place_id = in_place_id
                    ^
QUERY:  DELETE from search_name_0 WHERE place_id = in_place_id
CONTEXT:  PL/pgSQL function deletesearchname(integer,bigint) line 1260 at SQL statement
PL/pgSQL function placex_update() line 75 at assignment
index_placex: UPDATE failed: ERROR:  relation &quot;search_name_0&quot; does not exist
LINE 1: DELETE from search_name_0 WHERE place_id = in_place_id
                    ^
QUERY:  DELETE from search_name_0 WHERE place_id = in_place_id
CONTEXT:  PL/pgSQL function deletesearchname(integer,bigint) line 1260 at SQL statement
PL/pgSQL function placex_update() line 75 at assignment
ERROR: Error executing external command: /srv/Nominatim-2.5.1/nominatim/nominatim -i -d nominatim -P 5432 -t 8 -R 4
Error executing external command: /srv/Nominatim-2.5.1/nominatim/nominatim -i -d nominatim -P 5432 -t 8 -R 4
&#10;-bash-4.2$</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-setup.php" rel="tag" title="see questions tagged &#39;setup.php&#39;">setup.php</span> <span class="post-tag tag-link-index" rel="tag" title="see questions tagged &#39;index&#39;">index</span> <span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-indexing" rel="tag" title="see questions tagged &#39;indexing&#39;">indexing</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Sep '17, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/8d9e757af553c12945874ab8e007d724?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunsetjunks&#39;s gravatar image" />
<p><span>sunsetjunks</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunsetjunks has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59567" class="comments-container">
&#10;</div>
<div id="comment-tools-59567" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59567-form-container" class="comment-form-container">
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

<span id="59620"></span>

<div id="answer-container-59620" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59620-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It took some time to figure out but it happens when your "create-partition-tables" part of setup fails.</p>
<p>Restarting it will fail to re-create the tables. I had to manually remove all partition tables and then restarted the setup with "create-partition-tables" key to solve this!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '17, 22:43</strong></p>
<img src="https://secure.gravatar.com/avatar/8d9e757af553c12945874ab8e007d724?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunsetjunks&#39;s gravatar image" />
<p><span>sunsetjunks</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunsetjunks has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59620" class="comments-container">
&#10;</div>
<div id="comment-tools-59620" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59620-form-container" class="comment-form-container">
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

