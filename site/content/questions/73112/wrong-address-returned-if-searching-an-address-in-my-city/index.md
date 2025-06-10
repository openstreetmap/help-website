+++
type = "question"
title = "Wrong address returned if searching an Address in my city"
description = '''Since a month or so all the address gathered from OSM data in my city (Asti, Italy) shows the name of a nearby place as the city name, even it&#x27;s just a small village included within the city area. For example searching for &quot;Piazza Alfieri Asti&quot; on Nominatim it shows it belongs to Cascina Gioia, whic...'''
date = "2020-02-17T14:32:00Z"
lastmod = "2020-02-19T12:24:00Z"
weight = 73112
keywords = [ "node", "city", "osm" ]
aliases = [ "/questions/73112" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wrong address returned if searching an Address in my city](/questions/73112/wrong-address-returned-if-searching-an-address-in-my-city)

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
<span id="post-73112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73112-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Since a month or so all the address gathered from OSM data in my city (Asti, Italy) shows the name of a nearby place as the city name, even it's just a small village included within the city area.</p>
<p>For example searching for "Piazza Alfieri Asti" on Nominatim it shows it belongs to Cascina Gioia, which is a small village of 4 houses.</p>
<p>I'm a n00b in OSM, so I don't know how to fix it, any help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '20, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/3a9191aec5cc02baecce72ab611eba93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaRk_ViVi&#39;s gravatar image" />
<p><span>DaRk_ViVi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaRk_ViVi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73112" class="comments-container">
&#10;</div>
<div id="comment-tools-73112" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73112-form-container" class="comment-form-container">
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

<span id="73122"></span>

<div id="answer-container-73122" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73122-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't worry too much about it. What you see there is the response from the search engine that is used on openstreetmap.org called Nominatim. Nominatim takes some guesses on where a certain location is located in regards to region, city, suburb etc. If all administrative entities would be mapped as boarders Nominatim could be doing that quite accurately. But since Cascina Gioia is only mapped as a node Nominatim does not know its extent. Probably Cascina Gioiais the closest hamlet to the location you were searching and that's why Nominatim thought your location could possibly belong to Cascina Gioia.</p>
<p>You get these strange looking results all the time but except for mapping all administrative entities as areas there is not much you can do about it. But there is nothing wrong in the map data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '20, 10:34</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-73122" class="comments-container">
<span id="73126"></span>
<div id="comment-73126" class="comment">
<div id="post-73126-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, Asti and its neighborhoods are mapped as areas, and Cascina Gioia is just a random hamlet on the other side of the city...</p>
<p>It's probably a bug of the current version of Nominatim. On <a href="https://nominatim.openstreetmap.org/search.php?q=Piazza+Alfieri+Asti&amp;polygon_geojson=1&amp;viewbox=">nominatim.openstreetmap.org</a> (development version?), you will see that Cascina Gioia does not appear in the detailed results.</p>
</div>
<div id="comment-73126-info" class="comment-info">
<span class="comment-age">(18 Feb '20, 13:57)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73128"></span>
<div id="comment-73128" class="comment">
<div id="post-73128-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It does appear for me when I follow your link. If you press the details button you get to the <a href="https://nominatim.openstreetmap.org/details.php?osmtype=N&amp;osmid=2379926385&amp;class=highway">data page of the bus stop</a>. There it shows you five different hamlets around the location, of which Cascina Gioia is the closest.</p>
<p>I'm not saying it makes much sense to name such small hamlet for a feature inside a city. But then again the search engine is used globally and there are probably enough locations out there where finding the nearest village does make an awful lot of sense. I wouldn't call it a bug but just not enough differentiation done depending on location. But the active developer team of the tool is small and I guess changing this behavior is rather on the lower end of priorities.</p>
</div>
<div id="comment-73128-info" class="comment-info">
<span class="comment-age">(18 Feb '20, 14:45)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="73140"></span>
<div id="comment-73140" class="comment">
<div id="post-73140-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, so in the end this is just a bug on how the infos are read, and they are fine as it is. My main concern is that I use a Telegram bot who gives info based on coordinates and it reply with the same results of Nominatim.</p>
</div>
<div id="comment-73140-info" class="comment-info">
<span class="comment-age">(19 Feb '20, 12:24)</span> <span class="comment-user userinfo">DaRk_ViVi</span>
</div>
</div>
</div>
<div id="comment-tools-73122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73122-form-container" class="comment-form-container">
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

