+++
type = "question"
title = "Postcode brings up wrong country!"
description = '''When looking at postcode NR32 4BF, (This is Lowestoft, Suffolk, UK) OSM brings up a location in Eastern Australia.  How can this be corrected?'''
date = "2019-06-03T16:32:00Z"
lastmod = "2019-06-07T09:14:00Z"
weight = 69430
keywords = [ "country", "wrong", "nominatim", "postcode" ]
aliases = [ "/questions/69430" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Postcode brings up wrong country!](/questions/69430/postcode-brings-up-wrong-country)

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
<span id="post-69430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69430-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When looking at postcode NR32 4BF, (This is Lowestoft, Suffolk, UK) OSM brings up a location in Eastern Australia.</p>
<p>How can this be corrected?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-wrong" rel="tag" title="see questions tagged &#39;wrong&#39;">wrong</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '19, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/e4820d701be90ad61d61355f27c1070b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GiantHD&#39;s gravatar image" />
<p><span>GiantHD</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GiantHD has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jun '19, 15:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-69430" class="comments-container">
&#10;</div>
<div id="comment-tools-69430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69430-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="69439"></span>

<div id="answer-container-69439" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69439-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-69439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can invesigate what's going on using the web interface for the search engine at <a href="https://nominatim.openstreetmap.org">https://nominatim.openstreetmap.org</a></p>
<p>Searching for "NR32 4BF" turns up the road in Australia, because it has an <code>old_ref</code> of "NR32". <a href="https://nominatim.openstreetmap.org/details.php?place_id=167374628">https://nominatim.openstreetmap.org/details.php?place_id=167374628</a> . I think this is because nominatim doesn't recognise the exact postcode - is it new? - and so it tries to find other objects that match either the first or second half of the postcode.</p>
<p>Using the "reverse search" on the same site allows you to find the Aspire Centre and check what nominatim thinks the postcode for that is. <a href="https://nominatim.openstreetmap.org/details.php?place_id=164924374">https://nominatim.openstreetmap.org/details.php?place_id=164924374</a> shows nominatim has computed the postcode as "NR32 4HE". Perhaps the source of the post codes for nominatim is old, or has some inaccuracies.</p>
<p>If you want a deeper dive into how Nominatim works, and how it chooses the search results, then have a look at <a href="http://nominatim.org/release-docs/latest/">http://nominatim.org/release-docs/latest/</a> . Otherwise I would suggest adding the postcode to the correct building.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '19, 09:17</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-69439" class="comments-container">
&#10;</div>
<div id="comment-tools-69439" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69439-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69435"></span>

<div id="answer-container-69435" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69435-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you know the postcode of a house or building it is simple to map. Using iD pick "area"<img src="https://help.openstreetmap.org/upfiles/iD_postcode.JPG" alt="alt text" /> draw the building outline easy with bing harder without. Choose house or building for the polygon you have drawn. Add the postcode. Save it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '19, 08:43</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
</div>
<div id="comments-container-69435" class="comments-container">
<span id="69444"></span>
<div id="comment-69444" class="comment">
<div id="post-69444-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>While doing so you could also add the remaining missing address information of such place.</p>
</div>
<div id="comment-69444-info" class="comment-info">
<span class="comment-age">(04 Jun '19, 13:27)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-69435" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69435-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69431"></span>

<div id="answer-container-69431" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69431-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To search and find an item it needs to be mapped. I tired a few postcodes, my own, that i mapped and some business ones from a magazine, they work if mapped. I guess the one you found means something in Australia but is not mapped yet in the UK. The solution is for us to map any that we know, especially if it is a new build . I seem to remember that the GB postcodes were something that the Royal Mail owned and couldn't be copied in total. More info. <a href="https://wikileaks.org/wiki/UK_government_database_of_all_1,841,177_post_codes_together_with_precise_geographic_coordinates_and_other_information,_8_Jul_2009">https://wikileaks.org/wiki/UK_government_database_of_all_1,841,177_post_codes_together_with_precise_geographic_coordinates_and_other_information,_8_Jul_2009</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '19, 18:03</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '19, 08:56</strong> </span></p>
</div>
</div>
<div id="comments-container-69431" class="comments-container">
&#10;</div>
<div id="comment-tools-69431" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69431-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69475"></span>

<div id="answer-container-69475" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69475-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've mapped the building now, Changeset: 70954094.</p>
<p>How long will it take before the postcode NR32 4BF will appear correctly in searches?</p>
<p>Thanks</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '19, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/e4820d701be90ad61d61355f27c1070b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GiantHD&#39;s gravatar image" />
<p><span>GiantHD</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GiantHD has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69475" class="comments-container">
<span id="69518"></span>
<div id="comment-69518" class="comment">
<div id="post-69518-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>nominatim.openstreetmap.org is usually pretty fast with updating (seconds to hours). The postcode is searchable by now.</p>
</div>
<div id="comment-69518-info" class="comment-info">
<span class="comment-age">(07 Jun '19, 09:14)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-69475" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69475-form-container" class="comment-form-container">
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

