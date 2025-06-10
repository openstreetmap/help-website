+++
type = "question"
title = "gb postcodes data and searching"
description = '''I&#x27;m trying to use Nominatim to get the Lat/Long for GB Postcodes and struggling. To avoid pounding on OpenStreetMaps&#x27;s servers I&#x27;ve setup my own Nominatim with the gb_postcode_data but it doesn&#x27;t seem to get used. If I query like so: wget -O - -q &quot;http://mynominatim.somewhere/search?format=xml&amp;amp;p...'''
date = "2015-01-14T11:36:00Z"
lastmod = "2015-01-14T18:22:00Z"
weight = 40341
keywords = [ "searching", "gb", "postcodes" ]
aliases = [ "/questions/40341" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [gb postcodes data and searching](/questions/40341/gb-postcodes-data-and-searching)

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
<span id="post-40341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40341-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to use Nominatim to get the Lat/Long for GB Postcodes and struggling. To avoid pounding on OpenStreetMaps's servers I've setup my own Nominatim with the gb_postcode_data but it doesn't seem to get used.</p>
<p>If I query like so:</p>
<p><em>wget -O - -q "http://mynominatim.somewhere/search?format=xml&amp;postalcode=KA2 9AE&amp;country=gb"</em></p>
<p>I get no result (same result if I use nominatim.openstreetmap.org for the above query).</p>
<p><em>wget -O - -q "http://mynominatim.somewhere/search?format=xml&amp;postcode=KA2 9AE&amp;country=gb"</em></p>
<p>I get no result (using nominatim.openstreetmap.org I get a place in the Lake District returned).</p>
<p><em>wget -O - -q "http://mynominatim.somewhere/search?format=xml&amp;q=KA2 9AE&amp;country=gb"</em></p>
<p>Returns a place in Wales but the KA2 9AE postcode is in Dundonald, Scotland (the same query on nominatim.openstreetmap.org returns no result). However using "PE8 6XH" as the postcode in the above query I get sensible results from both the official and my nominatim. Huh?</p>
<p>I've checked and "KA2 9AE" is in the gb_postcode_data.sql.gz file so why's it not being used? Why the different results from 'my' nominatim and the official one?</p>
<p>I'm probably doing something stupid but I can't work out what. Enlightenment would be greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-searching" rel="tag" title="see questions tagged &#39;searching&#39;">searching</span> <span class="post-tag tag-link-gb" rel="tag" title="see questions tagged &#39;gb&#39;">gb</span> <span class="post-tag tag-link-postcodes" rel="tag" title="see questions tagged &#39;postcodes&#39;">postcodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jan '15, 11:36</strong></p>
<img src="https://secure.gravatar.com/avatar/245a6d5e9436ee948ea50719bfdd84dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ruffle&#39;s gravatar image" />
<p><span>ruffle</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ruffle has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40341" class="comments-container">
<span id="40350"></span>
<div id="comment-40350" class="comment">
<div id="post-40350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The result you are getting for the 2nd query is simply the centroid for the GB admin boundary polygon. What I know about nominatim the postcode support is minimal and likely you should be asking the developers directly (aka opening an issue).</p>
</div>
<div id="comment-40350-info" class="comment-info">
<span class="comment-age">(14 Jan '15, 14:07)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="40357"></span>
<div id="comment-40357" class="comment">
<div id="post-40357-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the advice, new issue opened:</p>
<p><a href="https://github.com/twain47/Nominatim/issues/221">https://github.com/twain47/Nominatim/issues/221</a></p>
<p>When I get an answered I'll update this page.</p>
</div>
<div id="comment-40357-info" class="comment-info">
<span class="comment-age">(14 Jan '15, 17:09)</span> <span class="comment-user userinfo">ruffle</span>
</div>
</div>
</div>
<div id="comment-tools-40341" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40341-form-container" class="comment-form-container">
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

<span id="40362"></span>

<div id="answer-container-40362" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40362-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40362-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40362-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you just want postcode centroids, then Nominatim is probably not the best tool for the job. You can download the centroids for free from Ordnance Survey's <a href="http://www.ordnancesurvey.co.uk/business-and-government/products/code-point-open.html">OpenData initiative</a>, which will be much more complete than the equivalent data in OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '15, 18:22</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-40362" class="comments-container">
&#10;</div>
<div id="comment-tools-40362" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40362-form-container" class="comment-form-container">
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

