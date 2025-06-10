+++
type = "question"
title = "How to extract boundaries (different administrative levels) from planet file"
description = '''Hello, This is my first approach at OSM, so forgive me for my lack of knowledge. I would like to have the borders from Belgium on the following administrative levels:  2 (national border) 4 (regions) 6 (provinces) 8 (municipalities)  These borders would be read into a Java application to draw a heat...'''
date = "2012-09-26T03:14:00Z"
lastmod = "2013-03-22T20:33:00Z"
weight = 16471
keywords = [ "boundaries", "planet", "administrative", "osmosis" ]
aliases = [ "/questions/16471" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to extract boundaries (different administrative levels) from planet file](/questions/16471/how-to-extract-boundaries-different-administrative-levels-from-planet-file)

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
<span id="post-16471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16471-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>This is my first approach at OSM, so forgive me for my lack of knowledge. I would like to have the borders from Belgium on the following administrative levels:</p>
<ul>
<li>2 (national border)</li>
<li>4 (regions)</li>
<li>6 (provinces)</li>
<li>8 (municipalities)</li>
</ul>
<p>These borders would be read into a Java application to draw a heatmap, displaying a certain value for each municipality. Therefore it would be nice to get these borders in a format that I can read in Java (like some sort of XML), in the form of an ordered list of points (with lat/lng coordinates) that form a polygon.</p>
<p>After browsing the OSM wiki and really breaking my head over this matter, I figured I should download a (part of a) planet file, and extract the data that I need using osmosis. So currently I have a part of a planet file (planet-benelux-120926.osm.gz) and osmosis, and this is where I'm stuck.</p>
<p>I hope someone can help me out.</p>
<p>Thanks in advance,</p>
<p>Vincent</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-administrative" rel="tag" title="see questions tagged &#39;administrative&#39;">administrative</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Sep '12, 03:14</strong></p>
<img src="https://secure.gravatar.com/avatar/4ac40f72d2b4ff11d512a39f364921cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20Baeten&#39;s gravatar image" />
<p><span>Vincent Baeten</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent Baeten has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16471" class="comments-container">
&#10;</div>
<div id="comment-tools-16471" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16471-form-container" class="comment-form-container">
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

<span id="16472"></span>

<div id="answer-container-16472" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16472-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a number of things you can do. One is doing it with Osmosis or osmfilter (if you can read a little German or use an auto-translator, see <a href="http://forum.openstreetmap.org/viewtopic.php?id=12582">this forum thread</a>). This will however only extract the ways and relations and you will still need some processing afterwards. (Simply speaking, you'll end up with a file that says "the boundary of province X is made up of parts A, B, and C ... the part B consists of points G, H, and J... the point J has the coordinate lat/lon".)</p>
<p>If you have Linux machine and are not afraid to use it, then you could also take the osm2pgsql (or imposm) utility and import your Benelux file into a PostGIS datbase. This has the advantage that you'll then have the boundaries assembled for you (you can then do something along the lines of "select name,geometry from some_table where admin_level=6"). You can easily request the geometry as a sequence of coordinates, or even export it to KML or some other format easily readable in your Java application.</p>
<p>There's also a rather new piece of software specially geared towards creating a set of admin shape files, here: <a href="https://github.com/bussed/osmgadm">https://github.com/bussed/osmgadm.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '12, 07:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Oct '12, 07:46</strong> </span></p>
</div>
</div>
<div id="comments-container-16472" class="comments-container">
&#10;</div>
<div id="comment-tools-16472" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16472-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20922"></span>

<div id="answer-container-20922" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20922-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's extremely easy to do with the <a href="http://josm.openstreetmap.de">JOSM</a> editor.<br />
Focus on any part of the Belgian boundary and File&gt;download the map around it.<br />
You've go the Belgian relation. Select it (right-click&gt;Select relation)<br />
Create a File&gt;New layer and Edit&gt;Merge selection into it.<br />
Then successively select boundaries[X] (of lower level X) and right-click&gt;Download incomplete members.<br />
You've got boundaries down to level X.<br />
<br />
As it still needs installing JOSM and some expertise, I have done that for you.<br />
<a href="http://www.papou.byethost9.com/maps/Belgium/Belgium.html">You will find the files here.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '13, 20:33</strong></p>
<img src="https://secure.gravatar.com/avatar/22d0547d929d81aa90014a6f0aef484a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GentilPapou&#39;s gravatar image" />
<p><span>GentilPapou</span><br />
<span class="score" title="160 reputation points">160</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GentilPapou has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '13, 20:40</strong> </span></p>
</div>
</div>
<div id="comments-container-20922" class="comments-container">
&#10;</div>
<div id="comment-tools-20922" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20922-form-container" class="comment-form-container">
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

