+++
type = "question"
title = "R-osmar: osmosis not reading osm.pbf"
description = '''Hi there,  I am using osmar to work with open streetmap data in R. I tried to import a small area (25km²) from the german os.pbf (2.7 GB). Yet this failed due to osmosis not parsing the osm file. System: Ubuntu 15.04, i686 GNU/Linux, 4 Cores, 8GB Ram R: platform i686-pc-linux-gnu  arch i686  os linu...'''
date = "2016-03-18T12:26:00Z"
lastmod = "2016-03-18T13:27:00Z"
weight = 48729
keywords = [ "osmar", "r", "osmosis" ]
aliases = [ "/questions/48729" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [R-osmar: osmosis not reading osm.pbf](/questions/48729/r-osmar-osmosis-not-reading-osmpbf)

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
<span id="post-48729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48729-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I am using osmar to work with open streetmap data in R. I tried to import a small area (25km²) from the german os.pbf (2.7 GB). Yet this failed due to osmosis not parsing the osm file.</p>
<p>System: Ubuntu 15.04, i686 GNU/Linux, 4 Cores, 8GB Ram</p>
<p>R: platform i686-pc-linux-gnu<br />
arch i686<br />
os linux-gnu<br />
system i686, linux-gnu<br />
status<br />
major 3<br />
minor 1.2<br />
year 2014<br />
month 10<br />
day 31<br />
svn rev 66913<br />
language R<br />
version.string R version 3.1.2 (2014-10-31) nickname Pumpkin Helmet</p>
<p>R-Script:</p>
<pre><code>require (osmar)
&#10;setwd (&quot;~/data/&quot;)
&#10;### Datasource
src &lt;- osmsource_osmosis(&quot;/home/administrator/data/pgsql/osm_germany/germany-latest.osm.pbf&quot;)
&#10;### BBox
bb_sol_leipz &lt;- center_bbox(12.359383, 51.403859,  width = 5000, height = 5000)
&#10;sol_leipz &lt;- get_osm(bb_sol_leipz, source = src)</code></pre>
<p>Error Report:</p>
<pre><code>Mrz 18, 2016 12:19:23 PM org.openstreetmap.osmosis.core.Osmosis run
INFORMATION: Osmosis Version 0.43.1
Mrz 18, 2016 12:19:23 PM org.openstreetmap.osmosis.core.Osmosis run
INFORMATION: Preparing pipeline.
Mrz 18, 2016 12:19:23 PM org.openstreetmap.osmosis.core.Osmosis run
INFORMATION: Launching pipeline execution.
Mrz 18, 2016 12:19:23 PM org.openstreetmap.osmosis.core.Osmosis run
INFORMATION: Pipeline executing, waiting for completion.
Mrz 18, 2016 12:19:23 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SCHWERWIEGEND: Thread for task 1-read-xml failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to parse xml file /home/administrator/data/pgsql/osm_germany/germany-latest.osm.pbf.  publicId=(null), systemId=(null), lineNumber=1, columnNumber=1.
    at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:116)
    at java.lang.Thread.run(Thread.java:745)
Caused by: org.xml.sax.SAXParseException: Content is not allowed in prolog.
    at org.apache.xerces.util.ErrorHandlerWrapper.createSAXParseException(Unknown Source)
    at org.apache.xerces.util.ErrorHandlerWrapper.fatalError(Unknown Source)
    at org.apache.xerces.impl.XMLErrorReporter.reportError(Unknown Source)
    at org.apache.xerces.impl.XMLErrorReporter.reportError(Unknown Source)
    at org.apache.xerces.impl.XMLErrorReporter.reportError(Unknown Source)
    at org.apache.xerces.impl.XMLScanner.reportFatalError(Unknown Source)
    at org.apache.xerces.impl.XMLDocumentScannerImpl$PrologDispatcher.dispatch(Unknown Source)
    at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanDocument(Unknown Source)
    at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source)
    at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source)
    at org.apache.xerces.parsers.XMLParser.parse(Unknown Source)
    at org.apache.xerces.parsers.AbstractSAXParser.parse(Unknown Source)
    at org.apache.xerces.jaxp.SAXParserImpl$JAXPSAXParser.parse(Unknown Source)
    at org.apache.xerces.jaxp.SAXParserImpl.parse(Unknown Source)
    at javax.xml.parsers.SAXParser.parse(SAXParser.java:189)
    at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:111)
    ... 1 more
