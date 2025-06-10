+++
type = "question"
title = "ZIP code may be prevent locating address"
description = '''I have a problem locating an address (10000 S 400 E, Markleville, IN, 46056). When I search for 46056 alone it brings up two towns, Emporia and Markleville. People in Emporia have a 46056 zip code, but they have Markleville addresses. I suspect that when I search for 46056 that Emporia should not be...'''
date = "2012-11-26T22:37:00Z"
lastmod = "2012-11-30T12:43:00Z"
weight = 17995
keywords = [ "city", "search", "nominatim", "address", "zip-code" ]
aliases = [ "/questions/17995" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ZIP code may be prevent locating address](/questions/17995/zip-code-may-be-prevent-locating-address)

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
<span id="post-17995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17995-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a problem locating an address (10000 S 400 E, Markleville, IN, 46056). When I search for 46056 alone it brings up two towns, Emporia and Markleville. People in Emporia have a 46056 zip code, but they have Markleville addresses. I suspect that when I search for 46056 that Emporia should not be listed. If I (incorrectly) change the city in the address above to Emporia the address is correctly plotted on the map.</p>
<p>I think there is some kind of incorrect zip code entry that makes nominatim think that people have Emporia addresses when they should all be Markleville addresses. What would be the way to correct the problem?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-zip-code" rel="tag" title="see questions tagged &#39;zip-code&#39;">zip-code</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '12, 22:37</strong></p>
<img src="https://secure.gravatar.com/avatar/69c21e426e2f19730f0d983a2f1e8847?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dennis%20Wallen&#39;s gravatar image" />
<p><span>Dennis Wallen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dennis Wallen has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>27 Nov '12, 05:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/01d01832dff61a6bcf68913f1dc001bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Circeus&#39;s gravatar image" />
<p><span>Circeus</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span></p>
</div>
</div>
<div id="comments-container-17995" class="comments-container">
<span id="17999"></span>
<div id="comment-17999" class="comment">
<div id="post-17999-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why, if you are searching (presumably) for the <em>zipcode alone</em> would it <em>not</em> make sense that the database returns all inhabited places it locates within that zipcode?</p>
</div>
<div id="comment-17999-info" class="comment-info">
<span class="comment-age">(27 Nov '12, 05:40)</span> <span class="comment-user userinfo">Circeus</span>
</div>
</div>
<span id="18005"></span>
<div id="comment-18005" class="comment">
<div id="post-18005-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Germany has an interesting concept to solve this problem (and to avoid heuristics that may fail) : it maps boundaries for postal_code areas that frequently do not follow the administrative areas and their hierarchy of admin_level's.</p>
<p>This case is not unique, it exists in many countries, and postcode areas generaly do not evolve at the same time as administrative areas.</p>
<p>The same could be said to regional phone areas (the 3 digits in US and Canada before the local 7-digit phone number).</p>
</div>
<div id="comment-18005-info" class="comment-info">
<span class="comment-age">(27 Nov '12, 08:35)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="18046"></span>
<div id="comment-18046" class="comment">
<div id="post-18046-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Circeus, there is nothing inherently wrong with returning all cities/towns that share the same zip code. That could certainly be useful as a feature.</p>
<p>My road has tags that point it to the 46056 zip code so it should be able to figure out that I have a Markleville address. They are TIGER tags so maybe there needs to be a "postalCode" tag? When nominatim tries to find me it seems to be insisting that I have an Emporia address. I think that because it returns Emporia first and then Markleville when searching only by ZIP code.</p>
<p>I'm just trying to figure out how to corretly locate my address.</p>
</div>
<div id="comment-18046-info" class="comment-info">
<span class="comment-age">(28 Nov '12, 01:10)</span> <span class="comment-user userinfo">Dennis Wallen</span>
</div>
</div>
<span id="18068"></span>
<div id="comment-18068" class="comment">
<div id="post-18068-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You might go to the Nominatim page (<a href="http://nominatim.openstreetmap.org/search)">http://nominatim.openstreetmap.org/search)</a> and enter different terms and see what results you get. Note that you can click on Details for each result and get more info about it. So, for example, the zip codes appear to be nodes that aren't in OSM. There are two nodes for 46056, so there's no reason why Nominatim would know you're in one or the other. Your address doesn't have a road name (it's x,y style), which is something that might help it determine the correct city (municipal boundaries are parents for roads within them).</p>
</div>
<div id="comment-18068-info" class="comment-info">
<span class="comment-age">(28 Nov '12, 15:20)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-17995" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17995-form-container" class="comment-form-container">
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

<span id="18086"></span>

<div id="answer-container-18086" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18086-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-18086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem with your address is not the postcode but the <a href="http://www.openstreetmap.org/browse/relation/127615">administrative boundary for Markleville</a>. It only encloses the village itself. Road S 400 E is outside the village according to that. Nominatim then messes up a little bit as you can see on the <a href="http://nominatim.openstreetmap.org/details.php?place_id=31403768">details page for the road</a>. It actually places your road into Emporia because it is the closest village that does not have a boundary defined.</p>
<p>To correct the situation, I'd recommend to do two things: add a addr:city=Markleville tag to your street, so that Nominatim knows to which village the road belongs, and then define a proper boundary relation for Emporia, so it knows to which village the road does not belong.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '12, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-18086" class="comments-container">
<span id="18117"></span>
<div id="comment-18117" class="comment">
<div id="post-18117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But DOES this road belong to Markleville adminsitratively? I bet no, otherwise the boundary of Markleville would include the road and its surrounding households. So These households belong to another administrative town/city, Emporia, and Emporia has several ZIPs.</p>
<p>To correct this the Germany solution (which is to map the postal code areas independantly of administrative boundaries) is a good solution. It allows a town to have several postal code areas, or the same postal area covering multiple towns or parts of them. And it's much easier than tagging each address node or street in that area.</p>
</div>
<div id="comment-18117-info" class="comment-info">
<span class="comment-age">(30 Nov '12, 11:34)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="18118"></span>
<div id="comment-18118" class="comment">
<div id="post-18118-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And effectively, Emporia needs its own administrative boundary (covering that street, even if its postal addresses are handled in Markleville) : here again the postal area of Emporia does not cover the whole administrative town but only a part of it, excluding this street which is in another postal area.</p>
<p>So: add the administrative boundary for Emporia, and add the two distinct boundaries for the postal areas of Emporia and Markleville. You then don't need to tag the streets to their postal areas, this is implicit. But you still need to associate the households to their street relation.</p>
</div>
<div id="comment-18118-info" class="comment-info">
<span class="comment-age">(30 Nov '12, 11:41)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="18119"></span>
<div id="comment-18119" class="comment">
<div id="post-18119-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note also that the admininstrative boundary of the city of Markleville has two small enclaves that are excluded administratively. To which city they belong then administratively? It's unknown (OSM does not specify it for these enclaves), even if they are in the postal area of Markleville (also not specified: Nominatim "guesses" it should be Markleville).</p>
<p>Once again the postal area does not match the admininstrative boundary of the city, and the German solution (mapping separate postal boundary relations) is excellent to cover these cases without complex tagging for each household or street.</p>
</div>
<div id="comment-18119-info" class="comment-info">
<span class="comment-age">(30 Nov '12, 11:54)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="18120"></span>
<div id="comment-18120" class="comment">
<div id="post-18120-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>As Dennis was looking for the address '10000 S 400 E, Markleville, IN, 46056', I dared to assume that Markleville is part of the postal address for this street even though it may not be within the administrative boundaries of the village. The answer relates to exactly this special case.</p>
<p>The area of the postal code is completely irrelevant here, it is the town name that prevents Nominatim from finding the address. (Nominatim does get the postcode completely right, searching for 'S 400 E, 46056' returns the correct street.)</p>
</div>
<div id="comment-18120-info" class="comment-info">
<span class="comment-age">(30 Nov '12, 12:43)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-18086" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18086-form-container" class="comment-form-container">
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

