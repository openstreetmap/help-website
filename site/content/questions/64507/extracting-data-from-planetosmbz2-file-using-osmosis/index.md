+++
type = "question"
title = "Extracting data from planet.osm.bz2 file using Osmosis ?"
description = '''Hi everybody, I am trying to extract only african roads data from a planet.osm.bz2 2013 file. I used Osmosis and, with the coordinates found on openstreetmap, entered : osmosis --read-xml file=&quot;planet.osm.bz2&quot; --bounding-box top=37.58 left=-18.11 bottom=-35.46 right=54.14 --write-xml file=&quot;africaroa...'''
date = "2018-07-03T15:05:00Z"
lastmod = "2018-08-03T15:18:00Z"
weight = 64507
keywords = [ "openstreetmap", "osmosis" ]
aliases = [ "/questions/64507" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting data from planet.osm.bz2 file using Osmosis ?](/questions/64507/extracting-data-from-planetosmbz2-file-using-osmosis)

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
<span id="post-64507-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64507-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64507-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everybody,</p>
<p>I am trying to extract only african roads data from a planet.osm.bz2 2013 file. I used Osmosis and, with the coordinates found on openstreetmap, entered :</p>
<p>osmosis --read-xml file="planet.osm.bz2" --bounding-box top=37.58 left=-18.11 bottom=-35.46 right=54.14 --write-xml file="africaroads.osm"</p>
<p>Here is what I get :</p>
<p>C:\Users\Users\Documents\osm test&gt;osmosis --read-xml file="planet.osm.bz2" --bou nding-box top=37.58 left=-18.11 bottom=-35.46 right=54.14 --write-xml file="afri caroads.osm" juil. 03, 2018 3:54:47 PM org.openstreetmap.osmosis.core.Osmosis run INFOS: Osmosis Version 0.46 juil. 03, 2018 3:54:47 PM org.openstreetmap.osmosis.core.Osmosis run INFOS: Preparing pipeline. juil. 03, 2018 3:54:47 PM org.openstreetmap.osmosis.core.Osmosis run INFOS: Launching pipeline execution. juil. 03, 2018 3:54:47 PM org.openstreetmap.osmosis.core.Osmosis run INFOS: Pipeline executing, waiting for completion. juil. 03, 2018 3:54:48 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveT askManager waitForCompletion GRAVE: Thread for task 1-read-xml failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to parse xml file planet.osm.bz2. publicId=(null), systemId=(null), lineNumber=3959, columnNumbe r=127. at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:100) at java.lang.Thread.run(Unknown Source) Caused by: org.xml.sax.SAXParseException; lineNumber: 3959; columnNumber: 127; X ML document structures must start and end within the same entity. at org.apache.xerces.util.ErrorHandlerWrapper.createSAXParseException(Un known Source) at org.apache.xerces.util.ErrorHandlerWrapper.fatalError(Unknown Source)</p>
<pre><code>    at org.apache.xerces.impl.XMLErrorReporter.reportError(Unknown Source)
    at org.apache.xerces.impl.XMLErrorReporter.reportError(Unknown Source)
    at org.apache.xerces.impl.XMLErrorReporter.reportError(Unknown Source)
    at org.apache.xerces.impl.XMLScanner.reportFatalError(Unknown Source)
    at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.endEntity(Unkno</code></pre>
<p>wn Source) at org.apache.xerces.impl.XMLDocumentScannerImpl.endEntity(Unknown Sourc e) at org.apache.xerces.impl.XMLEntityManager.endEntity(Unknown Source) at org.apache.xerces.impl.XMLEntityScanner.load(Unknown Source) at org.apache.xerces.impl.XMLEntityScanner.skipSpaces(Unknown Source) at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanAttribute(U nknown Source) at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanStartElemen t(Unknown Source) at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl$FragmentContent Dispatcher.dispatch(Unknown Source) at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanDocument(Un known Source) at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source) at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source) at org.apache.xerces.parsers.XMLParser.parse(Unknown Source) at org.apache.xerces.parsers.AbstractSAXParser.parse(Unknown Source) at org.apache.xerces.jaxp.SAXParserImpl$JAXPSAXParser.parse(Unknown Sour ce) at org.apache.xerces.jaxp.SAXParserImpl.parse(Unknown Source) at javax.xml.parsers.SAXParser.parse(Unknown Source) at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:90) ... 1 more</p>
<p>juil. 03, 2018 3:54:48 PM org.openstreetmap.osmosis.core.Osmosis main GRAVE: Execution aborted. org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed . at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForComple tion(Pipeline.java:146) at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92) at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37) at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source) at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source) at java.lang.reflect.Method.invoke(Unknown Source) at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Laun cher.java:330) at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.jav a:238) at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(La uncher.java:415) at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java: 356) at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</p>
<p>Do you have any idea how I can fix this ? thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '18, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/7bc1f6bf924207c7d04c9fd282e250a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Clementbat&#39;s gravatar image" />
<p><span>Clementbat</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Clementbat has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64507" class="comments-container">
<span id="64600"></span>
<div id="comment-64600" class="comment">
<div id="post-64600-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd actually start from an extract of Africa from e.g. <a href="http://download.geofabrik.de/africa.html">Geofabrik</a>.</p>
</div>
<div id="comment-64600-info" class="comment-info">
<span class="comment-age">(09 Jul '18, 11:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64507" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64507-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="65045"></span>

<div id="answer-container-65045" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65045-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>Given that osmosis is failing out of the gate, and that the error message seems to indicate a difficulty parsing the xml, I guess that the error has to do with the --read-xml portion. Try adding the compressionMethod option to the --read-xml statement. So for a .bz2 file it would be --read-xml -compressionMethod=bzip2</p>
<p>See if that helps, and good luck!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '18, 22:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0a1767df93ea1e4b0ee7d17b40f8645f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="egarnica&#39;s gravatar image" />
<p><span>egarnica</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="egarnica has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jul '18, 22:55</strong> </span></p>
</div>
</div>
<div id="comments-container-65045" class="comments-container">
&#10;</div>
<div id="comment-tools-65045" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65045-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65108"></span>

<div id="answer-container-65108" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65108-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These days I tend to use osmium-tool instead of osmosis. And I would recommend to use the pbf file instead of the xml one in any case.</p>
<p>A comparable commandline would thus look like this: osmium extract -b -18.11-35.46 54.14 37.58 planet.osm.pbf -o africaroads.pbf -v</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '18, 15:18</strong></p>
<img src="https://secure.gravatar.com/avatar/ed4b275dcccc85019201630e7cf0e3b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giggls&#39;s gravatar image" />
<p><span>giggls</span><br />
<span class="score" title="126 reputation points">126</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giggls has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-65108" class="comments-container">
&#10;</div>
<div id="comment-tools-65108" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65108-form-container" class="comment-form-container">
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

