+++
type = "question"
title = "Overpass-api: Union of data types with &#x27;area&#x27; filter"
description = '''I&#x27;m failing to get a union of node/way/relation using the area filter. It&#x27;s returning only the first types (ie node). How do I return all? http://overpass-api.de/api/interpreter?data=[out:xml];area[name=&#x27;London&#x27;];(node&#x27;fhrs:id&#x27;;way&#x27;fhrs:id&#x27;;relation&#x27;fhrs:id&#x27;;);out body;&amp;gt;;out skel qt;&quot;'''
date = "2017-02-09T20:19:00Z"
lastmod = "2017-02-10T14:44:00Z"
weight = 54575
keywords = [ "overpass-api", "area" ]
aliases = [ "/questions/54575" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass-api: Union of data types with 'area' filter](/questions/54575/overpass-api-union-of-data-types-with-area-filter)

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
<span id="post-54575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54575-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm failing to get a union of node/way/relation using the area filter. It's returning only the first types (ie node). How do I return all?</p>
<p><a href="http://overpass-api.de/api/interpreter?data=%5Bout:xml%5D;area%5Bname=&#39;London&#39;%5D;(node">http://overpass-api.de/api/interpreter?data=[out:xml];area[name='London'];(node</a><a href="area">'fhrs:id'</a>;way<a href="area">'fhrs:id'</a>;relation<a href="area">'fhrs:id'</a>;);out body;&gt;;out skel qt;"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '17, 20:19</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-54575" class="comments-container">
&#10;</div>
<div id="comment-tools-54575" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54575-form-container" class="comment-form-container">
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

<span id="54578"></span>

<div id="answer-container-54578" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54578-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-54578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DaveF has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The help site seems to have mangled your url. Maybe the Overpass Turbo wizard does what you want?</p>
<p><a href="http://overpass-turbo.eu/s/mC7">http://overpass-turbo.eu/s/mC7</a></p>
<p>That's the result of <code>"fhrs:id"=* in London</code> in the Wizard input box.</p>
<p>Turbo has a special operator to lookup places in Nominatim, but the area syntax works too:</p>
<p><a href="http://overpass-turbo.eu/s/mC8">http://overpass-turbo.eu/s/mC8</a></p>
<p>If your url is mostly intact, the main issue is likely that the area filter has to be applied to each query as in the above links.</p>
<p>If you need the data outside Turbo, the "Export" button provides a range of options.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '17, 23:41</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-54578" class="comments-container">
<span id="54580"></span>
<div id="comment-54580" class="comment">
<div id="post-54580-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the reply. Turbo was my starting point, but I want to automate the download process via a windows batch file.</p>
<p>The Overpass help is quite confusing, but it appears that overpass.api doesn't accept (area.searchArea). It also seems to not like quote marks (") but I haven't worked out why.</p>
<p>When exported as overpassQL your Turbo routine returns the error: 'Invalid IPv6 numeric address.' (As did my attempts).</p>
</div>
<div id="comment-54580-info" class="comment-info">
<span class="comment-age">(10 Feb '17, 00:17)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="54581"></span>
<div id="comment-54581" class="comment">
<div id="post-54581-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The named areas are a feature of Overpass API. The <code>{{geocodeArea:London}}</code> in the first link is an Overpass Turbo feature, but I've swapped it out in the second link (and the "Export" feature on the Turbo website will do that for you anyway). You want to use the "raw data directly from Overpass API" export option to pull the data somewhere else.</p>
<p><a href="http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%5Btimeout%3A25%5D%3B%0Aarea%5Bname%3DLondon%5D-%3E.searchArea%3B%0A%28%0A%20%20node%5B%22fhrs%3Aid%22%5D%28area.searchArea%29%3B%0A%20%20way%5B%22fhrs%3Aid%22%5D%28area.searchArea%29%3B%0A%20%20relation%5B%22fhrs%3Aid%22%5D%28area.searchArea%29%3B%0A%29%3B%0Aout%20body%3B%0A%3E%3B%0Aout%20skel%20qt%3B">I just successfully fetched this url using wget</a></p>
</div>
<div id="comment-54581-info" class="comment-info">
<span class="comment-age">(10 Feb '17, 00:57)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="54593"></span>
<div id="comment-54593" class="comment">
<div id="post-54593-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. Got there in the end with your last example.</p>
<p>Apologies for my first post's copy/paste but this forum won't format it properly. Trying to post <a href="http://overpass-api.de/api/interpreter?data=%5Bout:xml%5D%5Btimeout:25%5D;area(3600065606);(node%5B&#39;fhrs:id&#39;%5D(area);way%5B&#39;fhrs:id&#39;%5D(area);relation%5B&#39;fhrs:id&#39;%5D(area);">this api call</a>;out center;) (&lt;Markdown won't create link or code element! it gets confused by the brackets)</p>
<p>Which I'd extrapolated from <a href="https://help.openstreetmap.org/questions/19063/get-city-nodes-within-a-country-using-overpass-api">This OSM Help Question</a></p>
<p>As I said I only get the first item (nodes) returned. Is it possible to get it to work, or is your solution the only way?</p>
</div>
<div id="comment-54593-info" class="comment-info">
<span class="comment-age">(10 Feb '17, 14:09)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="54595"></span>
<div id="comment-54595" class="comment">
<div id="post-54595-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it is necessary to either use the named area or to repeat the area statement for each query. The node(area) query overwrites the input set, so the way(area) query looks for areas in the result of the node query, and of course there are none.</p>
<p>It's possible to explicitly include the area in each query rather than doing it before the query: node(area:3600065606),way(area(3600065606) etc. I find the method using a named set clearer.</p>
<p>The docs have more about it: <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29">http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29</a></p>
</div>
<div id="comment-54595-info" class="comment-info">
<span class="comment-age">(10 Feb '17, 14:44)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-54578" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54578-form-container" class="comment-form-container">
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

