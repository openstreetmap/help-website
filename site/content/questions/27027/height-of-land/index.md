+++
type = "question"
title = "Height of land"
description = '''Is there a better way to mark the highest elevation of a highway other then using a simple node with the tag ele=xxx meters? The kind of place I&#x27;m referring to is known in hiker&#x27;s parlance as the &quot;height of land&quot;. It is not necessarily a mountain pass but does mark the highest point a highway (or tr...'''
date = "2013-10-09T03:50:00Z"
lastmod = "2013-10-10T04:06:00Z"
weight = 27027
keywords = [ "elevation", "tagging", "height" ]
aliases = [ "/questions/27027" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Height of land](/questions/27027/height-of-land)

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
<span id="post-27027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27027-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a better way to mark the highest elevation of a highway other then using a simple node with the tag ele=xxx meters?</p>
<p>The kind of place I'm referring to is known in hiker's parlance as the "height of land". It is not necessarily a mountain pass but does mark the highest point a highway (or trail) attains.</p>
<p>Furthermore, because the height specified in the "ele" tag is supposed to be in meters should one refrain from adding a units indicator (e.g. "m." or "meters")?</p>
<p>Thanks, Dave</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-elevation" rel="tag" title="see questions tagged &#39;elevation&#39;">elevation</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-height" rel="tag" title="see questions tagged &#39;height&#39;">height</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '13, 03:50</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Oct '13, 03:51</strong> </span></p>
</div>
</div>
<div id="comments-container-27027" class="comments-container">
&#10;</div>
<div id="comment-tools-27027" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27027-form-container" class="comment-form-container">
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

<span id="27032"></span>

<div id="answer-container-27032" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27032-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AlaskaDave has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you tag the elevation anywhere, it should be on a node as it doesn't make sense otherwise (puting contour lines into osm is not a good idea either). It is usually combined with natural=peak, but it is usable on any physical feature really.</p>
<p>Note that there are many different reference points that can be used to give the elevation of a point. If you know which one is being used, you should tag the specific ele:XXXX in addition to ele.</p>
<p>However, depending on your needs, OSM might not be the best place to store elevation data, because elevation is continuous whereas osm is discrete. Most often, elevation data is obtained from STRM and ASTER public datasets, and combined with OSM to get the desired output.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '13, 11:12</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-27032" class="comments-container">
<span id="27043"></span>
<div id="comment-27043" class="comment">
<div id="post-27043-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I wasn't wanting to add contours but I was hoping for something more significant than a simple node with an ele=1500 tag. At the high point of these highways there are no reference points, only the fact that the road is at its highest elevation. Thanks for your help.</p>
</div>
<div id="comment-27043-info" class="comment-info">
<span class="comment-age">(09 Oct '13, 14:46)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="27044"></span>
<div id="comment-27044" class="comment">
<div id="post-27044-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As already explained by Vincent the highest point can be tagged as <a href="https://wiki.openstreetmap.org/wiki/Tag:natural%3Dpeak">natural=peak</a>. But this should only be done for somewhat important peaks and not every small hill.</p>
</div>
<div id="comment-27044-info" class="comment-info">
<span class="comment-age">(09 Oct '13, 14:52)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="27045"></span>
<div id="comment-27045" class="comment">
<div id="post-27045-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Roads and trails often go through passes rather than over peaks. And they may well have an elevation marker on them. For hikers especially they have significance in trip planning. So natural=peak would not be appropriate. I see a few natural=pass tags in use but despite its low usage I think it would be appropriate.</p>
<p>Rereading original post and apparently passes are not specific here. I agree that tagging the high point on a trail or road is useful but can't suggest another companion tag to use in all cases.</p>
</div>
<div id="comment-27045-info" class="comment-info">
<span class="comment-age">(09 Oct '13, 15:13)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="27065"></span>
<div id="comment-27065" class="comment">
<div id="post-27065-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm fairly sure this point is an actual pass so the natural=pass tag should serve. Thailand is not as carefully mapped or as well known as most countries I've been in -- we're working to change that ;-)</p>
<p>Thanks again to all.</p>
</div>
<div id="comment-27065-info" class="comment-info">
<span class="comment-age">(10 Oct '13, 04:06)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-27032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27032-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27047"></span>

<div id="answer-container-27047" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27047-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Simply add the tag "ele" (described <a href="https://wiki.openstreetmap.org/wiki/Key:ele">here</a>) to the nodes of interest on the trail/path/highway. If the node doesn't exist, add a new node on the way. This node does <em>not</em> need to be tagged with anything else, like natural=peak.</p>
<p>There are a few examples on the documentation page for the tag, and it seems that these use cases are the ones you described in the original question.</p>
<p>Also, ways <em>may</em> be tagged with the "ele" key, like airport runways, etc, as described in the documentation as well, provided they are "flat".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '13, 16:26</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-27047" class="comments-container">
&#10;</div>
<div id="comment-tools-27047" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27047-form-container" class="comment-form-container">
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

