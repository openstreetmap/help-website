+++
type = "question"
title = "Scope of Nominatim"
description = '''Hi, I set up my own Nominatim instance, because I wanted to generate Latitude / Longitude for all addresses in germany. Before I did that, I found an .csv file online with Lat / Lon for all german addresses, it had almost 11 millionen entries. When I was checking randomly the missing addresses on my...'''
date = "2016-08-31T09:00:00Z"
lastmod = "2016-09-01T11:54:00Z"
weight = 51836
keywords = [ "nominatim", "osmfilter" ]
aliases = [ "/questions/51836" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Scope of Nominatim](/questions/51836/scope-of-nominatim)

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
<span id="post-51836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51836-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I set up my own Nominatim instance, because I wanted to generate Latitude / Longitude for all addresses in germany.</p>
<p>Before I did that, I found an .csv file online with Lat / Lon for all german addresses, it had almost 11 millionen entries.</p>
<p>When I was checking randomly the missing addresses on my Nominatim instance, I found out that it doesnt provide me with more addresses. The only thing that Nominatim does, when u enter an address with a housenumbeer that seemed to not exist, is to give back lat / long for an already existing address with a lower housenumber.</p>
<p>I did convert the germany-latest.osm.pbf to a .o5m-file and then checked the following with osmfilter: <img src="/upfiles/osm_adressenzahl11millionen.png" alt="alt text" /></p>
<p>My question is now: Even with my own Nominatim Instance, if I use it with the germany-latest.osm.pbf file, it wont provide me with more addresses then the germany-latest.osm.pbf contains (red square), is that correct? Or is there some kind of a trick, that Nominatim can calculate new addresses with an algorithm or anything similar (that was what I expected to be honoust)?</p>
<p>Thank in advance, Stephano</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '16, 09:00</strong></p>
<img src="https://secure.gravatar.com/avatar/4aeaae6ed1cbb7581b9338affb59e4d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stephano007&#39;s gravatar image" />
<p><span>Stephano007</span><br />
<span class="score" title="61 reputation points">61</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stephano007 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-51836" class="comments-container">
<span id="51841"></span>
<div id="comment-51841" class="comment">
<div id="post-51841-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes mtmail, the .csv file is derived from OSM data.</p>
<p>I was tryin to build a geo-database for lat / lon enrichment for addresses.</p>
<p>It does not has to be that accurate, so If I have my 11 millionen addresses, I could write a script that will create housenumbers for every street up to housenumber 1000, using the lat / lot from a housenumber of that street that is already existent in the database of 11 millionen addresses. With that derived data, I could still do analyses about customer rates in for example city destricts etc. , is that correct?</p>
</div>
<div id="comment-51841-info" class="comment-info">
<span class="comment-age">(31 Aug '16, 10:30)</span> <span class="comment-user userinfo">Stephano007</span>
</div>
</div>
<span id="51854"></span>
<div id="comment-51854" class="comment">
<div id="post-51854-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I can comment on Nominatim, but can't say if you can do analysis of customer rates (another data set). Creating the additional address records in the Nominatim database will too time and disc-space intensive. OpenStreetmap worldwide currently has 60 million house-numbers and you want to create 500 million or more for Germany. There are still many streets in Germany that don't have any buildings or house numbers mapped, you'd essentially guessing data. An analysis on street level, ignoring house numbers, might work better.</p>
</div>
<div id="comment-51854-info" class="comment-info">
<span class="comment-age">(01 Sep '16, 11:54)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-51836" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51836-form-container" class="comment-form-container">
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

<span id="51838"></span>

<div id="answer-container-51838" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51838-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While obviously technically Nominatim could be expanded to extrapolate locations for addresses that are not contained in the database. Given that doesn't mean that such addresses actually exist, it is probably outside the current design goals of Nominatim (you can naturally write such an extension yourself and make it available).</p>
<p>As mtmail noted, the above applies to not explicitly mapped interpolations (there we assume that everything between start and end address exists using the resp. interval).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '16, 09:28</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Aug '16, 10:21</strong> </span></p>
</div>
</div>
<div id="comments-container-51838" class="comments-container">
&#10;</div>
<div id="comment-tools-51838" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51838-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51839"></span>

<div id="answer-container-51839" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51839-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the .csv file contained 11 million entries then it's most likely exported or derived from OSM data (and should have proper license/attribution) because the with 80m citizens and 37m households one would expect more house numbers to exist in Germany. The 11m probably contains duplicates, e.g. when a building has an address and a POI (shop etc) in the building is also marked with the same house number.</p>
<p>As Simon already said Nominatim support address interpolation (<a href="https://wiki.openstreetmap.org/wiki/Addresses#Using_interpolation)">https://wiki.openstreetmap.org/wiki/Addresses#Using_interpolation)</a> where a mapper only marks the beginning and end of a street and the house numbers in between are guessed, we don't know if they really exist. Mappers use interpolation rarely in Germany, it's much more common in for example South America.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '16, 09:50</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-51839" class="comments-container">
&#10;</div>
<div id="comment-tools-51839" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51839-form-container" class="comment-form-container">
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

