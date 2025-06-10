+++
type = "question"
title = "Incorrect data return in own setup ?"
description = '''hi, We setup our own instance of nominatim(version 3.1.0) with planet data (Planet data downloaded on July 1st week 2018 &amp;amp; not yet updating regularly). The below Nominatim reverse geocode URL return correct data. https://nominatim.openstreetmap.org/reverse?format=json&amp;amp;lat=19.1896835&amp;amp;lon=...'''
date = "2018-09-11T07:24:00Z"
lastmod = "2018-09-14T11:05:00Z"
weight = 65858
keywords = [ "postalcode", "reversegeocoding", "update", "nominatim" ]
aliases = [ "/questions/65858" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Incorrect data return in own setup ?](/questions/65858/incorrect-data-return-in-own-setup)

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
<span id="post-65858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65858-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi,</p>
<p>We setup our own instance of nominatim(version 3.1.0) with planet data (Planet data downloaded on July 1st week 2018 &amp; not yet updating regularly).</p>
<p>The below Nominatim reverse geocode URL return correct data.</p>
<p><a href="https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=19.1896835&amp;lon=72.9465236">https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=19.1896835&amp;lon=72.9465236</a></p>
<p>But my nominatim server return incorrect result(postalcode only incorrect) as follows:</p>
<pre><code>{&quot;place_id&quot;:&quot;1568360&quot;,&quot;licence&quot;:&quot;Data © OpenStreetMap contributors, ODbL 1.0. https:\/\/osm.org\/copyright&quot;,&quot;osm_type&quot;:&quot;way&quot;,&quot;osm_id&quot;:&quot;390034175&quot;,&quot;lat&quot;:&quot;19.18943535&quot;,&quot;lon&quot;:&quot;72.9461104562161&quot;,&quot;display_name&quot;:&quot;MANGAL KARYALAY, Shreenagar Main Rd, Kisan Nagar, ठाणे, Thane, Maharashtra, 560092, India&quot;,&quot;address&quot;:{&quot;townhall&quot;:&quot;MANGAL KARYALAY&quot;,&quot;road&quot;:&quot;Shreenagar Main Rd&quot;,&quot;suburb&quot;:&quot;Kisan Nagar&quot;,&quot;city&quot;:&quot;ठाणे&quot;,&quot;state_district&quot;:&quot;Thane&quot;,&quot;state&quot;:&quot;Maharashtra&quot;,&quot;postcode&quot;:&quot;560092&quot;,&quot;country&quot;:&quot;India&quot;,&quot;country_code&quot;:&quot;in&quot;},&quot;boundingbox&quot;:[&quot;19.1891871&quot;,&quot;19.1896785&quot;,&quot;72.9458731&quot;,&quot;72.9463452&quot;]}</code></pre>
<p>Note: The same data may updated recently(after i have downloaded planet data)? If yes, how to confirm the same. I tried as <a href="https://www.openstreetmap.org/api/0.6/way/390034175">https://www.openstreetmap.org/api/0.6/way/390034175</a> . But it shows timestamp as 2 years old.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postalcode" rel="tag" title="see questions tagged &#39;postalcode&#39;">postalcode</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '18, 07:24</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '18, 19:18</strong> </span></p>
</div>
</div>
<div id="comments-container-65858" class="comments-container">
&#10;</div>
<div id="comment-tools-65858" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65858-form-container" class="comment-form-container">
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

<span id="65859"></span>

<div id="answer-container-65859" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65859-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try running <code>./utils/update.php --calculate-postcodes</code> from the <code>build</code> directory. It will look at all postcodes and recalculate their (center) position.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '18, 12:25</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '18, 12:26</strong> </span></p>
</div>
</div>
<div id="comments-container-65859" class="comments-container">
<span id="65861"></span>
<div id="comment-65861" class="comment">
<div id="post-65861-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/150/mtmail"></a><a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a>: Thanks for your reply. But, Still got the same incorrect postcode only.</p>
<p>Also tried as fresh import of india data only (<a href="https://download.geofabrik.de/asia/india-latest.osm.pbf">https://download.geofabrik.de/asia/india-latest.osm.pbf</a> ). But got the above incorrect postcode only. Is there any changes done in Nominatim_3.2.0 for this issue? (Note: I am using 3.1.0)</p>
</div>
<div id="comment-65861-info" class="comment-info">
<span class="comment-age">(11 Sep '18, 18:27)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="65862"></span>
<div id="comment-65862" class="comment">
<div id="post-65862-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sounds like the OSM postcode data might be incorrect and nominatim.osm.org is displaying older data. Go to <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> zoom in to India and run the query "addr:postcode=560092" in the wizard. It will show one postcode 100km away from the others. That could be a reason. There's even two more that don't quite fit the others (10km away).</p>
</div>
<div id="comment-65862-info" class="comment-info">
<span class="comment-age">(11 Sep '18, 18:44)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="65896"></span>
<div id="comment-65896" class="comment">
<div id="post-65896-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/150/mtmail"></a><a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a>: Thanks again. Yes. Thats the issue. Now i have deleted that incorrect node in osm and re-import with latest india data. Got correct postcode data now.</p>
</div>
<div id="comment-65896-info" class="comment-info">
<span class="comment-age">(14 Sep '18, 11:05)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
</div>
<div id="comment-tools-65859" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65859-form-container" class="comment-form-container">
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

