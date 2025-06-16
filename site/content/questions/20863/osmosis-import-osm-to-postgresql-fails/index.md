+++
type = "question"
title = "Osmosis: import .osm to postgresql fails"
description = '''Hi, I am trying to import a 2GB .osm file to a new empty postgresql database but the command I use fails and I have no idea why. This is the command: osmosis --read-xml file=&quot;D:&#92;Licenta&#92;Romania OSM&#92;romania.osm&quot; --write-pgsql host=&quot;localhost&quot; database=&quot;romania&quot; user=&quot;postgres&quot; password=&quot;mypassword&quot; T...'''
date = "2013-03-21T07:59:00Z"
lastmod = "2013-03-24T09:03:00Z"
weight = 20863
keywords = [ "import" ]
aliases = [ "/questions/20863" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Osmosis: import .osm to postgresql fails](/questions/20863/osmosis-import-osm-to-postgresql-fails)

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
<span id="post-20863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20863-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am trying to import a 2GB .osm file to a new empty postgresql database but the command I use fails and I have no idea why. This is the command:</p>
<p><em>osmosis --read-xml file="D:\Licenta\Romania OSM\romania.osm" --write-pgsql host="localhost" database="romania" user="postgres" password="mypassword"</em></p>
<p>This is the error I get:</p>
<p>...</p>
<p><em>SEVERE: Thread for task 1-read-xml failed org.springframework.jdbc.BadSqlGrammarException: StatementCallback; bad SQL gram mar [SELECT version FROM schema_info]; nested exception is org.postgresql.util.P SQLException: ERROR: relation "schema_info" does not exist Position: 21 at org.springframework.jdbc.support.SQLErrorCodeSQLExceptionTranslator.d oTranslate(SQLErrorCodeSQLExceptionTranslator.java:233)</em></p>
<p>...</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Mar '13, 07:59</strong></p>
<img src="https://secure.gravatar.com/avatar/af030346f57b37767fe7e80f23e07d7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raduzugravu&#39;s gravatar image" />
<p><span>raduzugravu</span><br />
<span class="score" title="31 reputation points">31</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raduzugravu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20863" class="comments-container">
&#10;</div>
<div id="comment-tools-20863" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20863-form-container" class="comment-form-container">
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

<span id="20944"></span>

<div id="answer-container-20944" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20944-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="raduzugravu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to create the correct schema (i.e. create the database tables) first. One of the tables (i.e. relations) created will be called "schema_info", which osmosis checks before it loads anything, and that's where the error 'relation "schema_info" does not exist' comes from.</p>
<p>Please have a read of the <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#PostGIS_Tasks_.28Snapshot_Schema.29">osmosis documentation on the PostgreSQL tasks</a>. You will need to choose which of the schemas is appropriate for your task, then load the schema (e.g. <code>psql -d romania -f /path/to/schema.sql</code>) then load the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '13, 09:03</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-20944" class="comments-container">
&#10;</div>
<div id="comment-tools-20944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20944-form-container" class="comment-form-container">
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

