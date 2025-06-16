+++
type = "question"
title = "Is there a web-browser-friendly way to obtain previous versions of large OSM objects?"
description = '''Let&#x27;s imagine that I want to have a look at previous versions of the Pennine Way. It&#x27;s quite large and has quite a few versions, so the history link times out, and a message &quot;Sorry, the data for the relation with the id 63872, took too long to retrieve&quot;. Suppose I just want to see the previous versi...'''
date = "2011-07-07T15:38:00Z"
lastmod = "2013-08-20T22:46:00Z"
weight = 6208
keywords = [ "api", "history", "versions" ]
aliases = [ "/questions/6208" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a web-browser-friendly way to obtain previous versions of large OSM objects?](/questions/6208/is-there-a-web-browser-friendly-way-to-obtain-previous-versions-of-large-osm-objects)

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
<span id="post-6208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6208-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Let's imagine that I want to have a look at previous versions of the <a href="https://www.openstreetmap.org/browse/relation/63872">Pennine Way</a>. It's quite large and has quite a few versions, so the <a href="https://www.openstreetmap.org/browse/relation/63872/history">history</a> link times out, and a message "Sorry, the data for the relation with the id 63872, took too long to retrieve". Suppose I just want to see the previous version - is there a clicky pointy way of doing that?</p>
<p>The only alternatives that I'm aware of is to do something like this:<br />
</p>
<pre><code>wget --timeout=120 http://api.openstreetmap.org/api/0.6/relation/63872/208</code></pre>
<p>or to obtain the same data from an old planet extract. Is there an obvious obtion that I'm missing?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span> <span class="post-tag tag-link-versions" rel="tag" title="see questions tagged &#39;versions&#39;">versions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '11, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-6208" class="comments-container">
<span id="25612"></span>
<div id="comment-25612" class="comment">
<div id="post-25612-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Has anyone developed a repository of older versions that enable a user to view a time-series set of improvements to the basemap with a slider?</p>
</div>
<div id="comment-25612-info" class="comment-info">
<span class="comment-age">(20 Aug '13, 22:19)</span> <span class="comment-user userinfo">mmcnabb</span>
</div>
</div>
</div>
<div id="comment-tools-6208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6208-form-container" class="comment-form-container">
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

<span id="6235"></span>

<div id="answer-container-6235" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6235-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could try using the OSM History Browser to list the change sets and allow you to compare selected changes.</p>
<p><a href="http://osm.virtuelle-loipe.de/history/">http://osm.virtuelle-loipe.de/history/</a></p>
<p>Also the Route Relations 'h' link on the <a href="https://wiki.openstreetmap.org/wiki/WikiProject_United_Kingdom_Long_Distance_Paths">https://wiki.openstreetmap.org/wiki/WikiProject_United_Kingdom_Long_Distance_Paths</a> page will provide the relation number and take you straight there: <a href="http://osm.virtuelle-loipe.de/history/?type=relation&amp;ref=63872">http://osm.virtuelle-loipe.de/history/?type=relation&amp;ref=63872</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '11, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/6edb4957e57770118c3b8022cfce68a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srbrook&#39;s gravatar image" />
<p><span>srbrook</span><br />
<span class="score" title="993 reputation points">993</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srbrook has 3 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-6235" class="comments-container">
<span id="6265"></span>
<div id="comment-6265" class="comment">
<div id="post-6265-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks - just what I was looking for</p>
</div>
<div id="comment-6265-info" class="comment-info">
<span class="comment-age">(10 Jul '11, 22:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-6235" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6235-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6212"></span>

<div id="answer-container-6212" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6212-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, there's no access to old versions (aside from the history link) through the data browser. I use the API link you mentioned above, but from my web browser rather than wget, and then 'View Source'.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '11, 23:40</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-6212" class="comments-container">
&#10;</div>
<div id="comment-tools-6212" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6212-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25614"></span>

<div id="answer-container-25614" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25614-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Since I asked this question back in the dim and distant past a lot of water has passed under the bridge.</p>
<p>There's the <a href="http://iandees.github.io/osm-deep-history/">OSM Deep History tool</a>, for example. That works on nodes on ways, but not on the relation that I asked the question about. It doesn't plot on a map with a slider though - maybe there's something else that does that?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '13, 22:46</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-25614" class="comments-container">
&#10;</div>
<div id="comment-tools-25614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25614-form-container" class="comment-form-container">
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

