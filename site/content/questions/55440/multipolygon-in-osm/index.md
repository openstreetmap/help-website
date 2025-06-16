+++
type = "question"
title = "Multipolygon in OSM"
description = '''Hi, I&#x27;m developing a Java program to work with OSM data. I&#x27;m having big troubles to handle multipolygons due to the fact that the ways that make them up are not ordered and often the roles (outer / inner) are incorrect, so I&#x27;m looking for a way to build multipolygons that is not based on roles. I sh...'''
date = "2017-04-02T14:15:00Z"
lastmod = "2017-04-05T06:54:00Z"
weight = 55440
keywords = [ "openstreetmap", "overpass", "multipolygon" ]
aliases = [ "/questions/55440" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Multipolygon in OSM](/questions/55440/multipolygon-in-osm)

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
<span id="post-55440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55440-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm developing a Java program to work with OSM data. I'm having big troubles to handle multipolygons due to the fact that the ways that make them up are not ordered and often the roles (outer / inner) are incorrect, so I'm looking for a way to build multipolygons that is not based on roles. I should be able, given all the roads, to rebuild the individual polygons that make up the multipolygon, but how do I know which of these polygons are contained in the other? I'm going crazy, any help is more than appreciated. Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Apr '17, 14:15</strong></p>
<img src="https://secure.gravatar.com/avatar/3561366bd49459f5b003a79c5dbee78c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CillaLu&#39;s gravatar image" />
<p><span>CillaLu</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CillaLu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55440" class="comments-container">
<span id="55441"></span>
<div id="comment-55441" class="comment">
<div id="post-55441-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"and often the roles (outer / inner) are incorrect" Can you show examples of multipolygons with incorrect roles? Almost always roles should be correct. Maybe you are misinterpreting something?</p>
</div>
<div id="comment-55441-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 14:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="55442"></span>
<div id="comment-55442" class="comment">
<div id="post-55442-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't understand "given all the roads" - maybe it's a typing error?</p>
</div>
<div id="comment-55442-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 14:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="55447"></span>
<div id="comment-55447" class="comment">
<div id="post-55447-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not saying that I found errors in the roles but I read that it is possible and I won't take the risk. But let's assume that the roles are correct, looking at this example: &lt;relation id="1"&gt; &lt;tag k="type" v="multipolygon"/&gt; &lt;member type="way" id="1" role="outer"/&gt; &lt;member type="way" id="2" role="inner"/&gt; &lt;member type="way" id="3" role="outer"/&gt; &lt;/relation&gt; Now I ordered them correctly, but the order is not always guaranteed. Assuming the members are not ordered, how do I build the multipolygon?</p>
</div>
<div id="comment-55447-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 15:04)</span> <span class="comment-user userinfo">CillaLu</span>
</div>
</div>
<span id="55448"></span>
<div id="comment-55448" class="comment">
<div id="post-55448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I meant "given all the ways" instead of "given all the roads". With ways i mean multipolygon relation's members.</p>
</div>
<div id="comment-55448-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 15:08)</span> <span class="comment-user userinfo">CillaLu</span>
</div>
</div>
</div>
<div id="comment-tools-55440" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55440-form-container" class="comment-form-container">
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

<span id="55455"></span>

<div id="answer-container-55455" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55455-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-55455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use this algorithm described in our Wiki: <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon/Algorithm">https://wiki.openstreetmap.org/wiki/Relation:multipolygon/Algorithm</a> - it works without looking at the roles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '17, 19:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-55455" class="comments-container">
<span id="55479"></span>
<div id="comment-55479" class="comment">
<div id="post-55479-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Frederik, there is though one problem with this (similar) algorithm. If for any reasons a polygonal line (essentially meant to present an outer border section) should be dropped, then the whole multipolygon must be dropped. Otherwise, the polygons (essentially meant to be holes in the ignored outer polygon) will be inverted and will overwrite everything beneath them. With the rules we still may detect which multipolygon elemts are to be ignored and keep many others.</p>
</div>
<div id="comment-55479-info" class="comment-info">
<span class="comment-age">(05 Apr '17, 06:54)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
</div>
<div id="comment-tools-55455" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55455-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55446"></span>

<div id="answer-container-55446" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55446-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I really think you should not be re-inventing the wheel. There are plenty of open source projects and code bases, also for Java, that can handle reading OSM data. Admittedly, the number of programs that properly handle multipolygons, is less, but nonetheless, there are several well maintained ones out there:</p>
<ol>
<li><a href="https://wiki.openstreetmap.org/wiki/Osmosis">https://wiki.openstreetmap.org/wiki/Osmosis</a></li>
<li><a href="https://github.com/osmcode/libosmium">https://github.com/osmcode/libosmium</a></li>
<li><a href="https://github.com/osmcode/pyosmium">https://github.com/osmcode/pyosmium</a></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '17, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Apr '17, 15:01</strong> </span></p>
</div>
</div>
<div id="comments-container-55446" class="comments-container">
<span id="55452"></span>
<div id="comment-55452" class="comment">
<div id="post-55452-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the links. The fact is that I'm doing a thesis on OSM and my thesis advisor asked me to write a java tool to do things with OSM data, so I can not just use other libraries. But nothing prevents me to try to figure out how those libraries manage multipolygons.</p>
</div>
<div id="comment-55452-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 16:14)</span> <span class="comment-user userinfo">CillaLu</span>
</div>
</div>
<span id="55456"></span>
<div id="comment-55456" class="comment">
<div id="post-55456-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I did the implementation in libosmium and it cost me several months of my life. Unless your thesis is about the intricacies of the OSM data model, I wouldn't recommend to do this yourself...</p>
</div>
<div id="comment-55456-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 20:38)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-55446" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55446-form-container" class="comment-form-container">
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

