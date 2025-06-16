+++
type = "question"
title = "How to get state list for a country?"
description = '''I need to get a list of states for every country(by country code). it&#x27;s possible with overpass QL? I wrote this code and it&#x27;s works fine. but it&#x27;s takes a long time to be executed for countries like &quot;us&quot;: [timeout:900]; area[&quot;ISO3166-1&quot;=&quot;us&quot;][&quot;admin_level&quot;=&quot;2&quot;];(rel(area)[&quot;admin_level&quot;=&quot;4&quot;];); out q...'''
date = "2013-12-30T22:15:00Z"
lastmod = "2017-02-12T23:31:00Z"
weight = 29485
keywords = [ "states", "country", "overpass-api" ]
aliases = [ "/questions/29485" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to get state list for a country?](/questions/29485/how-to-get-state-list-for-a-country)

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
<span id="post-29485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29485-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to get a list of states for every country(by country code). it's possible with overpass QL?</p>
<p>I wrote this code and it's works fine. but it's takes a long time to be executed for countries like "us":</p>
<p>[timeout:900]; area["ISO3166-1"="us"]["admin_level"="2"];(rel(area)["admin_level"="4"];); out qt;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-states" rel="tag" title="see questions tagged &#39;states&#39;">states</span> <span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '13, 22:15</strong></p>
<img src="https://secure.gravatar.com/avatar/57fadcd89e00b509fec577a14acc3447?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Izikb&#39;s gravatar image" />
<p><span>Izikb</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Izikb has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Dec '13, 07:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span></p>
</div>
</div>
<div id="comments-container-29485" class="comments-container">
&#10;</div>
<div id="comment-tools-29485" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29485-form-container" class="comment-form-container">
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

<span id="29486"></span>

<div id="answer-container-29486" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29486-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well indeed it is possible, but not that easy. The reason is that the country informations are attached at the country boundaries and the way how OSM models them are the so called <a href="https://wiki.openstreetmap.org/wiki/Relation">'relations'</a>. In short this are container objects that can hold other OSM objects (here: the OSM ways that create the outer shape of a country).</p>
<p>For boundaries there is a <a href="https://wiki.openstreetmap.org/wiki/Boundaries">boundary relation</a> that holds all the single ways of the (shared by 2..n countries!) borders. Unfortunatly esp. on national level, the meaning of the levels can be different, so you might need to check/adapt your request per country. So you need:</p>
<ol>
<li>Get a relation ID of the desired country (maybe with an editor or by walking trough the relation IDs)</li>
<li>Request the relation object by Overpass-API</li>
<li>Get all child objects that are refered within the relation</li>
<li>Check if the child-ways fit seamless together and maybe fix broken ways/relations</li>
<li>Process whatever you like...</li>
</ol>
<p>Steps 3,4 are optional if you want to do some real geospatial processing or rendering of the shape.</p>
<p>In short: If you really just need a (string) list, it might be easier to get it from Wikipedia?<br />
(I heard they are working on that Wikidata thing?)<br />
It depends you understanding of country code (domain, RFC3066, <a href="http://www.iso.org/iso/prods-services/iso3166ma/02iso-3166-code-lists/country_names_and_code_elements">ISO3166</a>, ...) if you might happily find other lists on the net...</p>
<p>For Germany we have this pretty nice page to get GeoJSON of our countries/cities/... <a href="http://ags.misterboo.de"></a><a href="http://ags.misterboo.de">http://ags.misterboo.de</a> but AFAIK there is nothing similar with global coverage, not even at <a href="http://openstreetmapdata.com/data">http://openstreetmapdata.com/data</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '13, 23:25</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Dec '13, 23:28</strong> </span></p>
</div>
</div>
<div id="comments-container-29486" class="comments-container">
<span id="29487"></span>
<div id="comment-29487" class="comment">
<div id="post-29487-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks! I wrote this code and it's works fine. but it's takes a long time to be executed for countries like "us":</p>
<pre><code>[timeout:900];
area[&quot;ISO3166-1&quot;=&quot;us&quot;][&quot;admin_level&quot;=&quot;2&quot;];(rel(area)[&quot;admin_level&quot;=&quot;4&quot;];);
out qt;</code></pre>
<p>what I doing wrong?</p>
</div>
<div id="comment-29487-info" class="comment-info">
<span class="comment-age">(30 Dec '13, 23:46)</span> <span class="comment-user userinfo">Izikb</span>
</div>
</div>
</div>
<div id="comment-tools-29486" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29486-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54614"></span>

<div id="answer-container-54614" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54614-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This query is fast, but currently only results in 47 states for the US:</p>
<p><code>rel[admin_level=4]["is_in:country_code"=US];</code></p>
<p>This query is equally fast, but includes some things that you may not consider a "state". Like for the US it includes Guam.</p>
<p><code>rel[admin_level=4]["ISO3166-2"~"^US-"];</code></p>
<p>The reason both of these queries are fast is because it is just looking up the info based on tags rather than determining if the boundaries are within the country's boundary. Depending on your needs, they may be good enough.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '17, 23:31</strong></p>
<img src="https://secure.gravatar.com/avatar/c49788c38bdb7c114ccf27d800a3bd73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joshcoady&#39;s gravatar image" />
<p><span>joshcoady</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joshcoady has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54614" class="comments-container">
&#10;</div>
<div id="comment-tools-54614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54614-form-container" class="comment-form-container">
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

