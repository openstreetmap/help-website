+++
type = "question"
title = "Unable to write osm data into database"
description = '''We are using PostgreSQL (with postgis)! The below are the extensions I added to the database CREATE EXTENSION hstore; osmosis/script/pgsnapshot_schema_0.6.sql osmosis/script/pgsnapshot_schema_0.6_action.sql pgsnapshot_schema_0.6_linestring.sql  When I execute the below command, osmosis --read-xml fi...'''
date = "2013-07-31T14:08:00Z"
lastmod = "2013-08-01T09:28:00Z"
weight = 24766
keywords = [ "postgresql", "osmosis", "postgis" ]
aliases = [ "/questions/24766" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to write osm data into database](/questions/24766/unable-to-write-osm-data-into-database)

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
<span id="post-24766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24766-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We are using PostgreSQL (with postgis)! The below are the extensions I added to the database</p>
<pre><code>CREATE EXTENSION hstore;
osmosis/script/pgsnapshot_schema_0.6.sql
osmosis/script/pgsnapshot_schema_0.6_action.sql
pgsnapshot_schema_0.6_linestring.sql</code></pre>
<p>When I execute the below command,</p>
<pre><code>osmosis --read-xml file=&quot;map.osm&quot; --write-pgsql host=&quot;localhost:5432&quot; database=&quot;mymap&quot; user=&quot;postgres&quot; password=&quot;1234&quot;</code></pre>
<p>I am getting this error</p>
<pre><code>Jul 31, 2013 2:44:44 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.40.1
Jul 31, 2013 2:44:44 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
Jul 31, 2013 2:44:44 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
Jul 31, 2013 2:44:44 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
log4j:WARN No appenders could be found for logger (org.springframework.jdbc.datasource.DataSourceUtils).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
Jul 31, 2013 2:44:45 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-xml failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Cannot begin reading in Add stage, must call complete first.
    at org.openstreetmap.osmosis.core.store.RandomAccessObjectStore.initializeReadingStage(RandomAccessObjectStore.java:156)
    at org.openstreetmap.osmosis.core.store.RandomAccessObjectStore.createReader(RandomAccessObjectStore.java:181)
    at org.openstreetmap.osmosis.core.store.IndexStore.createReader(IndexStore.java:151)
    at org.openstreetmap.osmosis.core.store.IndexedObjectStore.createReader(IndexedObjectStore.java:96)
    at org.openstreetmap.osmosis.pgsnapshot.common.CompactPersistentNodeLocationStore.getNodeLocation(CompactPersistentNodeLocationStore.java:50)
    at org.openstreetmap.osmosis.pgsnapshot.v0_6.impl.WayGeometryBuilder.createWayLinestring(WayGeometryBuilder.java:204)
    at org.openstreetmap.osmosis.pgsnapshot.v0_6.impl.CopyFilesetBuilder.process(CopyFilesetBuilder.java:190)
    at org.openstreetmap.osmosis.core.container.v0_6.WayContainer.process(WayContainer.java:60)
    at org.openstreetmap.osmosis.pgsnapshot.v0_6.impl.CopyFilesetBuilder.process(CopyFilesetBuilder.java:115)
    at org.openstreetmap.osmosis.pgsnapshot.v0_6.PostgreSqlCopyWriter.process(PostgreSqlCopyWriter.java:95)
    at org.openstreetmap.osmosis.xml.v0_6.impl.WayElementProcessor.end(WayElementProcessor.java:117)
    at org.openstreetmap.osmosis.xml.v0_6.impl.OsmHandler.endElement(OsmHandler.java:107)
    at org.apache.xerces.parsers.AbstractSAXParser.endElement(Unknown Source)
    at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanEndElement(Unknown Source)
    at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl$FragmentContentDispatcher.dispatch(Unknown Source)
    at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanDocument(Unknown Source)
    at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source)
    at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source)
    at org.apache.xerces.parsers.XMLParser.parse(Unknown Source)
    at org.apache.xerces.parsers.AbstractSAXParser.parse(Unknown Source)
    at org.apache.xerces.jaxp.SAXParserImpl$JAXPSAXParser.parse(Unknown Source)
    at org.apache.xerces.jaxp.SAXParserImpl.parse(Unknown Source)
    at javax.xml.parsers.SAXParser.parse(SAXParser.java:189)
    at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:108)
    at java.lang.Thread.run(Thread.java:722)
&#10;Jul 31, 2013 2:44:45 PM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
    at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
    at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
    at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke(Method.java:601)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:328)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238)
    at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:408)
    at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:351)
    at org.codehaus.classworlds.Launcher.main(Launcher.java:31)</code></pre>
<p>Can anyone let me know how to fix it?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '13, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/406204185bd4c7e587eb8206395da4bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iamlol&#39;s gravatar image" />
<p><span>iamlol</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iamlol has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jul '13, 19:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span></p>
</div>
</div>
<div id="comments-container-24766" class="comments-container">
&#10;</div>
<div id="comment-tools-24766" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24766-form-container" class="comment-form-container">
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

<span id="24772"></span>

<div id="answer-container-24772" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24772-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like the problem is with reading the XML file and is unrelated to PostgreSQL. What version of osmosis do you have, and does the <code>--fast-read-xml</code> command work?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '13, 23:16</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-24772" class="comments-container">
<span id="24782"></span>
<div id="comment-24782" class="comment">
<div id="post-24782-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Its not working.. I am using Latest stable version</p>
</div>
<div id="comment-24782-info" class="comment-info">
<span class="comment-age">(01 Aug '13, 09:28)</span> <span class="comment-user userinfo">iamlol</span>
</div>
</div>
</div>
<div id="comment-tools-24772" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24772-form-container" class="comment-form-container">
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

