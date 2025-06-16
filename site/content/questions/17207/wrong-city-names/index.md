+++
type = "question"
title = "Wrong city names"
description = '''Hi, I&#x27;m new to OpenStreetMap so forgive me if this is a naive question. I am exploring the use of the Nominatim service/API and notice that for the Bay Area of California the city names are completely wrong.  For example, when I specify the location of the Marriott in Downtown San Jose and do a nomi...'''
date = "2012-10-26T17:52:00Z"
lastmod = "2013-12-04T19:56:00Z"
weight = 17207
keywords = [ "city", "reversegeocoding", "nominatim" ]
aliases = [ "/questions/17207" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wrong city names](/questions/17207/wrong-city-names)

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
<span id="post-17207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17207-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm new to OpenStreetMap so forgive me if this is a naive question. I am exploring the use of the Nominatim service/API and notice that for the Bay Area of California the city names are completely wrong.<br />
</p>
<p>For example, when I specify the location of the Marriott in Downtown San Jose and do a nominatim lookup:</p>
<pre><code>http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=37.330144&amp;lon=-121.889052&amp;zoom=18&amp;addressdetails=1</code></pre>
<p>I get back:</p>
<pre><code>&lt;addressparts&gt;
&lt;hotel&gt;Marriott&lt;/hotel&gt;
&lt;road&gt;South Market Street&lt;/road&gt;
&lt;city&gt;Santa Clara&lt;/city&gt;
&lt;county&gt;Santa Clara County&lt;/county&gt;
&lt;state&gt;California&lt;/state&gt;
&lt;postcode&gt;95113&lt;/postcode&gt;
&lt;country&gt;United States of America&lt;/country&gt;
&lt;country_code&gt;us&lt;/country_code&gt;
&lt;/addressparts&gt;</code></pre>
<p>Everything is absolutely correct except for the city name, which should be San Jose.</p>
<p>Similarly, picking the lat/long of the oval park on Stanford's Campus I get a similar wrong city name.</p>
<pre><code>http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=37.429806&amp;lon=-122.169491&amp;zoom=18&amp;addressdetails=1</code></pre>
<pre><code>&lt;addressparts&gt;
&lt;common&gt;The Oval Park&lt;/common&gt;
&lt;road&gt;Palm Drive&lt;/road&gt;
&lt;place&gt;Southgate&lt;/place&gt;
&lt;city&gt;Santa Clara&lt;/city&gt;
&lt;county&gt;Santa Clara County&lt;/county&gt;
&lt;state&gt;California&lt;/state&gt;
&lt;postcode&gt;94305-6072&lt;/postcode&gt;
&lt;country&gt;United States of America&lt;/country&gt;
&lt;country_code&gt;us&lt;/country_code&gt;
&lt;/addressparts&gt;</code></pre>
<p>In all the cases that I've tested, it <em>seems</em> that the county name is being incorrectly used for the city. I'm not sure if this is an OSM data problem, or a logic problem with Nominatim.</p>
<p>Any help on how to get this resolved would be very much appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Oct '12, 17:52</strong></p>
<img src="https://secure.gravatar.com/avatar/69eff4676356be8a3abea72ea1a7fe32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JBiehl&#39;s gravatar image" />
<p><span>JBiehl</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JBiehl has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '13, 15:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-17207" class="comments-container">
<span id="17482"></span>
<div id="comment-17482" class="comment">
<div id="post-17482-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've been investigating this on my own for a bit, and I'm at a loss for why Nominatim is still returning the wrong city names for the reverse queries.<br />
</p>
<p>As folks suggested on this post, all the cities where this is an issue DO have relations to represent the administrative boundaries, and those relations seem to be properly labeled (as do the ways). I have compared the relations for the cities in the Bay Area to those in other part of California where Nominatim DOES get the city names right, and I can't tell any difference.</p>
<p>If anyone could help identify what is going on I'd be very appreciative. We'd like to use this service in a project, but if the data is not accurate we'll unfortunately have to look at the commercial options.</p>
</div>
<div id="comment-17482-info" class="comment-info">
<span class="comment-age">(05 Nov '12, 03:42)</span> <span class="comment-user userinfo">JBiehl</span>
</div>
</div>
<span id="17605"></span>
<div id="comment-17605" class="comment">
<div id="post-17605-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the responses.</p>
<p>I have two additional questions:<br />
</p>
<p>1) How long does it take for changes to a relation to propagate to Nominatim? Seems like even after a few days the changes are not reflected.</p>
<p>2) I still think that something else is going on with the data. Forget San Jose for the moment (because Nominatim still thinks the relation is broken). Take the Los Altos Post Office:</p>
<p><a href="http://nominatim.openstreetmap.org/details.php?place_id=3431300">http://nominatim.openstreetmap.org/details.php?place_id=3431300</a></p>
<p>As you can see from the details, Nominatim is finding the Los Altos Administrative Boundary (which is a correct/valid relation), but is <em>still</em> identifying it's city as Santa Clara (which should obviously be Los Altos).</p>
<p>Thanks in advance for any insight into what is going on here.</p>
</div>
<div id="comment-17605-info" class="comment-info">
<span class="comment-age">(09 Nov '12, 06:02)</span> <span class="comment-user userinfo">JBiehl</span>
</div>
</div>
<span id="17606"></span>
<div id="comment-17606" class="comment">
<div id="post-17606-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>At first glance the above seems like something going wrong with nominatim. Will investigate.</p>
</div>
<div id="comment-17606-info" class="comment-info">
<span class="comment-age">(09 Nov '12, 10:31)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
<span id="18087"></span>
<div id="comment-18087" class="comment">
<div id="post-18087-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did the issue in Nominatim get addressed?</p>
</div>
<div id="comment-18087-info" class="comment-info">
<span class="comment-age">(28 Nov '12, 23:16)</span> <span class="comment-user userinfo">JBiehl</span>
</div>
</div>
<span id="27788"></span>
<div id="comment-27788" class="comment">
<div id="post-27788-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm running Nominatim 2.1 and I noticed several locations with wrong city names as well. For one, I live in Fremont (Alameda County). There's also a city named Alameda, which is located 30+ miles north of Fremont. Reverse-geocoding my home's coordinates says my home is in City: Alameda, County: Alameda Country.</p>
</div>
<div id="comment-27788-info" class="comment-info">
<span class="comment-age">(04 Nov '13, 19:27)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
<span id="27806"></span>
<div id="comment-27806" class="comment not_top_scorer">
<div id="post-27806-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@baekacaek</span> without sample coordinates that show the issue (best the query itself) it is difficult to help. But first thing to check is if the OSMF nominatim instance returns the same result.</p>
</div>
<div id="comment-27806-info" class="comment-info">
<span class="comment-age">(05 Nov '13, 11:29)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="28786"></span>
<div id="comment-28786" class="comment not_top_scorer">
<div id="post-28786-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@SimonPoole</span> I opened another question with two examples, one where the city is wrong (both my nominatim and OSM), and two where city is wrong and inconsistent with OSM (my nominatim wrong, but OSM right). <a href="/questions/28784/nominatim-returning-wrong-city-names">https://help.openstreetmap.org/questions/28784/nominatim-returning-wrong-city-names</a></p>
</div>
<div id="comment-28786-info" class="comment-info">
<span class="comment-age">(04 Dec '13, 19:56)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
</div>
<div id="comment-tools-17207" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-17207-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="17208"></span>

<div id="answer-container-17208" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17208-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-17208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you search for <a href="http://nominatim.openstreetmap.org/search.php?q=South+Market+Street%2C+Santa+Clara+County&amp;viewbox=-122.02%2C37.42%2C-121.86%2C37.35">South Market Street, Santa Clara County</a> you will see two results, the first belongs to Santa Clara and the second one to San José. Opening the <a href="http://nominatim.openstreetmap.org/details.php?place_id=74614186">details for the first result</a> reveals that <a href="https://www.openstreetmap.org/browse/node/150938195">Santa Clara</a> is only a <em>node</em>, likewise the <a href="http://nominatim.openstreetmap.org/details.php?place_id=38536497">details of the second result</a> show that <a href="https://www.openstreetmap.org/browse/node/1690212988">San José</a> is also just a <em>node</em>. Now, how should Nominatim know which map feature in this region belongs to Santa Clara and which belongs to San José? It can't without having a border for those two cities and consequently it tries to estimate the borders. The solution is to add both cities as an <em>area</em> instead of a <em>node</em>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '12, 18:09</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-17208" class="comments-container">
<span id="17210"></span>
<div id="comment-17210" class="comment">
<div id="post-17210-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Excellent explanation. Is this something I can change using Potlatch2? If so, can someone provide a pointer to a tutorial for editing/setting city areas?</p>
</div>
<div id="comment-17210-info" class="comment-info">
<span class="comment-age">(26 Oct '12, 18:29)</span> <span class="comment-user userinfo">JBiehl</span>
</div>
</div>
<span id="17211"></span>
<div id="comment-17211" class="comment">
<div id="post-17211-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, just draw a closed way (that's an area in OSM) and add all the tags from the city node to the area.</p>
</div>
<div id="comment-17211-info" class="comment-info">
<span class="comment-age">(26 Oct '12, 18:34)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="17216"></span>
<div id="comment-17216" class="comment">
<div id="post-17216-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OK - looking closer it seems that there are fragments of TIGER bounding lines, they just aren't connected, and thus don't form a closed way. I tried using Potlatch to "link" the appropriate ways together, but I soon encountered this issue:</p>
<p>A server error occurred. Do you want to retry? (The server said: You tried to add 2498 nodes to way 38549944, however only 2000 are allowed.</p>
<p>Anyway around this?</p>
</div>
<div id="comment-17216-info" class="comment-info">
<span class="comment-age">(26 Oct '12, 23:39)</span> <span class="comment-user userinfo">JBiehl</span>
</div>
</div>
<span id="17223"></span>
<div id="comment-17223" class="comment">
<div id="post-17223-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@JBiehl</span>: For technical reasons, you cannot add too many nodes to a single way, thus the error. You probably need to use a "relation", see twain's answer.</p>
</div>
<div id="comment-17223-info" class="comment-info">
<span class="comment-age">(27 Oct '12, 14:28)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="17267"></span>
<div id="comment-17267" class="comment">
<div id="post-17267-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes -- Relation is the way to do it. I revoked my original changes and started to make a relation. However, it seems that one already exists for the city: <a href="https://www.openstreetmap.org/browse/relation/112143">https://www.openstreetmap.org/browse/relation/112143</a></p>
<p>What I don't understand is why this is not being using to return the proper city name in the nominatim reverse query?</p>
</div>
<div id="comment-17267-info" class="comment-info">
<span class="comment-age">(29 Oct '12, 16:47)</span> <span class="comment-user userinfo">JBiehl</span>
</div>
</div>
</div>
<div id="comment-tools-17208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17208-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17217"></span>

<div id="answer-container-17217" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17217-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-17217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are probably best off creating the boundary using a relation which is documented here: <a href="https://wiki.openstreetmap.org/wiki/Relation:boundary">https://wiki.openstreetmap.org/wiki/Relation:boundary</a></p>
<p>If you want you can link the previous node as a 'label' relation member - which is an advantage of using a relation since it allow you to define the exact centre as well as the outline.</p>
<p>You may find this help topic useful although it relates to editing an existing boundary rather than adding a new one: <a href="/questions/13858/how-do-i-correct-an-administrative-boundary-in-the-nominatim">https://help.openstreetmap.org/questions/13858/how-do-i-correct-an-administrative-boundary-in-the-nominatim</a></p>
<p>I generally find this sort of editing easier to do in JOSM rather than potlatch but I belive it is possible in either.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '12, 00:07</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-17217" class="comments-container">
<span id="17218"></span>
<div id="comment-17218" class="comment">
<div id="post-17218-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So it turns out there is a relation that defines the city:</p>
<p><a href="https://www.openstreetmap.org/browse/relation/112143">https://www.openstreetmap.org/browse/relation/112143</a></p>
<p>It looks closed to me, so I'm wondering why this relation is not used to define the city in the nominatim query. Perhaps it's missing required tags?</p>
<p>Thanks for all the help -- this forum is great.</p>
</div>
<div id="comment-17218-info" class="comment-info">
<span class="comment-age">(27 Oct '12, 01:21)</span> <span class="comment-user userinfo">JBiehl</span>
</div>
</div>
<span id="17495"></span>
<div id="comment-17495" class="comment">
<div id="post-17495-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I've investigated relation 112143. From the nominatim database:</p>
<p>nominatim=# select st_isvalid(geometry) from place where osm_type = 'R' and osm_id = 112143; NOTICE: Self-intersection at or near point -121.80706582236448 37.369616207441474</p>
<p>i.e.: <a href="https://www.openstreetmap.org/?lat=37.369616207441474&amp;lon=-121.80706582236448&amp;zoom=18&amp;layers=M&amp;relation=112143">https://www.openstreetmap.org/?lat=37.369616207441474&amp;lon=-121.80706582236448&amp;zoom=18&amp;layers=M&amp;relation=112143</a></p>
<p>The error is so small you can't really see it at zoom 18. Try JOSM.</p>
<p>Unfortunately none of the standard relation tools seem to pick this up as an error! I'll see if I can get something added to nominatim to allow these to be found.</p>
</div>
<div id="comment-17495-info" class="comment-info">
<span class="comment-age">(05 Nov '12, 13:35)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
<span id="17502"></span>
<div id="comment-17502" class="comment">
<div id="post-17502-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wow! That is small! Nice catch. In the meantime should I correct the error? Or leave it as a test condition for your modification?</p>
</div>
<div id="comment-17502-info" class="comment-info">
<span class="comment-age">(05 Nov '12, 18:44)</span> <span class="comment-user userinfo">JBiehl</span>
</div>
</div>
<span id="17504"></span>
<div id="comment-17504" class="comment">
<div id="post-17504-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can find self-intersecting ways with the <a href="http://tools.geofabrik.de/osmi/?view=geometry&amp;lon=-122.23150&amp;lat=37.63009&amp;zoom=9&amp;overlays=self_intersection_ways,self_intersection_points">OSM Inspector</a>. After you've found them, you can fix them. Nominatim isn't the only tool that doesn't like these errors.</p>
</div>
<div id="comment-17504-info" class="comment-info">
<span class="comment-age">(05 Nov '12, 19:18)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="17506"></span>
<div id="comment-17506" class="comment not_top_scorer">
<div id="post-17506-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Another <a href="http://tools.geofabrik.de/osmi/?view=multipolygon&amp;lon=-122.19511&amp;lat=37.54630&amp;zoom=9&amp;overlays=duplicate_ways,intersections,intersection_lines,ring_not_closed,unconnected_end_nodes">OSMI view with broken multipolygons</a>.</p>
</div>
<div id="comment-17506-info" class="comment-info">
<span class="comment-age">(05 Nov '12, 19:27)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="17573"></span>
<div id="comment-17573" class="comment">
<div id="post-17573-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You can now also see polygon problems from within nominatim:</p>
<p><a href="http://nominatim.openstreetmap.org/details?osmtype=R&amp;osmid=112143">http://nominatim.openstreetmap.org/details?osmtype=R&amp;osmid=112143</a></p>
<p>The details page shows how nominatim interpreted the openstreetmap data for that feature.</p>
</div>
<div id="comment-17573-info" class="comment-info">
<span class="comment-age">(07 Nov '12, 23:49)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
</div>
<div id="comment-tools-17217" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-17217-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17521"></span>

<div id="answer-container-17521" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17521-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-17521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Has anyone considered that the most simple way to "fix" this problem shoudl be to give <a href="https://www.openstreetmap.org/browse/way/37918472">the Marriott</a> address data of some sort? It doesn't even have a street number!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '12, 17:45</strong></p>
<img src="https://secure.gravatar.com/avatar/01d01832dff61a6bcf68913f1dc001bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Circeus&#39;s gravatar image" />
<p><span>Circeus</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Circeus has 2 accepted answers">7%</span></p>
</div>
</div>
<div id="comments-container-17521" class="comments-container">
<span id="17522"></span>
<div id="comment-17522" class="comment">
<div id="post-17522-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Adding the full address would probably lead to the correct city name being returned but doesn't fix the actual problem.</p>
</div>
<div id="comment-17522-info" class="comment-info">
<span class="comment-age">(06 Nov '12, 18:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="17523"></span>
<div id="comment-17523" class="comment">
<div id="post-17523-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That fixes one address - not any of the other roads/houses nearby. Fixing the relation fixes all of them.</p>
</div>
<div id="comment-17523-info" class="comment-info">
<span class="comment-age">(06 Nov '12, 18:06)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
</div>
<div id="comment-tools-17521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17521-form-container" class="comment-form-container">
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

