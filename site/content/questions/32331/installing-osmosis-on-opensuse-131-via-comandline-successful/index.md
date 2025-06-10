+++
type = "question"
title = "installing osmosis on opensuse 13.1 via comandline - successful"
description = '''hello dear linux-experts ive installed osmosis on suselinux version 13.1 )  linux-70ce:/home/martin # LANG=en_US.UTF-8 wget http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz --2014-04-12 22:09:52-- http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz Resolving bret...'''
date = "2014-04-12T21:22:00Z"
lastmod = "2014-04-13T09:02:00Z"
weight = 32331
keywords = [ "osmosis", "linux" ]
aliases = [ "/questions/32331" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [installing osmosis on opensuse 13.1 via comandline - successful](/questions/32331/installing-osmosis-on-opensuse-131-via-comandline-successful)

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
<span id="post-32331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32331-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello dear linux-experts</p>
<p>ive installed osmosis on suselinux version 13.1</p>
<pre><code>) 
linux-70ce:/home/martin # LANG=en_US.UTF-8  wget http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz
--2014-04-12 22:09:52--  http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz
Resolving bretth.dev.openstreetmap.org (bretth.dev.openstreetmap.org)... 128.40.168.103
Connecting to bretth.dev.openstreetmap.org (bretth.dev.openstreetmap.org)|128.40.168.103|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 9079737 (8.7M) [application/x-gzip]
Saving to: ‘osmosis-latest.tgz’
&#10;100%[==========================================================================================================================================&gt;] 9,079,737   1.38MB/s   in 6.3s
&#10;2014-04-12 22:09:58 (1.39 MB/s) - ‘osmosis-latest.tgz’ saved [9079737/9079737]
&#10;linux-70ce:/home/martin # tar xvfz osmosis-latest.tgz
readme.txt
copying.txt
changes.txt
script/
script/pgsnapshot_load_0.6.sql
script/pgsnapshot_schema_0.6_action.sql
script/pgsimple_schema_0.6_linestring.sql
script/pgsnapshot_schema_0.6_linestring.sql
script/pgsnapshot_schema_0.6_upgrade_4-5.sql
script/pgsimple_schema_0.6_action.sql
script/pgsimple_load_0.6.sql
script/pgsnapshot_schema_0.6_bbox.sql
script/pgsnapshot_schema_0.6_upgrade_5-6.sql
script/pgsnapshot_and_pgsimple.txt
script/fix_line_endings.sh
script/pgsimple_schema_0.6.sql
script/pgsimple_schema_0.6_bbox.sql
script/pgsnapshot_schema_0.6.sql
script/contrib/
script/contrib/dump_apidb.sh
script/contrib/replicate_osm_file.sh
script/contrib/CreateGeometryForWays.sql
script/contrib/apidb_0.6_osmosis_xid_indexing.sql
script/contrib/apidb_0.6.sql
script/munin/
script/munin/README
script/munin/osm_replication_lag
script/munin/osm_replication.conf
bin/
bin/osmosis-extract-apidb-0.6
bin/osmosis.bat
bin/osmosis-extract-mysql-0.6
bin/osmosis
config/
config/plexus.conf
lib/
lib/default/
lib/default/plexus-classworlds-2.4.jar
lib/default/commons-logging-1.1.1.jar
lib/default/jpf-1.5.jar
lib/default/stax2-api-3.1.1.jar
lib/default/woodstox-core-lgpl-4.1.4.jar
lib/default/xz-1.0.jar
lib/default/commons-compress-1.4.1.jar
lib/default/xercesImpl-2.9.1.jar
lib/default/commons-codec-1.7.jar
lib/default/commons-pool-1.5.4.jar
lib/default/commons-dbcp-1.4.jar
lib/default/spring-asm-3.1.2.RELEASE.jar
lib/default/spring-core-3.1.2.RELEASE.jar
lib/default/spring-beans-3.1.2.RELEASE.jar
lib/default/aopalliance-1.0.jar
lib/default/spring-aop-3.1.2.RELEASE.jar
lib/default/spring-expression-3.1.2.RELEASE.jar
lib/default/spring-context-3.1.2.RELEASE.jar
lib/default/spring-tx-3.1.2.RELEASE.jar
lib/default/spring-jdbc-3.1.2.RELEASE.jar
lib/default/postgresql-9.1-901-1.jdbc4.jar
lib/default/mysql-connector-java-5.1.21.jar
lib/default/protobuf-java-2.4.1.jar
lib/default/postgis-jdbc-1.3.3.jar
lib/default/netty-3.2.7.Final.jar
lib/default/osmosis-apidb-0.43.1.jar
lib/default/osmosis-areafilter-0.43.1.jar
lib/default/osmosis-core-0.43.1.jar
lib/default/osmosis-dataset-0.43.1.jar
lib/default/osmosis-extract-0.43.1.jar
lib/default/osmosis-pbf-0.43.1.jar
lib/default/osmosis-pbf2-0.43.1.jar
lib/default/osmosis-pgsimple-0.43.1.jar
lib/default/osmosis-pgsnapshot-0.43.1.jar
lib/default/osmosis-replication-0.43.1.jar
lib/default/osmosis-replication-http-0.43.1.jar
lib/default/osmosis-set-0.43.1.jar
lib/default/osmosis-tagfilter-0.43.1.jar
lib/default/osmosis-tagtransform-0.43.1.jar
lib/default/osmosis-xml-0.43.1.jar
lib/default/osmosis-osm-binary-0.43.1.jar
lib/default/osmosis-hstore-jdbc-0.43.1.jar
linux-70ce:/home/martin # cd osmosis-0.39
bash: cd: osmosis-0.39: Datei oder Verzeichnis nicht gefunden
linux-70ce:/home/martin # chmod a+x bin/osmosis
linux-70ce:/home/martin # bin/osmosis ls
Apr 12, 2014 10:16:19 PM org.openstreetmap.osmosis.core.Osmosis main
Schwerwiegend: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Expected argument 1 to be an option or task name.
        at org.openstreetmap.osmosis.core.cli.CommandLineParser.parse(CommandLineParser.java:79)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:74)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:606)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:329)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:239)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:409)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:352)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)
