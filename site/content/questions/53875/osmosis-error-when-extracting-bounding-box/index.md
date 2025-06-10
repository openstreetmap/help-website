+++
type = "question"
title = "OSMOSIS error when extracting bounding box"
description = '''Hello, I downloaded europe-latest.osm.pbf from geofabrik last night. I am using OSMOSIS 0.45 version and trying to extract an area (an extended version of Isle Of Man for test) from europe download using OSMOSIS with the following command osmosis --read-pbf file=europe-latest.osm.pbf --bounding-box ...'''
date = "2017-01-05T17:06:00Z"
lastmod = "2017-01-06T15:35:00Z"
weight = 53875
keywords = [ "osmosis" ]
aliases = [ "/questions/53875" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSMOSIS error when extracting bounding box](/questions/53875/osmosis-error-when-extracting-bounding-box)

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
<span id="post-53875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53875-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I downloaded europe-latest.osm.pbf from geofabrik last night. I am using OSMOSIS 0.45 version and trying to extract an area (an extended version of Isle Of Man for test) from europe download using OSMOSIS with the following command</p>
<pre><code>osmosis   --read-pbf file=europe-latest.osm.pbf   --bounding-box left=-4.85 top=54.45 bottom=54.025 right=-4.25 --write-pbf Test.osm.pbf omitmetadata=true</code></pre>
<p>get the following error after it runs for about 13 minutes:</p>
<pre><code>Jan 05, 2017 10:34:34 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.45
Jan 05, 2017 10:34:35 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
Jan 05, 2017 10:34:35 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
Jan 05, 2017 10:34:35 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
java.util.zip.DataFormatException: invalid distance too far back
        at java.util.zip.Inflater.inflateBytes(Native Method)
        at java.util.zip.Inflater.inflate(Unknown Source)
        at java.util.zip.Inflater.inflate(Unknown Source)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlockPosition.parseData(FileBlockPosition.java:57)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlockHead.readContents(FileBlockHead.java:95)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlock.process(FileBlock.java:135)
        at org.openstreetmap.osmosis.osmbinary.file.BlockInputStream.process(BlockInputStream.java:34)
        at crosby.binary.osmosis.OsmosisReader.run(OsmosisReader.java:45)
        at java.lang.Thread.run(Unknown Source)
Jan 05, 2017 10:47:18 AM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-pbf failed
java.lang.Error: java.util.zip.DataFormatException: invalid distance too far back
        at org.openstreetmap.osmosis.osmbinary.file.FileBlockPosition.parseData(FileBlockPosition.java:60)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlockHead.readContents(FileBlockHead.java:95)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlock.process(FileBlock.java:135)
        at org.openstreetmap.osmosis.osmbinary.file.BlockInputStream.process(BlockInputStream.java:34)
        at crosby.binary.osmosis.OsmosisReader.run(OsmosisReader.java:45)  
      at java.lang.Thread.run(Unknown Source)Caused by: java.util.zip.DataFormatException: invalid distance too far back
        at java.util.zip.Inflater.inflateBytes(Native Method)
        at java.util.zip.Inflater.inflate(Unknown Source)
        at java.util.zip.Inflater.inflate(Unknown Source)
        at org.openstreetmap.osmosis.osmbinary.file.FileBlockPosition.parseData(FileBlockPosition.java:57)
        ... 5 more
&#10;Jan 05, 2017 10:47:18 AM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
        at java.lang.reflect.Method.invoke(Unknown Source)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:330)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:415)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:356)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
<p>when I do the same using the europe download from august of 2016, it works just fine. Is there a newer version of OSMOSIS that I need to download?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '17, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/343237842fce1f7a82f69ebf7a92f6b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kcjailbirds&#39;s gravatar image" />
<p><span>kcjailbirds</span><br />
<span class="score" title="141 reputation points">141</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kcjailbirds has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jan '17, 20:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-53875" class="comments-container">
<span id="53887"></span>
<div id="comment-53887" class="comment">
<div id="post-53887-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also, working in a windows 7 64 bit environment and running java 1.8.0_101.</p>
</div>
<div id="comment-53887-info" class="comment-info">
<span class="comment-age">(05 Jan '17, 21:02)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
</div>
<div id="comment-tools-53875" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53875-form-container" class="comment-form-container">
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

<span id="53898"></span>

<div id="answer-container-53898" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53898-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think I fixed it. I am not sure why the error above has anything todo with the java heap size but I modified the OSMOSIS.bat file and added parameter to change the heap size that java uses to 1G and it works now.</p>
<p>SET EXEC="%JAVACMD%" -Xmx1024m -cp "%PLEXUS_CP%" -Dapp.home="%MYAPP_HOME%" -Dclassworlds.conf="%MYAPP_HOME%\config\plexus.conf" %MAINCLASS% %OSMOSIS_OPTIONS% %*</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '17, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/343237842fce1f7a82f69ebf7a92f6b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kcjailbirds&#39;s gravatar image" />
<p><span>kcjailbirds</span><br />
<span class="score" title="141 reputation points">141</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kcjailbirds has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53898" class="comments-container">
&#10;</div>
<div id="comment-tools-53898" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53898-form-container" class="comment-form-container">
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

