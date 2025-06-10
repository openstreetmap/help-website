+++
type = "question"
title = "Can&#x27;t find a state anymore in nominatim (there is a city with the same name)"
description = '''I used to find objects inside the São Paulo State by simply using &quot;São Paulo&quot; in nominatim. Likewise, objcets inside the city of São Paulo could be found by using &quot;SP&quot;. Now it seems that something has changed and, no matter what kind of combination of &quot;SP&quot; and &quot;São Paulo&quot; I use, they all return the ...'''
date = "2019-07-27T03:39:00Z"
lastmod = "2019-08-08T20:01:00Z"
weight = 70212
keywords = [ "nominatim" ]
aliases = [ "/questions/70212" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can't find a state anymore in nominatim (there is a city with the same name)](/questions/70212/cant-find-a-state-anymore-in-nominatim-there-is-a-city-with-the-same-name)

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
<span id="post-70212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70212-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I used to find objects inside the <a href="https://www.openstreetmap.org/relation/298204">São Paulo State</a> by simply using "São Paulo" in nominatim. Likewise, objcets inside the <a href="https://www.openstreetmap.org/relation/298285">city of São Paulo</a> could be found by using "SP".</p>
<p>Now it seems that something has changed and, no matter what kind of combination of "SP" and "São Paulo" I use, they all return the city as the first result (and this also affects overpass queries).</p>
<p>Some examples that I did try without success:</p>
<ul>
<li><a href="https://nominatim.openstreetmap.org/search.php?q=S%C3%A3o+Paulo&amp;polygon_geojson=1">São Paulo</a></li>
<li><a href="https://nominatim.openstreetmap.org/search.php?q=SP&amp;polygon_geojson=1">SP</a></li>
<li><a href="https://nominatim.openstreetmap.org/search.php?q=State+of+São+Paulo&amp;polygon_geojson=1">State of São Paulo</a></li>
<li><a href="https://nominatim.openstreetmap.org/search.php?q=São+Paulo%2C+Brasil&amp;polygon_geojson=1">São Paulo, Brasil</a></li>
<li><a href="https://nominatim.openstreetmap.org/search.php?q=São+Paulo+state&amp;polygon_geojson=1">São Paulo state</a></li>
<li><a href="https://nominatim.openstreetmap.org/search.php?q=São+Paulo%2C+southeast+region&amp;polygon_geojson=1">São Paulo, southeast region</a></li>
<li><a href="https://nominatim.openstreetmap.org/search.php?q=São+Paulo%2C+southeast+region%2C+brazil&amp;polygon_geojson=1">São Paulo, southeast region, brazil</a></li>
<li>You got the idea</li>
</ul>
<p>What do I need to do to differentiate if I want to search for the city or for the State, when both have the same name, please?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '19, 03:39</strong></p>
<img src="https://secure.gravatar.com/avatar/c605758904cf00f577053e4e130f89a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naoliv&#39;s gravatar image" />
<p><span>naoliv</span><br />
<span class="score" title="600 reputation points">600</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naoliv has 3 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-70212" class="comments-container">
&#10;</div>
<div id="comment-tools-70212" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70212-form-container" class="comment-form-container">
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

<span id="70213"></span>

<div id="answer-container-70213" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70213-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="naoliv has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Both have the same <code>name</code> and <code>short_name</code>. Which of state or the city are more relevant as first result is debatable, both are in the top 5 results. Since the city is inside the state there is no phrase you can add to the Nominatim query to make it prefer one or the other, Nominatim doesn't have tag filters like some other search engine do. Same issue with many state capitals around the world: Washington D.C. (both city and district), Berlin (city and state), Vienna. Does Overpass allow setting the osm_id instead?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '19, 03:59</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-70213" class="comments-container">
<span id="70348"></span>
<div id="comment-70348" class="comment">
<div id="post-70348-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indeed, we can search/filter by the area (relation) id <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29</a> For my case <a href="https://overpass-turbo.eu/s/LpZ">https://overpass-turbo.eu/s/LpZ</a> Thanks!</p>
</div>
<div id="comment-70348-info" class="comment-info">
<span class="comment-age">(08 Aug '19, 20:01)</span> <span class="comment-user userinfo">naoliv</span>
</div>
</div>
</div>
<div id="comment-tools-70213" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70213-form-container" class="comment-form-container">
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

