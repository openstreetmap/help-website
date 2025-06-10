+++
type = "question"
title = "Get Street like an element not chunks without relation"
description = '''Hello! Im triying to get streets like unique element, but open street maps returns me the id of the chunk and a chunk that doesnt have a clearly relation between the other chunks of the same street and if i use the name like identifier sometimes in a small radius that name of street repeats and i ca...'''
date = "2019-08-29T07:59:00Z"
lastmod = "2019-08-29T23:28:00Z"
weight = 70543
keywords = [ "indentify", "indentifier" ]
aliases = [ "/questions/70543" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get Street like an element not chunks without relation](/questions/70543/get-street-like-an-element-not-chunks-without-relation)

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
<span id="post-70543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70543-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello! Im triying to get streets like unique element, but open street maps returns me the id of the chunk and a chunk that doesnt have a clearly relation between the other chunks of the same street and if i use the name like identifier sometimes in a small radius that name of street repeats and i cant get the street like an element. Any idea? thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-indentify" rel="tag" title="see questions tagged &#39;indentify&#39;">indentify</span> <span class="post-tag tag-link-indentifier" rel="tag" title="see questions tagged &#39;indentifier&#39;">indentifier</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Aug '19, 07:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ade8a947ba75b44a417615043cfff3f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markvex&#39;s gravatar image" />
<p><span>markvex</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markvex has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70543" class="comments-container">
<span id="70544"></span>
<div id="comment-70544" class="comment">
<div id="post-70544-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What are you trying to accomplish?</p>
</div>
<div id="comment-70544-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 08:26)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="70545"></span>
<div id="comment-70545" class="comment">
<div id="post-70545-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Get all the chunks of a street from a query. The only way i found was using the name of the street and a bounding box, but sometimes it returns two different near streets that are called equal...</p>
</div>
<div id="comment-70545-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 08:35)</span> <span class="comment-user userinfo">markvex</span>
</div>
</div>
<span id="70551"></span>
<div id="comment-70551" class="comment">
<div id="post-70551-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What is "a street" to you? How do you define it? Is it just the having the same name, or exactly the same highway tag (look at some of the elements of <a href="https://overpass-turbo.eu/s/LUL">https://overpass-turbo.eu/s/LUL</a> for example). What about <a href="https://overpass-turbo.eu/s/LUM">https://overpass-turbo.eu/s/LUM</a> ? Is "High Street East" there part of the same street as "High Street" to the west? Is the pedestrian area to the west part of the same street?</p>
</div>
<div id="comment-70551-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 10:30)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70553"></span>
<div id="comment-70553" class="comment">
<div id="post-70553-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For me in that example that you gave me those are different elements /streets. I know that different chunks are necesary to label it with their own properties but in this case street is the same and one chunk doesnt have a relation to the others =&gt; "http://lz4.overpass-api.de/api/interpreter?data=[out:json];%20way[%27highway%27]<a href="42.597639598334,-5.5825567245483,42.617538785605,-5.5655193328857">%22name%22=%27Calle%20Lope%20de%20Vega%27</a>;%20out;%20%3E;%20out%20skel%20qt;"</p>
</div>
<div id="comment-70553-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 10:40)</span> <span class="comment-user userinfo">markvex</span>
</div>
</div>
<span id="70554"></span>
<div id="comment-70554" class="comment">
<div id="post-70554-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you link to that in OSM? Across the world there are many streets with that name: <a href="https://overpass-turbo.eu/s/LUO">https://overpass-turbo.eu/s/LUO</a> .</p>
</div>
<div id="comment-70554-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 10:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70555"></span>
<div id="comment-70555" class="comment not_top_scorer">
<div id="post-70555-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, and in 2km around as well...thats the problem why i cannot limit it. The thing is that actually the postman can deliver the package to the correct street because ZIP adds a unique id to differ one street to another with the same name but open street maps doesnt supply me anything to know we are talking about the same element</p>
</div>
<div id="comment-70555-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 10:46)</span> <span class="comment-user userinfo">markvex</span>
</div>
</div>
<span id="70556"></span>
<div id="comment-70556" class="comment not_top_scorer">
<div id="post-70556-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you link to the area that you are talking about in OSM? Without that, we've no idea where in the world you're talking about.</p>
</div>
<div id="comment-70556-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 10:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70557"></span>
<div id="comment-70557" class="comment not_top_scorer">
<div id="post-70557-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Im talking in general to some cases for example in spain, most of the cities have that problem</p>
</div>
<div id="comment-70557-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 11:05)</span> <span class="comment-user userinfo">markvex</span>
</div>
</div>
<span id="70560"></span>
<div id="comment-70560" class="comment not_top_scorer">
<div id="post-70560-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sounds like it's <a href="https://overpass-turbo.eu/s/LV0">here</a></p>
</div>
<div id="comment-70560-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 12:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70543" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-70543-form-container" class="comment-form-container">
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

