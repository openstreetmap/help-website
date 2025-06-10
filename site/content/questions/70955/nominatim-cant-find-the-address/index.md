+++
type = "question"
title = "Nominatim can&#x27;t find the address"
description = '''I have some listings with addresses and coordinates. Some of these coordinates are not accurate and I can&#x27;t do the point-in-polygon check. So there is a situation when a house has coordinates which are not inside the polygon I have. Of course, it&#x27;s a problem with my data provider. So I went further ...'''
date = "2019-09-29T16:37:00Z"
lastmod = "2019-10-01T04:15:00Z"
weight = 70955
keywords = [ "osm", "nominatim", "geocoding", "coordinates" ]
aliases = [ "/questions/70955" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim can't find the address](/questions/70955/nominatim-cant-find-the-address)

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
<span id="post-70955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70955-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have some listings with addresses and coordinates. Some of these coordinates are not accurate and I can't do the point-in-polygon check. So there is a situation when a house has coordinates which are not inside the polygon I have. Of course, it's a problem with my data provider. So I went further and tried to take the address and convert it into the right coordinates. Here is where the troibles begin.</p>
<p>Try to do this: 1. Open Nominatim. 2. Enter "58 West St #33A, NY" and you will have no results 3. But enter the same in Google Maps and you will have the result 4. Try to delete "#33A" and you will have a street coordinates. But I need the house coordinates.</p>
<p>I've tried to change # to № and change the position of words, It doesn't help.</p>
<p>Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Sep '19, 16:37</strong></p>
<img src="https://secure.gravatar.com/avatar/d107175b90214ff725c8ad69153427e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Skrypch&#39;s gravatar image" />
<p><span>Skrypch</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Skrypch has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70955" class="comments-container">
&#10;</div>
<div id="comment-tools-70955" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70955-form-container" class="comment-form-container">
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

<span id="70962"></span>

<div id="answer-container-70962" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70962-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>58 West Street is not in the OSM data, let alone #33. <a href="https://www.openstreetmap.org/node/2824641192">56</a> is and <a href="https://www.openstreetmap.org/node/2824641193">62</a> is but <a href="https://www.openstreetmap.org/#map=19/40.70830/-74.01489&amp;layers=D">nothing inbetween</a>.</p>
<p>Nominatim.openstreetmap.org also uses addresses from tiger data. With that it for example finds <a href="https://nominatim.openstreetmap.org/search.php?q=58+west+street%2C+manhattan&amp;polygon_geojson=1&amp;viewbox=">"58 West Street, Manhattan"</a>, albeit a bit too far north.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Sep '19, 21:09</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-70962" class="comments-container">
<span id="70963"></span>
<div id="comment-70963" class="comment">
<div id="post-70963-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But then, what can I do with it? Google Maps greatly cope with such situation and show me the right polygon. I found that 58 West Street is a historical name of the building but still, the issue exists.This your 56 example is the right polygon I need.</p>
</div>
<div id="comment-70963-info" class="comment-info">
<span class="comment-age">(29 Sep '19, 21:39)</span> <span class="comment-user userinfo">Skrypch</span>
</div>
</div>
<span id="70967"></span>
<div id="comment-70967" class="comment not_top_scorer">
<div id="post-70967-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not sure what you are really looking for. Is it <a href="https://nominatim.openstreetmap.org/search.php?q=33+rector+street%2C+new+york&amp;polygon_geojson=1&amp;viewbox=">33 Rector Street</a>? That's found by Nominatim. If I put your search term into Google Maps it shows me the building across the street (40 Rector St). Is this rather an exercise getting your addresses corrected than finding the geolocation?</p>
</div>
<div id="comment-70967-info" class="comment-info">
<span class="comment-age">(30 Sep '19, 08:25)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="70968"></span>
<div id="comment-70968" class="comment not_top_scorer">
<div id="post-70968-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, it's about finding the geolocation. The address is "58 West St #33A, NY" which means that the street is 58 W st and 33a is the building number. Google Maps easily cope with that</p>
</div>
<div id="comment-70968-info" class="comment-info">
<span class="comment-age">(30 Sep '19, 09:28)</span> <span class="comment-user userinfo">Skrypch</span>
</div>
</div>
<span id="70969"></span>
<div id="comment-70969" class="comment">
<div id="post-70969-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't understand what you mean by "the street is 58 W st and 33a is the building number". I thought you were looking for unit/apartment 33a in the house number 58 on West Street. Are you actually looking for house number 33a on West 58th Street? Can you link to the Google page that shows the correct building?</p>
</div>
<div id="comment-70969-info" class="comment-info">
<span class="comment-age">(30 Sep '19, 13:37)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="70970"></span>
<div id="comment-70970" class="comment">
<div id="post-70970-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Try "33A West 58th St, NY" , then it finds <a href="https://www.openstreetmap.org/way/308322447#map=18/40.76554/-73.97794">https://www.openstreetmap.org/way/308322447#map=18/40.76554/-73.97794</a></p>
<p>So the data is there, the problem is in translating your input "58 West St" to "West 58th St". OSM does not have the resources to pay developers to convert every possible input format to a "normalized" address. So you will have to adapt your input strings to what is known.</p>
</div>
<div id="comment-70970-info" class="comment-info">
<span class="comment-age">(30 Sep '19, 14:08)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="70972"></span>
<div id="comment-70972" class="comment not_top_scorer">
<div id="post-70972-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://www.google.com/maps/place/58+West+St+%2333A,+New+York,+NY+10006,+%D0%A1%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D1%96+%D0%A8%D1%82%D0%B0%D1%82%D0%B8+%D0%90%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B8/data=!4m2!3m1!1s0x89c25a10f122fba5:0x5155b37225ebfc7a?sa=X&amp;ved=2ahUKEwjV-o-e6PjkAhUBuIsKHSKfAqwQ8gEwAHoECAoQAQ">https://www.google.com/maps/place/58+West+St+%2333A,+New+York,+NY+10006,+%D0%A1%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D1%96+%D0%A8%D1%82%D0%B0%D1%82%D0%B8+%D0%90%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B8/data=!4m2!3m1!1s0x89c25a10f122fba5:0x5155b37225ebfc7a?sa=X&amp;ved=2ahUKEwjV-o-e6PjkAhUBuIsKHSKfAqwQ8gEwAHoECAoQAQ</a></p>
<p>I figured out that OSM can't deal with situations when there is a string with "#".</p>
</div>
<div id="comment-70972-info" class="comment-info">
<span class="comment-age">(30 Sep '19, 16:02)</span> <span class="comment-user userinfo">Skrypch</span>
</div>
</div>
<span id="70973"></span>
<div id="comment-70973" class="comment">
<div id="post-70973-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So you are looking for "40 Rector Street". If this building ever had the address "58 West Street" assigned (whatever #33a is supposed to be), you will likely not find it in OSM since OSM does not usually keep track of former addresses (former names of streets yes but not assembled addresses). Current addresses in New York should be pretty complete, though.</p>
<p>This has nothing to do with a "#" in the search string not being searchable.</p>
</div>
<div id="comment-70973-info" class="comment-info">
<span class="comment-age">(30 Sep '19, 17:10)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="70975"></span>
<div id="comment-70975" class="comment not_top_scorer">
<div id="post-70975-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I didn't know it is former address. I used the one that listing websites give - <a href="https://www.trulia.com/p/ny/manhattan/58-west-st-33a-manhattan-ny-10006--2419635685">https://www.trulia.com/p/ny/manhattan/58-west-st-33a-manhattan-ny-10006--2419635685</a></p>
</div>
<div id="comment-70975-info" class="comment-info">
<span class="comment-age">(30 Sep '19, 18:01)</span> <span class="comment-user userinfo">Skrypch</span>
</div>
</div>
<span id="70976"></span>
<div id="comment-70976" class="comment">
<div id="post-70976-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You wrote yourself above that 58 West Street is a historical name.</p>
<p>But now that you link to that website I see it comes back to correcting the address as I speculated all along. If you look at the view from the balcony and into the text description that address is right South of Central Park. That cannot be West Street nor Rector Street. What Google Maps gives you as location is plain wrong (when I click on your google link I get the building 40 Rector Street highlighted). I guess this is really on "West 58th Street" as I already wrote above and escada linked to. #33 is the unit number. Here's the add with an correct address by the way: <a href="https://streeteasy.com/building/tower-58/33a">https://streeteasy.com/building/tower-58/33a</a></p>
</div>
<div id="comment-70976-info" class="comment-info">
<span class="comment-age">(30 Sep '19, 18:18)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="70977"></span>
<div id="comment-70977" class="comment not_top_scorer">
<div id="post-70977-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I got it. Thanks a lot for your help!</p>
</div>
<div id="comment-70977-info" class="comment-info">
<span class="comment-age">(30 Sep '19, 18:22)</span> <span class="comment-user userinfo">Skrypch</span>
</div>
</div>
<span id="70981"></span>
<div id="comment-70981" class="comment not_top_scorer">
<div id="post-70981-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please note that it is also possible that there is a unit #33 in 58, West Street, Greenpoint, NY, which is here: <a href="https://www.openstreetmap.org/node/2842929259">https://www.openstreetmap.org/node/2842929259</a></p>
</div>
<div id="comment-70981-info" class="comment-info">
<span class="comment-age">(01 Oct '19, 04:15)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-70962" class="comment-tools">
<span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-70962-form-container" class="comment-form-container">
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

