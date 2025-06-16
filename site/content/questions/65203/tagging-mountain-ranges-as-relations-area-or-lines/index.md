+++
type = "question"
title = "Tagging mountain ranges as relations? Area or lines?"
description = '''Here in Papua, Indonesia, there are many mountainous areas where the main features are the rivers, valleys and mountain ranges. Some individual peaks are named, but often a whole ridge or range of mountains has the best-known name and defines the boundaries of a village or district. The ranges are a...'''
date = "2018-08-08T02:39:00Z"
lastmod = "2018-08-16T19:40:00Z"
weight = 65203
keywords = [ "mountains", "relation", "mountain_range", "relations", "mountain" ]
aliases = [ "/questions/65203" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tagging mountain ranges as relations? Area or lines?](/questions/65203/tagging-mountain-ranges-as-relations-area-or-lines)

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
<span id="post-65203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65203-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-65203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Here in Papua, Indonesia, there are many mountainous areas where the main features are the rivers, valleys and mountain ranges. Some individual peaks are named, but often a whole ridge or range of mountains has the best-known name and defines the boundaries of a village or district. The ranges are also available in many old maps and open databases like GNIS and the 1916 Dutch map of western New Guinea, and several also have Wikipedia articles.( In Indonesian, these features are called "Pengunungan XYZ", meaning "XYZ Mountains" or "XYZ Mountain Range", while a single peak is "Gunung XYZ" or "Puncak XYZ". ). I've added many of the names for peaks, with elevation data from wikipedia or SRTM or OpenTopoMap, but we really need to be able to find larger features like "<a href="https://www.openstreetmap.org/relation/8512380">Pengunungan Cyclop</a>".</p>
<p>I tried checking the proposed features, but it seems there as never a consensus about natural=mountain_range. In the Alps it seems <a href="https://wiki.openstreetmap.org/wiki/Talk:Proposed_features/Mountains#Mountain_Range_-_Gebirge">people are tagging</a> place=region, region:type=mountain_area (see this <a href="/questions/50129/mountain-ranges">previous answer about mountain ranges</a>. But at the <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Mountains">Mountains proposal</a>, it was suggested to tag natural=mountain_range as an area (or way?):</p>
<p>And at natural=ridge, which seems to be well-used, <a href="https://wiki.openstreetmap.org/wiki/Tag:natural%3Dridge">it is said</a> that the way should be drawn from low to high ground. This means that I should draw a separate way between each saddle or pass to each peak. For a mountain range, I would need to use a relation of some kind to combine all of the ridges, saddles and peaks.</p>
<p>Using the default ID editor, I don't see any suggested relation type. Should I just make a relation, tag the relation natural=mountain_range and add each ridge, peak and saddle? Or do I need to choose a type of relation, such as route, multipolygon etc?</p>
<p>Or would it be better to draw a closed way around the whole mountainous area and tag it as natural=mountain_range plus place=region, region:type=mountain_area ? This is quite a bit more difficult in the ID editor at least</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mountains" rel="tag" title="see questions tagged &#39;mountains&#39;">mountains</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-mountain_range" rel="tag" title="see questions tagged &#39;mountain_range&#39;">mountain_range</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-mountain" rel="tag" title="see questions tagged &#39;mountain&#39;">mountain</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Aug '18, 02:39</strong></p>
<img src="https://secure.gravatar.com/avatar/984eadc21cb77cb316db4ff21c94b869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joseph%20E&#39;s gravatar image" />
<p><span>Joseph E</span><br />
<span class="score" title="390 reputation points">390</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joseph E has 2 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-65203" class="comments-container">
<span id="65208"></span>
<div id="comment-65208" class="comment">
<div id="post-65208-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I can only answer the part on the relation type. You should not use another relation type. You should create a new relation can give that the correct type by adding the tag type = &lt;the type="" you="" need=""&gt;.</p>
</div>
<div id="comment-65208-info" class="comment-info">
<span class="comment-age">(08 Aug '18, 08:26)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-65203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65203-form-container" class="comment-form-container">
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

<span id="65289"></span>

<div id="answer-container-65289" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65289-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><em>"And at natural=ridge, which seems to be well-used, it is said that the way should be drawn from low to high ground. This means that I should draw a separate way between each saddle or pass to each peak. For a mountain range, I would need to use a relation of some kind to combine all of the ridges, saddles and peaks."</em></p>
<p>Please don't add senseless huge relations, and not with the wrong tag. <strong>natural=ridge</strong> is generally for much smaller features than mountain ranges (although some ridges can at occassions be big).</p>
<p>Even if the tag is not rendered, I would stick to <strong>natural=mountain_range</strong> and simply draw one closed way around the entire feature, or a single line along its main length (if the range has a clear orientation). At some point, there will be a renderer that renders it.</p>
<p><strong>place=region, region:type=mountain_area</strong> is also a useful tag in some cases, to denote sub-areas or ragions of a mountain range, e.g. the "Alps" would classify as natural=mountain_range, while something like the "Bayerische Voralpen" is clearly neither a natural=mountain_range nor a natural=ridge, but classifies as place=region, region:type=mountain_area (as it is currently tagged).</p>
<p>Actually, I think the hierachy is a bit like this in terms of size and use:</p>
<ul>
<li>natural=mountain_range: BIGGEST FEATURE</li>
<li>place=region, region:type=mountain_area: sub-region of above: MEDIUM SIZED</li>
<li>natural=ridge: ridges on individual mountain downslope or acrorss multiple mountain peaks within a natural=mountain_range or place=region, region:type=mountain_area: SMALLEST FEATURE</li>
</ul>
<p>As linked from one of the website's you listed, the <a href="https://geo.dianacht.de/topo/?zoom=11&amp;lat=47.3947&amp;lon=11.29501&amp;layers=B0000FFFFT">https://geo.dianacht.de/topo/?zoom=11&amp;lat=47.3947&amp;lon=11.29501&amp;layers=B0000FFFFT</a> map is at least one map that (unfortunately only for the Alps currently) already displays some of this stuff (the place=region, region:type=mountain_area)</p>
<p>It is just a matter of time for the other stuff to be rendered in some other map. Tagging stuff with tags that clearly were not designed for a certain feature (like natural=ridge used for mountain ranges), won't help this though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '18, 23:51</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-65289" class="comments-container">
<span id="65312"></span>
<div id="comment-65312" class="comment">
<div id="post-65312-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"Please don't add senseless huge relations, and not with the wrong tag". I wasn't planning to make relations of type=ridge. I agree that would be incorrect.</p>
<p>I was thinking that mountain ranges could be considered the counterpart of waterways, or better yet a watershed. A waterway relation consists of several ways that are the main_stream (the largest river) and can have many tributaries (though some people think this should be included in a watershed relation instead), a spring, and can also include water areas like lakes or riverbanks. This way, the actual ways would be the tops of the ridges and the mountain peaks (and saddles / passes)</p>
<p>If I use "natural=mountain_range" and "place=region region:type=mountain_area" I would need to draw a new way or closed way for each part. I suppose this is like how a natural=valley is similar to but not the same as the course of a river through the valley. But it would seem more elegant to me if the small-scale features (ridges, peaks etc) make up the bigger feature via a relation.</p>
</div>
<div id="comment-65312-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 01:56)</span> <span class="comment-user userinfo">Joseph E</span>
</div>
</div>
<span id="65317"></span>
<div id="comment-65317" class="comment">
<div id="post-65317-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Joseph E,</p>
<p>What is your intention with wanting to tag mountain ranges? Do you want them to show up with a label in the map for identification, or not?</p>
<p>If yes, you do want them to show up in any map that may support this in the future, then honestly, the approach you suggest, is a dead end.</p>
<p>Label engines as used for rendering or in a GIS (Geographical Information System) like QGIS, cannot handle this type of relation with mixed geometry types (point, line, polygon), and even if they could, the performance would be needlessly slow and likely horrible, due the enormous complexity of the relation you suggest.</p>
<p>For any realistic chance to have your natural=mountain_range to show up in a future map as a label with the name of the range, tag with a simple closed way or a single line along its main length. This is the only realistic approach that will allow proper labeling.</p>
</div>
<div id="comment-65317-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 08:30)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
<span id="65389"></span>
<div id="comment-65389" class="comment">
<div id="post-65389-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree with <a href="https://help.openstreetmap.org/users/9580/mboeringa">@mboeringa</a>. Considering rendering and reuse of data, the most logic yet simple way to tag mountain ranges is just to draw a closed way or multipolygon and tag it as natural=mountain_range.</p>
</div>
<div id="comment-65389-info" class="comment-info">
<span class="comment-age">(16 Aug '18, 19:40)</span> <span class="comment-user userinfo">Privatemajory</span>
</div>
</div>
</div>
<div id="comment-tools-65289" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65289-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65288"></span>

<div id="answer-container-65288" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65288-score" class="post-score" title="current number of votes">
-4
</div>
<span id="post-65288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have found that tagging a way natural=ridge and name=Name of Mountain Range yields good results. My local example is <a href="https://www.openstreetmap.org/way/174808173">https://www.openstreetmap.org/way/174808173</a> for the Santa Cruz Mountains.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '18, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/cf7aea21ed49687fadf85fd50e79d16b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stevea&#39;s gravatar image" />
<p><span>stevea</span><br />
<span class="score" title="22 reputation points">22</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stevea has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65288" class="comments-container">
<span id="65293"></span>
<div id="comment-65293" class="comment">
<div id="post-65293-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That look horribly like mapping for the renderer. One rule must be that ridges dont cross watercourses, and here the line crosses several: <a href="https://www.openstreetmap.org/way/174808173#map=15/37.3117/-122.1702&amp;layers=N">https://www.openstreetmap.org/way/174808173#map=15/37.3117/-122.1702&amp;layers=N</a></p>
</div>
<div id="comment-65293-info" class="comment-info">
<span class="comment-age">(13 Aug '18, 10:46)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="65311"></span>
<div id="comment-65311" class="comment">
<div id="post-65311-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think this isn't a good solution. As Stevea said, ridges are small features that do not cross waterways. They area also supposed to be drawn with the direction of the way facing uphill, so one mountain or hill should consist of at least 2 ridge ways. The other problem is that ridges are small features that probably not be rendered on a large-scale map normally, but mountain ranges are very large features that consist of numerous peaks and ridges, so they should be tagged differently to help data users. There may only be a couple of thousand "mountain ranges" in the whole world, but there are a huge number of individual ridges, sort of like how there are millions of small streams in the world, but fewer rivers, and even fewer large rivers that need to have their area mapped out as natural=water</p>
</div>
<div id="comment-65311-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 01:46)</span> <span class="comment-user userinfo">Joseph E</span>
</div>
</div>
<span id="65318"></span>
<div id="comment-65318" class="comment">
<div id="post-65318-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would also suggest to smooth out this particular mountain range feature and remove unnecessary nodes. This will give far better labeling results than with the jagged line element that has now been entered.</p>
</div>
<div id="comment-65318-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 08:50)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
</div>
<div id="comment-tools-65288" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65288-form-container" class="comment-form-container">
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

