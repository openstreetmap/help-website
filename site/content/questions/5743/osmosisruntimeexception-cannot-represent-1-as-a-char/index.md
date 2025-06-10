+++
type = "question"
title = "OsmosisRuntimeException: Cannot represent -1 as a char."
description = '''Hi, extracting a polygon from postgres via osmosis fails: /home/osm/osmosis -v --read-pgsql database=&quot;osm&quot; user=&quot;osm&quot; password=&quot;secret&quot; validateSchemaVersion=no --dataset-bounding-box bottom=50.0 left=8.6 top=50.1 right=8.7 --write-xml db.osm   FINE: Rolling back JDBC transaction on Connection [jdbc...'''
date = "2011-06-13T22:27:00Z"
lastmod = "2011-06-14T18:11:00Z"
weight = 5743
keywords = [ "postgres", "osmosis" ]
aliases = [ "/questions/5743" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OsmosisRuntimeException: Cannot represent -1 as a char.](/questions/5743/osmosisruntimeexception-cannot-represent-1-as-a-char)

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
<span id="post-5743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5743-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, extracting a polygon from postgres via osmosis fails:</p>
<pre><code>/home/osm/osmosis -v --read-pgsql database=&quot;osm&quot; user=&quot;osm&quot; password=&quot;secret&quot; validateSchemaVersion=no --dataset-bounding-box bottom=50.0 left=8.6 top=50.1 right=8.7 --write-xml db.osm</code></pre>
<blockquote>
<p>FINE: Rolling back JDBC transaction on Connection [jdbc:<span>postgresql://localhost/osm_rn,</span> UserName=osm, PostgreSQL Native Driver] Jun 13, 2011 10:24:13 PM org.springframework.jdbc.datasource.DataSourceTransactionManager doCleanupAfterCompletion FINE: Releasing JDBC Connection [jdbc:<span>postgresql://localhost/osm_rn,</span> UserName=osm, PostgreSQL Native Driver] after transaction Jun 13, 2011 10:24:13 PM org.springframework.jdbc.datasource.DataSourceUtils doReleaseConnection FINE: Returning JDBC Connection to DataSource Jun 13, 2011 10:24:13 PM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion SEVERE: Thread for task 1-read-pgsql failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: Cannot represent -1 as a char. at org.openstreetmap.osmosis.core.util.IntAsChar.intToChar(IntAsChar.java:35)</p>
</blockquote>
<p>Any hints?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '11, 22:27</strong></p>
<img src="https://secure.gravatar.com/avatar/9d5e50bc4c330755560bc1a4eccb1574?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gwk&#39;s gravatar image" />
<p><span>gwk</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gwk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '11, 09:21</strong> </span></p>
</div>
</div>
<div id="comments-container-5743" class="comments-container">
&#10;</div>
<div id="comment-tools-5743" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5743-form-container" class="comment-form-container">
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

<span id="5744"></span>

<div id="answer-container-5744" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5744-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-5744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gwk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="http://lists.openstreetmap.org/listinfo/osmosis-dev">osmosis-dev mailing list</a> is a good place to ask such questions.</p>
<p>Specifically, are you using Osmosis 0.39 or an earlier version? There has been a change affecting the internal serialization of objects in r25674 which is included in 0.39 but not older versions of Osmosis. This change has fixed the "Cannot represent -1 as a char" bug in a different scenario; maybe it helps for your case as well. <a href="http://lists.openstreetmap.org/pipermail/osmosis-dev/2011-March/000961.html">(Mailing list article.)</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '11, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jun '11, 18:17</strong> </span></p>
</div>
</div>
<div id="comments-container-5744" class="comments-container">
<span id="5772"></span>
<div id="comment-5772" class="comment">
<div id="post-5772-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Extracting a polygon via osmosis-0.39 works fine. Tried osmosis-0.38 before.</p>
</div>
<div id="comment-5772-info" class="comment-info">
<span class="comment-age">(14 Jun '11, 18:11)</span> <span class="comment-user userinfo">gwk</span>
</div>
</div>
</div>
<div id="comment-tools-5744" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5744-form-container" class="comment-form-container">
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

