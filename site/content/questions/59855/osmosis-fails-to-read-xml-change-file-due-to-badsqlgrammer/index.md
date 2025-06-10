+++
type = "question"
title = "Osmosis Fails to read XML Change file due to BadSQLGrammer"
description = '''Good Afternoon all. I am new to osmosis but have been spending a lot of time messing around with it. I finally got my process down to creating a postgres, Running the pgsnapshot_schema_0.6, actions, bbox and linestring commands to bulild the schema. I have postgis and hstore installed. I have succes...'''
date = "2017-09-26T19:49:00Z"
lastmod = "2017-09-26T19:49:00Z"
weight = 59855
keywords = [ "pgsql", "osmosis" ]
aliases = [ "/questions/59855" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis Fails to read XML Change file due to BadSQLGrammer](/questions/59855/osmosis-fails-to-read-xml-change-file-due-to-badsqlgrammer)

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
<span id="post-59855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59855-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good Afternoon all. I am new to osmosis but have been spending a lot of time messing around with it. I finally got my process down to creating a postgres, Running the pgsnapshot_schema_0.6, actions, bbox and linestring commands to bulild the schema. I have postgis and hstore installed. I have successfully imported great britain and belgium using this command below but for respective pbf files.</p>
<p>osmosis --read-pbf file=/N:/RawData/OSM/Great_Britain/great-britain-latest.osm.pbf --write-pgsql host=localhost database=great_britain user=postgres</p>
<p>My issue is on the read xml change files and write pgsql change commands. i have tried the following commands for both db and downloading the change files from geofabrik. How ever i always run into the same exact error every single time. It appears Java or Osmoisis is not finding postgres and doesnt know how to execute the query. I found similar issues online but NO ONE to explain this one because i feel pretty good about having all other things set up correctly. If someone can help resolve this error it would be greatly appreciated!!!</p>
<p>N:\RawData\OSM\Belgium&gt;osmosis --read-xml-change file=N:/RawData/OSM/Belgium/bel_diff.osc.gz outPipe(mypipe) --write-pgsql-change host=localhost database=belgium user=postgres password=postgres inPipe(mypipe) Sep 26, 2017 1:47:07 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.45 Sep 26, 2017 1:47:07 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. Sep 26, 2017 1:47:08 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Launching pipeline execution. Sep 26, 2017 1:47:08 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline executing, waiting for completion. Sep 26, 2017 1:47:09 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion SEVERE: Thread for task 1-read-xml-change failed org.springframework.jdbc.BadSqlGrammarException: PreparedStatementCallback; bad SQL grammar [UPDATE nodes SET id = ?, version = ?, user_id = ?, tstamp = ?, changeset_id = ?, tags = ?, geom = ? WHERE id = ?]; nested exception is org.postgresql.util.PSQLException: Can't infer the SQL type to use for an instance of java.util.HashMap. Use setObject() with an explicit Types value to specify the type to use. at org.springframework.jdbc.support.SQLStateSQLExceptionTranslator.doTranslate(SQLStateSQLExceptionTranslator.java:99) at org.springframework.jdbc.support.AbstractFallbackSQLExceptionTranslator.translate(AbstractFallbackSQLExceptionTranslator.java:73) at org.springframework.jdbc.support.AbstractFallbackSQLExceptionTranslator.translate(AbstractFallbackSQLExceptionTranslator.java:81) at org.springframework.jdbc.support.AbstractFallbackSQLExceptionTranslator.translate(AbstractFallbackSQLExceptionTranslator.java:81) at org.springframework.jdbc.core.JdbcTemplate.execute(JdbcTemplate.java:645) at org.springframework.jdbc.core.JdbcTemplate.update(JdbcTemplate.java:866) at org.springframework.jdbc.core.JdbcTemplate.update(JdbcTemplate.java:890) at org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate.update(NamedParameterJdbcTemplate.java:287) at org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate.update(NamedParameterJdbcTemplate.java:292) at org.openstreetmap.osmosis.pgsnapshot.v0_6.impl.EntityDao.modifyEntity(EntityDao.java:132) at org.openstreetmap.osmosis.pgsnapshot.v0_6.impl.NodeDao.modifyEntity(NodeDao.java:65) at org.openstreetmap.osmosis.pgsnapshot.v0_6.impl.ChangeWriter.write(ChangeWriter.java:126) at org.openstreetmap.osmosis.pgsnapshot.v0_6.impl.ActionChangeWriter.process(ActionChangeWriter.java:54) at org.openstreetmap.osmosis.core.container.v0_6.NodeContainer.process(NodeContainer.java:58) at org.openstreetmap.osmosis.pgsnapshot.v0_6.PostgreSqlChangeWriter.process(PostgreSqlChangeWriter.java:101) at org.openstreetmap.osmosis.xml.v0_6.impl.ChangeSourceElementProcessor$ChangeSinkAdapter.process(ChangeSourceElementProcessor.java:144) at org.openstreetmap.osmosis.xml.v0_6.impl.NodeElementProcessor.end(NodeElementProcessor.java:139) at org.openstreetmap.osmosis.xml.v0_6.impl.OsmChangeHandler.endElement(OsmChangeHandler.java:94) at org.apache.xerces.parsers.AbstractSAXParser.endElement(Unknown Source) at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanEndElement(Unknown Source) at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl$FragmentContentDispatcher.dispatch(Unknown Source) at org.apache.xerces.impl.XMLDocumentFragmentScannerImpl.scanDocument(Unknown Source) at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source) at org.apache.xerces.parsers.XML11Configuration.parse(Unknown Source) at org.apache.xerces.parsers.XMLParser.parse(Unknown Source) at org.apache.xerces.parsers.AbstractSAXParser.parse(Unknown Source) at org.apache.xerces.jaxp.SAXParserImpl$JAXPSAXParser.parse(Unknown Source) at org.apache.xerces.jaxp.SAXParserImpl.parse(Unknown Source) at javax.xml.parsers.SAXParser.parse(Unknown Source) at org.openstreetmap.osmosis.xml.v0_6.XmlChangeReader.run(XmlChangeReader.java:90) at java.lang.Thread.run(Unknown Source) Caused by: org.postgresql.util.PSQLException: Can't infer the SQL type to use for an instance of java.util.HashMap. Use setObject() with an explicit Types value to specify the type to use.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pgsql" rel="tag" title="see questions tagged &#39;pgsql&#39;">pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Sep '17, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/913ce6c316180974e96f3ed3dfe6fc4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Asinger321&#39;s gravatar image" />
<p><span>Asinger321</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Asinger321 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59855" class="comments-container">
&#10;</div>
<div id="comment-tools-59855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59855-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

