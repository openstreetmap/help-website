+++
type = "question"
title = "How to find road is urban or interurban?"
description = '''How to find road is urban or interurban?'''
date = "2015-06-22T09:48:00Z"
lastmod = "2015-06-25T09:23:00Z"
weight = 43690
keywords = [ "interurban", "urban", "or" ]
aliases = [ "/questions/43690" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to find road is urban or interurban?](/questions/43690/how-to-find-road-is-urban-or-interurban)

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
<span id="post-43690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43690-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How to find road is urban or interurban?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-interurban" rel="tag" title="see questions tagged &#39;interurban&#39;">interurban</span> <span class="post-tag tag-link-urban" rel="tag" title="see questions tagged &#39;urban&#39;">urban</span> <span class="post-tag tag-link-or" rel="tag" title="see questions tagged &#39;or&#39;">or</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '15, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/f5272d3a2e54ebca28981adbb4a3105f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gauravk&#39;s gravatar image" />
<p><span>Gauravk</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gauravk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43690" class="comments-container">
&#10;</div>
<div id="comment-tools-43690" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43690-form-container" class="comment-form-container">
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

<span id="43691"></span>

<div id="answer-container-43691" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43691-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-43691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a very difficult question to answer. Whether something is an urban road, or not, is quite subjective. OSM doesn't have good coverage of the physical descriptive things that would allow you decide whether a road is urban (e.g. lanes, road width, footpath, parking status). Maybe you could look at surrounding features (like how many km of residential roads there are? How many buildings are nearby? Speed limit of the road?)</p>
<p>Can I ask what you're trying to do? Perhaps there's a better solution?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '15, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-43691" class="comments-container">
<span id="43692"></span>
<div id="comment-43692" class="comment">
<div id="post-43692-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your suggestion. My end goal is to find the max speed.I have longitude and latitude value only. I put longitude and latitude value to url as a parameter: <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=</a>&lt;latitude&gt;&amp;lon=&lt;longitude&gt; Output: { "place_id": "72249684", "licence": "Data © OpenStreetMap contributors, ODbL 1.0. <a href="https://www.openstreetmap.org/copyright">https://www.openstreetmap.org/copyright",</a> "osm_type": "way", "osm_id": "78164485", "lat": "40.713746", "lon": "14.7016650663124", ......</p>
<p>For here I pass osm_id to another url to find speed limit: output</p>
<p>&lt;tag k="highway" v="motorway"/&gt; &lt;tag k="int_ref" v="E 45"/&gt; &lt;tag k="lanes" v="2"/&gt; &lt;tag k="lit" v="no"/&gt; &lt;tag k="maxspeed" v="90"/&gt; &lt;tag k="name" v="Autostrada A3 Napoli-Reggio Calabria"/&gt; &lt;tag k="oneway" v="yes"/&gt; &lt;tag k="ref" v="A3"/&gt; &lt;tag k="surface" v="asphalt"/&gt; &lt;/way&gt; &lt;/osm&gt;</p>
<p>From this output we can extract the maximum speed for that particular longitude and latitude in two ways First search for the ‘k="maxspeed"’ tag in the XML output, and extract the ‘v’ value for the tag. That represents the max speed in km/hrs. format.</p>
<p>If above tag not present search for ‘k="highway"’ tag, and get the ‘v’ attributes value; Next we need to have a lookup table from where we can get the default value for highway types. Please find the below link for lookup table for different country: <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Maxspeed.">https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Maxspeed.</a></p>
</div>
<div id="comment-43692-info" class="comment-info">
<span class="comment-age">(22 Jun '15, 10:35)</span> <span class="comment-user userinfo">Gauravk</span>
</div>
</div>
<span id="43713"></span>
<div id="comment-43713" class="comment">
<div id="post-43713-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Gauravk, is there a kind of government (city, regional, provincial and country wide), who have a highway plan released with categories like the one you’re searching ? Those plans should or could contain urban or interurban ways and eventually other categories of ways.</p>
</div>
<div id="comment-43713-info" class="comment-info">
<span class="comment-age">(22 Jun '15, 21:45)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="43743"></span>
<div id="comment-43743" class="comment">
<div id="post-43743-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for you comment. Its is kind of GPS. Still no luck I hope someone will help me out here.</p>
</div>
<div id="comment-43743-info" class="comment-info">
<span class="comment-age">(24 Jun '15, 07:29)</span> <span class="comment-user userinfo">Gauravk</span>
</div>
</div>
<span id="43745"></span>
<div id="comment-43745" class="comment">
<div id="post-43745-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is no easy solution to your problem. The only thing you can do is creating a heuristic based on the information mentioned in rorym's answer. Currently most routers don't even create complex heuristics but instead just look at the highway class and surface value if no maxspeed tag is present.</p>
</div>
<div id="comment-43745-info" class="comment-info">
<span class="comment-age">(24 Jun '15, 08:21)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="43748"></span>
<div id="comment-43748" class="comment">
<div id="post-43748-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks scai,How can I use Tag:surface for urban area?</p>
</div>
<div id="comment-43748-info" class="comment-info">
<span class="comment-age">(24 Jun '15, 09:54)</span> <span class="comment-user userinfo">Gauravk</span>
</div>
</div>
<span id="43749"></span>
<div id="comment-43749" class="comment not_top_scorer">
<div id="post-43749-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's not what I meant. But you can use it additionally to the highway class to <em>guess</em> the maxspeed if it is not present.</p>
</div>
<div id="comment-43749-info" class="comment-info">
<span class="comment-age">(24 Jun '15, 10:10)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43691" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-43691-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43773"></span>

<div id="answer-container-43773" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43773-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Although I am not sure about your practical reasons, here is one possible geometry based option. The answer is an interpretation/application of a higher grade student task in algorithms to your case (naturally, many fine details are left out). 1. Assume, from an OSM Planet-dump (or from other OSM based sources) and for an area of interest you have extracted all area objects that you consider as "urban" (e.g. landuse=residential, and landuse=industrial ... add filters as you wish). For practical/efficiency reasons you could merge and convert this set of areas into a set "U" of disjunctive closed simple areas (no common border sections, borders belong to the areas and one outer with arbitrary inner borders in relations).<br />
2. Assume, you have a road "R" from road-class of interest (e.g. from primary roads) as a polygonal line (careful about the roundabouts, long edge-vectors...). Also, assume you have a distance criteria "D" (e.g. 50m) what you consider as a critical distance whether a point or a vector might be considered as "urban" or not.<br />
Now, for any of the edge vectors of R find the closest element from U at distance d (minimum distance d, between a point of the vector and a point of the area). If this distance d is less than D mark the vector as "u" (urban). At the end, all consecutive vectors/edges marked with "u" form/create your urban road sections and the contrary.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '15, 09:23</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-43773" class="comments-container">
&#10;</div>
<div id="comment-tools-43773" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43773-form-container" class="comment-form-container">
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

