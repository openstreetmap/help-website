+++
type = "question"
title = "Nominatim - ways from planet.pbf are being imported very slowly"
description = '''I have installed Nominatim to a server dedicated just for OSM data, with the following configurations: CentOS 7 operating system, 2x Intel XEON CPU L5420 @ 2.50GHz (Total 8 CPU cores), 16 GB of ram, and 2x2TB SATA hard drive. I&#x27;ve configured the postgresql based on the recomendations on the Nominati...'''
date = "2016-02-25T15:53:00Z"
lastmod = "2018-10-01T23:42:00Z"
weight = 48359
keywords = [ "planet", "nominatim", "osm2pgsql" ]
aliases = [ "/questions/48359" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim - ways from planet.pbf are being imported very slowly](/questions/48359/nominatim-ways-from-planetpbf-are-being-imported-very-slowly)

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
<span id="post-48359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48359-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have installed Nominatim to a server dedicated just for OSM data, with the following configurations: CentOS 7 operating system, 2x Intel XEON CPU L5420 @ 2.50GHz (Total 8 CPU cores), 16 GB of ram, and 2x2TB SATA hard drive.</p>
<p>I've configured the postgresql based on the recomendations on the Nominatim install wiki (<a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation#PostgreSQL_Tuning),">http://wiki.openstreetmap.org/wiki/Nominatim/Installation#PostgreSQL_Tuning),</a> taking into account, that my machine has only got 16 GB instead of the 32 GB recommended for those configs. I've used the following things:<br />
</p>
<p><code>shared_buffers = 1GB # recommended for a 32GB machine was 2 GB maintenance_work_mem = 4GB # recommended for a 32GB macinhe was 8 GB work_mem = 20MB # recommended for a 32GB machine was 50 MB effective_cache_size = 10GB # recommended for a 32GB machine was 24 GB synchronous_commit = off checkpoint_segments = 100 checkpoint_timeout = 10min checkpoint_completion_target = 0.9 fsync = off full_page_writes = off</code></p>
<p>First, I've tried importing a small country extract(Luxembourg), setting a cache size of 6000, using the setup.php file from utils, it was imported succesfully under 1 hour.</p>
<p>Secondly, I've deleted the data of Luxembourg, and imported for another test purpose the country extract of Great Brittain, using a cache size of 8000, it imported succesfully as well, in around 2-3 hours.</p>
<p>Today, I've decided, to try to import the whole planet.pbf file, so I've deleted the postgresql database, downloaded a pbf of the planet from one of the official mirror sites, and ran the setup with a cache size of 10000. Beforehand, I've read up some benchmarks to get a vague idea of how much time and space will this operation take.</p>
<p>When the import started, I was very surprised. The importing of the nodes went with a whopping high speed of 1095.6k/s, in the benchmark which I've analyized (a 32GB ram machine), it was only 311.7k/s.</p>
<p>But when the import of the nodes finished, and the import of the ways started, the speed significantly dropped. It was importing the ways with the speed of 0.16k/s (altough it was slowly rising, it started from 0.05k/s, and in 4 hours it rised to the above mentioned value).</p>
<p>I've stopped the import, and tried to tweak the settings. I've allocated a higher cache size first (12000), but with no success, the nodes imported with a very high speed, but the ways remained at 0.10-0.13k/s. I then tried allocating a new swap file(the original was 8GB, I've allocated another 32GB as a swap file), but that didn't change anything neither. Lastly, I've edited the setup.php, changed the --number-processes from 1, to 6, and included the --slim keyword when osm2psql is started from there, but nothing changed.</p>
<p>Right now I am out of ideas. Is this speed decrease normal? Should I upgrade my machine to the recommended memory? I tought that a 16GB ram would be enough for planet pbf, I was aware that it could take more time with this machine, then with a 32 GB, but this seems very much. If the whole planet import would take not more then 12-15 days, I would be ok with that, but as things look now, with these settings the import would take around 2 months, and this is just too much, considering, an error could occur anywhere, and I have to start the whole import process again.</p>
<p>Any ideas what could cause this problem, or what other tweaks could I try, to fasten the import process?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '16, 15:53</strong></p>
<img src="https://secure.gravatar.com/avatar/8d611d043d7267073e41089a5283fbe1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adam%20Baranyai&#39;s gravatar image" />
<p><span>Adam Baranyai</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adam Baranyai has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Feb '16, 15:58</strong> </span></p>
</div>
</div>
<div id="comments-container-48359" class="comments-container">
&#10;</div>
<div id="comment-tools-48359" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48359-form-container" class="comment-form-container">
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

<span id="66119"></span>

<div id="answer-container-66119" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66119-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are some parts in the import-process that can not be done in parallel. But have you seen the options: <em>threads</em> and <em>osm2pgsql-cache</em> to speed up the import.</p>
<pre><code>Nominatim-3.2.0/build$./utils/setup.php
  --threads           Number of threads (where possible)   
  --osm2pgsql-cache   Cache size used by osm2pgsql</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '18, 23:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a899069511378c2de10d9ccc93c5adc6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alfonx&#39;s gravatar image" />
<p><span>alfonx</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alfonx has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66119" class="comments-container">
&#10;</div>
<div id="comment-tools-66119" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66119-form-container" class="comment-form-container">
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

