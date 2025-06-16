+++
type = "question"
title = "Getting hospitals near GPS coordinates via Nominatim is returning unexpected results"
description = '''I&#x27;ve constructed the following query, I want to get &quot;hospitals&quot; which is a special phrase according to this link https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/EN This is my query https://nominatim.openstreetmap.org/search?q=hospitals&amp;amp;format=jsonv2&amp;amp;polygon=50&amp;amp;addressdetail...'''
date = "2018-07-29T16:40:00Z"
lastmod = "2018-11-06T14:31:00Z"
weight = 65004
keywords = [ "query", "gps", "nominatim", "coordinates", "poi" ]
aliases = [ "/questions/65004" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Getting hospitals near GPS coordinates via Nominatim is returning unexpected results](/questions/65004/getting-hospitals-near-gps-coordinates-via-nominatim-is-returning-unexpected-results)

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
<span id="post-65004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65004-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've constructed the following query, I want to get "hospitals" which is a special phrase according to this link</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/EN">https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/EN</a></p>
<p>This is my query</p>
<p><a href="https://nominatim.openstreetmap.org/search?q=hospitals&amp;format=jsonv2&amp;polygon=50&amp;addressdetails=1&amp;lat=40.406932&amp;lon=-79.932963">https://nominatim.openstreetmap.org/search?q=hospitals&amp;format=jsonv2&amp;polygon=50&amp;addressdetails=1&amp;lat=40.406932&amp;lon=-79.932963</a></p>
<p>those GPS coordinates are from Pittsburgh, PA. But the results contains results from Nicaragua and Libya and they are not hospitals. Where have I made a mistake?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jul '18, 16:40</strong></p>
<img src="https://secure.gravatar.com/avatar/4f6e295d4a3e0e24268e948e79eae3fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dave4784&#39;s gravatar image" />
<p><span>Dave4784</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dave4784 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jul '18, 21:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-65004" class="comments-container">
&#10;</div>
<div id="comment-tools-65004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65004-form-container" class="comment-form-container">
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

<span id="65007"></span>

<div id="answer-container-65007" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65007-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A special phrase just means that nominatim will give some preference to items tagged amenity=hospital, it's still doing name matching on "Hospitals", so it's returning things with exactly that name.</p>
<p><a href="http://overpass-turbo.eu/s/ADE">Here's an example Overpass-API query</a> that returns hospitals within a 10 Km radius of that location. Note that you can use that query outside of Overpass Turbo, it's just a convenient way to share it.</p>
<p>You could also compute a bounding box from the coordinate and restrict the search to that area, if that were more suitable for your goal.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '18, 17:25</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jul '18, 17:25</strong> </span></p>
</div>
</div>
<div id="comments-container-65007" class="comments-container">
<span id="66667"></span>
<div id="comment-66667" class="comment">
<div id="post-66667-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello. Is something like that available for Nominatim API?</p>
</div>
<div id="comment-66667-info" class="comment-info">
<span class="comment-age">(05 Nov '18, 10:17)</span> <span class="comment-user userinfo">user5555</span>
</div>
</div>
<span id="66669"></span>
<div id="comment-66669" class="comment">
<div id="post-66669-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not beyond what is mentioned in the other answer.</p>
</div>
<div id="comment-66669-info" class="comment-info">
<span class="comment-age">(05 Nov '18, 10:46)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="66670"></span>
<div id="comment-66670" class="comment">
<div id="post-66670-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There isn't.</p>
</div>
<div id="comment-66670-info" class="comment-info">
<span class="comment-age">(05 Nov '18, 10:47)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="66692"></span>
<div id="comment-66692" class="comment">
<div id="post-66692-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, thanks. Now I want to try Overpass-API. How to send just query using REST API (POST some json url)? And where to get results? Because your example draws on the map, but I want result in text format (json)</p>
</div>
<div id="comment-66692-info" class="comment-info">
<span class="comment-age">(06 Nov '18, 11:48)</span> <span class="comment-user userinfo">user5555</span>
</div>
</div>
<span id="66694"></span>
<div id="comment-66694" class="comment">
<div id="post-66694-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Never mind. Found out <a href="https://www.overpass-api.de/api/interpreter?data=THE">https://www.overpass-api.de/api/interpreter?data=THE</a> SAME QUERY AS IN YOUR EXAMPLE, BUT EVERYTHING IN ONE LINE</p>
</div>
<div id="comment-66694-info" class="comment-info">
<span class="comment-age">(06 Nov '18, 12:04)</span> <span class="comment-user userinfo">user5555</span>
</div>
</div>
<span id="66696"></span>
<div id="comment-66696" class="comment not_top_scorer">
<div id="post-66696-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And one more question - how to search for any building/place using any name? So it can be anything, not necessarily hospital. I tried replace "amenity" with "name", but it does't work like with Nominatim API, it excepts name which will match 100%, but I want just normal name query (like we search in Google and in Nominatim API)</p>
</div>
<div id="comment-66696-info" class="comment-info">
<span class="comment-age">(06 Nov '18, 13:55)</span> <span class="comment-user userinfo">user5555</span>
</div>
</div>
<span id="66700"></span>
<div id="comment-66700" class="comment not_top_scorer">
<div id="post-66700-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Don't add questions to answers. Instead <a href="/questions/ask/">create a new question</a>.</p>
</div>
<div id="comment-66700-info" class="comment-info">
<span class="comment-age">(06 Nov '18, 14:31)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65007" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-65007-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65009"></span>

<div id="answer-container-65009" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65009-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The /search endpoint doesn't understand &amp;lat or &amp;lon parameters (only /reverse does), setting &amp;polygon= to 50 has the same effect as 1 and only affects the output. See <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Search">https://wiki.openstreetmap.org/wiki/Nominatim#Search</a></p>
<p>The closest you can get with Nominatim is using a query 'hospitals near 40.406932,-79.932963'. The 'near' (or 'in') is optional. You can set the &amp;limit=50 to get more results (maximum is 100).</p>
<p>The Overpass-API system is more flexible (support more types of point-of-interest, more filters, better control over the search radius) overall.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '18, 21:45</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-65009" class="comments-container">
<span id="65068"></span>
<div id="comment-65068" class="comment">
<div id="post-65068-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I like using the "hospital near 40.406932,-79.932963" method, but at some places it returns nothing. Is there a way to increase the sq miles it checks?</p>
</div>
<div id="comment-65068-info" class="comment-info">
<span class="comment-age">(01 Aug '18, 21:26)</span> <span class="comment-user userinfo">Dave4784</span>
</div>
</div>
<span id="65152"></span>
<div id="comment-65152" class="comment">
<div id="post-65152-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nominatim doesn't have a parameter for that.</p>
</div>
<div id="comment-65152-info" class="comment-info">
<span class="comment-age">(06 Aug '18, 11:13)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-65009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65009-form-container" class="comment-form-container">
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

