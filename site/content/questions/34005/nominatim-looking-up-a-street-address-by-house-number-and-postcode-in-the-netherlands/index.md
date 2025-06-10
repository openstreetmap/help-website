+++
type = "question"
title = "Nominatim: Looking up a street address by house number and postcode in the Netherlands"
description = '''I&#x27;ve installed my own Nominatim instance with the Netherlands database. In the Netherlands it is possible to lookup a street address by entering a house number and postcode. You can verify this at http://postcode.nl by entering the postcode 9718ES and the house number 24, which will return &quot;Melkweg&quot;...'''
date = "2014-06-16T15:05:00Z"
lastmod = "2021-10-18T22:21:00Z"
weight = 34005
keywords = [ "geocoding", "nominatim", "street", "postcode", "address" ]
aliases = [ "/questions/34005" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim: Looking up a street address by house number and postcode in the Netherlands](/questions/34005/nominatim-looking-up-a-street-address-by-house-number-and-postcode-in-the-netherlands)

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
<span id="post-34005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34005-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've installed my own Nominatim instance with the Netherlands database.</p>
<p>In the Netherlands it is possible to lookup a street address by entering a house number and postcode. You can verify this at <a href="http://postcode.nl">http://postcode.nl</a> by entering the postcode 9718ES and the house number 24, which will return "Melkweg" as the street name.</p>
<p>In fact, in most cases it is possible to get the street address just from the postcode (without a house number). This is also possible at postcode.nl.</p>
<p>Nominatim also has this data. E.g. when you search for Melkweg 24 the correct postcode 9718ES is returned. However, when you do a lookup like <code>?q=9718ES 24</code> or <code>?street=24&amp;postcode=9718ES</code> nothing is returned.</p>
<p>Is it possible to perform this lookup with Nominatim, or perhaps Nominatim can be altered to include such logic?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jun '14, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/04361eba6e039eecdd3458e2545f03e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomM&#39;s gravatar image" />
<p><span>TomM</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34005" class="comments-container">
&#10;</div>
<div id="comment-tools-34005" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34005-form-container" class="comment-form-container">
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

<span id="34006"></span>

<div id="answer-container-34006" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34006-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-34006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No this is currently not possible. Postcode systems the world over are all very different and nobody has yet taken the effort to create the code so Nominatim can understand all those systems. There is some generic support for postcodes, but it is very limited.</p>
<p>On top of that Nominatim doesn't really index the address nodes. It indexes the streets (and selected POI's) and then connects the address nodes to the nearby streets with the same name. For the Netherlands the effect of this is, that the only part of the postcode that is in the index are the four numbers. This is however imprecise (and probably incomplete) as this is based on nodes with a certain tag and not on boundaries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jun '14, 15:37</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-34006" class="comments-container">
<span id="34007"></span>
<div id="comment-34007" class="comment">
<div id="post-34007-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you mean that Nominatim never includes the "ES" of the postcode when I search for "9718ES"? If this is the case, how come Nominatim does return "9718ES" when I search for the street address, rather than just "9718"? I would like to patch Nominatim to allow for postcode lookups in the Netherlands (I already forked it), but I have no clue on how its geocoding algorithm currently works. I tried to grasp it in Geocode.php but find it somewhat difficult to understand.</p>
</div>
<div id="comment-34007-info" class="comment-info">
<span class="comment-age">(16 Jun '14, 17:15)</span> <span class="comment-user userinfo">TomM</span>
</div>
</div>
<span id="34009"></span>
<div id="comment-34009" class="comment">
<div id="post-34009-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are <a href="http://overpass-turbo.eu/s/3L7">nodes with the tag "postal_code"</a>. This has in the Netherlands mostly only the 4PP code. Until recently this was basically the only postcode data around here. Now with the BAG data in OSM we have lots of nodes (and ways) with the tag "addr:postcode". However these are only seen as a postcode POI for the indexing when they are included for another reason. E.g. because they are put on an ATM.</p>
<ul>
<li><a href="http://nominatim.openstreetmap.org/details.php?place_id=3666123377">Another Melkweg</a>.</li>
<li><a href="http://nominatim.openstreetmap.org/details.php?place_id=98004972">It's administrative area</a> (only 4 postcode children).</li>
<li><a href="http://nominatim.openstreetmap.org/details.php?place_id=98396126">It's guestimate postcode point</a>.</li>
</ul>
<p>If you search with a housenumber (<a href="http://nominatim.openstreetmap.org/details.php?place_id=9170503075">Melkweg 34, Hellevoetsluis</a>) it notices the addr:postcode on the end result and decides that is better (because explicitly tagged) than the guestimate. Notice the greyed out guestimate and the fact the used postcode has no ID in the index.</p>
<p>On top of all this there is the search string parser. How should it know what is a postcode in the following string: "Melkweg 34 3225VE Hellevoetsluis". It's immediately obvious for a Dutchman, but for a computer it could equally be just a long housenumber.</p>
<p>Sorry, I can't help you with the coding.</p>
</div>
<div id="comment-34009-info" class="comment-info">
<span class="comment-age">(16 Jun '14, 18:21)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="52379"></span>
<div id="comment-52379" class="comment">
<div id="post-52379-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's been two years, the "No this is currently not possible." is still correct?</p>
</div>
<div id="comment-52379-info" class="comment-info">
<span class="comment-age">(06 Oct '16, 13:17)</span> <span class="comment-user userinfo">lucas_steffen</span>
</div>
</div>
<span id="82223"></span>
<div id="comment-82223" class="comment">
<div id="post-82223-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's been seven years. Unfortunately it still isn't possible.</p>
<p><a href="https://help.openstreetmap.org/users/2933/cartinus"></a><a href="https://help.openstreetmap.org/users/2933/cartinus">@cartinus</a>, it can be immediately obvious for a computer too. Four digits followed by two letters can only be a postcode, in the Netherlands. So with RegEx it shouldn't be a problem.</p>
<p>For example:</p>
<hr />
<p>// This will return the postcode IF the address string contains one, IF not it will return an empty string</p>
<p>$address_string = "Melkweg 34 3225VE Hellevoetsluis";</p>
<p>$postcode = preg_match("/\d\d\d\d[a-z][a-z]/i", $address_string, $matches) ? $matches[0] : "";</p>
<p>echo $postcode;</p>
<hr />
<p>The only thing left to do is check if the address country is the Netherlands. Nominatim already seems to be able to do this with just the postcode.</p>
<p>Therefor it's only a matter of implementing it. The code exists, it works, it only needs someone who knows Nominatim to add it.</p>
<p>If you're that someone, please add this option, it would be incredibly useful to us.</p>
</div>
<div id="comment-82223-info" class="comment-info">
<span class="comment-age">(18 Oct '21, 21:17)</span> <span class="comment-user userinfo">WebDev_21</span>
</div>
</div>
<span id="82225"></span>
<div id="comment-82225" class="comment">
<div id="post-82225-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/20920/webdev_21">@WebDev_21</a> you obviously have little idea how OSM software develops, or the resources available to do it. No-one is going to drop everything to implement an obscure tweak just for The Netherlands. Either fork the project and do it yourself submitting a pull request for it to be pulled back into core, or pay someone to do it. Don't tell volunteers "it's only a matter of implementing it", the same is true of nuclear fusion!</p>
</div>
<div id="comment-82225-info" class="comment-info">
<span class="comment-age">(18 Oct '21, 22:21)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-34006" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34006-form-container" class="comment-form-container">
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

