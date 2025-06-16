+++
type = "question"
title = "[closed] How to add markers on a map from OSM using PHP and JavaScript?"
description = '''I want to put a marker for every customer in our customer database on a map using OSM with PHP and JavaScript. How can I do this? Is it possible to get the location for the customers without having the latitude and longitude for the addresses? greetz ronnie'''
date = "2011-09-26T09:47:00Z"
lastmod = "2011-10-06T10:43:00Z"
weight = 8147
keywords = [ "maps", "geocoding", "markers" ]
aliases = [ "/questions/8147" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to add markers on a map from OSM using PHP and JavaScript?](/questions/8147/how-to-add-markers-on-a-map-from-osm-using-php-and-javascript)

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
<span id="post-8147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8147-score" class="post-score" title="current number of votes">
-6
</div>
<span id="post-8147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to put a marker for every customer in our customer database on a map using OSM with PHP and JavaScript. How can I do this? Is it possible to get the location for the customers without having the latitude and longitude for the addresses?</p>
<p>greetz ronnie</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maps" rel="tag" title="see questions tagged &#39;maps&#39;">maps</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-markers" rel="tag" title="see questions tagged &#39;markers&#39;">markers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Sep '11, 09:47</strong></p>
<img src="https://secure.gravatar.com/avatar/955bc8893e2101aa2be2f5abb4302943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RonnieB&#39;s gravatar image" />
<p><span class="suspended-user">RonnieB</span><br />
(suspended)<br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RonnieB has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '11, 13:28</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-8147" class="comments-container">
<span id="8329"></span>
<div id="comment-8329" class="comment">
<div id="post-8329-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>No matter how many times you keep prodding this to appear on the front page, you're unlikely to get any more answers!</p>
</div>
<div id="comment-8329-info" class="comment-info">
<span class="comment-age">(06 Oct '11, 10:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8147-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Questioner appears unable to do own programming research; is breaking etiquette by repeatedly 'hup'ping the question, is uncivil to those who politely point this out." by Richard 06 Oct '11, 15:53

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8154"></span>

<div id="answer-container-8154" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8154-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-8154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is certainly possible to place markers on a map using <a href="http://openlayers.org/">OpenLayers</a>. Have a look at the <a href="https://wiki.openstreetmap.org/wiki/OpenLayers_Dynamic_POI">Dynamic POI example</a> in our wiki.</p>
<p>However for that you need to have the latitude and longitude of each point. If you lack that you can use <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a> to geocode the address information that you have and convert it into an usable format.</p>
<p>In the end you are going to need a bit of programming skill or you'll need to pay somebody to do the coding for you as there is no readymade solution that accepts a list of addresses and automatically plots them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '11, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-8154" class="comments-container">
<span id="8156"></span>
<div id="comment-8156" class="comment">
<div id="post-8156-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sure there is, you can use Nominatim for obtaining latitude and longitude as already mentioned by petschge.</p>
</div>
<div id="comment-8156-info" class="comment-info">
<span class="comment-age">(26 Sep '11, 15:52)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="8161"></span>
<div id="comment-8161" class="comment">
<div id="post-8161-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That would be very inefficient as every request to draw the marker at a given address would need to resolve it to lat/long instead of doing it once and storing lat/long in the database.</p>
</div>
<div id="comment-8161-info" class="comment-info">
<span class="comment-age">(26 Sep '11, 22:21)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
</div>
<div id="comment-tools-8154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8154-form-container" class="comment-form-container">
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

