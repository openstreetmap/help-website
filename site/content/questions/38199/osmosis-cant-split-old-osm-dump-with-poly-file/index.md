+++
type = "question"
title = "Osmosis - Can&#x27;t split old OSM dump with .poly-file"
description = '''Hey guys, Trying to split a planet dump from before the earthquake in Haiti, I am undergoing some trouble. I am using a .poly-file from Geofabrik and the planet dump is from the 6th January 2010. I am using the latest Osmosis version (0.43) with the following command: osmosis --read-xml file=&quot;planet...'''
date = "2014-10-31T22:55:00Z"
lastmod = "2014-11-09T16:42:00Z"
weight = 38199
keywords = [ "error", "planet_osm", "osmosis", "bounding-polygon" ]
aliases = [ "/questions/38199" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Osmosis - Can't split old OSM dump with .poly-file](/questions/38199/osmosis-cant-split-old-osm-dump-with-poly-file)

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
<span id="post-38199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38199-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys,</p>
<p>Trying to split a planet dump from before the earthquake in Haiti, I am undergoing some trouble. I am using a .poly-file from Geofabrik and the planet dump is from the 6th January 2010. I am using the latest Osmosis version (0.43) with the following command:</p>
<pre><code>osmosis --read-xml file=&quot;planet-100106.osm&quot; --bounding-polygon file=&quot;haiti-and-domrep.poly&quot; --write-xml file=&quot;haiti-100107.osm&quot; -v5</code></pre>
<p>Osmosis will start doing something for 5 minutes to 2 hours and then sooner or later give out the following Error. Do you have any ideas why this is happening? I am desperate!</p>
<pre><code>G:\&gt;OSM_CutHaiti.bat
&#10;G:\&gt;osmosis --read-xml file=&quot;planet-100106.osm&quot; --bounding-polygon file=&quot;haiti-a
nd-domrep.poly&quot; --write-xml file=&quot;haiti-100107.osm&quot; -v5
Oct 31, 2014 11:31:44 PM org.openstreetmap.osmosis.core.Osmosis run
INFORMATION: Osmosis Version 0.43.1
Oct 31, 2014 11:31:45 PM org.openstreetmap.osmosis.core.Osmosis run
INFORMATION: Preparing pipeline.
Oct 31, 2014 11:31:45 PM org.openstreetmap.osmosis.core.Osmosis run
INFORMATION: Launching pipeline execution.
Oct 31, 2014 11:31:45 PM org.openstreetmap.osmosis.core.Osmosis run
INFORMATION: Pipeline executing, waiting for completion.
Oct 31, 2014 11:34:49 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTa
skManager waitForCompletion
SCHWERWIEGEND: Thread for task 1-read-xml failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to read XML file
planet-100106.osm.
        at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:126)
        at java.lang.Thread.run(Unknown Source)
Caused by: java.io.IOException: Datenfehler (CRC-Pr³fung)
        at java.io.FileInputStream.readBytes(Native Method)
        at java.io.FileInputStream.read(Unknown Source)
        at org.apache.xerces.impl.XMLEntityManager$RewindableInputStream.read(Un
known Source)
        at org.apache.xerces.impl.io.UTF8Reader.read(Unknown Source)
        at org.apache.xerces.impl.XMLEntityScanner.load(Unknown Source)
        at org.apache.xerces.impl.XMLEntityScanner.scanLiteral(Unknown Source)
        at org.apache.xerces.impl.XMLScanner.scanAttributeValue(Unknown Source)
        at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanAttribute(U
nknown Source)
        at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanStartElemen
t(Unknown Source)
        at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl$FragmentContent
Dispatcher.dispatch(Unknown Source)
        at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanDocument(Un
known Source)
        at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source)
        at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source)
        at org.apache.xerces.parsers.XMLParser.parse(Unknown Source)
        at org.apache.xerces.parsers.AbstractSAXParser.parse(Unknown Source)
        at org.apache.xerces.jaxp.SAXParserImpl$JAXPSAXParser.parse(Unknown Sour
ce)
        at org.apache.xerces.jaxp.SAXParserImpl.parse(Unknown Source)
        at javax.xml.parsers.SAXParser.parse(Unknown Source)
        at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:111)
        ... 1 more
&#10;Oct 31, 2014 11:34:49 PM org.openstreetmap.osmosis.core.Osmosis main
SCHWERWIEGEND: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed
.
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForComple
tion(Pipeline.java:146)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
        at java.lang.reflect.Method.invoke(Unknown Source)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Laun
cher.java:329)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.jav
a:239)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(La
uncher.java:409)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:
352)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-bounding-polygon" rel="tag" title="see questions tagged &#39;bounding-polygon&#39;">bounding-polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '14, 22:55</strong></p>
<img src="https://secure.gravatar.com/avatar/999e9ededccde512b3cbd43683233d30?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kartenmalergidi&#39;s gravatar image" />
<p><span>kartenmalergidi</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kartenmalergidi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38199" class="comments-container">
&#10;</div>
<div id="comment-tools-38199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38199-form-container" class="comment-form-container">
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

<span id="38214"></span>

<div id="answer-container-38214" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38214-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-38214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kartenmalergidi has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As Frederik pointed out this is likely a disk error</p>
<p>Caused by: java.io.IOException: Datenfehler (CRC-Pr³fung)</p>
<p>I would suggest checking your logs etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '14, 08:36</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-38214" class="comments-container">
<span id="38406"></span>
<div id="comment-38406" class="comment">
<div id="post-38406-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hey Simon, thank you for the assitance. You were correct: one of my external Hard Disks was spoiled causing the mistake.</p>
</div>
<div id="comment-38406-info" class="comment-info">
<span class="comment-age">(09 Nov '14, 16:42)</span> <span class="comment-user userinfo">kartenmalergidi</span>
</div>
</div>
</div>
<div id="comment-tools-38214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38214-form-container" class="comment-form-container">
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

