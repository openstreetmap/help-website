+++
type = "question"
title = "Issue with selfhosted nominatim - empty reply for postcodes"
description = '''Hello,  we got an issue with private instance using official docker image. We have issue with some postal codes. For example the public api returns correct data (the issue also occurs with street name and number) for the city:  https://nominatim.openstreetmap.org/search.php?postalcode=89-501&amp;amp;for...'''
date = "2022-05-12T08:53:00Z"
lastmod = "2022-05-19T14:17:00Z"
weight = 84448
keywords = [ "problem", "nominatim", "docker", "server", "postcode" ]
aliases = [ "/questions/84448" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Issue with selfhosted nominatim - empty reply for postcodes](/questions/84448/issue-with-selfhosted-nominatim-empty-reply-for-postcodes)

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
<span id="post-84448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84448-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, we got an issue with private instance using official docker image. We have issue with some postal codes. For example the public api returns correct data (the issue also occurs with street name and number) for the city:</p>
<p><a href="https://nominatim.openstreetmap.org/search.php?postalcode=89-501&amp;format=jsonv2">https://nominatim.openstreetmap.org/search.php?postalcode=89-501&amp;format=jsonv2</a></p>
<p>but our instance returns empty reply. However, when refering to county postcode:</p>
<p><a href="https://nominatim.openstreetmap.org/search.php?postalcode=89-500&amp;format=jsonv2">https://nominatim.openstreetmap.org/search.php?postalcode=89-500&amp;format=jsonv2</a></p>
<p>we do get proper reply from our selfhosted instance, including detailed query with street name/number (we get correct geolocation using the general county post-code)</p>
<p>Our instance configuration is as follows (deployed using docker compose):</p>
<p>POSTGRES_SHARED_BUFFERS: "2GB"</p>
<p>POSTGRES_MAINTENANCE_WORK_MEM: "10GB"</p>
<p>POSTGRES_AUTOVACUUM_WORK_MEM: "2GB"</p>
<p>POSTGRES_WORK_MEM: "50MB"</p>
<p>POSTGRES_EFFECTIVE_CACHE_SIZE: "8GB"</p>
<p>PBF_URL: "https://download.geofabrik.de/europe/poland-latest.osm.pbf" REPLICATION_URL: "https://download.geofabrik.de/europe/poland-updates/" IMPORT_STYLE: "address"</p>
<p>Docker image we use is: mediagis/nominatim:4.0.</p>
<p>Checked for update using:</p>
<p>sudo -u nominatim nominatim replication -v --check-for-updates --project-dir /nominatim</p>
<p>and its up-to-date. Any hints on what may be the issue here? Can too low level import style have anything to do with it?</p>
<p>The 89-500 is general county code <a href="https://znajdzkodpocztowy.pl/szukaj/mk-89-500/,">https://znajdzkodpocztowy.pl/szukaj/mk-89-500/,</a> the 89-501 is strictly city code <a href="https://znajdzkodpocztowy.pl/szukaj/mk-89-501/">https://znajdzkodpocztowy.pl/szukaj/mk-89-501/</a> . The issue extends to other cities as well. If address is specified with general county code everything works, but when local city code is used, reply is empty. The issue does not occur on public api - all local city codes give correct rply. Anything in config we should change?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-docker" rel="tag" title="see questions tagged &#39;docker&#39;">docker</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 May '22, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/cdfa325e85e9c7a9278241e2cb943446?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mzaw9&#39;s gravatar image" />
<p><span>mzaw9</span><br />
<span class="score" title="14 reputation points">14</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mzaw9 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 May '22, 10:57</strong> </span></p>
</div>
</div>
<div id="comments-container-84448" class="comments-container">
<span id="84451"></span>
<div id="comment-84451" class="comment">
<div id="post-84451-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When was the initial import?</p>
</div>
<div id="comment-84451-info" class="comment-info">
<span class="comment-age">(12 May '22, 09:19)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="84452"></span>
<div id="comment-84452" class="comment">
<div id="post-84452-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>around 2 months ago. replication is working once/day the issue is wide - it has county codes, but missing local city-codes; however, it works on public api.</p>
<p>can this: <a href="https://github.com/osm-search/Nominatim/blob/2d1a22705f7f2f067f2c839c32caf55941a37b01/settings/import-full.style#L18">https://github.com/osm-search/Nominatim/blob/2d1a22705f7f2f067f2c839c32caf55941a37b01/settings/import-full.style#L18</a> difference between address and full import be a culprit?</p>
</div>
<div id="comment-84452-info" class="comment-info">
<span class="comment-age">(12 May '22, 09:22)</span> <span class="comment-user userinfo">mzaw9</span>
</div>
</div>
</div>
<div id="comment-tools-84448" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84448-form-container" class="comment-form-container">
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

<span id="84500"></span>

<div id="answer-container-84500" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84500-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mzaw9 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Quick answer: You need to update the postcode data on your instance with the following command: <code>nominatim refresh --postcode</code>. Make sure that there are no updates running at the same time. The update takes between 20min and an hour, depending on your hardware.</p>
<p>Background: Postcode data is not directly available in OSM. There are only postcodes as part of addresses. To make search for postcodes work, Nominatim takes the postcodes from all the address and computes a centroid point for each of them. This is a rather expensive process, so it is not done as part of the regular updates. You have to occasionally run the process manually using the command above.</p>
<p>Addresses with the postcode '89-501' were first entered in OSM only a couple of weeks ago. That's why your instance does not have them yet. If you have regularly applied updates, the data is there. Recomputing the postcode centroids will make them searchable.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 May '22, 08:34</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-84500" class="comments-container">
<span id="84527"></span>
<div id="comment-84527" class="comment">
<div id="post-84527-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks, that helped; we also automated the refresh to once a day (same as update)</p>
</div>
<div id="comment-84527-info" class="comment-info">
<span class="comment-age">(19 May '22, 14:17)</span> <span class="comment-user userinfo">mzaw9</span>
</div>
</div>
</div>
<div id="comment-tools-84500" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84500-form-container" class="comment-form-container">
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

