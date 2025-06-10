+++
type = "question"
title = "Unable to open file for writing. Importing updated"
description = '''&quot;Unable to open file for writing.&quot; Does anyone know where I can find out why an update will not apply Command-line that was being run was osmosis --read-replication-interval workingDirectory=/var/lib/mod_tile/.osmosis --simplify-change --write-xml-change /var/lib/mod_tile/changes.osc.gz Aug 21, 2019...'''
date = "2019-08-21T11:04:00Z"
lastmod = "2019-08-21T11:04:00Z"
weight = 70447
keywords = [ "openstreetmap", "open", "osmosis", "file", "writing" ]
aliases = [ "/questions/70447" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to open file for writing. Importing updated](/questions/70447/unable-to-open-file-for-writing-importing-updated)

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
<span id="post-70447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70447-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>"Unable to open file for writing."</p>
<p>Does anyone know where I can find out why an update will not apply</p>
<p>Command-line that was being run was</p>
<p><strong>osmosis --read-replication-interval workingDirectory=/var/lib/mod_tile/.osmosis --simplify-change --write-xml-change /var/lib/mod_tile/changes.osc.gz</strong></p>
<pre><code>Aug 21, 2019 9:40:12 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.46
Aug 21, 2019 9:40:12 AM org.java.plugin.registry.xml.ManifestParser &lt;init&gt;
INFO: got SAX parser factory - org.apache.xerces.jaxp.SAXParserFactoryImpl@1e397ed7
Aug 21, 2019 9:40:12 AM org.java.plugin.registry.xml.PluginRegistryImpl configure
INFO: configured, stopOnError=false, isValidating=true
Aug 21, 2019 9:40:12 AM org.java.plugin.registry.xml.PluginRegistryImpl register
INFO: plug-in and fragment descriptors registered - 1
Aug 21, 2019 9:40:12 AM org.java.plugin.standard.StandardPluginManager activatePlugin
INFO: plug-in started - org.openstreetmap.osmosis.core.plugin.Core@0.46.0 (active/total: 1 of 1)
Aug 21, 2019 9:40:12 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
Aug 21, 2019 9:40:12 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
Aug 21, 2019 9:40:12 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
Aug 21, 2019 9:43:41 AM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-replication-interval failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to open file for writing.
    at org.openstreetmap.osmosis.xml.common.BaseXmlWriter.initialize(BaseXmlWriter.java:161)
    at org.openstreetmap.osmosis.xml.v0_6.XmlChangeWriter.process(XmlChangeWriter.java:56)
    at org.openstreetmap.osmosis.set.v0_6.impl.ChangeSimplifierImpl.flushCurrentChanges(ChangeSimplifierImpl.java:60)
    at org.openstreetmap.osmosis.set.v0_6.impl.ChangeSimplifierImpl.process(ChangeSimplifierImpl.java:88)
    at org.openstreetmap.osmosis.core.sort.v0_6.SortedHistoryChangePipeValidator.process(SortedHistoryChangePipeValidator.java:71)
    at org.openstreetmap.osmosis.set.v0_6.ChangeSimplifier.process(ChangeSimplifier.java:50)
    at org.openstreetmap.osmosis.core.sort.v0_6.ChangeSorter.complete(ChangeSorter.java:69)
    at org.openstreetmap.osmosis.replication.v0_6.ReplicationDownloader.processComplete(ReplicationDownloader.java:116)
    at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.runImpl(BaseReplicationDownloader.java:280)
    at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.run(BaseReplicationDownloader.java:350)
    at java.base/java.lang.Thread.run(Thread.java:834)
Caused by: java.io.FileNotFoundException: /var/lib/mod_tile/changes.osc.gz (Permission denied)
    at java.base/java.io.FileOutputStream.open0(Native Method)
    at java.base/java.io.FileOutputStream.open(FileOutputStream.java:298)
    at java.base/java.io.FileOutputStream.&lt;init&gt;(FileOutputStream.java:237)
    at java.base/java.io.FileOutputStream.&lt;init&gt;(FileOutputStream.java:187)
    at org.openstreetmap.osmosis.xml.common.BaseXmlWriter.initialize(BaseXmlWriter.java:148)
    ... 10 more
&#10;Aug 21, 2019 9:43:41 AM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
    at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
    at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
    at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
    at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
    at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.base/java.lang.reflect.Method.invoke(Method.java:566)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:330)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238)
    at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:415)
    at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:356)
    at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-open" rel="tag" title="see questions tagged &#39;open&#39;">open</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span> <span class="post-tag tag-link-writing" rel="tag" title="see questions tagged &#39;writing&#39;">writing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Aug '19, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/38e6d558e7e337c63ce2551c30287e3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karl_G&#39;s gravatar image" />
<p><span>Karl_G</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karl_G has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70447" class="comments-container">
&#10;</div>
<div id="comment-tools-70447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70447-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

