+++
type = "question"
title = "Stream running along and over a road"
description = '''There is a small stream hereabouts that runs along and in some places actually along a road. How can I ensure that the stream is not covered by the road when its rendered? Need z dimension if you see what I mean'''
date = "2019-12-15T10:35:00Z"
lastmod = "2019-12-16T20:35:00Z"
weight = 72108
keywords = [ "road", "stream" ]
aliases = [ "/questions/72108" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Stream running along and over a road](/questions/72108/stream-running-along-and-over-a-road)

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
<span id="post-72108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72108-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is a small stream hereabouts that runs along and in some places actually along a road. How can I ensure that the stream is not covered by the road when its rendered? Need z dimension if you see what I mean</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Dec '19, 10:35</strong></p>
<img src="https://secure.gravatar.com/avatar/3c0c172fce97d93cb27893aa77313b22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quanglewangle&#39;s gravatar image" />
<p><span>Quanglewangle</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quanglewangle has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Dec '19, 11:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-72108" class="comments-container">
<span id="72114"></span>
<div id="comment-72114" class="comment">
<div id="post-72114-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here is a link showing the "leats" in Helston, Cornwall, UK several Cornish towns have them. I towns the are quite neat and tidy but the rural ones are less so and spill over the road. <a href="https://historicengland.org.uk/listing/the-list/list-entry/1208156">https://historicengland.org.uk/listing/the-list/list-entry/1208156</a></p>
</div>
<div id="comment-72114-info" class="comment-info">
<span class="comment-age">(15 Dec '19, 14:23)</span> <span class="comment-user userinfo">Quanglewangle</span>
</div>
</div>
</div>
<div id="comment-tools-72108" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72108-form-container" class="comment-form-container">
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

<span id="72110"></span>

<div id="answer-container-72110" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72110-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-72110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the stream actually runs along the road for a bit then you can map that bit of way as "both road and stream" - <a href="https://www.openstreetmap.org/way/42000985">https://www.openstreetmap.org/way/42000985</a> is an example. The important thing to do is to make sure that a "ford=yes" tag is set on the bit of way that is both road and stream so that data consumers know about it.</p>
<p>Different renderers will show this in different ways - "OSM Carto" shows an icon in the middle of it; <a href="https://map.atownsend.org.uk/maps/map/map.html#zoom=19&amp;lat=53.137397&amp;lon=-1.468399">this one</a> shows the road slightly differently (with a blue border) to show that it is a "long ford".</p>
<p>If you can link to the area we can make more detailed suggestions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '19, 11:33</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-72110" class="comments-container">
&#10;</div>
<div id="comment-tools-72110" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72110-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72109"></span>

<div id="answer-container-72109" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72109-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would create a node on the stream ford=yes like this one. The stream is also tagged as layer -1, the road as no layer tag. <a href="https://www.openstreetmap.org/#map=19/52.19760/-0.07389">https://www.openstreetmap.org/#map=19/52.19760/-0.07389</a></p>
<p>I have seen almost a meter of water on the road half way between these two fords although 99.9% of the time the steam is to the side and off the road.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '19, 11:01</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Dec '19, 11:12</strong> </span></p>
</div>
</div>
<div id="comments-container-72109" class="comments-container">
<span id="72122"></span>
<div id="comment-72122" class="comment">
<div id="post-72122-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Tagging the objects with different layers conflicts with the definition of a ford: a spot where a road and waterway physically intersect. In the case of a ford, both should have the same layer. In your example, the tags indicate that the stream flows under the road, which then isn't a ford.</p>
</div>
<div id="comment-72122-info" class="comment-info">
<span class="comment-age">(16 Dec '19, 18:09)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="72125"></span>
<div id="comment-72125" class="comment">
<div id="post-72125-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for pointing that out. I just used a local ford as an example, then described the tags i had found. I did have doubts, but maybe the mapper used -1 as the water is usually in the gulley by the road.</p>
</div>
<div id="comment-72125-info" class="comment-info">
<span class="comment-age">(16 Dec '19, 20:35)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-72109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72109-form-container" class="comment-form-container">
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

