+++
type = "question"
title = "osmosis - invalid mysql schema?"
description = '''I downloaded the latest osmosis and I have the following MySQL database schema: http://91.239.67.150/db.sql. The problem lies in the fact that something this database is not compatible with my version of osmosis. With &quot;validateSchemaVersion = yes&quot; the program returns to me: root@vz32970:~/osm# osmos...'''
date = "2015-01-09T19:05:00Z"
lastmod = "2015-01-10T11:49:00Z"
weight = 40180
keywords = [ "osmosis" ]
aliases = [ "/questions/40180" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmosis - invalid mysql schema?](/questions/40180/osmosis-invalid-mysql-schema)

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
<span id="post-40180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40180-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I downloaded the latest osmosis and I have the following MySQL database schema: <a href="http://91.239.67.150/db.sql">http://91.239.67.150/db.sql</a>.</p>
<p>The problem lies in the fact that something this database is not compatible with my version of osmosis. With "validateSchemaVersion = yes" the program returns to me:</p>
<pre><code>root@vz32970:~/osm# osmosis --read-xml file=&quot;liechtenstein-latest.osm.bz2&quot; --write-apidb-0.6 host=&quot;localhost&quot; dbType=&quot;mysql&quot; database=&quot;liechtenstein&quot; user=&quot;root&quot; password=&quot;pass&quot; validateSchemaVersion=yes
Jan 09, 2015 5:08:36 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.40.1
Jan 09, 2015 5:08:36 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
Jan 09, 2015 5:08:36 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
Jan 09, 2015 5:08:36 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
Jan 09, 2015 5:08:37 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-xml failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Database version mismatch. The schema is missing migrations [20110925112722, 35, 36, 33, 34, 39, 37, 38, 20100516124737, 43, 42, 41, 40, 20100910084426, 26, 27, 28, 29, 30, 32, 31, 20111116184519, 20110322001319, 20101114011429, 20100513171259, 49, 48, 45, 44, 47, 46, 51, 52, 50], may need to upgrade schema or specify validateSchemaVersion=no.
    at org.openstreetmap.osmosis.apidb.v0_6.impl.SchemaVersionValidator.validateDBVersion(SchemaVersionValidator.java:119)
    at org.openstreetmap.osmosis.apidb.v0_6.impl.SchemaVersionValidator.validateVersion(SchemaVersionValidator.java:55)
    at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.initialize(ApidbWriter.java:323)
    at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.process(ApidbWriter.java:1080)
    at org.openstreetmap.osmosis.xml.v0_6.impl.NodeElementProcessor.end(NodeElementProcessor.java:118)
    at org.openstreetmap.osmosis.xml.v0_6.impl.OsmHandler.endElement(OsmHandler.java:107)
    at org.apache.xerces.parsers.AbstractSAXParser.endElement(Unknown Source)
    at org.apache.xerces.parsers.AbstractXMLDocumentParser.emptyElement(Unknown Source)
    at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanStartElement(Unknown Source)
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
    at java.lang.Thread.run(Thread.java:745)
&#10;Jan 09, 2015 5:08:37 PM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
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
    at org.codehaus.classworlds.Launcher.main(Launcher.java:31)</code></pre>
<p>In contrast, when I set "validateSchemaVersion = no", I get the error:</p>
<pre><code>root@vz32970:~/osm# osmosis --read-xml file=&quot;liechtenstein-latest.osm.bz2&quot; --write-apidb-0.6 host=&quot;localhost&quot; dbType=&quot;mysql&quot; database=&quot;liechtenstein&quot; user=&quot;root&quot; password=&quot;PASS&quot; validateSchemaVersion=no 
Jan 09, 2015 5:14:31 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.40.1
Jan 09, 2015 5:14:32 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
Jan 09, 2015 5:14:32 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
Jan 09, 2015 5:14:32 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
Jan 09, 2015 5:15:49 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-xml failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to load current nodes.
    at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.populateCurrentNodes(ApidbWriter.java:928)
    at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.populateCurrentTables(ApidbWriter.java:1029)
    at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.complete(ApidbWriter.java:1055)
    at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:110)
    at java.lang.Thread.run(Thread.java:745)
Caused by: com.mysql.jdbc.exceptions.jdbc4.MySQLIntegrityConstraintViolationException: Duplicate entry &#39;26032956&#39; for key &#39;PRIMARY&#39;
    at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
    at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:57)
    at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
    at java.lang.reflect.Constructor.newInstance(Constructor.java:526)
    at com.mysql.jdbc.Util.handleNewInstance(Util.java:411)
    at com.mysql.jdbc.Util.getInstance(Util.java:386)
    at com.mysql.jdbc.SQLError.createSQLException(SQLError.java:1040)
    at com.mysql.jdbc.MysqlIO.checkErrorPacket(MysqlIO.java:3597)
    at com.mysql.jdbc.MysqlIO.checkErrorPacket(MysqlIO.java:3529)
    at com.mysql.jdbc.MysqlIO.sendCommand(MysqlIO.java:1990)
    at com.mysql.jdbc.MysqlIO.sqlQueryDirect(MysqlIO.java:2151)
    at com.mysql.jdbc.ConnectionImpl.execSQL(ConnectionImpl.java:2625)
    at com.mysql.jdbc.PreparedStatement.executeInternal(PreparedStatement.java:2119)
    at com.mysql.jdbc.PreparedStatement.execute(PreparedStatement.java:1362)
    at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.populateCurrentNodes(ApidbWriter.java:925)
    ... 4 more
&#10;Jan 09, 2015 5:15:49 PM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
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
    at org.codehaus.classworlds.Launcher.main(Launcher.java:31)</code></pre>
<p>Load about 71.3 MB database Liechtenstein but the whole thing does not want to ... What am I doing wrong? Something is incorrect in the database?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '15, 19:05</strong></p>
<img src="https://secure.gravatar.com/avatar/874f428b539f501361c6a9947fe859f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rysiu&#39;s gravatar image" />
<p><span>Rysiu</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rysiu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40180" class="comments-container">
&#10;</div>
<div id="comment-tools-40180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40180-form-container" class="comment-form-container">
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

<span id="40188"></span>

<div id="answer-container-40188" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40188-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'll start by confessing I'm not an expert, but the references in the validate=yes error look to refer to <a href="http://git.openstreetmap.org/rails.git/tree/HEAD:/db/migrate">the scripts here</a>.</p>
<p>Having a quick look at the first mentioned, 20110925112722, and your SQL scripts, the line</p>
<pre><code>rename_column :current_way_nodes, :id, :way_id</code></pre>
<p>suggests to me that the current_way_nodes table should have a way_id field, and yours doesn't. This was just the first issue I found.</p>
<p>The error when validation is switched off suggests you are trying to violate a unique constraint - is there some data in the tables already? The id in the error suggests it is <a href="https://www.openstreetmap.org/node/26032956">this node</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jan '15, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jan '15, 10:33</strong> </span></p>
</div>
</div>
<div id="comments-container-40188" class="comments-container">
<span id="40189"></span>
<div id="comment-40189" class="comment">
<div id="post-40189-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I fixed it (the field in the database). Also analyzed the remaining differences in the database and most concerning, eg. The users table so this do not have a relationship with an error. The error persists, and I do not know what to do :/</p>
</div>
<div id="comment-40189-info" class="comment-info">
<span class="comment-age">(10 Jan '15, 11:49)</span> <span class="comment-user userinfo">Rysiu</span>
</div>
</div>
</div>
<div id="comment-tools-40188" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40188-form-container" class="comment-form-container">
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

