+++
type = "question"
title = "osm2pgsql error with connection to database"
description = '''I&#x27;ve been following the instructions at Manually building a tile server (18.04 LTS) but am stuck on the following step: The following command will insert the OpenStreetMap data you downloaded earlier into the database. This step is very disk I/O intensive; importing the full planet might take many h...'''
date = "2019-04-27T10:30:00Z"
lastmod = "2019-05-16T12:10:00Z"
weight = 68980
keywords = [ "switch2osm", "osm2pgsql", "ubuntu", "tileserver" ]
aliases = [ "/questions/68980" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql error with connection to database](/questions/68980/osm2pgsql-error-with-connection-to-database)

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
<span id="post-68980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68980-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been following the instructions at <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">Manually building a tile server (18.04 LTS)</a> but am stuck on the following step:</p>
<p><em>The following command will insert the OpenStreetMap data you downloaded earlier into the database. This step is very disk I/O intensive; importing the full planet might take many hours, days or weeks depending on the hardware. For smaller extracts the import time is much faster accordingly, and you may need to experiment with different -C values to fit within your machine’s available memory.</em></p>
<pre><code>osm2pgsql -d gis --create --slim  -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 2500 --number-processes 1 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/azerbaijan-latest.osm.pbf</code></pre>
<p>However when I run it, I keep getting the following error:</p>
<pre><code>osm2pgsql version 0.96.0 (64 bit id space)
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=2500MB, maxblocks=40000*65536, allocation method=11
Mid: pgsql, cache=2500
DB writer thread failed due to ERROR: Connection to database failed: FATAL:  role &quot;localuser&quot; does not exist</code></pre>
<p>I've gone through to ensure I've followed all the steps. I've also tried adding -U renderaccount -W options to set it run as the renderaccount, not the localuser account, but still no improvement.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '19, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/9417cdf5fb49e5c18f617fdab020f203?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="breno-au&#39;s gravatar image" />
<p><span>breno-au</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="breno-au has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68980" class="comments-container">
<span id="69197"></span>
<div id="comment-69197" class="comment">
<div id="post-69197-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you.</p>
</div>
<div id="comment-69197-info" class="comment-info">
<span class="comment-age">(15 May '19, 12:39)</span> <span class="comment-user userinfo">breno-au</span>
</div>
</div>
</div>
<div id="comment-tools-68980" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68980-form-container" class="comment-form-container">
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

<span id="68981"></span>

<div id="answer-container-68981" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68981-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-68981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looks like you are running it from a unix account localuser. You need to replace "renderaccount" with the account your mod_tile/renderd will run under (not necessarily your regular logon). See this bit on switch2osm:</p>
<p>Now you need to create a postgis database. The defaults of various programs assume the database is called gis and we will use the same convention in this tutorial, although this is not necessary. Substitute your username for renderaccount where is is used below. This should be the username that will render maps with Mapnik. sudo -u postgres -i createuser renderaccount # answer yes for superuser (although this isn't strictly necessary) createdb -E UTF8 -O renderaccount gis</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '19, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-68981" class="comments-container">
<span id="69210"></span>
<div id="comment-69210" class="comment">
<div id="post-69210-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>While mostly a description of how to solve a different problem, <a href="https://www.openstreetmap.org/user/SomeoneElse/diary/47027">https://www.openstreetmap.org/user/SomeoneElse/diary/47027</a> does describe what you need to have different map layers (or just one map layer) rendering from different databases not called "gis".</p>
</div>
<div id="comment-69210-info" class="comment-info">
<span class="comment-age">(16 May '19, 12:10)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68981" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68981-form-container" class="comment-form-container">
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

