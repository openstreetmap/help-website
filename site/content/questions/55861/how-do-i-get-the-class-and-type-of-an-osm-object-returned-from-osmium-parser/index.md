+++
type = "question"
title = "How do I get the class and type of an osm-object returned from osmium parser ?"
description = '''Hello. I am using node-osmium for parsing a .pbf file. It works pretty well but I am missing some information: class and type of the osm-object e.g. class=amenity, type=parking These are available in objects I get e.g with overpass or nominatim. My question ist, if this information is simply not ava...'''
date = "2017-04-25T15:07:00Z"
lastmod = "2017-04-26T12:54:00Z"
weight = 55861
keywords = [ "osmium", "openstreetmap", "pbf" ]
aliases = [ "/questions/55861" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I get the class and type of an osm-object returned from osmium parser ?](/questions/55861/how-do-i-get-the-class-and-type-of-an-osm-object-returned-from-osmium-parser)

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
<span id="post-55861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55861-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello.</p>
<p>I am using node-osmium for parsing a .pbf file. It works pretty well but I am missing some information: class and type of the osm-object e.g. class=amenity, type=parking</p>
<p>These are available in objects I get e.g with overpass or nominatim.</p>
<p>My question ist, if this information is simply not available in the returned object, or if I did not find the correct method to receive it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '17, 15:07</strong></p>
<img src="https://secure.gravatar.com/avatar/d001d4c331042ef1dade5af6ed5f7ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="autumnus&#39;s gravatar image" />
<p><span>autumnus</span><br />
<span class="score" title="121 reputation points">121</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="autumnus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55861" class="comments-container">
&#10;</div>
<div id="comment-tools-55861" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55861-form-container" class="comment-form-container">
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

<span id="55867"></span>

<div id="answer-container-55867" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55867-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="autumnus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap objects don't have a "class" and "type". Rather, they can have any number of tags and values. Nominatim simplifies that into a "class" and "type" - for example, something tagged <code>building=house</code> will boil down to class=building, type=house in Nominatim. Nominatim tries to guess what the "important" thing is about the object but if something is tagged <code>amenity=place_of_worship</code> and <code>shop=books</code> at the same time, Nominatim will have to choose and neither choice is "clearly correct". Overpass doesn't do this; it returns the full list of tags and their values, just as Osmium does. Osmium exposes the tags through the "tags" and "get_value_by_key" methods on the Object class, see: <a href="https://github.com/osmcode/libosmium/blob/master/include/osmium/osm/object.hpp#L324-L337">https://github.com/osmcode/libosmium/blob/master/include/osmium/osm/object.hpp#L324-L337</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '17, 22:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '17, 08:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-55867" class="comments-container">
<span id="55885"></span>
<div id="comment-55885" class="comment">
<div id="post-55885-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I new about the functions "tags()" and "get_value_by_key()" and I recognized that Nominatim sometimes has two lines in its database with the same osm_id and different class and type. The fact, that the class and type are somehow "calculated" is new to me. That helps a lot and saves me time, as I don't have to search any more :-) Thanks!</p>
</div>
<div id="comment-55885-info" class="comment-info">
<span class="comment-age">(26 Apr '17, 12:54)</span> <span class="comment-user userinfo">autumnus</span>
</div>
</div>
</div>
<div id="comment-tools-55867" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55867-form-container" class="comment-form-container">
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

