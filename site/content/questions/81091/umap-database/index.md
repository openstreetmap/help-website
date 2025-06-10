+++
type = "question"
title = "uMap : database"
description = '''Weird question, but does anybody know where are the data stored on uMap (DBMS, servers location, etc.) ? If you have references it&#x27;s even better. Thanks'''
date = "2021-07-27T16:23:00Z"
lastmod = "2021-07-27T23:20:00Z"
weight = 81091
keywords = [ "umap" ]
aliases = [ "/questions/81091" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [uMap : database](/questions/81091/umap-database)

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
<span id="post-81091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81091-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Weird question, but does anybody know where are the data stored on uMap (DBMS, servers location, etc.) ?</p>
<p>If you have references it's even better.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '21, 16:23</strong></p>
<img src="https://secure.gravatar.com/avatar/3447c3fbc55351f06dd75ec10cd6c919?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DouxDoux&#39;s gravatar image" />
<p><span>DouxDoux</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DouxDoux has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81091" class="comments-container">
&#10;</div>
<div id="comment-tools-81091" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81091-form-container" class="comment-form-container">
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

<span id="81092"></span>

<div id="answer-container-81092" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81092-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DouxDoux has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It depends on the <a href="https://wiki.openstreetmap.org/wiki/UMap#Instances">instance</a> you're using.</p>
<p>If it's <code>umap.openstreetmap.fr</code>, the <a href="https://wiki.openstreetmap.org/wiki/FR:Serveurs_OpenStreetMap_France">wiki</a> says it's managed by OSM-FR, hosted by OVH in Roubaix, France.</p>
<p>As for the DBMS, it uses <a href="https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/">GeoDjango</a>, which support most databases (with a preference for PostgreSQL with PostGIS).</p>
<p>If I might be curious, why do you ask ?</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '21, 20:15</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-81092" class="comments-container">
<span id="81093"></span>
<div id="comment-81093" class="comment">
<div id="post-81093-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The database only holds map metadata. There's also a "datalayer" directory on disk that holds all the map layers as GeoJSON. If you have added a lot of data to your map(s), then that datalayer directory can contain GeoJSON files that dwarf the actual database size.</p>
</div>
<div id="comment-81093-info" class="comment-info">
<span class="comment-age">(27 Jul '21, 23:20)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-81092" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81092-form-container" class="comment-form-container">
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

