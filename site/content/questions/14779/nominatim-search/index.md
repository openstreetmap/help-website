+++
type = "question"
title = "Nominatim search"
description = '''I need help in nominatim search. i need to get nearest schools,banks,grocery stores, etc of a particular city. I found the keywords in http://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/EN, but i don&#x27;t know how it can use , i tried to give like http://nominatim.openstreetmap.org/search?q=g...'''
date = "2012-08-02T07:53:00Z"
lastmod = "2012-08-14T10:09:00Z"
weight = 14779
keywords = [ "openstreetmap", "map", "javascript", "nominatim" ]
aliases = [ "/questions/14779" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim search](/questions/14779/nominatim-search)

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
<span id="post-14779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14779-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need help in nominatim search. i need to get nearest schools,banks,grocery stores, etc of a particular city. I found the keywords in <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/EN">http://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/EN</a>, but i don't know how it can use , i tried to give like <a href="http://nominatim.openstreetmap.org/search?q=grocery,bangalore&amp;format=xml&amp;polygon=1&amp;addressdetails=1">http://nominatim.openstreetmap.org/search?q=grocery,bangalore&amp;format=xml&amp;polygon=1&amp;addressdetails=1</a> , but for some keywords no results getting. Can any one help me please..?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '12, 07:53</strong></p>
<img src="https://secure.gravatar.com/avatar/954504ad2324b1cbc000a0ddc2c2ba1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pramod_ck&#39;s gravatar image" />
<p><span>pramod_ck</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pramod_ck has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '12, 09:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-14779" class="comments-container">
<span id="14783"></span>
<div id="comment-14783" class="comment">
<div id="post-14783-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I've fixed the first link; the second worked for me. If you miss out the "format=xml" part of the query string you get the more usual nominatim search results.</p>
</div>
<div id="comment-14783-info" class="comment-info">
<span class="comment-age">(02 Aug '12, 09:15)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="14784"></span>
<div id="comment-14784" class="comment">
<div id="post-14784-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which grocery shops would you expect to find that Nominatim didn't? Do you have node or way IDs for any examples?</p>
<p>A search for fuel stations works:</p>
<p><a href="http://nominatim.openstreetmap.org/search.php?q=fuel%2Cbangalore&amp;viewbox=-161.72%2C79.92%2C161.72%2C-69.59&amp;polygon=1">http://nominatim.openstreetmap.org/search.php?q=fuel%2Cbangalore&amp;viewbox=-161.72%2C79.92%2C161.72%2C-69.59&amp;polygon=1</a></p>
<p>or in XML format</p>
<p><a href="http://nominatim.openstreetmap.org/search.php?format=xml&amp;q=fuel%2Cbangalore&amp;viewbox=-161.72%2C79.92%2C161.72%2C-69.59&amp;polygon=1">http://nominatim.openstreetmap.org/search.php?format=xml&amp;q=fuel%2Cbangalore&amp;viewbox=-161.72%2C79.92%2C161.72%2C-69.59&amp;polygon=1</a></p>
</div>
<div id="comment-14784-info" class="comment-info">
<span class="comment-age">(02 Aug '12, 09:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="14786"></span>
<div id="comment-14786" class="comment">
<div id="post-14786-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have this &lt;searchresults timestamp="Thu, 02 Aug 12 09:40:35 +0100" attribution="Data Copyright OpenStreetMap Contributors, Some Rights Reserved. CC-BY-SA 2.0." querystring="grocery,bangalore" polygon="true" more_url="http://nominatim.openstreetmap.org/search?format=xml&amp;amp;exclude_place_ids=&amp;amp;accept-language=en-GB,en-US;q=0.8,en;q=0.6&amp;amp;polygon=1&amp;amp;addressdetails=1&amp;amp;q=grocery%2Cbangalore"&gt;&lt;/searchresults&gt;</p>
</div>
<div id="comment-14786-info" class="comment-info">
<span class="comment-age">(02 Aug '12, 09:42)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="14787"></span>
<div id="comment-14787" class="comment">
<div id="post-14787-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>so what next</p>
</div>
<div id="comment-14787-info" class="comment-info">
<span class="comment-age">(02 Aug '12, 09:42)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="14789"></span>
<div id="comment-14789" class="comment">
<div id="post-14789-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span></span><span>@andy mackey</span> for me also getting same results. <span></span><span>@SomeoneElse</span> thanks it works, but in my site i need to show all grocery stores in bangalore. I searched how to use the keywords in nominatim, i found one example like <a href="http://nominatim.openstreetmap.org/search?q=bangalore%5Bhospitals%5D&amp;format=xml&amp;polygon=0&amp;addressdetails=1">http://nominatim.openstreetmap.org/search?q=bangalore[hospitals]&amp;format=xml&amp;polygon=0&amp;addressdetails=1</a> that also not working for all keywords.</p>
</div>
<div id="comment-14789-info" class="comment-info">
<span class="comment-age">(02 Aug '12, 09:53)</span> <span class="comment-user userinfo">pramod_ck</span>
</div>
</div>
</div>
<div id="comment-tools-14779" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14779-form-container" class="comment-form-container">
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

<span id="14797"></span>

<div id="answer-container-14797" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14797-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For the avoidance of doubt - grocery shops will only appear on the map and in the data in Bangalore if:</p>
<ol>
<li>Someone's actually added any to the map there.</li>
<li>They've tagged them as "shop=grocery"</li>
<li>They've subsequently agreed to the licence change so that the data is still there.</li>
</ol>
<p>If I go to "<a href="http://nominatim.openstreetmap.org">nominatim.openstreetmap.org</a>" and search for "shop near bangalore" I see two results - "<a href="http://nominatim.openstreetmap.org/details.php?place_id=7542324">Govt fair price shop</a>" and "<a href="http://nominatim.openstreetmap.org/details.php?place_id=7540868">Govt Kerosene retail shop</a>". They were both tagged as "shop=convenience". Unfortunately, the mapper of both of these <a href="http://www.openstreetmap.org/browse/node/704396287/history">didn't agree</a> to the <a href="http://www.osmfoundation.org/wiki/License/About_The_License_Change">licence change</a> and so, although they're still found by Nominatim until its data updates, they're no longer on the map.</p>
<p>A quick search for "<a href="http://nominatim.openstreetmap.org/search.php?q=supermarket+near+bangalore&amp;viewbox=77.63%2C13.01%2C77.68%2C12.97">supermarket near bangalore</a>" finds lots of hits, though, such as <a href="http://nominatim.openstreetmap.org/details.php?place_id=2487827295">this</a> <a href="http://www.openstreetmap.org/browse/way/169826257">one</a>, tagged as "shop=supermarket". If you're looking for grocery stores you'll need to think about how people might have tagged them, and perhaps use the <a href="http://wiki.openstreetmap.org/wiki/Xapi">XAPI</a> or <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass</a> to search for e.g. "shop=*" within the area that you're interested in.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '12, 12:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-14797" class="comments-container">
<span id="15058"></span>
<div id="comment-15058" class="comment">
<div id="post-15058-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can see all the shop= <em>in Bangalore through XAPI on this page: <a href="http://osm.dumoulin63.net/xapiviewer/?zoom=15&amp;lat=12.9725&amp;lon=77.58443&amp;layers=B0T&amp;icon=icons%2Fshopping_convenience.n.32.png&amp;request=shop%3D">http://osm.dumoulin63.net/xapiviewer/?zoom=15&amp;lat=12.9725&amp;lon=77.58443&amp;layers=B0T&amp;icon=icons%2Fshopping_convenience.n.32.png&amp;request=shop%3D</a></em></p>
</div>
<div id="comment-15058-info" class="comment-info">
<span class="comment-age">(14 Aug '12, 10:09)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
</div>
<div id="comment-tools-14797" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14797-form-container" class="comment-form-container">
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

