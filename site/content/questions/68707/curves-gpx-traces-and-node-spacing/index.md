+++
type = "question"
title = "Curves, GPX traces, and node spacing"
description = '''This morning I did a walking capture of a GPX trace. One of the road curves I walked (all rural, limerock/minimal surface) is represented in OSM data as 7 straight segments. The GPX trace captured a few hundred points in this specific road segment (i.e. the long sweeping curve). The original data (f...'''
date = "2019-04-08T15:26:00Z"
lastmod = "2019-04-10T08:18:00Z"
weight = 68707
keywords = [ "tiger", "accuracy", "gpx", "curves", "dime" ]
aliases = [ "/questions/68707" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Curves, GPX traces, and node spacing](/questions/68707/curves-gpx-traces-and-node-spacing)

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
<span id="post-68707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68707-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This morning I did a walking capture of a GPX trace. One of the road curves I walked (all rural, limerock/minimal surface) is represented in OSM data as 7 straight segments. The GPX trace captured a few hundred points in this specific road segment (i.e. the long sweeping curve).</p>
<p>The original data (for the curve) was entered in 2007 from TIGER file sources. Looking at the history, I see that I did some minimal editing (nodes neither added nor removed) in 2012. At that time I did not have a GPS capable device. The road has not been edited other than those two instances. I now have a GPX capable phone, and walked it this morning. It is obvious, from the ground truth, that the original TIGER sourced segments do not properly represent the arc of the curve. As the TIGER data dates from ~2007, they are likely descended from the much earlier US Census DIME files (used in the 1990 and 2000 census collections).</p>
<p>Which all brings me to the question … How accurate should those curve segments be (and totally ignoring what any BING images might show) ? Should I move, and increase, the number of segments representing the curve ? Is there a standard for the length of each of those straight line nodes ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiger" rel="tag" title="see questions tagged &#39;tiger&#39;">tiger</span> <span class="post-tag tag-link-accuracy" rel="tag" title="see questions tagged &#39;accuracy&#39;">accuracy</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-curves" rel="tag" title="see questions tagged &#39;curves&#39;">curves</span> <span class="post-tag tag-link-dime" rel="tag" title="see questions tagged &#39;dime&#39;">dime</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '19, 15:26</strong></p>
<img src="https://secure.gravatar.com/avatar/6e364ade0c0316e0d5bca4a10bec276f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NitaRae&#39;s gravatar image" />
<p><span>NitaRae</span><br />
<span class="score" title="61 reputation points">61</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NitaRae has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68707" class="comments-container">
&#10;</div>
<div id="comment-tools-68707" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68707-form-container" class="comment-form-container">
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

<span id="68709"></span>

<div id="answer-container-68709" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68709-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Good question. I have no idea as I'm not that knowledgeable about OSM. My guess would be several meters. Two things come to mind: how accurate is your and most anyone else's GPS trace? Often reported by the GPS as about 9 meters; although it usually seems better than that. And how accurately aligned are the Bing aerial views?</p>
<p>How far off is the OSM route for the route in question?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '19, 16:15</strong></p>
<img src="https://secure.gravatar.com/avatar/262ace94f9a2925629114f9260378be5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MtnBiker&#39;s gravatar image" />
<p><span>MtnBiker</span><br />
<span class="score" title="116 reputation points">116</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MtnBiker has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Apr '19, 16:16</strong> </span></p>
</div>
</div>
<div id="comments-container-68709" class="comments-container">
<span id="68710"></span>
<div id="comment-68710" class="comment">
<div id="post-68710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Accuracy of the GPX capture … it varies from minute to minute, based on foliage overhead, satellite angles, etc. I walked the entire trace with my device held flat on the palm of my hand, out in front, to minimize other variances.</p>
<p>My question was both about the accuracy of the original nodes (which are straight lines that cross my trace several times), and (if I am going to replace the original much longer nodes with more shorter straight-line nodes) how many and what is the suggested length for each ? Short of a Bézier curve, the curves have to be represented as a collection of short straight line segments.</p>
<p>I do not believe the OSM route is off, but it does not represent the curve, as found on the ground. Most of the nodes are +/- the actual road. Shorter straight lines will more accurately represent the curve, by bringing the average error of the nodes down. How many is the question.</p>
</div>
<div id="comment-68710-info" class="comment-info">
<span class="comment-age">(08 Apr '19, 16:43)</span> <span class="comment-user userinfo">NitaRae</span>
</div>
</div>
<span id="68711"></span>
<div id="comment-68711" class="comment">
<div id="post-68711-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In addition to issues with foliage, etc., there can be ionospheric weather conditions. Generally, the best practice would be to collect several sets of GPX tracks on different days. With that you can align the imagery to a best fit. Finally, dealing with your specific question of how many line segments to use: I usually add as many points as needed to keep the line segments completely on the paved way as seen in the aerial imagery.</p>
</div>
<div id="comment-68711-info" class="comment-info">
<span class="comment-age">(08 Apr '19, 17:19)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="68713"></span>
<div id="comment-68713" class="comment">
<div id="post-68713-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's a fair answer. I have now compared my GPX trace, the original OSM nodes, and the BING overhead images. My GPX traces, on the non-straightline segments, track closer to the where BING images suggest the road should be, than the OSM nodes do. Time to do some editing.</p>
</div>
<div id="comment-68713-info" class="comment-info">
<span class="comment-age">(08 Apr '19, 18:12)</span> <span class="comment-user userinfo">NitaRae</span>
</div>
</div>
<span id="68742"></span>
<div id="comment-68742" class="comment">
<div id="post-68742-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I always use Potlatch2 to edit. P2 can show all traces which i use to check Bing alignment. I plot enough nodes to get an accurate copy of the road line by plotting nodes on the image of the road centre line.</p>
</div>
<div id="comment-68742-info" class="comment-info">
<span class="comment-age">(10 Apr '19, 08:15)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="68743"></span>
<div id="comment-68743" class="comment">
<div id="post-68743-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I haven't used JOSM for some time but i think you can also see lots of traces at once, i think iD also does it as well.</p>
</div>
<div id="comment-68743-info" class="comment-info">
<span class="comment-age">(10 Apr '19, 08:18)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-68709" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68709-form-container" class="comment-form-container">
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