&#10;Mrz 18, 2016 12:19:23 PM org.openstreetmap.osmosis.core.Osmosis main
SCHWERWIEGEND: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
    at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
    at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
    at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke(Method.java:606)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:328)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238)
    at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:408)
    at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:351)
    at org.codehaus.classworlds.Launcher.main(Launcher.java:31)
&#10;Fehler in file(con, &quot;r&quot;) : kann Verbindung nicht öffnen
Zusätzlich: Warnmeldung:
In file(con, &quot;r&quot;) :
  kann Datei &#39;/tmp/RtmpLD8AMb/file5f1170f48b12&#39; nicht öffnen: Datei oder Verzeichnis nicht gefunden</code></pre>
<p>Thanks for your help,</p>
<p>Gunnar</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmar" rel="tag" title="see questions tagged &#39;osmar&#39;">osmar</span> <span class="post-tag tag-link-r" rel="tag" title="see questions tagged &#39;r&#39;">r</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Mar '16, 12:26</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd169e59e1c133ddc655c921f83c73e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GunnarOeh&#39;s gravatar image" />
<p><span>GunnarOeh</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GunnarOeh has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-48729" class="comments-container">
<span id="48730"></span>
<div id="comment-48730" class="comment">
<div id="post-48730-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just checking, but does the MD5sum of the germany-latest file match?</p>
</div>
<div id="comment-48730-info" class="comment-info">
<span class="comment-age">(18 Mar '16, 12:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48731"></span>
<div id="comment-48731" class="comment">
<div id="post-48731-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi, thanks for the hint:</p>
<p>md5sum -c data/pgsql/osm_germany/germany-latest.osm.pbf</p>
<p>md5sum: data/pgsql/osm_germany/germany-latest.osm.pbf: keine korrekt formatierte MD5‐Prüfsummenzeile gefunden</p>
<p>(no correct md5sum found)</p>
</div>
<div id="comment-48731-info" class="comment-info">
<span class="comment-age">(18 Mar '16, 12:34)</span> <span class="comment-user userinfo">GunnarOeh</span>
</div>
</div>
<span id="48733"></span>
<div id="comment-48733" class="comment">
<div id="post-48733-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Try without the -c, and manually compare the resulting checksum with the .osm.pbf.md5 file on the download site.</p>
</div>
<div id="comment-48733-info" class="comment-info">
<span class="comment-age">(18 Mar '16, 13:22)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48729" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48729-form-container" class="comment-form-container">
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

<span id="48734"></span>

<div id="answer-container-48734" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48734-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The error message</p>
<pre><code>org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to parse xml file</code></pre>
<p>tells us that it is trying to parse the file as an XML file but it is a PBF file. Download the .osm.bz2 file and try with that, or fix Osmar to use the --read-pbf flag to Osmosis instead of --read-xml.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '16, 13:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-48734" class="comments-container">
&#10;</div>
<div id="comment-tools-48734" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48734-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48732"></span>

<div id="answer-container-48732" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48732-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"Unable to parse xml file" means that osmosis can open OK but can't make sense of it, which usually means a partial download (as confirmed in the comment above).</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '16, 13:01</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> wikified <strong>18 Mar '16, 13:01</strong> </span></p>
</div>
</div>
<div id="comments-container-48732" class="comments-container">
&#10;</div>
<div id="comment-tools-48732" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48732-form-container" class="comment-form-container">
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

