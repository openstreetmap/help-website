+++
type = "question"
title = "how can I make adresses of (parts) of buildings?"
description = '''On the map of my home town there are buildings shown, that in reality consits of one or more home adresses. How can I make that split up? Deleting the building and after that creating each individual adres is quite a lot of work. Must be possible simpler.'''
date = "2014-02-13T10:33:00Z"
lastmod = "2014-02-13T12:44:00Z"
weight = 30709
keywords = [ "adresses" ]
aliases = [ "/questions/30709" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how can I make adresses of (parts) of buildings?](/questions/30709/how-can-i-make-adresses-of-parts-of-buildings)

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
<span id="post-30709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30709-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>On the map of my home town there are buildings shown, that in reality consits of one or more home adresses. How can I make that split up? Deleting the building and after that creating each individual adres is quite a lot of work. Must be possible simpler.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-adresses" rel="tag" title="see questions tagged &#39;adresses&#39;">adresses</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '14, 10:33</strong></p>
<img src="https://secure.gravatar.com/avatar/d6f3972c64ad95596aaad72d7cc9aebb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HWdJ&#39;s gravatar image" />
<p><span>HWdJ</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HWdJ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30709" class="comments-container">
&#10;</div>
<div id="comment-tools-30709" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30709-form-container" class="comment-form-container">
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

<span id="30715"></span>

<div id="answer-container-30715" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30715-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't split a single physical building up just for addressing purposes. There are a number of ways you can approach the problem:</p>
<ul>
<li>If the address of the building covers a range of street numbers, just record this, e.g. addr:housenumber=17-21</li>
<li>If different addresses have separate physical entrances, add nodes for those using building=entrance and tag those with the house number.</li>
<li>If buildings are physically joined but internally separate, such as terraced houses, use the terracing facility/plugin available on most editors to create the terrace. This will be easier and more accurate than doing it by hand.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '14, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-30715" class="comments-container">
<span id="30717"></span>
<div id="comment-30717" class="comment">
<div id="post-30717-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"building=entrance" is more or less deprecated. See "entrance=yes" or "entrance=main" : <a href="http://wiki.openstreetmap.org/wiki/Entrance">http://wiki.openstreetmap.org/wiki/Entrance</a><br />
If you don't know the exact position of the entrance, put the addresses on nodes on the building facade (front) and forget the "entrance" tag.</p>
</div>
<div id="comment-30717-info" class="comment-info">
<span class="comment-age">(13 Feb '14, 12:44)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-30715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30715-form-container" class="comment-form-container">
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

