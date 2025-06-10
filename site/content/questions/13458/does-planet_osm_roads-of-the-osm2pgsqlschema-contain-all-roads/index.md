+++
type = "question"
title = "Does planet_osm_roads of the Osm2pgsql/schema contain all roads?"
description = '''Regarding to wiki, planet_osm_roads contains a subset of planet_osm_line. see wiki But does it cover all roads? I am only interested in the data about roads for cars. Can I use the planet_osm_roads to filter this information, or is it maybe incomplete?'''
date = "2012-06-12T13:30:00Z"
lastmod = "2018-10-31T12:29:00Z"
weight = 13458
keywords = [ "osm2pgsql", "mapnik", "database" ]
aliases = [ "/questions/13458" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Does planet_osm_roads of the Osm2pgsql/schema contain all roads?](/questions/13458/does-planet_osm_roads-of-the-osm2pgsqlschema-contain-all-roads)

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
<span id="post-13458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13458-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Regarding to wiki, <em>planet_osm_roads</em> contains a subset of <em>planet_osm_line</em>. <a href="http://wiki.openstreetmap.org/wiki/Osm2pgsql/schema#Processed_Data">see wiki</a></p>
<p>But does it cover all roads? I am only interested in the data about roads for cars.</p>
<p>Can I use the <em>planet_osm_roads</em> to filter this information, or is it maybe incomplete?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '12, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/49f0c5218671e039c889fc520ea55a92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="np00&#39;s gravatar image" />
<p><span>np00</span><br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="np00 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13458" class="comments-container">
&#10;</div>
<div id="comment-tools-13458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13458-form-container" class="comment-form-container">
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

<span id="13460"></span>

<div id="answer-container-13460" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13460-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://github.com/openstreetmap/osm2pgsql/blob/8bf4e4a9f6eafb4a4c31b6fb6be831983fefc8ce/output-pgsql.c#L90">This</a> might be the list of tags included in planet_osm_roads but I am not quite sure about this. It does not include all road types, as for example living_street, service and track are missing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '12, 14:39</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jun '12, 14:43</strong> </span></p>
</div>
</div>
<div id="comments-container-13460" class="comments-container">
<span id="66599"></span>
<div id="comment-66599" class="comment">
<div id="post-66599-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, in nowadays (2018) there are a option in the software osm2pgsql to show the list of tags?</p>
</div>
<div id="comment-66599-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 12:29)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-13460" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13460-form-container" class="comment-form-container">
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

