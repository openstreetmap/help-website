+++
type = "question"
title = "Using Osmosis, bzcat and Postgresql"
description = '''I&#x27;m using Osmosis to load an extract of OSM data for the USA into a Postgresql database. I have previously used osm2pgsql.exe to load data into a postgresql database, but it is taking an extremely long time to load on my computer (Win 7 64 bit) using osm2pgsql 32 bit with the -s argument. I&#x27;m a uncl...'''
date = "2012-03-19T15:24:00Z"
lastmod = "2012-03-19T16:17:00Z"
weight = 11330
keywords = [ "bzip2", "postgresql", "osmosis" ]
aliases = [ "/questions/11330" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Using Osmosis, bzcat and Postgresql](/questions/11330/using-osmosis-bzcat-and-postgresql)

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
<span id="post-11330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11330-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using Osmosis to load an extract of OSM data for the USA into a Postgresql database. I have previously used osm2pgsql.exe to load data into a postgresql database, but it is taking an extremely long time to load on my computer (Win 7 64 bit) using osm2pgsql 32 bit with the <code>-s</code> argument. I'm a unclear about a couple of things using <code>osmosis</code> and <code>bzcat</code>. On the Osmosis wiki <a href="http://wiki.openstreetmap.org/wiki/Osmosis">page</a> I see the following instructions:</p>
<blockquote>
<p>Import a planet file into a local PostgreSQL rails port database.</p>
</blockquote>
<pre><code>osmosis --read-xml file=&quot;planet.osm&quot; --write-apidb host=&quot;x&quot; database=&quot;x&quot; user=&quot;x&quot; password=&quot;x&quot;</code></pre>
<p>I changed this line to the following, and tried adding a port argument</p>
<pre><code>osmosis --read-xml file=&quot;J:\DATA\OSM\massachusetts.osm&quot; --write-apidb host=&quot;localhost&quot; database=&quot;osm&quot; user=&quot;postgres&quot; password=&quot;**&quot; port=&quot;5436&quot;</code></pre>
<p>The error message I got was the following:</p>
<pre><code>J:\osmosis-0.40.1\bin&gt;osmosis --read-xml file=&quot;J:\DATA\OSM\massachusetts.osm&quot; --write-apidb host=&quot;localhost&quot; database=&quot;osm&quot; user=&quot;postgres&quot; password=&quot;***&quot; port=&quot;5436&quot;
Mar 19, 2012 11:28:16 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.40.1
Mar 19, 2012 11:28:29 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
Mar 19, 2012 11:28:32 AM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Argument port for task 2-write-apidb was not recognised.
        at org.openstreetmap.osmosis.core.pipeline.common.TaskManagerFactory.createTaskManager(TaskManagerFactory.java:64)
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.buildTasks(Pipeline.java:50)
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.prepare(Pipeline.java:112)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:86)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
        at java.lang.reflect.Method.invoke(Unknown Source)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:329)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:239)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:409)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:352)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
<p>Where I can I pass the port-number? While I am using localhost, my port-number is 5436 for this database. More generally, what does a <code>rails port</code> mean? Do I need to create a set of tables to match what the data is importing?</p>
<p>I am also trying to use <code>bzcat</code> to pull out an extract of the data so that I could use osm2pgsql.exe but this does not work.</p>
<pre><code>bzcat J:\DATA\OSM\massachusetts.osm.bz2 | J:\osmosis-0.40.1\bin\osmosis.bat --read-xml enableDateParsing=no file= --bounding-box top=42.48 left=-71.31 bottom=42.23 right=42.48 --write-xml file=  | bzip2 &gt; J:\DATA\OSM\extracted.osm.bz2</code></pre>
<p>When I ran this, I got an error message saying that bzip.dll was not on my system. I just saved the file linked on this <a href="http://wiki.openstreetmap.org/wiki/Osmosis#Windows_notes">page</a> and tried running that but it seems not to work.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bzip2" rel="tag" title="see questions tagged &#39;bzip2&#39;">bzip2</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '12, 15:24</strong></p>
<img src="https://secure.gravatar.com/avatar/2045d6b31de30983e8e020345da6cf55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="djq&#39;s gravatar image" />
<p><span>djq</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="djq has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '12, 15:40</strong> </span></p>
</div>
</div>
<div id="comments-container-11330" class="comments-container">
&#10;</div>
<div id="comment-tools-11330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11330-form-container" class="comment-form-container">
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

<span id="11332"></span>

<div id="answer-container-11332" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11332-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="djq has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First off osm2pgsql is importing to a postgis scheme usfull for rendering, osmosis is importing to a different postgresql scheme that is used by the api. The rails port is the implementation of the api and website at osm.org. These two schemes are not the same.</p>
<p>You are dealing with huge data here and you should give osm2pgsql lots of memmory, compile it in 64 bit mode, tune your database and use fast disks.</p>
<p>As for the dll problems you have, osmosis <em>--read-xml</em> and <em>--write-xml</em> have the option <em>compressionMethod</em> that can be set to gzip, bzip2, none or auto. The default is auto so your command should be</p>
<pre><code> J:\osmosis-0.40.1\bin\osmosis.bat --read-xml enableDateParsing=no file=&quot;J:\DATA\OSM\massachusetts.osm.bz2&quot; --bounding-box top=42.48 left=-71.31 bottom=42.23 right=42.48 --write-xml file=&quot;J:\DATA\OSM\extracted.osm.bz2&quot;</code></pre>
<p>Most of the tools in osm are not tested in windows and linux is prefered for development and hosting. You should try out a common linux distro like Ubuntu if you run into more problems.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Mar '12, 15:54</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-11332" class="comments-container">
<span id="11334"></span>
<div id="comment-11334" class="comment">
<div id="post-11334-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you, that fixed the dll/extract problem (it is running, anyway). I realize this is much easier on Linux (and have used it for similar tasks in the past), but unfortunately that is not an option for me at the moment. I can't find an osm2pgsql for Win 64 bit and I'm not familiar enough with MinGW to be able to build it (in a reasonable time frame). I am fortunate to have a fast computer and fast disks though....</p>
</div>
<div id="comment-11334-info" class="comment-info">
<span class="comment-age">(19 Mar '12, 16:17)</span> <span class="comment-user userinfo">djq</span>
</div>
</div>
</div>
<div id="comment-tools-11332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11332-form-container" class="comment-form-container">
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

