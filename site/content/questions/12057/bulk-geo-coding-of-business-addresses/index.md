+++
type = "question"
title = "Bulk Geo-coding of Business Addresses"
description = '''Can Open Street Map be used to derive latitude and longitude coordinates to an address provided by the user? If not, thanks anyway, but if so Can it be done in bulk? (I have a few million business listings I need to do this with) If not, thanks anyway, but if so Is there an indicator of the accuracy...'''
date = "2012-04-16T12:40:00Z"
lastmod = "2022-10-10T12:59:00Z"
weight = 12057
keywords = [ "bulk", "search", "geocoding", "geocoder" ]
aliases = [ "/questions/12057" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Bulk Geo-coding of Business Addresses](/questions/12057/bulk-geo-coding-of-business-addresses)

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
<span id="post-12057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12057-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can Open Street Map be used to derive latitude and longitude coordinates to an address provided by the user?</p>
<p><em>If not, thanks anyway, but if so</em></p>
<p>Can it be done in bulk? (I have a few million business listings I need to do this with)</p>
<p><em>If not, thanks anyway, but if so</em></p>
<p>Is there an indicator of the accuracy level which something has been geocoded at? For example, commercial solutions will indicate whether the address specified has been geocoded at a 10 meter level or a 100 meter level or at a town level etc...</p>
<p>Thanks in advance for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bulk" rel="tag" title="see questions tagged &#39;bulk&#39;">bulk</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-geocoder" rel="tag" title="see questions tagged &#39;geocoder&#39;">geocoder</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Apr '12, 12:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a81ca60cf3eea7ef121ce0860c778bf8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Saint%20Jimmy&#39;s gravatar image" />
<p><span>Saint Jimmy</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Saint Jimmy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jan '13, 17:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-12057" class="comments-container">
&#10;</div>
<div id="comment-tools-12057" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12057-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="12058"></span>

<div id="answer-container-12058" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12058-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-12058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap does not offer a service that lets you geocode millions of addresses, but OpenStreetMap has the <em>data</em> that allows you to do this.</p>
<p>You will have to run the software yourself. Check out <a href="http://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a>. Some Linux/database experience will be required to operate it. There's a free Nominatim service by <a href="http://developer.mapquest.com/web/products/open/nominatim">MapQuest</a> but I'm not sure if that can be used for bulk geocoding, check their terms.</p>
<p>The Nominatim result does have an indication of whether a house number was found or not (in which case some location along the street have been guessed), but there's not a precision indicator as such.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '12, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '12, 12:52</strong> </span></p>
</div>
</div>
<div id="comments-container-12058" class="comments-container">
&#10;</div>
<div id="comment-tools-12058" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12058-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85842"></span>

<div id="answer-container-85842" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85842-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85842-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85842-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I highly recommend <a href="https://photon.komoot.io">https://photon.komoot.io</a>! It has no accuracy indicator, but provides a list of potential matches.</p>
<p>I got it set up in minutes and then could geocode away on my local machine simply using curl :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '22, 08:15</strong></p>
<img src="https://secure.gravatar.com/avatar/09f491ff872d3ed578d7e246d1bf30cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xerusf&#39;s gravatar image" />
<p><span>xerusf</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xerusf has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85842" class="comments-container">
&#10;</div>
<div id="comment-tools-85842" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85842-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62392"></span>

<div id="answer-container-62392" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62392-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are free batch geocoders such as <a href="https://geocode.xyz/batch">https://geocode.xyz/batch</a> ; but there are limits on file sizes you can do for free. There is also AWS based geocoders that do the same thing. ( <a href="https://www.google.com/search?q=aws+geocoders">https://www.google.com/search?q=aws+geocoders</a> )</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '18, 16:21</strong></p>
<img src="https://secure.gravatar.com/avatar/30d69959228dbbc64c3b3a8785a7e399?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ERV%20R&#39;s gravatar image" />
<p><span>ERV R</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ERV R has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62392" class="comments-container">
&#10;</div>
<div id="comment-tools-62392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62392-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69833"></span>

<div id="answer-container-69833" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69833-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>TomTom's Geocoder supports address geocoding. You need to specify options.apiKey nominatimmapquest: Same geocoder as openstreetmap, but queries the MapQuest servers. You need to specify options.apiKey</p>
<p><img src="https://help.openstreetmap.org/upfiles/geocoding.PNG" alt="alt text" /></p>
<p>Read all about it here: <a href="https://developer.tomtom.com/blog/decoded/what-geocoding">https://developer.tomtom.com/blog/decoded/what-geocoding</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '19, 22:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a5521ec6394892d7404efd1c45f782a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="russel3k&#39;s gravatar image" />
<p><span>russel3k</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="russel3k has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-69833" class="comments-container">
&#10;</div>
<div id="comment-tools-69833" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69833-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85852"></span>

<div id="answer-container-85852" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85852-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://opencagedata.com/api#confidence">https://opencagedata.com/api#confidence</a> has a confidence indicator. It used OSM and other open data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '22, 12:59</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '22, 13:00</strong> </span></p>
</div>
</div>
<div id="comments-container-85852" class="comments-container">
&#10;</div>
<div id="comment-tools-85852" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85852-form-container" class="comment-form-container">
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

