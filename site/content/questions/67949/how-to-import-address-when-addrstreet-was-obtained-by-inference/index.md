+++
type = "question"
title = "How to import address when addr:street was obtained by inference?"
description = '''Sometimes we can use &quot;official address database&quot; to import them as nodes, but there are only point (latlong) and addr:housenumber in the official database, the addr:street must be obtained by inference, checking the nearst road or similar heuristic...  There are a tool (software, rules or algorithm)...'''
date = "2019-02-09T14:26:00Z"
lastmod = "2019-02-11T17:25:00Z"
weight = 67949
keywords = [ "import", "interpolation" ]
aliases = [ "/questions/67949" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to import address when addr:street was obtained by inference?](/questions/67949/how-to-import-address-when-addrstreet-was-obtained-by-inference)

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
<span id="post-67949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67949-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Sometimes we can use "official address database" to <a href="https://wiki.openstreetmap.org/wiki/Import">import</a> them as nodes, but there are only <em>point</em> (latlong) and <code>addr:housenumber</code> in the official database, the <code>addr:street</code> must be obtained by <a href="https://en.wikipedia.org/wiki/Statistical_inference">inference</a>, checking the nearst road or similar heuristic...</p>
<p>There are a tool (software, rules or algorithm) to accomplish this process? There are a tag to say <em>"this <code>addr:street</code> was inferred"</em>?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-interpolation" rel="tag" title="see questions tagged &#39;interpolation&#39;">interpolation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '19, 14:26</strong></p>
<img src="https://secure.gravatar.com/avatar/6963015ca2c3146e2a2a348b7fcb793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppKrauss&#39;s gravatar image" />
<p><span>ppKrauss</span><br />
<span class="score" title="95 reputation points">95</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppKrauss has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67949" class="comments-container">
<span id="67966"></span>
<div id="comment-67966" class="comment">
<div id="post-67966-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would say that an object with just addr:housenumber and no addr:street or associatedStreet relation would mostly be considered an error/incomplete data. One could potentially infer the street by proximity, but this would likely lead to lots of errors and wouldn't be a good idea.</p>
</div>
<div id="comment-67966-info" class="comment-info">
<span class="comment-age">(11 Feb '19, 16:47)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="67968"></span>
<div id="comment-67968" class="comment">
<div id="post-67968-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello <a href="https://help.openstreetmap.org/users/8189/alester">@alester</a> yes, "wouldn't be a good idea", but it is not Europe, it is the only official information in many countries of Latim America and Africa... Welcome to the <em>"real world of The Third World"</em>: we are face with the "do nothing" or "do something although partially"... Fortunately with good tools like PostGIS and some statistical methodologies, we can obtain good partial/filtered results, with 99,9% reliability: this question is about tools and techniques used/recommended by the OSM community.</p>
</div>
<div id="comment-67968-info" class="comment-info">
<span class="comment-age">(11 Feb '19, 17:25)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-67949" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67949-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

