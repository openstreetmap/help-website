+++
type = "question"
title = "Extract road network data from niedersachsen-latest.osm.pbf"
description = '''Hello, I want to extract the road network data (coodinates of street and street name) from niedersachsen-latest.osm.pbf. I first tried to convert the file into .sm format using Osmosis. I installed Osmosis on windows xp. I tried to convert niedersachsen-latest.osm.pbf to niedersachsen.osm usingthe c...'''
date = "2013-03-26T11:11:00Z"
lastmod = "2013-03-26T12:23:00Z"
weight = 20982
keywords = [ "routes", "extract", "osm", "coordinates", "osmosis" ]
aliases = [ "/questions/20982" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Extract road network data from niedersachsen-latest.osm.pbf](/questions/20982/extract-road-network-data-from-niedersachsen-latestosmpbf)

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
<span id="post-20982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20982-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I want to extract the road network data (coodinates of street and street name) from niedersachsen-latest.osm.pbf.</p>
<p>I first tried to convert the file into .sm format using Osmosis. I installed Osmosis on windows xp. I tried to convert niedersachsen-latest.osm.pbf to niedersachsen.osm usingthe command: osmosis --read-xml file=niedersachsen-latest.osm.pbf --write-xml file=niedersachsen.osm But I am getting error:</p>
<p>C:\Programme\osmosis-latest\bin&gt;osmosis --read-xml file=niedersachsen-latest.osm .pbf --write-xml file=niedersachsen.osm 26.03.2013 12:07:22 org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.42 26.03.2013 12:07:22 org.java.plugin.registry.xml.ManifestParser &lt;init&gt; INFO: got SAX parser factory - org.apache.xerces.jaxp.SAXParserFactoryImpl@1a8c4 e7 26.03.2013 12:07:22 org.java.plugin.registry.xml.PluginRegistryImpl configure INFO: configured, stopOnError=false, isValidating=true 26.03.2013 12:07:22 org.java.plugin.registry.xml.PluginRegistryImpl register INFO: plug-in and fragment descriptors registered - 1 26.03.2013 12:07:22 org.java.plugin.standard.StandardPluginManager activatePlugi n INFO: plug-in started - org.openstreetmap.osmosis.core.plugin.Core@0.42.0 26.03.2013 12:07:22 org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. 26.03.2013 12:07:22 org.openstreetmap.osmosis.core.Osmosis run INFO: Launching pipeline execution. 26.03.2013 12:07:22 org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline executing, waiting for completion. 26.03.2013 12:07:22 org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskMan ager waitForCompletion SCHWERWIEGEND: Thread for task 1-read-xml failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to parse xml file niedersachsen-latest.osm.pbf. publicId=(null), systemId=(null), lineNumber=1, columnNumber=1. at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:116) at java.lang.Thread.run(Unknown Source) Caused by: org.xml.sax.SAXParseException: Content is not allowed in prolog. at org.apache.xerces.util.ErrorHandlerWrapper.createSAXParseException(Un known Source) at org.apache.xerces.util.ErrorHandlerWrapper.fatalError(Unknown Source)</p>
<pre><code>    at org.apache.xerces.impl.XMLErrorReporter.reportError(Unknown Source)
    at org.apache.xerces.impl.XMLErrorReporter.reportError(Unknown Source)
    at org.apache.xerces.impl.XMLErrorReporter.reportError(Unknown Source)
    at org.apache.xerces.impl.XMLScanner.reportFatalError(Unknown Source)
    at org.apache.xerces.impl.XMLDocumentScannerImpl$PrologDispatcher.dispat</code></pre>
<p>ch(Unknown Source) at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanDocument(Un known Source) at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source) at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source) at org.apache.xerces.parsers.XMLParser.parse(Unknown Source) at org.apache.xerces.parsers.AbstractSAXParser.parse(Unknown Source) at org.apache.xerces.jaxp.SAXParserImpl$JAXPSAXParser.parse(Unknown Sour ce) at org.apache.xerces.jaxp.SAXParserImpl.parse(Unknown Source) at javax.xml.parsers.SAXParser.parse(Unknown Source) at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:111) ... 1 more 26.03.2013 12:07:22 org.openstreetmap.osmosis.core.Osmosis main SCHWERWIEGEND: Execution aborted. org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed . at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForComple tion(Pipeline.java:146) at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92) at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37) at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source) at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source) at java.lang.reflect.Method.invoke(Unknown Source) at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Laun cher.java:329) at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.jav a:239) at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(La uncher.java:409) at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java: 352) at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</p>
<p>After converting it into .osm file I want to extract the road network data from it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routes" rel="tag" title="see questions tagged &#39;routes&#39;">routes</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Mar '13, 11:11</strong></p>
<img src="https://secure.gravatar.com/avatar/f5d31b13d0fced1a8297e7d9e9385a53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tfarooqi&#39;s gravatar image" />
<p><span>tfarooqi</span><br />
<span class="score" title="30 reputation points">30</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tfarooqi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20982" class="comments-container">
&#10;</div>
<div id="comment-tools-20982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20982-form-container" class="comment-form-container">
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

<span id="20984"></span>

<div id="answer-container-20984" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20984-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tfarooqi has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think that you will need to use "read-pbf" to read a PBF file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Mar '13, 11:17</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-20984" class="comments-container">
<span id="20987"></span>
<div id="comment-20987" class="comment">
<div id="post-20987-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Its working, thanks a lot. Can you suggest the command to extract the start and end coordinates of a link/Street alon with street's name?</p>
</div>
<div id="comment-20987-info" class="comment-info">
<span class="comment-age">(26 Mar '13, 11:44)</span> <span class="comment-user userinfo">tfarooqi</span>
</div>
</div>
<span id="20988"></span>
<div id="comment-20988" class="comment">
<div id="post-20988-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You're probably better off asking a separate question with a few more details of what you're trying to do. The answer to <a href="/questions/19213/osm-xml-into-graph">this question</a> my help (although that's essentially doing the reverse of what you're attempting).</p>
</div>
<div id="comment-20988-info" class="comment-info">
<span class="comment-age">(26 Mar '13, 11:53)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="20989"></span>
<div id="comment-20989" class="comment">
<div id="post-20989-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am using this querry to extract road network used by cars: osmosis --read-xml niedersachsen.osm --tf accept-ways highway=* --tf reject-ways highway=pedestrian,footway,steps,cycleway,bridleway --tf reject-relations --used-node --write-xml niedersachsen_roadnetwork.osm</p>
<p>But still I need to find the start and end coordinates of the street and street name, Any suggestions?</p>
</div>
<div id="comment-20989-info" class="comment-info">
<span class="comment-age">(26 Mar '13, 11:58)</span> <span class="comment-user userinfo">tfarooqi</span>
</div>
</div>
<span id="20992"></span>
<div id="comment-20992" class="comment">
<div id="post-20992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have raised it as a seperate question: <a href="/questions/20990/to-find-the-start-and-end-coordinates-of-the-street-and-street-name-using-osmosis">https://help.openstreetmap.org/questions/20990/to-find-the-start-and-end-coordinates-of-the-street-and-street-name-using-osmosis</a></p>
</div>
<div id="comment-20992-info" class="comment-info">
<span class="comment-age">(26 Mar '13, 12:23)</span> <span class="comment-user userinfo">tfarooqi</span>
</div>
</div>
</div>
<div id="comment-tools-20984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20984-form-container" class="comment-form-container">
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

