+++
type = "question"
title = "How to filter only street names and city id in osmfilter?"
description = '''Hello, I&#x27;m newbie with the .osm files and I&#x27;m trying to get All streets names from a Country with the ID of the city, filtering the file with osmfilter. Now I&#x27;m trying to get them with: ./osmfilter ...o5m --keep=&quot;highway=cycleway highway=path highway=primary highway=residential highway=tertiary&quot; &amp;gt...'''
date = "2014-04-06T17:58:00Z"
lastmod = "2014-04-12T11:15:00Z"
weight = 32163
keywords = [ "city", "streets", "osmfilter", "name" ]
aliases = [ "/questions/32163" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter only street names and city id in osmfilter?](/questions/32163/how-to-filter-only-street-names-and-city-id-in-osmfilter)

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
<span id="post-32163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32163-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I'm newbie with the .osm files and I'm trying to get All streets names from a Country with the ID of the city, filtering the file with osmfilter. Now I'm trying to get them with: ./osmfilter ...o5m --keep="highway=cycleway highway=path highway=primary highway=residential highway=tertiary" &gt; ....o5m But I'm getting nodes without bodies and I can't figure out which is the City ID.</p>
<p>Regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-streets" rel="tag" title="see questions tagged &#39;streets&#39;">streets</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Apr '14, 17:58</strong></p>
<img src="https://secure.gravatar.com/avatar/b1f1fd6379c69bc7e75b9eb7f90afdf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Petar81&#39;s gravatar image" />
<p><span>Petar81</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Petar81 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Apr '14, 18:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-32163" class="comments-container">
<span id="32203"></span>
<div id="comment-32203" class="comment not_top_scorer">
<div id="post-32203-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>are you sure that you only get an osm file with only nodes and NO ways?</p>
<p>And about the city where each way belongs to: Tell us where any filter program should know what belongs to a single city in the area you need. Are there good boundary relations or boundary ways for each city? or do you want to differentiate address data via the addr:city tag?</p>
</div>
<div id="comment-32203-info" class="comment-info">
<span class="comment-age">(08 Apr '14, 15:53)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="32227"></span>
<div id="comment-32227" class="comment not_top_scorer">
<div id="post-32227-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello, I'm not familiar with osm files like I said, I don't know if I need to get ways or nodes, I read somewhere in the documentation that for each street there is ID of the City which it belongs to. I extracted the Cities successfuly and now I'm trying to get the streets. That's all. I want to put them in 2 MySQL Tables and list them Cities and Streets</p>
</div>
<div id="comment-32227-info" class="comment-info">
<span class="comment-age">(09 Apr '14, 16:18)</span> <span class="comment-user userinfo">Petar81</span>
</div>
</div>
<span id="32229"></span>
<div id="comment-32229" class="comment">
<div id="post-32229-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Would it be possible to link to the "I read somewhere..." link?</p>
</div>
<div id="comment-32229-info" class="comment-info">
<span class="comment-age">(09 Apr '14, 16:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="32239"></span>
<div id="comment-32239" class="comment">
<div id="post-32239-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Petar, if you want to use raw OSM data for your aims you should at least get familiar with the model of OSM elements ... see <a href="http://wiki.openstreetmap.org/wiki/Elements">http://wiki.openstreetmap.org/wiki/Elements</a> as a starting point.</p>
<p>You wrote: "I extracted the cities successfully" ... How did you do that in detail?? Tell us please so that we can lead you to a solution.</p>
<p>Getting a list of all streets belonging to a certain city is definitively possible with OSM data.</p>
</div>
<div id="comment-32239-info" class="comment-info">
<span class="comment-age">(09 Apr '14, 19:33)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="32290"></span>
<div id="comment-32290" class="comment not_top_scorer">
<div id="post-32290-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Like I said I used OSMFILTER for this:</p>
<p>./osmfilter32 country.o5m --keep="place=city or place=town" --ignore-dependencies --keep-tags="all place= is_in:country= name:bg= name:en=" &gt; coutry-cities.o5m</p>
<p>Simple as that. Now I'm trying to get ALL street. I'm now using "&lt;way&gt;" and to keep the "addr:tag" BUT it not all &lt;way&gt;s have addr:city..., THIS is my osmfilter details: ./osmfilter32 coutry.o5m --keep-ways --drop-nodes --keep-tags="is_in:country= name:en= name= name:bg=" --keep="highway=cycleway or highway=path or highway=primary or highway=residential or highway=tertiary"</p>
<blockquote>
<p>country-streets.o5m</p>
</blockquote>
</div>
<div id="comment-32290-info" class="comment-info">
<span class="comment-age">(11 Apr '14, 11:36)</span> <span class="comment-user userinfo">Petar81</span>
</div>
</div>
<span id="32294"></span>
<div id="comment-32294" class="comment">
<div id="post-32294-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please be aware that having any addr: tag on any highway in the main OSM data you have downloaded is basically WRONG!</p>
<p>Because addr: tags are to determine the position of addresses, and NOT any streets belonging to a city.</p>
<p>So if you have cities or places with addr: tags in your area, that is "not so good tagging style" about the raw OSM data.</p>
</div>
<div id="comment-32294-info" class="comment-info">
<span class="comment-age">(11 Apr '14, 12:26)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="32296"></span>
<div id="comment-32296" class="comment not_top_scorer">
<div id="post-32296-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So that's just Wrong, ok. Then how to use the raw OSM data to get streets names with Cities without Polygon in MySQL?</p>
</div>
<div id="comment-32296-info" class="comment-info">
<span class="comment-age">(11 Apr '14, 12:55)</span> <span class="comment-user userinfo">Petar81</span>
</div>
</div>
<span id="32298"></span>
<div id="comment-32298" class="comment">
<div id="post-32298-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You need polygons, or to be more exact in OSM language: you need boundary relations that display the boundary around a city or a place.</p>
<p>It depends on the area what you are aiming at whethet these boundary relations are already in OSM database.</p>
<p>Either tell us the area you are aiming at, or have a look on your own via <a href="http://openmapsurfer.uni-hd.de">http://openmapsurfer.uni-hd.de</a> -&gt; choose layer: OSM roads grayscale and overlay: OSM admin boundaries.</p>
</div>
<div id="comment-32298-info" class="comment-info">
<span class="comment-age">(11 Apr '14, 14:14)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="32300"></span>
<div id="comment-32300" class="comment not_top_scorer">
<div id="post-32300-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm aming at: user inputs City from database and that selects all streets from the City. Can you give me example how to extract all Cities and Streets from given Country and put them into MySQL? Thank you in advance =)</p>
</div>
<div id="comment-32300-info" class="comment-info">
<span class="comment-age">(11 Apr '14, 14:42)</span> <span class="comment-user userinfo">Petar81</span>
</div>
</div>
<span id="32301"></span>
<div id="comment-32301" class="comment not_top_scorer">
<div id="post-32301-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Re "... that selects all streets from the City" - what criteria should be used to determine that a particular street is within the city?</p>
</div>
<div id="comment-32301-info" class="comment-info">
<span class="comment-age">(11 Apr '14, 14:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="32302"></span>
<div id="comment-32302" class="comment not_top_scorer">
<div id="post-32302-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The criteria is if it is in the city(even if it continues to other city) or it's very small in size, to be shown as IN the city. And only show up 1 in the results(because I read that a street can be represented as multiple vectors).</p>
</div>
<div id="comment-32302-info" class="comment-info">
<span class="comment-age">(11 Apr '14, 14:50)</span> <span class="comment-user userinfo">Petar81</span>
</div>
</div>
<span id="32303"></span>
<div id="comment-32303" class="comment">
<div id="post-32303-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OK, but how does the server that you're talking to know whether it's in a city or not? A way in OSM will NOT have an attribute of what city it's in - it just has nodes, each of which has a latitude and longitude value (as previously mentioned, see <a href="http://wiki.openstreetmap.org/wiki/Elements">http://wiki.openstreetmap.org/wiki/Elements</a> for more info).</p>
</div>
<div id="comment-32303-info" class="comment-info">
<span class="comment-age">(11 Apr '14, 14:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="32305"></span>
<div id="comment-32305" class="comment not_top_scorer">
<div id="post-32305-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I found this link: <a href="http://cdn.oreillystatic.com/en/assets/1/event/56/Openstreetmap%20-">http://cdn.oreillystatic.com/en/assets/1/event/56/Openstreetmap%20-</a><em>%20_PostGIS%7CMySQL%7CSpatiaLite</em>%20-<em>%20OpenLayers</em>%20From%20Map%20to%20Web%20Presentation.pdf</p>
<p>The guy which has created it, have tables(if you see page 21): 1) Planet_osm_polygon 2) Planet_osm_roads He's using Planet polygon for cities(not sure how) and he has separate table for all roads.</p>
<p>But how to separate the Cities in the Planet_osm_polygon?</p>
<p>I want to do it like here: <a href="http://services.gisgraphy.com/public/geocoding_worldwide.htm">http://services.gisgraphy.com/public/geocoding_worldwide.htm</a> Choose Country, choose City, list all Streets. How can it be done?</p>
</div>
<div id="comment-32305-info" class="comment-info">
<span class="comment-age">(11 Apr '14, 15:24)</span> <span class="comment-user userinfo">Petar81</span>
</div>
</div>
</div>
<div id="comment-tools-32163" class="comment-tools">
<span class="comments-showing"> showing 5 of 13 </span> <a href="#" class="show-all-comments-link">show 8 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-32163-form-container" class="comment-form-container">
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

<span id="32308"></span>

<div id="answer-container-32308" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32308-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>looking further at the website of gisgraphy.com they say that their framework is opensource, and they have installation instructions if you want to set up an own server.</p>
<p>Have you tried that already?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '14, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-32308" class="comments-container">
<span id="32313"></span>
<div id="comment-32313" class="comment">
<div id="post-32313-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is one problem - This is JAVA application. I need it to be PHP. Secondly for the server part I will need 155 GB of space which is a lot for just Streetnames and cities... Is there an alternative way I can use for PHP?</p>
</div>
<div id="comment-32313-info" class="comment-info">
<span class="comment-age">(12 Apr '14, 11:15)</span> <span class="comment-user userinfo">Petar81</span>
</div>
</div>
</div>
<div id="comment-tools-32308" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32308-form-container" class="comment-form-container">
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

