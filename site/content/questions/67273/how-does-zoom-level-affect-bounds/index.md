+++
type = "question"
title = "How does zoom level affect bounds?"
description = '''Hello! I am trying to find a method to find bbox bounds (left, right, top, bottom) from given zoom level and coordinates. I am writing a function in MATLAB that uses zoom and coordinates as parameters to go to openstreetmap.org and export the OSM just as openstreetmap does so that I can easily save ...'''
date = "2018-12-18T22:50:00Z"
lastmod = "2018-12-20T19:07:00Z"
weight = 67273
keywords = [ "zoomlevel", "matlab", "bbox" ]
aliases = [ "/questions/67273" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How does zoom level affect bounds?](/questions/67273/how-does-zoom-level-affect-bounds)

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
<span id="post-67273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67273-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello! I am trying to find a method to find bbox bounds (left, right, top, bottom) from given zoom level and coordinates. I am writing a function in MATLAB that uses zoom and coordinates as parameters to go to openstreetmap.org and export the OSM just as openstreetmap does so that I can easily save several different OSM files and open them as xml files from within MATLAB, moving towards the next goal of recreating maps from the OSM files.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-matlab" rel="tag" title="see questions tagged &#39;matlab&#39;">matlab</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '18, 22:50</strong></p>
<img src="https://secure.gravatar.com/avatar/35ea97637fc08dfdde60934ba34c6996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jholland4134&#39;s gravatar image" />
<p><span>jholland4134</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jholland4134 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Dec '18, 19:10</strong> </span></p>
</div>
</div>
<div id="comments-container-67273" class="comments-container">
<span id="67274"></span>
<div id="comment-67274" class="comment">
<div id="post-67274-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I do not understand your question, sorry. Why should a zoom level affect coordinates at all? Please give some more detail. By chance: do you mean the edge coordinates of a view area?</p>
</div>
<div id="comment-67274-info" class="comment-info">
<span class="comment-age">(19 Dec '18, 06:56)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="67283"></span>
<div id="comment-67283" class="comment">
<div id="post-67283-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My apologies, I meant how does the zoom level effect the bound box's coordinates/min and max latitude and longitude.</p>
<p>For example, if I select latitude of 28.06597 and longitude of -82.52889 with a zoom level of 19, top=28.06582, bottom=28.06612, left=-82.52937, and right=-82.52841. I'm trying to figure out how to calculate these bounds. Link I'm referring to: <a href="https://www.openstreetmap.org/export#map=19/28.06597/-82.52889">https://www.openstreetmap.org/export#map=19/28.06597/-82.52889</a></p>
</div>
<div id="comment-67283-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 03:06)</span> <span class="comment-user userinfo">jholland4134</span>
</div>
</div>
<span id="67285"></span>
<div id="comment-67285" class="comment">
<div id="post-67285-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So basically you wan to know how the website calculates these four values based on your centre coordinates from the URL ("28.06597/-82.52889") and the currently displayed map size? While someone could surely answer that (probably with a deep reference to the <a href="https://github.com/openstreetmap/openstreetmap-website/">OSM website code</a>), I fail to see why this is useful - except if you want to program such a website. So, is this what you want?</p>
</div>
<div id="comment-67285-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 06:09)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="67290"></span>
<div id="comment-67290" class="comment">
<div id="post-67290-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The bounds of the map on the website don't just depend on the zoom level and center coordinate.T he size of the map div inside the browser window also matters, i.e. the screen resolution and a few things more. But maybe you are actually searching for something different. Did you already read <a href="https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames">slippy map tilenames</a>? It contains a collection of formulas and explanations.</p>
</div>
<div id="comment-67290-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 09:19)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="67294"></span>
<div id="comment-67294" class="comment">
<div id="post-67294-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>aseerel4c26, that is correct but what I am trying to do is to write a function for MATLAB to retrieve the OSM from openstreetmap.org by providing zoom and coordinates as parameters. Right now, the code works but how I was handling zoom's effect on the bbox is not the same as open street map, leading to a smaller bbox and OSM files that differ from open street's exported OSM files.</p>
<p>scai, I have not yet but will take a look. Thank you for the link.</p>
</div>
<div id="comment-67294-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 17:52)</span> <span class="comment-user userinfo">jholland4134</span>
</div>
</div>
<span id="67296"></span>
<div id="comment-67296" class="comment not_top_scorer">
<div id="post-67296-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>After looking over the link to the slippy tilenames, I noticed the Perl LonLat_to_bbox program seems to be what I'm looking for. The only issue to sort out is that the code is meant for embedding a map and uses the desired width and height as part finding the corresponding OSM.</p>
</div>
<div id="comment-67296-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 18:30)</span> <span class="comment-user userinfo">jholland4134</span>
</div>
</div>
<span id="67297"></span>
<div id="comment-67297" class="comment not_top_scorer">
<div id="post-67297-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16047/jholland4134">@jholland4134</a>: Yes, Perl LonLat_to_bbox seems to be what you want, but I do not understand your problem to use this code. As also said in my first comment: you need to provide more detail. E.g. which framework do you use in Matlab? What are you displaying there?</p>
<p>It would be nice if you could add this to your original question text ("edit") - that makes this question entry easier to read for others coming by with the same question later on.</p>
</div>
<div id="comment-67297-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 18:53)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="67298"></span>
<div id="comment-67298" class="comment not_top_scorer">
<div id="post-67298-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16047/jholland4134"></a><a href="https://help.openstreetmap.org/users/16047/jholland4134">@jholland4134</a>: By the way, the <a href="https://www.openstreetmap.org/export">https://www.openstreetmap.org/export</a> function of osm.org is meant for small scale exports only. No big ones, no heavy use, and is - as the website in general - targeted at mappers. There are other options - see <a href="https://wiki.openstreetmap.org/wiki/Downloading_data">https://wiki.openstreetmap.org/wiki/Downloading_data</a> . As long as you are just in development phase that use of /export is perfectly fine!</p>
</div>
<div id="comment-67298-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 18:53)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="67299"></span>
<div id="comment-67299" class="comment not_top_scorer">
<div id="post-67299-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> Thank you for the suggestion, I updated the question with some more detail. I simply want to use MATLAB to export the OSM file and then open it within MATLAB as an XML. The purpose is to use coordinates for several locations from another file as function parameters to go to openstreetmap and export the corresponding OSM files.</p>
</div>
<div id="comment-67299-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 19:07)</span> <span class="comment-user userinfo">jholland4134</span>
</div>
</div>
</div>
<div id="comment-tools-67273" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-67273-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

