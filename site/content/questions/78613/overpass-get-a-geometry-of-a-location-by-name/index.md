+++
type = "question"
title = "Overpass: Get a geometry of a location by name"
description = '''I am given a ISO 3361 Alpha-2 country code and a location name. I&#x27;m trying to use Overpass to extract the geometries (or boundaries, or polygon) of that location. I don&#x27;t know the location&#x27;s specific administrative level (i.e. it could be a town, a city, a county, etc..., but not any lower resolutio...'''
date = "2021-01-31T13:29:00Z"
lastmod = "2021-02-06T15:41:00Z"
weight = 78613
keywords = [ "overpass", "polygon", "name" ]
aliases = [ "/questions/78613" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass: Get a geometry of a location by name](/questions/78613/overpass-get-a-geometry-of-a-location-by-name)

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
<span id="post-78613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78613-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am given a ISO 3361 Alpha-2 country code and a location name.</p>
<p>I'm trying to use Overpass to extract the geometries (or boundaries, or polygon) of that location. I don't know the location's specific administrative level (i.e. it could be a town, a city, a county, etc..., but <em>not</em> any lower resolution/division than that).</p>
<p>For example: <code>DE + berlin DE + munich US + chicago FR + Levroux</code></p>
<p>Tried the following query, but got way more data than I need: <code>(rel[boundary="administrative"][name="Berlin"][admin_level="4"];&gt;;);(._;&gt;;);out;</code></p>
<p>or <code>{{geocodeArea:"DE"}}-&gt;.a; ( nwr["name:en"="Berlin"][boundary=administrative][type=boundary][admin_level="4"](area.a); ); out geom;</code> I exported it as Geojson and projected it on map, but besides getting the boundaries of Berlin (type=boundary), I got some more nodes that I wasn't expecting.</p>
<p>So what is the best way to extract this data? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jan '21, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/cd378382281f1616746c9d4dbfb41699?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RamidAshar&#39;s gravatar image" />
<p><span>RamidAshar</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RamidAshar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78613" class="comments-container">
<span id="78616"></span>
<div id="comment-78616" class="comment">
<div id="post-78616-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Was "some more nodes" just the admin_centre node or actual nodes of the relation? Explain what "projected it on map" means? What map? uMap?</p>
</div>
<div id="comment-78616-info" class="comment-info">
<span class="comment-age">(31 Jan '21, 16:54)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="78617"></span>
<div id="comment-78617" class="comment">
<div id="post-78617-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, thats probably it (the admin_centre), but even more nodes in some weird places (some in the middle of the city, some on the boundaries). I converted to GeoJson and put it on kepler.gl for instance. maxerickson's answer seems to solve this issue for me.</p>
</div>
<div id="comment-78617-info" class="comment-info">
<span class="comment-age">(31 Jan '21, 17:40)</span> <span class="comment-user userinfo">RamidAshar</span>
</div>
</div>
</div>
<div id="comment-tools-78613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78613-form-container" class="comment-form-container">
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

<span id="78615"></span>

<div id="answer-container-78615" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78615-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One way is to <a href="http://overpass-turbo.eu/s/12ZQ">use explicit steps to fetch the ways and nodes</a> instead of <code>out geom</code>:</p>
<pre><code>{{geocodeArea:&quot;DE&quot;}}-&gt;.a;
nwr[&quot;name:en&quot;=&quot;Berlin&quot;][boundary=administrative][type=boundary][admin_level=&quot;4&quot;](area.a);
out;
(way(r);
 &gt;;);
out skel;</code></pre>
<p>The <code>way(r);</code> line fetches only the ways from the boundary relation, and then <code>out skel;</code> fetches the nodes without their tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '21, 15:22</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-78615" class="comments-container">
<span id="78618"></span>
<div id="comment-78618" class="comment">
<div id="post-78618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>interesting. yes, it works. I got only the boundaries I needed. 1. Also, limiting to <code>{{geocodeArea:"DE"}}</code> seems to be really slow (I guess because the extra calls to OSM geocoding?) 2. Say I wanted all cities in Germany, should I simply remove the <code>["name:en"="Berlin"]</code> part? (query goes timeout on UI).</p>
</div>
<div id="comment-78618-info" class="comment-info">
<span class="comment-age">(31 Jan '21, 17:43)</span> <span class="comment-user userinfo">RamidAshar</span>
</div>
</div>
<span id="78619"></span>
<div id="comment-78619" class="comment">
<div id="post-78619-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>admin_level=4 is not for cities, so you'd have to do more than remove the name.</p>
</div>
<div id="comment-78619-info" class="comment-info">
<span class="comment-age">(31 Jan '21, 18:55)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="78689"></span>
<div id="comment-78689" class="comment">
<div id="post-78689-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> For some reason, back in 2012 This relation was defined as place=state</p>
</div>
<div id="comment-78689-info" class="comment-info">
<span class="comment-age">(06 Feb '21, 06:06)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="78700"></span>
<div id="comment-78700" class="comment">
<div id="post-78700-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it's a reflection of the political organization of Berlin. <a href="https://en.wikipedia.org/wiki/Berlin#Government">https://en.wikipedia.org/wiki/Berlin#Government</a></p>
</div>
<div id="comment-78700-info" class="comment-info">
<span class="comment-age">(06 Feb '21, 15:41)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-78615" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78615-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78688"></span>

<div id="answer-container-78688" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78688-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have you got 'Don't display small features as POIs.' under Settings&gt;Map turned off?</p>
<p>Checking only for relations will return only relations &amp; speed the search up a bit.</p>
<pre><code>area[&quot;ISO3166-1&quot;=DE]; // Germany
rel[&quot;name:en&quot;=Berlin][type=boundary](area);
way(r);
out geom;</code></pre>
<p>PS Could you use the Code button when posting a routine. It makes it easier to read &amp; copy/ppate/</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '21, 05:06</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-78688" class="comments-container">
&#10;</div>
<div id="comment-tools-78688" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78688-form-container" class="comment-form-container">
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

