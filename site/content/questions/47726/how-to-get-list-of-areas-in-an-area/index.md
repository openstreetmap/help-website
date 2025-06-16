+++
type = "question"
title = "How to get list of areas, in an area?"
description = '''lets say i have an area boundary of a country. now how do i get all the boundaries available in this country? like available state,city, even deeper boundaries? Shorter version of my ques: i need the list of areas(boundaries) inside a country(boundary)?'''
date = "2016-01-29T09:16:00Z"
lastmod = "2016-02-27T08:41:00Z"
weight = 47726
keywords = [ "overpassapi", "overpass", "overpass-api", "overpass-ql" ]
aliases = [ "/questions/47726" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to get list of areas, in an area?](/questions/47726/how-to-get-list-of-areas-in-an-area)

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
<span id="post-47726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47726-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>lets say i have an area boundary of a country. now how do i get all the boundaries available in this country? like available state,city, even deeper boundaries?</p>
<p>Shorter version of my ques: i need the list of areas(boundaries) inside a country(boundary)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '16, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/dfcf9d391ca68ff816e8f9f8ec9f3fc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20Gowtham&#39;s gravatar image" />
<p><span>Arun Gowtham</span><br />
<span class="score" title="0 reputation points">0</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun Gowtham has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47726" class="comments-container">
&#10;</div>
<div id="comment-tools-47726" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47726-form-container" class="comment-form-container">
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

<span id="48373"></span>

<div id="answer-container-48373" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48373-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Search for administrative boundaries using the known area as a filter:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29</a></p>
<p>Take care of the note there, that area(area) is not implemented, so you will need to search for ways and relations, the ones you want are probably tagged with boundary=administrative.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '16, 21:18</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-48373" class="comments-container">
<span id="48384"></span>
<div id="comment-48384" class="comment">
<div id="post-48384-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>To convert a way or relation back to an area (if available), use the <code>map_to_area</code> statement.</p>
</div>
<div id="comment-48384-info" class="comment-info">
<span class="comment-age">(27 Feb '16, 08:40)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-48373" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48373-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48372"></span>

<div id="answer-container-48372" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48372-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a big difference between "areas inside areas" and "boundaries inside boundaries". The first issue is much more general and I will try to answer that one.<br />
Assume an open simple 2D area is a set of all points strictly inside an outer/enclosing border polygon and strictly outside and arbitrary number (including zero) of inner/excluding/hole border polygons. A closed area, besides its inner points, contains all border points as well. You can prove that any complex area, or a set of complex areas, has a perfect coverage of disjunctive simple areas. Therefore, hereafter we consider only simple closed areas.<br />
We can say/define that an area Ab is inside another area Aa if, and only if, any inner or border point of Ab is an inner or border point of Aa. Now the question is how to check this condition efficiently? Here are some hints and suggestions:<br />
Any math/GIS library should contain (almost guaranteed) a function point-polygon(…) that returns one of the values for a given point and polygon: the point is strictly inside, outside or it is exactly on the polygon. Also, the library should contain a function polygon-in-polygon(…) that returns yes or no for two given polygons Pb and Pa. If not, you can make it easily using the point-polygon(…) function. Namely, we can say/define that Pb is inside Pa if any point of Pb is not strictly outside Pa. In addition, you can prove that Pb is inside Pa if, and only if, any of the node points of Pb is not strictly outside Pa and none of the node points of Pa is strictly inside Pb.<br />
Now, using the polygon-in-polygon(…) function you can efficiently check whether and area Ab is inside another area Aa. Namely, you can prove that a given area Ab is inside a given area Aa if, and only if:<br />
1. The outer border polygon Pb of area Ab is inside the outer border polygon Pa of area Aa; and<br />
2. Any hole polygon Ha of area Aa is either inside or outside the outer polygon Pb of area Ab. If inside, then Ha must be inside of a hole polygon Hb of area Ab.<br />
Good luck and enjoy the OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '16, 20:44</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-48372" class="comments-container">
<span id="48385"></span>
<div id="comment-48385" class="comment">
<div id="post-48385-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>As the question was specifically about Overpass API, this seems a bit OT.</p>
</div>
<div id="comment-48385-info" class="comment-info">
<span class="comment-age">(27 Feb '16, 08:41)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-48372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48372-form-container" class="comment-form-container">
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

