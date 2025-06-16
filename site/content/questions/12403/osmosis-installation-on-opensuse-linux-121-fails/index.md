+++
type = "question"
title = "osmosis installation on OpenSuse-Linux - 12.1 fails"
description = '''hello dear buddies on OpenStreetMap - good evening,  welll i am pretty new to GIS-Computing: at the moment i am tryin to install OsMosis on my openSuse 12.1 linux-system. if i follow this steps here - the steps i found here on the page called - installing osmosis  https://wiki.openstreetmap.org/wiki/...'''
date = "2012-04-27T22:27:00Z"
lastmod = "2014-04-13T21:36:00Z"
weight = 12403
keywords = [ "openstreetmap", "database", "data", "linux" ]
aliases = [ "/questions/12403" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmosis installation on OpenSuse-Linux - 12.1 fails](/questions/12403/osmosis-installation-on-opensuse-linux-121-fails)

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
<span id="post-12403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12403-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello dear buddies on OpenStreetMap - good evening,</p>
<p>welll i am pretty new to GIS-Computing: at the moment i am tryin to install OsMosis on my openSuse 12.1 linux-system.</p>
<p>if i follow this steps here - the steps i found here on the page called - installing osmosis</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Osmosis/Installation">https://wiki.openstreetmap.org/wiki/Osmosis/Installation</a></p>
<pre><code>LANG=en_US.UTF-8  wget http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz
tar xvfz osmosis-latest.tgz
cd osmosis-0.39
chmod a+x bin/osmosis
bin/osmosis</code></pre>
<p>then i get the following results:</p>
<pre><code>linux-wyee:/home/martin # LANG=en_US.UTF-8  wget http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz
asking libproxy about url &#39;http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz&#39;
libproxy suggest to use &#39;direct://&#39;
--2012-04-27 22:58:10--  http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz
Resolving bretth.dev.openstreetmap.org (bretth.dev.openstreetmap.org)... 128.40.168.103
Connecting to bretth.dev.openstreetmap.org (bretth.dev.openstreetmap.org)|128.40.168.103|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 7683042 (7.3M) [application/x-gzip]
Saving to: `osmosis-latest.tgz.2&#39;
&#10;100%[======================================================================================================================================================&gt;] 7,683,042    502K/s   in 15s
&#10;2012-04-27 22:58:26 (496 KB/s) - `osmosis-latest.tgz.2&#39; saved [7683042/7683042]
&#10;linux-wyee:/home/martin # tar xvfz osmosis-latest.tgz
osmosis-0.40.1/bin/
osmosis-0.40.1/build/
osmosis-0.40.1/config/
osmosis-0.40.1/lib/
osmosis-0.40.1/lib/default/
osmosis-0.40.1/script/
osmosis-0.40.1/script/contrib/
osmosis-0.40.1/script/munin/
osmosis-0.40.1/build/version.txt
osmosis-0.40.1/changes.txt
osmosis-0.40.1/config/plexus.conf
osmosis-0.40.1/copying.txt
osmosis-0.40.1/lib/default/aopalliance-1.0.jar
osmosis-0.40.1/lib/default/commons-codec-1.5.jar
osmosis-0.40.1/lib/default/commons-compress-1.2.jar
osmosis-0.40.1/lib/default/commons-dbcp-1.4.jar
osmosis-0.40.1/lib/default/commons-logging-1.1.1.jar
osmosis-0.40.1/lib/default/commons-pool-1.5.4.jar
osmosis-0.40.1/lib/default/jpf-1.5.jar
osmosis-0.40.1/lib/default/mysql-connector-java-5.1.18.jar
osmosis-0.40.1/lib/default/osmosis-apidb-0.40.1.jar
osmosis-0.40.1/lib/default/osmosis-areafilter-0.40.1.jar
osmosis-0.40.1/lib/default/osmosis-core-0.40.1.jar
osmosis-0.40.1/lib/default/osmosis-dataset-0.40.1.jar
osmosis-0.40.1/lib/default/osmosis-extract-0.40.1.jar
osmosis-0.40.1/lib/default/osmosis-hstore-0.40.1.jar
osmosis-0.40.1/lib/default/osmosis-pbf-0.40.1.jar
osmosis-0.40.1/lib/default/osmosis-pgsimple-0.40.1.jar
osmosis-0.40.1/lib/default/osmosis-pgsnapshot-0.40.1.jar
osmosis-0.40.1/lib/default/osmosis-replication-0.40.1.jar
osmosis-0.40.1/lib/default/osmosis-set-0.40.1.jar
osmosis-0.40.1/lib/default/osmosis-tagfilter-0.40.1.jar
osmosis-0.40.1/lib/default/osmosis-xml-0.40.1.jar
osmosis-0.40.1/lib/default/osmpbf-1.1.1-754a33af.jar
osmosis-0.40.1/lib/default/plexus-classworlds-2.4.jar
osmosis-0.40.1/lib/default/postgis-jdbc-1.3.3.jar
osmosis-0.40.1/lib/default/postgresql-9.0-801.jdbc4.jar
osmosis-0.40.1/lib/default/protobuf-java-2.4.1.jar
osmosis-0.40.1/lib/default/spring-aop-3.0.6.RELEASE.jar
osmosis-0.40.1/lib/default/spring-asm-3.0.6.RELEASE.jar
osmosis-0.40.1/lib/default/spring-beans-3.0.6.RELEASE.jar
osmosis-0.40.1/lib/default/spring-context-3.0.6.RELEASE.jar
osmosis-0.40.1/lib/default/spring-core-3.0.6.RELEASE.jar
osmosis-0.40.1/lib/default/spring-expression-3.0.6.RELEASE.jar
osmosis-0.40.1/lib/default/spring-jdbc-3.0.6.RELEASE.jar
osmosis-0.40.1/lib/default/spring-tx-3.0.6.RELEASE.jar
osmosis-0.40.1/lib/default/stax2-api-3.1.1.jar
osmosis-0.40.1/lib/default/woodstox-core-lgpl-4.1.2.jar
osmosis-0.40.1/lib/default/xercesImpl-2.9.1.jar
osmosis-0.40.1/readme.txt
osmosis-0.40.1/script/contrib/CreateGeometryForWays.sql
osmosis-0.40.1/script/contrib/apidb_0.6.sql
osmosis-0.40.1/script/contrib/apidb_0.6_osmosis_xid_indexing.sql
osmosis-0.40.1/script/contrib/dump_apidb.sh
osmosis-0.40.1/script/contrib/replicate_osm_file.sh
osmosis-0.40.1/script/fix_line_endings.sh
osmosis-0.40.1/script/munin/README
osmosis-0.40.1/script/munin/osm_replication.conf
osmosis-0.40.1/script/munin/osm_replication_lag
osmosis-0.40.1/script/pgsimple_load_0.6.sql
osmosis-0.40.1/script/pgsimple_schema_0.6.sql
osmosis-0.40.1/script/pgsimple_schema_0.6_action.sql
osmosis-0.40.1/script/pgsimple_schema_0.6_bbox.sql
osmosis-0.40.1/script/pgsimple_schema_0.6_linestring.sql
osmosis-0.40.1/script/pgsnapshot_and_pgsimple.txt
osmosis-0.40.1/script/pgsnapshot_load_0.6.sql
osmosis-0.40.1/script/pgsnapshot_schema_0.6.sql
osmosis-0.40.1/script/pgsnapshot_schema_0.6_action.sql
osmosis-0.40.1/script/pgsnapshot_schema_0.6_bbox.sql
osmosis-0.40.1/script/pgsnapshot_schema_0.6_linestring.sql
osmosis-0.40.1/script/pgsnapshot_schema_0.6_upgrade_4-5.sql
osmosis-0.40.1/script/pgsnapshot_schema_0.6_upgrade_5-6.sql
osmosis-0.40.1/bin/osmosis
osmosis-0.40.1/bin/osmosis-extract-apidb-0.6
osmosis-0.40.1/bin/osmosis-extract-mysql-0.6
osmosis-0.40.1/bin/osmosis.bat
linux-wyee:/home/martin # cd osmosis-0.39
bash: cd: osmosis-0.39: Datei oder Verzeichnis nicht gefunden
linux-wyee:/home/martin # chmod a+x bin/osmosis
chmod: Zugriff auf „bin/osmosis“ nicht möglich: Datei oder Verzeichnis nicht gefunden
linux-wyee:/home/martin # bin/osmosis
bash: bin/osmosis: Datei oder Verzeichnis nicht gefunden</code></pre>
<p>the last lines mean;</p>
<pre><code>bash: cd: osmosis-0.39: Datei oder Verzeichnis nicht gefunden</code></pre>
<p>So we have some intersting lines at the end:</p>
<pre><code>bash: cd: osmosis-0.39: file or directory was not found 
chmod: no access on „bin/osmosis“ it is not possible to access &quot;bin/osmosis&quot;: file or direcory werent found 
linux-wyee:/home/martin # bin/osmosis
bash: bin/osmosis: directory or file werent found</code></pre>
<p>so what!? what goes wrong here. What can we do here to install osmosis in a correct way!? thx for any and all help...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '12, 22:27</strong></p>
<img src="https://secure.gravatar.com/avatar/600fc90e36ff81dfaba666708cf91dc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tagtheworld&#39;s gravatar image" />
<p><span>tagtheworld</span><br />
<span class="score" title="0 reputation points">0</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tagtheworld has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12403" class="comments-container">
&#10;</div>
<div id="comment-tools-12403" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12403-form-container" class="comment-form-container">
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