&#10;linux-70ce:/home/martin #</code></pre>
<p>well what do you say - is this all correct!?</p>
<p>see here</p>
<pre><code>bash: cd: osmosis-0.39: Datei oder Verzeichnis nicht gefunden</code></pre>
<p>which means - file or directory not found!`?</p>
<p>btw i afterwards tried to install osmfilter</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Osmfilter">http://wiki.openstreetmap.org/wiki/Osmfilter</a></p>
<p>Download and build in one run: wget -O - <a href="http://m.m.i24.cc/osmfilter.c">http://m.m.i24.cc/osmfilter.c</a> |cc -x c - -O3 -o osmfilter</p>
<p>As usual: There is no warranty, to the extent permitted by law.</p>
<pre><code>linux-70ce:/home/martin #  wget -O - http://m.m.i24.cc/osmfilter.c |cc -x c - -O3 -o osmfilter
--2014-04-12 22:34:49--  http://m.m.i24.cc/osmfilter.c
Auflösen des Hostnamen »m.m.i24.cc (m.m.i24.cc)«... 80.67.17.148, 2a00:1158:0:300:432f::1
Verbindungsaufbau zu m.m.i24.cc (m.m.i24.cc)|80.67.17.148|:80... verbunden.
HTTP-Anforderung gesendet, warte auf Antwort... 200 OK
Länge: 213497 (208K) [text/plain]
In »»STDOUT«« speichern.
&#10;100%[==========================================================================================================================================&gt;] 213.497     1,14MB/s   in 0,2s
&#10;2014-04-12 22:34:49 (1,14 MB/s) - auf die Standardausgabe geschrieben [213497/213497]
&#10;&lt;stdin&gt;: In function ‘oo__close’:
&lt;stdin&gt;:5166:5: warning: call to function ‘read_close’ without a real prototype [-Wunprototyped-calls]
&lt;stdin&gt;:1079:13: note: ‘read_close’ was declared here
linux-70ce:/home/martin #</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '14, 21:22</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '14, 21:36</strong> </span></p>
</div>
</div>
<div id="comments-container-32331" class="comments-container">
&#10;</div>
<div id="comment-tools-32331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32331-form-container" class="comment-form-container">
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

<span id="32332"></span>

<div id="answer-container-32332" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32332-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You successfully installed osmosis and you can now run it by typing</p>
<pre><code>/home/martin/bin/osmosis ...arguments...</code></pre>
<p>In your first attempt, you called osmosis and passed the argument "ls" which is not valid. See the Osmsis documentation for what arguments Osmosis accepts. In your second attempt, you tried to enter a directory called "osmosis-0.39" which you never created.</p>
<p>The one thing that you should have done differently is creating an extra directory for osmosis, like</p>
<pre><code>wget http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz
mkdir osmosis
cd osmosis
tar xzf ../osmosis-latest.tgz</code></pre>
<p>That way, Osmosis wouldn't have ended up directly in your $HOME, and you would then use</p>
<pre><code>/home/martin/osmosis/bin/osmosis ...arguments...</code></pre>
<p>to call it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '14, 21:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-32332" class="comments-container">
<span id="32346"></span>
<div id="comment-32346" class="comment">
<div id="post-32346-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello - many many thanks!!</p>
<p>did it like you adviced:</p>
<pre><code>linux-70ce:/home/martin # wget http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz
--2014-04-13 09:54:23--  http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz
Auflösen des Hostnamen »bretth.dev.openstreetmap.org (bretth.dev.openstreetmap.org)«... 128.40.168.103
Verbindungsaufbau zu bretth.dev.openstreetmap.org (bretth.dev.openstreetmap.org)|128.40.168.103|:80... verbunden.
HTTP-Anforderung gesendet, warte auf Antwort... 200 OK
Länge: 9079737 (8,7M) [application/x-gzip]
In »»osmosis-latest.tgz.1«« speichern.
&#10;100%[==========================================================================================================================================&gt;] 9.079.737   1,41MB/s   in 6,3s
&#10;2014-04-13 09:54:29 (1,38 MB/s) - »»osmosis-latest.tgz.1«« gespeichert [9079737/9079737]
&#10;linux-70ce:/home/martin # mkdir osmosis
linux-70ce:/home/martin # cd osmosis</code></pre>
<p>btw regarding the two other toools osmconvert osmfilter - i have had a loook at the corresponding websites.</p>
<p>should i have to install it like it is written on here :</p>
<blockquote>
<p>wiki.openstreetmap.org/wiki/Osmconvert‎</p>
<p>wiki.openstreetmap.org/wiki/Osmfilter‎</p>
</blockquote>
<p>Download and build in one run: wget -O - <a href="http://m.m.i24.cc/osmconvert.c">http://m.m.i24.cc/osmconvert.c</a> | cc -x c - -lz -O3 -o osmconvert</p>
<p>Download and build in one run: wget -O - <a href="http://m.m.i24.cc/osmfilter.c">http://m.m.i24.cc/osmfilter.c</a> |cc -x c - -O3 -o osmfilter</p>
<p>is this correct!? can i install osmconvert and filter in the above mentioned way.?</p>
</div>
<div id="comment-32346-info" class="comment-info">
<span class="comment-age">(13 Apr '14, 09:02)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-32332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32332-form-container" class="comment-form-container">
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

