+++
type = "question"
title = "How can I find the closest way to a point with Overpass API?"
description = '''Hello: I want to find the closest way to a point defined by its geographic coordinates. I found out Overpass API which gave me a list of ways near a point. But I would like having one and only way. Thank you.'''
date = "2015-02-23T16:19:00Z"
lastmod = "2015-02-23T22:25:00Z"
weight = 41285
keywords = [ "overpass", "closest", "way", "point" ]
aliases = [ "/questions/41285" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I find the closest way to a point with Overpass API?](/questions/41285/how-can-i-find-the-closest-way-to-a-point-with-overpass-api)

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
<span id="post-41285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41285-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello:</p>
<p>I want to find the closest way to a point defined by its geographic coordinates. I found out Overpass API which gave me a list of ways near a point. But I would like having one and only way.</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-closest" rel="tag" title="see questions tagged &#39;closest&#39;">closest</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-point" rel="tag" title="see questions tagged &#39;point&#39;">point</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Feb '15, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a22332aa5e78b395c9b22d5375a631c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osmccecsg&#39;s gravatar image" />
<p><span>osmccecsg</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osmccecsg has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Feb '15, 23:14</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-41285" class="comments-container">
<span id="41296"></span>
<div id="comment-41296" class="comment">
<div id="post-41296-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>that is the same question (if I assume you mean walkable/driveable "ways") as <a href="/questions/23579/">given-a-lat-lon-is-it-possible-to-find-the-closest-highwaystreet-record</a> (or the linked questions there), isn't it? Update: ah, okay, specifically with Overpass here …</p>
</div>
<div id="comment-41296-info" class="comment-info">
<span class="comment-age">(23 Feb '15, 20:13)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41285" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41285-form-container" class="comment-form-container">
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

<span id="41298"></span>

<div id="answer-container-41298" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41298-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorting based on distance using Overpass API is already discussed in a Github issue, see <a href="https://github.com/drolbr/Overpass-API/issues/81#issuecomment-37845462">[1]</a> and <a href="https://github.com/drolbr/Overpass-API/issues/81#issuecomment-37846226">[2]</a>. Unfortunately, this feature is not yet available at this time.</p>
<p>I would suggest that you add this use case to the mentioned ticket (i.e. sorting by distance combined with top 1 result), so it doesn't get lost and could be considered for future development.</p>
<p>For the time being, you'd need to use your own logic and post process the Overpass API result to return the closest way only.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '15, 22:25</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-41298" class="comments-container">
&#10;</div>
<div id="comment-tools-41298" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41298-form-container" class="comment-form-container">
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

