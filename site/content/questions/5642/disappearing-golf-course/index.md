+++
type = "question"
title = "Disappearing golf course"
description = '''Hi. I&#x27;m quite new to the OpenStreeMap community, and I&#x27;m still learning my way around potlatch. I recently added a golf course to the map. Initially, every detail that I had mapped out eventually rendered and showed up in mapnik. Later, I learned about multipolygons, and I linked every bit of the go...'''
date = "2011-06-09T06:47:00Z"
lastmod = "2012-11-30T15:32:00Z"
weight = 5642
keywords = [ "rendering", "golf", "multipolygon" ]
aliases = [ "/questions/5642" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Disappearing golf course](/questions/5642/disappearing-golf-course)

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
<span id="post-5642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5642-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. I'm quite new to the OpenStreeMap community, and I'm still learning my way around potlatch. I recently added a <a href="https://www.openstreetmap.org/?lat=32.2111&amp;lon=-111.04319&amp;zoom=16&amp;layers=M">golf course</a> to the map. Initially, every detail that I had mapped out eventually rendered and showed up in mapnik. Later, I learned about multipolygons, and I linked every bit of the golf course to eachother using a relation. I think I was successful at doing this, but had the unexpected result of having the name of the golf course printed on every little bit of grass that I had mapped. This looked pretty bad on the map, so I removed the relation that I had created on every polygon. Now, only a portion of the golf course is rendered in mapnik, and I'm not sure why. I've waited a couple days to see if it gets redrawn, but every time I check, there's less and less of the course remaining. Anybody have any suggestions?</p>
<p>(Side question -- When defining multiploygon relationships, is there a way to set up the relationship so that the name of the feature is only displayed over one of the polygons?)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-golf" rel="tag" title="see questions tagged &#39;golf&#39;">golf</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jun '11, 06:47</strong></p>
<img src="https://secure.gravatar.com/avatar/e598af26f33a523499e440f70901ed91?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="namannik&#39;s gravatar image" />
<p><span>namannik</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="namannik has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jun '11, 22:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span></p>
</div>
</div>
<div id="comments-container-5642" class="comments-container">
&#10;</div>
<div id="comment-tools-5642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5642-form-container" class="comment-form-container">
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

<span id="5643"></span>

<div id="answer-container-5643" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5643-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-5643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you've been confusing a few different concepts, but without a link to the area that you are discussing it's hard to investigate.</p>
<p>Relations are used for many different things. Their use as multipolygons is for the situation where a given feature's geometry can't be described with just one line (way). So a forest with a hole in it would be described using two ways - one inner, one outer - joined by a multipolygon relation. But a fairway and a clubhouse are two separate things, and so wouldn't be part of the same multipolygon.</p>
<p>You may have also fallen into the trap of trying to "link" together all the different parts of a course just for the sake of indicating they are part of the same course. This is unnecessary - all the features have coordinates, and so it is easy to detect, for example, which bunkers belong to which course by detecting which lie within the perimeter of the course. You can add all the individual features, and a perimeter of the course and name that feature and that's it.</p>
<p>Finally, your issues with rendering are impossible to diagnose without further details. Sometimes the rendering is delayed, and you can find similar questions on this topic.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '11, 09:19</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-5643" class="comments-container">
<span id="5644"></span>
<div id="comment-5644" class="comment">
<div id="post-5644-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A quick search through namannik's edit history suggests this way is one of a number that aren't rendering - <a href="https://www.openstreetmap.org/browse/way/116540821">https://www.openstreetmap.org/browse/way/116540821</a> - I have tried flagging various tiles as dirty after checking status before and after to check they have rerendered, but that hasn't seemed to help.</p>
</div>
<div id="comment-5644-info" class="comment-info">
<span class="comment-age">(09 Jun '11, 09:37)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-5643" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5643-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5650"></span>

<div id="answer-container-5650" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5650-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In mapping this golf course you have mapped the more prominent features: fairways, greens etc, but not the main outline of the golf course which would include not just rough but trees and other plantings up to the boundaries of the residential properties which back onto the golf course. This has meant that you have a very large number of ways which belong to the golf course (and hence the relation issue), when many of these are best mapped with the widely used golf tags: <code>golf=bunker</code>, <code>golf=green</code>, <code>golf=fairway</code>, <code>golf=tee</code> and <code>golf=hole</code>. So I would recommend using a more inclusive boundary for the golf course as a whole, and using the golf-specific tags for obvious features visible in the aerial imagery.</p>
<p>There are some detailed discussions <a href="http://forum.openstreetmap.org/viewtopic.php?id=11715">about mapping</a> the 'country club' type layout with a golf course in the middle on the OSM Forum.</p>
<p>Also check Richard Weait's blog about <a href="http://weait.com/content/golf-course-style-openstreetmap">golf course mapping</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '11, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-5650" class="comments-container">
<span id="5651"></span>
<div id="comment-5651" class="comment">
<div id="post-5651-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks to both of you for the tips. I'll definitely check out the info about mapping out golf courses.</p>
<p>I had meant to include a link to the golf course in my original post, but it slipped my mind. Here it is:</p>
<p><a href="https://www.openstreetmap.org/?lat=32.2111&amp;lon=-111.04319&amp;zoom=16&amp;layers=M">https://www.openstreetmap.org/?lat=32.2111&amp;lon=-111.04319&amp;zoom=16&amp;layers=M</a></p>
</div>
<div id="comment-5651-info" class="comment-info">
<span class="comment-age">(09 Jun '11, 17:37)</span> <span class="comment-user userinfo">namannik</span>
</div>
</div>
<span id="18114"></span>
<div id="comment-18114" class="comment">
<div id="post-18114-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By the way, as of now December 2012, Richard Weait's blog website - at <a href="http://weait.com">http://weait.com</a> - seems to be no longer active...</p>
<p>PS A presentation from him about OSM : <a href="http://fr.slideshare.net/rweait/">http://fr.slideshare.net/rweait/</a> and a video with him : <a href="http://www.youtube.com/watch?v=tWCGkAZtnME">http://www.youtube.com/watch?v=tWCGkAZtnME</a></p>
</div>
<div id="comment-18114-info" class="comment-info">
<span class="comment-age">(30 Nov '12, 11:32)</span> <span class="comment-user userinfo">Pascal Boule...</span>
</div>
</div>
<span id="18124"></span>
<div id="comment-18124" class="comment">
<div id="post-18124-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>One additional thing: there is a golf course-specific rendering on ItoMap, which is a good check on whether your tagging is correct (and I like the GC rendering more than the default Mapnik): <a href="http://www.itoworld.com/map/47">http://www.itoworld.com/map/47</a></p>
</div>
<div id="comment-18124-info" class="comment-info">
<span class="comment-age">(30 Nov '12, 15:32)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-5650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5650-form-container" class="comment-form-container">
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

