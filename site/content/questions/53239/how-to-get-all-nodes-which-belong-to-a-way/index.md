+++
type = "question"
title = "How to get all nodes which belong to a way?"
description = '''Hi there, Im working on an Android App and trying to highlight a complete street. Right now Im doing this by the coordinates which are given to me by making a HTTP Request to nominatim. But unfortunately it doesnt give me the whole street, but only a small part of it.  So my question is: How can I a...'''
date = "2016-12-04T21:38:00Z"
lastmod = "2016-12-06T11:25:00Z"
weight = 53239
keywords = [ "ways", "nominatim" ]
aliases = [ "/questions/53239" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to get all nodes which belong to a way?](/questions/53239/how-to-get-all-nodes-which-belong-to-a-way)

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
<span id="post-53239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53239-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>Im working on an Android App and trying to highlight a complete street. Right now Im doing this by the coordinates which are given to me by making a HTTP Request to nominatim. But unfortunately it doesnt give me the whole street, but only a small part of it.</p>
<p>So my question is: How can I achieve it, that I get all the coordinates which are shown to me when I search like this: <a href="https://www.openstreetmap.org/way/3957228">https://www.openstreetmap.org/way/3957228</a></p>
<p>Thanks for your help! cheers Jan</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Dec '16, 21:38</strong></p>
<img src="https://secure.gravatar.com/avatar/606668446fa89971264a71ab1dd984a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="janPhil&#39;s gravatar image" />
<p><span>janPhil</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="janPhil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53239" class="comments-container">
<span id="53250"></span>
<div id="comment-53250" class="comment">
<div id="post-53250-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Where are you fetching your data from? (Note that the API provided at openstreetmap.org is only really for the use of editing software.)</p>
</div>
<div id="comment-53250-info" class="comment-info">
<span class="comment-age">(05 Dec '16, 13:46)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53239" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53239-form-container" class="comment-form-container">
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

<span id="53251"></span>

<div id="answer-container-53251" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53251-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Downloading from <a href="https://www.openstreetmap.org/api/0.6/way/3957228/full">https://www.openstreetmap.org/api/0.6/way/3957228/full</a> will return the way including all of its nodes. Read the <a href="https://wiki.openstreetmap.org/wiki/API">API documentation</a> for more information.</p>
<p>Please keep in mind that his API is mainly for <em>editing</em> the map as already explained by Richard. Read the <a href="https://wiki.openstreetmap.org/wiki/API_usage_policy">API usage policy</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '16, 15:13</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-53251" class="comments-container">
<span id="53257"></span>
<div id="comment-53257" class="comment">
<div id="post-53257-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey Scai,</p>
<p>thanks for your answer! The App is just for my Master thesis and so its only a showcase. I will only make a few requests per day, not many.</p>
<p>Thanks again!</p>
<p>Jan</p>
</div>
<div id="comment-53257-info" class="comment-info">
<span class="comment-age">(06 Dec '16, 09:50)</span> <span class="comment-user userinfo">janPhil</span>
</div>
</div>
</div>
<div id="comment-tools-53251" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53251-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53262"></span>

<div id="answer-container-53262" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53262-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As <a href="https://help.openstreetmap.org/users/158/scai">@scai</a> suggested you can use overpass api</p>
<p>Get Method as JSON output:</p>
<pre><code>http://overpass-api.de/api/interpreter?data=[out:json];way(24777894);(._;&gt;;);out;</code></pre>
<p>Post Method with curl as XML output:</p>
<pre><code>curl \
  -H &quot;Host: overpass-api.de&quot; -H &quot;Content-Type: text/xml&quot;  \
  -d &#39;data=[out:xml];way(3957228);(._;&gt;;);out;&#39;  \
  http://overpass-api.de/api/interpreter  \
  -o my-way.osm</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '16, 11:25</strong></p>
<img src="https://secure.gravatar.com/avatar/39d75f04e1a21ba653b41ac75ec1b026?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gagan&#39;s gravatar image" />
<p><span>Gagan</span><br />
<span class="score" title="305 reputation points">305</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gagan has 2 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-53262" class="comments-container">
&#10;</div>
<div id="comment-tools-53262" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53262-form-container" class="comment-form-container">
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

