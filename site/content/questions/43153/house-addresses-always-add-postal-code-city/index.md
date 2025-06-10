+++
type = "question"
title = "House addresses: Always add postal code + city?"
description = '''Is it necessary to add the postal code (zip) and city fields in the address of an house? I see the reason for street and house number, but city and zip should be discoverable from the surrounding areas. Also, it&#x27;s tedious to fill that fields again and again for each house in a street.'''
date = "2015-05-21T19:22:00Z"
lastmod = "2015-05-26T08:31:00Z"
weight = 43153
keywords = [ "house", "address" ]
aliases = [ "/questions/43153" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [House addresses: Always add postal code + city?](/questions/43153/house-addresses-always-add-postal-code-city)

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
<span id="post-43153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43153-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-43153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it necessary to add the postal code (zip) and city fields in the address of an house?</p>
<p>I see the reason for street and house number, but city and zip should be discoverable from the surrounding areas. Also, it's tedious to fill that fields again and again for each house in a street.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-house" rel="tag" title="see questions tagged &#39;house&#39;">house</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 May '15, 19:22</strong></p>
<img src="https://secure.gravatar.com/avatar/9e263681488308e5e5d5e548b2f9bc99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cweiske&#39;s gravatar image" />
<p><span>cweiske</span><br />
<span class="score" title="156 reputation points">156</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cweiske has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '15, 21:46</strong> </span></p>
</div>
</div>
<div id="comments-container-43153" class="comments-container">
&#10;</div>
<div id="comment-tools-43153" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43153-form-container" class="comment-form-container">
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

<span id="43157"></span>

<div id="answer-container-43157" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43157-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-43157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cweiske has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You mention ZIP code rather than postal code so I assume you are in the United States. Turns out that US ZIP codes are based on lists of addresses and don't always map nicely into areas. So putting the ZIP code on each address is a good thing.</p>
<p>Regarding the city, if the object is within the boundary relation for a town or city then the data consumers should be able to figure that out. However there are times when the postal address does not match the city or town boundaries and in those cases you should put the city into the address too.</p>
<p>I don't know what editor you are using but at least one (JOSM) allows you to select your changed objects and, one selected, you can apply the city and/or ZIP to all of them in one operation. Assuming, of course that it is appropriate to do so.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '15, 20:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-43157" class="comments-container">
<span id="43161"></span>
<div id="comment-43161" class="comment">
<div id="post-43161-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>I'm actually located in germany and editing german data :) And I'm using the web editor (iD). I've updated the post to read "postal code" now.</p>
</div>
<div id="comment-43161-info" class="comment-info">
<span class="comment-age">(21 May '15, 21:45)</span> <span class="comment-user userinfo">cweiske</span>
</div>
</div>
<span id="43168"></span>
<div id="comment-43168" class="comment">
<div id="post-43168-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Germany has a complete set of administrative boundaries and postal code boundaries. So there is no need to map them again. Unfortunately not all data consumers can handle those boundaries. See <a href="http://forum.openstreetmap.org/viewtopic.php?id=23238">this topic</a> on the German forum</p>
</div>
<div id="comment-43168-info" class="comment-info">
<span class="comment-age">(22 May '15, 16:37)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="43215"></span>
<div id="comment-43215" class="comment">
<div id="post-43215-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>re: wording of "postal code" vs "zip", perhaps it depends on what dialect of English the person has learned :)</p>
</div>
<div id="comment-43215-info" class="comment-info">
<span class="comment-age">(26 May '15, 08:31)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
</div>
<div id="comment-tools-43157" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43157-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43158"></span>

<div id="answer-container-43158" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43158-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Of course, if the city or zip boundaries have been mapped as areas correctly, it becomes redundant to add this information as it is retrievable based on where the building is located</p>
<p>e.g. <a href="http://www.openstreetmap.org/search?query=1%20Corrib%20Park#map=19/53.28173/-9.07195">this search</a> shows the full address string but if you look at the <a href="http://www.openstreetmap.org/way/207248053">building itself</a>, it only has the addr:housenumber and addr:street tagging applied</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '15, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/9f0faef4659de616c82f448ff3f4e8e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaCor&#39;s gravatar image" />
<p><span>DaCor</span><br />
<span class="score" title="1339 reputation points"><span>1.3k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaCor has one accepted answer">2%</span></p>
</div>
</div>
<div id="comments-container-43158" class="comments-container">
&#10;</div>
<div id="comment-tools-43158" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43158-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43154"></span>

<div id="answer-container-43154" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43154-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>cweiske, zip and city fields are unmistakable part of the address of a building, apartments or companies. Read these lines as well <a href="http://wiki.openstreetmap.org/wiki/Addresses">http://wiki.openstreetmap.org/wiki/Addresses</a> - the zip, house number and country code are enough to get to the right address - not every router uses all elements of the address code - so add all the available address elements into OSM</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '15, 20:18</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-43154" class="comments-container">
<span id="43155"></span>
<div id="comment-43155" class="comment">
<div id="post-43155-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Depending on the editor you're using, you can apply the same street, city, and zipcode to many nodes and then simply go through them editing the housenumbers. In JOSM [ctrl]-R repeats tagging. Select all the nodes you're working with by [shift]clicking on each, then hit [ctrl]-R to apply the tags. I think Potlatch has the same shortcut.</p>
</div>
<div id="comment-43155-info" class="comment-info">
<span class="comment-age">(21 May '15, 20:42)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-43154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43154-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43179"></span>

<div id="answer-container-43179" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43179-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Adding zip codes or postal codes to each addr: object CAN be helpful:</p>
<p>There are some quality check tools that try to find any OSM objects with addr:postcode=12354 that are in an area (postalcode boundary relation) with postal_code=12345.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '15, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-43179" class="comments-container">
<span id="43182"></span>
<div id="comment-43182" class="comment">
<div id="post-43182-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>USPS ZIP codes are based on postal routes and are not necessarily bound geographically in any reasonable fashion. Census ZIPs try to approximate the geographic boundaries of the USPS ZIPs, but don't always line up (and include large areas that the USPS does not). Census ZIPs aren't used in addresses, though, USPS ZIPs are.</p>
</div>
<div id="comment-43182-info" class="comment-info">
<span class="comment-age">(24 May '15, 11:23)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-43179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43179-form-container" class="comment-form-container">
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

