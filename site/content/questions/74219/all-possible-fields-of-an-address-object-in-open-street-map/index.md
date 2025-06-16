+++
type = "question"
title = "All possible fields of an address object in Open Street Map"
description = '''I am developping a web application and I use Nominatin service to get addresses.  In JSON format, Nominatin sends an address object like this : &quot;address&quot;: {&quot;road&quot;: &quot;Hillcrest Road&quot;, &quot;suburb&quot;: &quot;Gidea Park&quot;, &quot;city&quot;: &quot;London Borough of Havering&quot;, &quot;state_district&quot;: &quot;Grand Londres&quot;,&quot;state&quot;: &quot;Angleterre&quot;,...'''
date = "2020-04-16T11:17:00Z"
lastmod = "2020-04-16T11:17:00Z"
weight = 74219
keywords = [ "address" ]
aliases = [ "/questions/74219" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [All possible fields of an address object in Open Street Map](/questions/74219/all-possible-fields-of-an-address-object-in-open-street-map)

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
<span id="post-74219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74219-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am developping a web application and I use Nominatin service to get addresses.</p>
<p>In JSON format, Nominatin sends an address object like this : "address": {"road": "Hillcrest Road", "suburb": "Gidea Park", "city": "London Borough of Havering", "state_district": "Grand Londres","state": "Angleterre", "postcode": "RM11 1EA", "country": "Royaume-Uni", "country_code": "gb"}. Of course, address fields change depending on the country.</p>
<p>In the database of our web application, we would like to build a table to store all fields of an address object of OSM, because we want to be compatible to all addresses around the world. I've been looking for days, for the list of all fields contained in an address object of OSM : on the net, in documentations, in nominatim and osm2pgsql code.</p>
<p>I saw this post on Open Street Map Help : "/questions/61683/all-possible-fields-of-address-object".</p>
<p>But :</p>
<ul>
<li>1) it was in January 2018,</li>
<li>2) the answer was "https://github.com/OpenCageData/address-formatting/blob/master/conf/components.yaml"</li>
<li>3) and "https://github.com/openstreetmap/Nominatim/blob/6c1977b448e8b195bf96b6144674ffe0527e79de/lib/lib.php#L63"</li>
</ul>
<p>The "https://github.com/osm-search/Nominatim/blob/v3.4.1/lib/lib.php" is different than witch I quoted above in point 3).</p>
<p>Concerning the above point 2) :</p>
<ul>
<li>is OSM (Nominatim) using OpenCageData address-formatting ?</li>
<li>Can I rely on it to build my address table ?</li>
</ul>
<p>Please help me...</p>
<p>Thanks in advance for your response.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Apr '20, 11:17</strong></p>
<img src="https://secure.gravatar.com/avatar/cbcf16c73a5b3d0f232fb49ea8d084d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pasgirard&#39;s gravatar image" />
<p><span>Pasgirard</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pasgirard has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74219" class="comments-container">
&#10;</div>
<div id="comment-tools-74219" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74219-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

