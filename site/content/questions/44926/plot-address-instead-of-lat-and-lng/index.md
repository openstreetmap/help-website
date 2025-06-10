+++
type = "question"
title = "[closed] Plot address instead of lat and lng"
description = '''Currently I convert the address to lat and lng in the backend (php) then plot the point with the code below. var point = new MQA.Poi({ lat: result[i][&#x27;Lat&#x27;], lng: result[i][&#x27;Lng&#x27;] }); map.addShape(point);  How would I be able to plot the point with just an address rather than converting it myself.'''
date = "2015-08-27T00:41:00Z"
lastmod = "2015-08-27T22:15:00Z"
weight = 44926
keywords = [ "development", "plot", "javascript", "mapquest", "point" ]
aliases = [ "/questions/44926" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Plot address instead of lat and lng](/questions/44926/plot-address-instead-of-lat-and-lng)

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
<span id="post-44926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44926-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Currently I convert the address to lat and lng in the backend (php) then plot the point with the code below.</p>
<pre><code>var point = new MQA.Poi({ lat: result[i][&#39;Lat&#39;], lng: result[i][&#39;Lng&#39;] });
map.addShape(point);</code></pre>
<p>How would I be able to plot the point with just an address rather than converting it myself.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-plot" rel="tag" title="see questions tagged &#39;plot&#39;">plot</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-mapquest" rel="tag" title="see questions tagged &#39;mapquest&#39;">mapquest</span> <span class="post-tag tag-link-point" rel="tag" title="see questions tagged &#39;point&#39;">point</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Aug '15, 00:41</strong></p>
<img src="https://secure.gravatar.com/avatar/c627551db989f565b95aaa04918b9b12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MahoreLee&#39;s gravatar image" />
<p><span>MahoreLee</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MahoreLee has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>27 Aug '15, 22:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-44926" class="comments-container">
<span id="44927"></span>
<div id="comment-44927" class="comment">
<div id="post-44927-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Which library are you talking about?</p>
</div>
<div id="comment-44927-info" class="comment-info">
<span class="comment-age">(27 Aug '15, 07:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44941"></span>
<div id="comment-44941" class="comment">
<div id="post-44941-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Mapquest open API</p>
</div>
<div id="comment-44941-info" class="comment-info">
<span class="comment-age">(27 Aug '15, 15:38)</span> <span class="comment-user userinfo">MahoreLee</span>
</div>
</div>
<span id="44942"></span>
<div id="comment-44942" class="comment">
<div id="post-44942-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>crossposting at <a href="http://forum.openstreetmap.org/viewtopic.php?id=32751">http://forum.openstreetmap.org/viewtopic.php?id=32751</a></p>
</div>
<div id="comment-44942-info" class="comment-info">
<span class="comment-age">(27 Aug '15, 16:54)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="44943"></span>
<div id="comment-44943" class="comment">
<div id="post-44943-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Didn't know which one to post the question on. So far no answers.</p>
</div>
<div id="comment-44943-info" class="comment-info">
<span class="comment-age">(27 Aug '15, 21:19)</span> <span class="comment-user userinfo">MahoreLee</span>
</div>
</div>
<span id="44946"></span>
<div id="comment-44946" class="comment">
<div id="post-44946-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11409/mahorelee">@MahoreLee</a>: please <span>choose</span> only one next time, that saves resources.</p>
</div>
<div id="comment-44946-info" class="comment-info">
<span class="comment-age">(27 Aug '15, 22:14)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44926" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44926-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason ""I finally found the answer" at the forum entry" by aseerel4c26 27 Aug '15, 22:13

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44944"></span>

<div id="answer-container-44944" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44944-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>map.geocodeAndAddLocations('Denver CO');</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '15, 21:21</strong></p>
<img src="https://secure.gravatar.com/avatar/c627551db989f565b95aaa04918b9b12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MahoreLee&#39;s gravatar image" />
<p><span>MahoreLee</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MahoreLee has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44944" class="comments-container">
<span id="44947"></span>
<div id="comment-44947" class="comment">
<div id="post-44947-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you!</p>
</div>
<div id="comment-44947-info" class="comment-info">
<span class="comment-age">(27 Aug '15, 22:15)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44944-form-container" class="comment-form-container">
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

