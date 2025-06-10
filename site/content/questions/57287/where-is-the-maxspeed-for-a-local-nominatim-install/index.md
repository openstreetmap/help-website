+++
type = "question"
title = "Where Is The Maxspeed For A Local Nominatim Install?"
description = '''I have installed my own instance of Nominatim. I followed the instructions per the openmap Nominatim docs. I imported north-america-latest.osm.pbf into my database.  All went well with installation, however, when I query the information i need (i.e. using extratags=1) on my server I do not get a max...'''
date = "2017-07-26T17:12:00Z"
lastmod = "2017-07-27T08:27:00Z"
weight = 57287
keywords = [ "osm", "maxspeed", "data", "osm2pgsql", "nominatim" ]
aliases = [ "/questions/57287" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Where Is The Maxspeed For A Local Nominatim Install?](/questions/57287/where-is-the-maxspeed-for-a-local-nominatim-install)

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
<span id="post-57287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57287-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have installed my own instance of Nominatim. I followed the instructions per the openmap Nominatim docs. I imported north-america-latest.osm.pbf into my database.</p>
<p>All went well with installation, however, when I query the information i need (i.e. using extratags=1) on my server I do not get a maxspeed returned in the extratags. I have tried querying multiple records and none have the maxspeed tag. When I query <a href="http://nominatim.openstreetmap.org">http://nominatim.openstreetmap.org</a> I get maxspeed returned.</p>
<p>Examples: <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=28.5383331&amp;lon=-82.3792121&amp;zoom=18&amp;addressdetails=1&amp;extratags=1">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=28.5383331&amp;lon=-82.3792121&amp;zoom=18&amp;addressdetails=1&amp;extratags=1</a></p>
<p>Returns:</p>
<pre><code>{&quot;place_id&quot;:&quot;105669388&quot;,&quot;licence&quot;:&quot;Data © OpenStreetMap contributors, ODbL 1.0. http:\/\/www.openstreetmap.org\/copyright&quot;,&quot;osm_type&quot;:&quot;way&quot;,&quot;osm_id&quot;:&quot;158732182&quot;,&quot;lat&quot;:&quot;28.5382777&quot;,&quot;lon&quot;:&quot;-82.3808788&quot;,&quot;display_name&quot;:&quot;Cortez Boulevard, Brooksville, Hernando County, Florida, 34603, United States of America&quot;,&quot;address&quot;:{&quot;road&quot;:&quot;Cortez Boulevard&quot;,&quot;village&quot;:&quot;Brooksville&quot;,&quot;county&quot;:&quot;Hernando County&quot;,&quot;state&quot;:&quot;Florida&quot;,&quot;postcode&quot;:&quot;34603&quot;,&quot;country&quot;:&quot;United States of America&quot;,&quot;country_code&quot;:&quot;us&quot;},&quot;extratags&quot;:{&quot;hgv&quot;:&quot;designated&quot;,&quot;lanes&quot;:&quot;2&quot;,&quot;oneway&quot;:&quot;yes&quot;,&quot;surface&quot;:&quot;asphalt&quot;,**&quot;maxspeed&quot;:&quot;50 mph&quot;**},&quot;boundingbox&quot;:[&quot;28.5381558&quot;,&quot;28.5427913&quot;,&quot;-82.3938975&quot;,&quot;-82.3680374&quot;]}</code></pre>
<p>My local instance: <a href="http://192.168.1.75/nominatim/reverse?format=json&amp;lat=28.5383331&amp;lon=-82.3792121&amp;zoom=18&amp;addressdetails=1&amp;extratags=1">http://192.168.1.75/nominatim/reverse?format=json&amp;lat=28.5383331&amp;lon=-82.3792121&amp;zoom=18&amp;addressdetails=1&amp;extratags=1</a></p>
<pre><code>{&quot;place_id&quot;:&quot;23114698&quot;,&quot;licence&quot;:&quot;Data © OpenStreetMap contributors, ODbL 1.0. http:\/\/www.openstreetmap.org\/copyright&quot;,&quot;osm_type&quot;:&quot;way&quot;,&quot;osm_id&quot;:&quot;158732182&quot;,&quot;lat&quot;:&quot;28.5382777&quot;,&quot;lon&quot;:&quot;-82.3808788&quot;,&quot;display_name&quot;:&quot;Cortez Boulevard, Brooksville, Hernando County, Florida, 34603, United States of America&quot;,&quot;address&quot;:{&quot;road&quot;:&quot;Cortez Boulevard&quot;,&quot;village&quot;:&quot;Brooksville&quot;,&quot;county&quot;:&quot;Hernando County&quot;,&quot;state&quot;:&quot;Florida&quot;,&quot;postcode&quot;:&quot;34603&quot;,&quot;country&quot;:&quot;United States of America&quot;,&quot;country_code&quot;:&quot;us&quot;},**&quot;extratags&quot;:{}**,&quot;boundingbox&quot;:[&quot;28.5381558&quot;,&quot;28.5427913&quot;,&quot;-82.3938975&quot;,&quot;-82.3680374&quot;]}</code></pre>
<p>My question is where can I get a the maxspeed for Nominatim records in my local database? Is there a separate osm.pbf file containing this? Would I be able to obtain the maxspeed by re-importing the data using --hstore or adding "node,way maxspeed text linear" to the default.style?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jul '17, 17:12</strong></p>
<img src="https://secure.gravatar.com/avatar/73f2644bddbee6cc29ad4d358f6e3d0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddd_ddd&#39;s gravatar image" />
<p><span>ddd_ddd</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddd_ddd has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jul '17, 18:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-57287" class="comments-container">
<span id="57291"></span>
<div id="comment-57291" class="comment">
<div id="post-57291-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What version of postgresql do you use?</p>
</div>
<div id="comment-57291-info" class="comment-info">
<span class="comment-age">(26 Jul '17, 19:57)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="57302"></span>
<div id="comment-57302" class="comment">
<div id="post-57302-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am using 9.6.</p>
</div>
<div id="comment-57302-info" class="comment-info">
<span class="comment-age">(27 Jul '17, 01:43)</span> <span class="comment-user userinfo">ddd_ddd</span>
</div>
</div>
<span id="57304"></span>
<div id="comment-57304" class="comment">
<div id="post-57304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And which version of Nominatim?</p>
</div>
<div id="comment-57304-info" class="comment-info">
<span class="comment-age">(27 Jul '17, 08:27)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-57287" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57287-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

