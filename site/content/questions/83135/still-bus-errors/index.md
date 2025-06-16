+++
type = "question"
title = "still bus errors"
description = '''Example: At 51.3669 7.3097 split the street and save.  Use iD-Editor in browser. This produces 12 bus errors, enclosure 1. The problem exists till spring 2021, compare with questions/81881'''
date = "2022-01-21T07:20:00Z"
lastmod = "2022-01-21T09:03:00Z"
weight = 83135
keywords = [ "bus", "errors" ]
aliases = [ "/questions/83135" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [still bus errors](/questions/83135/still-bus-errors)

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
<span id="post-83135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83135-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Example: At 51.3669 7.3097 split the street and save. Use iD-Editor in browser. This produces 12 bus errors, enclosure <span>1</span>. The problem exists till spring 2021, compare with questions/81881</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '22, 07:20</strong></p>
<img src="https://secure.gravatar.com/avatar/5b255884ec6417c17c8f44e571606b9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NorbertOpen&#39;s gravatar image" />
<p><span>NorbertOpen</span><br />
<span class="score" title="54 reputation points">54</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NorbertOpen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83135" class="comments-container">
<span id="83136"></span>
<div id="comment-83136" class="comment">
<div id="post-83136-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>where is my enclosure?</p>
</div>
<div id="comment-83136-info" class="comment-info">
<span class="comment-age">(21 Jan '22, 07:21)</span> <span class="comment-user userinfo">NorbertOpen</span>
</div>
</div>
<span id="83140"></span>
<div id="comment-83140" class="comment">
<div id="post-83140-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://www.openstreetmap.org/#map=18/51.36690/7.30970">Area of interest</a>.<br />
<a href="https://www.openstreetmap.org/changeset/116414308">Changeset</a>.</p>
<p>Norbert: For future reference, please include clickable links in your questions. You can copy them from the URL field in your browser. That makes it easier for people to respond to you.</p>
</div>
<div id="comment-83140-info" class="comment-info">
<span class="comment-age">(21 Jan '22, 09:03)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-83135" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83135-form-container" class="comment-form-container">
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

<span id="83139"></span>

<div id="answer-container-83139" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83139-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think what you are seeing are general issues iD found in the data you are working on. They have not been caused by your edit.</p>
<p>When you split the road, iD also changed the bus routes following this road in the background. That's normal and expected. It then discovered that these bus routes were missing some information that they - in iDs opinion - should have had, like <code>network:wikidata=Q448199</code> and <code>network:wikipedia=de:Verkehrsverbund Rhein-Ruhr</code>. I disagree that iD should warn when these keys are missing. iD should also not present those warnings to you when the routes were only changed by iD itself and not by our your own doing.</p>
<p>Short summary: Just ignore those bus related warnings.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '22, 08:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jan '22, 10:45</strong> </span></p>
</div>
</div>
<div id="comments-container-83139" class="comments-container">
&#10;</div>
<div id="comment-tools-83139" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83139-form-container" class="comment-form-container">
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

