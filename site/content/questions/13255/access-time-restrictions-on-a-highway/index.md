+++
type = "question"
title = "access time restrictions on a highway"
description = '''Hi all, I read about the acces restrictions but i can&#x27;t work out how to tag this street:  acces for all vehicles from 6pm to  11am  acces only for vehicles with a city  permit from 11am to 6pm pedestrians, cyclist, public  transport and taxi may enter at all  times  And to make it even better: the o...'''
date = "2012-06-04T19:00:00Z"
lastmod = "2012-06-04T20:39:00Z"
weight = 13255
keywords = [ "access" ]
aliases = [ "/questions/13255" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [access time restrictions on a highway](/questions/13255/access-time-restrictions-on-a-highway)

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
<span id="post-13255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13255-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I read about the acces restrictions but i can't work out how to tag this street:</p>
<ul>
<li>acces for all vehicles from 6pm to 11am</li>
<li>acces only for vehicles with a city permit from 11am to 6pm</li>
<li>pedestrians, cyclist, public transport and taxi may enter at all times</li>
</ul>
<p>And to make it even better: the opening hours on saturday are diffirent</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jun '12, 19:00</strong></p>
<img src="https://secure.gravatar.com/avatar/8ebaab14eda9cc949a08719ec6c42959?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joske&#39;s gravatar image" />
<p><span>Joske</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joske has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jun '12, 18:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-13255" class="comments-container">
&#10;</div>
<div id="comment-tools-13255" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13255-form-container" class="comment-form-container">
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

<span id="13256"></span>

<div id="answer-container-13256" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13256-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a proposal about <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Extended_conditions_for_access_tags#Examples">extended access conditions</a> that can handle such special cases. I'll try to find the right tags for your conditions:</p>
<p><em>foot=yes</em><br />
<em>vehicle=yes</em> (includes bicycle, bus, taxi, ...)<br />
<em>vehicle:(11:00-18:00)=destination</em> (there might be a better tag for "city permit" than <em>destination</em>)<br />
<em>vehicle:(Sa 11:00-14:00)=no</em> (as an example, you didn't mention the exact conditions for saturday)</p>
<p>But don't expect any application to handle those conditions correctly at the moment.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '12, 20:39</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '12, 20:40</strong> </span></p>
</div>
</div>
<div id="comments-container-13256" class="comments-container">
&#10;</div>
<div id="comment-tools-13256" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13256-form-container" class="comment-form-container">
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

