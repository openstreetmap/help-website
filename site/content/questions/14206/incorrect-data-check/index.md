+++
type = "question"
title = "incorrect data check"
description = '''Yesterday I downloaded planet-latest.osm.pbf. Today I tried to run: osmosis --rb file=&quot;c:&#92;osm_data&#92;planet-latest.osm.pbf&quot;  --bp file=&quot;c:&#92;osm_data&#92;united_states.poly&quot; --bp file=&quot;c:&#92;osm_data&#92;canada.poly&quot;  --tf accept-ways highway=*  --wb omitmetadata=true file=&quot;d:&#92;spatialite_data&#92;usa_can.osm.pbf  Afte...'''
date = "2012-07-12T02:22:00Z"
lastmod = "2012-07-12T03:13:00Z"
weight = 14206
keywords = [ "windows", "data", "check", "osmosis" ]
aliases = [ "/questions/14206" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [incorrect data check](/questions/14206/incorrect-data-check)

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
<span id="post-14206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14206-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Yesterday I downloaded planet-latest.osm.pbf.</p>
<p>Today I tried to run:</p>
<pre><code>osmosis --rb file=&quot;c:\osm_data\planet-latest.osm.pbf&quot;  
--bp file=&quot;c:\osm_data\united_states.poly&quot;  --bp file=&quot;c:\osm_data\canada.poly&quot; 
--tf accept-ways highway=* 
--wb omitmetadata=true file=&quot;d:\spatialite_data\usa_can.osm.pbf</code></pre>
<p>After running for about 15 minutes I get:</p>
<pre><code>C:\Program Files (x86)\osmosis\bin&gt;osmosis --rb file=&quot;c:\osm_data\planet-latest.osm.pbf&quot;  --bp file=&quot;c:\osm_data\united_states.poly&quot;
c:\osm_data\canada.poly&quot; --tf accept-ways highway=* --wb omitmetadata=true file=&quot;d:\spatialite_data\usa_can.osm.pbf&quot;
Jul 11, 2012 6:47:50 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.40.1
Jul 11, 2012 6:47:50 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
Jul 11, 2012 6:47:50 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
Jul 11, 2012 6:47:50 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
java.util.zip.DataFormatException: incorrect data check   &lt;&lt;===================     
        at java.util.zip.Inflater.inflateBytes(Native Method)
        at java.util.zip.Inflater.inflate(Unknown Source)
        at java.util.zip.Inflater.inflate(Unknown Source)
        at crosby.binary.file.FileBlockPosition.parseData(FileBlockPosition.java:57)
        at crosby.binary.file.FileBlockHead.readContents(FileBlockHead.java:95)
        at crosby.binary.file.FileBlock.process(FileBlock.java:135)
        at crosby.binary.file.BlockInputStream.process(BlockInputStream.java:34)
        at crosby.binary.osmosis.OsmosisReader.run(OsmosisReader.java:37)
        at java.lang.Thread.run(Unknown Source)
Jul 11, 2012 7:02:57 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-rb failed
java.lang.Error: java.util.zip.DataFormatException: incorrect data check
        at crosby.binary.file.FileBlockPosition.parseData(FileBlockPosition.java:60)
        at crosby.binary.file.FileBlockHead.readContents(FileBlockHead.java:95)
        at crosby.binary.file.FileBlock.process(FileBlock.java:135)
        at crosby.binary.file.BlockInputStream.process(BlockInputStream.java:34)
        at crosby.binary.osmosis.OsmosisReader.run(OsmosisReader.java:37)
        at java.lang.Thread.run(Unknown Source)
Caused by: java.util.zip.DataFormatException: incorrect data check
        at java.util.zip.Inflater.inflateBytes(Native Method)
        at java.util.zip.Inflater.inflate(Unknown Source)
        at java.util.zip.Inflater.inflate(Unknown Source)
        at crosby.binary.file.FileBlockPosition.parseData(FileBlockPosition.java:57)
        ... 5 more
&#10;Jul 11, 2012 7:02:57 PM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
        at java.lang.reflect.Method.invoke(Unknown Source)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:329)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:239)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:409)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:352)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)
&#10;C:\Program Files (x86)\osmosis\bin&gt;</code></pre>
<p>What is causing this? Is there a work-around?</p>
<p>Regards, Jim</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-check" rel="tag" title="see questions tagged &#39;check&#39;">check</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '12, 02:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a91c10377b432d3352bd072df1aa4633?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="obrienj&#39;s gravatar image" />
<p><span>obrienj</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="obrienj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jul '12, 02:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-14206" class="comments-container">
&#10;</div>
<div id="comment-tools-14206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14206-form-container" class="comment-form-container">
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

<span id="14207"></span>

<div id="answer-container-14207" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14207-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like it's inside the crosby code (the pbf reader) at the point where it falls over. Perhaps it's incorrect data in planet-latest.osm.pbf (i.e. a download error)? You couldn't double-check the MD5, could you? There's an MD5 of a few-days-old planet <a href="http://planet.openstreetmap.org/">here</a>, but of course that may not be the one that you're downloading.</p>
<p>Another possibility, perhaps, may be Java running out of temporary storage, like in <a href="/questions/14085/osmosis-planetosm-to-postgresql-disk-space-caching">this question</a>.<br />
</p>
<p>Finally, it's not trying to write any files locally (to "Program Files (x86)") is it? Because if so, and you're on Windows Vista or 7, UAC may try and stop you. I seem to remember that osmosis ships with a batch file on Windows these days - you may want to have a look at that to see if you want any of the settings from it. Also see the "Win 7 64 bit" note at the bottom of <a href="https://wiki.openstreetmap.org/wiki/Osmosis#Windows_notes">this page</a>.</p>
<p>(all of this is, unfortunately, guesswork; I haven't run osmosis for ages and on Windows for even longer).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '12, 02:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-14207" class="comments-container">
<span id="14208"></span>
<div id="comment-14208" class="comment">
<div id="post-14208-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You were correct, I checked the md5 sum of the downloaded file and it didn't match that on the website you referenced.</p>
<p>So, I know the "rest of the story".</p>
<p>Thanks for reminding me about the md5 check.</p>
<p>Regards, Jim</p>
<p>P.S. I won't be downloading the planet file again, it took 12 hours!!</p>
</div>
<div id="comment-14208-info" class="comment-info">
<span class="comment-age">(12 Jul '12, 03:13)</span> <span class="comment-user userinfo">obrienj</span>
</div>
</div>
</div>
<div id="comment-tools-14207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14207-form-container" class="comment-form-container">
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

