+++
type = "question"
title = "Is adding POIs to a OSM-map on a private website already a &quot;Derived Database&quot;?"
description = '''Hello, I browsed through the ODbL , but somehow, I am still not sure whether I got it right. Please, could you help me w.r.t. how the terms of the licence apply to my project? If I incorporate a map/tile of OpenStreetMap into my own (publicly available) website (let&#x27;s say, using  Leaflet&#x27;s API) and ...'''
date = "2020-12-28T18:27:00Z"
lastmod = "2020-12-29T11:16:00Z"
weight = 78087
keywords = [ "license", "poi" ]
aliases = [ "/questions/78087" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is adding POIs to a OSM-map on a private website already a "Derived Database"?](/questions/78087/is-adding-pois-to-a-osm-map-on-a-private-website-already-a-derived-database)

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
<span id="post-78087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78087-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I browsed through the ODbL , but somehow, I am still not sure whether I got it right. Please, could you help me w.r.t. how the terms of the licence apply to my project?</p>
<p>If I incorporate a map/tile of OpenStreetMap into my own (publicly available) website (let's say, using Leaflet's API) and enhance it by adding markers (pins) for POI of my own (e.g. sculptures which I took photographs of) like on this webpage: <a href="http://u-dreher.de/skulpturenwege/de9/96190_untermerzbach.html">http://u-dreher.de/skulpturenwege/de9/96190_untermerzbach.html</a> : would this usage trigger the ODbl share-alike terms? I would not use any latitude/longitude data of OSM - the sculptures (POIs) would be geocoded by myself. The website would just use the map of OSM.</p>
<p>Clearly, the latitude/longitude data would be publicly available through the HTML source code of my page. Hence, my questions is: is this already a "Derived Database"? Would the geo-coordinates of the POI (that I geocoded myself) then under Share-Alike? I.e. be part of OSM?</p>
<p>Clarifications would be warmly welcome - thank you!</p>
<p>Best regards, Thomas</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Dec '20, 18:27</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef2f7a59886f1a702bf6bcab7ebde81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thomasew&#39;s gravatar image" />
<p><span>thomasew</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thomasew has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78087" class="comments-container">
&#10;</div>
<div id="comment-tools-78087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78087-form-container" class="comment-form-container">
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

<span id="78093"></span>

<div id="answer-container-78093" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78093-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you record the latitude and longitude of the pins without any recourse to OSM, for example because your camera has a built-in GPS, then displaying the data together with OSM data does not trigger any share-alike - you would at most be creating a collective database if you mixed OSM data and your data in a database, but displaying your data on top of OSM tiles would not even do that.</p>
<p>However, if you rely on OSM to find the latitude and longitude of an object - for example, if your recordings just indicate that something was "at the intersection of A street and B street" and then you use OSM to actually locate that intersection - then your coordinate might form a derivative database.</p>
<p>Even if that were the case, though, (1) the share-alike provision only kicks in if you make "substantial" use (<a href="https://wiki.osmfoundation.org/wiki/Licence/Community_Guidelines/Substantial_-_Guideline">https://wiki.osmfoundation.org/wiki/Licence/Community_Guidelines/Substantial_-_Guideline</a> ) and (2) even if share-alike kicks in, that doesn't mean your data becomes part of OSM, it just means that you have to make it available on request under ODbL.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '20, 00:34</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Dec '20, 10:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-78093" class="comments-container">
<span id="78099"></span>
<div id="comment-78099" class="comment">
<div id="post-78099-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Frederik - thank you so much. I love concise answers... :-)</p>
<p>By the way, I use the photographs' EXIF data, Google Maps or <a href="https://www.maps.ie/coordinates.html">https://www.maps.ie/coordinates.html</a> to geocode locations, thus, no share-alike as you explain. On the other hand, the geo-coordinates of my pins are available even without a request, so I could figure out, they might become part of OSM even without me noticing it, right?</p>
<p>All the best, Thomas</p>
</div>
<div id="comment-78099-info" class="comment-info">
<span class="comment-age">(29 Dec '20, 10:45)</span> <span class="comment-user userinfo">thomasew</span>
</div>
</div>
<span id="78100"></span>
<div id="comment-78100" class="comment">
<div id="post-78100-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Anyone using your pins to add data to OSM would be expected to attribute the source (i.e. your site), and only if that source makes it clear that the pin data is under a license compatible with OSM would we allow adding that data to OSM.</p>
</div>
<div id="comment-78100-info" class="comment-info">
<span class="comment-age">(29 Dec '20, 11:16)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-78093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78093-form-container" class="comment-form-container">
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

