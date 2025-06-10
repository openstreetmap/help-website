+++
type = "question"
title = "Issue importing planet.osm file with osm2pgsql"
description = '''I&#x27;m currently trying to import an osm planet file into my GIS render DB using osm2pgsql and the import keeps failing at the same point. I ran pgtune prior to running the ingest. I have autovac set to off I&#x27;m running a linux server with 16 cores and 64 GB ram. postgresql 9.2 osm2pgsql 0.86 I have run...'''
date = "2016-05-04T15:26:00Z"
lastmod = "2016-05-04T15:26:00Z"
weight = 49575
keywords = [ "planet", "import", "osm", "osm2pgsql" ]
aliases = [ "/questions/49575" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Issue importing planet.osm file with osm2pgsql](/questions/49575/issue-importing-planetosm-file-with-osm2pgsql)

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
<span id="post-49575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49575-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently trying to import an osm planet file into my GIS render DB using osm2pgsql and the import keeps failing at the same point.</p>
<p>I ran pgtune prior to running the ingest. I have autovac set to off</p>
<p>I'm running a linux server with 16 cores and 64 GB ram.<br />
postgresql 9.2 osm2pgsql 0.86</p>
<p>I have run the following with 16GB, 24GB and 40GB Cache using 4 processors.</p>
<p>nohup time osm2pgsql --create --proj 3857 --style /usr/local/share/osm2pgsql/default.style -j --slim -C 40000 --number-processes 4 --database gis /home/centos/APIdbplanet.osm</p>
<p>Each time I get the following error:</p>
<p>node cache: stored: 3180786074(100.00%), storage efficiency: 83.61% (dense blocks: 434757, sparse nodes: 121306150), hit rate: -nan% Osm2pgsql failed due to ERROR: CREATE INDEX planet_osm_ways_nodes ON planet_osm_ways USING gin (nodes) WITH (FASTUPDATE=OFF) ; failed: ERROR: invalid memory alloc request size 2013265920</p>
<p>I have a hard time thinking that this is a memory issue. Any help would be great. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '16, 15:26</strong></p>
<img src="https://secure.gravatar.com/avatar/943c484e8c04680902357de8f080dcc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cellington&#39;s gravatar image" />
<p><span>Cellington</span><br />
<span class="score" title="216 reputation points">216</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cellington has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-49575" class="comments-container">
&#10;</div>
<div id="comment-tools-49575" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49575-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

