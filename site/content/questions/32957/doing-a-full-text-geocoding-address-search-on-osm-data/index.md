+++
type = "question"
title = "Doing a full-text geocoding address search on OSM data?"
description = '''I&#x27;m currently downloading OSM data of the Netherlands, with the plan to import and query the data in MongoDB. However, I have a very specific use-case. I need to do a full-text search of an address string, which can contain anything from the street address to the postal code, (sub-)district, provinc...'''
date = "2014-05-08T03:29:00Z"
lastmod = "2014-05-09T15:10:00Z"
weight = 32957
keywords = [ "mongodb", "nominatim", "geocoding", "address" ]
aliases = [ "/questions/32957" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Doing a full-text geocoding address search on OSM data?](/questions/32957/doing-a-full-text-geocoding-address-search-on-osm-data)

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
<span id="post-32957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32957-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently downloading OSM data of the Netherlands, with the plan to import and query the data in MongoDB.</p>
<p>However, I have a very specific use-case. I need to do a full-text search of an address string, which can contain anything from the street address to the postal code, (sub-)district, province, state, country, etc. For example, I would like to search for any of the following strings in the database:</p>
<ul>
<li>Grand Parkview Asoke Flr. 11, Unit 444/12 Sukhumvit 21 10110 Bangkok</li>
<li>Grand Parkview Asoke, Sukhumvit</li>
<li>Sukhumvit 21 Bangkok</li>
<li>etc.</li>
</ul>
<p>In all of these cases, the "address" that matches all of these searches the most would be something like the following:</p>
<pre><code>{
    country: &quot;Thailand&quot;,
    city: &quot;Bangkok&quot;,
    city_district: &quot;Watthana District&quot;,
    neighborhood: &quot;Sukhumvit&quot;,
    postal_code: 10110
    street: &quot;Sukhumvit&quot;
}</code></pre>
<p>The problem is that OSM data isn't setup like this, i.e. there is no <code>node</code> that contains all of this information. Rather there are different nodes such as streets, districts, neighborhoods etc. that are in one way or another linked with each other. My question is how can I search for the entire address string,like "Grand Parkview Asoke Flr. 11 Unit 444/12 Sukhumvit 21 10110 Bangkok", to determine what other information we know about this address. For example, in this case we know that this address is in Thailand.</p>
<p>So, should I restructure the data to be able to perform such searches? Or would there be another way of achieving such geocoding?</p>
<p>If anything is unclear, please ask for further elaboration.</p>
<p>P. S. I know about nominatim, but I have to run this locally. Nominatim's local installation requires a server with 32GB+ of RAM for the planet, which is why I would like to try and implement my specific needs using MongoDB as to hopefully achieve a less resource intensive application.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mongodb" rel="tag" title="see questions tagged &#39;mongodb&#39;">mongodb</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '14, 03:29</strong></p>
<img src="https://secure.gravatar.com/avatar/04361eba6e039eecdd3458e2545f03e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomM&#39;s gravatar image" />
<p><span>TomM</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomM has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 May '14, 03:31</strong> </span></p>
</div>
</div>
<div id="comments-container-32957" class="comments-container">
&#10;</div>
<div id="comment-tools-32957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32957-form-container" class="comment-form-container">
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

<span id="32960"></span>

<div id="answer-container-32960" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32960-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-32960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TomM has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim doesn't <em>require</em> 32 GB of RAM; you can run it on a machine with much less. The weakest point is the initial data loading which greatly benefits from having more RAM (for caching); if you run an initial data load on a machine with, say, only 4 GB of RAM and no SSDs then it will very likely take between two and four weeks to complete.</p>
<p>Having said that, the data import and using the data are two separate issues; you could for example run the import on a high-memory rented server somewhere, and then download a database dump to your local low-memory machine for using it. There's already a <a href="https://github.com/komoot/photon">geocoder based on Apache Solr</a> which uses only the data import part of Nominatim and builds its own search on top of that.</p>
<p>Nominatim contains a lot of logic to try and build an address hierarchy like the one you're after, and it is not very likely that you will be able to re-invent a better version of this wheel without spending a huge amount of time. "MongoDB vs Postgres" is probably just a side issue - I should be very surprised if building a proper hierarchy from the whole planet's data were any faster on a MongoDB powered system than on a Postgres powered one.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 May '14, 08:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-32960" class="comments-container">
<span id="32961"></span>
<div id="comment-32961" class="comment">
<div id="post-32961-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting, so if I rent a 32GB system and then transfer the resulting database to another system with less resources, what kind of system would you recommend? E.g. would 2GB of RAM be enough? And would the requirements be lower if I use the Apache Solr based geocoder?</p>
</div>
<div id="comment-32961-info" class="comment-info">
<span class="comment-age">(08 May '14, 09:16)</span> <span class="comment-user userinfo">TomM</span>
</div>
</div>
<span id="33009"></span>
<div id="comment-33009" class="comment">
<div id="post-33009-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The usual advice is to start with a <a href="http://download.geofabrik.de/">small extract</a>, experiment with it, and progressively try with bigger extracts until you tacle the whole planet.</p>
</div>
<div id="comment-33009-info" class="comment-info">
<span class="comment-age">(08 May '14, 21:57)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="33026"></span>
<div id="comment-33026" class="comment">
<div id="post-33026-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know about the requirements of the Solr based geocoder. 2 GB of RAM would certainly be enough to <em>run</em> Nominatim but I can't say how fast it would be; it could take a few seconds to resolve a query.</p>
</div>
<div id="comment-33026-info" class="comment-info">
<span class="comment-age">(09 May '14, 08:57)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="33048"></span>
<div id="comment-33048" class="comment">
<div id="post-33048-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hello Tom, maybe you can have a look at "Pelias" which was now added in the OSM overwiew page <a href="https://wiki.openstreetmap.org/wiki/Search_engines">https://wiki.openstreetmap.org/wiki/Search_engines</a></p>
</div>
<div id="comment-33048-info" class="comment-info">
<span class="comment-age">(09 May '14, 15:10)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-32960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32960-form-container" class="comment-form-container">
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

