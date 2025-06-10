+++
type = "question"
title = "Nominatim lookup by id: admin_level not present on administrative boundaries"
description = '''Nominatim lookup by id: admin_level not present on administrative boundaries Is this by design or am I missing a parameter? My URL: https://nominatim.openstreetmap.org/lookup.php?osm_ids=R113765&amp;amp;polygon_geojson=1&amp;amp;format=json&amp;amp;extratags=1 I there a subsequent call I should make to get the ...'''
date = "2021-03-12T01:43:00Z"
lastmod = "2021-03-12T15:17:00Z"
weight = 79227
keywords = [ "admin_level", "boundary", "nominatim", "administrative" ]
aliases = [ "/questions/79227" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim lookup by id: admin_level not present on administrative boundaries](/questions/79227/nominatim-lookup-by-id-admin_level-not-present-on-administrative-boundaries)

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
<span id="post-79227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79227-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Nominatim lookup by id: admin_level not present on administrative boundaries Is this by design or am I missing a parameter? My URL: <a href="https://nominatim.openstreetmap.org/lookup.php?osm_ids=R113765&amp;polygon_geojson=1&amp;format=json&amp;extratags=1">https://nominatim.openstreetmap.org/lookup.php?osm_ids=R113765&amp;polygon_geojson=1&amp;format=json&amp;extratags=1</a></p>
<p>I there a subsequent call I should make to get the data I need? I should not be calling the details endpoint but that has exactly the data I need</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-admin_level" rel="tag" title="see questions tagged &#39;admin_level&#39;">admin_level</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-administrative" rel="tag" title="see questions tagged &#39;administrative&#39;">administrative</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '21, 01:43</strong></p>
<img src="https://secure.gravatar.com/avatar/4c59b4f7ab13fcad459411d38030acb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TSaldana&#39;s gravatar image" />
<p><span>TSaldana</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TSaldana has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Mar '21, 01:47</strong> </span></p>
</div>
</div>
<div id="comments-container-79227" class="comments-container">
&#10;</div>
<div id="comment-tools-79227" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79227-form-container" class="comment-form-container">
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

<span id="79241"></span>

<div id="answer-container-79241" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79241-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's no further parameter for /lookup.php what would return the field. Entirely possible nobody needed the field so far or used /detail.php. You could request it to be added <a href="https://github.com/osm-search/Nominatim/">https://github.com/osm-search/Nominatim/</a></p>
<p>Alternatively change 'format=json' to 'format=jsonv2' and you'll see a 'place_rank' field. In most cases you can calculate the admin_level from that, e.g. place_rank=16 is admin_level=8</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '21, 15:17</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-79241" class="comments-container">
&#10;</div>
<div id="comment-tools-79241" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79241-form-container" class="comment-form-container">
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

