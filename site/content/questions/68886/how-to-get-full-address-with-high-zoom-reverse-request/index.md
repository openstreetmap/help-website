+++
type = "question"
title = "How to get full address with high zoom reverse request?"
description = '''Revers geocoding with high zoom level doesn&#x27;t return the full address. for example city is missed in this request zoom = 14 while zooming out shows the missing city field zoom = 10 so my question is how to get the full address with high zoom levels?'''
date = "2019-04-23T13:27:00Z"
lastmod = "2019-04-23T14:22:00Z"
weight = 68886
keywords = [ "reversegeocoding", "reverse", "zoom" ]
aliases = [ "/questions/68886" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get full address with high zoom reverse request?](/questions/68886/how-to-get-full-address-with-high-zoom-reverse-request)

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
<span id="post-68886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68886-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Revers geocoding with high zoom level doesn't return the full address. for example city is missed in this request</p>
<p><a href="https://nominatim.openstreetmap.org/reverse?lat=10.2986952&amp;lon=123.9557301&amp;format=json&amp;zoom=14">zoom = 14</a></p>
<p>while zooming out shows the missing city field</p>
<p><a href="https://nominatim.openstreetmap.org/reverse?lat=10.2986952&amp;lon=123.9557301&amp;format=json&amp;zoom=10">zoom = 10</a></p>
<p><strong>so my question is</strong> how to get the full address with high zoom levels?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '19, 13:27</strong></p>
<img src="https://secure.gravatar.com/avatar/4133acd2a994938b45ac147d2e0c1437?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nagy&#39;s gravatar image" />
<p><span>Nagy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nagy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68886" class="comments-container">
&#10;</div>
<div id="comment-tools-68886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68886-form-container" class="comment-form-container">
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

<span id="68887"></span>

<div id="answer-container-68887" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68887-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim doesn't know how big the city is. The OSM data only contains the center point (node) of the city <a href="https://www.openstreetmap.org/node/534548619">https://www.openstreetmap.org/node/534548619</a> On zoom level 14 it find a smaller feature (island) and doesn't know it belongs to a city. On zoom level 10 it ignores all smaller features and looks for the nearest city more of less by distance (in other words the algorithm is guessing).</p>
<p>Adding a boundary (OSM relation) like <a href="https://www.openstreetmap.org/relation/30005">https://www.openstreetmap.org/relation/30005</a> for the city helps. Alternatively setting <code>is_in</code> tags to the suburbs and islands belonging to the city <a href="https://wiki.openstreetmap.org/wiki/Key:is_in">https://wiki.openstreetmap.org/wiki/Key:is_in</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '19, 13:58</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-68887" class="comments-container">
<span id="68889"></span>
<div id="comment-68889" class="comment">
<div id="post-68889-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the response, but how can I achieve that with the reverse get call? ex: <a href="https://nominatim.openstreetmap.org/reverse?lat=10.2986952&amp;lon=123.9557301&amp;format=json&amp;zoom=14">https://nominatim.openstreetmap.org/reverse?lat=10.2986952&amp;lon=123.9557301&amp;format=json&amp;zoom=14</a></p>
</div>
<div id="comment-68889-info" class="comment-info">
<span class="comment-age">(23 Apr '19, 14:19)</span> <span class="comment-user userinfo">Nagy</span>
</div>
</div>
<span id="68890"></span>
<div id="comment-68890" class="comment">
<div id="post-68890-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nominatim doesn't know how big the city is. Somebody needs to add more data to the OSM database first.</p>
</div>
<div id="comment-68890-info" class="comment-info">
<span class="comment-age">(23 Apr '19, 14:22)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-68887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68887-form-container" class="comment-form-container">
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

