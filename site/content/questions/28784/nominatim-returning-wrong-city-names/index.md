+++
type = "question"
title = "nominatim returning wrong city names"
description = '''I have a server running Nominatim 2.1 with data downloaded from http://download.geofabrik.de/ and I noticed that on many occasions, the nominatim on my server is returning wrong city names. Sometimes, it&#x27;s wrong AND also different from results from nominatim on nominatim.openstreetmap.org.  I also n...'''
date = "2013-12-04T19:52:00Z"
lastmod = "2013-12-05T15:30:00Z"
weight = 28784
keywords = [ "nominatim", "osm" ]
aliases = [ "/questions/28784" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nominatim returning wrong city names](/questions/28784/nominatim-returning-wrong-city-names)

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
<span id="post-28784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28784-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-28784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a server running Nominatim 2.1 with data downloaded from <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a> and I noticed that on many occasions, the nominatim on my server is returning wrong city names. Sometimes, it's wrong AND also different from results from nominatim on nominatim.openstreetmap.org.</p>
<p>I also noticed that when the return city name is wrong, it often gets the city name from the county it's in. For instance, if the county name is "Santa Clara County", sometimes the city is incorrectly returned as "Santa Clara" (when it should've been "San Jose"). Below are examples where the returned city name is incorrect.</p>
<p><strong>Example 1 - wrong city (should've been "San Jose"):</strong></p>
<pre><code>{&quot;place_id&quot;:&quot;7866664&quot;,
&quot;licence&quot;:&quot;Data \u00a9 OpenStreetMap contributors, ODbL 1.0. http:\/\/www.openstreetmap.org\/copyright&quot;,
&quot;osm_type&quot;:&quot;way&quot;,
&quot;osm_id&quot;:&quot;8965496&quot;,
&quot;lat&quot;:&quot;37.3175321691594&quot;,
&quot;lon&quot;:&quot;-121.788455885124&quot;,
&quot;display_name&quot;:&quot;D&#39;Amico Drive, Santa Clara, Santa Clara County, California, 95148, United States of America&quot;,
&quot;address&quot;:{
    &quot;road&quot;:&quot;D&#39;Amico Drive&quot;,
    &quot;city&quot;:&quot;Santa Clara&quot;,
    &quot;county&quot;:&quot;Santa Clara County&quot;,
    &quot;state&quot;:&quot;California&quot;,
    &quot;postcode&quot;:&quot;95148&quot;,
    &quot;country&quot;:&quot;United States of America&quot;,
    &quot;country_code&quot;:&quot;us&quot;}
}</code></pre>
<p>Perhaps even more mind-boggling is the fact that sometimes, not only is the returned city wrong, but also different from the results from OSM nominatim.</p>
<p><strong>Example 2 - wrong city, and different results than nominatim.openstreetmap.org</strong></p>
<p>My nominatim:</p>
<pre><code>{&quot;place_id&quot;:&quot;22439557&quot;,
&quot;licence&quot;:&quot;Data \u00a9 OpenStreetMap contributors, ODbL 1.0. http:\/\/www.openstreetmap.org\/copyright&quot;,
&quot;osm_type&quot;:&quot;way&quot;,
&quot;osm_id&quot;:&quot;60691604&quot;,
&quot;lat&quot;:&quot;37.3963095743164&quot;,
&quot;lon&quot;:&quot;-121.928365877892&quot;,
&quot;display_name&quot;:&quot;Zanker Road, Santa Clara, Santa Clara County, California, 95134, United States of America&quot;,
&quot;address&quot;:{
    &quot;road&quot;:&quot;Zanker Road&quot;,
    &quot;city&quot;:&quot;Santa Clara&quot;,
    &quot;county&quot;:&quot;Santa Clara County&quot;,
    &quot;state&quot;:&quot;California&quot;,
    &quot;postcode&quot;:&quot;95134&quot;,
    &quot;country&quot;:&quot;United States of America&quot;,
    &quot;country_code&quot;:&quot;us&quot;}
}</code></pre>
<p>OSM nominatim:</p>
<pre><code>{&quot;place_id&quot;:&quot;55231842&quot;,
&quot;licence&quot;:&quot;Data \u00a9 OpenStreetMap contributors, ODbL 1.0. http:\/\/www.openstreetmap.org\/copyright&quot;,
&quot;osm_type&quot;:&quot;way&quot;,
&quot;osm_id&quot;:&quot;60691604&quot;,
&quot;lat&quot;:&quot;37.4026925&quot;,&quot;lon&quot;:&quot;-121.9337568&quot;,
&quot;display_name&quot;:&quot;Zanker Road, Alviso, San Jose, Santa Clara County, California, 95134, United States of America&quot;,
&quot;address&quot;:{
    &quot;road&quot;:&quot;Zanker Road&quot;,
    &quot;suburb&quot;:&quot;Alviso&quot;,
    &quot;city&quot;:&quot;San Jose&quot;,
    &quot;county&quot;:&quot;Santa Clara County&quot;,
    &quot;state&quot;:&quot;California&quot;,
    &quot;postcode&quot;:&quot;95134&quot;,
    &quot;country&quot;:&quot;United States of America&quot;,
    &quot;country_code&quot;:&quot;us&quot;}
}</code></pre>
<p>Why is it returning the wrong city name? (everything else seems to be correct). Also, why are my results sometimes different from OSM nominatim? Do they use a different nominatim? or do they use different data?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Dec '13, 19:52</strong></p>
<img src="https://secure.gravatar.com/avatar/61de868d7785f30711497cecbdddf5f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baekacaek&#39;s gravatar image" />
<p><span>baekacaek</span><br />
<span class="score" title="176 reputation points">176</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baekacaek has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Dec '13, 19:53</strong> </span></p>
</div>
</div>
<div id="comments-container-28784" class="comments-container">
&#10;</div>
<div id="comment-tools-28784" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28784-form-container" class="comment-form-container">
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

<span id="28826"></span>

<div id="answer-container-28826" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28826-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim wrongly matches 'Santa Clara' from the <code>tiger:county</code> tag against the city instead of the county because the county is called 'Santa Clara <em>County</em>'. Quick-fix is to make sure that the place node of the county (which by convention comes without the County suffix) is included as a member <code>label</code> in the county relation, like <a href="https://www.openstreetmap.org/changeset/19286866">that</a>. Proper fix would be to resolve the issue in Nominatim but it might take a while to get that implemented.</p>
<p>If you run your own instance, you have to force an update of Santa Clara county as described in the comment of <a href="/questions/27544/sf-bay-area-city-names-in-nominatim">this question</a> after the changes have been applied.</p>
<p>Slightly longer explanation:</p>
<p>Nominatim collects for each object a number of potential address parts from interesting tags, among them <code>addr:*</code> tags and <code>tiger:county</code>. Problem is that it only retains the name not the type of object (a legacy from the days of the <code>is_in</code> tag). When collecting the places for the address it gives a slight preference to those that match exactly with any of these names. Most of the times that does the right thing but the County suffix confuses Nominatim. It really needs the county name without suffix to get the exact match. Adding the place node as a label to the relation will resolve exactly that. The suffix-less name is taken from the place node and will provide the exact match.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '13, 15:30</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '13, 14:49</strong> </span></p>
</div>
</div>
<div id="comments-container-28826" class="comments-container">
&#10;</div>
<div id="comment-tools-28826" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28826-form-container" class="comment-form-container">
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

