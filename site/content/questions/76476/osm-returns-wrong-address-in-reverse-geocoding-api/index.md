+++
type = "question"
title = "OSM returns wrong address in reverse geocoding API"
description = '''Hi, I see there is a problem with OSM regarding reverse geocoding. For example for address in city Katowice: Katowice, Śródmieście, 18 sierpnia It returns that it is city &quot;Gorzów Wielkopolski&quot; =   https://nominatim.openstreetmap.org/?format=jsonv2&amp;amp;accept-language=pl&amp;amp;countrycodes=pl&amp;amp;addre...'''
date = "2020-09-06T11:14:00Z"
lastmod = "2020-09-08T18:21:00Z"
weight = 76476
keywords = [ "reversed", "reversegeocoding", "reverse" ]
aliases = [ "/questions/76476" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM returns wrong address in reverse geocoding API](/questions/76476/osm-returns-wrong-address-in-reverse-geocoding-api)

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
<span id="post-76476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76476-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I see there is a problem with OSM regarding reverse geocoding. For example for address in city Katowice: Katowice, Śródmieście, 18 sierpnia</p>
<p>It returns that it is city "Gorzów Wielkopolski" =</p>
<blockquote>
<p><a href="https://nominatim.openstreetmap.org/?format=jsonv2&amp;accept-language=pl&amp;countrycodes=pl&amp;addressdetails=1&amp;polygon_geojson=1&amp;limit=1&amp;q=Katowice,%20%C5%9Ar%C3%B3dmie%C5%9Bcie,%2018%20sierpnia">https://nominatim.openstreetmap.org/?format=jsonv2&amp;accept-language=pl&amp;countrycodes=pl&amp;addressdetails=1&amp;polygon_geojson=1&amp;limit=1&amp;q=Katowice,%20%C5%9Ar%C3%B3dmie%C5%9Bcie,%2018%20sierpnia</a></p>
</blockquote>
<p>But, if word in address will be changed to "Katowice, 18 sierpnia" it returns corect address for city Katowice:</p>
<blockquote>
<p><a href="https://nominatim.openstreetmap.org/?format=jsonv2&amp;accept-language=pl&amp;countrycodes=pl&amp;addressdetails=1&amp;polygon_geojson=1&amp;limit=1&amp;q=Katowice,%2018%20sierpnia">https://nominatim.openstreetmap.org/?format=jsonv2&amp;accept-language=pl&amp;countrycodes=pl&amp;addressdetails=1&amp;polygon_geojson=1&amp;limit=1&amp;q=Katowice,%2018%20sierpnia</a></p>
</blockquote>
<p>How to avoid such problems? Cause it totally different cities and provide more problems than help. I don't understand why OSM does not include word "Katowice" as main city or at least try to check Katowice, because it is better result than Gorzów (street match as well as city).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversed" rel="tag" title="see questions tagged &#39;reversed&#39;">reversed</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '20, 11:14</strong></p>
<img src="https://secure.gravatar.com/avatar/aefa66e38ab97c23b4e61071c5b76b4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="michal%20galaszewski&#39;s gravatar image" />
<p><span>michal galas...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="michal galaszewski has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76476" class="comments-container">
&#10;</div>
<div id="comment-tools-76476" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76476-form-container" class="comment-form-container">
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

<span id="76515"></span>

<div id="answer-container-76515" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76515-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The street and the address in question is not within the boundary of Śródmieście (in Katowice) see <a href="https://nominatim.openstreetmap.org/ui/search.html?q=%C5%9Ar%C3%B3dmie%C5%9Bcie%2C+">https://nominatim.openstreetmap.org/ui/search.html?q=%C5%9Ar%C3%B3dmie%C5%9Bcie%2C+</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '20, 13:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '20, 13:40</strong> </span></p>
</div>
</div>
<div id="comments-container-76515" class="comments-container">
<span id="76517"></span>
<div id="comment-76517" class="comment">
<div id="post-76517-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I get it, but still adress more similar for Katowice disregarding that the street does not belong to Srodmiescie boundary that searching for totally different city. Still think it is a problem with reverse geocoding or I am doing something wrong. Cause I have no influece on what the address I expect - i get it from real estate advertisement and just making sure, that geo_point is similar to text address provided.</p>
</div>
<div id="comment-76517-info" class="comment-info">
<span class="comment-age">(08 Sep '20, 17:10)</span> <span class="comment-user userinfo">michal galas...</span>
</div>
</div>
<span id="76518"></span>
<div id="comment-76518" class="comment">
<div id="post-76518-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you tested against Photon? It uses data form nominatim, but is more forgiving wrt errors. <a href="http://photon.komoot.de/">http://photon.komoot.de/</a></p>
</div>
<div id="comment-76518-info" class="comment-info">
<span class="comment-age">(08 Sep '20, 18:21)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-76515" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76515-form-container" class="comment-form-container">
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

