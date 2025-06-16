+++
type = "question"
title = "How does OpenStreetMap queries Nominatim"
description = '''When searching for &quot;London Eye&quot; on Open Street Map I get 3 results from Nominatim (1 attraction + 2 bus stops): OSM - London Eye. When I do the same search on Nominatim I only get 2 results (2 bus stops): Nominatim - London Eye. This is consistent with the results I get when I use the Nominatim API....'''
date = "2015-06-03T22:44:00Z"
lastmod = "2015-06-04T10:12:00Z"
weight = 43389
keywords = [ "openstreetmap", "nominatim", "api" ]
aliases = [ "/questions/43389" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How does OpenStreetMap queries Nominatim](/questions/43389/how-does-openstreetmap-queries-nominatim)

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
<span id="post-43389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43389-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When searching for "London Eye" on Open Street Map I get 3 results from Nominatim (1 attraction + 2 bus stops): <a href="https://www.openstreetmap.org/search?query=london%20eye&amp;xhr=1">OSM - London Eye</a>.</p>
<p>When I do the same search on Nominatim I only get 2 results (2 bus stops): <a href="http://nominatim.openstreetmap.org/search.php?q=London+Eye&amp;viewbox=-101.78%2C54.06%2C101.78%2C-54.06">Nominatim - London Eye</a>. This is consistent with the results I get when I use the Nominatim API.</p>
<p>Why are the results different? Shouldn't OSM be showing the same results as the Nominatim API?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '15, 22:44</strong></p>
<img src="https://secure.gravatar.com/avatar/b5ce394e21b680a20fa8747c026d2482?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brunocostalopes&#39;s gravatar image" />
<p><span>brunocostalopes</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brunocostalopes has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43389" class="comments-container">
<span id="43394"></span>
<div id="comment-43394" class="comment">
<div id="post-43394-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Both have a "more results" button. However the order (i.e. importance) of the search results still differs.</p>
</div>
<div id="comment-43394-info" class="comment-info">
<span class="comment-age">(04 Jun '15, 07:25)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="43396"></span>
<div id="comment-43396" class="comment">
<div id="post-43396-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I believe the "more results" is actually doing a new query. if you query the API directly you will only get 2 results.</p>
</div>
<div id="comment-43396-info" class="comment-info">
<span class="comment-age">(04 Jun '15, 08:11)</span> <span class="comment-user userinfo">brunocostalopes</span>
</div>
</div>
<span id="43397"></span>
<div id="comment-43397" class="comment">
<div id="post-43397-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, after digging around a bit more, I now suspect that the OSM website is actually using the Mapquest servers, not sure if anyone can confirm that? That would explain the different results and I guess the question of why the Mapquest Nominatim Search Service does not match the OSM Nominatim is for a different forum.</p>
</div>
<div id="comment-43397-info" class="comment-info">
<span class="comment-age">(04 Jun '15, 10:12)</span> <span class="comment-user userinfo">brunocostalopes</span>
</div>
</div>
</div>
<div id="comment-tools-43389" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43389-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

