+++
type = "question"
title = "How can i check with coordinates type of place?"
description = '''Hello I am looking for way how can i check with coordinates type of place for example 50.064317, 19.948575 is it building, street or some field? I am using leaflet too Best regards'''
date = "2018-10-22T15:19:00Z"
lastmod = "2018-10-25T11:02:00Z"
weight = 66417
keywords = [ "leaflet", "coordinates" ]
aliases = [ "/questions/66417" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can i check with coordinates type of place?](/questions/66417/how-can-i-check-with-coordinates-type-of-place)

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
<span id="post-66417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66417-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>I am looking for way how can i check with coordinates type of place for example</p>
<p>50.064317, 19.948575</p>
<p>is it building, street or some field?</p>
<p>I am using leaflet too</p>
<p>Best regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '18, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/cd63a6756d8d22b50ff9faea27b00ab4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adacho26&#39;s gravatar image" />
<p><span>adacho26</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adacho26 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66417" class="comments-container">
&#10;</div>
<div id="comment-tools-66417" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66417-form-container" class="comment-form-container">
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

<span id="66423"></span>

<div id="answer-container-66423" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66423-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The technical term for what you are trying to do is "reverse geocoding". Likely the easiest way to that with OSM is to use nominatim <a href="https://nominatim.openstreetmap.org/search.php?q=50.064317%2C+19.948575&amp;polygon_geojson=1&amp;viewbox=">https://nominatim.openstreetmap.org/search.php?q=50.064317%2C+19.948575&amp;polygon_geojson=1&amp;viewbox=</a></p>
<p>If you are thinking of using this in a bulk mode please adhere to the aup <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> , our data licence <a href="https://wiki.osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ#What_is_the_licence.2C_how_can_I_use_it.3F">https://wiki.osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ#What_is_the_licence.2C_how_can_I_use_it.3F</a> and our general terms of use <a href="https://wiki.osmfoundation.org/wiki/Terms_of_Use">https://wiki.osmfoundation.org/wiki/Terms_of_Use</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '18, 12:08</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-66423" class="comments-container">
<span id="66424"></span>
<div id="comment-66424" class="comment">
<div id="post-66424-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have too much operations, so this way is not good :( Is there another option to load all building in some layer and then check without connection ?</p>
</div>
<div id="comment-66424-info" class="comment-info">
<span class="comment-age">(23 Oct '18, 12:17)</span> <span class="comment-user userinfo">adacho26</span>
</div>
</div>
<span id="66425"></span>
<div id="comment-66425" class="comment">
<div id="post-66425-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Reverse geocoding only works well for addresses and POIs. It doesn't really work for "fields", buildings without addresses and other objects which don't really fit into the POI category. Overpass API might be the better choice.</p>
</div>
<div id="comment-66425-info" class="comment-info">
<span class="comment-age">(23 Oct '18, 12:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="66429"></span>
<div id="comment-66429" class="comment">
<div id="post-66429-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai"></a><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> I cannot find any toturial how to use Overpass API with react or/and leaflet.. can u tell me briefly how to get info about type of pattern (grass/building) with overpass?</p>
</div>
<div id="comment-66429-info" class="comment-info">
<span class="comment-age">(23 Oct '18, 15:10)</span> <span class="comment-user userinfo">adacho26</span>
</div>
</div>
<span id="66431"></span>
<div id="comment-66431" class="comment">
<div id="post-66431-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks like there are multiple Leaflet plugins available for Overpass API. I've never used both together so I can't recommend a specific one. But you should find multiple examples when using your favorite search engine.</p>
</div>
<div id="comment-66431-info" class="comment-info">
<span class="comment-age">(24 Oct '18, 08:15)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="66434"></span>
<div id="comment-66434" class="comment">
<div id="post-66434-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a>, I wonder whether the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Relative_to_other_elements_.28around.29">around function</a> is the solution for the OP's problem. One has to specify a "distance" around the current point to find polygons in the neighbourhood of the give point. The will also give nearby objects, not just enclosing objects. Or do you have something else in mind ?</p>
</div>
<div id="comment-66434-info" class="comment-info">
<span class="comment-age">(24 Oct '18, 11:14)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="66436"></span>
<div id="comment-66436" class="comment not_top_scorer">
<div id="post-66436-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a> That's what I have in mind. Similar to the query feature at openstreetmap.org. It works a little bit different than reverse geocoding, that's true.</p>
</div>
<div id="comment-66436-info" class="comment-info">
<span class="comment-age">(24 Oct '18, 11:44)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66423" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-66423-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66458"></span>

<div id="answer-container-66458" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66458-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I use overpass with leaflet and i have something like this</p>
<p>first checking nodes of clicked point queryOverpass(<code>[out:json]; way["building"~"."](around:10, 50.065342, 19.952249)-&gt;.interesting_ways; node(w.interesting_ways)-&gt;.allnodes; .allnodes out;</code>).then(console.log).catch(console.error);</p>
<p>and then beacuse i use radius (so this is approximately ) i am using leaflet function</p>
<pre><code>Polygon.getBounds().contains(MarketLatLng);</code></pre>
<p>Maybe it will help somebody</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '18, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/cd63a6756d8d22b50ff9faea27b00ab4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adacho26&#39;s gravatar image" />
<p><span>adacho26</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adacho26 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66458" class="comments-container">
&#10;</div>
<div id="comment-tools-66458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66458-form-container" class="comment-form-container">
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

