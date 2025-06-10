+++
type = "question"
title = "Restarting osm2pqsql full planet import because of too low --cache setting? (import runs for 6 days already)"
description = '''I&#x27;ve started a full osm planet import 6 days ago with: osm2pgsql --number-processes 8 --slim --cache 14384 -d osm_planet_db --hstore --hstore-match-only -W -m -S default.style osm-planet-150303.osm.pbf  It is now at: Processing: Node(2786658k 90.9k/s) Way(243561k 0.52k/s) Relation(0 0.00/s)  So node...'''
date = "2015-04-08T09:16:00Z"
lastmod = "2015-04-08T10:45:00Z"
weight = 42186
keywords = [ "import", "planet_osm", "postgresql", "osm2pgsql", "postgis" ]
aliases = [ "/questions/42186" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Restarting osm2pqsql full planet import because of too low --cache setting? (import runs for 6 days already)](/questions/42186/restarting-osm2pqsql-full-planet-import-because-of-too-low-cache-setting-import-runs-for-6-days-already)

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
<span id="post-42186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42186-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've started a full osm planet import 6 days ago with:</p>
<pre><code>osm2pgsql --number-processes 8 --slim --cache 14384 -d osm_planet_db --hstore --hstore-match-only -W -m -S default.style osm-planet-150303.osm.pbf</code></pre>
<p>It is now at:</p>
<pre><code>Processing: Node(2786658k 90.9k/s) Way(243561k 0.52k/s) Relation(0 0.00/s)</code></pre>
<p>So nodes have been processed, ways almost, relations not yet.</p>
<p>Is it possible to estimate how more days it will take to finalize?</p>
<p>2nd point: I followed the instruction for optimizing PostgreSQL (set <code>autovacuum</code> <code>off</code>, incresed <code>checkpoint_segments</code>, etc.). But I only <a href="http://wiki.openstreetmap.org/wiki/Osm2pgsql#Parameters">now read</a> that my <code>--cache</code> setting of <code>14384</code> might be a too low for a full planet import:</p>
<p><em>"osm2pgsql relies much on its node cache during import. If the nodes do not fit into the cache in slim mode it needs to do database lookups which slow down the process. (Without slim mode, it fails if the nodes do not fit in the cache). Use enough cache so all nodes are cached. <strong>-C 22000 seems to do the job</strong>, even if that means you have to configure more swap space."</em></p>
<p>Does it make sense to kill the osm2pqsql process and restart with <code>--cache 28000</code>? (I have a total of 32GB RAM, 8 cores, 64bit CentOS). That is, throw away the last 6 days of importing because it will still take ages to finish, and with the increased Cache it will still be faster in the end?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '15, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/42c22f7724a32aa2d2e19609d8e7f1b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jnachtigall&#39;s gravatar image" />
<p><span>jnachtigall</span><br />
<span class="score" title="101 reputation points">101</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jnachtigall has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42186" class="comments-container">
&#10;</div>
<div id="comment-tools-42186" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42186-form-container" class="comment-form-container">
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

<span id="42189"></span>

<div id="answer-container-42189" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42189-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-42189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jnachtigall has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You're likely to get a performance of under 5 relations per second on this machine, which would mean at least a week for relation processing, and after that you still need to go through index creation. My guess is that you're looking for at least two more weeks here. You can speed up the job with more cache and the --flatnodes option but probably not by 30%.</p>
<p>The fastest way to get a planet file imported is to order a large SSD disk and install it to your server. If you order it now, receive it tomorrow, install it a day later, and then restart the import, you can be done within a week.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '15, 10:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-42189" class="comments-container">
&#10;</div>
<div id="comment-tools-42189" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42189-form-container" class="comment-form-container">
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

