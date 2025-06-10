+++
type = "question"
title = "Import data to Nominatim for reverse geocoding API purpose only querying up to city level"
description = '''I am building a Nominatim server which will serve as reverse geocoding api server. Only city/state(province)/country information are required in the api result. The street/road level information are not required. For example, the server will give result: http://localhost/nominatim/reverse?lat=43.815...'''
date = "2016-11-23T18:48:00Z"
lastmod = "2016-11-24T15:54:00Z"
weight = 53088
keywords = [ "nominatim", "osmosis" ]
aliases = [ "/questions/53088" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Import data to Nominatim for reverse geocoding API purpose only querying up to city level](/questions/53088/import-data-to-nominatim-for-reverse-geocoding-api-purpose-only-querying-up-to-city-level)

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
<span id="post-53088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53088-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am building a Nominatim server which will serve as reverse geocoding api server. Only city/state(province)/country information are required in the api result. The street/road level information are not required.</p>
<p>For example, the server will give result: <a href="http://localhost/nominatim/reverse?lat=43.815031&amp;lon=-79.716834">http://localhost/nominatim/reverse?lat=43.815031&amp;lon=-79.716834</a></p>
<p>{ city:Brampton; state:Ontario; country:Canada }</p>
<p>I would like to use osmosis to filter the data before I import the whole planet data. What command line should I use for this purpose? How about the one below? Thank you.</p>
<h1 id="filter-relations-by-administrative">filter relations by administrative</h1>
<p><em>osmosis --read-pbf planet-latest.osm.pbf --tf accept-relations boundary=administrative --used-way --used-node --lp --write-pbf import1.osm.pbf</em></p>
<h1 id="filter-ways-by-administrative">filter ways by administrative</h1>
<p><em>osmosis --read-pbf planet-latest.osm.pbf --tf accept-ways boundary=administrative --used-node --tf reject-relations --lp --write-pbf import2.osm.pbf</em></p>
<h1 id="merge-all-files-together">merge all files together</h1>
<p><em>osmosis --read-pbf import1.osm.pbf --read-pbf import2.osm.pbf --merge --write-pbf import.osm.pbf</em></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Nov '16, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/b672df800641ade552d1b53512b9bcaa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CQG&#39;s gravatar image" />
<p><span>CQG</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CQG has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Nov '16, 19:43</strong> </span></p>
</div>
</div>
<div id="comments-container-53088" class="comments-container">
&#10;</div>
<div id="comment-tools-53088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53088-form-container" class="comment-form-container">
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

<span id="53095"></span>

<div id="answer-container-53095" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53095-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should also include all nodes/relations with the <code>place</code> tag because in countries with less coverage cities are often just nodes without boundaries.</p>
<p><a href="http://taginfo.openstreetmap.org/keys/?key=place#values">http://taginfo.openstreetmap.org/keys/?key=place#values</a> Not all values are interesting, try <code>'state','county','district','city','territorial','town','island'</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Nov '16, 11:08</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-53095" class="comments-container">
<span id="53098"></span>
<div id="comment-53098" class="comment">
<div id="post-53098-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good point. Thank you so much.</p>
</div>
<div id="comment-53098-info" class="comment-info">
<span class="comment-age">(24 Nov '16, 15:54)</span> <span class="comment-user userinfo">CQG</span>
</div>
</div>
</div>
<div id="comment-tools-53095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53095-form-container" class="comment-form-container">
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

