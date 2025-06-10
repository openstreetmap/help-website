+++
type = "question"
title = "Get data using Overpass API"
description = '''Hello, I use the Overpass API to get osm data. I use this query from this link: http://overpass-turbo.eu/s/cQQ Whe I ran it, it generated only nodes and ways and not relations.  How can I please modify this query in order to download an osm file which containes nodes, ways and relations?'''
date = "2015-11-30T13:53:00Z"
lastmod = "2015-11-30T15:44:00Z"
weight = 46905
keywords = [ "overpass-turbo", "osm" ]
aliases = [ "/questions/46905" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get data using Overpass API](/questions/46905/get-data-using-overpass-api)

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
<span id="post-46905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46905-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I use the Overpass API to get osm data. I use this query from this link:</p>
<p><a href="http://overpass-turbo.eu/s/cQQ">http://overpass-turbo.eu/s/cQQ</a></p>
<p>Whe I ran it, it generated only nodes and ways and not relations. How can I please modify this query in order to download an osm file which containes nodes, ways and relations?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '15, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/b408abbe87d5551cc26d19f0bb74b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MyriamBah&#39;s gravatar image" />
<p><span>MyriamBah</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MyriamBah has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46905" class="comments-container">
<span id="46906"></span>
<div id="comment-46906" class="comment">
<div id="post-46906-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>cross-posted on the French mailing list: <a href="https://lists.openstreetmap.org/pipermail/talk-fr/2015-November/078876.html">https://lists.openstreetmap.org/pipermail/talk-fr/2015-November/078876.html</a> . There I explained that when there are no relations with tags fulfilling the conditions specified in the Overpass query, no relations will be returned.</p>
</div>
<div id="comment-46906-info" class="comment-info">
<span class="comment-age">(30 Nov '15, 14:18)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="46907"></span>
<div id="comment-46907" class="comment">
<div id="post-46907-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why are relations needed in your specific example? Your current question reads like "I need the number of legs of humans, dogs and snakes". But snakes usually don't have any legs. Likewise, amenity=bicycle_rental is <a href="https://taginfo.openstreetmap.org/tags/amenity=bicycle_rental">usually not mapped as relation</a>.</p>
</div>
<div id="comment-46907-info" class="comment-info">
<span class="comment-age">(30 Nov '15, 15:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="46908"></span>
<div id="comment-46908" class="comment">
<div id="post-46908-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are 27 mapped as relations according to <a href="https://taginfo.openstreetmap.org/tags/amenity=bicycle_rental">https://taginfo.openstreetmap.org/tags/amenity=bicycle_rental</a> . That may be a mistagging, but they do exist.</p>
</div>
<div id="comment-46908-info" class="comment-info">
<span class="comment-age">(30 Nov '15, 15:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46905" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46905-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

