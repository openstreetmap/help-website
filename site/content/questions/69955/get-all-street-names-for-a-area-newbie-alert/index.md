+++
type = "question"
title = "get all street names for a area &quot;Newbie Alert&quot;"
description = '''Hi im as new as can be to OSM im looking for a way to divide up a city into four parts and get all the street names of each area, from googling around i can see there is a way but i have no idea how to use OSM so its not so helpfull (remember go easy im a newbie) pls be nice to the rookie and help o...'''
date = "2019-07-09T19:33:00Z"
lastmod = "2019-07-12T03:15:00Z"
weight = 69955
keywords = [ "openstreetmap", "street", "streetnames", "road" ]
aliases = [ "/questions/69955" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [get all street names for a area "Newbie Alert"](/questions/69955/get-all-street-names-for-a-area-newbie-alert)

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
<span id="post-69955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69955-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi im as new as can be to OSM im looking for a way to divide up a city into four parts and get all the street names of each area, from googling around i can see there is a way but i have no idea how to use OSM so its not so helpfull (remember go easy im a newbie) pls be nice to the rookie and help out. Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '19, 19:33</strong></p>
<img src="https://secure.gravatar.com/avatar/9e3a09c93f408b1f16f2daa7cae61821?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zgivod&#39;s gravatar image" />
<p><span>zgivod</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zgivod has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69955" class="comments-container">
<span id="69961"></span>
<div id="comment-69961" class="comment">
<div id="post-69961-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is this a one time task for a specific city or do you need a reproducible approach?</p>
<p>How do you want to divide up the city? By drawing a cross (so basically by coordinates) or along certain features (rivers, suburb boundaries)?</p>
</div>
<div id="comment-69961-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 09:32)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="69974"></span>
<div id="comment-69974" class="comment">
<div id="post-69974-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10133/tzorn">@TZorn</a> it would be with coordinates and just a one time task. thanks so much</p>
</div>
<div id="comment-69974-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 18:31)</span> <span class="comment-user userinfo">zgivod</span>
</div>
</div>
</div>
<div id="comment-tools-69955" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69955-form-container" class="comment-form-container">
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

<span id="69978"></span>

<div id="answer-container-69978" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69978-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="zgivod has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use Overpass Turbo to generate a list of all mapped streets in an area.</p>
<p><a href="http://overpass-turbo.eu/s/KDM">This code</a> would for example return all named highways meant for traffic with all their attributes in the city of Kiel:</p>
<pre><code>[out:json][timeout:25];
// fetch area “Kiel” to search in
{{geocodeArea:Kiel}}-&gt;.searchArea;
// gather results
(
 way[highway~&quot;^(motorway|trunk|primary|secondary|tertiary|unclassified|residential|living_street|pedestrian)$&quot;][name](area.searchArea);
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>Klick on the data button on the top right hand side to see the data. You would have to extract all the "name": "xyz street" to get your list of names. Maybe someone more Overpass savvy can find a leaner approach for just extracting the names.</p>
<p>You could use <a href="http://overpass-turbo.eu/s/KDP">a slightly different query</a> to define your quadrants:</p>
<pre><code>[out:json][timeout:25]
// define area:
[bbox:50.6,7.0,50.7,7.1];
// gather results
(  way[highway~&quot;^(motorway|trunk|primary|secondary|tertiary|unclassified|residential|living_street|pedestrian)$&quot;];
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '19, 21:18</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jul '19, 21:27</strong> </span></p>
</div>
</div>
<div id="comments-container-69978" class="comments-container">
<span id="69981"></span>
<div id="comment-69981" class="comment">
<div id="post-69981-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>that helps a little bit thanks! i can always copy and paste the code to a code that i am familiar with and using my own coding experience i can get every word that follows name: now i am wondering is there a way to get actual home addresses in a coordinates area is that possible?</p>
</div>
<div id="comment-69981-info" class="comment-info">
<span class="comment-age">(11 Jul '19, 00:59)</span> <span class="comment-user userinfo">zgivod</span>
</div>
</div>
<span id="69982"></span>
<div id="comment-69982" class="comment">
<div id="post-69982-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is a csv mode:</p>
<pre><code>[out:csv(name)][timeout:25]
// define area:
[bbox:50.6,7.0,50.7,7.1];
// gather results
(     way[highway~&quot;^(motorway|trunk|primary|secondary|tertiary|unclassified|residential|living_street|pedestrian)$&quot;];
);
// print results
out;</code></pre>
<p>It doesn't deal with duplicate names though.</p>
<p>For addresses, you'd search on <code>addr:housenumber</code>.</p>
</div>
<div id="comment-69982-info" class="comment-info">
<span class="comment-age">(11 Jul '19, 03:00)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="69990"></span>
<div id="comment-69990" class="comment">
<div id="post-69990-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> that works amazing. Thanks! since im very new and not familler with the code where to i search addr:housenumber ?</p>
</div>
<div id="comment-69990-info" class="comment-info">
<span class="comment-age">(11 Jul '19, 15:03)</span> <span class="comment-user userinfo">zgivod</span>
</div>
</div>
<span id="69991"></span>
<div id="comment-69991" class="comment">
<div id="post-69991-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>House numbers are mostly on the buildings, POIs, entrances or pure address nodes but can also be in a combination of way/node (interpolation). Sometimes numbers and streets are associated through a "associated street" relation. Have a look a the <a href="https://wiki.openstreetmap.org/wiki/Addresses">Addresses wiki page</a> to get familiar on how house numbers are mapped in OSM. You can extract the data similarly as with the streets but it depends a on what you want to do with the data how to do it exactly.</p>
</div>
<div id="comment-69991-info" class="comment-info">
<span class="comment-age">(11 Jul '19, 15:12)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="69993"></span>
<div id="comment-69993" class="comment">
<div id="post-69993-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i see.... but im still very unfamiller with the code, what would be an example code with addr:housenumber with <a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> code above?</p>
</div>
<div id="comment-69993-info" class="comment-info">
<span class="comment-age">(11 Jul '19, 17:12)</span> <span class="comment-user userinfo">zgivod</span>
</div>
</div>
<span id="69994"></span>
<div id="comment-69994" class="comment not_top_scorer">
<div id="post-69994-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What is it you want to achieve? Surely not just a list of all house numbers? I guess you want at least all addresses including street name and house number. You have to be a bit more precise for anyone to help.</p>
</div>
<div id="comment-69994-info" class="comment-info">
<span class="comment-age">(11 Jul '19, 17:35)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="69995"></span>
<div id="comment-69995" class="comment not_top_scorer">
<div id="post-69995-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes sorry for being unprecise im looking for all addresses including street name and house number in specific coordinates</p>
</div>
<div id="comment-69995-info" class="comment-info">
<span class="comment-age">(11 Jul '19, 17:56)</span> <span class="comment-user userinfo">zgivod</span>
</div>
</div>
<span id="69999"></span>
<div id="comment-69999" class="comment not_top_scorer">
<div id="post-69999-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>replace the <code>way[highway...</code> part with <code>nwr["addr:housenumber"];</code>. nwr is a shortcut to search on all types of osm objects.</p>
<p>Then replace the <code>out:csv(name)</code> part with something like <code>out:csv("addr:street","addr:housenumber")</code>. You also may want to include some more tags, take a look at <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/House_numbers/Karlsruhe_Schema#Tags">https://wiki.openstreetmap.org/wiki/Proposed_features/House_numbers/Karlsruhe_Schema#Tags</a> .</p>
</div>
<div id="comment-69999-info" class="comment-info">
<span class="comment-age">(12 Jul '19, 03:15)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-69978" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-69978-form-container" class="comment-form-container">
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

