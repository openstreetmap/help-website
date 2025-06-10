+++
type = "question"
title = "osmosis - merged bugs?"
description = '''Why not work? osmium-tool-1.14.0 osmosis.bat --rx a.osm.pbf --rx b.osm.pbf --merge --wx merged.osm.pbf lut 20, 2023 6:38:19 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.48.3 lut 20, 2023 6:38:19 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. lut 20, ...'''
date = "2023-02-20T19:37:00Z"
lastmod = "2023-02-21T12:15:00Z"
weight = 86752
keywords = [ "osmium" ]
aliases = [ "/questions/86752" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmosis - merged bugs?](/questions/86752/osmosis-merged-bugs)

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
<span id="post-86752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86752-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Why not work?</p>
<p>osmium-tool-1.14.0</p>
<p>osmosis.bat --rx a.osm.pbf --rx b.osm.pbf --merge --wx merged.osm.pbf lut 20, 2023 6:38:19 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.48.3 lut 20, 2023 6:38:19 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. lut 20, 2023 6:38:19 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Launching pipeline execution. lut 20, 2023 6:38:19 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline executing, waiting for completion. lut 20, 2023 6:38:20 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion SEVERE: Thread for task 1-rx failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to unzip gz file a.osm.pbf. at org.openstreetmap.osmosis.xml.v0_6.impl.BaseXMLReader.unzipParse(BaseXMLReader.java:109) at org.openstreetmap.osmosis.xml.v0_6.impl.BaseXMLReader.handleXML(BaseXMLReader.java:84) at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:52) at java.base/java.lang.Thread.run(Thread.java:834) Caused by: java.util.zip.ZipException: Not in GZIP format at java.base/java.util.zip.GZIPInputStream.readHeader(GZIPInputStream.java:166) at java.base/java.util.zip.GZIPInputStream.&lt;init&gt;(GZIPInputStream.java:80) at java.base/java.util.zip.GZIPInputStream.&lt;init&gt;(GZIPInputStream.java:92) at org.openstreetmap.osmosis.xml.v0_6.impl.BaseXMLReader.unzipParse(BaseXMLReader.java:101) ... 3 more</p>
<p>lut 20, 2023 6:38:20 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion SEVERE: Thread for task 2-rx failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to unzip gz file b.osm.pbf. at org.openstreetmap.osmosis.xml.v0_6.impl.BaseXMLReader.unzipParse(BaseXMLReader.java:109) at org.openstreetmap.osmosis.xml.v0_6.impl.BaseXMLReader.handleXML(BaseXMLReader.java:84) at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:52) at java.base/java.lang.Thread.run(Thread.java:834) Caused by: java.util.zip.ZipException: Not in GZIP format at java.base/java.util.zip.GZIPInputStream.readHeader(GZIPInputStream.java:166) at java.base/java.util.zip.GZIPInputStream.&lt;init&gt;(GZIPInputStream.java:80) at java.base/java.util.zip.GZIPInputStream.&lt;init&gt;(GZIPInputStream.java:92) at org.openstreetmap.osmosis.xml.v0_6.impl.BaseXMLReader.unzipParse(BaseXMLReader.java:101) ... 3 more</p>
<p>lut 20, 2023 6:38:20 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion SEVERE: Thread for task 3-merge failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: An input error has occurred, aborting. at org.openstreetmap.osmosis.core.store.DataPostbox.checkForInputErrors(DataPostbox.java:174) at org.openstreetmap.osmosis.core.store.DataPostbox.consumeCentralQueue(DataPostbox.java:244) at org.openstreetmap.osmosis.core.store.DataPostbox.hasNext(DataPostbox.java:441) at org.openstreetmap.osmosis.set.v0_6.EntityMerger.nextOrNull(EntityMerger.java:290) at org.openstreetmap.osmosis.set.v0_6.EntityMerger.run(EntityMerger.java:126) at java.base/java.lang.Thread.run(Thread.java:834)</p>
<p>lut 20, 2023 6:38:20 PM org.openstreetmap.osmosis.core.Osmosis main SEVERE: Execution aborted. org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed. at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146) at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92) at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37) at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) at java.base/java.lang.reflect.Method.invoke(Method.java:566) at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:330) at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238) at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:415) at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:356) at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '23, 19:37</strong></p>
<img src="https://secure.gravatar.com/avatar/e8a4658f2ce25009c47822805215939d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zeofil&#39;s gravatar image" />
<p><span>Zeofil</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zeofil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86752" class="comments-container">
<span id="86763"></span>
<div id="comment-86763" class="comment">
<div id="post-86763-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>From the logs, it looks like the files you are trying to read are not in gzip format. Probably they got corrupted. Or maybe try specifying the compressionMethod option as explained in the wiki <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.48#--read-xml_(--rx)">https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.48#--read-xml_(--rx)</a></p>
</div>
<div id="comment-86763-info" class="comment-info">
<span class="comment-age">(21 Feb '23, 10:56)</span> <span class="comment-user userinfo">gabenarni</span>
</div>
</div>
</div>
<div id="comment-tools-86752" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86752-form-container" class="comment-form-container">
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

<span id="86765"></span>

<div id="answer-container-86765" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86765-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86765-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86765-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osmosis --rb file="name.osm.pbf" -rb file= .. --merge --merge --wb file="output.osm.pbf" - its work :) thanks</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '23, 12:15</strong></p>
<img src="https://secure.gravatar.com/avatar/e8a4658f2ce25009c47822805215939d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zeofil&#39;s gravatar image" />
<p><span>Zeofil</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zeofil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86765" class="comments-container">
&#10;</div>
<div id="comment-tools-86765" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86765-form-container" class="comment-form-container">
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

