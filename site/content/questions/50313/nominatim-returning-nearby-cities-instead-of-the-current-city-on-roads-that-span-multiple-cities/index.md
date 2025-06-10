+++
type = "question"
title = "Nominatim returning nearby cities instead of the current city on roads that span multiple cities"
description = '''I&#x27;m using the latitude/longitude argument to get the current town the user is in from nominatim, but sometimes when the user is on long roads that span multiple towns it gives a neighboring town instead of the town they are currently in. For example, the coordinates (41.036389, -74.031476) are clear...'''
date = "2016-06-19T16:22:00Z"
lastmod = "2016-06-19T22:12:00Z"
weight = 50313
keywords = [ "cities", "nominatim", "geocoding", "highway" ]
aliases = [ "/questions/50313" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim returning nearby cities instead of the current city on roads that span multiple cities](/questions/50313/nominatim-returning-nearby-cities-instead-of-the-current-city-on-roads-that-span-multiple-cities)

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
<span id="post-50313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50313-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using the latitude/longitude argument to get the current town the user is in from nominatim, but sometimes when the user is on long roads that span multiple towns it gives a neighboring town instead of the town they are currently in. For example, the coordinates (41.036389, -74.031476) are clearly inside the borders of Park Ridge but nominatim says the nearest road, Kinderkamack Road, is located in Woodcliff Lake so the field that returns the town/city in nominatim says the user is in Woodcliff Lake instead of Park Ridge. Is there any way to accurately get the city/town the user is in with nominatim?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '16, 16:22</strong></p>
<img src="https://secure.gravatar.com/avatar/65b0bbd9a3b9c3cfa1e31af84f97ebf5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pdrum1030&#39;s gravatar image" />
<p><span>pdrum1030</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pdrum1030 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '16, 16:24</strong> </span></p>
</div>
</div>
<div id="comments-container-50313" class="comments-container">
&#10;</div>
<div id="comment-tools-50313" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50313-form-container" class="comment-form-container">
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

<span id="50323"></span>

<div id="answer-container-50323" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50323-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the Nominatim database each street section (way) is linked to one parent only. During reverse geocoding it's not re-evaluated if the coordinate might be in a different parent (city). Setting &amp;zoom=10 (city level) limits the output and takes shortcuts in the search logic but has the same behavior. If there were houses on that street or the street split at the city boundary the result would be better, I don't recommend changing OSM data over this though. Currently it's a limitation (bug) in Nominatim, in worst case if a street crosses country borders it even returns the wrong country.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '16, 22:12</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-50323" class="comments-container">
&#10;</div>
<div id="comment-tools-50323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50323-form-container" class="comment-form-container">
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

