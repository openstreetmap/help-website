+++
type = "question"
title = "From rendering db into APIDB"
description = '''Several years ago I&#x27;ve installed the tile server for my own projects and inserted some houses with coordinates  directly into OSM database. After some time my client decided to edit maps using API and I&#x27;ve installed latest API. Now when my client wants to edit maps with JOSM he can&#x27;t see the houses ...'''
date = "2016-07-13T11:23:00Z"
lastmod = "2016-07-15T05:48:00Z"
weight = 50886
keywords = [ "db", "rendering", "api", "apidb", "osm" ]
aliases = [ "/questions/50886" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [From rendering db into APIDB](/questions/50886/from-rendering-db-into-apidb)

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
<span id="post-50886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50886-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Several years ago I've installed the tile server for my own projects and inserted some houses with coordinates directly into OSM database. After some time my client decided to edit maps using API and I've installed latest API. Now when my client wants to edit maps with JOSM he can't see the houses that I've inserted years ago. How to export data from rendering DB into APIDB so that I can see them in JOSM. PS: there are 70k houses</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-db" rel="tag" title="see questions tagged &#39;db&#39;">db</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-apidb" rel="tag" title="see questions tagged &#39;apidb&#39;">apidb</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jul '16, 11:23</strong></p>
<img src="https://secure.gravatar.com/avatar/dad1a4b83b169f8eae00710c41b087b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Black_Corsair&#39;s gravatar image" />
<p><span>Black_Corsair</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Black_Corsair has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '16, 11:57</strong> </span></p>
</div>
</div>
<div id="comments-container-50886" class="comments-container">
<span id="50887"></span>
<div id="comment-50887" class="comment">
<div id="post-50887-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It might be useful to explain a bit more what you're trying to do here. There's typically an awful lot less in a typical rendering database than an apidb.</p>
</div>
<div id="comment-50887-info" class="comment-info">
<span class="comment-age">(13 Jul '16, 11:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50888"></span>
<div id="comment-50888" class="comment">
<div id="post-50888-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Edited my question</p>
</div>
<div id="comment-50888-info" class="comment-info">
<span class="comment-age">(13 Jul '16, 12:46)</span> <span class="comment-user userinfo">Black_Corsair</span>
</div>
</div>
<span id="50899"></span>
<div id="comment-50899" class="comment">
<div id="post-50899-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why don't you export building geometries in your rendering db to some file, which can be loaded/imported by JOSM and then continue populating your API DB via JOSM?</p>
</div>
<div id="comment-50899-info" class="comment-info">
<span class="comment-age">(13 Jul '16, 18:42)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="50903"></span>
<div id="comment-50903" class="comment">
<div id="post-50903-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm new to OSM. Any detailed explanations with some commands will be appreciated.</p>
</div>
<div id="comment-50903-info" class="comment-info">
<span class="comment-age">(14 Jul '16, 07:29)</span> <span class="comment-user userinfo">Black_Corsair</span>
</div>
</div>
<span id="50906"></span>
<div id="comment-50906" class="comment">
<div id="post-50906-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How did you manage to insert some houses directly into the OSM database some years ago?! If you already succeeded in installing a tile server and API DB, you're definitely not new to OSM.</p>
</div>
<div id="comment-50906-info" class="comment-info">
<span class="comment-age">(14 Jul '16, 17:45)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="50914"></span>
<div id="comment-50914" class="comment not_top_scorer">
<div id="post-50914-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I'm not new, but also not a professional, I did it years ago, so I might forgot something. The problem is that I can't export OSM database as a file and then import it into API server, because the OSM database is optimized for tiles rendering only.</p>
</div>
<div id="comment-50914-info" class="comment-info">
<span class="comment-age">(15 Jul '16, 05:48)</span> <span class="comment-user userinfo">Black_Corsair</span>
</div>
</div>
</div>
<div id="comment-tools-50886" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-50886-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

