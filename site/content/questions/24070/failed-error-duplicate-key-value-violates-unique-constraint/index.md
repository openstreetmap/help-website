+++
type = "question"
title = "Failed error : duplicate key value violates unique constraint"
description = '''I want to upload planet-latest.osm on a PostgreSQL database via osm2pgsql but even if I&#x27;ve got no error for the creation of the table, the process stops acting near the 2Go and the error is (sorry it&#x27;s french):  Reading in file: osm/planet-latest.osm Processing: Node(1873580k) Way(0k) Relation(0k)CO...'''
date = "2013-07-08T08:40:00Z"
lastmod = "2013-07-08T12:21:00Z"
weight = 24070
keywords = [ "postgresql", "osm", "osm2pgsql" ]
aliases = [ "/questions/24070" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Failed error : duplicate key value violates unique constraint](/questions/24070/failed-error-duplicate-key-value-violates-unique-constraint)

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
<span id="post-24070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24070-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to upload planet-latest.osm on a PostgreSQL database via osm2pgsql but even if I've got no error for the creation of the table, the process stops acting near the 2Go and the error is (sorry it's french):</p>
<blockquote>
<p>Reading in file: osm/planet-latest.osm Processing: Node(1873580k) Way(0k) Relation(0k)COPY_END for COPY planet_osm_nodes FROM STDIN; failed: ERREUR: la valeur d'une clé dupliquée rompt la contrainte unique « planet_osm_nodes_pkey » CONTEXT: COPY planet_osm_nodes, ligne 1758128898 : « 2147483647 688301347 -16699132 \N »</p>
<p>Error occurred, cleaning up</p>
</blockquote>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '13, 08:40</strong></p>
<img src="https://secure.gravatar.com/avatar/932e88b416fd1b03552a6d58ef1a351a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="so4ne&#39;s gravatar image" />
<p><span>so4ne</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="so4ne has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24070" class="comments-container">
&#10;</div>
<div id="comment-tools-24070" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24070-form-container" class="comment-form-container">
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

<span id="24076"></span>

<div id="answer-container-24076" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24076-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="so4ne has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have a version of osm2pgsql that only supports 32bit IDs (if you type "osm2pgsql" it will say something about "32bit ID space" in the first line of output, or even worse, nothing about ID space at all. You have to re-compile osm2pgsql or download a version compiled for 64bit IDs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '13, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-24076" class="comments-container">
<span id="24080"></span>
<div id="comment-24080" class="comment">
<div id="post-24080-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your reply, do you know how to switch to 64bit on a Debian 6.0 Squeeze? I have the 0.69 version of osm2pgsql</p>
</div>
<div id="comment-24080-info" class="comment-info">
<span class="comment-age">(08 Jul '13, 12:03)</span> <span class="comment-user userinfo">so4ne</span>
</div>
</div>
<span id="24081"></span>
<div id="comment-24081" class="comment">
<div id="post-24081-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The osm2pgsql package of Debian 6.0 ("Squeeze") doesn't support 64bit IDs. This is because Squeeze is rather old (from early 2011). The current stable version of Debian (7.0 aka "Wheezy") supports 64bit IDs. But if you cannot upgrade to Wheezy you can still get a recent version from <a href="https://github.com/openstreetmap/osm2pgsql">GitHub</a>, see the <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql wiki page</a> for more information.</p>
</div>
<div id="comment-24081-info" class="comment-info">
<span class="comment-age">(08 Jul '13, 12:21)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24076" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24076-form-container" class="comment-form-container">
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

