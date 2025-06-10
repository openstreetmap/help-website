+++
type = "question"
title = "osm2pgsql import - disk space running out during index creation"
description = '''When I am trying to import a Europe pbf file with osm2pgsql, my diskspace keeps running full during the index creation.  After the import of nodes, ways and relations the tablespace of the database has a size of 233 GB and there is still 244GB disk space available. But during index creation, these 2...'''
date = "2016-10-25T09:58:00Z"
lastmod = "2016-11-03T09:23:00Z"
weight = 52672
keywords = [ "import", "index", "osm2pgsql", "disk_usage" ]
aliases = [ "/questions/52672" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql import - disk space running out during index creation](/questions/52672/osm2pgsql-import-disk-space-running-out-during-index-creation)

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
<span id="post-52672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52672-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I am trying to import a Europe pbf file with osm2pgsql, my diskspace keeps running full during the index creation.</p>
<p>After the import of nodes, ways and relations the tablespace of the database has a size of 233 GB and there is still 244GB disk space available. But during index creation, these 244GB are completely used up. When I imported a europe data set one year ago, the disk space was enough for the database + the prerendered tiles.</p>
<p>Any suggestions as to why the index creation might use up so much disk space this time? Is this normal?</p>
<p>I'm using the following <strong>import command</strong>:</p>
<pre><code>nohup osm2pgsql ~/osm/europe-latest.osm.pbf --create --slim --database gis --number-processes=4 --cache=22000 --multi-geometry --flat-nodes ~/osm/flat-nodes.bin</code></pre>
<p>And the following <strong>postgres config</strong>:</p>
<pre><code>shared_buffers 8 MB
work_mem 1 MB
maintenance_work_mem 4096 MB
fsync off
autovacuum off
checkpoint_segments 60</code></pre>
<p>My Stack: Mod_tile, renderd, mapnik, osm2pgsql and a postgresql/postgis database.</p>
<p>Maybe it's worth mentioning that the system has 4CPU and 16GB RAM, with another 16GB of SWAP space.</p>
<p>This is the <strong>error message</strong> in the log file:</p>
<pre><code>Creating geometry index on  planet_osm_polygon
pthread_join() returned exception: Throw location unknown (consider using BOOST_THROW_EXCEPTION)
Dynamic exception type: boost::exception_detail::clone_impl&lt;boost::exception_detail::current_exception_std_exception_wrapper&lt;std::runtime_error&gt; &gt;
std::exception::what: CREATE INDEX planet_osm_polygon_index ON planet_osm_polygon USING GIST (way)   failed: ERROR:  could not extend file &quot;base/16385/8687919.15&quot;: No space left on device
HINT:  Check free disk space.
St13runtime_error
Error occurred, cleaning up</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-index" rel="tag" title="see questions tagged &#39;index&#39;">index</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-disk_usage" rel="tag" title="see questions tagged &#39;disk_usage&#39;">disk_usage</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '16, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/0c518db7e694b9e6d2b7f092621a3d4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cosmo42&#39;s gravatar image" />
<p><span>cosmo42</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cosmo42 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52672" class="comments-container">
&#10;</div>
<div id="comment-tools-52672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52672-form-container" class="comment-form-container">
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

<span id="52673"></span>

<div id="answer-container-52673" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52673-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The total disk space used by all indexes on an Europe import should be about 150 GB but I can't say how much space might be temporarily used in addition to that. If you don't need the capability to update your data with incremental updates, add the <code>--drop</code> flag to avoid building unnecessary indexes.</p>
<p>You could also create your PostGIS tablespace on a compressed ZFS volume which will not only give you about twice the storage space but in all likelihood even speed up database operations. See <a href="http://www.paulnorman.ca/blog/2014/11/zfs-settings-for-osm2pgsql/">http://www.paulnorman.ca/blog/2014/11/zfs-settings-for-osm2pgsql/</a> for examples.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '16, 11:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-52673" class="comments-container">
<span id="52707"></span>
<div id="comment-52707" class="comment">
<div id="post-52707-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the hint. Unfortunately I need to run updates later. Could it have an effect that autvacuum ist turned off?</p>
</div>
<div id="comment-52707-info" class="comment-info">
<span class="comment-age">(27 Oct '16, 08:11)</span> <span class="comment-user userinfo">cosmo42</span>
</div>
</div>
<span id="52710"></span>
<div id="comment-52710" class="comment">
<div id="post-52710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, autovacuum turned off should only be a problem for updates to an existing database, not for the initial import.</p>
</div>
<div id="comment-52710-info" class="comment-info">
<span class="comment-age">(27 Oct '16, 08:28)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52673-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52808"></span>

<div id="answer-container-52808" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52808-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Turning on autovacuum did the trick for me. During index creation 204 GB were used (instead of completely using up the 244 GB of left disk space). The indexes now take up about 131 GB.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '16, 09:14</strong></p>
<img src="https://secure.gravatar.com/avatar/0c518db7e694b9e6d2b7f092621a3d4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cosmo42&#39;s gravatar image" />
<p><span>cosmo42</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cosmo42 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52808" class="comments-container">
<span id="52809"></span>
<div id="comment-52809" class="comment">
<div id="post-52809-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Since most guides for tuning of OSM postgres configs state that autovacuum should be turned off, I think it is worth mentioning that autovacuum could be necessary if disk space is scarce. Also I found no drawbacks in speed with autovacuum turned on - actually the overall import time was a bit faster.</p>
</div>
<div id="comment-52809-info" class="comment-info">
<span class="comment-age">(03 Nov '16, 09:23)</span> <span class="comment-user userinfo">cosmo42</span>
</div>
</div>
</div>
<div id="comment-tools-52808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52808-form-container" class="comment-form-container">
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

