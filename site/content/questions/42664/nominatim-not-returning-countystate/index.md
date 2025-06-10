+++
type = "question"
title = "Nominatim not returning county/state"
description = '''Working on a gadget that gets city/town/village/hamlet nodes from Overpass and then uses Nominatim to get the state_district/state.  This works for Birmingham example. This works for Siglufjörður (Iceland). This does not work for Pratt, Kansas. Only returned country=&quot;United States of America&quot; and no...'''
date = "2015-04-29T02:03:00Z"
lastmod = "2015-04-30T15:32:00Z"
weight = 42664
keywords = [ "overpass", "state", "nominatim" ]
aliases = [ "/questions/42664" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim not returning county/state](/questions/42664/nominatim-not-returning-countystate)

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
<span id="post-42664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42664-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Working on a gadget that gets city/town/village/hamlet nodes from Overpass and then uses Nominatim to get the state_district/state.</p>
<ul>
<li><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&amp;zoom=18&amp;addressdetails=1">This works for Birmingham example</a>.</li>
<li><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;osm_id=61365704&amp;osm_type=N&amp;zoom=18&amp;addressdetails=1&amp;accept-language=en">This works for Siglufjörður (Iceland)</a>.</li>
<li><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;osm_id=151421301&amp;osm_type=N&amp;zoom=18&amp;addressdetails=1&amp;accept-language=en">This does not work for Pratt, Kansas</a>. Only returned country="United States of America" and not state_district=Pratt, state=Kansas.</li>
<li><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;osm_id=61785451&amp;osm_type=N&amp;zoom=18&amp;addressdetails=1&amp;accept-language=en">Same for New York City</a> as for Pratt.</li>
</ul>
<p>Is there no better way to automatically get the two top tier administrative levels for each city/town/village/hamlet?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-state" rel="tag" title="see questions tagged &#39;state&#39;">state</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '15, 02:03</strong></p>
<img src="https://secure.gravatar.com/avatar/de4f470e89a01a4709cd5d7b382f0ffa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stalfur&#39;s gravatar image" />
<p><span>Stalfur</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stalfur has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42664" class="comments-container">
&#10;</div>
<div id="comment-tools-42664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42664-form-container" class="comment-form-container">
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

<span id="42666"></span>

<div id="answer-container-42666" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42666-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems like the first two queries are working in different ways from one another. The first one is using lat/lon coordinates for its reverse lookup, and the second one is using osm_id. The third and fourth one are relying on the osm_id method.</p>
<p>When I used <a href="http://www.latlong.net/">this tool</a> to find the lat/lon coordinates for Pratt, Kansas, it seems to work better for me.</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=37.643907&amp;lon=-98.737591&amp;zoom=18&amp;addressdetails=1">Here</a> is what I got for the Pratt, Kansas query when I used lat/lon to look it up.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '15, 02:24</strong></p>
<img src="https://secure.gravatar.com/avatar/c670337199fd7c4d89f48c2e3d3df07c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baghaii&#39;s gravatar image" />
<p><span>baghaii</span><br />
<span class="score" title="216 reputation points">216</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baghaii has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-42666" class="comments-container">
&#10;</div>
<div id="comment-tools-42666" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42666-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42668"></span>

<div id="answer-container-42668" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42668-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using lat/lon gives me</p>
<ul>
<li><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=40.7305991&amp;lon=-73.9865812&amp;zoom=18&amp;addressdetails=1">this for New York City</a> county=New York, state=New York</li>
<li><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=37.6439071&amp;lon=-98.7375911&amp;zoom=18&amp;addressdetails=1">And this for Pratt</a> county=Pratt County, state=Kansas</li>
</ul>
<p>Why does lat/lon give me this when osm_id doesn't?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '15, 02:49</strong></p>
<img src="https://secure.gravatar.com/avatar/de4f470e89a01a4709cd5d7b382f0ffa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stalfur&#39;s gravatar image" />
<p><span>Stalfur</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stalfur has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Apr '15, 03:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42668" class="comments-container">
<span id="42669"></span>
<div id="comment-42669" class="comment">
<div id="post-42669-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta: this should be a comment on baghaii's answer, right? please could you use the "add new comment" button to add it there (due to technical problem I cannot convert it)</p>
</div>
<div id="comment-42669-info" class="comment-info">
<span class="comment-age">(29 Apr '15, 03:03)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42674"></span>
<div id="comment-42674" class="comment">
<div id="post-42674-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I hadn't seen baghaii's answer when I posted this. I'm still perplexed as to why these two methods don't return the same answer. OSM_ID is reccomended over lat/lon.</p>
</div>
<div id="comment-42674-info" class="comment-info">
<span class="comment-age">(29 Apr '15, 08:44)</span> <span class="comment-user userinfo">Stalfur</span>
</div>
</div>
<span id="42726"></span>
<div id="comment-42726" class="comment">
<div id="post-42726-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When I try this <a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;osm_id=316955993&amp;osm_type=N&amp;zoom=18&amp;addressdetails=1&amp;accept-language=en">query</a> with node 316955993 The result returns the state. So IMHO it depends on the node you are investigating.</p>
<p>I found that node ID via <a href="http://nominatim.openstreetmap.org/details.php?place_id=127699730">http://nominatim.openstreetmap.org/details.php?place_id=127699730</a> (the first link when I looked for Pratt on that website), then I took the node id under the section "linked places"</p>
</div>
<div id="comment-42726-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 11:16)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="42746"></span>
<div id="comment-42746" class="comment">
<div id="post-42746-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your query escada is for the county, my query was for the city within the county. I've filed a bug at nominatim for this <a href="https://github.com/twain47/Nominatim/issues/269">https://github.com/twain47/Nominatim/issues/269</a></p>
</div>
<div id="comment-42746-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 15:32)</span> <span class="comment-user userinfo">Stalfur</span>
</div>
</div>
</div>
<div id="comment-tools-42668" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42668-form-container" class="comment-form-container">
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

