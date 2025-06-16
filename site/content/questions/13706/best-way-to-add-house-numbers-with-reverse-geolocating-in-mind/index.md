+++
type = "question"
title = "Best way to add house numbers with reverse geolocating in mind?"
description = '''How is a good way to add house numbers when the house building is not shown and in such a way that reverse geolocating will find it later?  Specifically, it seems to me that a X,Y point will not work and what is needed is a polygon showing the general shape of either the house or house&#x27;s property. G...'''
date = "2012-06-21T20:54:00Z"
lastmod = "2013-11-30T18:27:00Z"
weight = 13706
keywords = [ "addressing", "reversegeocoding", "editing", "address" ]
aliases = [ "/questions/13706" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Best way to add house numbers with reverse geolocating in mind?](/questions/13706/best-way-to-add-house-numbers-with-reverse-geolocating-in-mind)

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
<span id="post-13706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13706-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How is a good way to add house numbers when the house building is not shown and in such a way that reverse geolocating will find it later?</p>
<p>Specifically, it seems to me that a X,Y point will not work and what is needed is a polygon showing the general shape of either the house or house's property. Google maps can reverse geolocate addresses by dragging a marker to the house property and I would like to add addresses in a way that also does that.</p>
<p>From what I'm seeing, many in OSM would like specific points for addresses, like front doors, but I would like areas, for future reverse geolocating. Any ideas? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-addressing" rel="tag" title="see questions tagged &#39;addressing&#39;">addressing</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '12, 20:54</strong></p>
<img src="https://secure.gravatar.com/avatar/af8387f11be652a161c9771b36caf25b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidLR&#39;s gravatar image" />
<p><span>DavidLR</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidLR has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '13, 15:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-13706" class="comments-container">
&#10;</div>
<div id="comment-tools-13706" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13706-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="13707"></span>

<div id="answer-container-13707" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13707-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-13707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You don't have to add a building outline. If you know lat and lon of the address, it is enough to <a href="https://wiki.openstreetmap.org/wiki/Potlatch_2/Primer">add</a> a node with the <a href="https://wiki.openstreetmap.org/wiki/Addr">addr</a> key. Adding a whole <a href="https://wiki.openstreetmap.org/wiki/Buildings">building</a> just allows to draw a nice looking map but is not required for finding the address.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '12, 21:01</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-13707" class="comments-container">
<span id="13708"></span>
<div id="comment-13708" class="comment">
<div id="post-13708-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I'm trying to wrap my head around this 'node' thing. Let's say I add a node with the addr key, then come back some time when it's been updated into OpenStreetMap and I'm reverse geolocating by dragging a marker across a zoomed-in map. When will I enter the boundary for this address? As I continue dragging, when will I exit ? I'm working on a website that uses reverse geolocating, in addition to having users add addresses.</p>
</div>
<div id="comment-13708-info" class="comment-info">
<span class="comment-age">(21 Jun '12, 21:19)</span> <span class="comment-user userinfo">DavidLR</span>
</div>
</div>
<span id="13711"></span>
<div id="comment-13711" class="comment">
<div id="post-13711-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I really don't understand what boundary you want to add and what it has to do with addresses and reverse geolocating. Please explain it.</p>
</div>
<div id="comment-13711-info" class="comment-info">
<span class="comment-age">(21 Jun '12, 21:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="13712"></span>
<div id="comment-13712" class="comment">
<div id="post-13712-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By 'boundary' I mean the edges of that property. Assume a portion of a street has 5 houses on each side. As I drag a mouse along each side of the street on a map, I want each address to show up as I pass over that property.</p>
</div>
<div id="comment-13712-info" class="comment-info">
<span class="comment-age">(21 Jun '12, 22:11)</span> <span class="comment-user userinfo">DavidLR</span>
</div>
</div>
<span id="13714"></span>
<div id="comment-13714" class="comment">
<div id="post-13714-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Reverse geocoding tools will usually just choose the address closest to your position. This works with either nodes or building outlines.</p>
</div>
<div id="comment-13714-info" class="comment-info">
<span class="comment-age">(22 Jun '12, 01:29)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="13721"></span>
<div id="comment-13721" class="comment">
<div id="post-13721-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>You have to understand that OSM contributors can specify addresses on 'nodes' or 'areas' where the area is usually a building footprint. It is very unusal to map house properties (parcels) in OSM. So you will have anyway many empty 'areas' without any address, you will have to find out the closest one (either a node or a building).</p>
</div>
<div id="comment-13721-info" class="comment-info">
<span class="comment-age">(22 Jun '12, 12:13)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-13707" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13707-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28624"></span>

<div id="answer-container-28624" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28624-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you do not have the outlines of the building add a simple one (four corners) tag the adress and add something like "note=outline to be checked"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '13, 18:27</strong></p>
<img src="https://secure.gravatar.com/avatar/83e18b36cdfac8da38cdf30d141151d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hfst&#39;s gravatar image" />
<p><span>hfst</span><br />
<span class="score" title="306 reputation points">306</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hfst has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28624" class="comments-container">
&#10;</div>
<div id="comment-tools-28624" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28624-form-container" class="comment-form-container">
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

