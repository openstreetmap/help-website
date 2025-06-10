+++
type = "question"
title = "OverpassAPI: url interpreter and geocodeArea"
description = '''Hi,  I try to get all restaurants by cities in a region. In Overpass Turbo, I have : (http://overpass-turbo.eu/s/S9W) [out:json][timeout:300];  {{geocodeArea:&quot;Le Puy-en-Velay Auvergne-Rhône-Alpes France&quot;}}-&amp;gt;.searchArea;  (  node[&quot;amenity&quot;=&quot;restaurant&quot;](area.searchArea);  way[&quot;amenity&quot;=&quot;restaurant...'''
date = "2020-04-01T09:26:00Z"
lastmod = "2020-04-01T12:53:00Z"
weight = 73905
keywords = [ "url", "overpass-turbo", "geocodearea", "overpass-api" ]
aliases = [ "/questions/73905" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OverpassAPI: url interpreter and geocodeArea](/questions/73905/overpassapi-url-interpreter-and-geocodearea)

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
<span id="post-73905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73905-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I try to get all restaurants by cities in a region. In Overpass Turbo, I have : (<a href="http://overpass-turbo.eu/s/S9W)">http://overpass-turbo.eu/s/S9W)</a></p>
<pre><code>[out:json][timeout:300];
    {{geocodeArea:&quot;Le Puy-en-Velay Auvergne-Rhône-Alpes France&quot;}}-&gt;.searchArea;
    (
      node[&quot;amenity&quot;=&quot;restaurant&quot;](area.searchArea);
      way[&quot;amenity&quot;=&quot;restaurant&quot;](area.searchArea);
      relation[&quot;amenity&quot;=&quot;restaurant&quot;](area.searchArea);
    );
    out center;</code></pre>
<p>This is working fine.<br />
But I have hundred of cities in my region (all recovered from Wikidata) and I want to get restaurants for all cities.</p>
<p>I don't want to do it manually in overpass-turbo.eu tool, so I tried to export my "query" as an url. This is the generated url:</p>
<blockquote>
<p><a href="http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%5Btimeout%3A300%5D%3B%0Aarea%283600120067%29-%3E.searchArea%3B%0A%28%0A%20%20node%5B%22amenity%22%3D">http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%5Btimeout%3A300%5D%3B%0Aarea%283600120067%29-%3E.searchArea%3B%0A%28%0A%20%20node%5B%22amenity%22%3D</a> %22restaurant%22%5D%28area.searchArea%29%3B%0A%20%20way%5B%22amenity%22%3D%22restaurant %22%5D%28area.searchArea%29%3B%0A%20%20relation%5B%22amenity%22%3D %22restaurant%22%5D%28area.searchArea%29%3B%0A%29%3B%0Aout%20center%3B</p>
</blockquote>
<p>As you can see in the generated url, <strong>the geocodeArea is converted to an area with ID 3600120067.</strong></p>
<p>Is there a way to keep generated url with the geocodeArea as string, so I can write a script which will generate url for all cities ?<br />
And, if not, where can I get this area ID ?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-geocodearea" rel="tag" title="see questions tagged &#39;geocodearea&#39;">geocodearea</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '20, 09:26</strong></p>
<img src="https://secure.gravatar.com/avatar/4d18662ea155ef401b24f79a0789f354?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aximem&#39;s gravatar image" />
<p><span>Aximem</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aximem has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Apr '20, 09:28</strong> </span></p>
</div>
</div>
<div id="comments-container-73905" class="comments-container">
<span id="73909"></span>
<div id="comment-73909" class="comment">
<div id="post-73909-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>the algorithm to determine the ID is given in <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Area_clauses_.28.22area_filters.22.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Area_clauses_.28.22area_filters.22.29</a></p>
</div>
<div id="comment-73909-info" class="comment-info">
<span class="comment-age">(01 Apr '20, 10:34)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="73913"></span>
<div id="comment-73913" class="comment">
<div id="post-73913-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If the names are consistent in OSM, you can use a query like <code>area[admin_level=8][name=NAME];</code> to access the area directly from Overpass API. Cities are usually admin level 8, but that can vary.</p>
</div>
<div id="comment-73913-info" class="comment-info">
<span class="comment-age">(01 Apr '20, 12:23)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="73914"></span>
<div id="comment-73914" class="comment">
<div id="post-73914-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your help, I will give it a try</p>
</div>
<div id="comment-73914-info" class="comment-info">
<span class="comment-age">(01 Apr '20, 12:25)</span> <span class="comment-user userinfo">Aximem</span>
</div>
</div>
<span id="73915"></span>
<div id="comment-73915" class="comment">
<div id="post-73915-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a>, this is working but I have to use exact city name. Some cities have the same name. For example there is 12 "Beaulieu" in France. That's why, with geocodeArea, I use "city + region + country". I cannot do this with area.</p>
</div>
<div id="comment-73915-info" class="comment-info">
<span class="comment-age">(01 Apr '20, 12:32)</span> <span class="comment-user userinfo">Aximem</span>
</div>
</div>
<span id="73916"></span>
<div id="comment-73916" class="comment">
<div id="post-73916-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can do an outer area query to deal with that, and then restrict the city query to that area. And then do another one to restrict the region query to a country, and so on.</p>
<p>Having nominatim deal with all that is nice. For some problems, using the admin_level based area query ends up being quite a bit simpler.</p>
</div>
<div id="comment-73916-info" class="comment-info">
<span class="comment-age">(01 Apr '20, 12:53)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-73905" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73905-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

