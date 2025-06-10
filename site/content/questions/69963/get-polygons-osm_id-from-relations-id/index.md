+++
type = "question"
title = "Get polygon&#x27;s osm_id from relation&#x27;s id"
description = '''Hello, I&#x27;m going to use Photon as a search engine. In a result, Photon give the id of the node / way / relation. How can I get the associated point / roads / polygon in my OSM DB (I don&#x27;t have a Nominatim DB)? Is it always -1*&amp;lt;id&amp;gt;? Am I sure to get a result? Thanks in advance'''
date = "2019-07-10T12:41:00Z"
lastmod = "2019-07-10T15:13:00Z"
weight = 69963
keywords = [ "relation", "photon", "id", "polygon" ]
aliases = [ "/questions/69963" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get polygon's osm_id from relation's id](/questions/69963/get-polygons-osm_id-from-relations-id)

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
<span id="post-69963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69963-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm going to use Photon as a search engine. In a result, Photon give the id of the node / way / relation.</p>
<p>How can I get the associated point / roads / polygon in my OSM DB (I don't have a Nominatim DB)? Is it always -1*&lt;id&gt;? Am I sure to get a result?</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-photon" rel="tag" title="see questions tagged &#39;photon&#39;">photon</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '19, 12:41</strong></p>
<img src="https://secure.gravatar.com/avatar/2a936bbff59e8151128d083b194a0fd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tim%20Autin&#39;s gravatar image" />
<p><span>Tim Autin</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tim Autin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69963" class="comments-container">
&#10;</div>
<div id="comment-tools-69963" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69963-form-container" class="comment-form-container">
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

<span id="69964"></span>

<div id="answer-container-69964" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69964-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tim Autin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ul>
<li>If Photon gives you a node, it will either be in planet_osm_point with its ID, or not present at all.</li>
<li>If Photon gives you a way, it will either be in planet_osm_line with its ID, or in planet_osm_polygon with its ID, nor not present at all.</li>
<li>If Photon gives you a relation, it will either be in planet_osm_line with -ID, or in planet_osm_polygon with -ID, or not present at all.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '19, 12:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-69964" class="comments-container">
<span id="69965"></span>
<div id="comment-69965" class="comment">
<div id="post-69965-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for the very clear answer! The links between relations/line, relations/polygons, way/line &amp; node/point are still a bit obscure to me. If a relation is updated/deleted/added, does the polygon (or line) also get updated/deleted/added?</p>
</div>
<div id="comment-69965-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 12:49)</span> <span class="comment-user userinfo">Tim Autin</span>
</div>
</div>
<span id="69966"></span>
<div id="comment-69966" class="comment">
<div id="post-69966-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you do process updates with your database (<code>osm2pgsql -a</code>), then yes, the polygon or line will get updated when the relation changes.</p>
</div>
<div id="comment-69966-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 15:13)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69964" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69964-form-container" class="comment-form-container">
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

