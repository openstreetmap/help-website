+++
type = "question"
title = "Looking for best practices for all-way stop intersections."
description = '''What are the best practices for mapping an all-way stop intersection? I&#x27;ve seen where the stop is a single shared node for all the ways at the intersection and I&#x27;ve also seen a separate stop for each way usually at the point of the stop sign or crosswalk. I&#x27;m wondering primarily about stop signs but...'''
date = "2021-08-30T00:54:00Z"
lastmod = "2021-08-30T17:23:00Z"
weight = 81548
keywords = [ "intersections", "stop", "traffic_signals", "stopsign" ]
aliases = [ "/questions/81548" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Looking for best practices for all-way stop intersections.](/questions/81548/looking-for-best-practices-for-all-way-stop-intersections)

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
<span id="post-81548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81548-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What are the best practices for mapping an all-way stop intersection? I've seen where the stop is a single shared node for all the ways at the intersection and I've also seen a separate stop for each way usually at the point of the stop sign or crosswalk. I'm wondering primarily about stop signs but do the same rules apply for traffic signals?</p>
<p><img src="https://help.openstreetmap.org/upfiles/single_node_stop.jpg" alt="Single node stop" /> <img src="https://help.openstreetmap.org/upfiles/multi-stop_intersection.jpg" alt="Muti-stop intersection" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intersections" rel="tag" title="see questions tagged &#39;intersections&#39;">intersections</span> <span class="post-tag tag-link-stop" rel="tag" title="see questions tagged &#39;stop&#39;">stop</span> <span class="post-tag tag-link-traffic_signals" rel="tag" title="see questions tagged &#39;traffic_signals&#39;">traffic_signals</span> <span class="post-tag tag-link-stopsign" rel="tag" title="see questions tagged &#39;stopsign&#39;">stopsign</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Aug '21, 00:54</strong></p>
<img src="https://secure.gravatar.com/avatar/dfbf4141bd05182318d157ff3d1f0b04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mccarbc&#39;s gravatar image" />
<p><span>mccarbc</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mccarbc has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-81548" class="comments-container">
&#10;</div>
<div id="comment-tools-81548" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81548-form-container" class="comment-form-container">
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

<span id="81555"></span>

<div id="answer-container-81555" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81555-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>=traffic_signals</code> and all-way <code>=stop</code> are similar. Changing from tagging on intersection to the stop line is basically iterative refinement, adding increasing details with each edit. If you have time, you are very welcomed and encouraged to draw the point of the stopping.</p>
<p>If you want to map these crosswalks which have no set-back from the intersection and stop line, it's also more logical to represent the <code>=stop</code> at the stop line to present a correct order on the road.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Aug '21, 05:00</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</img>
</div>
</div>
<div id="comments-container-81555" class="comments-container">
&#10;</div>
<div id="comment-tools-81555" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81555-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81552"></span>

<div id="answer-container-81552" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81552-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dstop">stop page</a> on the wiki is rather firm on the mapping of all way stops, although the degree to which mappers agree with the wiki is a little variable. There are supplementary <a href="https://wiki.openstreetmap.org/wiki/Key:traffic_sign">traffic signs</a> tags if you would like to map the sign separately in this instance (same again for <a href="https://wiki.openstreetmap.org/wiki/Tag:road_marking%3Dsolid_stop_line">stop lines</a>).</p>
<p>The various accepted traffic light tagging methods are described <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dtraffic_signals#How_to_map">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Aug '21, 03:10</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-81552" class="comments-container">
<span id="81554"></span>
<div id="comment-81554" class="comment">
<div id="post-81554-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The section isn't really reasonable on duplicating <code>highway=stop</code> on intersection and stop line. This is akin to violating One Feature One Object.</p>
</div>
<div id="comment-81554-info" class="comment-info">
<span class="comment-age">(30 Aug '21, 04:56)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="81560"></span>
<div id="comment-81560" class="comment">
<div id="post-81560-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Where does it recommend duplicate tagging? The all way stop section says don't remove the tag on the intersection and recommends <code>traffic_sign=*</code> for the individual stop positions.</p>
</div>
<div id="comment-81560-info" class="comment-info">
<span class="comment-age">(30 Aug '21, 11:52)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="81561"></span>
<div id="comment-81561" class="comment">
<div id="post-81561-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The text is a bit ambigues. I also read it as Kovoschiz:</p>
<p>"All-way stops should ALWAYS be shown using highway=stop at the intersection node. If you <em>also want to add the individual stopping points</em>, say for use by a safety app (so that the exact stopping points have been recorded) <em>do NOT remove the intersection node highway=stop</em>, which confirms that this junction is an all-way stop." -&gt; It says not to remove the intersection node but to also add nodes at the stopping points. Here there is no mention of traffic sign so I would assume <code>higway=stop</code> is meant.</p>
<p>"If you want to show that <em>the stop line highway=stop nodes</em> are marked with traffic signs, use the traffic_sign=* tag to indicate a physical sign, painted line or an implied stop such as a driveway." -&gt; and here the <code>highway=stop</code> nodes (plural) at the stop lines are mentioned explicitly.</p>
</div>
<div id="comment-81561-info" class="comment-info">
<span class="comment-age">(30 Aug '21, 13:03)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="81562"></span>
<div id="comment-81562" class="comment">
<div id="post-81562-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also find the stop page to be ambiguous (per Kovoschiz) on the point of keeping the intersecting node <code>highway=stop</code> and adding (what seems to me) the redundant <code>highway=stop</code> to the individual stop positions. So for now I'm going to be conservative and just method to mark the intersecting node with <code>highway=stop</code> and not mark the individual stops.</p>
<p>A follow-up question regarding how to mark the single intersecting node, I see that the stop page mentions the option of adding <code>stop=all</code> to that node, but I'm also seeing intersections tagged <code>direction=both</code> instead of <code>stop=all</code>. Could someone add some clarity to that? Would one ever use both tags; <code>stop=all</code> and <code>direction=both</code>? That seems redundant to me.</p>
</div>
<div id="comment-81562-info" class="comment-info">
<span class="comment-age">(30 Aug '21, 16:34)</span> <span class="comment-user userinfo">mccarbc</span>
</div>
</div>
<span id="81563"></span>
<div id="comment-81563" class="comment">
<div id="post-81563-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I hadn't seen the combination stop=all + direction=both before, so I just went to find some. The cases I found were all three- or four-way intersections. IMO, direction=both makes no semantic sense in this context. "Both" directions implies both forward and backward. When tagged on an intersecting node with three four possible directions, the tag doesn't provide anything useful. The only reason I can think of for using direction=both on a highway=stop is in the middle of a way where both forward and backward directions are required to stop (maybe for a footway crossing), though such a case would probably be better represented by two separate highway=stop each with the correct direction.</p>
<p>I would consider it redundant.</p>
</div>
<div id="comment-81563-info" class="comment-info">
<span class="comment-age">(30 Aug '21, 17:23)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-81552" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81552-form-container" class="comment-form-container">
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

