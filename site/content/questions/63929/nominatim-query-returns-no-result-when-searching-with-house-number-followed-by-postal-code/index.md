+++
type = "question"
title = "Nominatim query returns no result when searching with House number followed by postal code"
description = '''I have setup nominatim in my server and its working fine but if I search a address with the following pattern its not returning any geocoding results: city/street name/House No./postal code OR city/street name/postal code/House No. But returning result for same if I supply the post code before stree...'''
date = "2018-05-31T22:05:00Z"
lastmod = "2018-06-01T21:56:00Z"
weight = 63929
keywords = [ "postalcode", "openstreetmap", "housenumbers", "nominatim", "geocoding" ]
aliases = [ "/questions/63929" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim query returns no result when searching with House number followed by postal code](/questions/63929/nominatim-query-returns-no-result-when-searching-with-house-number-followed-by-postal-code)

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
<span id="post-63929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63929-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have setup nominatim in my server and its working fine but if I search a address with the following pattern its not returning any geocoding results:</p>
<p>city/street name/House No./postal code OR city/street name/postal code/House No.</p>
<p>But returning result for same if I supply the post code before street name or or city. city/postal code/street name/House No. OR postal code/city/street name/House No.</p>
<p>For Example: Working : <a href="https://nominatim.openstreetmap.org/search.php?q=brussels+1000+allee+verte+10+&amp;polygon_geojson=1&amp;viewbox=">https://nominatim.openstreetmap.org/search.php?q=brussels+1000+allee+verte+10+&amp;polygon_geojson=1&amp;viewbox=</a></p>
<p>Not working: <a href="https://nominatim.openstreetmap.org/search.php?q=brussels+allee+verte+10+1000&amp;polygon_geojson=1&amp;viewbox=">https://nominatim.openstreetmap.org/search.php?q=brussels+allee+verte+10+1000&amp;polygon_geojson=1&amp;viewbox=</a></p>
<p>It would also be helpful if you can let me know what is the correct way to search and if i missing something. Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postalcode" rel="tag" title="see questions tagged &#39;postalcode&#39;">postalcode</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '18, 22:05</strong></p>
<img src="https://secure.gravatar.com/avatar/ac0f41ae33fc8543acc12aaae64309a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="suroKarma&#39;s gravatar image" />
<p><span>suroKarma</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="suroKarma has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 May '18, 22:13</strong> </span></p>
</div>
</div>
<div id="comments-container-63929" class="comments-container">
&#10;</div>
<div id="comment-tools-63929" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63929-form-container" class="comment-form-container">
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

<span id="63931"></span>

<div id="answer-container-63931" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63931-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Commas will help Nominatim to distinguish the address components better. They're optional, but for postcode and housenumbers next to each other useful. Try <a href="https://nominatim.openstreetmap.org/search.php?q=brussels%2C+allee+verte+10%2C+1000&amp;polygon_geojson=1">https://nominatim.openstreetmap.org/search.php?q=brussels%2C+allee+verte+10%2C+1000&amp;polygon_geojson=1</a> (Here the exact building <a href="https://www.openstreetmap.org/node/2640980784">https://www.openstreetmap.org/node/2640980784</a> isn't found because the street is named 'Allée Verte - Groendreef', not 'Allée Verte').</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '18, 23:40</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-63931" class="comments-container">
<span id="63932"></span>
<div id="comment-63932" class="comment">
<div id="post-63932-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>which is still strange, as the street has name:fr and name:nl. When I <a href="https://www.openstreetmap.org/search?query=groendreef%2010%2C%20brussel#map=19/50.86388/4.35434">search</a> for Groendreef 10, Brussel, the third answer is that building.</p>
<p>The same for <a href="https://www.openstreetmap.org/search?query=allee%20verte%2010%2C%20bruxelles#map=19/50.86388/4.35434">allee verte 10, bruxelles</a>.</p>
<p>It's even the only answer for "allee verte 10, 1000" or "brussels, allee verte 10"</p>
<p>So just use comma's to seperate city/street + housenumber/postal.</p>
</div>
<div id="comment-63932-info" class="comment-info">
<span class="comment-age">(01 Jun '18, 04:16)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="63934"></span>
<div id="comment-63934" class="comment">
<div id="post-63934-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for answering, the street has two names one in fr and one in nl so any of the name should be fine.</p>
<p>But if i get input from a consumer and the address parts may jumble and i don't have control over the request then if i put a comma after each address parts still for some combination it wont work.</p>
<p>for example: <a href="https://nominatim.openstreetmap.org/search.php?q=brussels%2C+All%C3%A9e+Verte+-+Groendreef%2C+10%2C+1000&amp;polygon_geojson=1&amp;viewbox=">https://nominatim.openstreetmap.org/search.php?q=brussels%2C+All%C3%A9e+Verte+-+Groendreef%2C+10%2C+1000&amp;polygon_geojson=1&amp;viewbox=</a></p>
<p>But in the the below case i'm getting a response but not the exact house address: <a href="https://nominatim.openstreetmap.org/search.php?q=brussels%2C+allee+verte+10%2C+1000&amp;polygon_geojson=1&amp;viewbox=">https://nominatim.openstreetmap.org/search.php?q=brussels%2C+allee+verte+10%2C+1000&amp;polygon_geojson=1&amp;viewbox=</a></p>
</div>
<div id="comment-63934-info" class="comment-info">
<span class="comment-age">(01 Jun '18, 08:58)</span> <span class="comment-user userinfo">suroKarma</span>
</div>
</div>
<span id="63936"></span>
<div id="comment-63936" class="comment">
<div id="post-63936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>but its strange if i parse only &lt;street&gt;,&lt;house number=""&gt;,&lt;post code=""&gt; which is without the city name but in the same order, its working.</p>
<p><a href="https://nominatim.openstreetmap.org/search.php?q=allee+verte%2C+10%2C+1000&amp;polygon_geojson=1&amp;viewbox=">https://nominatim.openstreetmap.org/search.php?q=allee+verte%2C+10%2C+1000&amp;polygon_geojson=1&amp;viewbox=</a></p>
</div>
<div id="comment-63936-info" class="comment-info">
<span class="comment-age">(01 Jun '18, 10:49)</span> <span class="comment-user userinfo">suroKarma</span>
</div>
</div>
<span id="63948"></span>
<div id="comment-63948" class="comment">
<div id="post-63948-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nomatim has its limitations on recognizing the parts. Why do you insist on putting Brussels in front ? As I showed above, it works when Brussels is placed at the end. It even <a href="https://www.openstreetmap.org/search?query=groendreef%2010%20brussels#map=19/50.86388/4.35434">works</a> without comma then.</p>
</div>
<div id="comment-63948-info" class="comment-info">
<span class="comment-age">(01 Jun '18, 21:56)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-63931" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63931-form-container" class="comment-form-container">
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

