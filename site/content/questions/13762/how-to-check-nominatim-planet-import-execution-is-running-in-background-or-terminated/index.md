+++
type = "question"
title = "How to check Nominatim planet import execution is running in background or terminated?"
description = '''I am doing Nominatim OSM installation as per the steps given in https://wiki.openstreetmap.org/wiki/Nominatim/Installation. Currently I am on following command   ./utils/setup.php --osm-file /usr/share/osmgeplanet/gujarat.osm.bz2 --all  Script is running and the last line of output is &quot;Partitions&quot; an...'''
date = "2012-06-25T13:35:00Z"
lastmod = "2012-06-26T07:56:00Z"
weight = 13762
keywords = [ "import", "nominatim", "osm", "postgresql" ]
aliases = [ "/questions/13762" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to check Nominatim planet import execution is running in background or terminated?](/questions/13762/how-to-check-nominatim-planet-import-execution-is-running-in-background-or-terminated)

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
<span id="post-13762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13762-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am doing Nominatim OSM installation as per the steps given in <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">https://wiki.openstreetmap.org/wiki/Nominatim/Installation</a>. Currently I am on following command</p>
<blockquote>
<p>./utils/setup.php --osm-file /usr/share/osmgeplanet/gujarat.osm.bz2 --all</p>
</blockquote>
<p>Script is running and the last line of output is "Partitions" and I can see around 589 tables in DB. But after one-two days no progress is there. Is script is terminated in background? How can I find the error? How can I check that script is running in background or not?</p>
<p>As I can see in the setup.php after writing "partitions" keyword as output, script is going to execute a large script (around 1.5MB sql queries) in postgresql shell. So how can I check if its still running or not? If terminated what is the error?</p>
<p>Please guide.</p>
<p><strong>EDIT</strong></p>
<p>Output of select * from pg_stat_activity where datname = 'nominatim'; is:</p>
<pre><code>datid  |  datname  | procpid | usesysid | usename | current_query | waiting | xact_start |          query_start          |         backend_start         | client_addr | client _port</code></pre>
<p>---------+-----------+---------+----------+---------+---------------+---------+------------+-------------------------------+-------------------------------+-------------+------------- 2393113 | nominatim | 4537 | 16385 | root | &lt;idle&gt; | f | | 2012-06-25 13:27:22.345186+02 | 2012-06-25 12:55:53.153181+02 | | -1 2393113 | nominatim | 5399 | 16385 | root | &lt;idle&gt; | f | | 2012-06-25 13:32:27.59859+02 | 2012-06-25 13:27:22.387147+02 | | -1 (2 rows)</p>
<p>So is my process is currently runniing?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jun '12, 13:35</strong></p>
<img src="https://secure.gravatar.com/avatar/b3013a84207a32bed7ddfad7004100f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ravi%20Kotwani&#39;s gravatar image" />
<p><span>Ravi Kotwani</span><br />
<span class="score" title="136 reputation points">136</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ravi Kotwani has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '12, 06:49</strong> </span></p>
</div>
</div>
<div id="comments-container-13762" class="comments-container">
&#10;</div>
<div id="comment-tools-13762" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13762-form-container" class="comment-form-container">
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

<span id="13769"></span>

<div id="answer-container-13769" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13769-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-13769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Normally, Nominatim shouldn't be silent for more than a few hours unless you try to import the entire planet on a slow machine. Even then, it should not hang in this particular line.</p>
<p>You can check what postgresql is doing with psql:</p>
<pre><code> psql -d postgres -c &quot;select * from pg_stat_activity where datname = &#39;nominatim&#39;&quot;</code></pre>
<p>You can ignore the lines where the query is <code>&lt;IDLE&gt;</code>. But if you see another query there stuck in waiting state, something might be blocking Nominatim. If you can't find a reason, stop the import, restart postgresql and restart the import. If you still get stuck in the same place, file a bug report in <a href="https://trac.openstreetmap.org/newticket">trac</a> or <a href="https://github.com/twain47/Nominatim/issues">github</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '12, 17:21</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '12, 07:46</strong> </span></p>
</div>
</div>
<div id="comments-container-13769" class="comments-container">
<span id="13779"></span>
<div id="comment-13779" class="comment">
<div id="post-13779-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can see 2 rows as the result of above query. Value of "current_query" field name is "&lt;idle&gt;". Value of "waiting" field is "f". For more details of result of above query, you can see my this edited question. What this columns mean? Is my process is currently running in backend or not?</p>
</div>
<div id="comment-13779-info" class="comment-info">
<span class="comment-age">(26 Jun '12, 06:51)</span> <span class="comment-user userinfo">Ravi Kotwani</span>
</div>
</div>
<span id="13781"></span>
<div id="comment-13781" class="comment">
<div id="post-13781-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can ignore the lines with &lt;idle&gt;, those are just open connections to the database. If there are no other lines, then it is not a database access that is stuck. I edited my answer to make that more clear. Finding another cause is more difficult. Just try to restart the import. It shouldn't take more than a few hours overall. If you get stuck again, ask over at the <a href="https://wiki.openstreetmap.org/wiki/Contact#IRC">IRC channel</a>.</p>
</div>
<div id="comment-13781-info" class="comment-info">
<span class="comment-age">(26 Jun '12, 07:56)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-13769" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13769-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13771"></span>

<div id="answer-container-13771" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13771-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You really should be running the install while running a <a href="https://www.gnu.org/software/screen/">screen</a> session. That way if you disconnect (intentionally or not) your commands will continue to execute.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '12, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/e17c2bfaed82349f7a355866ff24e4cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Norm1&#39;s gravatar image" />
<p><span>Norm1</span><br />
<span class="score" title="126 reputation points">126</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Norm1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 May '16, 01:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span></p>
</div>
</div>
<div id="comments-container-13771" class="comments-container">
&#10;</div>
<div id="comment-tools-13771" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13771-form-container" class="comment-form-container">
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

