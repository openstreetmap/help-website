+++
type = "question"
title = "How to build a high performance tile server?"
description = '''Hi there, Just trying to build up a new tile server and can&#x27;t figure out how to get best performance on it. Followed up the guide at switch2osm and it works but quite slow. Imported the entire world map in 45h in a 64 Cores and 128GB RAM and 2TB SSD server, I expected to be much faster so probably I...'''
date = "2021-03-08T11:28:00Z"
lastmod = "2021-03-09T11:37:00Z"
weight = 79182
keywords = [ "renderd", "tileserversetup", "osm2pgsql", "tileserver" ]
aliases = [ "/questions/79182" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to build a high performance tile server?](/questions/79182/how-to-build-a-high-performance-tile-server)

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
<span id="post-79182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79182-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>Just trying to build up a new tile server and can't figure out how to get best performance on it. Followed up the guide at switch2osm and it works but quite slow.</p>
<p>Imported the entire world map in 45h in a 64 Cores and 128GB RAM and 2TB SSD server, I expected to be much faster so probably I messed up with some importing option.</p>
<p>Wonder if someone could help me with best configuration hardware/software (osm2pgsql import, postgresql and renderd options).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-tileserversetup" rel="tag" title="see questions tagged &#39;tileserversetup&#39;">tileserversetup</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '21, 11:28</strong></p>
<img src="https://secure.gravatar.com/avatar/43c9dee0f31babb81a8c6baf85ef2720?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="antoniodelapradera&#39;s gravatar image" />
<p><span>antoniodelap...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="antoniodelapradera has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79182" class="comments-container">
&#10;</div>
<div id="comment-tools-79182" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79182-form-container" class="comment-form-container">
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

<span id="79183"></span>

<div id="answer-container-79183" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79183-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Cores won't help that much as expected for import as some of the osm2pgsql work is done single-threaded. 45h for importing planet.osm.pbf may not be the best performance but not that bad either. Is this a single ssd? What's the write/sec. for that one? Did you adjust the postgresql conf settings? Are you using a flat nodes file? Which version of osm2pgsql are you using?</p>
<p>Comparing with e.g. this benchmark: <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql/benchmarks#Desktop_Debian_9.2C_4_cores_i5-6500_CPU_.40_3.20GHz.2F32GB_RAM.2C_1TB.2B500GB_SSD_.28hstore_slim_drop_flat-nodes_and_ZFS_filesystem.29">https://wiki.openstreetmap.org/wiki/Osm2pgsql/benchmarks#Desktop_Debian_9.2C_4_cores_i5-6500_CPU_.40_3.20GHz.2F32GB_RAM.2C_1TB.2B500GB_SSD_.28hstore_slim_drop_flat-nodes_and_ZFS_filesystem.29</a> with your hardware you should perform better than 45hrs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '21, 11:36</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-79183" class="comments-container">
<span id="79184"></span>
<div id="comment-79184" class="comment">
<div id="post-79184-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The osm2pgsql version is 1.4.1 and here is the command I used for the import:</p>
<p>osm2pgsql \ --cache 32768 \ --number-processes 32 \ --hstore \ --multi-geometry \ --database gis \ --slim \ --drop \ --style openstreetmap-carto.style \ --tag-transform-script openstreetmap-carto.lua \ planet.osm.pbf</p>
<p>And for the postgresql I only changed 3 values:</p>
<p>work_mem=1GB maintenance_work_mem=4GB shared_buffers=32GB</p>
<p>I do not know if tunning any other option in the db would be better.</p>
</div>
<div id="comment-79184-info" class="comment-info">
<span class="comment-age">(08 Mar '21, 13:32)</span> <span class="comment-user userinfo">antoniodelap...</span>
</div>
</div>
<span id="79191"></span>
<div id="comment-79191" class="comment">
<div id="post-79191-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I trust you have read <a href="https://osm2pgsql.org/doc/manual.html#tuning-the-postgresql-server">https://osm2pgsql.org/doc/manual.html#tuning-the-postgresql-server</a> ?</p>
</div>
<div id="comment-79191-info" class="comment-info">
<span class="comment-age">(08 Mar '21, 21:30)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="79196"></span>
<div id="comment-79196" class="comment">
<div id="post-79196-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was checking this: <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql/benchmarks">https://wiki.openstreetmap.org/wiki/Osm2pgsql/benchmarks</a> But I will check that one for sure.</p>
<p>Do you think I should use --flat-nodes option while importing?</p>
</div>
<div id="comment-79196-info" class="comment-info">
<span class="comment-age">(09 Mar '21, 11:37)</span> <span class="comment-user userinfo">antoniodelap...</span>
</div>
</div>
</div>
<div id="comment-tools-79183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79183-form-container" class="comment-form-container">
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

