+++
type = "question"
title = "Search does not find address when city is not municipality"
description = '''Eg this building, which is located in Vionnaz municipality, is tagged with: addr:city Torgon addr:housenumber 90 addr:postcode 1899 addr:street Route de Plan-de-Croix but looking up Route de Plan-de-Croix 90 Torgon in the search field does not give any result. What do I have to change, so that the s...'''
date = "2017-04-25T12:44:00Z"
lastmod = "2017-04-26T06:46:00Z"
weight = 55856
keywords = [ "city", "search", "municipality", "address" ]
aliases = [ "/questions/55856" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Search does not find address when city is not municipality](/questions/55856/search-does-not-find-address-when-city-is-not-municipality)

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
<span id="post-55856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55856-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Eg <a href="https://www.openstreetmap.org/way/489040406">this building</a>, which is located in Vionnaz municipality, is tagged with:</p>
<p><code>addr:city Torgon addr:housenumber 90 addr:postcode 1899 addr:street Route de Plan-de-Croix</code></p>
<p>but looking up <em>Route de Plan-de-Croix 90 Torgon</em> in the search field does not give any result. What do I have to change, so that the search finds the building?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-municipality" rel="tag" title="see questions tagged &#39;municipality&#39;">municipality</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '17, 12:44</strong></p>
<img src="https://secure.gravatar.com/avatar/011f2efc4889b702eedefe6a061cb648?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SelfishSeahorse&#39;s gravatar image" />
<p><span>SelfishSeahorse</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SelfishSeahorse has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55856" class="comments-container">
&#10;</div>
<div id="comment-tools-55856" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55856-form-container" class="comment-form-container">
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

<span id="55857"></span>

<div id="answer-container-55857" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55857-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is reasonably simple, Torgon is defined as a polygon <a href="https://www.openstreetmap.org/way/44418169">https://www.openstreetmap.org/way/44418169</a> which does not include the building you referenced.</p>
<p>You either need to expand the polygon (by adding the additional areas that belong to Torgon to it), or create a place node for Torgon (which will not work as good as a polygon). There may be an effort coming up to add post code areas to OSM in Switzerland see the discussion on the Swiss mailing list, however that will only help with postal cities, not with the multitude of other places.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '17, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-55857" class="comments-container">
<span id="55863"></span>
<div id="comment-55863" class="comment">
<div id="post-55863-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your explanation! However, there are even buildings inside the Torgon polygon - eg <em>Chemin du Four 2 Torgon</em> - that the search cannot find!?</p>
</div>
<div id="comment-55863-info" class="comment-info">
<span class="comment-age">(25 Apr '17, 18:27)</span> <span class="comment-user userinfo">SelfishSeahorse</span>
</div>
</div>
<span id="55864"></span>
<div id="comment-55864" class="comment">
<div id="post-55864-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That would have to be looked at in detail, however there is a completely different issue with that address: it is not from a source that is legal to use in OpenStreetMap and needs to be removed.</p>
</div>
<div id="comment-55864-info" class="comment-info">
<span class="comment-age">(25 Apr '17, 18:33)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="55868"></span>
<div id="comment-55868" class="comment">
<div id="post-55868-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Back to the topic on hand, yes your example fails, but it is found without the place <a href="http://nominatim.openstreetmap.org/details.php?place_id=121822350">http://nominatim.openstreetmap.org/details.php?place_id=121822350</a></p>
<p>On the other hand <a href="http://nominatim.openstreetmap.org/details.php?place_id=119568839">http://nominatim.openstreetmap.org/details.php?place_id=119568839</a> is found with place (Rue de la Lanche 2, Torgon)</p>
<p>Can't explain it right now but that might be due to the time of day.</p>
</div>
<div id="comment-55868-info" class="comment-info">
<span class="comment-age">(25 Apr '17, 22:51)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="55871"></span>
<div id="comment-55871" class="comment">
<div id="post-55871-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nominatim (the search engine behind osm.org website) ignores a lot of address information on the nodes. Basically it takes the house number from the node and uses the street name to look up a nearby road with the same name. Then the rest of the address is taken from information found via the way.</p>
<p>This does not mean that the address information on a node is completely useless, as there might be other geocoders that use that information.</p>
<p>You can find more information about this topic on <a href="https://wiki.openstreetmap.org/wiki/Nominatim/FAQ">https://wiki.openstreetmap.org/wiki/Nominatim/FAQ</a> and <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Development_overview">https://wiki.openstreetmap.org/wiki/Nominatim/Development_overview</a></p>
</div>
<div id="comment-55871-info" class="comment-info">
<span class="comment-age">(26 Apr '17, 06:46)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-55857" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55857-form-container" class="comment-form-container">
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

