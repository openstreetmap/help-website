+++
type = "question"
title = "Calculating the distance (length) of an OSM Way"
description = '''The title pretty much says it all. Is there an accurate method to calculate the distance of an OSM way?'''
date = "2013-02-10T19:45:00Z"
lastmod = "2013-02-11T12:29:00Z"
weight = 19799
keywords = [ "ways", "distance", "osm", "longitude", "latitude" ]
aliases = [ "/questions/19799" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Calculating the distance (length) of an OSM Way](/questions/19799/calculating-the-distance-length-of-an-osm-way)

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
<span id="post-19799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19799-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The title pretty much says it all. Is there an accurate method to calculate the distance of an OSM way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '13, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/361e0b98020ca3f3d7db7baa2ec6c590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sadeer&#39;s gravatar image" />
<p><span>Sadeer</span><br />
<span class="score" title="176 reputation points">176</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sadeer has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Feb '13, 19:55</strong> </span></p>
</div>
</div>
<div id="comments-container-19799" class="comments-container">
<span id="19800"></span>
<div id="comment-19800" class="comment">
<div id="post-19800-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please add some details like what accuracy do you need. What is your source data? Is it a way id, an osm file or do you have these ways in a database?</p>
<p>Also knowing what you need to do, would help to write a good answer (otherwise you might get a perfectly good formula for calculating the length with pencil and paper).</p>
</div>
<div id="comment-19800-info" class="comment-info">
<span class="comment-age">(10 Feb '13, 20:12)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="19801"></span>
<div id="comment-19801" class="comment">
<div id="post-19801-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'm given an OSM XML file and would like to calculate the distances of the ways in the XML file. It's needed for my academic project which is to implement a routing engine.</p>
</div>
<div id="comment-19801-info" class="comment-info">
<span class="comment-age">(10 Feb '13, 20:24)</span> <span class="comment-user userinfo">Sadeer</span>
</div>
</div>
</div>
<div id="comment-tools-19799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19799-form-container" class="comment-form-container">
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

<span id="19820"></span>

<div id="answer-container-19820" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19820-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For any consecutive points P1(lat1,lon1), P2(lat2,lon2) in a "way" calculate the corresponding P1(x1,y1,z1), P2(v2,y2,z2) and so calculate the cetral angle "alpha" in the corresponding main circle (use the scalar or vector product of the 2 position vectors). The diatnce is then dist=alpha*R (R, the major semi-axis of the WGS'84 sphere). You can find many related articles by searching, for example using "latitude longitude distance" key-words, like the following one <a href="http://www.movable-type.co.uk/scripts/latlong.html">http://www.movable-type.co.uk/scripts/latlong.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '13, 12:01</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-19820" class="comments-container">
&#10;</div>
<div id="comment-tools-19820" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19820-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19822"></span>

<div id="answer-container-19822" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19822-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Everything about routing or similar aims based on OSM data is collected in the OSM wiki about <a href="http://wiki.openstreetmap.org/wiki/Routing">Routing</a>.</p>
<p>Search for opensource solutions to implement something in your project.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '13, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-19822" class="comments-container">
&#10;</div>
<div id="comment-tools-19822" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19822-form-container" class="comment-form-container">
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

