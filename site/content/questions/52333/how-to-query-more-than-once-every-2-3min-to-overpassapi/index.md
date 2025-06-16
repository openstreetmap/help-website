+++
type = "question"
title = "how to query more than once every 2-3min to overpass.api?"
description = '''I have an application with leaflet and overpass.api written in javascript. I use overpass-layer plugin to query to OSM data. My problem , when i query 2 times to overpass.api i get an Too Many request error. http://overpass-api.de/api/status  status shows me that there is a limitation. There is 1 av...'''
date = "2016-10-02T22:04:00Z"
lastmod = "2016-10-07T19:46:00Z"
weight = 52333
keywords = [ "leaflet", "overpass", "javascript", "overpass-api" ]
aliases = [ "/questions/52333" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to query more than once every 2-3min to overpass.api?](/questions/52333/how-to-query-more-than-once-every-2-3min-to-overpassapi)

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
<span id="post-52333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52333-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an application with leaflet and overpass.api written in javascript. I use overpass-layer plugin to query to OSM data. My problem , when i query 2 times to overpass.api i get an Too Many request error.</p>
<p><a href="http://overpass-api.de/api/status">http://overpass-api.de/api/status</a> status shows me that there is a limitation. There is 1 available slot, and after i send a request my IP is blocked for a time period (30sec-3min). Why is my IP banned already after 1 query? And why for so long?.</p>
<p>in <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">wiki</a> there stands <a href="http://overpass-api.de/api/">http://overpass-api.de/api/</a> :</p>
<blockquote>
<p>"Both servers have a total capacity of about 1.000.000 requests per day. You can safely assume that you don't disturb other users when you do less than 10.000 queries per day or download less than 5 GB data per day."</p>
</blockquote>
<p>Need to query more than just once in 3 min. How can i achieve that?</p>
<p><a href="http://overpass-api.de/api/interpreter?data=%5Bout:json%5D;%20area%5Bname=%22Mannheim%22%5D-%3E.a;(%20node(area.a)%5B%22man_made%22=%22works%22%5D;way(area.a)%5B%22man_made%22=%22works%22%5D;relation(area.a)%5B%22man_made%22=%22works%22%5D;);out%20body;%3E;out%20skel%20qt;">this</a> is an example query i sent with my application.</p>
<p>I just created the biggest query possible with my application slot is available after 5min when i use this query:</p>
<pre><code>area[name=&quot;Berlin&quot;]-&gt;.a;
&#10;(node(area.a)[&quot;landuse&quot;=&quot;industrial&quot;][&quot;name&quot;];
way(area.a)[&quot;landuse&quot;=&quot;industrial&quot;][&quot;name&quot;];
relation(area.a)[&quot;landuse&quot;=&quot;industrial&quot;][&quot;name&quot;];
&#10;node(area.a)[&quot;landuse&quot;=&quot;industrial&quot;][&quot;phone&quot;];
way(area.a)[&quot;landuse&quot;=&quot;industrial&quot;][&quot;phone&quot;];
relation(area.a)[&quot;landuse&quot;=&quot;industrial&quot;][&quot;phone&quot;];
&#10;node(area.a)[&quot;landuse&quot;=&quot;industrial&quot;][&quot;contact:phone&quot;];
way(area.a)[&quot;landuse&quot;=&quot;industrial&quot;][&quot;contact:phone&quot;];
relation(area.a)[&quot;landuse&quot;=&quot;industrial&quot;][&quot;contact:phone&quot;];
&#10;node(area.a)[&quot;landuse&quot;=&quot;industrial&quot;][&quot;website&quot;];
way(area.a)[&quot;landuse&quot;=&quot;industrial&quot;][&quot;website&quot;];
relation(area.a)[&quot;landuse&quot;=&quot;industrial&quot;][&quot;website&quot;];
&#10;node(area.a)[&quot;building&quot;=&quot;industrial&quot;][&quot;name&quot;];
way(area.a)[&quot;building&quot;=&quot;industrial&quot;][&quot;name&quot;];
relation(area.a)[&quot;building&quot;=&quot;industrial&quot;][&quot;name&quot;];
&#10;node(area.a)[&quot;building&quot;=&quot;industrial&quot;][&quot;phone&quot;];
way(area.a)[&quot;building&quot;=&quot;industrial&quot;][&quot;phone&quot;];
relation(area.a)[&quot;building&quot;=&quot;industrial&quot;][&quot;phone&quot;];
&#10;node(area.a)[&quot;building&quot;=&quot;industrial&quot;][&quot;contact:phone&quot;];
way(area.a)[&quot;building&quot;=&quot;industrial&quot;][&quot;contact:phone&quot;];
relation(area.a)[&quot;building&quot;=&quot;industrial&quot;][&quot;contact:phone&quot;];
&#10;node(area.a)[&quot;building&quot;=&quot;industrial&quot;][&quot;website&quot;];
way(area.a)[&quot;building&quot;=&quot;industrial&quot;][&quot;website&quot;];
relation(area.a)[&quot;building&quot;=&quot;industrial&quot;][&quot;website&quot;];
);
out body;
&gt;;
out skel qt;</code></pre>
<p><strong>It gives me all tags with name, phone,contact:phone,website for landuse=industrial and building=industrial</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Oct '16, 22:04</strong></p>
<img src="https://secure.gravatar.com/avatar/fdd97ceec9f9544f1c9d7c57b1ee9707?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JsonKh&#39;s gravatar image" />
<p><span>JsonKh</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JsonKh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Oct '16, 12:39</strong> </span></p>
</div>
</div>
<div id="comments-container-52333" class="comments-container">
<span id="52334"></span>
<div id="comment-52334" class="comment">
<div id="post-52334-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your example appears to be data returned by the query not the query.</p>
</div>
<div id="comment-52334-info" class="comment-info">
<span class="comment-age">(03 Oct '16, 09:12)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="52335"></span>
<div id="comment-52335" class="comment">
<div id="post-52335-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a>: the query is in the link's URL</p>
</div>
<div id="comment-52335-info" class="comment-info">
<span class="comment-age">(03 Oct '16, 10:00)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="52336"></span>
<div id="comment-52336" class="comment">
<div id="post-52336-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So it is, but that requires more effort on my part to cut paste &amp; format!</p>
</div>
<div id="comment-52336-info" class="comment-info">
<span class="comment-age">(03 Oct '16, 10:08)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="52400"></span>
<div id="comment-52400" class="comment">
<div id="post-52400-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This related question contains possibly usefull feedback: <a href="/questions/52384">https://help.openstreetmap.org/questions/52384</a></p>
</div>
<div id="comment-52400-info" class="comment-info">
<span class="comment-age">(07 Oct '16, 19:46)</span> <span class="comment-user userinfo">alexvanderli...</span>
</div>
</div>
</div>
<div id="comment-tools-52333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52333-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

