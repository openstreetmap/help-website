+++
type = "question"
title = "duplicate key value violates unique constraint &quot;users_display_name_idx&quot;"
description = '''When i use the latest osmosis to import china-latest.psm.pbf into openstreetmap database, some error eccurs, it says that unable to insert user with id 3642735 into the database, duplicate key value violates unique constraint &quot;users_display_name_idx&quot;, Key (display_name)=(Nodes&amp;amp;Roads) already exi...'''
date = "2016-09-27T15:36:00Z"
lastmod = "2016-09-28T10:06:00Z"
weight = 52248
keywords = [ "apidb", "osmosis" ]
aliases = [ "/questions/52248" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [duplicate key value violates unique constraint "users_display_name_idx"](/questions/52248/duplicate-key-value-violates-unique-constraint-users_display_name_idx)

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
<span id="post-52248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52248-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When i use the latest osmosis to import china-latest.psm.pbf into openstreetmap database, some error eccurs, it says that <strong>unable to insert user with id 3642735 into the database</strong>, <strong>duplicate key value violates unique constraint "users_display_name_idx", Key (display_name)=(Nodes&amp;Roads) already exists</strong>. I drop the openstreetmap database and re-create it before run the osmosis command, so the database is empty, but the error still appears. I also try to import other data file such as jordan-latest.osm.pbf, it runs successfully without any error. Only the china-latest.psm.pbf file can not import correctly. It confuses me serveral days and i still could not find out the solution, anyone can help me or give me some useful tips please,thank you.</p>
<p>The command line is <strong>osmosis --read-pbf planet/china-lastet.osm.pbf --write-apidb host="localhost" database="openstreetmap" user="osm" password="osm" validateSchemaVersion="no"</strong>.</p>
<p>And here is the error log:</p>
<p>Thread for task 1-read-pbf failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to insert user with id 3642735 into the database. at org.openstreetmap.osmosis.apidb.v0_6.impl.UserManager.insertUser(UserManager.java:143) at org.openstreetmap.osmosis.apidb.v0_6.impl.UserManager.addOrUpdateUser(UserManager.java:191) at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.process(ApidbWriter.java:1098) at crosby.binary.osmosis.OsmosisBinaryParser.parseDense(OsmosisBinaryParser.java:138) at org.openstreetmap.osmosis.osmbinary.BinaryParser.parse(BinaryParser.java:124) at org.openstreetmap.osmosis.osmbinary.BinaryParser.handleBlock(BinaryParser.java:68) at org.openstreetmap.osmosis.osmbinary.file.FileBlock.process(FileBlock.java:135) at org.openstreetmap.osmosis.osmbinary.file.BlockInputStream.process(BlockInputStream.java:34) at crosby.binary.osmosis.OsmosisReader.run(OsmosisReader.java:45) at java.lang.Thread.run(Thread.java:745) Caused by: org.postgresql.util.PSQLException: ERROR: duplicate key value violates unique constraint "users_display_name_idx" 详细：Key (display_name)=(Nodes&amp;Roads) already exists. at org.postgresql.core.v3.QueryExecutorImpl.receiveErrorResponse(QueryExecutorImpl.java:2157) at org.postgresql.core.v3.QueryExecutorImpl.processResults(QueryExecutorImpl.java:1886) at org.postgresql.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.java:255) at org.postgresql.jdbc2.AbstractJdbc2Statement.execute(AbstractJdbc2Statement.java:555) at org.postgresql.jdbc2.AbstractJdbc2Statement.executeWithFlags(AbstractJdbc2Statement.java:417) at org.postgresql.jdbc2.AbstractJdbc2Statement.executeUpdate(AbstractJdbc2Statement.java:363) at org.openstreetmap.osmosis.apidb.v0_6.impl.UserManager.insertUser(UserManager.java:140) ... 9 more</p>
<p>九月 28, 2016 10:04:30 上午 org.openstreetmap.osmosis.core.Osmosis main 严重: Execution aborted. org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed. at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146) at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92) at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37) at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) at java.lang.reflect.Method.invoke(Method.java:498) at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:328) at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238) at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:408) at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:351) at org.codehaus.classworlds.Launcher.main(Launcher.java:31)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apidb" rel="tag" title="see questions tagged &#39;apidb&#39;">apidb</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Sep '16, 15:36</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Sep '16, 03:05</strong> </span></p>
</div>
</div>
<div id="comments-container-52248" class="comments-container">
<span id="52257"></span>
<div id="comment-52257" class="comment">
<div id="post-52257-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I assume you are using a download from geofabrik.</p>
<p>The error doesn't ring a bell. Can you give us the complete command line you are using an the complete error log (right now I would suspect a character encoding or similar error).</p>
</div>
<div id="comment-52257-info" class="comment-info">
<span class="comment-age">(27 Sep '16, 23:54)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="52266"></span>
<div id="comment-52266" class="comment">
<div id="post-52266-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please never add what should be a comment as an answer and then edit it. That makes it impossible to rearrange questions and comments as they should be.</p>
<p>Back to the question: this looks like an issue somewhere in the API code or the data dumper or on the extract side as this "should not happen".</p>
<p>We've checked and it seems to be a specific issue with the extract you are using. See answer below.</p>
</div>
<div id="comment-52266-info" class="comment-info">
<span class="comment-age">(28 Sep '16, 09:48)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="52267"></span>
<div id="comment-52267" class="comment">
<div id="post-52267-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks to your reply, i will be more careful next time.</p>
</div>
<div id="comment-52267-info" class="comment-info">
<span class="comment-age">(28 Sep '16, 09:58)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
</div>
<div id="comment-tools-52248" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52248-form-container" class="comment-form-container">
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

<span id="52268"></span>

<div id="answer-container-52268" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52268-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yuyy has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The extracts from Geofabrik are kept up to date by applying diffs, as a consequence when a contributor changes their display name this is not propagated to all the data contributed in the extract.</p>
<p>Or put differently: you cannot use Geofabrik extracts to populate an API database with osmosis except if you are very lucky, which you are not.</p>
<p>I would suggest checking with mapzen <a href="https://mapzen.com/data/metro-extracts/">https://mapzen.com/data/metro-extracts/</a> or another provider of extracts if they generate them differently.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '16, 10:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Sep '16, 10:08</strong> </span></p>
</div>
</div>
<div id="comments-container-52268" class="comments-container">
&#10;</div>
<div id="comment-tools-52268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52268-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52265"></span>

<div id="answer-container-52265" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52265-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I transformed the china-latest.osm.pbf into .osc file, and i find that there are two different user_id use the same display_name, one is :</p>
<p>&lt;node id="221454099" version="4" timestamp="2016-02-19T01:31:31Z" uid="1708958" user="Nodes&amp;amp;Roads" changeset="37300193" lat="28.5580746" lon="98.4585189"/&gt;</p>
<p>Another is :</p>
<p>&lt;node id="224205729" version="3" timestamp="2016-02-20T00:02:20Z" uid="3642735" user="Nodes&amp;amp;Roads" changeset="37320893" lat="28.0394804" lon="99.5276968"/&gt;</p>
<p>Maybe we can change one of the display_name in the .osc file to solve the problem. But if i want use the .pbf file, what should i do? I don't know how to edit the .pbf file, i also asked another question <a href="/questions/52262/two-user_id-use-the-same-display_name-in-the-pbf-data-file">here</a>. If someone have some ideal, please answer <a href="/questions/52262/two-user_id-use-the-same-display_name-in-the-pbf-data-file">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '16, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Sep '16, 08:59</strong> </span></p>
</div>
</div>
<div id="comments-container-52265" class="comments-container">
&#10;</div>
<div id="comment-tools-52265" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52265-form-container" class="comment-form-container">
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

