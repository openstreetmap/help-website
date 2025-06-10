+++
type = "question"
title = "Getting administrative boundaries of a given country for all its admin_level"
description = '''Hello, I have found the website &quot;OSM Boundaries Map 4.1&quot; on https://wambachers-osm.website/boundaries/, it shows exactly what I would like to perfom with its exploring tree: for a given country I would like to get all the lower admin_levels and their administrative boundaries. So I tried to find the...'''
date = "2017-02-14T18:07:00Z"
lastmod = "2022-04-27T10:42:00Z"
weight = 54632
keywords = [ "openstreetmap", "boundaries", "overpass-ql" ]
aliases = [ "/questions/54632" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Getting administrative boundaries of a given country for all its admin_level](/questions/54632/getting-administrative-boundaries-of-a-given-country-for-all-its-admin_level)

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
<span id="post-54632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54632-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have found the website "OSM Boundaries Map 4.1" on <a href="https://wambachers-osm.website/boundaries/,">https://wambachers-osm.website/boundaries/,</a> it shows exactly what I would like to perfom with its exploring tree: for a given country I would like to get all the lower admin_levels and their administrative boundaries. So I tried to find the queries allowing me to get the boundaries for each admin_level of a given country.</p>
<p>From levels 2 to 4 it's ok and quite simple, I came succesfully to the generic query:</p>
<pre><code>rel[admin_level=(level number)]
   [type=boundary]
   [boundary=administrative]
   [ (specific tag to identify the country, see below) ];
out geom;
&#10;--With the specific tags to identify the country (with XX=iso2 country code):
admin_level=2 &gt; [&quot;ISO3166-1&quot;~&quot;^XX&quot;]
admin_level=3 &gt; [&quot;is_in:country&quot;=&quot;XX&quot;]
admin_level=4 &gt; [&quot;ISO3166-2&quot;~&quot;^XX&quot;]</code></pre>
<p>But after that I encounter two issues: - I can't find a generic query effective for all the countries - I can't link lower admin_level to its upper admin_level (or inversely)</p>
<p>Indeed, from level 5 I can't find any generic query I could use in any country. Indeed the different countries in the world will have specific tags in their admin_levels or won't have tag at all identifying the country. For example admin_level=5 "Greater London" in England doesn't have any tag identifying the country or upper level identification. Admin_level=6 "London" has the following tag to identify "is_in:iso_3166_2"="GB-ENG", but admin_level=6 "Nord" in France has a different tag: "ISO3166-2", not the "is_in" tag. Last example, for all cities in France (admin_level=8), I can't find any tag linked to the country or at list the upper level.</p>
<p>I found out that some levels has a "subarea" mentionned, but it's not in all levels. The only solution I have at the moment is to search all boundaries whose the "admin_center" is in the upper boundary, but it's very heavy to perform on all admin levels of all countries...</p>
<p>Do you know how I can get all administrative boundaries of all admin_level of a given country? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Feb '17, 18:07</strong></p>
<img src="https://secure.gravatar.com/avatar/dd59778562963735dafa722bbbb02158?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thomas_bilendi&#39;s gravatar image" />
<p><span>thomas_bilendi</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thomas_bilendi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '17, 08:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-54632" class="comments-container">
<span id="54656"></span>
<div id="comment-54656" class="comment">
<div id="post-54656-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>crosspost: <a href="https://stackoverflow.com/questions/42257339/openstreetmap-getting-administrative-boundaries-of-a-given-country-for-all-its">https://stackoverflow.com/questions/42257339/openstreetmap-getting-administrative-boundaries-of-a-given-country-for-all-its</a></p>
</div>
<div id="comment-54656-info" class="comment-info">
<span class="comment-age">(15 Feb '17, 19:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="56830"></span>
<div id="comment-56830" class="comment">
<div id="post-56830-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you solved this problem since then?</p>
</div>
<div id="comment-56830-info" class="comment-info">
<span class="comment-age">(01 Jul '17, 23:10)</span> <span class="comment-user userinfo">meglio</span>
</div>
</div>
</div>
<div id="comment-tools-54632" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54632-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="54633"></span>

<div id="answer-container-54633" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54633-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Trying to do that with Overpass is probably not a good idea as you rely on structures that may or may not be there (even the admin_centre is not guaranteed to be set). Did you notice the wno-edv-service.de web site has a download option?</p>
<p>I'd recommend loading the OSM data for your area of interest into a database with osm2pgsql (you can use a much reduced style file on import if you're only interested in administrative areas). After that, you can use the power of PostGIS to answer questions like "give me all admin boundaries that are inside this polygon" and so on. And you can easily export to GeoJSON or Shape files.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '17, 18:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54633" class="comments-container">
<span id="54646"></span>
<div id="comment-54646" class="comment">
<div id="post-54646-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Frederik, Yes I have seen the download section, but since this service is kindly provided by a private individual, it could stop at any moment. So this is why I wanted to be able to query myself directly osm data.</p>
<p>Indeed, I could load the osm data for my area into my postgis db then query it, but this is a huge amount of data and that's why I try to find the query to download only admin_levels (I will have to download data every month). After that, as you said, I can use PostGIS and query the imported boundaries.</p>
</div>
<div id="comment-54646-info" class="comment-info">
<span class="comment-age">(15 Feb '17, 10:46)</span> <span class="comment-user userinfo">thomas_bilendi</span>
</div>
</div>
</div>
<div id="comment-tools-54633" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54633-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54634"></span>

<div id="answer-container-54634" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54634-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For a country where it works (i.e. Denmark) you can try <code>boundary=administrative &amp; type:relation in Danmark</code> in the Overpass Turbo wizard (replace "Danmark" with the name of your preferred country).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '17, 20:32</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-54634" class="comments-container">
<span id="54647"></span>
<div id="comment-54647" class="comment">
<div id="post-54647-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Hjart, Yes I can, but its not the same for every country, and even in Denmark some admin_levels (e.g. admin_level=7) don't have that country tag (specific example: rel(2190242). So what I try to find is how the admin_levels are linked to each other</p>
</div>
<div id="comment-54647-info" class="comment-info">
<span class="comment-age">(15 Feb '17, 10:53)</span> <span class="comment-user userinfo">thomas_bilendi</span>
</div>
</div>
</div>
<div id="comment-tools-54634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54634-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84286"></span>

<div id="answer-container-84286" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84286-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This website presents the boundaries hierarchically using admin_level: <a href="https://osm-boundaries.com"></a><a href="https://osm-boundaries.com">https://osm-boundaries.com</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '22, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/61c58c3ad85157ecf983d3358a4a0903?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pcgomes&#39;s gravatar image" />
<p><span>pcgomes</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pcgomes has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84286" class="comments-container">
&#10;</div>
<div id="comment-tools-84286" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84286-form-container" class="comment-form-container">
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

