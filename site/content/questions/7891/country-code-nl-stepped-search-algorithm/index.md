+++
type = "question"
title = "Country code NL + stepped search algorithm"
description = '''Hi, I&#x27;m new here so I hope this question is to the right audience. I&#x27;m developing software that wants to use the nominatim API for geocoding. We have all the technicalities solved, and get satisfactory results as long as the entered address data is correct. But of course there are situations where t...'''
date = "2011-09-15T10:23:00Z"
lastmod = "2011-09-16T09:19:00Z"
weight = 7891
keywords = [ "openstreetmap", "country", "nominatim", "geocoding" ]
aliases = [ "/questions/7891" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Country code NL + stepped search algorithm](/questions/7891/country-code-nl-stepped-search-algorithm)

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
<span id="post-7891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7891-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm new here so I hope this question is to the right audience.</p>
<p>I'm developing software that wants to use the nominatim API for geocoding. We have all the technicalities solved, and get satisfactory results as long as the entered address data is correct. But of course there are situations where the address data we send to nominatim is incorrect. We now have an algorithm as follows: 1) try to get the geocode for street + house number, city, (state,) country code (we add state only for US addresses) 2) if 1 fails, try to get the geocode for city, (state,) country code 3) if 2 fails, try to get the geocode for (state,) country code</p>
<p>Unfortunately I can only use country codes, no country names.</p>
<p>Now I have two questions:</p>
<ul>
<li>When we get to step 3 for The Netherlands (code NL), (<a href="http://nominatim.openstreetmap.org/search?q=,,,NL&amp;format=xml)">http://nominatim.openstreetmap.org/search?q=,,,NL&amp;format=xml)</a> we get this geocode (lat="49.4026367037741" lon="-0.234108765413479") which is in the Atlantic next to France. This looks like an OpenStreetMap data problem. Can this be resolved somehow?</li>
<li>The 1-2-3 logic above perhaps is way to simple. On the other hand, trying to find a geocode on increasing less-precise level until you succeed sounds like a generic solution. Isn't such a feature available standard in nominatim?</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '11, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/b98e1f9c0bc31e2a0059d90912e27154?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msol&#39;s gravatar image" />
<p><span>msol</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msol has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7891" class="comments-container">
&#10;</div>
<div id="comment-tools-7891" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7891-form-container" class="comment-form-container">
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

<span id="7897"></span>

<div id="answer-container-7897" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7897-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-7897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Regarding the Netherlands: Nominatim is giving the location based on <a href="https://www.openstreetmap.org/browse/relation/47796">relation 47796</a>. This includes the 'mainland' part (in Europe), as well as several islands in the Caribbean. These are all part of the country of the Netherlands, so it appears the OSM data is actually correct. But it seems Nominatim is calculating the centre point of all of this, which is somewhere in the Atlantic.</p>
<p>I don't know whether this should be mapped or tagged differently. Maybe Nominatim could somehow calculate the centre of just the mainland part. Or use the location of the node with role admin_centre. This should probably be discussed on the appropriate mailing lists.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '11, 13:47</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-7897" class="comments-container">
<span id="7921"></span>
<div id="comment-7921" class="comment">
<div id="post-7921-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. Funny to be punished for colonialism even today :-) So, what are the "appropriate mailing lists" to address this issue? (Sorry, I'm a newbee here.)</p>
</div>
<div id="comment-7921-info" class="comment-info">
<span class="comment-age">(16 Sep '11, 09:19)</span> <span class="comment-user userinfo">msol</span>
</div>
</div>
</div>
<div id="comment-tools-7897" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7897-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7901"></span>

<div id="answer-container-7901" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7901-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you can accept solutions next to Nominatim's geocoding, have a look at <strong>Navit</strong> or <strong>OsmAnd</strong> (both opensourced) how they can find their addresses and how they output if some locations fail.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '11, 18:17</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-7901" class="comments-container">
&#10;</div>
<div id="comment-tools-7901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7901-form-container" class="comment-form-container">
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

