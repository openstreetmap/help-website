+++
type = "question"
title = "Finding and merging parallel ways that are part of the same street in OSM file"
description = '''I am using OSM data for a programming task I&#x27;m working on, and one thing I&#x27;ve noticed is that often, major streets that have a barrier or divider in the middle are represented as two separate, parallel ways - one way for each direction. This behavior is not desirable for the particular program I&#x27;m w...'''
date = "2015-06-19T21:19:00Z"
lastmod = "2015-06-30T11:53:00Z"
weight = 43654
keywords = [ "programing", "geojson" ]
aliases = [ "/questions/43654" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Finding and merging parallel ways that are part of the same street in OSM file](/questions/43654/finding-and-merging-parallel-ways-that-are-part-of-the-same-street-in-osm-file)

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
<span id="post-43654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43654-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using OSM data for a programming task I'm working on, and one thing I've noticed is that often, major streets that have a barrier or divider in the middle are represented as two separate, parallel ways - one way for each direction. This behavior is not desirable for the particular program I'm writing, so I want parallel ways to be merged into a single way running down the center of the street. It seems like a fairly simple problem, but I'm having a trouble getting the program to identify ways that need to be merged and then merge them properly.</p>
<p>Right now, the program looks for ways that need to be merged by looking at pairs of ways, using the first and last node of each way to figure out the angle at which it is oriented. If the ways are oriented at a similar angle and are close enough that small rectangles drawn around them would overlap, then the program will try to merge the two ways.</p>
<p>Unfortunately this technique doesn't work as well as I'd like it to in practice - it's pretty inefficient (as it would need to compare lots of pairs in a large map) and there are many edge cases in which it fails, like when one side consists of a single long way and the other side consists of multiple short ways.</p>
<p>Is there an easier way to accomplish this? Perhaps with an existing tool, or something obvious I haven't thought of?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-programing" rel="tag" title="see questions tagged &#39;programing&#39;">programing</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '15, 21:19</strong></p>
<img src="https://secure.gravatar.com/avatar/1884f079651ae2f214e9795ba46947a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tongning&#39;s gravatar image" />
<p><span>tongning</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tongning has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '15, 21:22</strong> </span></p>
</div>
</div>
<div id="comments-container-43654" class="comments-container">
<span id="43655"></span>
<div id="comment-43655" class="comment">
<div id="post-43655-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd be interested in hearing about what you are doing where merging those ways would be advantageous.</p>
<p>In OSM those parallel ways will generally be marked with a oneway tag, perhaps that can help identify the ways of interest.</p>
</div>
<div id="comment-43655-info" class="comment-info">
<span class="comment-age">(19 Jun '15, 21:40)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="43657"></span>
<div id="comment-43657" class="comment">
<div id="post-43657-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting suggestion, thanks! As for the program, it tries to predict where sidewalks and crosswalks should be located, as part of a project to improve accessibility. It's written in Python and generates geojson output showing predicted crosswalk and sidewalk locations when fed an OSM file as input. It should be putting sidewalks on each side of a street, of course, but when there are two parallel ways it tries to put four sidewalks rather than two.</p>
</div>
<div id="comment-43657-info" class="comment-info">
<span class="comment-age">(19 Jun '15, 22:30)</span> <span class="comment-user userinfo">tongning</span>
</div>
</div>
<span id="43668"></span>
<div id="comment-43668" class="comment">
<div id="post-43668-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Tags should be a good option, no? I've just checked such a double-way next to my place and realized that it was also tagged &lt; lane=2 &gt;. A combination of tags could help reduce the number of ways to compare... But you certainly have looked at tags carefully yet.</p>
</div>
<div id="comment-43668-info" class="comment-info">
<span class="comment-age">(20 Jun '15, 21:04)</span> <span class="comment-user userinfo">wiltomap</span>
</div>
</div>
</div>
<div id="comment-tools-43654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43654-form-container" class="comment-form-container">
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

<span id="43688"></span>

<div id="answer-container-43688" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43688-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tongning has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>major streets that have a barrier or divider in the middle are represented as two separate, parallel ways - one way for each direction</p>
</blockquote>
<p>Yep this is intentional. The idea being that if you could <em>physically</em> (as opposed to legally) do a U-turn in a road, then you should map it as one OSM way, if you cannot (due to walls/barriers) then it should be 2 separate ways in OSM, with appropriate one way tags. This also makes much more sense for motorways, which will have complicated junctions which only merge into one "lane".</p>
<p>To solve your problem, I can give some hints: Many of these "split roads" will have <code>oneway</code> tags, they will have the same road classification (i.e. the <code>highway</code> tag), they will almost certainly have the same <code>ref</code> tag (e.g. <code>ref=A8</code>). They <em>may</em> have the same <code>name</code> tag. Perhaps this could help find candidate roads. It's also much less common the further down the road hierachy you go. <a href="http://taginfo.openstreetmap.org/tags/highway=motorway#combinations">97.5% of <code>highway=motorway</code> are <code>oneway=yes</code></a>, whereas only <a href="http://taginfo.openstreetmap.org/tags/highway=trunk#combinations">54% of <code>highway=trunk</code> are <code>oneway=yes</code></a>.</p>
<p>For example, <a href="https://www.openstreetmap.org/way/78025193#map=15/48.6335/2.1532">this road</a> and <a href="https://www.openstreetmap.org/way/131297913#map=15/48.6335/2.1422">this road</a> are one "split road". You'll notice they both are mapped <code>oneway=yes</code>, <code>highway=motorway</code>, <code>ref=A 10</code>, and both have the same <code>name</code> (<code>L'Aquitaine</code>).</p>
<blockquote>
<p>As for the program, it tries to predict where sidewalks and crosswalks should be located, as part of a project to improve accessibility. ... It should be putting sidewalks on each side of a street, of course, but when there are two parallel ways it tries to put four sidewalks rather than two.</p>
</blockquote>
<p>Perhaps, rather than trying to merge the 2 OSM ways, you could just use the approach I gave to detect "probably split roads", and then only add the sidewalk in one direction? i.e. the direction of the road itself?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '15, 09:04</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-43688" class="comments-container">
&#10;</div>
<div id="comment-tools-43688" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43688-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43660"></span>

<div id="answer-container-43660" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43660-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect that first merging ways that have been split along the length of the road would help a bit, naturally there is no guaranteee that the geometry of say a footway actually is parallel to the real road surface.</p>
<p>ASCII art of such a situation:</p>
<pre><code>                F
                F
FFFFFFFFFFFFFFFFXfffffffffffffffff
                f
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR</code></pre>
<p>F=footway 1 f=footway 2 R=Road</p>
<p>F and f woudn't be mergeable without splitting at X.</p>
<p>PS: in an answer becase markdown doesn't work in comments.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '15, 07:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-43660" class="comments-container">
&#10;</div>
<div id="comment-tools-43660" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43660-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43864"></span>

<div id="answer-container-43864" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43864-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question/issue is just a trivial case of the problem what we inevitably meet in vector map-making. Namely, in a road class, road sections are often presented by two "parallel" poly-line segments, one per direction. More precisely, the distance between the two "parallel" poly-line segments is never larger than a critical (parameter) distance "d". For illustration assume the primary road class and d=10m. In the data preparation, when creating the vector scale-levels, when the scale factor is less than 1:20000 the distance will vary between 0 and 2 pixels on a 120dpi rendering display. This has a bad aesthetic consequence end data redundancy in transmission and client rendering. Therefore, in the data preparation we try to detect and eliminate the parallel cases (the phase/step just before the vector smoothing).<br />
You have already got some suggestions how you can cope with the "parallel" issue. Here is one geometry/topology based option. Assume, for the mentioned illustration, we have two ways/poly-lines AC where B is an inner point and MP where N is an inner point. Assume that the distance d(B,M) and d(C,N) both are less than d. In an early version we have used a surface criterion for checking the parallel property between the BC and MN polylines. So, if the surface enclosed by the polygon BCNMB was less than the surface length(BC)*d, then we replaced the BC and MN poly-lines with only one keeping the proper connectivity. Occasionally this criterion was not enough strong and in the current version a corridor model is used. Assume that AC is longer than MP and a circular pen with radius d. Now, if you move this pen along the AC ply-line (as the skeleton) the contour of the thick line (in a vector format) is the border of an area we call for corridor. Now, if an edge vector of MN is inside the corridor of BC this is to be ignored/deleted from MN. The rest poly-lie(s) of MN and the NP poly-line with proper connections to AC create the new road segment.<br />
Of course, there are many, many fine details missing. But note that the same model might be used for bulk upload of a road class (or other line-work data types). E.g. a government suddenly makes public a road class in a country. The local OSM community would like to upload this more accurate road data by eliminating "parallel" cases from the older manual uploads.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '15, 11:53</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-43864" class="comments-container">
&#10;</div>
<div id="comment-tools-43864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43864-form-container" class="comment-form-container">
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

