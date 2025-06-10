+++
type = "question"
title = "What is the best way to download shapefiles for large amount of Nominatim Place Ids?"
description = '''Hi, for a project, I have been collecting a large amount of (about 110k) nominatim bounding boxes and corresponding Place IDs over the span of about a year.  I now need to get the actual geometry from OSM for as many of these as I can. I have thought about using the OSM bulk downloads from data prov...'''
date = "2021-06-10T14:48:00Z"
lastmod = "2021-06-11T12:34:00Z"
weight = 80520
keywords = [ "bulk", "shapefile", "nominatim", "ids" ]
aliases = [ "/questions/80520" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What is the best way to download shapefiles for large amount of Nominatim Place Ids?](/questions/80520/what-is-the-best-way-to-download-shapefiles-for-large-amount-of-nominatim-place-ids)

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
<span id="post-80520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80520-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>for a project, I have been collecting a large amount of (about 110k) nominatim bounding boxes and corresponding Place IDs over the span of about a year.</p>
<p>I now need to get the actual geometry from OSM for as many of these as I can. I have thought about using the OSM bulk downloads from data providers such as geofabrik. However, these of course do not have the nominatim identifier but rather the more general OSM identifier (which I am aware is also not stable).</p>
<p>I could also just query the IDs with nominatim again but, if possible, I would want to query such a large amount of data from OSM as do not want to overburden the servers with too many requests.</p>
<p>I would appreciate any suggestion on how to best approach this to keep the server load as minimal as possible.</p>
<p>Thank you so much in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bulk" rel="tag" title="see questions tagged &#39;bulk&#39;">bulk</span> <span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-ids" rel="tag" title="see questions tagged &#39;ids&#39;">ids</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jun '21, 14:48</strong></p>
<img src="https://secure.gravatar.com/avatar/608289a49f79fc0b01c186d197b8005c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FDenker&#39;s gravatar image" />
<p><span>FDenker</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FDenker has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80520" class="comments-container">
<span id="80528"></span>
<div id="comment-80528" class="comment">
<div id="post-80528-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For large scale queries either <a href="https://nominatim.org/release-docs/latest/admin/Installation/">install Nominatim on a local server</a> or use a <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Alternatives_.2F_Third-party_providers">third-party provider</a> or a <a href="https://switch2osm.org/providers/">paid-for provider</a>.</p>
</div>
<div id="comment-80528-info" class="comment-info">
<span class="comment-age">(11 Jun '21, 09:34)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-80520" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80520-form-container" class="comment-form-container">
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

<span id="80521"></span>

<div id="answer-container-80521" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80521-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="FDenker has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Place id is not a permanent id, it's not even the same between multiple servers. They also change after a reimport and there was one in the last 12 months. <a href="https://nominatim.org/release-docs/develop/api/Output/#place_id-is-not-a-persistent-id">https://nominatim.org/release-docs/develop/api/Output/#place_id-is-not-a-persistent-id</a></p>
<p>The /lookup API endpoint <a href="https://nominatim.org/release-docs/latest/api/Lookup/">https://nominatim.org/release-docs/latest/api/Lookup/</a> doesn't support place id search, only the /details API endpoint <a href="https://nominatim.org/release-docs/latest/api/Details/">https://nominatim.org/release-docs/latest/api/Details/</a> does. Note the disclaimer " You may not use it in scripts or to automatically query details about a result. "</p>
<p>Using osm_type+osm_id as identifier is better. Those ids might still change but with old data dumps and tools one can usually find out what an old id was referring to.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '21, 15:51</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jun '21, 17:29</strong> </span></p>
</div>
</div>
<div id="comments-container-80521" class="comments-container">
<span id="80522"></span>
<div id="comment-80522" class="comment">
<div id="post-80522-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As per usage policy, the details API is definitely off limits for this: <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> (see section 'Uacceptable Use')</p>
</div>
<div id="comment-80522-info" class="comment-info">
<span class="comment-age">(10 Jun '21, 16:46)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="80530"></span>
<div id="comment-80530" class="comment">
<div id="post-80530-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answers. I checked our data again and found that I was mistaken in my belief that we have the Place IDs. We actually do have the OSM ids. I will create another thread because I am still confused as to what these OSM ids actually mean.</p>
</div>
<div id="comment-80530-info" class="comment-info">
<span class="comment-age">(11 Jun '21, 12:34)</span> <span class="comment-user userinfo">FDenker</span>
</div>
</div>
</div>
<div id="comment-tools-80521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80521-form-container" class="comment-form-container">
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

