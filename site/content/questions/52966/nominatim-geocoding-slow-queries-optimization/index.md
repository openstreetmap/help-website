+++
type = "question"
title = "Nominatim geocoding slow queries optimization"
description = '''Hi , We are using Nominatim with following configs for geocoding (getting lat and lon) Nominatim Version 2.4.0 16 core CPUS, 122GB RAM 320GB SSD HD And our postgresql.conf looks like following shared_buffers = 1GB # min 128kB maintenance_work_mem = 10GB # min 1MB work_mem = 50MB # min 64kB maintenan...'''
date = "2016-11-15T07:46:00Z"
lastmod = "2016-11-15T10:57:00Z"
weight = 52966
keywords = [ "slow", "nominatim", "postgresql", "query" ]
aliases = [ "/questions/52966" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim geocoding slow queries optimization](/questions/52966/nominatim-geocoding-slow-queries-optimization)

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
<span id="post-52966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52966-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi ,</p>
<p>We are using Nominatim with following configs for geocoding (getting lat and lon) Nominatim Version 2.4.0 16 core CPUS, 122GB RAM 320GB SSD HD</p>
<p>And our postgresql.conf looks like following</p>
<p>shared_buffers = 1GB # min 128kB maintenance_work_mem = 10GB # min 1MB work_mem = 50MB # min 64kB maintenance_work_mem = 10GB # min 1MB effective_cache_size = 24GB synchronous_commit = off # synchronization level; checkpoint_segments = 100 # in logfile segments, min 1, 16MB each checkpoint_timeout = 10min # range 30s-1h checkpoint_completion_target = 0.9 # checkpoint target duration, 0.0 - 1.0</p>
<p>We are seeing following queries taking time (almost always&gt; 5 seconds) in postgres logs for geocode <a href="http://nominatim.local.com/nominatim/search.php?format=json&amp;limit=1&amp;q=322+West+Street%2CCarlisle%2CMassachusetts%2C01741%2CUnited+States">http://nominatim.local.com/nominatim/search.php?format=json&amp;limit=1&amp;q=322+West+Street%2CCarlisle%2CMassachusetts%2C01741%2CUnited+States</a></p>
<p>LOG: duration: 19915.484 ms statement: select place_id, (select count(*) from (select unnest(ARRAY[4523464,5730972,36867388]) INTERSECT select unnest(nameaddress_vector))s) as exactmatch from search_name where name_vector @&gt; ARRAY[2832006] and array_cat(nameaddress_vector,ARRAY[]::integer[]) @&gt; ARRAY[15678054,348921,362979,36867389] and country_code = 'us' order by (case when importance = 0 OR importance IS NULL then 0.75-(search_rank::float/40) else importance end) DESC, exactmatch DESC limit 2</p>
<p><a href="http://nominatim.local.com/nominatim/search.php?format=json&amp;limit=1&amp;q=106+Winchester+Street+%232%2CBrookline%2CMassachusetts%2C02446%2CUnited+States">http://nominatim.local.com/nominatim/search.php?format=json&amp;limit=1&amp;q=106+Winchester+Street+%232%2CBrookline%2CMassachusetts%2C02446%2CUnited+States</a></p>
<p>LOG: duration: 13518.676 ms statement: select place_id, (select count(*) from (select unnest(ARRAY[6122619,5730972,18878827]) INTERSECT select unnest(nameaddress_vector))s) as exactmatch from search_name where name_vector @&gt; ARRAY[2294177] and array_cat(nameaddress_vector,ARRAY[]::integer[]) @&gt; ARRAY[1997025,53652,362979,18878828] and country_code = 'us' order by (case when importance = 0 OR importance IS NULL then 0.75-(search_rank::float/40) else importance end) DESC, exactmatch DESC limit 2</p>
<p>Can someone suggest what are we missing here? Anyways to improve like creating indexes or changing postgres configs?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '16, 07:46</strong></p>
<img src="https://secure.gravatar.com/avatar/d2cd39e451cff2d68baea8d2070a9e8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aaphadke&#39;s gravatar image" />
<p><span>aaphadke</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aaphadke has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52966" class="comments-container">
&#10;</div>
<div id="comment-tools-52966" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52966-form-container" class="comment-form-container">
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

<span id="52967"></span>

<div id="answer-container-52967" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52967-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a duplicate of <a href="https://github.com/twain47/Nominatim/issues/578">https://github.com/twain47/Nominatim/issues/578</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '16, 10:57</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-52967" class="comments-container">
&#10;</div>
<div id="comment-tools-52967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52967-form-container" class="comment-form-container">
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

