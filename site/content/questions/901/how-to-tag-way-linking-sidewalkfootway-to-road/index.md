+++
type = "question"
title = "How to tag way linking sidewalk/footway to road?"
description = '''I&#x27;m editing a residential area in the US that has many sidewalks (tagged as highway=footway) with curb cuts (sloped curbs) allowing access to the road. In a number of locations these curb cuts come in pairs, and what I do to link them is create a way tagged highway=crossing between them. I use 5 nod...'''
date = "2010-09-22T12:39:00Z"
lastmod = "2021-06-18T12:45:00Z"
weight = 901
keywords = [ "tagging", "footway" ]
aliases = [ "/questions/901" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag way linking sidewalk/footway to road?](/questions/901/how-to-tag-way-linking-sidewalkfootway-to-road)

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
<span id="post-901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-901-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm editing a residential area in the US that has many sidewalks (tagged as <code>highway=footway</code>) with curb cuts (sloped curbs) allowing access to the road. In a number of locations these curb cuts come in pairs, and what I do to link them is create a way tagged <code>highway=crossing</code> between them. I use 5 nodes, two nodes in common with the footway/sidewalk, one node in common with the road, and one node on each of the curb cuts (which are tagged <code>sloped_curb=yes</code>).</p>
<p><strong>My question is what to do if I don't have a pair of curb cuts</strong>, but simply access to the road itself (near parking). Tagging the way as <code>highway=crossing</code> doesn't seem appropriate, but neither does <code>highway=footway</code>. I will do three nodes for the ways, one in common each with the road and the footway, and one for the curb cut.</p>
<p><strong>A related question is what to do when I have multiple curb cuts near each other</strong>. Crossings between each of them doesn't make sense to me, since it's a residential road people can cross between any of them, including diagonally. Should I just connect to a common node on the road?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-footway" rel="tag" title="see questions tagged &#39;footway&#39;">footway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '10, 12:39</strong></p>
<img src="https://secure.gravatar.com/avatar/214bdf717ba51e515f4072fc1b0c71c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joshdoe&#39;s gravatar image" />
<p><span>joshdoe</span><br />
<span class="score" title="110 reputation points">110</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joshdoe has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Sep '10, 10:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-901" class="comments-container">
<span id="7042"></span>
<div id="comment-7042" class="comment">
<div id="post-7042-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As noted in the selected answer, I shouldn't have tagged the way with <code>highway=crossing</code>.</p>
</div>
<div id="comment-7042-info" class="comment-info">
<span class="comment-age">(11 Aug '11, 17:23)</span> <span class="comment-user userinfo">JoshD</span>
</div>
</div>
<span id="80608"></span>
<div id="comment-80608" class="comment">
<div id="post-80608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For any reading along; apparently, only nodes should be tagged with <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dcrossing">highway=crossing</a>. For micro-mappers, you'd want <a href="https://wiki.openstreetmap.org/wiki/Tag:footway%3Dcrossing">highway=footway + footway=crossing</a>.</p>
</div>
<div id="comment-80608-info" class="comment-info">
<span class="comment-age">(18 Jun '21, 03:06)</span> <span class="comment-user userinfo">Joel D Reid</span>
</div>
</div>
<span id="80610"></span>
<div id="comment-80610" class="comment">
<div id="post-80610-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/6346/joel-d-reid">@Joel D Reid</a> You don't need to comment on ancient questions to make a point. Moreover, to update, in recent months over the past year there were discussions about <code>virtual=yes</code>, and <code>footway=link</code>.</p>
</div>
<div id="comment-80610-info" class="comment-info">
<span class="comment-age">(18 Jun '21, 07:54)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="80621"></span>
<div id="comment-80621" class="comment">
<div id="post-80621-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to tag things correctly. Is the wiki the canonical source for recommended tagging practices? You mentioned tag:virtual, which I cannot find as a proposal nor guideline in the wiki.</p>
</div>
<div id="comment-80621-info" class="comment-info">
<span class="comment-age">(18 Jun '21, 12:43)</span> <span class="comment-user userinfo">Joel D Reid</span>
</div>
</div>
<span id="80622"></span>
<div id="comment-80622" class="comment">
<div id="post-80622-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16887/kovoschiz">@Kovoschiz</a> Please don't assume my intent—I didn't comment to make a point. This question page was the first result in my searching, for example, despite being "ancient". This page is not archived or deleted, so I think it is here to inform people. So, my intent was: if I can help the next reader to jump to the answer, great.</p>
</div>
<div id="comment-80622-info" class="comment-info">
<span class="comment-age">(18 Jun '21, 12:45)</span> <span class="comment-user userinfo">Joel D Reid</span>
</div>
</div>
</div>
<div id="comment-tools-901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-901-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="918"></span>

<div id="answer-container-918" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-918-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joshdoe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This question is not easy to answer since mapping sidewalks, sloped curbs and crossings are called "micro-mapping" and are not extensively surveyed in OSM at the moment. So you are free to innovate or try to contact other people interested by the same level of details by other means like IRC or the OSM mailing lists (see <a href="https://wiki.openstreetmap.org/wiki/Contact">Contact</a> on the wiki) because at the moment, we don't have well established practices about these detailed things.<br />
But "highway=crossing" seems to be designed for the <em>intersection node</em> between the footway and the highway , see the wiki : <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dcrossing"></a><a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dcrossing"></a><a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dcrossing">https://wiki.openstreetmap.org/wiki/Tag:highway%3Dcrossing</a> and <a href="https://wiki.openstreetmap.org/wiki/Crossing"></a><a href="https://wiki.openstreetmap.org/wiki/Crossing"></a><a href="https://wiki.openstreetmap.org/wiki/Crossing">https://wiki.openstreetmap.org/wiki/Crossing</a>. So the way crossing the road should be tagged with <em>highway=footway</em>, like the sidewalks and the crossing tag only on the intersection node itself. Tagging sloped curbs has been proposed on the wiki : <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/sloped_curb"></a><a href="https://wiki.openstreetmap.org/wiki/Proposed_features/sloped_curb"></a><a href="https://wiki.openstreetmap.org/wiki/Proposed_features/sloped_curb">https://wiki.openstreetmap.org/wiki/Proposed_features/sloped_curb</a> and you can follow the discussion there. But your method to set them on two specific nodes seems to be the most accurate.<br />
The question about linking footways and roads outside sloped curbs is a general question about how far we want to symbolize entities in OSM (a polyline for a sidewalk or road where we should draw a polygon) and how far we want to draw ourselves all interconnections, especially for pedestrians which is much more complexe than for cars in order to help routing applications for pedestrians. Such applications for OSM should be able to find a route even when sidewalks are not represented (since the vast majority of them are missing) and even allow road crossing at the best for the shortest way even if crossing's are missing (but better use them if one can be found nearby).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '10, 13:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Sep '10, 09:14</strong> </span></p>
</div>
</div>
<div id="comments-container-918" class="comments-container">
<span id="937"></span>
<div id="comment-937" class="comment">
<div id="post-937-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the great response. I'm glad you caught my error about tagging of the way as a crossing rather than just the node.</p>
<p>For my question, I think I'd say the way should be tagged as <strong>highway=footway</strong>, with no special tag for the node where it intersects with the road.</p>
</div>
<div id="comment-937-info" class="comment-info">
<span class="comment-age">(27 Sep '10, 15:08)</span> <span class="comment-user userinfo">joshdoe</span>
</div>
</div>
</div>
<div id="comment-tools-918" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-918-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7043"></span>

<div id="answer-container-7043" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7043-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's what I do now. I tag such "links" with <code>highway=footway</code> and <code>footway=crossing</code>, which indicates it's not a physical strip of asphalt/concrete dedicated to pedestrians, but it's part of another highway. However, I don't add a <code>highway=crossing</code> node where it intersects the road.</p>
<p>For the second part, if there are dropped kerbs (aka curb cuts) on four corners of an intersection, I essentially draw a box connecting them, so I ignore the possibility of diagonal crossings, as that's typically not allowed or at least it's unusual to do so. Of course there are some cities which have such diagonal crossings, and those should be marked as such in that case. See <a href="https://wiki.openstreetmap.org/wiki/File:Kerb_key_example_map.jpg">this image on the wiki</a> for how I would map this type of situation (though for three kerbs rather than four).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '11, 17:24</strong></p>
<img src="https://secure.gravatar.com/avatar/ba99ad3778972fee07700e1eb36cc822?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoshD&#39;s gravatar image" />
<p><span>JoshD</span><br />
<span class="score" title="300 reputation points">300</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoshD has one accepted answer">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Aug '11, 17:28</strong> </span></p>
</div>
</div>
<div id="comments-container-7043" class="comments-container">
&#10;</div>
<div id="comment-tools-7043" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7043-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7045"></span>

<div id="answer-container-7045" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7045-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-7045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It does not really answer the question but at that level of detail it seem to be appropriate to tag the footway/streeet areas in some way (landuse=street has been suggested)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '11, 19:50</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-7045" class="comments-container">
<span id="7046"></span>
<div id="comment-7046" class="comment">
<div id="post-7046-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The links are necessary for routing, while <code>landuse=street</code> or <code>area:highway=*</code> tags for the area would only be useful for rendering or perhaps some analysis (% of earth covered by asphalt?).</p>
</div>
<div id="comment-7046-info" class="comment-info">
<span class="comment-age">(11 Aug '11, 20:28)</span> <span class="comment-user userinfo">JoshD</span>
</div>
</div>
<span id="7047"></span>
<div id="comment-7047" class="comment">
<div id="post-7047-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, they would be useful for rendering, or analysis. Also they can give you the information where the sidewalk ends and street starts. They give you the information about actual shape of the street (eg. oversized load can go over a sidewalk, but not through a house). You can find more uses. I am only saying that when you survey the area this deep, you can draw it to the map...</p>
</div>
<div id="comment-7047-info" class="comment-info">
<span class="comment-age">(11 Aug '11, 20:39)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
</div>
<div id="comment-tools-7045" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7045-form-container" class="comment-form-container">
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

