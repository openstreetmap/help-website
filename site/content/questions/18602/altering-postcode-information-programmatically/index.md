+++
type = "question"
title = "Altering postcode information programmatically"
description = '''G&#x27;Day folks! I&#x27;m a newbie here with OSM (but by no means a newbie with programming). I have a considerable amount of postcode data and I was wondering if there was a way of programmatically updating all towns in Australia that don&#x27;t have associated postcode information and whether this will automati...'''
date = "2012-12-19T13:50:00Z"
lastmod = "2012-12-19T17:19:00Z"
weight = 18602
keywords = [ "town", "streets", "postcode" ]
aliases = [ "/questions/18602" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Altering postcode information programmatically](/questions/18602/altering-postcode-information-programmatically)

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
<span id="post-18602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18602-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>G'Day folks! I'm a newbie here with OSM (but by no means a newbie with programming).</p>
<p>I have a considerable amount of postcode data and I was wondering if there was a way of programmatically updating all towns in Australia that don't have associated postcode information and whether this will automatically update the streets in them with the addr:postcode tag (or do I really have to manually do this?)</p>
<p>BTW- GREAT project. The street data information that I was able to download from it with Osmosis has been a real save for my projects. Cheers.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-town" rel="tag" title="see questions tagged &#39;town&#39;">town</span> <span class="post-tag tag-link-streets" rel="tag" title="see questions tagged &#39;streets&#39;">streets</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '12, 13:50</strong></p>
<img src="https://secure.gravatar.com/avatar/f3189459dcedec3695feb258f0a44142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jason%20Barraclough&#39;s gravatar image" />
<p><span>Jason Barrac...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jason Barraclough has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18602" class="comments-container">
<span id="18632"></span>
<div id="comment-18632" class="comment">
<div id="post-18632-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Updating the towns will not change tags on any other element. This is neither desired nor necessary. We have a spatial database, and therefore an adress already has a certain post code if it lies inside an area with that post code.</p>
<p>The "addr:postcode" tag ist rather a workaround in cases where the post code cannot be deducted automatically.</p>
</div>
<div id="comment-18632-info" class="comment-info">
<span class="comment-age">(19 Dec '12, 17:19)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-18602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18602-form-container" class="comment-form-container">
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

<span id="18619"></span>

<div id="answer-container-18619" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18619-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-18619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's wiki page about data importing <a href="https://wiki.openstreetmap.org/wiki/Import">here</a>, and that links to guidelines that you'll need to follow before doing any imports. When it comes to discussing people in the Australian community directly, you'll probably get more feedback via the <a href="http://lists.openstreetmap.org/listinfo/talk-au">country mailing list</a> rather than here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '12, 15:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-18619" class="comments-container">
&#10;</div>
<div id="comment-tools-18619" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18619-form-container" class="comment-form-container">
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

