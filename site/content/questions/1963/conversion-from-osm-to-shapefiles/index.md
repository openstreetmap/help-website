+++
type = "question"
title = "Conversion from osm to shapefiles"
description = '''I need to convert the &quot;osm data&quot; into &quot;shape files&quot; to work in our application for routing purpose. I have found my servers having shape files data available for download, and there are also converter available for converting osm data into shape files. My question is that for routing algorithms on s...'''
date = "2010-12-31T11:19:00Z"
lastmod = "2014-09-19T01:22:00Z"
weight = 1963
keywords = [ "shapefile" ]
aliases = [ "/questions/1963" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Conversion from osm to shapefiles](/questions/1963/conversion-from-osm-to-shapefiles)

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
<span id="post-1963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1963-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to convert the "osm data" into "shape files" to work in our application for routing purpose. I have found my servers having shape files data available for download, and there are also converter available for converting osm data into shape files. My question is that for routing algorithms on shape files to work, it is important that a road should be divided into multiple parts/roads at point of intersection, if any road is intersecting it. but this important aspect is ignored in the converters or converted shape files I have seen so far. Can some one please explain that is there any converter available for converting osm data into shape files that are suitable for routing?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Dec '10, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/e29b1c81193839acdd57ae7721619a60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Asif%20Mushtaq&#39;s gravatar image" />
<p><span>Asif Mushtaq</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Asif Mushtaq has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1963" class="comments-container">
<span id="27432"></span>
<div id="comment-27432" class="comment">
<div id="post-27432-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello, I am facing the same problem. Have you found a solution? Thanks.</p>
</div>
<div id="comment-27432-info" class="comment-info">
<span class="comment-age">(23 Oct '13, 07:28)</span> <span class="comment-user userinfo">hua zhang</span>
</div>
</div>
<span id="27450"></span>
<div id="comment-27450" class="comment">
<div id="post-27450-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>maybe you can do a search or ask once more at <a href="http://gis.stackexchange.com">http://gis.stackexchange.com</a> about this specual question.</p>
</div>
<div id="comment-27450-info" class="comment-info">
<span class="comment-age">(23 Oct '13, 18:42)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-1963" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1963-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="1967"></span>

<div id="answer-container-1967" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1967-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-1967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no such converter but it would not be too difficult to enhance any of the existing converters to do this - you would have to find out which nodes are used by more than one road in a first pass, and then in a second pass split the ways accordingly when writing shape files.</p>
<p>However, those "routable shapefiles" are a work-around anyway because the shapefile format does not support topology. You would probably get better results if you managed to import OSM data directly into your application, rather than using shape files.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Dec '10, 17:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-1967" class="comments-container">
&#10;</div>
<div id="comment-tools-1967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1967-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1986"></span>

<div id="answer-container-1986" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1986-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have you tried spatialite for this purpose? spatialite has a separate tool to import the osm data into it which then can be exported to shapefile. the document <a href="http://www.gaia-gis.it/spatialite-2.4.0/Using-Routing.pdf">here</a> describes the whole procedure of it.</p>
<p>cheers</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '11, 05:26</strong></p>
<img src="https://secure.gravatar.com/avatar/6722869e8cdec69a5cc8b38e401a9481?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hamad&#39;s gravatar image" />
<p><span>Hamad</span><br />
<span class="score" title="-2 reputation points">-2</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hamad has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jan '11, 05:31</strong> </span></p>
</div>
</div>
<div id="comments-container-1986" class="comments-container">
&#10;</div>
<div id="comment-tools-1986" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1986-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36921"></span>

<div id="answer-container-36921" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36921-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Si il EST possible de Convertir un fichier .osm en .shp en utilisant ogr2ogr. Ecrivez-moi un mail de rappel à petit bathie18@hotmail.com. Je mettrai la procédure en ligne.</p>
<p>Bon courage!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '14, 01:22</strong></p>
<img src="https://secure.gravatar.com/avatar/1011522df6087c422a760e2101d9169f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bnsig&#39;s gravatar image" />
<p><span>bnsig</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bnsig has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36921" class="comments-container">
&#10;</div>
<div id="comment-tools-36921" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36921-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29563"></span>

<div id="answer-container-29563" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29563-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-29563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think is better to save the map as .mp file then export it to shape file</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '14, 10:56</strong></p>
<img src="https://secure.gravatar.com/avatar/c3e9ceed9ff7dd9f319a64b1f70d1606?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tanask&#39;s gravatar image" />
<p><span>tanask</span><br />
<span class="score" title="25 reputation points">25</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tanask has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29563" class="comments-container">
&#10;</div>
<div id="comment-tools-29563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29563-form-container" class="comment-form-container">
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

