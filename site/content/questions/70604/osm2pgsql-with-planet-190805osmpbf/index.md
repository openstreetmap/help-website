+++
type = "question"
title = "osm2pgsql with planet-190805.osm.pbf ?"
description = '''Is it possible to import the planet-190805.osm.pbf in the server with: 8 vcpus, 32 GiB memory, 30GB(SSD)+1TB(SSD) ??? what is the min CACHESIZE for the import? I got Out of memory with CACHESIZE=8192 and CACHESIZE=4096 during import the Relation. shell: export CACHESIZE=??? osm2pgsql --create --slim...'''
date = "2019-09-03T01:15:00Z"
lastmod = "2019-09-03T07:27:00Z"
weight = 70604
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/70604" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql with planet-190805.osm.pbf ?](/questions/70604/osm2pgsql-with-planet-190805osmpbf)

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
<span id="post-70604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70604-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to import the planet-190805.osm.pbf in the server with:</p>
<p>8 vcpus, 32 GiB memory, 30GB(SSD)+1TB(SSD) ???</p>
<p>what is the min CACHESIZE for the import?</p>
<p>I got Out of memory with CACHESIZE=8192 and CACHESIZE=4096 during import the Relation.</p>
<p>shell:</p>
<p>export CACHESIZE=???</p>
<p>osm2pgsql --create --slim --hstore --cache ${CACHESIZE} --multi-geometry --unlogged --flat-nodes /var/lib/osm/nodes.cache --hstore-add-index --number-processes 8 --database gis --username osm /mnt/resource/planet-190805.osm.pbf</p>
<p>planet-190805.osm.pbf</p>
<p>Node,Way,Relation<br />
5369694,595461,7041415</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Sep '19, 01:15</strong></p>
<img src="https://secure.gravatar.com/avatar/5d7bbd96dde7f9bc6a9e599a925f9a76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nationals&#39;s gravatar image" />
<p><span>Nationals</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nationals has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-70604" class="comments-container">
<span id="70605"></span>
<div id="comment-70605" class="comment">
<div id="post-70605-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>even as CACHESIZE=18000,</p>
<p>and CACHESIZE=30000 in another server.</p>
</div>
<div id="comment-70605-info" class="comment-info">
<span class="comment-age">(03 Sep '19, 01:18)</span> <span class="comment-user userinfo">Nationals</span>
</div>
</div>
<span id="70607"></span>
<div id="comment-70607" class="comment">
<div id="post-70607-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I means disable the swap.</p>
</div>
<div id="comment-70607-info" class="comment-info">
<span class="comment-age">(03 Sep '19, 07:27)</span> <span class="comment-user userinfo">Nationals</span>
</div>
</div>
</div>
<div id="comment-tools-70604" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70604-form-container" class="comment-form-container">
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

<span id="70606"></span>

<div id="answer-container-70606" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70606-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>import the pbf file with : osm2pgsql --create --slim --flat-nodes /mnt/resource/nodes.cache /opt/osm/planet-190805.osm.pbf</p>
<p>then, the file /mnt/resource/nodes.cache must been keep for osm2pgsql --append ?</p>
<p>and will the osm2pgsql --append update the file /mnt/resource/nodes.cache for next running time?</p>
<p>and is the file /mnt/resource/nodes.cache need for mapnik etc.?</p>
<p>flat-nodes osm2pgsql asked 30 Aug, 02:35</p>
<p>Nationals's gravatar image Nationals 11●2 accept rate: 0%</p>
<p>edited 19 mins ago</p>
<p>how about the performance different using --flat-nodes or not while osm2pgs</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '19, 01:53</strong></p>
<img src="https://secure.gravatar.com/avatar/796a59faba9d9315e4c72733a08b5e9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fon&#39;s gravatar image" />
<p><span>fon</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70606" class="comments-container">
&#10;</div>
<div id="comment-tools-70606" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70606-form-container" class="comment-form-container">
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

