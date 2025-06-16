+++
type = "question"
title = "Error while following osmosis import to database examples"
description = '''Hello, I have problems to follow the examples on: https://wiki.openstreetmap.org/wiki/Osmosis  While I am trying to start: &#x27;osmosis --read-xml file=&quot;myosm.osm&quot; --write-apidb host=&quot;localhost&quot; database=&quot;postgis&quot; user=&quot;postgres&quot; password=&quot;xxx&quot;&#x27; I get the following errors. The database is fresh and clean...'''
date = "2011-05-09T09:49:00Z"
lastmod = "2011-05-10T16:50:00Z"
weight = 5066
keywords = [ "xml", "import", "exception", "postgresql", "osmosis" ]
aliases = [ "/questions/5066" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Error while following osmosis import to database examples](/questions/5066/error-while-following-osmosis-import-to-database-examples)

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
<span id="post-5066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5066-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have problems to follow the examples on: <a href="https://wiki.openstreetmap.org/wiki/Osmosis">https://wiki.openstreetmap.org/wiki/Osmosis</a></p>
<p>While I am trying to start: 'osmosis --read-xml file="myosm.osm" --write-apidb host="localhost" database="postgis" user="postgres" password="xxx"' I get the following errors.</p>
<p>The database is fresh and clean. My OS is Win x64</p>
<p>Here is the exception trace:</p>
<p>SCHWERWIEGEND: Thread for task 1-read-xml failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to create resultset. at org.openstreetmap.osmosis.apidb.common.DatabaseContext.executeQuery(DatabaseContext.java:429) ...etc... at java.lang.Thread.run(Unknown Source) Caused by: org.postgresql.util.PSQLException: FEHLER: Relation +schema_migrations½ existiert nicht Position: 21 at org.postgresql.core.v3.QueryExecutorImpl.receiveErrorResponse(QueryExecutorImpl.java:2062) ...etc... at org.openstreetmap.osmosis.apidb.common.DatabaseContext.executeQuery(DatabaseContext.java:424)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-exception" rel="tag" title="see questions tagged &#39;exception&#39;">exception</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '11, 09:49</strong></p>
<img src="https://secure.gravatar.com/avatar/07cec96eea4eef0a62afcb27da9e33c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="asdfasdfasdf&#39;s gravatar image" />
<p><span>asdfasdfasdf</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="asdfasdfasdf has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 May '11, 12:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-5066" class="comments-container">
&#10;</div>
<div id="comment-tools-5066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5066-form-container" class="comment-form-container">
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

<span id="5069"></span>

<div id="answer-container-5069" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5069-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at this answer <a href="/questions/4331/error-loading-the-osm-file-into-the-database.">https://help.openstreetmap.org/questions/4331/error-loading-the-osm-file-into-the-database.</a> You do not appear to have installed the database tables in PostGIS.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '11, 10:17</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-5069" class="comments-container">
<span id="5079"></span>
<div id="comment-5079" class="comment">
<div id="post-5079-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there a complete script/application for windows? 'https://wiki.openstreetmap.org/wiki/Osmosis/PostGIS_Setup' and especially the 9.04 section is useless for windows because of environment variables/ user restrictions and other things.</p>
</div>
<div id="comment-5079-info" class="comment-info">
<span class="comment-age">(09 May '11, 19:03)</span> <span class="comment-user userinfo">asdfasdfasdf</span>
</div>
</div>
<span id="5080"></span>
<div id="comment-5080" class="comment">
<div id="post-5080-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The standard PostGIS tools work for me under Windows. Perhaps try with cygwin, or use pgadmin &amp; copy paste DDL into query window. In general its usually best to run things either with full paths or a specially constructed PATH within a DOS shell.</p>
</div>
<div id="comment-5080-info" class="comment-info">
<span class="comment-age">(09 May '11, 21:23)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="5081"></span>
<div id="comment-5081" class="comment">
<div id="post-5081-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you tell me which files i have to paste into pgadmin. I already tried some of these. Especially the last one did not create the right shema (simple or something) for me.</p>
<p>hstore.sql postgis.sql spatial_ref_sys.sql pgsql_simple_schema_0.6.sql</p>
</div>
<div id="comment-5081-info" class="comment-info">
<span class="comment-age">(09 May '11, 22:06)</span> <span class="comment-user userinfo">asdfasdfasdf</span>
</div>
</div>
<span id="5088"></span>
<div id="comment-5088" class="comment">
<div id="post-5088-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suggest you raise a new question for this: documentation for getting things working on windows is usually poor. Frequently bits of OSM software don't work on Windows for trivial reasons such as assuming "/" is the separator of directory and filenames. Therefore a broader question is likely to be of more use to everyone.</p>
<p>Quickly, you need to install in this order postgis, hstore, either simple schema or the api schema. I don't know if you need spatial_ref_sys, but its easy to check by trying to load an empty or dumpy osm xml file.</p>
</div>
<div id="comment-5088-info" class="comment-info">
<span class="comment-age">(10 May '11, 10:19)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-5069" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5069-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5095"></span>

<div id="answer-container-5095" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5095-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You've tried loading the data into the format used by the "<a href="https://wiki.openstreetmap.org/wiki/Rails_port">Rails Port</a>" by using the --write-apidb flag. Osmosis is checking for the tables it expects to find, but you say you have a clean database so it's failing. Note that the apidb format is designed for use with the web front end and only uses Postgres types (i.e. no spatial columns) so might not be what you are looking for.</p>
<p>You need to decide what format you want the tables to be in, since osmosis supports a few different database structures. These can be chosen with the following options.</p>
<ul>
<li>--write-apidb</li>
<li>--write-pgsql</li>
<li>--write-pgsimp</li>
</ul>
<p>You need to investigate and decide which is the most appropriate. In every case you need to have the correct database tables set up before loading with osmosis. Instructions are available on the <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage">Osmosis Detailed Usage</a> page.</p>
<p>For loading data into postgres for use with mapnik you should look at <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a> instead, which uses yet another choice of table layouts.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 May '11, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-5095" class="comments-container">
&#10;</div>
<div id="comment-tools-5095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5095-form-container" class="comment-form-container">
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

