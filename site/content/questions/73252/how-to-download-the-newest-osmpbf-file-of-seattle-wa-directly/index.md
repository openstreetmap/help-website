+++
type = "question"
title = "How to download the newest osm.pbf file of Seattle, WA directly?"
description = '''Hello, I want to download the .pbf file of Seattle directly.  I tried using BBBike.org but the data on that site is not up to date, and other services seems no manual bbox (type the 4 coordinate) extract support. Also, I think download the plant.osm and crop it inconvenient. There&#x27;s no matter what s...'''
date = "2020-02-27T02:24:00Z"
lastmod = "2020-02-27T10:38:00Z"
weight = 73252
keywords = [ "osm.pbf" ]
aliases = [ "/questions/73252" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to download the newest osm.pbf file of Seattle, WA directly?](/questions/73252/how-to-download-the-newest-osmpbf-file-of-seattle-wa-directly)

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
<span id="post-73252-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73252-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73252-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I want to download the .pbf file of <strong>Seattle</strong> directly.</p>
<p>I tried using <a href="http://bbbike.org">BBBike.org</a> but the data on that site is not up to date, and other services seems no manual bbox (type the 4 coordinate) extract support.</p>
<p>Also, I think download the plant.osm and crop it inconvenient.</p>
<p>There's no matter what shape it is (a rectangle or the city border), and how to get the newest .pbf file?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.pbf" rel="tag" title="see questions tagged &#39;osm.pbf&#39;">osm.pbf</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Feb '20, 02:24</strong></p>
<img src="https://secure.gravatar.com/avatar/ce191c15bc265d7e06ed6c4c6ce9a527?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mxooc&#39;s gravatar image" />
<p><span>mxooc</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mxooc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73252" class="comments-container">
<span id="73263"></span>
<div id="comment-73263" class="comment">
<div id="post-73263-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Maybe it would be a good idea to explain what you actually want to acheive in the end?</p>
</div>
<div id="comment-73263-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 10:02)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="73269"></span>
<div id="comment-73269" class="comment">
<div id="post-73269-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Opening a whole city's data in JOSM is unusual, and might be impossible.</p>
</div>
<div id="comment-73269-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 10:22)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-73252" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73252-form-container" class="comment-form-container">
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

<span id="73253"></span>

<div id="answer-container-73253" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73253-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-73253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mxooc has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Would the state of Washington be too big? This one from Geofabrik is 5 hours old:</p>
<p><a href="http://download.geofabrik.de/north-america/us/washington-latest.osm.pbf">http://download.geofabrik.de/north-america/us/washington-latest.osm.pbf</a></p>
<p>Exact procedure:</p>
<ol>
<li>Download Washington extract from Geofabrik.</li>
<li>Download Seattle poly from ploygons.openstreetmap.fr as seattle.poly</li>
<li>Use osmconvert: osmconvert washington.osm.pbf -B=seattle.poly -o=seattle.osm.pbf</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '20, 07:08</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '20, 10:40</strong> </span></p>
</div>
</div>
<div id="comments-container-73253" class="comments-container">
<span id="73259"></span>
<div id="comment-73259" class="comment">
<div id="post-73259-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I think it will be too big and slower when render in JOSM. I also tried to use the Overpass API to download the Seattle area, but I don't know which format it is (seems it isn't a .osm but a .xml file) or how to open it. Is there a command that can convert it into a osm.pbf file in the Linux terminal?</p>
</div>
<div id="comment-73259-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 09:45)</span> <span class="comment-user userinfo">mxooc</span>
</div>
</div>
<span id="73262"></span>
<div id="comment-73262" class="comment">
<div id="post-73262-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>maybe try osmconvert like this: <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Example_using_a_polygon_file_from_polygons.openstreetmap.fr">https://wiki.openstreetmap.org/wiki/Osmconvert#Example_using_a_polygon_file_from_polygons.openstreetmap.fr</a> with poly <a href="http://polygons.openstreetmap.fr/get_poly.py?id=237385&amp;params=0">http://polygons.openstreetmap.fr/get_poly.py?id=237385&amp;params=0</a> on the washingon.osm.pbf ?</p>
</div>
<div id="comment-73262-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 09:53)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="73265"></span>
<div id="comment-73265" class="comment">
<div id="post-73265-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I generate the output .pbf file successfully, but I can't open it in JOSM because it isn't the .osm.pbf format, is there any difference between these 2 formats?</p>
</div>
<div id="comment-73265-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 10:08)</span> <span class="comment-user userinfo">mxooc</span>
</div>
</div>
<span id="73267"></span>
<div id="comment-73267" class="comment not_top_scorer">
<div id="post-73267-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hm, the pbf should be a .osm.pbf. Did you try renaming it or using osmconvert with -o seattle.osm.pbf?</p>
</div>
<div id="comment-73267-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 10:19)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="73268"></span>
<div id="comment-73268" class="comment not_top_scorer">
<div id="post-73268-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://wiki.openstreetmap.org/wiki/OSM_file_formats">https://wiki.openstreetmap.org/wiki/OSM_file_formats</a></p>
</div>
<div id="comment-73268-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 10:20)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73270"></span>
<div id="comment-73270" class="comment">
<div id="post-73270-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, and then it can be imported. Thank you.</p>
</div>
<div id="comment-73270-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 10:23)</span> <span class="comment-user userinfo">mxooc</span>
</div>
</div>
<span id="73272"></span>
<div id="comment-73272" class="comment">
<div id="post-73272-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>thank you, so I edited the answer to present a step by step procedure for anyone facing the same problem.</p>
</div>
<div id="comment-73272-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 10:38)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-73253" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-73253-form-container" class="comment-form-container">
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

