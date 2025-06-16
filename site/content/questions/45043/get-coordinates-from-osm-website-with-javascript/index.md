+++
type = "question"
title = "Get coordinates from OSM website with Javascript"
description = '''I have a script that queries the front browser tab and if it&#x27;s an OpenStreetMap.org map URL, extracts the latitude and longitude of the map&#x27;s centre. This used to be accomplished simply by sending the following Javascript to the front tab: map.getCenter();  However, I haven&#x27;t used the script in some...'''
date = "2015-09-03T19:48:00Z"
lastmod = "2015-09-04T13:04:00Z"
weight = 45043
keywords = [ "leaflet", "openstreetmap", "javascript" ]
aliases = [ "/questions/45043" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Get coordinates from OSM website with Javascript](/questions/45043/get-coordinates-from-osm-website-with-javascript)

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
<span id="post-45043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45043-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a script that queries the front browser tab and if it's an OpenStreetMap.org map URL, extracts the latitude and longitude of the map's centre. This used to be accomplished simply by sending the following Javascript to the front tab:</p>
<pre><code>map.getCenter();</code></pre>
<p>However, I haven't used the script in some time and this no longer works. I believe OSM was still using OpenLayers when I last used the script successfully and it's now using Leaflet? In any case, I've spent a couple of hours trying to find the map variable that I can send the <code>getCenter()</code> function to as detailed in the <a href="http://leafletjs.com/reference.html#map-get-methods">Leaflet documentation</a>, but no joy. Can anyone tell me how I can use Javascript to get the centre of the map on the current OSM website? To be clear, I'm not trying to write my own mapping application using OSM, I want this to work with the main OpenStreetMap.org website.</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Sep '15, 19:48</strong></p>
<img src="https://secure.gravatar.com/avatar/7919ba114865547c7b7fafc112dbc024?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jolin%20Warren&#39;s gravatar image" />
<p><span>Jolin Warren</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jolin Warren has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45043" class="comments-container">
&#10;</div>
<div id="comment-tools-45043" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45043-form-container" class="comment-form-container">
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

<span id="45044"></span>

<div id="answer-container-45044" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45044-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-45044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jolin Warren has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Center lat/lon and zoom level are in the URL of where ever your www.openstreetmap.org window is looking. . . Its been a while since I've looked at Javascript but I think you can access the URL within your code and then parse out the stuff you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '15, 20:30</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-45044" class="comments-container">
<span id="45045"></span>
<div id="comment-45045" class="comment">
<div id="post-45045-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did think about doing that, but the URL doesn't automatically update as you drag the map. One option is doing a page source dump and then searching through, as there are embedded links in the page that have updated lat/lon, but I'd rather not be screen scraping if I can avoid it. I'd prefer a cleaner solution where I query the lat/lon specifically. If it's possible!</p>
</div>
<div id="comment-45045-info" class="comment-info">
<span class="comment-age">(03 Sep '15, 20:43)</span> <span class="comment-user userinfo">Jolin Warren</span>
</div>
</div>
<span id="45051"></span>
<div id="comment-45051" class="comment">
<div id="post-45051-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that helped. I don't know what I was doing previously, but it turns out that the latitude, longitude, and zoom are continuously updated in the URL, and that bookmarklet uses the URL (<code>window.location.hash</code>). This works wonderfully. Thanks for your help.</p>
</div>
<div id="comment-45051-info" class="comment-info">
<span class="comment-age">(04 Sep '15, 13:03)</span> <span class="comment-user userinfo">Jolin Warren</span>
</div>
</div>
<span id="45052"></span>
<div id="comment-45052" class="comment">
<div id="post-45052-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My mistake. I don't know what I was doing before, but you are right that the lat/lon and zoom are always updated in the URL (after the hash). Thanks stf, this is the way to go. You'll see from my <a href="#45051">answer below</a> that I used the Javascript property <code>window.location.hash</code> to extract the info I needed. Many thanks.</p>
</div>
<div id="comment-45052-info" class="comment-info">
<span class="comment-age">(04 Sep '15, 13:04)</span> <span class="comment-user userinfo">Jolin Warren</span>
</div>
</div>
</div>
<div id="comment-tools-45044" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45044-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45047"></span>

<div id="answer-container-45047" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45047-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a bookmarklet <a href="https://wiki.openstreetmap.org/wiki/OS_Locator_Musical_Chairs">here</a> that does it so I'm sure that you could get some info out of that :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '15, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-45047" class="comments-container">
&#10;</div>
<div id="comment-tools-45047" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45047-form-container" class="comment-form-container">
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

