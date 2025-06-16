+++
type = "question"
title = "is is possible to download a reduced dataset of openstreetmap which doesn&#x27;t include fine zoom levels ?"
description = '''I don&#x27;t know exactly what sort of space partitioning algorithm OSM uses, and I wonder if the OSM supports what I want. Basically, if you want to render france, you render it at a certain zoom level, and you obviously don&#x27;t query small street data. At this point, does it make sense that if I don&#x27;t wa...'''
date = "2014-05-26T18:56:00Z"
lastmod = "2014-05-28T00:19:00Z"
weight = 33489
keywords = [ "zoomlevel", "download", "zoom" ]
aliases = [ "/questions/33489" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [is is possible to download a reduced dataset of openstreetmap which doesn't include fine zoom levels ?](/questions/33489/is-is-possible-to-download-a-reduced-dataset-of-openstreetmap-which-doesnt-include-fine-zoom-levels)

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
<span id="post-33489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33489-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I don't know exactly what sort of space partitioning algorithm OSM uses, and I wonder if the OSM supports what I want.</p>
<p>Basically, if you want to render france, you render it at a certain zoom level, and you obviously don't query small street data. At this point, does it make sense that if I don't want to zoom and display areas and details which are under 50km, the entire planet data would be much smaller than the 40GB file download.</p>
<p>Is there such available download, if not, is it supported in the API ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '14, 18:56</strong></p>
<img src="https://secure.gravatar.com/avatar/5b1e3128b33fa994d6c6640fb49898da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jokoon&#39;s gravatar image" />
<p><span>jokoon</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jokoon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33489" class="comments-container">
<span id="33511"></span>
<div id="comment-33511" class="comment">
<div id="post-33511-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>quite the same question as <a href="/questions/31760/">different-level-of-detail-at-different-zoom-level-api</a>, isn't it?</p>
</div>
<div id="comment-33511-info" class="comment-info">
<span class="comment-age">(27 May '14, 17:22)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33489" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33489-form-container" class="comment-form-container">
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

<span id="33491"></span>

<div id="answer-container-33491" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33491-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-33491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, OpenStreetMap doesn't have such a kind of download. OSM always works at the highest possible resolution.</p>
<p>To some extent it is possible to download a selection of data - e.g. just the boundary of France - using tools like the Overpass API, but again the boundary will be at maximum resolution.</p>
<p>If you want to draw a map for low zoom levels, maybe you shouldn't use OpenStreetMap at all - head over to <a href="http://www.naturalearthdata/">http://www.naturalearthdata/</a> and check out what they have.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '14, 19:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-33491" class="comments-container">
<span id="33495"></span>
<div id="comment-33495" class="comment">
<div id="post-33495-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Frederik is right. Moreover, natural earth data has shorelines and boundaries simplified for lower zoom levels using some sophisticated node elimination algorithms. I played with the 10m and the 110m datasets and coastlines are heavily reduced - meaning performance goes up.</p>
<p>I suspect that some aggregation algorithms are implemented in mapnik, since features are simplified at lower zoom levels.</p>
</div>
<div id="comment-33495-info" class="comment-info">
<span class="comment-age">(26 May '14, 19:57)</span> <span class="comment-user userinfo">MatthiasN</span>
</div>
</div>
<span id="33496"></span>
<div id="comment-33496" class="comment">
<div id="post-33496-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>so how are the lowest zoom PNG generated (meaning browsing at the scale of continents) ? if that's the case doesn't that mean generating low zoom is expensive ?</p>
</div>
<div id="comment-33496-info" class="comment-info">
<span class="comment-age">(26 May '14, 20:30)</span> <span class="comment-user userinfo">jokoon</span>
</div>
</div>
<span id="33499"></span>
<div id="comment-33499" class="comment">
<div id="post-33499-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The fact that the data is distributed as a big blob, doesn't mean that whoever renders a map from it can't preprocess parts of it or combine it with other lower resolution datasets. Also since the low zoom tiles are catched it is not really a problem if is more expensive to generate them.</p>
<p>Read <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> for the map style used by openstreetmap and follow some of the links for the data sources mentioned there.</p>
</div>
<div id="comment-33499-info" class="comment-info">
<span class="comment-age">(26 May '14, 22:12)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="33504"></span>
<div id="comment-33504" class="comment">
<div id="post-33504-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@jokoon</span> yes, low zoom tiles are expensive (most so in the "middle" zoom range)</p>
</div>
<div id="comment-33504-info" class="comment-info">
<span class="comment-age">(27 May '14, 07:57)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="33519"></span>
<div id="comment-33519" class="comment not_top_scorer">
<div id="post-33519-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>any planet dataset file in some "minimal" or "lite" version or with a low zoom level ?</p>
</div>
<div id="comment-33519-info" class="comment-info">
<span class="comment-age">(28 May '14, 00:12)</span> <span class="comment-user userinfo">jokoon</span>
</div>
</div>
<span id="33520"></span>
<div id="comment-33520" class="comment">
<div id="post-33520-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@jokoon</span> No - see SimonPoole's answer ("... no ... you will need to download an extract for the area you are interested in and filter out what you don't want.")</p>
</div>
<div id="comment-33520-info" class="comment-info">
<span class="comment-age">(28 May '14, 00:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33491" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-33491-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33492"></span>

<div id="answer-container-33492" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33492-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The simple answer: no.</p>
<p>The more complicated one: to acheive what you want you will need to download an extract for the area you are interested in and filter out what you don't want.</p>
<p>Extracts for example <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a></p>
<p>Filter for example: <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">https://wiki.openstreetmap.org/wiki/Osmfilter</a></p>
<p>But there are many ways to skin a cat.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '14, 19:05</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 May '14, 19:07</strong> </span></p>
</div>
</div>
<div id="comments-container-33492" class="comments-container">
&#10;</div>
<div id="comment-tools-33492" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33492-form-container" class="comment-form-container">
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

