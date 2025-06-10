+++
type = "question"
title = "Extracting country, name, lon, lat fields for every city/town, village on the planet"
description = '''Hi! I&#x27;m working on my bachelor thesis on the topic of how urban areas across the world cluster based on their walkable urban forms and the presence of greenery. For this, I need a large dataset of cities/towns/villages around the planet paired with their country and longitude and latitude values in ...'''
date = "2020-11-07T15:11:00Z"
lastmod = "2020-11-08T23:08:00Z"
weight = 77434
keywords = [ "osmconvert", "osmfilter" ]
aliases = [ "/questions/77434" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting country, name, lon, lat fields for every city/town, village on the planet](/questions/77434/extracting-country-name-lon-lat-fields-for-every-citytown-village-on-the-planet)

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
<span id="post-77434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77434-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I'm working on my bachelor thesis on the topic of how urban areas across the world cluster based on their walkable urban forms and the presence of greenery. For this, I need a large dataset of cities/towns/villages around the planet paired with their country and longitude and latitude values in the .csv format. I've downloaded the north-america-latest.osm.pbf, and I've been trying to extract data with my desired fields out of it for three days with osmfilter and osmconvert, but I'm just not having any luck. I first tried to extract only towns from north-america-latest.osm.pbf with &gt;osmfilter north-america-latest.osm_01.o5m --keep="place=town" --drop-version --ignore-dependencies --drop-relations --drop-ways -o=north-america-cities.osm&lt; and adding the longitude and latitude fields with osmconvert. This worked, but only for towns and I have no idea how to add the countries to it and I can't really find any resources about how to go about this, the wiki isn't really helpful here to a beginner. It seems to be that what I want, isn't really all that complex, so it shouldn't be this hard?</p>
<p>I would really really appreciate any advice and help.</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Nov '20, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/445c1723bc83ffe4df9ba6ca33dd9c8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tian&#39;s gravatar image" />
<p><span>Tian</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tian has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77434" class="comments-container">
&#10;</div>
<div id="comment-tools-77434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77434-form-container" class="comment-form-container">
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

<span id="77435"></span>

<div id="answer-container-77435" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77435-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The pbf format stores the OpenStreetMap data in a way that is convenient for multi-user, versioned editing. The country usually isn't attached to the item that represents a city or town (there's not restriction, so it might be). Country boundaries are usually present in the data (but the process used to create a country file might omit them).</p>
<p>The solution is to pass the location to a country level geocoder. I don't know if there is one that is particularly easy to install; for thousands of points a local instance is probably better than trying to run them through a free service.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '20, 18:27</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-77435" class="comments-container">
<span id="77437"></span>
<div id="comment-77437" class="comment">
<div id="post-77437-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for responding so promptly! I will look into some python geocoders then. Other than that, what is the best way to query for cities, towns and villages? Is it via addr or place? Thank you!</p>
</div>
<div id="comment-77437-info" class="comment-info">
<span class="comment-age">(07 Nov '20, 21:58)</span> <span class="comment-user userinfo">Tian</span>
</div>
</div>
<span id="77439"></span>
<div id="comment-77439" class="comment">
<div id="post-77439-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The <code>place</code> tag. It's probably a worthwhile exercise to examine the values used in some areas you are familiar with, in case you are interested in more than village/town/city.</p>
</div>
<div id="comment-77439-info" class="comment-info">
<span class="comment-age">(07 Nov '20, 23:42)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="77451"></span>
<div id="comment-77451" class="comment">
<div id="post-77451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, thank you! I've managed to extract the data for north-america-latest.osm.pbf after converting it to 'osm.o5m' format and then using osmfilter, but following the exact same steps with south-america-latest.osm.pbf, osmfilter gives the warning 'Warning: unexpected end of input file: south-america-latest.osm_01.o5m', which causes a write error when using osmconvert to produce a .csv file. I've used the osmconBert to convert the formats from pbf to o5m, so I don't know how this end of input file could be happening, do you know by any chance?</p>
</div>
<div id="comment-77451-info" class="comment-info">
<span class="comment-age">(08 Nov '20, 23:08)</span> <span class="comment-user userinfo">Tian</span>
</div>
</div>
</div>
<div id="comment-tools-77435" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77435-form-container" class="comment-form-container">
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

