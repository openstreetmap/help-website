+++
type = "question"
title = "Find street coordinates"
description = '''Hi, Can I use OpenStreetMap to find map coordinates for a street by name? I&#x27;m interested for a web application using php/html/javascript/mysql technologies.'''
date = "2011-05-11T08:29:00Z"
lastmod = "2021-11-23T22:05:00Z"
weight = 5107
keywords = [ "street", "geocoding" ]
aliases = [ "/questions/5107" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Find street coordinates](/questions/5107/find-street-coordinates)

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
<span id="post-5107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5107-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-5107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
3
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, Can I use OpenStreetMap to find map coordinates for a street by name?</p>
<p>I'm interested for a web application using php/html/javascript/mysql technologies.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '11, 08:29</strong></p>
<img src="https://secure.gravatar.com/avatar/921468edba4a8f80b698d71150029898?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xprt64&#39;s gravatar image" />
<p><span>xprt64</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xprt64 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 May '11, 08:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-5107" class="comments-container">
&#10;</div>
<div id="comment-tools-5107" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5107-form-container" class="comment-form-container">
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

<span id="5109"></span>

<div id="answer-container-5109" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5109-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-5109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are looking for <strong>geocoding</strong> based on OpenStreetMap.</p>
<p>There are several different ways to do it. If you want to set up your own server, try <a href="http://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a>. There are other solutions out there, e.g. the <a href="https://github.com/geocommons/geocoder">GeoCommons geocoder</a> aimed primarily at geocoding US addresses (not sure how far their OpenStreetMap import project has progressed) and <a href="http://www.gisgraphy.com">Gisgraphy</a> who have a working OSM import but don't do house numbers yet.</p>
<p>If you are looking for an online service (i.e. don't want to run your own server), then your best bet is <a href="http://open.mapquestapi.com/nominatim/">MapQuest's free Nominatim-based service</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '11, 08:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-5109" class="comments-container">
<span id="82435"></span>
<div id="comment-82435" class="comment">
<div id="post-82435-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you please provide more information regarding the link to "MapQuest's free Nominatim-based service"? I would need exactly the lat/lng coordinates which represent a street. Thx</p>
</div>
<div id="comment-82435-info" class="comment-info">
<span class="comment-age">(31 Oct '21, 18:34)</span> <span class="comment-user userinfo">VARGAPeter1971</span>
</div>
</div>
<span id="82439"></span>
<div id="comment-82439" class="comment">
<div id="post-82439-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The answer you referring to is 10 years old. To answer your question: <a href="https://nominatim.org/release-docs/latest/api/Search/">https://nominatim.org/release-docs/latest/api/Search/</a> should help for a start, but please adhere to the Nominatim usage policy found here: <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> . If you need to geocode large amounts of data, a third party provider may help, see list here: <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Alternatives_.2F_Third-party_providers">https://wiki.openstreetmap.org/wiki/Nominatim#Alternatives_.2F_Third-party_providers</a></p>
</div>
<div id="comment-82439-info" class="comment-info">
<span class="comment-age">(01 Nov '21, 09:32)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="82444"></span>
<div id="comment-82444" class="comment">
<div id="post-82444-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! I am a bloody beginner and somehow I am lost. I am playing around with this site:<br />
<a href="https://nominatim.openstreetmap.org/ui/search.html?street=avd+Huerta+Bel%C3%B3n&amp;city=Marbella&amp;county=M%C3%A1laga&amp;country=Spain">https://nominatim.openstreetmap.org/ui/search.html?street=avd+Huerta+Bel%C3%B3n&amp;city=Marbella&amp;county=M%C3%A1laga&amp;country=Spain</a></p>
<p>You see the street "Avenida Huerta Belón" is marked only partially. Can you please point me to the right direction that the whole road would be marked abd how do I get all of the latitudes/longitudes values for this polyline?</p>
<p>This would really help me a lot. I am missing something and I am "stuck".</p>
<p>I tried also - according to the link you posted - this URL, but it still doesn't return all coordinates for the road and the road is marked only partially:<br />
<a href="https://nominatim.openstreetmap.org/search/Avd%20Huerta%20Bel%C3%B3n,Marbella,%20Spain?format=json&amp;addressdetails=1&amp;limit=50&amp;polygon_geojson=1&amp;viewbox=36.5120612,-4.89550880,36.5152989,-4.8899952">https://nominatim.openstreetmap.org/search/Avd%20Huerta%20Bel%C3%B3n,Marbella,%20Spain?format=json&amp;addressdetails=1&amp;limit=50&amp;polygon_geojson=1&amp;viewbox=36.5120612,-4.89550880,36.5152989,-4.8899952</a></p>
</div>
<div id="comment-82444-info" class="comment-info">
<span class="comment-age">(01 Nov '21, 16:41)</span> <span class="comment-user userinfo">VARGAPeter1971</span>
</div>
</div>
<span id="82448"></span>
<div id="comment-82448" class="comment">
<div id="post-82448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>May be the viewbox had the wrong parameters. This is an updated URL, but no change:<br />
<a href="https://nominatim.openstreetmap.org/search/Avd%20Huerta%20Bel%C3%B3n,Marbella,%20Spain?format=json&amp;addressdetails=1&amp;limit=25&amp;polygon_geojson=1&amp;viewbox=-4.89550880,36.5152989,-4.8899952,36.5120612&amp;osm_type=W">https://nominatim.openstreetmap.org/search/Avd%20Huerta%20Bel%C3%B3n,Marbella,%20Spain?format=json&amp;addressdetails=1&amp;limit=25&amp;polygon_geojson=1&amp;viewbox=-4.89550880,36.5152989,-4.8899952,36.5120612&amp;osm_type=W</a></p>
</div>
<div id="comment-82448-info" class="comment-info">
<span class="comment-age">(01 Nov '21, 19:28)</span> <span class="comment-user userinfo">VARGAPeter1971</span>
</div>
</div>
</div>
<div id="comment-tools-5109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5109-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82666"></span>

<div id="answer-container-82666" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82666-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-82666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The comments of this answer have the solution. I could solve it. Apparently it's forbidden in OSM forums to be more specific so I don't want to be rude and break this rule.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '21, 22:05</strong></p>
<img src="https://secure.gravatar.com/avatar/1cc4e21ce90fdcc31abb1204bf419e64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VARGAPeter1971&#39;s gravatar image" />
<p><span>VARGAPeter1971</span><br />
<span class="score" title="8 reputation points">8</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VARGAPeter1971 has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Nov '21, 22:06</strong> </span></p>
</div>
</div>
<div id="comments-container-82666" class="comments-container">
&#10;</div>
<div id="comment-tools-82666" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82666-form-container" class="comment-form-container">
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

