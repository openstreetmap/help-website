+++
type = "question"
title = "Conflation of 3rd Party Data to Local OSM Planet Database (PostgreSQL)"
description = '''I am seeking advice for a workflow solution to accomplish the conflation of 3rd party (e.g., government/private) data (.shp) into a local PostgreSQL/PostGIS database of the entire planet running on an in-house server.  I have become fluent with applying daily OSM changesets using Osmosis and Osm2pgs...'''
date = "2018-10-31T15:15:00Z"
lastmod = "2018-10-31T15:15:00Z"
weight = 66603
keywords = [ "changefile", "postgresql", "osm2pgsql", "postgis", "conflation" ]
aliases = [ "/questions/66603" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Conflation of 3rd Party Data to Local OSM Planet Database (PostgreSQL)](/questions/66603/conflation-of-3rd-party-data-to-local-osm-planet-database-postgresql)

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
<span id="post-66603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66603-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am seeking advice for a workflow solution to accomplish the conflation of 3rd party (e.g., government/private) data (.shp) into a local PostgreSQL/PostGIS database of the entire planet running on an in-house server.</p>
<p>I have become fluent with applying daily OSM changesets using Osmosis and Osm2pgsql. I am currently keeping our database up to date by appending the daily .osc changefiles to the database. This is working great, and I am comfortable with the osm2pgsql --append command.</p>
<p>In my initial research for available conflation methodologies/tools (e.g., JOSM, Hootenany), it looks like these tools do a great job at conflation with manual review of conflicts in a GUI environment (this is what we want!) but then they just upload the changesets directly to OSM servers to update the public map.</p>
<p>In our project, we will be working with sensitive/confidential data that absolutely cannot go public. Hence, our local planetary OSM Postgres server, and the need to produce a local changefile for appending vs. an OSM.org changeset upload.</p>
<p>Is it currently possible with any existing tooling to conflate to/compare against a local PostgreSQL database on the planetary scale, and after conflating/conflict resolution, locally export a standard changefile that would go through the normal osm2pgsql --append process, like applying a daily diff?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changefile" rel="tag" title="see questions tagged &#39;changefile&#39;">changefile</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-conflation" rel="tag" title="see questions tagged &#39;conflation&#39;">conflation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '18, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/bbd0e184c8bbe03544aefb4e57ac5ccd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mykol404&#39;s gravatar image" />
<p><span>mykol404</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mykol404 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66603" class="comments-container">
&#10;</div>
<div id="comment-tools-66603" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66603-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

