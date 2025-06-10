+++
type = "question"
title = "place_id help with partially wrong information"
description = '''I&#x27;m new to OSM and am using it to perform a GPS coordinates to Address Query. A few of the queries come back incorrect which I would like to fix, the physical location on the map looks correct in the editor, but the query result is not. How do I bring up the place ID for editing which I guess is whe...'''
date = "2020-08-19T00:27:00Z"
lastmod = "2020-08-20T21:43:00Z"
weight = 76200
keywords = [ "place_id", "editor" ]
aliases = [ "/questions/76200" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [place_id help with partially wrong information](/questions/76200/place_id-help-with-partially-wrong-information)

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
<span id="post-76200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76200-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OSM and am using it to perform a GPS coordinates to Address Query. A few of the queries come back incorrect which I would like to fix, the physical location on the map looks correct in the editor, but the query result is not. How do I bring up the place ID for editing which I guess is where I need to look for the incorrect data? The place_id is 102283291 which is returned after a GPS query at a hospital site in New Zealand. The Hospital name is correct, but most of the address is incorrect which I'd like to edit.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-place_id" rel="tag" title="see questions tagged &#39;place_id&#39;">place_id</span> <span class="post-tag tag-link-editor" rel="tag" title="see questions tagged &#39;editor&#39;">editor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '20, 00:27</strong></p>
<img src="https://secure.gravatar.com/avatar/b5ce48feb9a545b262f72bc02821ef5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sheppy99&#39;s gravatar image" />
<p><span>sheppy99</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sheppy99 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '20, 00:27</strong> </span></p>
</div>
</div>
<div id="comments-container-76200" class="comments-container">
&#10;</div>
<div id="comment-tools-76200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76200-form-container" class="comment-form-container">
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

<span id="76205"></span>

<div id="answer-container-76205" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76205-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It appears that you have stumbled on a bug in Nominatim; the address of that hospital seems to have some random bits in it that make no sense. I have reported that to the Nominatim admin asking to look into it.</p>
<p>Generally speaking:</p>
<p>Sometimes an object in OSM has an explicit address (i.e. we record "this object has this housenumber, this street, this postal code, this city"). This is described here: <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/House_numbers/Karlsruhe_Schema.">https://wiki.openstreetmap.org/wiki/Proposed_features/House_numbers/Karlsruhe_Schema.</a> If such tags are wrong they can simply be corrected on the object itself.</p>
<p>More often than not, and this is also the case here, at least some parts of an address will be inferred - e.g. the post code from a post code boundary, the city name from a city boundary and so on. In these cases, if that data is wrong, it is good good to fix the incorrect polygons as they will apply to more than just that one object.</p>
<p>A <code>place_id</code> is always specific to one particular instance of the Nominatim geocoder. Your place id comes from OSM's Nominatim instance: <a href="https://nominatim.openstreetmap.org/ui/details.html?place_id=102283291">https://nominatim.openstreetmap.org/ui/details.html?place_id=102283291</a> and you can see how the address is constructed there. It starts with "North Island" because there apparently was pedestrian area by that name encompassing the hospital; this seems to be an issue with Nominatim since there isn't (any longer) a "pedestrian area" tag on NZ's North Island. Probably this was a glitch in the data that has been fixed in the data a while ago and Nominatim hasn't updated. From this initial problem follow a couple other mis-assignments that make little sense. But normally, in a non-buggy scenario, you would find in this list a proper hierarchy going from the suburb or city quarter up to the country.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '20, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '20, 09:16</strong> </span></p>
</div>
</div>
<div id="comments-container-76205" class="comments-container">
<span id="76206"></span>
<div id="comment-76206" class="comment">
<div id="post-76206-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Fixed in the Nominatim database. Unfortunately I slightly overdid it and removed the hospital as well. What was the name of the hospital again?</p>
</div>
<div id="comment-76206-info" class="comment-info">
<span class="comment-age">(19 Aug '20, 09:51)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-76205" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76205-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76224"></span>

<div id="answer-container-76224" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76224-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks very much for the insight. From casual observation of a few malformed address lookups that have long since left the logs I'd guess there are a few of these in that suburb. After I wrote the initial reply I see that the bug has been fixed - thanks! Currently <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/House_numbers/Karlsruhe_Schema.">https://wiki.openstreetmap.org/wiki/Proposed_features/House_numbers/Karlsruhe_Schema.</a> takes me to an empty page, and <a href="https://nominatim.openstreetmap.org/ui/details.html?place_id=102283291">https://nominatim.openstreetmap.org/ui/details.html?place_id=102283291</a> returns Error fetching results from /details.php?place_id=102283291&amp;addressdetails=1&amp;hierarchy=0&amp;group_hierarchy=1&amp;polygon_geojson=1&amp;format=json Is that correct?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '20, 23:38</strong></p>
<img src="https://secure.gravatar.com/avatar/b5ce48feb9a545b262f72bc02821ef5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sheppy99&#39;s gravatar image" />
<p><span>sheppy99</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sheppy99 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '20, 23:43</strong> </span></p>
</div>
</div>
<div id="comments-container-76224" class="comments-container">
<span id="76225"></span>
<div id="comment-76225" class="comment">
<div id="post-76225-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/2921/lonvia">@lonvia</a> It was 'North Shore Hospital'</p>
</div>
<div id="comment-76225-info" class="comment-info">
<span class="comment-age">(19 Aug '20, 23:41)</span> <span class="comment-user userinfo">sheppy99</span>
</div>
</div>
<span id="76228"></span>
<div id="comment-76228" class="comment">
<div id="post-76228-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As said above, I accidentally deleted the hospital from the Nominatim database which is why you got the error. Now reinstated: <a href="https://nominatim.openstreetmap.org/ui/details.html?osmtype=W&amp;osmid=58379525">https://nominatim.openstreetmap.org/ui/details.html?osmtype=W&amp;osmid=58379525</a></p>
</div>
<div id="comment-76228-info" class="comment-info">
<span class="comment-age">(20 Aug '20, 07:53)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="76245"></span>
<div id="comment-76245" class="comment">
<div id="post-76245-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much, its working now</p>
</div>
<div id="comment-76245-info" class="comment-info">
<span class="comment-age">(20 Aug '20, 21:43)</span> <span class="comment-user userinfo">sheppy99</span>
</div>
</div>
</div>
<div id="comment-tools-76224" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76224-form-container" class="comment-form-container">
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

