+++
type = "question"
title = "[osm2pgsql] error during uploading changeset to nominatim"
description = ''' /app/nominatim/build/osm2pgsql/osm2pgsql -klas --number-processes 1 -C 2000 -O gazetteer -d nominatim.nominatim -P 5432 -U n_user -H nominatim-pgpool-service.nominatim /app/diff_53820819.osc  I got pgpool and 3 psql nodes. Periodically cron spawning a script to download changes from osm and upload ...'''
date = "2018-10-09T12:09:00Z"
lastmod = "2018-10-09T12:09:00Z"
weight = 66253
keywords = [ "nominatim", "osm", "osm2pgsql" ]
aliases = [ "/questions/66253" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[osm2pgsql\] error during uploading changeset to nominatim](/questions/66253/osm2pgsql-error-during-uploading-changeset-to-nominatim)

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
<span id="post-66253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66253-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<pre><code>   /app/nominatim/build/osm2pgsql/osm2pgsql -klas --number-processes 1 -C 2000 -O gazetteer -d nominatim.nominatim -P 5432 -U n_user -H nominatim-pgpool-service.nominatim  /app/diff_53820819.osc</code></pre>
<p>I got pgpool and 3 psql nodes. Periodically cron spawning a script to download changes from osm and upload them to nominatim.</p>
<p>During upload process I there is error:</p>
<pre><code>osm2pgsql version 0.96.0 (64 bit id space)
&#10;Using projection SRS 4326 (Latlong)
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=2000MB, maxblocks=32000*65536, allocation method=11
Mid: pgsql, cache=2000
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
&#10;Reading in file: /app/diff_53820819.osc
Using XML parser.
node cache: stored: 0(-nan%), storage efficiency: -nan% (dense blocks: 0, sparse nodes: 0), hit rate: -nan%
Osm2pgsql failed due to ERROR: delete_rel failed: server closed the connection unexpectedly
    This probably means the server terminated abnormally
    before or while processing the request.
(7)
Arguments were: 80305167,
ERROR: Error from osm2pgsql, 1</code></pre>
<p>In pg-pool logs:</p>
<pre><code>2018-10-09 10:57:41 ERROR: pid 58: Bind: cannot get parse message &quot;delete_rel&quot;
2018-10-09 10:57:41 LOG:   pid 58: do_child: exits with status 1 due to error
&#10;2018-10-09 10:57:41 LOG:   pid 89: ProcessFrontendResponse: failed to read kind from frontend. frontend abnormally exited
2018-10-09 10:57:41 LOG:   pid 103: ProcessFrontendResponse: failed to read kind from frontend. frontend abnormally exited
2018-10-09 10:57:41 LOG:   pid 95: ProcessFrontendResponse: failed to read kind from frontend. frontend abnormally exited</code></pre>
<p>As I understand "delete_rel" is a <code>prepared statement</code> which was not created. But when I tried to do the same operation locally it's working even without that <code>prepared statement</code>.</p>
<p>Any suggestions how to resolve this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '18, 12:09</strong></p>
<img src="https://secure.gravatar.com/avatar/f42fcb7796c887298a533a28d7ab3153?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="awerger&#39;s gravatar image" />
<p><span>awerger</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="awerger has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66253" class="comments-container">
&#10;</div>
<div id="comment-tools-66253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66253-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

