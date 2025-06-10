+++
type = "question"
title = "Osmosis stops with error: insert or update on table &quot;current_way_nodes&quot; violates foreign key constraint &quot;current_way_nodes_node_id_fkey&quot;"
description = '''I successfully installed the rail port following the official tutorial on ubuntu but i can&#x27;t import my country in my db. Somewhere else i read that this is not the user&#x27;s fault but more of an inconsistency in my .osm file. But if so, then how can i avoid it? Is there a way to make osmosis ignore the...'''
date = "2011-10-25T08:18:00Z"
lastmod = "2011-10-26T12:13:00Z"
weight = 8630
keywords = [ "osmosis", "error" ]
aliases = [ "/questions/8630" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis stops with error: insert or update on table "current_way_nodes" violates foreign key constraint "current_way_nodes_node_id_fkey"](/questions/8630/osmosis-stops-with-error-insert-or-update-on-table-current_way_nodes-violates-foreign-key-constraint-current_way_nodes_node_id_fkey)

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
<span id="post-8630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8630-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I successfully installed the rail port following the official tutorial on ubuntu but i can't import my country in my db. Somewhere else i read that this is not the user's fault but more of an inconsistency in my .osm file. But if so, then how can i avoid it? Is there a way to make osmosis ignore these errors. How do other people install the rail port with such things going on?</p>
<pre><code>INFO: Pipeline executing, waiting for completion.
    Oct 25, 2011 10:01:41 AM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-xml-0.6 failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to load current way nodes.
    at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.populateCurrentWays(ApidbWriter.java:975)
    at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.populateCurrentTables(ApidbWriter.java:1026)
    at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.complete(ApidbWriter.java:1051)
    at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:110)
    at java.lang.Thread.run(Thread.java:679)
Caused by: org.postgresql.util.PSQLException: ERROR: insert or update on table &quot;current_way_nodes&quot; violates foreign key constraint &quot;current_way_nodes_node_id_fkey&quot;
  Detail: Key (node_id)=(26069636) is not present in table &quot;current_nodes&quot;.
    at org.postgresql.core.v3.QueryExecutorImpl.receiveErrorResponse(QueryExecutorImpl.java:2062)
    at org.postgresql.core.v3.QueryExecutorImpl.processResults(QueryExecutorImpl.java:1795)
    at org.postgresql.core.v3.QueryExecutorImpl.execute(QueryExecutorImpl.java:257)
    at org.postgresql.jdbc2.AbstractJdbc2Statement.execute(AbstractJdbc2Statement.java:479)
    at org.postgresql.jdbc2.AbstractJdbc2Statement.executeWithFlags(AbstractJdbc2Statement.java:367)
    at org.postgresql.jdbc2.AbstractJdbc2Statement.execute(AbstractJdbc2Statement.java:360)
    at org.openstreetmap.osmosis.apidb.v0_6.ApidbWriter.populateCurrentWays(ApidbWriter.java:972)
    ... 4 more
Oct 25, 2011 10:01:41 AM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
    at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
    at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
    at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke(Method.java:616)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:329)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:239)
    at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:409)
    at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:352)
    at org.codehaus.classworlds.Launcher.main(Launcher.java:31)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '11, 08:18</strong></p>
<img src="https://secure.gravatar.com/avatar/dc9b01669c0702f230fa57c384b947a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexz&#39;s gravatar image" />
<p><span>alexz</span><br />
<span class="score" title="225 reputation points">225</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Oct '11, 07:45</strong> </span></p>
</div>
</div>
<div id="comments-container-8630" class="comments-container">
&#10;</div>
<div id="comment-tools-8630" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8630-form-container" class="comment-form-container">
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

<span id="8663"></span>

<div id="answer-container-8663" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8663-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's an inconsistency in your .osm file, as you put in your question.</p>
<p>The most likely cause of this is that you have an extract which was created with the standard osmosis settings - which means that if a way references nodes outside of the bbox requested, the extra nodes are not included and so the extract has "incomplete" ways. Or the same thing with relations.</p>
<p>See the <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#Area_Filtering_Tasks">Detailed Usage</a> description of the bbox tasks of osmosis for more details.</p>
<p>To solve this, you will either need to obtain an extract with completed ways and relations, or make your own with the "completeWays" and "completeRelations" flags set to true. Alternatively, you can use the "clipIncompleteEntities" to alter the ways and relations in order that they won't refer to missing entities.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '11, 09:47</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-8663" class="comments-container">
<span id="8665"></span>
<div id="comment-8665" class="comment">
<div id="post-8665-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks i'll try that as soon as possible. Meanwhile, i can add that i was importing a country downloaded from <a href="http://cloudmade.com">cloudmade.com</a> . Do you happen to know if they practice such things as not including the extra nodes?</p>
</div>
<div id="comment-8665-info" class="comment-info">
<span class="comment-age">(26 Oct '11, 10:16)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8667"></span>
<div id="comment-8667" class="comment">
<div id="post-8667-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I believe that's the case. You can try downloading from <a href="http://www.geofabrik.de">www.geofabrik.de</a> instead - the extracts from there have completeWays set to true.</p>
</div>
<div id="comment-8667-info" class="comment-info">
<span class="comment-age">(26 Oct '11, 10:48)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="8668"></span>
<div id="comment-8668" class="comment">
<div id="post-8668-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I beleve geofabrik uses <em>clipIncompleteEntities</em> set and not <em>completeWays</em>. This means that you can not export the geofabrik data back to OSM.</p>
</div>
<div id="comment-8668-info" class="comment-info">
<span class="comment-age">(26 Oct '11, 11:25)</span> <span class="comment-user userinfo">Gnonthgol ♦</span>
</div>
</div>
<span id="8670"></span>
<div id="comment-8670" class="comment">
<div id="post-8670-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That's not the case - I checked with frederik before posting, and that matches what he's previously said on the mailing lists.</p>
</div>
<div id="comment-8670-info" class="comment-info">
<span class="comment-age">(26 Oct '11, 11:59)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="8671"></span>
<div id="comment-8671" class="comment">
<div id="post-8671-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Geofabrik has moved the planet splitting from osmosis to a program called 'history-splitter'.</p>
</div>
<div id="comment-8671-info" class="comment-info">
<span class="comment-age">(26 Oct '11, 12:13)</span> <span class="comment-user userinfo">ajoessen</span>
</div>
</div>
</div>
<div id="comment-tools-8663" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8663-form-container" class="comment-form-container">
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

