+++
type = "question"
title = "No space on device while using osm2postgresql (with PBF file)"
description = '''I am running osm2postgresql on an Ubuntu virtual machine (EC2 micro instance) using the instructions provided on the wiki.  Everything runs fine but I get the following error after the program has been running for a long time: Mar 04, 2014 2:42:31 PM org.openstreetmap.osmosis.core.pipeline.common.Ac...'''
date = "2014-03-04T16:40:00Z"
lastmod = "2014-03-05T09:06:00Z"
weight = 31275
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/31275" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [No space on device while using osm2postgresql (with PBF file)](/questions/31275/no-space-on-device-while-using-osm2postgresql-with-pbf-file)

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
<span id="post-31275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31275-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am running osm2postgresql on an Ubuntu virtual machine (EC2 micro instance) using the instructions provided on the wiki.</p>
<p>Everything runs fine but I get the following error after the program has been running for a long time:</p>
<pre><code>Mar 04, 2014 2:42:31 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
FINE: Waiting for task 1-read-pbf to complete.
Mar 04, 2014 3:29:56 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-pbf failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: An output error has occurred, aborting.
        at org.openstreetmap.osmosis.core.store.DataPostbox.checkForOutputErrors(DataPostbox.java:78)
        at org.openstreetmap.osmosis.core.store.DataPostbox.populateCentralQueue(DataPostbox.java:134)
        at org.openstreetmap.osmosis.core.store.DataPostbox.put(DataPostbox.java:184)
        at org.openstreetmap.osmosis.core.buffer.v0_6.EntityBuffer.process(EntityBuffer.java:38)
        at crosby.binary.osmosis.OsmosisBinaryParser.parseWays(OsmosisBinaryParser.java:172)
        at crosby.binary.BinaryParser.parse(BinaryParser.java:121)
        at crosby.binary.BinaryParser.handleBlock(BinaryParser.java:68)
        at crosby.binary.file.FileBlock.process(FileBlock.java:135)
        at crosby.binary.file.BlockInputStream.process(BlockInputStream.java:34)
        at crosby.binary.osmosis.OsmosisReader.run(OsmosisReader.java:37)
        at java.lang.Thread.run(Thread.java:744)
&#10;Mar 04, 2014 3:29:56 PM org.openstreetmap.osmosis.pgsnapshot.common.CopyFileWriter release
SEVERE: Unable to close writer.
java.io.IOException: No space left on device
        at java.io.FileOutputStream.writeBytes(Native Method)
        at java.io.FileOutputStream.write(FileOutputStream.java:345)
        at java.io.BufferedOutputStream.Mar 04, 2014 3:29:57 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 2-buffer failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to write value (SRID=4326;POLYGON((-93.2169649 44.9913991,-93.2169649 44.9914236,-93.2169311 44.9914236,-93.2169311 44.9913991,-93.2169649 44.9913991)))
        at org.openstreetmap.osmosis.pgsnapshot.common.CopyFileWriter.writeField(CopyFileWriter.java:253)
        at org.openstreetmap.osmosis.pgsnapshot.v0_6.impl.CopyFilesetBuilder.process(CopyFilesetBuilder.java:187)
        at org.openstreetmap.osmosis.core.container.v0_6.WayContainer.process(WayContainer.java:60)
        at org.openstreetmap.osmosis.pgsnapshot.v0_6.impl.CopyFilesetBuilder.process(CopyFilesetBuilder.java:115)
        at org.openstreetmap.osmosis.pgsnapshot.v0_6.PostgreSqlDumpWriter.process(PostgreSqlDumpWriter.java:58)
        at org.openstreetmap.osmosis.core.buffer.v0_6.EntityBuffer.run(EntityBuffer.java:74)
        at java.lang.Thread.run(Thread.java:744)
Caused by: java.io.IOException: No space left on device
        at java.io.FileOutputStream.writeBytes(Native Method)
        at java.io.FileOutputStream.write(FileOutputStream.java:345)
        at java.io.BufferedOutputStream.flushBuffer(BufferedOutputStream.java:82)
        at java.io.BufferedOutputStream.write(BufferedOutputStream.java:126)
        at sun.nio.cs.StreamEncoder.writeBytes(StreamEncoder.java:221)
        at sun.nio.cs.StreamEncoder.implWrite(StreamEncoder.java:282)
        at sun.nio.cs.StreamEncoder.write(StreamEncoder.java:125)
        at java.io.OutputStreamWriter.write(OutputStreamWriter.java:207)
        at java.io.BufferedWriter.flushBuffer(BufferedWriter.java:129)
        at java.io.BufferedWriter.write(BufferedWriter.java:230)
        at java.io.Writer.write(Writer.java:157)
        at org.openstreetmap.osmosis.pgsnapshot.common.CopyFileWriter.writeField(CopyFileWriter.java:249)
        ... 6 more
