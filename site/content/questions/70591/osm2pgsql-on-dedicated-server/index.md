+++
type = "question"
title = "osm2pgsql on Dedicated Server ???"
description = '''how to optimization the osm2pgsql on Dedicated Server (centos 7)? I have 2 of this testing server with: 1) 8 core, 32G RAM， NVME 512GB 2) 8 core, 64G RAM， NVME 512GB software: Linux (centos 7.6.1810) /etc/sysctl.conf vm.swappiness = 0 /etc/security/limits.conf * soft nofile 1024000  * hard nofile 10...'''
date = "2019-09-02T03:53:00Z"
lastmod = "2019-09-02T10:53:00Z"
weight = 70591
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/70591" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql on Dedicated Server ???](/questions/70591/osm2pgsql-on-dedicated-server)

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
<span id="post-70591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70591-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>how to optimization the osm2pgsql on Dedicated Server (centos 7)?</p>
<p>I have 2 of this testing server with:</p>
<p>1) 8 core, 32G RAM， NVME 512GB</p>
<p>2) 8 core, 64G RAM， NVME 512GB</p>
<p>software: Linux (centos 7.6.1810)</p>
<p>/etc/sysctl.conf</p>
<p>vm.swappiness = 0</p>
<p>/etc/security/limits.conf</p>
<p>* soft nofile 1024000<br />
* hard nofile 1024000<br />
* soft nproc unlimited<br />
* hard nproc unlimited<br />
* soft core unlimited<br />
* hard core unlimited<br />
* soft memlock unlimited<br />
* hard memlock unlimited</p>
<p>/etc/fstab</p>
<p>/dev/mapper/centos-root / xfs defaults,noatime,nodiratime 0 0</p>
<p>sh run:</p>
<p>export FLATNODESFILE=/var/osm/nodes.cache</p>
<p>export PBFFILE=/mnt/resource/planet-190805.osm.pbf</p>
<p>export CACHESIZE=30000 # how to optimization this para on differencce HW</p>
<p>export PGPASSWORD=&lt; pg_password &gt;</p>
<p># /usr/local/share/osm2pgsql/default.style</p>
<p>osm2pgsql --create --hstore --hstore-add-index --cache $CACHESIZE --multi-geometry --unlogged \</p>
<p>--flat-nodes $FLATNODESFILE --number-processes 8 -v \</p>
<p>--host &lt; PG_Server_IP &gt; --port 5432 --database gis --username osm $PBFFILE</p>
<p>any other optimization are need?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '19, 03:53</strong></p>
<img src="https://secure.gravatar.com/avatar/5d7bbd96dde7f9bc6a9e599a925f9a76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nationals&#39;s gravatar image" />
<p><span>Nationals</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nationals has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Sep '19, 04:20</strong> </span></p>
</div>
</div>
<div id="comments-container-70591" class="comments-container">
<span id="70593"></span>
<div id="comment-70593" class="comment">
<div id="post-70593-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>DateFile Node Way Relation</p>
<p>190722 5330978k 591991k 6917050</p>
</div>
<div id="comment-70593-info" class="comment-info">
<span class="comment-age">(02 Sep '19, 04:15)</span> <span class="comment-user userinfo">Nationals</span>
</div>
</div>
</div>
<div id="comment-tools-70591" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70591-form-container" class="comment-form-container">
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

<span id="70595"></span>

<div id="answer-container-70595" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70595-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suggest to set <code>--number-processes</code> to about half your cores, not the full number. Also, 512 GB of disk space will <em>not</em> be sufficient for a full planet import (1 TB is needed and even that will soon run out). This help site also has some recommendations about optimizing your postgresql.conf (e.g. <a href="https://help.openstreetmap.org/questions/60910/how-can-osm2pgsqlpostgresqlconf-be-optimized-to-process-ways">here).</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '19, 08:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-70595" class="comments-container">
<span id="70598"></span>
<div id="comment-70598" class="comment">
<div id="post-70598-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>PG SQL is on another Dedicated Server with 1TB NVME.</p>
</div>
<div id="comment-70598-info" class="comment-info">
<span class="comment-age">(02 Sep '19, 10:53)</span> <span class="comment-user userinfo">Nationals</span>
</div>
</div>
</div>
<div id="comment-tools-70595" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70595-form-container" class="comment-form-container">
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

