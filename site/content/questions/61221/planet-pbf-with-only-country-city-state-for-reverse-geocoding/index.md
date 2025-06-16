+++
type = "question"
title = "planet PBF with only country, city, state for reverse geocoding"
description = '''Hi guys, Is it possible to slim down a planet .pbf file to only contain Country/City/State names to be used for simple reverse geocoding purposes only? Any pointers or help will be appreciated.'''
date = "2017-12-16T20:39:00Z"
lastmod = "2017-12-16T22:54:00Z"
weight = 61221
keywords = [ "planet", "geocoding" ]
aliases = [ "/questions/61221" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [planet PBF with only country, city, state for reverse geocoding](/questions/61221/planet-pbf-with-only-country-city-state-for-reverse-geocoding)

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
<span id="post-61221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61221-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys,</p>
<p>Is it possible to slim down a planet .pbf file to only contain Country/City/State names to be used for simple reverse geocoding purposes only?</p>
<p>Any pointers or help will be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '17, 20:39</strong></p>
<img src="https://secure.gravatar.com/avatar/50b099a979b02728c4af845ffd24ffed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cbyter&#39;s gravatar image" />
<p><span>cbyter</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cbyter has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Dec '17, 20:46</strong> </span></p>
</div>
</div>
<div id="comments-container-61221" class="comments-container">
&#10;</div>
<div id="comment-tools-61221" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61221-form-container" class="comment-form-container">
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

<span id="61225"></span>

<div id="answer-container-61225" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61225-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You haven't mentioned a specific geocoder, so I assume you plan to write your own implementation, e.g. using a full-text search engine.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Osmfilter">https://wiki.openstreetmap.org/wiki/Osmfilter</a> allows you to extract only the places you want. Start with a small geographic area (e.g. one country) first. Look for <code>place</code> tags (<a href="https://wiki.openstreetmap.org/wiki/Key:place),">https://wiki.openstreetmap.org/wiki/Key:place),</a> <code>boundary=administrative</code> (<a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative)">https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative)</a> and <code>admin_level</code> (country is 2, city is 8, so anything in that range).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '17, 22:24</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-61225" class="comments-container">
<span id="61226"></span>
<div id="comment-61226" class="comment">
<div id="post-61226-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the response. I plan on using nominatim, does that change the answer at all?</p>
</div>
<div id="comment-61226-info" class="comment-info">
<span class="comment-age">(16 Dec '17, 22:45)</span> <span class="comment-user userinfo">cbyter</span>
</div>
</div>
<span id="61227"></span>
<div id="comment-61227" class="comment">
<div id="post-61227-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, Nominatim is a good choice. It will take care of linking cities to countries, handling all languages, abbreviations. It can't do spell-checking and can't incomplete search terms (type-ahead/autocomplete like search). Nominatim uses <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/output-gazetteer.cpp">https://github.com/openstreetmap/osm2pgsql/blob/master/output-gazetteer.cpp</a> during the import (utils/setup.php) and it might give you some hints on tags. For type-ahead have a look at <a href="http://photon.komoot.de/">http://photon.komoot.de/</a></p>
</div>
<div id="comment-61227-info" class="comment-info">
<span class="comment-age">(16 Dec '17, 22:54)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-61225" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61225-form-container" class="comment-form-container">
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

