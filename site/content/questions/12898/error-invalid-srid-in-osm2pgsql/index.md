+++
type = "question"
title = "ERROR invalid SRID in osm2pgsql"
description = '''Using osm2pgsql to import an OSM-File to PostGIS I get the following error: SELECT AddGeometryColumn(&#x27;planet_osm_point&#x27;, &#x27;way&#x27;, 900913, &#x27;POINT&#x27;, 2 ); failed: FEHLER: AddGeometryColumn() - invalid SRID CONTEXT: SQL statement &quot;SELECT AddGeometryColumn(&#x27;&#x27;,&#x27;&#x27;,$1,$2,$3,$4,$5, $6)&quot; PL/pgSQL-Funktion ┬╗add...'''
date = "2012-05-23T12:59:00Z"
lastmod = "2014-06-18T11:49:00Z"
weight = 12898
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/12898" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ERROR invalid SRID in osm2pgsql](/questions/12898/error-invalid-srid-in-osm2pgsql)

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
<span id="post-12898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12898-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using osm2pgsql to import an OSM-File to PostGIS I get the following error:</p>
<p>SELECT AddGeometryColumn('planet_osm_point', 'way', 900913, 'POINT', 2 ); failed: FEHLER: AddGeometryColumn() - invalid SRID CONTEXT: SQL statement "SELECT AddGeometryColumn('','',$1,$2,$3,$4,$5, $6)" PL/pgSQL-Funktion ┬╗addgeometrycolumn┬½ Zeile 5 bei SQL-Anweisung</p>
<p>Error occurred, cleaning up</p>
<p>Any hints what could be wrong would be helpful! Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '12, 12:59</strong></p>
<img src="https://secure.gravatar.com/avatar/8f313535c34b25d88be0d4119dc6b2bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="faxx&#39;s gravatar image" />
<p><span>faxx</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="faxx has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12898" class="comments-container">
<span id="12900"></span>
<div id="comment-12900" class="comment">
<div id="post-12900-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, just recognised I forgot some information: Windows (I know, Linux could do better...) osm2pgsql SVN version 0.69-21289M, pgAdmin III</p>
</div>
<div id="comment-12900-info" class="comment-info">
<span class="comment-age">(23 May '12, 13:32)</span> <span class="comment-user userinfo">faxx</span>
</div>
</div>
</div>
<div id="comment-tools-12898" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12898-form-container" class="comment-form-container">
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

<span id="12902"></span>

<div id="answer-container-12902" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12902-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your version of osm2pgsql is ancient. This is likely to give you more trouble in the future but for now, running this file through your PostGIS will likely help:</p>
<p><a href="http://svn.openstreetmap.org/applications/utils/export/osm2pgsql/900913.sql">http://svn.openstreetmap.org/applications/utils/export/osm2pgsql/900913.sql</a></p>
<p>For the record, if you have a rather new PostGIS, the easiest way is often not to add this projection but to make osm2pgsql use 3857 (-E 3857).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '12, 14:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-12902" class="comments-container">
<span id="34086"></span>
<div id="comment-34086" class="comment">
<div id="post-34086-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have latest version of osm2pgsql(downloaded and installed from github) but I still ran into that problem.</p>
<p>The download link for 900913.sql doesn't work anymore but if you installed osm2pgsql also from source code then you should have the file in here:</p>
<p>/usr/local/share/osm2pgsql/900913.sql</p>
<p>So what i did to fix this problem was following code:</p>
<p>psql -f /usr/local/share/osm2pgsql/900913.sql -d gis</p>
</div>
<div id="comment-34086-info" class="comment-info">
<span class="comment-age">(18 Jun '14, 11:49)</span> <span class="comment-user userinfo">hukko</span>
</div>
</div>
</div>
<div id="comment-tools-12902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12902-form-container" class="comment-form-container">
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

