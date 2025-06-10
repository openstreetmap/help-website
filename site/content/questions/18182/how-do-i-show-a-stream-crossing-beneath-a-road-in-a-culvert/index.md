+++
type = "question"
title = "How do I show a stream crossing beneath a road in a culvert?"
description = '''I am working on an area near my home town, adding streams and bridges where indicated. However, there are many cases in which a small stream passes beneath a gravel road in a culvert. That is, no actual bridge is involved. What is the best way to create and tag such crossings?'''
date = "2012-12-04T02:39:00Z"
lastmod = "2012-12-06T12:53:00Z"
weight = 18182
keywords = [ "stream", "culvert" ]
aliases = [ "/questions/18182" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I show a stream crossing beneath a road in a culvert?](/questions/18182/how-do-i-show-a-stream-crossing-beneath-a-road-in-a-culvert)

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
<span id="post-18182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18182-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am working on an area near my home town, adding streams and bridges where indicated. However, there are many cases in which a small stream passes beneath a gravel road in a culvert. That is, no actual bridge is involved. What is the best way to create and tag such crossings?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-culvert" rel="tag" title="see questions tagged &#39;culvert&#39;">culvert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Dec '12, 02:39</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-18182" class="comments-container">
<span id="18235"></span>
<div id="comment-18235" class="comment">
<div id="post-18235-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Once you've edited it, perhaps you could post a permalink to the area (either here or on IRC) so that people can say "yes! that's what we meant" or "no - not quite..."?</p>
</div>
<div id="comment-18235-info" class="comment-info">
<span class="comment-age">(06 Dec '12, 11:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="18239"></span>
<div id="comment-18239" class="comment">
<div id="post-18239-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@blahedo</span> - sorry I missed your 2nd reply until just now. Thanks. I figured it out after I realized what the nomenclature tunnel=culvert actually means and that it is set in the advanced tab of the Potlatch2 editor. I have several more to change but it will be easy now.</p>
<p><span>@Andy</span> - thank you as well. I used that method for several other projects. I did find a tally of the various methods used to represent streams running through culverts somewhere and the most popular by far is to split a small stream segment off the main one and tag it tunnel=culvert and level = -1.</p>
</div>
<div id="comment-18239-info" class="comment-info">
<span class="comment-age">(06 Dec '12, 12:53)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-18182" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18182-form-container" class="comment-form-container">
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

<span id="18183"></span>

<div id="answer-container-18183" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18183-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-18183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I believe the official received wisdom is to just tag a segment of the stream as tunnel=culvert (and, as with bridges, don't put a shared node at the crossing). At the moment this does not render in Mapnik as any different from any other stream segment, but then, it doesn't really need to, and any renderers or routers that would actually make use of the culvert information have it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '12, 03:44</strong></p>
<img src="https://secure.gravatar.com/avatar/4a4c8a91603aa21e05f5a441d5c13f26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blahedo&#39;s gravatar image" />
<p><span>blahedo</span><br />
<span class="score" title="736 reputation points">736</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blahedo has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-18183" class="comments-container">
<span id="18184"></span>
<div id="comment-18184" class="comment">
<div id="post-18184-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks blahedo,</p>
<p>You mean, make that stream segment a way? What sort of way - an Unknown Road maybe? When I do that in the "Advanced" panel it looks like this in the "Simple" panel: Tunnel (culvert).</p>
<p>I'm using Potlatch2 and do not yet know for sure how to set tunnel=culvert. I've attempted it for one of my crossings and would like you, or someone else, to to look at it and make it "proper". The latitude coordinates are not showing on Potlatch for some reason - yes, I have that set in my options but Google Earth shows this crossing at (N59.708393, W151.345675).</p>
<p>Thanks for your help.</p>
</div>
<div id="comment-18184-info" class="comment-info">
<span class="comment-age">(04 Dec '12, 04:36)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="18186"></span>
<div id="comment-18186" class="comment">
<div id="post-18186-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>A "way", in OSM parlance, is just a sequence of connected nodes---which could represent a stream, a road, a building outline, or anything else. It looks like you figured out how to identify a segment of a way, and how to tag it as tunnel=culvert; you don't want to mark a stream as a highway, though! Just leave it as a stream (I've switched it back for you).</p>
<p>As an aside, for crossings where the lower item is in a tunnel, you don't need the upper item to also be going over a bridge. Generally it's either/or.</p>
</div>
<div id="comment-18186-info" class="comment-info">
<span class="comment-age">(04 Dec '12, 05:20)</span> <span class="comment-user userinfo">blahedo</span>
</div>
</div>
</div>
<div id="comment-tools-18183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18183-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18234"></span>

<div id="answer-container-18234" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18234-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One method of learning tagging is to look around the map for another one, the search box may help in some cases. Then open the editor to look at it for an example of what to do. Bear in mind it may not be a good example though. someone may give you a permalink to one if you lucky.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '12, 10:56</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-18234" class="comments-container">
&#10;</div>
<div id="comment-tools-18234" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18234-form-container" class="comment-form-container">
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