<span id="70546"></span>

<div id="answer-container-70546" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70546-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no ready-made API that would give you that. It is also often subject to interpretation, as a street could well have gaps in it where there's a small plaza or something - when is it still "the same street"? What you can do is download all the chunks and look at the node IDs at either end - if two chunks share a node id then they belong together. But even if you do that you will often not end up with a linear object since it is not unusual to have little stubs branching off that carry the same name as the main street...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '19, 09:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70546" class="comments-container">
<span id="70547"></span>
<div id="comment-70547" class="comment">
<div id="post-70547-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But nodes wont be shared so i can get a relation in there rigth?</p>
</div>
<div id="comment-70547-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 09:38)</span> <span class="comment-user userinfo">markvex</span>
</div>
</div>
<span id="70548"></span>
<div id="comment-70548" class="comment">
<div id="post-70548-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you say this again, I don't understand where relations come into it.</p>
</div>
<div id="comment-70548-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 09:40)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="70549"></span>
<div id="comment-70549" class="comment not_top_scorer">
<div id="post-70549-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I mean, i can check if some chunks are of the same street by the node id independently of the name they have edit: i have check that and its only usefull in cases where the street chunks are stick to the next, if there is something in the middle nodes doesnt relate...so..How get the whole street?</p>
</div>
<div id="comment-70549-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 09:46)</span> <span class="comment-user userinfo">markvex</span>
</div>
</div>
<span id="70550"></span>
<div id="comment-70550" class="comment">
<div id="post-70550-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>All streets are connected somehow. The node at the end of one street will be connected to another street, e.g. here: <a href="https://www.openstreetmap.org/node/17716584">https://www.openstreetmap.org/node/17716584</a> so if you <em>only</em> check connectedness then all streets in the city are one!</p>
</div>
<div id="comment-70550-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 09:58)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="70552"></span>
<div id="comment-70552" class="comment not_top_scorer">
<div id="post-70552-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not always check "http://lz4.overpass-api.de/api/interpreter?data=[out:json];%20way[%27highway%27]<a href="42.597639598334,-5.5825567245483,42.617538785605,-5.5655193328857">%22name%22=%27Calle%20Lope%20de%20Vega%27</a>;%20out;%20%3E;%20out%20skel%20qt;" One chunk of that street its not related to the others and its the same street</p>
</div>
<div id="comment-70552-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 10:38)</span> <span class="comment-user userinfo">markvex</span>
</div>
</div>
<span id="70558"></span>
<div id="comment-70558" class="comment">
<div id="post-70558-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>One chunk of that street its not related to the others and its the same street</p>
</blockquote>
<p>Which actual street are you talking about?</p>
</div>
<div id="comment-70558-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 11:15)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70559"></span>
<div id="comment-70559" class="comment not_top_scorer">
<div id="post-70559-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Calle Lope de Vega, León, España</p>
</div>
<div id="comment-70559-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 11:52)</span> <span class="comment-user userinfo">markvex</span>
</div>
</div>
<span id="70561"></span>
<div id="comment-70561" class="comment not_top_scorer">
<div id="post-70561-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you're talking about <a href="https://www.openstreetmap.org/way/46509089">this street</a>, you can see that the last node of the way (594795551) is connected to <a href="https://www.openstreetmap.org/way/496936666">another way with the same name</a>.</p>
</div>
<div id="comment-70561-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 16:53)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="70563"></span>
<div id="comment-70563" class="comment not_top_scorer">
<div id="post-70563-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Although <a href="https://www.openstreetmap.org/way/680382506">this</a> has no name, it does have pieces named "Calle Lope de Vega" at each end. It's up to you whether you consider them all part of the "same street" or not - that's why I asked those questions in comments above.</p>
</div>
<div id="comment-70563-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 21:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70564"></span>
<div id="comment-70564" class="comment">
<div id="post-70564-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It would really help us if you can describe what goal you're trying to reach once you have this data.</p>
</div>
<div id="comment-70564-info" class="comment-info">
<span class="comment-age">(29 Aug '19, 23:28)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-70546" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-70546-form-container" class="comment-form-container">
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

