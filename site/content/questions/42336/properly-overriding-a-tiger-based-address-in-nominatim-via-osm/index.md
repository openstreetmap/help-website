+++
type = "question"
title = "Properly Overriding a Tiger-based address in Nominatim via OSM"
description = '''Here&#x27;s the situation: Searching OSM (and getting Nominatim results) for &quot;99 Railroad Ave, Albany NY&quot; gives a number of results. Two of them relevant to this discussion, the ones in zipcodes 12204 and 12205 have virtually the same USPS mailing addresses (99 Railroad Ave, Albany NY 1220x). The problem...'''
date = "2015-04-15T07:27:00Z"
lastmod = "2015-04-16T11:15:00Z"
weight = 42336
keywords = [ "tiger", "nominatim", "address" ]
aliases = [ "/questions/42336" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Properly Overriding a Tiger-based address in Nominatim via OSM](/questions/42336/properly-overriding-a-tiger-based-address-in-nominatim-via-osm)

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
<span id="post-42336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42336-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Here's the situation: Searching OSM (and getting Nominatim results) for "99 Railroad Ave, Albany NY" gives a number of results. Two of them relevant to this discussion, the ones in zipcodes 12204 and 12205 have virtually the same USPS mailing addresses (99 Railroad Ave, Albany NY 1220x). The problem is that 99 Railroad Ave in Menands, doesn't actually exist -- it's a figment of the US Census Bureau Tiger Data's imagination. (Many roads in the village are numbered 1-99 incorrectly in Tiger.)</p>
<p>My question is this - trying to correct the Railroad Ave addresses in 12204 -- how do I go about updating OSM in such a way as to override the (bad) Tiger data? For reference, the only actual address on that road in Menands is 32, for which I have placed a numbered building, but it doesn't stop the other 98 bad Tiger addresses from showing up in searches.</p>
<p>(Some background -- in the real world this Tiger data, which I've submitted a request to fix, we believe to be the cause of great confusion for those looking for the Real 99 Railroad Ave in zipcode 12205. Apparently searching in a fruit-named company's map for this address w/o the zipcode will return the Menands address first. As a result we have tractor trailers full of lumber supplies (or worse) trying to navigate turns that are near-impossible. To date we've lost count of the number of street signs run over, and a tree was even knocked into a house by one truck.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiger" rel="tag" title="see questions tagged &#39;tiger&#39;">tiger</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '15, 07:27</strong></p>
<img src="https://secure.gravatar.com/avatar/b90895fa8af92827a13cf081b18789a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Daroz&#39;s gravatar image" />
<p><span>Daroz</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Daroz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42336" class="comments-container">
<span id="42337"></span>
<div id="comment-42337" class="comment">
<div id="post-42337-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So you are not referring to wrong OSM data but to additional Tiger data Nominatim is using for answering US geocoding requests?</p>
</div>
<div id="comment-42337-info" class="comment-info">
<span class="comment-age">(15 Apr '15, 07:54)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="42370"></span>
<div id="comment-42370" class="comment">
<div id="post-42370-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's correct. Think of a road segment with a small number of actual addresses (be it buildings or lots), but the Tiger data has some seemingly larger superset of addresses applying to that same range -- with the Tiger data being incorrect.</p>
<p>If the reverse were true (a larger number of real addresses and a small incorrect subset in Tiger) you could "fix" it in OSM by enumerating nodes/buildings for each correct address, effectively overriding the bad data.</p>
<p>The problem is how to override data that exists in Tiger that shouldn't be there?</p>
</div>
<div id="comment-42370-info" class="comment-info">
<span class="comment-age">(16 Apr '15, 03:32)</span> <span class="comment-user userinfo">Daroz</span>
</div>
</div>
</div>
<div id="comment-tools-42336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42336-form-container" class="comment-form-container">
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

<span id="42338"></span>

<div id="answer-container-42338" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42338-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-42338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Daroz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I doubt that there is any solution outside of deleting the bad data from the input TIGER dataset/from the data in the nominatim database which in principle is possible and might be interesting in other situations too (for example in places like NYC where we have complete address data).</p>
<p>I expect that we need to let the nominatim devs sleep a bit on the issue and see if they can come up with something that scales and is maintainable.</p>
<p>See <a href="https://github.com/twain47/Nominatim/issues/262">https://github.com/twain47/Nominatim/issues/262</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '15, 08:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '15, 09:17</strong> </span></p>
</div>
</div>
<div id="comments-container-42338" class="comments-container">
<span id="42371"></span>
<div id="comment-42371" class="comment">
<div id="post-42371-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's an interesting idea but the conundrum is if we accept that the Tiger data in a given segment is out of date, how do we propagate that fact via OSM? If a Nominatim server operator could remove the Tiger data it would help - for that server and that instance, but not necessarily all. Really throwing a wrench into this discussion is what happens should the reverse be true - Tiger gets updated faster than OSM?</p>
</div>
<div id="comment-42371-info" class="comment-info">
<span class="comment-age">(16 Apr '15, 03:54)</span> <span class="comment-user userinfo">Daroz</span>
</div>
</div>
<span id="42375"></span>
<div id="comment-42375" class="comment">
<div id="post-42375-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I suspect any solution that the devs come up with will have a public black list for the TIGER data with other words anybody using TIGER data with OSM could remove the same data for their nominatim instance (or even for a different geocoder). The rest of your points are probably out of scope in the sense that our primary interest is OSM and if OSM is out of date then obviously the community in the area in question has to get its act together.</p>
</div>
<div id="comment-42375-info" class="comment-info">
<span class="comment-age">(16 Apr '15, 11:15)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42338" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42338-form-container" class="comment-form-container">
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

