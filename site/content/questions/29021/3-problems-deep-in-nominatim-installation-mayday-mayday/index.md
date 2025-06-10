+++
type = "question"
title = "[closed] 3 problems deep in   nominatim installation !! MAYDAY MAYDAY!"
description = '''Hello folks,  I am three problems deep into the whole setup of nominatim. I know little or nothing on postgresq. PLEASE HELP ME OUT :(. I have hardware configuration details listed below. i know its a 16 GB memory hardware and not 32 which is required for PLANET data but still tried it. And I am try...'''
date = "2013-12-13T01:47:00Z"
lastmod = "2013-12-13T05:43:00Z"
weight = 29021
keywords = [ "shmmax", "exception", "install" ]
aliases = [ "/questions/29021" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] 3 problems deep in nominatim installation !! MAYDAY MAYDAY!](/questions/29021/3-problems-deep-in-nominatim-installation-mayday-mayday)

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
<span id="post-29021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29021-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-29021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello folks, I am three problems deep into the whole setup of nominatim. I know little or nothing on postgresq. PLEASE HELP ME OUT :(. I have hardware configuration details listed below. i know its a 16 GB memory hardware and not 32 which is required for PLANET data but still tried it. And I am trying to setup planet data.</p>
<p>postgres@ilabshost18:/home/ilab$ free -m</p>
<pre><code>         total       used       free     shared    buffers     cached</code></pre>
<p>Mem: 16043 314 15729 0 19 74</p>
<p>-/+ buffers/cache: 220 15823</p>
<p>Swap: 16383 0 16383</p>
<p>postgres@ilabshost18:/home/ilab$ uname -a</p>
<p>Linux ilabshost18 3.5.0-34-generic #55~precise1-Ubuntu SMP Fri Jun 7 16:25:50 UTC 2013 x86_64 x86_64 x86_64 GNU/Linux</p>
<p>postgres@ilabshost18:/home/ilab$ df -kh</p>
<p>Filesystem Size Used Avail Use% Mounted on</p>
<p>/dev/mapper/ilabshost18-root 8.7G 4.3G 4.0G 52% /</p>
<p>udev 7.9G 4.0K 7.9G 1% /dev</p>
<p>tmpfs 3.2G 280K 3.2G 1% /run</p>
<p>none 5.0M 0 5.0M 0% /run/lock</p>
<p>none 7.9G 0 7.9G 0% /run/shm</p>
<p>/dev/sda1 228M 51M 166M 24% /boot</p>
<p>/dev/mapper/data-data 2.0T 40G 1.9T 3% /data</p>
<p>Problem 1.</p>
<p>I followed the installation instructions for ubuntu provided, in link <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">http://wiki.openstreetmap.org/wiki/Nominatim/Installation</a> think went fine until, I ran the command to import ./utils/setup.php --osm-file &lt;your planet="" file=""&gt; --all [--osm2pgsql-cache 18000] as it says. For me it did not pick up the arguments [--osm2pgsql-cache 18000] so had to run it without it. It ran for few minutes and then</p>
<p>Problem 2.</p>
<p>I ran just this ./utils/setup.php --osm-file &lt;your planet="" file=""&gt; --all but while import it failed with the following exception.</p>
<p>Reading in file: /data/Nominatim-2.1/planet-131204.osm.pbf Processing: Node(2113460k 494.6k/s) Way(0k 0.00k/s) Relation(0 0.00/s)COPY_END for COPY planet_osm_nodes FROM STDIN; failed: ERROR: could not extend file "base/16386/18838.1": wrote only 4096 of 8192 bytes at block 246872 HINT: Check free disk space. CONTEXT: COPY planet_osm_nodes, line 45671321: "76661940 473543350 -1009701829 \N"</p>
<p>Error occurred, cleaning up ERROR: Error executing external command: /data/Nominatim-2.1/osm2pgsql/osm2pgsql -lsc -O gazetteer --hstore -C 14914 -P 5432 -d nominatim /data/Nominatim-2.1planet-131204.osm.pbf Error executing external command: /data/Nominatim-2.1/osm2pgsql/osm2pgsql -lsc -O gazetteer --hstore -C 14914 -P 5432 -d nominatim /data/Nominatim-2.1/planet131204.osm.pbf</p>
<p>The hint clearly says its a disk space issue. The mount which the directory has over 2TB of free space is /data/Nominatim-2.1/ but /var/lib has only 4 GB space. So I changed the data_directory in postgreSQL.conf to point the directory /data/nominatimdata killed the postgresql process and then restarted with the following command.</p>
<p>/usr/lib/postgresql/9.1/bin/postgres -D /var/lib/postgresql/9.1/main -c config_file=/etc/postgresql/9.1/main/postgresql.conf</p>
<p>It errored out suggesting that the directory /data/nominatimdata has no PG_VERSION file. So I reverted it back to the same old configuration in postgresql.conf and try fix this in a different way.</p>
<p>Problem 3.</p>
<p>After I changed this and tried to restart it, it errored again, following is the exception.As the HINT says I tried to reset the shared_buffers size from 4 gb to 2gb. Also I found a comment to change /etc/sysctl.conf the values of kernel.shmmax to a bigger number and to run sudo sysctl -p, kernel.shmmax in /etc/sysctl.conf was not present so I added the value as 4GB and ran sudo sysctl -p. tried restarting and found the same error.</p>
<p>I found an another comment which said to update the values in /etc/sysctl.d/30-postgresql-shm.conf I tried that, even this dint work.</p>
<p>Following the detailed exception I am encountering. postgres@ilabshost18:/home/ilab$ /usr/lib/postgresql/9.1/bin/postgres -D /var/lib/postgresql/9.1/main -c config_file=/etc/postgresql/9.1/main/postgresql.conf 2013-12-12 19:36:03 EST FATAL: could not create shared memory segment: Invalid argument 2013-12-12 19:36:03 EST DETAIL: Failed system call was shmget(key=5432001, size=2220433408, 03600). 2013-12-12 19:36:03 EST H INT: This error usually means that PostgreSQL's request for a shared memory segment exceeded your kernel's SHMMAX parameter. You can either reduce the request size or reconfigure the kernel with larger SHMMAX. To reduce the request size (currently 2220433408 bytes), reduce PostgreSQL's shared memory usage, perhaps by reducing shared_buffers or max_connections. If the request size is already small, it's possible that it is less than your kernel's SHMMIN parameter, in which case raising the request size or reconfiguring SHMMIN is called for. The PostgreSQL documentation contains more information about shared memory configuration.</p>
<p>Please help me out.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shmmax" rel="tag" title="see questions tagged &#39;shmmax&#39;">shmmax</span> <span class="post-tag tag-link-exception" rel="tag" title="see questions tagged &#39;exception&#39;">exception</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '13, 01:47</strong></p>
<img src="https://secure.gravatar.com/avatar/576a9cbae52513a136aca47c4f0544e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ironknight&#39;s gravatar image" />
<p><span>Ironknight</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ironknight has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>13 Dec '13, 05:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-29021" class="comments-container">
&#10;</div>
<div id="comment-tools-29021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29021-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Tl;dr. Most of question relates to Postgres /Ubuntu rather than Nominatim in particular." by SK53 13 Dec '13, 05:56

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29024"></span>

<div id="answer-container-29024" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29024-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have already asked about questions 2 &amp; 3 a week ago on this site in response to <a href="https://help.openstreetmap.org/questions/26900/import-error-could-not-extend-file">this question.</a></p>
<p>This site is meant for short <strong>SINGLE</strong> questions of wide-spread interest: it is not meant for detailed support for a specific user.</p>
<p>Questions about allocating space for the default data storage of Postgres anyway belong on something like StackOverflow rather than here. In general it is much better to ask about this kind of detail via the OSM forum, on mailing lists or on an IRC channel: but before you do, please ensure you have sorted out how you allocate data for Postgres.</p>
<p>Your first question may be more useful: but it will require rephrasing and shortening. It also dont know why you want to pass in a cache allocation limit which is more than your available memory.</p>
<p>For these reasons I am closing this question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '13, 05:43</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-29024" class="comments-container">
&#10;</div>
<div id="comment-tools-29024" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29024-form-container" class="comment-form-container">
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

