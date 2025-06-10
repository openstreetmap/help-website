+++
type = "question"
title = "Populate a MySQL database - Thread for task 1-read-xml failed"
description = '''I am trying to export an OSM file to a MySQL database. The syntax am am using is: osmosis --read-xml file=&quot;d:/geo/maniu.osm&quot; --write-apidb populateCurrentTables=yes dbType=&quot;mysql&quot; host=&quot;localhost&quot; database=&quot;geo&quot; user=&quot;root&quot;  I get this error:  D:&#92;Geo&#92;osmosis&#92;bin&amp;gt;osmosis --read-xml file=&quot;d:/geo/ma...'''
date = "2012-07-04T20:39:00Z"
lastmod = "2018-12-22T22:50:00Z"
weight = 13988
keywords = [ "mysql" ]
aliases = [ "/questions/13988" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Populate a MySQL database - Thread for task 1-read-xml failed](/questions/13988/populate-a-mysql-database-thread-for-task-1-read-xml-failed)

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
<span id="post-13988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13988-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to export an OSM file to a MySQL database. The syntax am am using is:</p>
<p><strong>osmosis --read-xml file="d:/geo/maniu.osm" --write-apidb populateCurrentTables=yes dbType="mysql" host="localhost" database="geo" user="root"</strong></p>
<p>I get this error:</p>
<p>D:\Geo\osmosis\bin&gt;osmosis --read-xml file="d:/geo/maniu.osm" --write-apidb popu lateCurrentTables=yes dbType="mysql" host="localhost" database="geo" user="root" 04.07.2012 22:32:29 org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.40.1 04.07.2012 22:32:29 org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. 04.07.2012 22:32:29 org.openstreetmap.osmosis.core.Osmosis run INFO: Launching pipeline execution. 04.07.2012 22:32:29 org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline executing, waiting for completion. 04.07.2012 22:32:29 org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskMan ager waitForCompletion SEVERE: Thread for task 1-read-xml failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to create results et. at org.openstreetmap.osmosis.apidb.common.DatabaseContext.executeQuery(D atabaseContext.java:429) at org.openstreetmap.osmosis.apidb.v0_6.impl.SchemaVersionValidator.vali dateDBVersion(SchemaVersionValidator.java:82) at org.openstreetmap.osmosis.apidb.v0_6.impl.SchemaVersionValidator.vali dateVersion(SchemaVersionValidator.java:55) at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.initialize(ApidbWrit er.java:323) at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.process(ApidbWriter. java:1080) at org.openstreetmap.osmosis.xml.v0_6.impl.NodeElementProcessor.end(Node ElementProcessor.java:118) at org.openstreetmap.osmosis.xml.v0_6.impl.OsmHandler.endElement(OsmHand ler.java:107) at org.apache.xerces.parsers.AbstractSAXParser.endElement(Unknown Source ) at org.apache.xerces.parsers.AbstractXMLDocumentParser.emptyElement(Unkn own Source) at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanStartElemen t(Unknown Source) at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl$FragmentContent Dispatcher.dispatch(Unknown Source) at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanDocument(Un known Source) at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source) at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source) at org.apache.xerces.parsers.XMLParser.parse(Unknown Source) at org.apache.xerces.parsers.AbstractSAXParser.parse(Unknown Source) at org.apache.xerces.jaxp.SAXParserImpl$JAXPSAXParser.parse(Unknown Sour ce) at org.apache.xerces.jaxp.SAXParserImpl.parse(Unknown Source) at javax.xml.parsers.SAXParser.parse(Unknown Source) at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:108) at java.lang.Thread.run(Unknown Source) Caused by: com.mysql.jdbc.exceptions.jdbc4.MySQLSyntaxErrorException: Table 'geo .schema_migrations' doesn't exist at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method) at sun.reflect.NativeConstructorAccessorImpl.newInstance(Unknown Source) at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(Unknown Sou rce) at java.lang.reflect.Constructor.newInstance(Unknown Source) at com.mysql.jdbc.Util.handleNewInstance(Util.java:411) at com.mysql.jdbc.Util.getInstance(Util.java:386) at com.mysql.jdbc.SQLError.createSQLException(SQLError.java:1052) at com.mysql.jdbc.MysqlIO.checkErrorPacket(MysqlIO.java:3609) at com.mysql.jdbc.MysqlIO.checkErrorPacket(MysqlIO.java:3541) at com.mysql.jdbc.MysqlIO.sendCommand(MysqlIO.java:2002) at com.mysql.jdbc.MysqlIO.sqlQueryDirect(MysqlIO.java:2163) at com.mysql.jdbc.ConnectionImpl.execSQL(ConnectionImpl.java:2618) at com.mysql.jdbc.ConnectionImpl.execSQL(ConnectionImpl.java:2568) at com.mysql.jdbc.StatementImpl.executeQuery(StatementImpl.java:1557) at org.openstreetmap.osmosis.apidb.common.DatabaseContext.executeQuery(D atabaseContext.java:424) ... 20 more 04.07.2012 22:32:29 org.openstreetmap.osmosis.core.Osmosis main SEVERE: Execution aborted. org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed . at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForComple tion(Pipeline.java:146) at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92) at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37) at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at sun.reflect.NativeMethodAccessorImpl.invoke(Unknown Source) at sun.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source) at java.lang.reflect.Method.invoke(Unknown Source) at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Laun cher.java:329) at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.jav a:239) at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(La uncher.java:409) at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java: 352) at org.codehaus.classworlds.Launcher.main(Launcher.java:47)</p>
<p>So, am I doing something wrong? I have a database structure that I downloaded from here: <a href="http://gweb.bretth.com/apidb06-mysql-latest.sql?attredirects=0">http://gweb.bretth.com/apidb06-mysql-latest.sql?attredirects=0</a></p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '12, 20:39</strong></p>
<img src="https://secure.gravatar.com/avatar/aeb7b59188c6d4ab1846362547839eb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexandru&#39;s gravatar image" />
<p><span>Alexandru</span><br />
<span class="score" title="15 reputation points">15</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexandru has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13988" class="comments-container">
&#10;</div>
<div id="comment-tools-13988" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13988-form-container" class="comment-form-container">
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

