+++
type = "question"
title = "Addresses for POIs spanning multiple buildings"
description = '''I&#x27;ve just come across an issue of mapping a POI which covers several buildings each of which has its own address (Palace Hotel, Tallinn). In Estonia most buildings have been imported with their associated address data from Open Source government data, with the result that address data on buildings i...'''
date = "2013-08-18T22:20:00Z"
lastmod = "2013-08-19T21:46:00Z"
weight = 25561
keywords = [ "building", "hotel", "address", "poi" ]
aliases = [ "/questions/25561" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Addresses for POIs spanning multiple buildings](/questions/25561/addresses-for-pois-spanning-multiple-buildings)

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
<span id="post-25561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25561-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've just come across an issue of mapping a POI which covers several buildings each of which has its own address (<a href="http://www.openstreetmap.org/browse/way/234029034">Palace Hotel, Tallinn</a>). In Estonia most buildings have been imported with their associated address data from Open Source government data, with the result that address data on buildings is very complete and addresses for POIs are less complete. This reverses mapping situations familiar to me.</p>
<p>Although a hotel may include in its footprint several buildings, the actual address of the hotel may be:</p>
<ul>
<li>the housenumber of just one of the buildings (the current case)</li>
<li>just its name and a street name (fairly common in the UK)</li>
<li>a range of housenumbers, typically when all buildings are on the same street</li>
</ul>
<p>The way I have changed the mapping there are now two ways with the same address: the building at that address and the postal address of the hotel. Clearly it is not unreasonable to have a 1:M relationship between an address and other objects, but the way of mapping the hotel area is to potentially create two addresses for a specific building when it only has one.</p>
<p>If this is an issue it will affect data consumers. Can anyone envisage situations where this might cause problems for data consumers?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-hotel" rel="tag" title="see questions tagged &#39;hotel&#39;">hotel</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '13, 22:20</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-25561" class="comments-container">
&#10;</div>
<div id="comment-tools-25561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25561-form-container" class="comment-form-container">
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

<span id="25565"></span>

<div id="answer-container-25565" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25565-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's not uncommon to have the same address data on more than one entity in OSM. Some mappers like to add address data to node-only POIs for completeness, even if several POIs share the same address and even if the building they are in is indeed already mapped and has the same address on its building outline.</p>
<p>In your case, I would collect all buildings (and other detail belonging to the hotel complex) into a <a href="http://wiki.openstreetmap.org/wiki/Relation:site">site relation</a>, map all hotel-relevant details there and include the 'main' postal address of the hotel. I would still keep the addresses on the buildings.</p>
<p>This way you'll get the right address when searching for the hotel, but still retain the addresses of the single buildings should someone need them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '13, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/517667306ad8343f0ce93914517600db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chaos99&#39;s gravatar image" />
<p><span>Chaos99</span><br />
<span class="score" title="531 reputation points">531</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chaos99 has one accepted answer">14%</span></p>
</div>
</div>
<div id="comments-container-25565" class="comments-container">
<span id="25585"></span>
<div id="comment-25585" class="comment">
<div id="post-25585-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is more or less what I did, except I just added the hotel as an additional way rather than as a relation. Subsequently I've noticed many discrete buildings in Tallinn with the same housenumber.</p>
</div>
<div id="comment-25585-info" class="comment-info">
<span class="comment-age">(19 Aug '13, 21:46)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-25565" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25565-form-container" class="comment-form-container">
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

