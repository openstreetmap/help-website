+++
type = "question"
title = "Error loading the OSM File into the database."
description = '''I’ve been following the instructions found here. https://wiki.openstreetmap.org/wiki/Osmosis/PostGIS_Setup There have been some problems so I’ve had to grab updated versions of files, but when I try to import the iowa highway osm it gives me the this.  user@osgeolive:~/osmosis-0.31/bin$ ./osmosis —re...'''
date = "2011-04-08T06:29:00Z"
lastmod = "2011-04-08T09:11:00Z"
weight = 4331
keywords = [ "load", "osmosis", "file", "error" ]
aliases = [ "/questions/4331" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error loading the OSM File into the database.](/questions/4331/error-loading-the-osm-file-into-the-database)

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
<span id="post-4331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4331-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I’ve been following the instructions found here.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Osmosis/PostGIS_Setup">https://wiki.openstreetmap.org/wiki/Osmosis/PostGIS_Setup</a></p>
<p>There have been some problems so I’ve had to grab updated versions of files, but when I try to import the iowa highway osm it gives me the this.</p>
<pre><code> user@osgeolive:~/osmosis-0.31/bin$ ./osmosis —read-xml file=“/home/user/Downloa ds/iowa.osm.highway.bz2” —write-pgsql user=“osm” database=“osm” password=“osm”
 Apr 6, 2011 3:51:18 PM org.openstreetmap.osmosis.core.Osmosis run
 INFO: Osmosis Version 0.31
 Apr 6, 2011 3:51:20 PM org.openstreetmap.osmosis.core.Osmosis run
 INFO: Preparing pipeline.
 Apr 6, 2011 3:51:20 PM org.openstreetmap.osmosis.core.Osmosis run
 INFO: Launching pipeline execution.
 Apr 6, 2011 3:51:20 PM org.openstreetmap.osmosis.core.Osmosis run
 INFO: Pipeline executing, waiting for completion.
 Apr 6, 2011 3:51:20 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTask Manager waitForCompletion
 SEVERE: Thread for task 1-read-xml failed
 org.openstreetmap.osmosis.core.OsmosisRuntimeException: The database schema vers ion of 6 does not match the expected version of 4.
 at org.openstreetmap.osmosis.core.pgsql.common.SchemaVersionValidator.va lidateDBVersion(SchemaVersionValidator.java:82)
 at org.openstreetmap.osmosis.core.pgsql.common.SchemaVersionValidator.va lidateVersion(SchemaVersionValidator.java:52)
 at org.openstreetmap.osmosis.core.pgsql.v0_6.PostgreSqlWriter.initialize (PostgreSqlWriter.java:242)
 at org.openstreetmap.osmosis.core.pgsql.v0_6.PostgreSqlWriter.process(Po stgreSqlWriter.java:902)
 at org.openstreetmap.osmosis.core.xml.v0_6.impl.NodeElementProcessor.end (NodeElementProcessor.java:109)
 at org.openstreetmap.osmosis.core.xml.v0_6.impl.OsmHandler.endElement(Os mHandler.java:108)
 at com.sun.org.apache.xerces.internal.parsers.AbstractSAXParser.endEleme nt(AbstractSAXParser.java:604)
 at com.sun.org.apache.xerces.internal.parsers.AbstractXMLDocumentParser. emptyElement(AbstractXMLDocumentParser.java:183)
 at com.sun.org.apache.xerces.internal.impl.XMLDocumentFragmentScannerImp l.scanStartElement(XMLDocumentFragmentScannerImpl.java:1320)
 at com.sun.org.apache.xerces.internal.impl.XMLDocumentFragmentScannerImp l$FragmentContentDriver.next(XMLDocumentFragmentScannerImpl.java:2732)
 at com.sun.org.apache.xerces.internal.impl.XMLDocumentScannerImpl.next(X MLDocumentScannerImpl.java:625)
 at com.sun.org.apache.xerces.internal.impl.XMLDocumentFragmentScannerImp l.scanDocument(XMLDocumentFragmentScannerImpl.java:488)
 at com.sun.org.apache.xerces.internal.parsers.XML11Configuration.parse(X ML11Configuration.java:812)
 at com.sun.org.apache.xerces.internal.parsers.XML11Configuration.parse(X ML11Configuration.java:741)
 at com.sun.org.apache.xerces.internal.parsers.XMLParser.parse(XMLParser. java:123)
 at com.sun.org.apache.xerces.internal.parsers.AbstractSAXParser.parse(Ab stractSAXParser.java:1208)
 at com.sun.org.apache.xerces.internal.jaxp.SAXParserImpl$JAXPSAXParser.p arse(SAXParserImpl.java:525)
 at javax.xml.parsers.SAXParser.parse(SAXParser.java:392)
 at javax.xml.parsers.SAXParser.parse(SAXParser.java:195)
 at org.openstreetmap.osmosis.core.xml.v0_6.XmlReader.run(XmlReader.java: 108)
 at java.lang.Thread.run(Thread.java:636)
 Apr 6, 2011 3:51:20 PM org.openstreetmap.osmosis.core.Osmosis main
 SEVERE: Execution aborted.
 org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed .
 at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForComple tion(Pipeline.java:146)
 at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:85)
 at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:30)
 user@osgeolive:~/osmosis-0.31/bin$ The database schema vers ion of 6 does not match the expected version of 4.
 No command ‘The’ found, did you mean:
 Command ‘the’ from package ‘the’ (universe)
 The: command not found
 user@osgeolive:~/osmosis-0.31/bin$ ^C
 user@osgeolive:~/osmosis-0.31/bin$</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-load" rel="tag" title="see questions tagged &#39;load&#39;">load</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '11, 06:29</strong></p>
<img src="https://secure.gravatar.com/avatar/888db7df7c482556b5e3c601352f5d1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmuel&#39;s gravatar image" />
<p><span>jmuel</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmuel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '15, 19:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-4331" class="comments-container">
&#10;</div>
<div id="comment-tools-4331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4331-form-container" class="comment-form-container">
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

<span id="4336"></span>

<div id="answer-container-4336" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4336-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-4336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First this is a help forum, not a place for debugging specific installations. In future please use IRC, the forum or one of the mailing lists.</p>
<p>Second <strong>read</strong> the error message "SEVERE: Thread for task 1-read-xml failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: <strong>The database schema vers ion of 6 does not match the expected version of 4</strong>. at org.openstreetmap.osmosis.core.pgsql.common.SchemaVersionValidator.va lidateDBVersion(SchemaVersionValidator.java:82) at"</p>
<p>You look to be using a very old version of osmosis (IIRC 0.31 is about 2 years old) with an out-of-date simple Postgres database schema. The schema has changed significantly and must be kept in step with the relevant version of Osmosis (the schema DDL is usually in a sub-directory of any osmosis distribution). The --wp task checks that the currently supported schema matches a value in a table on the database, and this seems to be the root of the error message.</p>
<p>I would suggest that a) you upgrade to the current version of Osmosis (0.38), b) install hstore on your Postgres database, and c) replace the schema with the current version.</p>
<p>Carry out a few simple tests, before trying with a large file: can you create a copy of an OSM XML file, can you import and empty OSM XML file into a database etc. If you filter out the info lines from the Java exception its easier to get to the core of the problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '11, 09:11</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-4336" class="comments-container">
&#10;</div>
<div id="comment-tools-4336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4336-form-container" class="comment-form-container">
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

