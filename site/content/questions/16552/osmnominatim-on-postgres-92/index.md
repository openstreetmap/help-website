+++
type = "question"
title = "OSM/Nominatim on Postgres 9.2?"
description = '''I am trying to use Nominatim&#x27;s setup tool to populate an OSM database. On Postgres 9.0/PostGIS 1.5 this works fine. I am now attempting to perform this load on Postgres 9.2/PostGIS 2.0. I needed to modify some of the plpgsql functions for compatibility regarding hstore. Once this was done, the load ...'''
date = "2012-09-30T14:59:00Z"
lastmod = "2012-10-05T08:46:00Z"
weight = 16552
keywords = [ "nominatim", "postgres", "9.2" ]
aliases = [ "/questions/16552" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OSM/Nominatim on Postgres 9.2?](/questions/16552/osmnominatim-on-postgres-92)

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
<span id="post-16552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16552-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to use Nominatim's setup tool to populate an OSM database. On Postgres 9.0/PostGIS 1.5 this works fine. I am now attempting to perform this load on Postgres 9.2/PostGIS 2.0. I needed to modify some of the plpgsql functions for compatibility regarding hstore. Once this was done, the load starts fine but after some time Postgres runs out of memory. I tried reducing the memory usage settings in Postgres, and also tried running Nominatim with limited settings, such as disabling token precalc and limiting the number of threads to one, but Postgres will still eventually run out of memory and the load fails. Has anyone had success loading OSM into Postgres 9.2 or is this not recommended?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-9.2" rel="tag" title="see questions tagged &#39;9.2&#39;">9.2</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Sep '12, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/49e2f4e707a5627bd52b137db2384789?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bryanck&#39;s gravatar image" />
<p><span>bryanck</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bryanck has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Oct '12, 08:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span></p>
</div>
</div>
<div id="comments-container-16552" class="comments-container">
<span id="16565"></span>
<div id="comment-16565" class="comment">
<div id="post-16565-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Some clarifications would be helpful: How much RAM do you have? Do you try to load the planet or an extract? Is it indeed postgres that runs out of memory or is it osm2pgsql?</p>
</div>
<div id="comment-16565-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 09:06)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="16586"></span>
<div id="comment-16586" class="comment">
<div id="post-16586-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have 24 Gb of RAM, 12 core (24 w/ HT), Cent OS 6.3 64-bit with all updates. I'm loading a United States extract, which loads perfectly fine with Postgres 9.0. It is Postgres that runs out of memory, not Nominatim or osm2pgsql, many CachedPlans are accumulating and not being cleaned up. I have tried lowering the Postgres memory settings significantly (shared mem, effective cache, etc no more than 1 gb) but it didn't fix the problem. Also my higher memory settings work fine on Postgres 9.0. I was told Postgres 9.2 has more aggressive caching which is what could be at the root of this.</p>
</div>
<div id="comment-16586-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 17:24)</span> <span class="comment-user userinfo">bryanck</span>
</div>
</div>
</div>
<div id="comment-tools-16552" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16552-form-container" class="comment-form-container">
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

<span id="16589"></span>

<div id="answer-container-16589" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16589-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Postgres has <a href="http://www.postgresql.org/docs/current/static/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-MEMORY">many settings for memory usage</a> that you may want to look at. It also respects the settings pretty well, including shared_mem and effective_cache. These should be set to use most of your memory if the server is dedicated, as they are a shared ressource. One setting you might actually want to lower is work_mem <strong>IF</strong> you have many concurrent connections that use the maximum work_mem (each connection can individually use up to work_mem bytes of memory in addition to the shared memory).</p>
<p>But before changing values with a wild guess, you should try getting more info about where the memory is going. How many postgres processes are running ? How many use "too much" memory ? What queries are they running ? The first step to gather this info is using {a,h,}top, the pg_stats_activity table, and the postgres logs. Configure the logs to be more verbose if you didn't already.</p>
<p>If you still cannot find the culprit, you may be better served by the <a href="http://www.postgresql.org/community/lists/">postgres mailing lists</a>, than help.osm.org.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '12, 19:38</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Oct '12, 19:41</strong> </span></p>
</div>
</div>
<div id="comments-container-16589" class="comments-container">
&#10;</div>
<div id="comment-tools-16589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16589-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16672"></span>

<div id="answer-container-16672" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16672-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I discovered there were too many CachedPlans being created by Postgres. These accumulate and eventually Postgres runs out of memory and shuts the connections down and the import fails. I posted on the Postgresql forums but the only response was that Postgres 9.2 uses more aggressive caching to help improve performance, so I am guessing it is related to that. For now I have reverted to Postgres 9.0.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '12, 18:17</strong></p>
<img src="https://secure.gravatar.com/avatar/49e2f4e707a5627bd52b137db2384789?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bryanck&#39;s gravatar image" />
<p><span>bryanck</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bryanck has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16672" class="comments-container">
<span id="16687"></span>
<div id="comment-16687" class="comment">
<div id="post-16687-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I had one more report of somebody running into memory problems with postgres (although version 9.1) during the load stage. We never could quite figure out why it failed on this specific installation. Eventually, <a href="https://github.com/twain47/Nominatim/pull/26">the patch contained in this pull request</a> managed to work around the problem somehow. It is within the realms of possibility that your postgres 9.2 installation suffers from the same problem.</p>
</div>
<div id="comment-16687-info" class="comment-info">
<span class="comment-age">(05 Oct '12, 08:46)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-16672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16672-form-container" class="comment-form-container">
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

