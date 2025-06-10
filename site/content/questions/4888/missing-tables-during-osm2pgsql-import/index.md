+++
type = "question"
title = "Missing tables during osm2pgsql import"
description = '''I always get the following message during import of downloaded compressed osm data into my database (version 8.4). I can connect to the db via pgadmin tool. I have gone through the installation steps of the Mapnik Wiki Page (http://wiki.openstreetmap.org/wiki/Mapnik). Database is cool. But where are...'''
date = "2011-04-28T13:53:00Z"
lastmod = "2011-04-29T10:51:00Z"
weight = 4888
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/4888" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Missing tables during osm2pgsql import](/questions/4888/missing-tables-during-osm2pgsql-import)

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
<span id="post-4888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4888-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I always get the following message during import of downloaded compressed osm data into my database (version 8.4). I can connect to the db via pgadmin tool. I have gone through the installation steps of the Mapnik Wiki Page (<a href="http://wiki.openstreetmap.org/wiki/Mapnik">http://wiki.openstreetmap.org/wiki/Mapnik</a>). Database is cool. But where are the missing table?</p>
<p>postgres@oli-VirtualBox:~$ osm2pgsql -m -d gis /oli/Downloads/baden-wuerttemberg.osm.bz2 osm2pgsql SVN version 0.69-</p>
<p>Using projection SRS 900913 (Spherical Mercator) Setting up table: planet_osm_point ADVICE: Tabelle »planet_osm_point« doesn't exist, skipping ADVICE: Tabelle »planet_osm_point_tmp« doesn't exist, skipping SELECT AddGeometryColumn('planet_osm_point', 'way', 900913, 'POINT', 2 ); failed: ERROR: AddGeometryColumns() - invalid SRID CONTEXT: SQL statement "SELECT AddGeometryColumn('','', $1 , $2 , $3 , $4 , $5 )" PL/pgSQL-Function »addgeometrycolumn« Zeile 4 at SQL-Statement</p>
<p>Error occurred, cleaning up</p>
<p>Maybe the path to my downloaded osm files could be a problem? rights?</p>
<p>Thanx for helping Oliver</p>
<p><strong>I have added the missing table via SQL from an other osm database, but the errors are still the same!! Strange!</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Apr '11, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/7c86a8d60d75fd3b42099f9286dfc264?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nicioli&#39;s gravatar image" />
<p><span>nicioli</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nicioli has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Apr '11, 14:18</strong> </span></p>
</div>
</div>
<div id="comments-container-4888" class="comments-container">
<span id="4893"></span>
<div id="comment-4893" class="comment">
<div id="post-4893-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The message about the non-existing tables is not critical and can be ignored. The relevant error message is "invalid SRID".</p>
</div>
<div id="comment-4893-info" class="comment-info">
<span class="comment-age">(28 Apr '11, 15:24)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="4904"></span>
<div id="comment-4904" class="comment">
<div id="post-4904-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Frederik, you was right with your advice and i now have a solution for my problem but how it comes that the mercartor projection (epsg 900913) is missing?</p>
</div>
<div id="comment-4904-info" class="comment-info">
<span class="comment-age">(29 Apr '11, 10:51)</span> <span class="comment-user userinfo">nicioli</span>
</div>
</div>
</div>
<div id="comment-tools-4888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4888-form-container" class="comment-form-container">
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

<span id="4890"></span>

<div id="answer-container-4890" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4890-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm no expert, but your error message looks similar to the <a href="http://wiki.openstreetmap.org/wiki/Mapnik#Invalid_projection_in_pgSQL">one described here.</a> Have you seen and tried that solution to see if it helps in your case?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '11, 14:38</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-4890" class="comments-container">
<span id="4891"></span>
<div id="comment-4891" class="comment">
<div id="post-4891-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can try SELECT * FROM geometry_columns WHERE srid = 900913. If you get no rows back then this is indeed your problem.</p>
</div>
<div id="comment-4891-info" class="comment-info">
<span class="comment-age">(28 Apr '11, 14:53)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="4903"></span>
<div id="comment-4903" class="comment">
<div id="post-4903-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you EdLoach for you advice, this was the solution. But now i got a error while opening file - message. Sorry i'am a newbie in Ubuntu but i think i should find a solution for this..</p>
</div>
<div id="comment-4903-info" class="comment-info">
<span class="comment-age">(29 Apr '11, 10:49)</span> <span class="comment-user userinfo">nicioli</span>
</div>
</div>
</div>
<div id="comment-tools-4890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4890-form-container" class="comment-form-container">
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

