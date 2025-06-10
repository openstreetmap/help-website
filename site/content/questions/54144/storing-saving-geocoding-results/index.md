+++
type = "question"
title = "Storing / Saving Geocoding Results"
description = '''Hello everyone! If I use Nominatim to geocode addresses, am I allowed to save the results in my database? This is for an internal application with a very small set of users (20 perhaps). This would not be bulk geocoding, perhaps one request every now and again when a new address is entered within th...'''
date = "2017-01-18T14:50:00Z"
lastmod = "2017-01-18T18:14:00Z"
weight = 54144
keywords = [ "nominatim", "geocoding", "license" ]
aliases = [ "/questions/54144" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Storing / Saving Geocoding Results](/questions/54144/storing-saving-geocoding-results)

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
<span id="post-54144-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54144-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54144-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone! If I use Nominatim to geocode addresses, am I allowed to save the results in my database? This is for an internal application with a very small set of users (20 perhaps). This would not be bulk geocoding, perhaps one request every now and again when a new address is entered within the application. I do see a guideline within the Nominatim usuage policy that says: "Scraping of details The details page is there for debugging only and may not be downloaded automatically."</p>
<p>Is saving a geocode result to an internal database considered scraping?</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jan '17, 14:50</strong></p>
<img src="https://secure.gravatar.com/avatar/bb24c979b793fd252fdb45608e845bba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stillsmallvoice7&#39;s gravatar image" />
<p><span>stillsmallvo...</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stillsmallvoice7 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54144" class="comments-container">
&#10;</div>
<div id="comment-tools-54144" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54144-form-container" class="comment-form-container">
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

<span id="54146"></span>

<div id="answer-container-54146" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54146-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think this is the <a href="http://wiki.openstreetmap.org/wiki/Nominatim_usage_policy">usage policy</a> you are referring to:</p>
<blockquote>
<p><strong>Scraping of details</strong> The details page is there for debugging only and may not be downloaded automatically.</p>
</blockquote>
<p>This applies to the <em>details</em> page. The details page is the page behind the <em>details</em> button when searching at <a href="https://nominatim.openstreetmap.org">https://nominatim.openstreetmap.org</a>, for example this one: <a href="https://nominatim.openstreetmap.org/details.php?place_id=159214550">https://nominatim.openstreetmap.org/details.php?place_id=159214550</a></p>
<p>For automated requests you don't want to parse the details page but use the <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Search">Nominatim API</a> instead. In these cases the other usage policies apply. Performing a request "every now and again" is likely okay as long as you follow all the other policies, too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '17, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54146" class="comments-container">
<span id="54147"></span>
<div id="comment-54147" class="comment">
<div id="post-54147-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! So storage of this geocoded data is basically allowed? I'm having trouble finding this answer.</p>
</div>
<div id="comment-54147-info" class="comment-info">
<span class="comment-age">(18 Jan '17, 17:27)</span> <span class="comment-user userinfo">stillsmallvo...</span>
</div>
</div>
<span id="54149"></span>
<div id="comment-54149" class="comment">
<div id="post-54149-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Of course. Nevertheless the <a href="https://wiki.osmfoundation.org/wiki/Licence">license of OSM</a> applies to this stored data.</p>
</div>
<div id="comment-54149-info" class="comment-info">
<span class="comment-age">(18 Jan '17, 18:14)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-54146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54146-form-container" class="comment-form-container">
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

