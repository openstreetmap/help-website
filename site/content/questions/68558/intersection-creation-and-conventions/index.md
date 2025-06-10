+++
type = "question"
title = "intersection creation and conventions"
description = '''if this is a duplicate please link to answers or documentation when closing. 39.862359, -86.122204 is a dual carriage way intersection. I want to make this intersection searchable as a destination, i.e. type in &quot;kessler and keystone&quot; and have it show up as an option. I think this level of convenienc...'''
date = "2019-03-30T22:19:00Z"
lastmod = "2019-04-12T09:50:00Z"
weight = 68558
keywords = [ "intersection", "junction" ]
aliases = [ "/questions/68558" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [intersection creation and conventions](/questions/68558/intersection-creation-and-conventions)

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
<span id="post-68558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68558-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>if this is a duplicate please link to answers or documentation when closing.</p>
<p>39.862359, -86.122204 is a dual carriage way intersection.</p>
<p>I want to make this intersection searchable as a destination, i.e. type in "kessler and keystone" and have it show up as an option. I think this level of convenience is a necessity for open street maps. I assume the way to achieve this is to create some open street map "point". This is how I did it, and I am making this post to ask if I did it correctly because I am still unsure after looking at documentation. I did not want to name a street light node, because I dont like that solution and its not nice and symmetric.</p>
<ul>
<li>I created a point in the center of the intersection.</li>
<li>junction = yes</li>
<li>address::city</li>
<li>address::postcode</li>
<li>name = kessler boulevard and keystone avenue</li>
</ul>
<p><a href="https://nominatim.openstreetmap.org/details.php?osmtype=N&amp;osmid=6371398592&amp;class=junction">https://nominatim.openstreetmap.org/details.php?osmtype=N&amp;osmid=6371398592&amp;class=junction</a></p>
<p>One issue: After entering all this I am satisfied, except, if I type in "Kessler and Keystone" it shows up fine, however if i enter "Kessler and Keystone, Indianapolis" the search results do not list it. Any advice on where I can work to resolve this?</p>
<p>Thank you for your time, Rick</p>
<p>relevant documentation:</p>
<ol>
<li><a href="https://wiki.openstreetmap.org/wiki/Named_spots_instead_of_street_names">https://wiki.openstreetmap.org/wiki/Named_spots_instead_of_street_names</a></li>
<li><a href="https://help.openstreetmap.org/questions/50982/how-to-name-intersections">https://help.openstreetmap.org/questions/50982/how-to-name-intersections</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Junctions">https://wiki.openstreetmap.org/wiki/Junctions</a></li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-junction" rel="tag" title="see questions tagged &#39;junction&#39;">junction</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Mar '19, 22:19</strong></p>
<img src="https://secure.gravatar.com/avatar/f18844202962b4d8003d464e71f4ae6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OpenMapsRH&#39;s gravatar image" />
<p><span>OpenMapsRH</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OpenMapsRH has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Mar '19, 02:04</strong> </span></p>
</div>
</div>
<div id="comments-container-68558" class="comments-container">
<span id="68567"></span>
<div id="comment-68567" class="comment">
<div id="post-68567-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems that Nominatim (the geocode / search engine) does not know that the junction is in Indianapolis: <a href="https://nominatim.openstreetmap.org/details.php?place_id=257785410">https://nominatim.openstreetmap.org/details.php?place_id=257785410</a> The address tag is probably ignored, and it lists the junction in Dawnbury, Marion County</p>
<p>Some questions that have to be answered, are the admin boundaries correct in that area? Is the nearest street (from which the city is taken) passing through Dawnbury?</p>
</div>
<div id="comment-68567-info" class="comment-info">
<span class="comment-age">(01 Apr '19, 04:47)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-68558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68558-form-container" class="comment-form-container">
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

<span id="68588"></span>

<div id="answer-container-68588" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68588-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-68588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Rick,</p>
<p>I can totally understand your desire to find a junction by stating the two intersecting road names. But it should be up to the search engine to support that.</p>
<p>I find it a terribly bad idea to name junctions like this. If a junction had a proper name different from the street names this would be a different case (like in the first link you gave). But in your case you are merely duplicating the information that already exists: the two roads are in fact intersecting (here is a junction) plus the two names (on the intersecting ways) are already there.</p>
<p>So what happens if we started mapping all intersections with an additional (or existing tagged) node with the "x and y" naming scheme?</p>
<ol>
<li>it will clutter the editor with countless new nodes.</li>
<li>these nodes will have to be maintained: if a street name changes (granted, does not happen that often) one needs to make sure to also change the junction node.</li>
<li>proper junction names (i.e. different from road names) are indistinguishable from "x and y" names.</li>
<li>maps that want to display proper junction names now have to somehow exclude the "x and y" names they find in the data to not render the map unreadable.</li>
</ol>
<p>I would argue that "Kessler and Keystone" is not even a name. When you say "let's meet at the pub at Kessler and Keystone", this is merely an abbreviation for saying "let's meet at the pub at the intersection of Kessler and Keystone".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '19, 17:43</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-68588" class="comments-container">
<span id="68589"></span>
<div id="comment-68589" class="comment">
<div id="post-68589-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There's a long-standing issue to support this in Nominatim, OSM's default geocoder (search), but as yet no-one has stepped up to the plate to implement it: <a href="https://github.com/openstreetmap/Nominatim/issues/123">https://github.com/openstreetmap/Nominatim/issues/123</a> (and dupe <a href="https://github.com/openstreetmap/Nominatim/issues/1224)">https://github.com/openstreetmap/Nominatim/issues/1224)</a></p>
</div>
<div id="comment-68589-info" class="comment-info">
<span class="comment-age">(01 Apr '19, 18:13)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="68672"></span>
<div id="comment-68672" class="comment">
<div id="post-68672-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>TZorn I agree with everything in your post. Richard, I am excited to see if I can help resolve the issue you linked to. This is something I have wanted to help implement for a while. Thank both of you for taking the time to read and respond.</p>
</div>
<div id="comment-68672-info" class="comment-info">
<span class="comment-age">(06 Apr '19, 01:20)</span> <span class="comment-user userinfo">OpenMapsRH</span>
</div>
</div>
<span id="68767"></span>
<div id="comment-68767" class="comment">
<div id="post-68767-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16438/openmapsrh">@OpenMapsRH</a>: thanks for getting involved in the Nominatim issue resolution.</p>
</div>
<div id="comment-68767-info" class="comment-info">
<span class="comment-age">(12 Apr '19, 09:50)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-68588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68588-form-container" class="comment-form-container">
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

