+++
type = "question"
title = "osm2pgsql: Failed to allocate space for node"
description = '''Hi, I have the following error when i try to import europe-latest.osm.pbf into database: import command : ./utils/setup.php --osm-file europe-latest.osm.pbf --all --osm2pgsql-cache 1000 2&amp;gt;&amp;amp;1 | tee setup.log error: Failed to allocate space for node cache file: Internal error 22 Error occurred,...'''
date = "2017-06-09T12:02:00Z"
lastmod = "2017-06-09T12:02:00Z"
weight = 56549
keywords = [ "nominatim", "osm2pgsql" ]
aliases = [ "/questions/56549" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql: Failed to allocate space for node](/questions/56549/osm2pgsql-failed-to-allocate-space-for-node)

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
<span id="post-56549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56549-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have the following error when i try to import europe-latest.osm.pbf into database:</p>
<p>import command : ./utils/setup.php --osm-file europe-latest.osm.pbf --all --osm2pgsql-cache 1000 2&gt;&amp;1 | tee setup.log</p>
<pre><code>error: Failed to allocate space for node cache file: Internal error 22 Error occurred, cleaning up I&#39;m using ubuntu 14.04 and i have 800 GB free space, 24 GB RAM installed.
&#10;osm2pgsql SVN version 0.89.0-dev (64bit id space)
&#10;Using projection SRS 4326 (Latlong) NOTICE: table &quot;place&quot; does not exist, skipping Allocating memory for sparse node cache Node-cache: cache=1000MB, maxblocks=0*128000, allocation method=8192 Mid: loading persistent node cache from /home/nominatim/Nominatim-2.5.1/osm2pgsql/flat.nodes Failed to allocate space for node cache file: Internal error 22 Error occurred, cleaning up ERROR: Error executing external command: /home/nominatim/Nominatim-2.5.1/osm2pgsql/osm2pgsql --flat-nodes /home/nominatim/Nominatim-2.5.1/osm2pgsql/flat.nodes -lsc -O gazetteer --hstore --number-processes 1 -C 1000 -P 5432 -d nominatim /home/nominatim/Nominatim-2.5.1/europe-latest.osm.pbf Error executing external command: /home/nominatim/Nominatim-2.5.1/osm2pgsql/osm2pgsql --flat-nodes /home/nominatim/Nominatim-2.5.1/osm2pgsql/flat.nodes -lsc -O gazetteer --hstore --number-processes 1 -C 1000 -P 5432 -d nominatim /home/nominatim/Nominatim-2.5.1/europe-latest.osm.pbf</code></pre>
<p>If anyone has any ideea please help.</p>
<pre><code>root@:/home/nominatim/Nominatim-2.5.1# df -h
Filesystem      Size  Used Avail Use% Mounted on
udev             12G  4.0K   12G   1% /dev
tmpfs           2.4G  796K  2.4G   1% /run
/dev/dm-0       892G   41G  807G   5% /
none            4.0K     0  4.0K   0% /sys/fs/cgroup
none            5.0M     0  5.0M   0% /run/lock
none             12G     0   12G   0% /run/shm
none            100M     0  100M   0% /run/user
/dev/sda1       236M   39M  185M  18% /boot
&#10;root@:/home/nominatim/Nominatim-2.5.1# df -i
Filesystem       Inodes  IUsed    IFree IUse% Mounted on
udev             156520    480   156040    1% /dev
tmpfs            162032    516   161516    1% /run
/dev/dm-0      59400192 147447 59252745    1% /
none             162032      2   162030    1% /sys/fs/cgroup
none             162032      4   162028    1% /run/lock
none             162032      1   162031    1% /run/shm
none             162032      2   162030    1% /run/user
/dev/sda1         62248    298    61950    1% /boot</code></pre>
<p>Thank you !</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jun '17, 12:02</strong></p>
<img src="https://secure.gravatar.com/avatar/40b2e5d71e5d1cc30e9d19991cd9a5bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="valianghel&#39;s gravatar image" />
<p><span>valianghel</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="valianghel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jun '17, 13:02</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-56549" class="comments-container">
&#10;</div>
<div id="comment-tools-56549" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56549-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

