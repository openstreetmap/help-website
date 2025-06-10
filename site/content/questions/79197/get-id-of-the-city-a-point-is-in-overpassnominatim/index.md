+++
type = "question"
title = "Get id of the city a point is in (Overpass/Nominatim)"
description = '''I want to query the municipality (city or town) a given point is in, but not only its name, but also the OpenStreetMap id of the area of that city/town in order to fetch further tags from that city/town and to uniquely identify it. For example, for the node with the id 3127879237 (located in Vienna,...'''
date = "2021-03-09T11:51:00Z"
lastmod = "2021-07-14T20:01:00Z"
weight = 79197
keywords = [ "overpass", "nominatim", "municipality", "overpass-ql", "city" ]
aliases = [ "/questions/79197" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Get id of the city a point is in (Overpass/Nominatim)](/questions/79197/get-id-of-the-city-a-point-is-in-overpassnominatim)

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
<span id="post-79197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79197-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to query the municipality (city or town) a given point is in, but not only its name, but also the OpenStreetMap id of the area of that city/town in order to fetch further tags from that city/town and to uniquely identify it.</p>
<p>For example, for the node with the id <code>3127879237</code> (located in Vienna, Austria) I would like to get back the id <code>3600109166</code> for the area of Vienna.</p>
<p>With Overpass and Nominatim, i could only achieve that half-way so far:</p>
<p>Using <strong>Overpass</strong> the following query returns all surrounding boundaries:</p>
<pre><code>node(3127879237);
is_in;
area._[&quot;admin_level&quot;][&quot;boundary&quot;=&quot;administrative&quot;];
out;</code></pre>
<p>One of them is the city/town boundary I am looking for, but it doesn't have any tags signalling it's the city/town and it seems like the <code>admin_level</code> of the municipality depends on its size and the country.</p>
<p><strong>Nominatim</strong> <em>can</em> figure out the city/town, but it only gives back its name, which is not necessarily unique, and not its OSM-id:</p>
<pre><code>https://nominatim.openstreetmap.org/lookup?osm_ids=N3127879237&amp;format=json</code></pre>
<p>Is the only way to achieve that to get the name from Nominatim and then filtering the <code>is_in</code> results by the name returned from Nominatim?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-municipality" rel="tag" title="see questions tagged &#39;municipality&#39;">municipality</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '21, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbeb784759cdecafe404c17586762?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Loram&#39;s gravatar image" />
<p><span>Loram</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Loram has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79197" class="comments-container">
&#10;</div>
<div id="comment-tools-79197" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79197-form-container" class="comment-form-container">
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

<span id="79198"></span>

<div id="answer-container-79198" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79198-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim's /details endpoint can return a list of parent objects, each with name, osmtype, osmid. <a href="https://nominatim.openstreetmap.org/details?osmtype=N&amp;osmid=3127879237&amp;format=json&amp;addressdetails=1">https://nominatim.openstreetmap.org/details?osmtype=N&amp;osmid=3127879237&amp;format=json&amp;addressdetails=1</a> Ignore any items having isaddress=false. That can help you when you run your own Nominatim server. For the public nominatim.openstreetmap.org the access is discouraged as it puts a higher load on the database <a href="https://nominatim.org/release-docs/develop/api/Details/">https://nominatim.org/release-docs/develop/api/Details/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '21, 12:06</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-79198" class="comments-container">
&#10;</div>
<div id="comment-tools-79198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79198-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79202"></span>

<div id="answer-container-79202" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79202-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As with this example many place=city/town entities are nodes. If you're unable to rely on admin_level, you'll need to iterate the returned boundary relations to return nodes with 'admin_centre' roles. These should contain 'place=city/town'. Try expanding on this:</p>
<pre><code>node(3127879237);
is_in;
rel(pivot)[boundary=administrative];
node(r:admin_centre);
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '21, 13:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '21, 15:26</strong> </span></p>
</div>
</div>
<div id="comments-container-79202" class="comments-container">
<span id="80974"></span>
<div id="comment-80974" class="comment">
<div id="post-80974-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot! However, for other points, this query also returns the capital cities of the states and nations the point is in. The only way to filter the actual city the node is in that came to my mind is to pick the output city that is nearest to the given point in a post-processing step. Is there also a way to exclude the others from the query?</p>
</div>
<div id="comment-80974-info" class="comment-info">
<span class="comment-age">(14 Jul '21, 20:01)</span> <span class="comment-user userinfo">Loram</span>
</div>
</div>
</div>
<div id="comment-tools-79202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79202-form-container" class="comment-form-container">
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

