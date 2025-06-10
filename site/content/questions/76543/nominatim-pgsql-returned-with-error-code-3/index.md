+++
type = "question"
title = "Nominatim - pgsql returned with error code (3)"
description = '''Hello, When I try to install new osm file in my nominatim server. With the setup.php (10666 = 2/3 of 16G RAM) :  cd /srv/nominatim/build/ &amp;amp;&amp;amp; ./utils/setup.php --osm-file /srv/nominatim/Nominatim-3.4.1/data/france-latest.osm --all --osm2pgsql-cache 10666  I have some errors :  Done 9254119 in...'''
date = "2020-09-10T12:42:00Z"
lastmod = "2020-09-14T13:51:00Z"
weight = 76543
keywords = [ "setup.php", "pgsql", "nominatim", "osm", "osm2pgsql" ]
aliases = [ "/questions/76543" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim - pgsql returned with error code (3)](/questions/76543/nominatim-pgsql-returned-with-error-code-3)

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
<span id="post-76543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76543-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>When I try to install new osm file in my nominatim server.</p>
<p>With the setup.php (10666 = 2/3 of 16G RAM) :</p>
<pre><code>cd /srv/nominatim/build/ &amp;&amp; ./utils/setup.php --osm-file /srv/nominatim/Nominatim-3.4.1/data/france-latest.osm --all --osm2pgsql-cache 10666</code></pre>
<p>I have some errors :</p>
<pre><code>Done 9254119 in 55677 @ 166.210800 per second - Rank 30 ETA (seconds): 8.447104
  Done 9254226 in 55679 @ 166.206757 per second - Rank 30 ETA (seconds): 7.803534
  Done 9254333 in 55680 @ 166.205688 per second - Rank 30 ETA (seconds): 7.159803
  Done 9254458 in 55681 @ 166.204956 per second - Rank 30 ETA (seconds): 6.407751
  Done 9254596 in 55682 @ 166.204453 per second - Rank 30 ETA (seconds): 5.577468
  Done 9254744 in 55683 @ 166.204117 per second - Rank 30 ETA (seconds): 4.687008
  Done 9254913 in 55684 @ 166.204163 per second - Rank 30 ETA (seconds): 3.670185
  Done 9255092 in 55685 @ 166.204407 per second - Rank 30 ETA (seconds): 2.593192
  Done 9255256 in 55686 @ 166.204361 per second - Rank 30 ETA (seconds): 1.606456
  Done 9255349 in 55688 @ 166.200058 per second - Rank 30 ETA (seconds): 1.046931
  Done 9255508 in 55689 @ 166.199936 per second - Rank 30 ETA (seconds): 0.090253
  Done 9255523 in 55689 @ 166.200195 per second - ETA (seconds): 0.000000
  Done 9255523 in 55689 @ 166.200195 per second - FINISHED
&#10;2020-09-10 09:07:48 == Index postcodes
2020-09-10 09:09:32 == Create Search indices
ERROR:  out of memory
DETAIL:  Failed on request of size 10737418200.
ERROR: pgsql returned with error code (3)
string(34) &quot;pgsql returned with error code (3)&quot;</code></pre>
<p>I've change many times the --osm2pgsql-cache parameters with some values : Same errors :(</p>
<p>My configuration :</p>
<pre><code>~$ df -h
Filesystem         Size  Used Avail Use% Mounted on
/dev/ploop41196p1  296G  167G  117G  59% /
&#10;:~$ free -h
              total        used        free      shared  buff/cache   available
Mem:            16G         56M         14G        1.2G        1.5G         14G
Swap:          256M        256M</code></pre>
<p>Have you some ideas please ? Thanks</p>
<p>F.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-setup.php" rel="tag" title="see questions tagged &#39;setup.php&#39;">setup.php</span> <span class="post-tag tag-link-pgsql" rel="tag" title="see questions tagged &#39;pgsql&#39;">pgsql</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Sep '20, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/4d591ab994281c963a7fca1deaedf484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="__fabrice&#39;s gravatar image" />
<p><span>__fabrice</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="__fabrice has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Sep '20, 12:44</strong> </span></p>
</div>
</div>
<div id="comments-container-76543" class="comments-container">
&#10;</div>
<div id="comment-tools-76543" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76543-form-container" class="comment-form-container">
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

<span id="76546"></span>

<div id="answer-container-76546" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76546-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osm2pgsql imports the *.pbf file into the database. Then follows the indexing "Done 9254458 in 55681 @ 166.204956 per second". Changing "osm2pgsql-cache" has no effect on the indexing.</p>
<p>It looks like postgresql ran out of RAM when creating an index. The postgresql log file might have more information. You can repeat the step: "./utils/setup.php --index --create-search-indices --create-country-names"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Sep '20, 16:01</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-76546" class="comments-container">
<span id="76547"></span>
<div id="comment-76547" class="comment">
<div id="post-76547-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I restart the setup.php command, and I'll run : "./utils/setup.php --index --create-search-indices --create-country-names" after. And so, I'll post the result. Thanks.</p>
</div>
<div id="comment-76547-info" class="comment-info">
<span class="comment-age">(10 Sep '20, 16:09)</span> <span class="comment-user userinfo">__fabrice</span>
</div>
</div>
<span id="76579"></span>
<div id="comment-76579" class="comment">
<div id="post-76579-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi. I've run "./utils/setup.php --index --create-search-indices --create-country-names", and I've the same error "pgsql returned with error code (3)", out of memory. So, I check the configuration for postgresql, and all is ok. For example : "maintenance_work_mem = 10GB". Have you an another idea please ?</p>
</div>
<div id="comment-76579-info" class="comment-info">
<span class="comment-age">(14 Sep '20, 09:50)</span> <span class="comment-user userinfo">__fabrice</span>
</div>
</div>
<span id="76583"></span>
<div id="comment-76583" class="comment">
<div id="post-76583-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You need to monitor the RAM usage while the script is running. Assessing after the script ended if memory was low doesn't work. Most likely you need a server with more RAM.</p>
</div>
<div id="comment-76583-info" class="comment-info">
<span class="comment-age">(14 Sep '20, 12:20)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="76589"></span>
<div id="comment-76589" class="comment">
<div id="post-76589-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I've 16G of RAM, it's not good enough ?. I'm just re-run the script and check memory with "htop" command.</p>
</div>
<div id="comment-76589-info" class="comment-info">
<span class="comment-age">(14 Sep '20, 13:51)</span> <span class="comment-user userinfo">__fabrice</span>
</div>
</div>
</div>
<div id="comment-tools-76546" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76546-form-container" class="comment-form-container">
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

