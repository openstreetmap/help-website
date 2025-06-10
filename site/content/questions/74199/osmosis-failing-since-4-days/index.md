+++
type = "question"
title = "osmosis failing since 4 days"
description = '''Since 4 days the process seems to be failing ... it had been working fine since years Apr 14, 2020 8:00:04 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.46-14-ge344f05d-SNAPSHOT Apr 14, 2020 8:00:05 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. Apr 1...'''
date = "2020-04-15T06:37:00Z"
lastmod = "2020-04-26T17:43:00Z"
weight = 74199
keywords = [ "osmosis" ]
aliases = [ "/questions/74199" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [osmosis failing since 4 days](/questions/74199/osmosis-failing-since-4-days)

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
<span id="post-74199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74199-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Since 4 days the process seems to be failing ... it had been working fine since years</p>
<pre><code>Apr 14, 2020 8:00:04 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.46-14-ge344f05d-SNAPSHOT
Apr 14, 2020 8:00:05 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
Apr 14, 2020 8:00:05 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
Apr 14, 2020 8:00:05 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
Apr 14, 2020 8:21:33 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-replication-interval failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to parse xml file /tmp/change2988747640273014074.tmp.  publicId=(null), systemId=(null), lineNumber=1775, columnNumber=22.
        at org.openstreetmap.osmosis.xml.v0_6.XmlChangeReader.run(XmlChangeReader.java:100)
        at org.openstreetmap.osmosis.replication.v0_6.ReplicationDownloader.processChangeset(ReplicationDownloader.java:107)
        at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.processReplicationFile(BaseReplicationDownloader.java:133)
        at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.download(BaseReplicationDownloader.java:235)
        at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.runImpl(BaseReplicationDownloader.java:271)
        at org.openstreetmap.osmosis.replication.v0_6.BaseReplicationDownloader.run(BaseReplicationDownloader.java:350)
        at java.lang.Thread.run(Thread.java:748)
Caused by: org.xml.sax.SAXParseException; lineNumber: 1775; columnNumber: 22; Invalid byte 2 of 4-byte UTF-8 sequence.
        at org.apache.xerces.util.ErrorHandlerWrapper.createSAXParseException(Unknown Source)
        at org.apache.xerces.util.ErrorHandlerWrapper.fatalError(Unknown Source)
        at org.apache.xerces.impl.XMLErrorReporter.reportError(Unknown Source)
        at org.apache.xerces.impl.XMLErrorReporter.reportError(Unknown Source)
        at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl$FragmentContentDispatcher.dispatch(Unknown Source)
        at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanDocument(Unknown Source)
        at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source)
        at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source)
        at org.apache.xerces.parsers.XMLParser.parse(Unknown Source)
        at org.apache.xerces.parsers.AbstractSAXParser.parse(Unknown Source)
        at org.apache.xerces.jaxp.SAXParserImpl$JAXPSAXParser.parse(Unknown Source)
        at org.apache.xerces.jaxp.SAXParserImpl.parse(Unknown Source)
        at javax.xml.parsers.SAXParser.parse(SAXParser.java:195)
        at org.openstreetmap.osmosis.xml.v0_6.XmlChangeReader.run(XmlChangeReader.java:90)
        ... 6 more
Caused by: org.apache.xerces.impl.io.MalformedByteSequenceException: Invalid byte 2 of 4-byte UTF-8 sequence.
        at org.apache.xerces.impl.io.UTF8Reader.invalidByte(Unknown Source)
        at org.apache.xerces.impl.io.UTF8Reader.read(Unknown Source)
        at org.apache.xerces.impl.XMLEntityScanner.load(Unknown Source)
        at org.apache.xerces.impl.XMLEntityScanner.scanLiteral(Unknown Source)
        at org.apache.xerces.impl.XMLScanner.scanAttributeValue(Unknown Source)
        at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanAttribute(Unknown Source)
        at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanStartElement(Unknown Source)
        ... 16 more
&#10;Apr 14, 2020 8:21:33 PM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:330)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:415)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:356)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '20, 06:37</strong></p>
<img src="https://secure.gravatar.com/avatar/df8704d2a10bf36fc9c5b79301fbd118?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustusj&#39;s gravatar image" />
<p><span>augustusj</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustusj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '20, 07:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-74199" class="comments-container">
<span id="74200"></span>
<div id="comment-74200" class="comment">
<div id="post-74200-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The same here! Contact me if I could help with this somehow :)</p>
</div>
<div id="comment-74200-info" class="comment-info">
<span class="comment-age">(15 Apr '20, 07:28)</span> <span class="comment-user userinfo">jendrusk</span>
</div>
</div>
</div>
<div id="comment-tools-74199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74199-form-container" class="comment-form-container">
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

<span id="74201"></span>

<div id="answer-container-74201" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74201-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-74201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is an old bug in xerces.</p>
<p>It was fixed by this commit of osmosis: <a href="https://github.com/openstreetmap/osmosis/pull/51">https://github.com/openstreetmap/osmosis/pull/51</a></p>
<p>So update osmosis to <a href="https://github.com/openstreetmap/osmosis/releases/tag/0.47.4">https://github.com/openstreetmap/osmosis/releases/tag/0.47.4</a> (Version 0.47.4.).</p>
<p>And say thank you to <a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a> for fixing it ;)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '20, 08:07</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '20, 08:11</strong> </span></p>
</div>
</div>
<div id="comments-container-74201" class="comments-container">
<span id="74381"></span>
<div id="comment-74381" class="comment">
<div id="post-74381-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've made this the accepted answer - hope no-one minds!</p>
</div>
<div id="comment-74381-info" class="comment-info">
<span class="comment-age">(26 Apr '20, 17:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74201-form-container" class="comment-form-container">
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

