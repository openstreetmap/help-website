+++
type = "question"
title = "What makes a closed way show up as an Enclosing Feature with Query Features?"
description = '''There are two nearby state forests, &quot;A&quot; and &quot;B&quot;. When I use Query Features in OSM, and select a feature like a road or path inside &quot;A&quot;, the sidebar includes the state forest &quot;A&quot; as an Enclosing Feature. But when I do the same thing with a feature inside &quot;B&quot;, it does not list &quot;B&quot; as an enclosing feat...'''
date = "2016-02-13T03:22:00Z"
lastmod = "2016-02-16T19:34:00Z"
weight = 48088
keywords = [ "overpass", "boundary", "area", "multipolygon" ]
aliases = [ "/questions/48088" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What makes a closed way show up as an Enclosing Feature with Query Features?](/questions/48088/what-makes-a-closed-way-show-up-as-an-enclosing-feature-with-query-features)

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
<span id="post-48088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48088-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are two nearby state forests, "A" and "B". When I use Query Features in OSM, and select a feature like a road or path inside "A", the sidebar includes the state forest "A" as an Enclosing Feature. But when I do the same thing with a feature inside "B", it does not list "B" as an enclosing feature.</p>
<p>I would like to fix "B", so I looked closer at the features and tags.</p>
<p>Both "A" and "B" are closed ways, with landuse=forest and a name. But "A" is the outer-role member of a multipolygon relation, and B is not a member of a relation. That is the only difference. So it seems to me that being a member of a multipolygon relation makes the way a candidate for being an enclosing feature.</p>
<p>Other features I see listed under Enclosing Features are administrative boundaries (with or without multipolygons), so it seems that type=boundary and/or boundary=administrative also makes a closed way appear as an enclosing feature.</p>
<p>Am I right about this? Is there documentation on what causes a closed Way to be listed as an enclosing feature? (I couldn't find anything on the OSM wiki.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '16, 03:22</strong></p>
<img src="https://secure.gravatar.com/avatar/c1e98ded2982cd352d4c77075aa0cd74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ljb_nj&#39;s gravatar image" />
<p><span>ljb_nj</span><br />
<span class="score" title="659 reputation points">659</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ljb_nj has one accepted answer">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Feb '16, 08:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-48088" class="comments-container">
<span id="48116"></span>
<div id="comment-48116" class="comment">
<div id="post-48116-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It would help us a lot understanding your issue if you could provide links to "A" and "B".</p>
</div>
<div id="comment-48116-info" class="comment-info">
<span class="comment-age">(14 Feb '16, 08:54)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="48187"></span>
<div id="comment-48187" class="comment">
<div id="post-48187-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Follow up ticket: <a href="https://github.com/openstreetmap/openstreetmap-website/issues/1156">https://github.com/openstreetmap/openstreetmap-website/issues/1156</a></p>
</div>
<div id="comment-48187-info" class="comment-info">
<span class="comment-age">(16 Feb '16, 19:34)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-48088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48088-form-container" class="comment-form-container">
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

<span id="48089"></span>

<div id="answer-container-48089" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48089-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The enclosing features are area features coming from <a href="http://overpass-api.de/">http://overpass-api.de/</a> .</p>
<p>There is some discussion here:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Areas">https://wiki.openstreetmap.org/wiki/Overpass_API/Areas</a></p>
<p>I think a landuse=forest should create an area, but maybe it hasn't been generated yet. I used the script below to find out that areas were last generated 2 days ago. Is the feature newer than that?</p>
<p>This is about the simplest script that will return an area:</p>
<p><a href="http://overpass-turbo.eu/s/eo7">http://overpass-turbo.eu/s/eo7</a></p>
<p>The timestamp is returned in the output, Overpass Turbo does the math and displays it if you hover over the statistics on the lower right.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '16, 04:27</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Feb '16, 04:36</strong> </span></p>
</div>
</div>
<div id="comments-container-48089" class="comments-container">
<span id="48091"></span>
<div id="comment-48091" class="comment">
<div id="post-48091-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>According to the script that generates the areas (<a href="https://github.com/drolbr/Overpass-API/blob/master/rules/areas.osm3s">areas.osm3s</a>) multipolygon relations are only considered if they have a <em>name</em> tag. This name tag requirement also applies to some other objects (e.g. relations tagged with <em>admin_level</em> or <em>boundary</em>, various ways with certain tags) but not all of them (e.g. relations with <em>postal_code</em> or <em>addr:postcode</em> tag). But that doesn't mean that people should start adding <a href="https://wiki.openstreetmap.org/wiki/Names#Name_is_the_name_only">wrong name tags</a>.</p>
</div>
<div id="comment-48091-info" class="comment-info">
<span class="comment-age">(13 Feb '16, 08:21)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="48109"></span>
<div id="comment-48109" class="comment">
<div id="post-48109-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the info. The link lead me to this textual description of what makes a way into a polygon (area): <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo/Polygon_Features">https://wiki.openstreetmap.org/wiki/Overpass_turbo/Polygon_Features</a></p>
<p>According to that, landuse=forest on a closed loop way without area=no makes a polygon. But I know that isn't working as far as "enclosing features" goes. I also looked at the area3.osm3s script. With my very limited understanding of it, I see it does use landuse (other than no), with name, and not area=no to make a polygon. I also see the script considers a multipolygon to be a polygon but only if it has a name, and the one ("A" above) does not, yet it does work as an enclosing feature.</p>
<p>I'm going to try to fix my case "B" above - to make it like "A" and see what happens. As much as I would like to understand what is happening, I'm OK with fixing the feature and moving on.</p>
</div>
<div id="comment-48109-info" class="comment-info">
<span class="comment-age">(13 Feb '16, 23:07)</span> <span class="comment-user userinfo">ljb_nj</span>
</div>
</div>
<span id="48129"></span>
<div id="comment-48129" class="comment">
<div id="post-48129-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is very strange, and I obviously don't know what is going on. But after looking at it some more, the problem isn't that the State Forests don't show as Enclosing Features. The problem is that <em>nothing</em> shows as enclosing features. This is happening for large areas of Southern New Jersey, such as here: <a href="https://www.openstreetmap.org/#map=15/39.6176/-74.5007">https://www.openstreetmap.org/#map=15/39.6176/-74.5007</a></p>
<p>When I use Query Features on a road there, I see no Enclosing Features at all. But further south, I see at least a County, State, and Country as Enclosing Features.</p>
<p>Something seems to be blocking it from working there. I thought maybe it was the Pinelands National Reserve area ( <a href="https://www.openstreetmap.org/way/33832747">https://www.openstreetmap.org/way/33832747</a> ) which is a huge closed way that surrounds this (tags: area=yes, boundary=national_park) but that doesn't seem to be the cause. Enclosing Features works in some places inside this area.</p>
</div>
<div id="comment-48129-info" class="comment-info">
<span class="comment-age">(15 Feb '16, 03:10)</span> <span class="comment-user userinfo">ljb_nj</span>
</div>
</div>
<span id="48145"></span>
<div id="comment-48145" class="comment">
<div id="post-48145-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A script like this, with the coordinates copied from a failed query:</p>
<pre><code>is_in(39.6883,-74.4133);
out;</code></pre>
<p>(<a href="http://overpass-turbo.eu/s/eqa">try it here</a>)</p>
<p>Succeeds, so the problem does not seem to be the existence of the areas on the Overpass API server.</p>
<p>Firefox reports an error on the blank results <code>TypeError: e.bounds is undefined</code>, and not on successful results. So the issue is probably in the JS code powering the query feature. Not sure where to begin debugging that, maybe in <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/app/assets/javascripts/index/query.js">https://github.com/openstreetmap/openstreetmap-website/blob/master/app/assets/javascripts/index/query.js</a></p>
</div>
<div id="comment-48145-info" class="comment-info">
<span class="comment-age">(15 Feb '16, 15:14)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="48166"></span>
<div id="comment-48166" class="comment not_top_scorer">
<div id="post-48166-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>maxerickson: I think you have figured it out. The areas are OK, but the problem is with the browser and the query. I am seeing almost the same thing: "Error: TypeError: t.bounds is undefined", "Source File: <a href="https://www.openstreetmap.org/assets/...">https://www.openstreetmap.org/assets/..."</a> in my browser. (Using either Firefox or Seamonkey browsers.)</p>
<p>But I suppose it still could be something in the map data that triggers this, which would explain why it only happens in some areas.</p>
</div>
<div id="comment-48166-info" class="comment-info">
<span class="comment-age">(15 Feb '16, 23:31)</span> <span class="comment-user userinfo">ljb_nj</span>
</div>
</div>
<span id="48186"></span>
<div id="comment-48186" class="comment">
<div id="post-48186-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I created a ticket for this issue now: <a href="https://github.com/openstreetmap/openstreetmap-website/issues/1156">https://github.com/openstreetmap/openstreetmap-website/issues/1156</a></p>
<p>Please follow up there.</p>
</div>
<div id="comment-48186-info" class="comment-info">
<span class="comment-age">(16 Feb '16, 19:33)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-48089" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-48089-form-container" class="comment-form-container">
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

