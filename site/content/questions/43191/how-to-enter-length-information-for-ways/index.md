+++
type = "question"
title = "How to enter length information for ways?"
description = '''I&#x27;ve been measuring trails in town simultaneously with a GPS logger and a distance-measuring wheel. As a result, I know the distances between trail junctions quite accurately. My repeatability seems to be around 1/4 percent. Due to the relatively high curvature of trails (both horizontal and vertica...'''
date = "2015-05-24T21:14:00Z"
lastmod = "2015-05-25T16:54:00Z"
weight = 43191
keywords = [ "ways", "distance" ]
aliases = [ "/questions/43191" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to enter length information for ways?](/questions/43191/how-to-enter-length-information-for-ways)

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
<span id="post-43191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43191-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been measuring trails in town simultaneously with a GPS logger and a distance-measuring wheel. As a result, I know the distances between trail junctions quite accurately. My repeatability seems to be around 1/4 percent. Due to the relatively high curvature of trails (both horizontal and vertical), inferring distance by doing the math on the way points is not as accurate. How do I store my accurate distances?</p>
<p>I see that there is a DISTANCE tag, but according to the documentation only applies to relations. First, you have to actually create a relation to use it, which I don't think is appropriate for many of our trails. Second, it seems to be intended to give the length of a longer route thru a bunch of intersections and possibly as it switches ways in the OSM database.</p>
<p>I was expecting to make individual ways between trail junctions, then use something like the DISTANCE tag to explicitly state how long that way is, regardless of what you might get by adding up the individual line segments that were entered by eyeball-filtering GPS traces.</p>
<h2 id="added-in-response-to-comments">Added in response to comments</h2>
<p>I haven't directly compared my measurements to distances computed from OSM data, but I have seen significant discrepancies between the wheel-measured distances and distances computed from other people's GPS tracks, over 10% in some cases. That may have been because these other GPS tracks were rather sloppy, which is one reason I'm re-doing all the trails in town. It just seems a shame that there isn't a mechanism to save this data in OSM when known, but if that's not done then I will stop looking for it.</p>
<p>Trails are thin, so there is no issue of walking on the other side of a street. The biggest issue that will make the distance experienced by two people different is when they go around a wet area differently.</p>
<p>As for getting out of date when someone else edits the way, I can see the point to that. That is probably the best reason given to not add distances to ways.</p>
<p>I guess the overall answer is</p>
<ol>
<li></li>
<li>Distances on ways is not how OSM is intended to work.</li>
<li>Even if you did it, it would cause maintenance problems as people edit the ways and then don't update the distances accordingly.</li>
<li>We think that the error isn't that great, and don't care if it is.</li>
</ol>
If someone wants to write a nice answer stating this and possibly elaborating on it, I'll be happy to upvote and accept it. I'm not going to upvote or accept SK53's answer since it didn't address the question. I asked how to store the more accurate directly-measured distance data instead of requiring it to be calculated, and his answer is basically "It's not needed since it can be calculated".
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '15, 21:14</strong></p>
<img src="https://secure.gravatar.com/avatar/523875048fad58440c3d08d2b91a8de8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Olin%20Lathrop&#39;s gravatar image" />
<p><span>Olin Lathrop</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Olin Lathrop has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '15, 13:41</strong> </span></p>
</div>
</div>
<div id="comments-container-43191" class="comments-container">
<span id="43199"></span>
<div id="comment-43199" class="comment">
<div id="post-43199-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How does your measurement compare with measurements from OSM's 2D geometry ? And when correcting for relief using DEM data ? Did you consider that the personal decision of walking on this or that side of the road will throw off measurements ? Chances are that distance measured from OSM data + SRTM is just as good as manually-measured distance.</p>
</div>
<div id="comment-43199-info" class="comment-info">
<span class="comment-age">(25 May '15, 11:55)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="43206"></span>
<div id="comment-43206" class="comment">
<div id="post-43206-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the additional paragraphs, they seem spot-on.</p>
<p>Distances from GPS traces can have a big error, especially in forest/valley/city, or if making pauses, or if recording at less than 1s frequency. Map data corrected by a human and helped by satellite imagery ought to be much more accurate, on par with a measuring wheel if the path is narrow and relief is accounted for.</p>
</div>
<div id="comment-43206-info" class="comment-info">
<span class="comment-age">(25 May '15, 16:26)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="43207"></span>
<div id="comment-43207" class="comment">
<div id="post-43207-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suggest you create the <a href="https://wiki.openstreetmap.org/wiki/Route">route relation</a> corresponding to the trails when applicable, an then look up the trail details on <a href="http://hiking.waymarkedtrails.org/">waymarked trails</a>.</p>
</div>
<div id="comment-43207-info" class="comment-info">
<span class="comment-age">(25 May '15, 16:31)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43191" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43191-form-container" class="comment-form-container">
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

<span id="43208"></span>

<div id="answer-container-43208" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43208-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-43208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Olin Lathrop has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>I see that there is a DISTANCE tag, but according to the documentation only applies to relations. First, you have to actually create a relation to use it, which I don't think is appropriate for many of our trails. [...] I was expecting to make individual ways between trail junctions</p>
</blockquote>
<p>Nope. A way in OSM represents a real-world geometry with shared attributes. As soon as the attributes change, you start a new way.</p>
<p>The upshot is that a relation is the correct way to store trail-wide information, since you can't rely on there being just one way for your whole trail.</p>
<p>(It's technically possible to create a way that shares sequences of nodes with other ways; if you were determined to store the information in a way, this would be the way to do it. However, it's <em>strongly</em> discouraged because it's a nightmare to edit and a nightmare to parse.)</p>
<p>FWIW, I generally tend to agree with SK53 that this information can and ought to be automatically computed. If you absolutely need the level of accuracy that an accurate centreline can't provide, then OSM is probably not the right project for your needs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '15, 16:54</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '15, 16:56</strong> </span></p>
</div>
</div>
<div id="comments-container-43208" class="comments-container">
&#10;</div>
<div id="comment-tools-43208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43208-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43192"></span>

<div id="answer-container-43192" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43192-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-43192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just dont add distance to ways. It is completely unnecessary, just as adding lat/lon to each node is not needed.</p>
<p>OSM is a geographical database, it can be calculated, just as every router does.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '15, 21:36</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-43192" class="comments-container">
<span id="43193"></span>
<div id="comment-43193" class="comment">
<div id="post-43193-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>But the point is that these calculations will be less accurate than the explicitly measured data I have. When I walk a trail, the GPS point-samples my motion, adds inevitable error to these points, then the result of several GPS tracks are low pass filtered by eye and the point-sampled again to make the OSM ways. Adding up the lengths of this piecewise linear approximation won't be as accurate as measuring the actual trail by running over it with a 19 inch wheel. My question is how to provide this more accurate information for OSM ways. Are you saying there is no mechanism for this and to live with the less accurate summing of line segments?</p>
</div>
<div id="comment-43193-info" class="comment-info">
<span class="comment-age">(24 May '15, 21:43)</span> <span class="comment-user userinfo">Olin Lathrop</span>
</div>
</div>
<span id="43194"></span>
<div id="comment-43194" class="comment">
<div id="post-43194-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Well feel free to add this using the distance tag.</p>
<p>What happens when someone splits the trail? For instance to mark a change of surface. How do they re-calculate the distance for each segment. Elevation &amp; other aspects will obviously also affect distance. I really see no advantage of storing it in OSM for the sake of an apparent small increase in accuracy.</p>
</div>
<div id="comment-43194-info" class="comment-info">
<span class="comment-age">(25 May '15, 07:52)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="43200"></span>
<div id="comment-43200" class="comment">
<div id="post-43200-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The distance tag on relations is mainly (only ?) usefull for QA purposes : if a route's geometry is significantly shorter than its distance tag implies, then the route relation is probably incomplete and should be fixed.</p>
</div>
<div id="comment-43200-info" class="comment-info">
<span class="comment-age">(25 May '15, 11:59)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43192" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43192-form-container" class="comment-form-container">
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

