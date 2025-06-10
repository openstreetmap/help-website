+++
type = "question"
title = "Error occurs when use osmosis command to import planet-latest.osm.pbf file."
description = '''I use nohup osmosis --read-pbf /mnt/planet/planet-latest.osm.pbf --write-apidb host=&quot;localhost&quot; database=&quot;openstreetmap&quot; user=&quot;osm&quot; password=&quot;osm&quot; validateSchemaVersion=&quot;no command to import data into openstreetmap database three days ago, today , the command failed by following error: 十二月 15, 2016 ...'''
date = "2016-12-18T01:59:00Z"
lastmod = "2016-12-22T14:56:00Z"
weight = 53591
keywords = [ "pgsql", "planet.osm", "osmosis" ]
aliases = [ "/questions/53591" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error occurs when use osmosis command to import planet-latest.osm.pbf file.](/questions/53591/error-occurs-when-use-osmosis-command-to-import-planet-latestosmpbf-file)

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
<span id="post-53591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53591-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I use <strong>nohup osmosis --read-pbf /mnt/planet/planet-latest.osm.pbf --write-apidb host="localhost" database="openstreetmap" user="osm" password="osm" validateSchemaVersion="no</strong> command to import data into openstreetmap database three days ago, today , the command failed by following error:</p>
<pre><code>十二月 15, 2016 3:31:01 上午 org.openstreetmap.osmosis.core.Osmosis run
信息: Osmosis Version 0.40.1
十二月 15, 2016 3:31:01 上午 org.openstreetmap.osmosis.core.Osmosis run
信息: Preparing pipeline.
十二月 15, 2016 3:31:01 上午 org.openstreetmap.osmosis.core.Osmosis run
信息: Launching pipeline execution.
        at crosby.binary.osmosis.OsmosisBinaryParser.parseWays(OsmosisBinaryParser.java:172)
        at crosby.binary.BinaryParser.parse(Unknown Source)
        at crosby.binary.BinaryParser.handleBlock(Unknown Source)
        at crosby.binary.file.FileBlock.process(Unknown Source)
        at crosby.binary.file.BlockInputStream.process(Unknown Source)
        at crosby.binary.osmosis.OsmosisReader.run(OsmosisReader.java:37)
        at java.lang.Thread.run(Thread.java:745)
**Caused by**: org.postgresql.util.PSQLException: ERROR: cannot have more than 2^32-1 commands in a transaction
  在位置：SQL statement &quot;SELECT 1 FROM ONLY &quot;public&quot;.&quot;ways&quot; x WHERE &quot;way_id&quot; OPERATOR(pg_catalog.=) $1 AND &quot;version&quot; OPERATOR(pg_catalog.=) $2 FOR KEY SHARE OF x&quot;
        at org.postgresql.core.v3.QueryExecutorImpl.receiveErrorResponse(QueryExecutorImpl.java:2157)
        at org.postgresql.core.v3.QueryExecutorImpl.processResults(QueryExecutorImpl.java:1886)
        at org.postgresql.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.java:255)
        at org.postgresql.jdbc2.AbstractJdbc2Statement.execute(AbstractJdbc2Statement.java:555)
        at org.postgresql.jdbc2.AbstractJdbc2Statement.executeWithFlags(AbstractJdbc2Statement.java:417)
        at org.postgresql.jdbc2.AbstractJdbc2Statement.executeUpdate(AbstractJdbc2Statement.java:363)
        at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.flushWayTags(ApidbWriter.java:723)
        ... 12 more</code></pre>
<p>It has import 821GB data into the database, and this makes me lose hope to import the planet data successfully, please help me. The osmosis version is 0.40.1, should i use the latest version 0.45 to re-run the command again?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pgsql" rel="tag" title="see questions tagged &#39;pgsql&#39;">pgsql</span> <span class="post-tag tag-link-planet.osm" rel="tag" title="see questions tagged &#39;planet.osm&#39;">planet.osm</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '16, 01:59</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Dec '16, 09:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-53591" class="comments-container">
<span id="53594"></span>
<div id="comment-53594" class="comment">
<div id="post-53594-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>org.postgresql.util.PSQLException: ERROR: cannot have more than 2^32-1 commands in a transaction</code> -&gt; This is a bug in osmosis: <a href="https://trac.openstreetmap.org/ticket/4597">https://trac.openstreetmap.org/ticket/4597</a> .Unfortunately still open, at least according to the ticket. However version 0.40.1 is <em>very very</em> old. I think there is a valid chance that the newest version doesn't produce this error any more.</p>
</div>
<div id="comment-53594-info" class="comment-info">
<span class="comment-age">(18 Dec '16, 09:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="53650"></span>
<div id="comment-53650" class="comment">
<div id="post-53650-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I use the newest version 0.45 to re-run the command, but the error appears again, what should i do, Is there any other solution to import the planet data into the database?</p>
</div>
<div id="comment-53650-info" class="comment-info">
<span class="comment-age">(22 Dec '16, 02:53)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
<span id="53664"></span>
<div id="comment-53664" class="comment">
<div id="post-53664-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, for example using osm2pgsql. It really depends on your use-case. See <a href="https://wiki.openstreetmap.org/wiki/Databases_and_data_access_APIs#Database_Schemas">https://wiki.openstreetmap.org/wiki/Databases_and_data_access_APIs#Database_Schemas</a></p>
</div>
<div id="comment-53664-info" class="comment-info">
<span class="comment-age">(22 Dec '16, 11:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="53673"></span>
<div id="comment-53673" class="comment">
<div id="post-53673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How to use osm2pgsql to import planet data into the openstreetmap database? What's the command if i just need the updatable schemas? I have installed the rails port, and i need to display the detail message after i use nominatiom to search a place name.</p>
</div>
<div id="comment-53673-info" class="comment-info">
<span class="comment-age">(22 Dec '16, 14:56)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
</div>
<div id="comment-tools-53591" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53591-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

