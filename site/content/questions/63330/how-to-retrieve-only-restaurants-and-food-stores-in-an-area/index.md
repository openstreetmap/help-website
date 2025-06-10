+++
type = "question"
title = "How to retrieve only restaurants and food stores in an area"
description = '''I don&#x27;t need a map, or really show anything. All I need is the ability to put in my longitude and latitude (or address) and get the restaurants or food places in a range of some sort. OpenStreetMap doesn&#x27;t have all of the restaurants but it&#x27;s something, and I&#x27;m going to also be allowing my users to ...'''
date = "2018-05-05T19:34:00Z"
lastmod = "2018-05-06T09:03:00Z"
weight = 63330
keywords = [ "openstreetmap", "api", "store" ]
aliases = [ "/questions/63330" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to retrieve only restaurants and food stores in an area](/questions/63330/how-to-retrieve-only-restaurants-and-food-stores-in-an-area)

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
<span id="post-63330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63330-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I don't need a map, or really show anything. All I need is the ability to put in my longitude and latitude (or address) and get the restaurants or food places in a range of some sort.</p>
<p>OpenStreetMap doesn't have all of the restaurants but it's something, and I'm going to also be allowing my users to enter addresses of things that aren't available and I'll be pushing it onto OpenStreetMap to fill it up more.</p>
<p>Think of something like what FourSquare does. Actually I noticed they used OpenStreetMap as well along with MapBox but when I search on their site, they have most of the places around me.</p>
<p>Is this possible? I've looked all around and I've found things like Google Places API and Here Maps API but they're both pretty expensive and I'm unable to save the data and do as I please (Add ratings and such). MapBox looks great but I think that's more for just creating maps and they don't have actual data on places.</p>
<p>If need be, I'm okay with hosting it on my own server since I assume it will be very small in size as I don't need any information other than the longitude and latitude and name of all the restaurants.</p>
<p>How will I grab just that info?</p>
<p>Thanks!</p>
<p>PS. If you know of a service that does this well, I'm all ears!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-store" rel="tag" title="see questions tagged &#39;store&#39;">store</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 May '18, 19:34</strong></p>
<img src="https://secure.gravatar.com/avatar/11549d7d66032164856aad04bbea914a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ButterScotchPudding&#39;s gravatar image" />
<p><span>ButterScotch...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ButterScotchPudding has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 May '18, 19:40</strong> </span></p>
</div>
</div>
<div id="comments-container-63330" class="comments-container">
&#10;</div>
<div id="comment-tools-63330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63330-form-container" class="comment-form-container">
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

<span id="63331"></span>

<div id="answer-container-63331" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63331-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You may be best served with the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">overpass api</a> (if you want to automate things), or <a href="http://overpass-turbo.eu/">overpass-turbo</a> (<a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">wiki</a>).</p>
<p>There are however lots of other ways of achieving the same thing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '18, 20:31</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 May '18, 20:34</strong> </span></p>
</div>
</div>
<div id="comments-container-63331" class="comments-container">
<span id="63334"></span>
<div id="comment-63334" class="comment">
<div id="post-63334-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! When you say other ways to achieve the same thing, do you mean other OpenStreetMap methods or through other third parties?</p>
</div>
<div id="comment-63334-info" class="comment-info">
<span class="comment-age">(05 May '18, 22:49)</span> <span class="comment-user userinfo">ButterScotch...</span>
</div>
</div>
<span id="63341"></span>
<div id="comment-63341" class="comment">
<div id="post-63341-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Other ways with OSM data, for example you could load it in to a spatial database (Postgres with Postgis for example) or extract them directly from OSM data or ...</p>
</div>
<div id="comment-63341-info" class="comment-info">
<span class="comment-age">(06 May '18, 09:03)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63331-form-container" class="comment-form-container">
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