<span id="12406"></span>

<div id="answer-container-12406" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12406-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You asked for the latest version and got "<code>osmosis-0.40.1</code>" (it's at the start of the first line of each file that the "<code>tar xvfz</code>" command outputs) but you're trying to cd to "<code>osmosis-0.39</code>".</p>
<p>If you want to keep working with osmosis-0.40.1 (which I guess you do) just "<code>cd osmosis-0.40.1</code>" instead, or obtain a copy of osmosis-0.39 if you want to work with that instead.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '12, 23:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-12406" class="comments-container">
<span id="32347"></span>
<div id="comment-32347" class="comment">
<div id="post-32347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello - thx again - i did it.</p>
<p>see here</p>
<pre><code>martin # 
linux-70ce:/home/martin # wget http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz
--2014-04-13 09:54:23--  http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz
Auflösen des Hostnamen »bretth.dev.openstreetmap.org (bretth.dev.openstreetmap.org)«... 128.40.168.103
Verbindungsaufbau zu bretth.dev.openstreetmap.org (bretth.dev.openstreetmap.org)|128.40.168.103|:80... verbunden.
HTTP-Anforderung gesendet, warte auf Antwort... 200 OK
Länge: 9079737 (8,7M) [application/x-gzip]
In »»osmosis-latest.tgz.1«« speichern.
&#10;100%[==========================================================================================================================================&gt;] 9.079.737   1,41MB/s   in 6,3s
&#10;2014-04-13 09:54:29 (1,38 MB/s) - »»osmosis-latest.tgz.1«« gespeichert [9079737/9079737]
&#10;linux-70ce:/home/martin # mkdir osmosis
linux-70ce:/home/martin # cd osmosis^C
linux-70ce:/home/martin # cd osmosis-0.40.1
bash: cd: osmosis-0.40.1: Datei oder Verzeichnis nicht gefunden
linux-70ce:/home/martin # cd osmosis
linux-70ce:/home/martin/osmosis # ls
linux-70ce:/home/martin/osmosis # ls -l
insgesamt 0
linux-70ce:/home/martin/osmosis #</code></pre>
<p>btw - how can ic check the version that i installed</p>
<p>btw regarding the two other toools osmconvert osmfilter - i have had a loook at the corresponding websites. should i have to install it like it is written on here :</p>
<blockquote>
<p>wiki.openstreetmap.org/wiki/Osmconvert‎</p>
</blockquote>
<p>and here</p>
<blockquote>
<p>wiki.openstreetmap.org/wiki/Osmfilter‎</p>
<p>Download and build in one run: wget -O - <a href="http://m.m.i24.cc/osmconvert.c">http://m.m.i24.cc/osmconvert.c</a> | cc -x c - -lz -O3 -o osmconvert Download and build in one run: wget -O - <a href="http://m.m.i24.cc/osmfilter.c">http://m.m.i24.cc/osmfilter.c</a> |cc -x c - -O3 -o osmfilter</p>
</blockquote>
<p>what do you suggest?</p>
</div>
<div id="comment-32347-info" class="comment-info">
<span class="comment-age">(13 Apr '14, 09:37)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="32352"></span>
<div id="comment-32352" class="comment">
<div id="post-32352-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think that the above comment is actually part of the conversation on <a href="/questions/32331/installing-osmosis-on-opensuse-131-via-comandline-successful">this other question</a> (though as it's to do with osmosis installation, I suppose it makes some sense to leave it here as a link).</p>
</div>
<div id="comment-32352-info" class="comment-info">
<span class="comment-age">(13 Apr '14, 21:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-12406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12406-form-container" class="comment-form-container">
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

