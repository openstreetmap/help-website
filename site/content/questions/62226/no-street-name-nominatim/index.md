+++
type = "question"
title = "No Street Name - Nominatim"
description = '''Ive setup my own nominatim instance with data from here: https://download.geofabrik.de/europe/great-britain.html However when i run a reverse geocode, i dont get any street names as below  {&quot;place_id&quot;:&quot;2192355&quot;,&quot;licence&quot;:&quot;Data © OpenStreetMap contributors, ODbL 1.0. https:&#92;/&#92;/osm.org&#92;/copyright&quot;,&quot;os...'''
date = "2018-02-20T19:54:00Z"
lastmod = "2018-02-21T15:41:00Z"
weight = 62226
keywords = [ "reversegeocoding", "nominatim" ]
aliases = [ "/questions/62226" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No Street Name - Nominatim](/questions/62226/no-street-name-nominatim)

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
<span id="post-62226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62226-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Ive setup my own nominatim instance with data from here: <a href="https://download.geofabrik.de/europe/great-britain.html">https://download.geofabrik.de/europe/great-britain.html</a></p>
<p>However when i run a reverse geocode, i dont get any street names as below</p>
<pre><code>{&quot;place_id&quot;:&quot;2192355&quot;,&quot;licence&quot;:&quot;Data © OpenStreetMap contributors, ODbL 1.0. https:\/\/osm.org\/copyright&quot;,&quot;osm_type&quot;:&quot;way&quot;,&quot;osm_id&quot;:&quot;48368272&quot;,&quot;lat&quot;:&quot;51.3971413&quot;,&quot;lon&quot;:&quot;0.458866249992111&quot;,&quot;display_name&quot;:&quot;Knights Place Estate, Strood, Medway, South East, England, Groussbritannien an Nordirland&quot;,&quot;address&quot;:{&quot;residential&quot;:&quot;Knights Place Estate&quot;,&quot;town&quot;:&quot;Strood&quot;,&quot;county&quot;:&quot;Medway&quot;,&quot;state_district&quot;:&quot;South East&quot;,&quot;state&quot;:&quot;England&quot;,&quot;country&quot;:&quot;Groussbritannien an Nordirland&quot;,&quot;country_code&quot;:&quot;gb&quot;},&quot;boundingbox&quot;:[&quot;51.3957208&quot;,&quot;51.3985316&quot;,&quot;0.4521022&quot;,&quot;0.4643315&quot;]}</code></pre>
<p>When i run the same query at <a href="http://nominatim.openstreetmap.org">http://nominatim.openstreetmap.org</a></p>
<p>and i get the below {"place_id":"82606933","licence":"Data © OpenStreetMap contributors, ODbL 1.0. https:\/\/osm.org\/copyright","osm_type":"way","osm_id":"48368273","lat":"51.3967521","lon":"0.4586866","display_name":"Swale Road, Knights Place Estate, Strood, Medway, South East, England, ME2 2TT, United Kingdom","address":{"road":"Swale Road","residential":"Knights Place Estate","town":"Strood","county":"Medway","state_district":"South East","state":"England","postcode":"ME2 2TT","country":"United Kingdom","country_code":"gb"},"boundingbox":["51.3967496","51.3977321","0.4575055","0.4592328"]}</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '18, 19:54</strong></p>
<img src="https://secure.gravatar.com/avatar/5eb51b2fbf0f82509523633744b21186?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Teshiburu&#39;s gravatar image" />
<p><span>Teshiburu</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Teshiburu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62226" class="comments-container">
<span id="62229"></span>
<div id="comment-62229" class="comment">
<div id="post-62229-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you post the full URL with all parameters (OK, to remove the domain name)? Which version of Nominatim are you running? When was the data last imported/updated?</p>
</div>
<div id="comment-62229-info" class="comment-info">
<span class="comment-age">(20 Feb '18, 21:14)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="62233"></span>
<div id="comment-62233" class="comment">
<div id="post-62233-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh wait, you say you never get any street names? That's a first. Do you get street names when you forward geocode?</p>
</div>
<div id="comment-62233-info" class="comment-info">
<span class="comment-age">(20 Feb '18, 23:33)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="62236"></span>
<div id="comment-62236" class="comment">
<div id="post-62236-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Forward geocode? Sorry fairly new to all of this!</p>
<p>I don't have the UK postcodes or Wikipedia data</p>
</div>
<div id="comment-62236-info" class="comment-info">
<span class="comment-age">(21 Feb '18, 06:59)</span> <span class="comment-user userinfo">Teshiburu</span>
</div>
</div>
<span id="62242"></span>
<div id="comment-62242" class="comment">
<div id="post-62242-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just managed to get back to the machine in question, and it appears that it is still doing some setup tasks?</p>
<p>Done 1605812 in 46677 @ 34.402641 per second - Rank 26 ETA (seconds): 4190.986328 Done 1605880 in 46678 @ 34.403358 per second - Rank 26 ETA (seconds): 4188.922363</p>
<p>Got lots of lines of this, guess ill have to wait 5000 seconds :P</p>
</div>
<div id="comment-62242-info" class="comment-info">
<span class="comment-age">(21 Feb '18, 08:25)</span> <span class="comment-user userinfo">Teshiburu</span>
</div>
</div>
<span id="62243"></span>
<div id="comment-62243" class="comment">
<div id="post-62243-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Longer. After Rank 26 there'll be Rank 30 which takes twice as long alone. Then follows the search index generation.</p>
</div>
<div id="comment-62243-info" class="comment-info">
<span class="comment-age">(21 Feb '18, 10:30)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="62249"></span>
<div id="comment-62249" class="comment not_top_scorer">
<div id="post-62249-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can't help you with Nominatim, but I'm interested as I grew up on that estate and mapped it eight years ago!</p>
</div>
<div id="comment-62249-info" class="comment-info">
<span class="comment-age">(21 Feb '18, 13:33)</span> <span class="comment-user userinfo">sdoerr</span>
</div>
</div>
<span id="62253"></span>
<div id="comment-62253" class="comment not_top_scorer">
<div id="post-62253-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4383/sdoerr">@sdoerr</a> - which estate?</p>
</div>
<div id="comment-62253-info" class="comment-info">
<span class="comment-age">(21 Feb '18, 13:58)</span> <span class="comment-user userinfo">Teshiburu</span>
</div>
</div>
<span id="62256"></span>
<div id="comment-62256" class="comment not_top_scorer">
<div id="post-62256-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Knights Place</p>
</div>
<div id="comment-62256-info" class="comment-info">
<span class="comment-age">(21 Feb '18, 15:41)</span> <span class="comment-user userinfo">sdoerr</span>
</div>
</div>
</div>
<div id="comment-tools-62226" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-62226-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