&#10;Mar 04, 2014 3:29:57 PM org.openstreetmap.osmosis.core.pipeline.common.PassiveTaskManager waitForCompletion
FINE: Task 3-write-pgsql-dump is passive, no completion wait required.
Mar 04, 2014 3:29:57 PM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
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
&#10;Error 1. The command which triggered the error was:
./$osmosis_version/bin/osmosis -v --read-$filetype file=&quot;$osmfile&quot; --buffer --write-pgsql-dump enableBboxBuilder=yes enableLinestringBuilder=yes nodeLocationStoreType=&quot;TempFile&quot; directory=&quot;$temporarydir&quot;
on line 435 of the osm2postgresql script.
## To delete the imported or temporary data, you might need to
 ## run something similar to this (use with care the lines with the &#39;*&#39;):
 # To remove osmosis temporary data:
 rm osmosis-0.40.tgz
 rm -r osmosis-0.40/
 rm -r ./tempgis
 # To delete the imported data, you may need to run:
 dropdb -p 5432 gis
 # If you created a tablespace:
 echo &quot;DROP TABLESPACE ;&quot; | /usr/lib/postgresql/9.1/bin/psql -p 5432
 # If you created a tablespace or used the --install option:
 sudo rm -r /var/lib/postgresql/PostgresPlus/data</code></pre>
<p>Only 20% of the disk space (out of 30 gigs) has been used. How can I resolve this error?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '14, 16:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ce2105c628f0492c916ba08fab8455d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vr3690&#39;s gravatar image" />
<p><span>vr3690</span><br />
<span class="score" title="66 reputation points">66</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vr3690 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '14, 16:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-31275" class="comments-container">
<span id="31276"></span>
<div id="comment-31276" class="comment">
<div id="post-31276-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>30 GB disk space is very little. Are you sure you aren't using more than 20% <em>during</em> the run of osm2postgresql? I would expect it to clean up afterwards, even if an error occurs. And how large is the file you are trying to import?</p>
</div>
<div id="comment-31276-info" class="comment-info">
<span class="comment-age">(04 Mar '14, 16:59)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="31277"></span>
<div id="comment-31277" class="comment">
<div id="post-31277-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How big's the PBF you're using?</p>
</div>
<div id="comment-31277-info" class="comment-info">
<span class="comment-age">(04 Mar '14, 17:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="31278"></span>
<div id="comment-31278" class="comment">
<div id="post-31278-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The PBF file is about 144MB in size. After the temp files are removed, around 9% of the disk space shows up as used. Should I be using a bigger disk?</p>
<p>EDIT: just checked again. The PBF file is around 137 MB downloaded from here - <a href="http://download.geofabrik.de/north-america/us/minnesota.html">http://download.geofabrik.de/north-america/us/minnesota.html</a></p>
</div>
<div id="comment-31278-info" class="comment-info">
<span class="comment-age">(04 Mar '14, 17:10)</span> <span class="comment-user userinfo">vr3690</span>
</div>
</div>
</div>
<div id="comment-tools-31275" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31275-form-container" class="comment-form-container">
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

<span id="31317"></span>

<div id="answer-container-31317" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31317-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-31317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="vr3690 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, are you really sure you need osm2postgresql? The program has been last modified 3 years ago. A lot has happened since then. For most uses, <a href="http://wiki.openstreetmpap.org/osm2pgsql">osm2pgsql</a> or <a href="http://www.imposm.org/">imposm</a> are the superior choices.<br />
</p>
<p>osm2postgresql will download and install an Osmosis version (0.40) that is known to have issues with 64-bit node IDs in some situations, but I am unsure if this would affect your use case.</p>
<p>Osmosis will write a temporary file to store node locations, and the results of Osmosis will be stored in another temporary file, to be loaded into PostgreSQL after; meaning that the process is likely to temporarily use much more memory than needed in the end. osm2postgresql lets you select where these files are stored; make sure you're not accidentally writing them to a partition that only has a fraction of the total hard disk available.</p>
<p>But again, check if you really want to use osm2postgresql at all.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '14, 09:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Mar '14, 09:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span></p>
</div>
</div>
<div id="comments-container-31317" class="comments-container">
&#10;</div>
<div id="comment-tools-31317" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31317-form-container" class="comment-form-container">
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