<span id="13989"></span>

<div id="answer-container-13989" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13989-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The error message is <strong>Table 'geo.schema_migrations' doesn't exist</strong>. This is a table that contains the version information of the schema. It is important that your schema is the one that osmosis is expecting.</p>
<p>MySQL is no longer supported by the rails port so there is no way to get a current schema for MySQL, on the other hand you would not need it for anything. You could pass <em>validateSchemaVersion=no</em> to osmosis to prevent it from checking the version, however that can cause an error in the process or the result.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '12, 21:43</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-13989" class="comments-container">
<span id="67278"></span>
<div id="comment-67278" class="comment">
<div id="post-67278-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have the same problem. Its a brick wall for me using osmosis. I tried setting validateSchemaVersion=no and still does not work. bummer</p>
</div>
<div id="comment-67278-info" class="comment-info">
<span class="comment-age">(19 Dec '18, 19:53)</span> <span class="comment-user userinfo">Ant</span>
</div>
</div>
<span id="67300"></span>
<div id="comment-67300" class="comment">
<div id="post-67300-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16065/ant">@Ant</a>: what about using PostgreSQL instead?</p>
</div>
<div id="comment-67300-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 20:40)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="67304"></span>
<div id="comment-67304" class="comment">
<div id="post-67304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>aseerel4c26 I am integrating the data into an existing mariadb database and I am more familiar with mariadb. Maybe I could go from PostgreSQL to mariadb.</p>
</div>
<div id="comment-67304-info" class="comment-info">
<span class="comment-age">(21 Dec '18, 02:10)</span> <span class="comment-user userinfo">Ant</span>
</div>
</div>
<span id="67326"></span>
<div id="comment-67326" class="comment">
<div id="post-67326-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16065/ant">@Ant</a>: I'd be surprised if anyone is using the MySQL features of Osmosis now. They effectively became redundant 10 years ago &amp; are maintained for backward compatibility. I suspect it will be difficult to find someone with contemporary knowledge, but also piggy-backing of an old question is not the way to do it.</p>
</div>
<div id="comment-67326-info" class="comment-info">
<span class="comment-age">(22 Dec '18, 22:50)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-13989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13989-form-container" class="comment-form-container">
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

