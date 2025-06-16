+++
type = "question"
title = "Find overlapping part about line and polygon"
description = '''I&#x27;m try to find Singapore MRT line in a range like below: [out:json][timeout:100];(node(around:1000,1.284249, 103.844004)[&quot;name&quot;~&quot;Downtown Line MRT&quot;];way(around:1000,1.284249, 103.844004)[&quot;name&quot;~&quot;Downtown Line MRT&quot;];);out body;._;&amp;gt;;out skel qt;  (around:1000,1.284249, 103.844004) is a circle poly...'''
date = "2017-06-02T03:37:00Z"
lastmod = "2017-06-14T03:26:00Z"
weight = 56411
keywords = [ "mrt", "line", "polygon", "overpass-ql" ]
aliases = [ "/questions/56411" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Find overlapping part about line and polygon](/questions/56411/find-overlapping-part-about-line-and-polygon)

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
<span id="post-56411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56411-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm try to find Singapore MRT line in a range like below:</p>
<pre><code>[out:json][timeout:100];(node(around:1000,1.284249, 103.844004)[&quot;name&quot;~&quot;Downtown Line MRT&quot;];way(around:1000,1.284249, 103.844004)[&quot;name&quot;~&quot;Downtown Line MRT&quot;];);out body;._;&gt;;out skel qt;</code></pre>
<p>(around:1000,1.284249, 103.844004) is a circle polygon and Downtown Line MRT is a line. How can I get the overlapping part only(red line in picture)? The query result will partially out of circle.</p>
<p><img src="/upfiles/Noname.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mrt" rel="tag" title="see questions tagged &#39;mrt&#39;">mrt</span> <span class="post-tag tag-link-line" rel="tag" title="see questions tagged &#39;line&#39;">line</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '17, 03:37</strong></p>
<img src="https://secure.gravatar.com/avatar/adb24ae063869f3b1c62e61672cf087b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ob9619&#39;s gravatar image" />
<p><span>ob9619</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ob9619 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jun '17, 04:25</strong> </span></p>
</div>
</div>
<div id="comments-container-56411" class="comments-container">
&#10;</div>
<div id="comment-tools-56411" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56411-form-container" class="comment-form-container">
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

<span id="56559"></span>

<div id="answer-container-56559" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56559-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are indicating two issues - for a given poly-line and circle/polygon detect the poly-line's segments being inside the circle/polygon (clipping a poly-line by a circle/polygon). If you have not yet found these functions (answers) in the OSM public tools, here are some hints in bullets. Namely, the mentioned tools (should) have functions like - vectors to none crossing vectors transformation, point in (on, outside) a polygon, vectors to poly-lines transformation, change poly-line's orientation and some more, even simpler, functions and using them you (anyone) may create the missing functions.<br />
The simple/circle case's procedure. 1)From the poly-line edge-vector set detect/select the set {Vi} where any of the vectors Vi has a point inside the circle's bounding box. 2)If the line defined by a vector Vi crosses the circle, let us say in points A and B, select the vector Ej as part of Vi being inside the segment AB. The new set {Ej} contains only vectors being strictly inside the circle. 3)Connect the vectors from {Ej} into poly-line(s) and if necessary change the orientation of these.<br />
The general/polygon case's procedure is the same as the former (when "circle" is replaced by "polygon") except the step 2. Here, the procedure is more complex. The {Ej} set contains all Vi vectors having no common points with the polygon. If a vector Vi is crossing the polygon, let us say in a point X, then Vi should be divided by X into two new Ej vectors. Further, if a Vi is overlapping a polygon edge vector Pk then we replace Vi with its Ej parts being outside the vector Pk. Now, the set {Ej} contains vectors never crossing the polygon. You may prove that a vector Ej from this set {Ej} is strictly inside the polygon if, and only if, an inner point of it (e.g. the midpoint) is inside the polygon. Using the mentioned "point-in-polygon" function, from the set {Ej} we can keep only the elements being inside the polygon.<br />
Note that the former general/polygon model is (should be) used in a robust data preparation toll chain. For instance, we can detect and remove common area parts from one of the areas when two areas partly overlap (remove from a forest area part of it that is over a lake area), or find and recognize a missing section of a river area, or detect and remove anomalies caused by incorrect relations between river-lines (waterway=river) and the corresponding river-area objects and so on. For illustration of many similar examples see the river in the link <a href="https://goo.gl/p9lR3R">https://goo.gl/p9lR3R</a> . There are many (really large number) of virtual islands, wrong name positions, wrong river width, large redundancy, unnecessary rendering... just to mention some. These anomalies could be removed by using the mentioned general model.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '17, 16:05</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-56559" class="comments-container">
<span id="56612"></span>
<div id="comment-56612" class="comment">
<div id="post-56612-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for getting me back. In OSM, way is a set of nodes. Currently, I could find the nodes inside the circle polygon. However, sometimes there is only one point inside the circle polygon. How can I get the intersection points of line and circle? There should be two intersection points about one line and one circle which is not OSM nodes. I am still trying~ Do you have any idea? Thanks!</p>
</div>
<div id="comment-56612-info" class="comment-info">
<span class="comment-age">(14 Jun '17, 03:26)</span> <span class="comment-user userinfo">ob9619</span>
</div>
</div>
</div>
<div id="comment-tools-56559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56559-form-container" class="comment-form-container">
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

