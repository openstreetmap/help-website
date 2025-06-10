+++
type = "question"
title = "error with osm2pgsql"
description = '''Hi! I use https://protomaps.com/extracts to get extracts of 4 small areas. I merge those with &quot;osmium&quot; into one .osm.pbf that i import with osm2pgsql. This works great with 3 of those extracts, but after adding the 4th I get the following error when importing the data:   DB writer thread failed due ...'''
date = "2021-06-17T09:50:00Z"
lastmod = "2021-06-19T12:37:00Z"
weight = 80604
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/80604" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [error with osm2pgsql](/questions/80604/error-with-osm2pgsql)

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
<span id="post-80604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80604-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I use <a href="https://protomaps.com/extracts">https://protomaps.com/extracts</a> to get extracts of 4 small areas. I merge those with "osmium" into one .osm.pbf that i import with osm2pgsql. This works great with 3 of those extracts, but after adding the 4th I get the following error when importing the data: DB writer thread failed due to ERROR: result COPY_END for planet_osm_rels failed: ERROR: duplicate key value violates unique constraint "planet_osm_rels_pkey" DETAIL: Key (id)=(21510) already exists. CONTEXT: COPY planet_osm_rels, line 43</p>
<p>Any idea how to fix this?</p>
<p>Tobias</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jun '21, 09:50</strong></p>
<img src="https://secure.gravatar.com/avatar/fd01b28100b26992f2d75b2afde1292c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marx1st&#39;s gravatar image" />
<p><span>Marx1st</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marx1st has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80604" class="comments-container">
<span id="80609"></span>
<div id="comment-80609" class="comment">
<div id="post-80609-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Difficult to say without all the details like the file contents, osm2pgsql version used, command line used etc.</p>
<p>Chances are you have different versions of the same object in the input files. This can happen when you downloaded those areas at different points in time.</p>
</div>
<div id="comment-80609-info" class="comment-info">
<span class="comment-age">(18 Jun '21, 07:50)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="80630"></span>
<div id="comment-80630" class="comment">
<div id="post-80630-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, I don't think it is a bug, but rather a problem with the "workflow" I've chosen. I've now downloaded the boundaries as .geojson and used those with "osmium extract" on a .pbf of Germany (from Geofabrik) and merged those files with "osmium merge". That .pbf can be imported without problems into the database... So, I've found a solution for that problem, but ain't that happy about it. It's too complicated for the client I'm building this for, to add new extracts...</p>
</div>
<div id="comment-80630-info" class="comment-info">
<span class="comment-age">(19 Jun '21, 12:37)</span> <span class="comment-user userinfo">Marx1st</span>
</div>
</div>
</div>
<div id="comment-tools-80604" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80604-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

