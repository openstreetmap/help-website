+++
type = "question"
title = "Overpass API: Length of a way"
description = '''Hey, Is it possible to factor in the length of a way in Overpass API query? For example querying for ways that are highway=service and that are longer than 100m. Thanks in advance!'''
date = "2014-08-10T08:09:00Z"
lastmod = "2021-09-25T11:15:00Z"
weight = 35676
keywords = [ "overpass", "overpass-turbo", "query" ]
aliases = [ "/questions/35676" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API: Length of a way](/questions/35676/overpass-api-length-of-a-way)

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
<span id="post-35676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35676-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey,</p>
<p>Is it possible to factor in the length of a way in Overpass API query? For example querying for ways that are highway=service and that are longer than 100m.</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Aug '14, 08:09</strong></p>
<img src="https://secure.gravatar.com/avatar/7ec5c174de466f97a699757f71dc398b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kerosin&#39;s gravatar image" />
<p><span>kerosin</span><br />
<span class="score" title="411 reputation points">411</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kerosin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35676" class="comments-container">
<span id="35691"></span>
<div id="comment-35691" class="comment">
<div id="post-35691-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How do you define a <em>way</em>? An <a href="https://wiki.openstreetmap.org/wiki/Way">OSM way</a> where a single street can consist of many individual ways? A part of a street up to the next intersection? A whole street consisting of multiple OSM ways all having the same name? Something else?</p>
</div>
<div id="comment-35691-info" class="comment-info">
<span class="comment-age">(11 Aug '14, 08:40)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="35692"></span>
<div id="comment-35692" class="comment">
<div id="post-35692-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I was talking about OSM ways - not streets. So a way is a set of nodes that are connected and that (in my case) don't form an area. A street can exist of one or more way(s). So basically I meant ways as there're defined for overpass queries (just without areas).</p>
</div>
<div id="comment-35692-info" class="comment-info">
<span class="comment-age">(11 Aug '14, 08:54)</span> <span class="comment-user userinfo">kerosin</span>
</div>
</div>
</div>
<div id="comment-tools-35676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35676-form-container" class="comment-form-container">
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

<span id="35677"></span>

<div id="answer-container-35677" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35677-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-35677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kerosin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unfortunately, it's not possible to specify the length of a way as filter criterion in Overpass API. You need to resort to some kind of post-processing, e.g. using PostGIS or something similar.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '14, 08:35</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-35677" class="comments-container">
&#10;</div>
<div id="comment-tools-35677" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35677-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35712"></span>

<div id="answer-container-35712" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35712-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at the former question:</p>
<p><a href="https://help.openstreetmap.org/questions/469/where-can-i-see-the-length-of-a-certain-way-element-in-the-osm-data">where-can-i-see-the-length-of-a-certain-way-element-in-the-osm-data</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '14, 18:12</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-35712" class="comments-container">
&#10;</div>
<div id="comment-tools-35712" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35712-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71697"></span>

<div id="answer-container-71697" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71697-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Length">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Length</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '19, 12:04</strong></p>
<img src="https://secure.gravatar.com/avatar/47edd1ee4d973c50bbe7991bb063d09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jidanni&#39;s gravatar image" />
<p><span>jidanni</span><br />
<span class="score" title="339 reputation points">339</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jidanni has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71697" class="comments-container">
&#10;</div>
<div id="comment-tools-71697" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71697-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81948"></span>

<div id="answer-container-81948" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81948-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can add length data to the output of an overpass query, see <a href="https://github.com/drolbr/Overpass-API/issues/237#issuecomment-303974281">https://github.com/drolbr/Overpass-API/issues/237#issuecomment-303974281</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '21, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/ea3ff1b44d6b6c958e1b5283ba7a1132?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tordans&#39;s gravatar image" />
<p><span>tordans</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tordans has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81948" class="comments-container">
&#10;</div>
<div id="comment-tools-81948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81948-form-container" class="comment-form-container">
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

