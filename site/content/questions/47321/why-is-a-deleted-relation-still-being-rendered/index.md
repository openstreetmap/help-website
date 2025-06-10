+++
type = "question"
title = "Why is a deleted relation still being rendered?"
description = '''I have a problem with the following boundary relation: http://www.openstreetmap.org/relation/5617489  It was deleted yet it&#x27;s still being displayed in the map. Any idea why?'''
date = "2015-12-30T07:55:00Z"
lastmod = "2016-01-14T09:04:00Z"
weight = 47321
keywords = [ "update", "relations", "delete" ]
aliases = [ "/questions/47321" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why is a deleted relation still being rendered?](/questions/47321/why-is-a-deleted-relation-still-being-rendered)

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
<span id="post-47321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47321-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a problem with the following boundary relation:</p>
<p><span></span><a href="http://www.openstreetmap.org/relation/5617489">http://www.openstreetmap.org/relation/5617489</a></p>
<p>It was deleted yet it's still being displayed in the map. Any idea why?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '15, 07:55</strong></p>
<img src="https://secure.gravatar.com/avatar/4f491c3e8c50267c8656b4cc30ee2793?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andresuco&#39;s gravatar image" />
<p><span>Andresuco</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andresuco has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Dec '15, 10:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-47321" class="comments-container">
&#10;</div>
<div id="comment-tools-47321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47321-form-container" class="comment-form-container">
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

<span id="47322"></span>

<div id="answer-container-47322" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47322-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-47322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Andresuco has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's the usual story I think - tiles just not yet updated. <a href="https://help.openstreetmap.org/questions/178/how-often-does-the-main-mapnik-map-get-updated">This question</a> has lots of details about the process. I requested an immediate rerender via "/dirty" of <a href="http://b.tile.openstreetmap.org/14/3700/7146.png">http://b.tile.openstreetmap.org/14/3700/7146.png</a> and the rendering of the relation was removed from that tile.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '15, 08:20</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-47322" class="comments-container">
<span id="47323"></span>
<div id="comment-47323" class="comment">
<div id="post-47323-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the clarification.</p>
</div>
<div id="comment-47323-info" class="comment-info">
<span class="comment-age">(30 Dec '15, 08:47)</span> <span class="comment-user userinfo">Andresuco</span>
</div>
</div>
<span id="47344"></span>
<div id="comment-47344" class="comment">
<div id="post-47344-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi! Is there a way I can request all the tiles showing this behavior to be re-rendered, it's not just the tile you sent here, it's the whole region covered by the old no longer existing relation.</p>
</div>
<div id="comment-47344-info" class="comment-info">
<span class="comment-age">(31 Dec '15, 01:18)</span> <span class="comment-user userinfo">Andresuco</span>
</div>
</div>
<span id="47500"></span>
<div id="comment-47500" class="comment">
<div id="post-47500-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Anything that did an automated series of "/dirty" requests might be frowned upon by the server admins and other users because it's trying to "jump the rendering queue". If the server's busy there's no guarantee that your rendering request will get processed before everyone else's.</p>
</div>
<div id="comment-47500-info" class="comment-info">
<span class="comment-age">(13 Jan '16, 19:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="47508"></span>
<div id="comment-47508" class="comment">
<div id="post-47508-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>General advice for out-of-date rendering: be patient :) The rendering server <em>will</em> eventually get around to updating all the tiles, it may just take a few days.</p>
</div>
<div id="comment-47508-info" class="comment-info">
<span class="comment-age">(14 Jan '16, 07:30)</span> <span class="comment-user userinfo">Lightsider</span>
</div>
</div>
<span id="47509"></span>
<div id="comment-47509" class="comment">
<div id="post-47509-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you want more control over what is and isn't rendered, you are always free to set up your own tileserver, and rerender whatever you want as often as you want/can. However if you don't want to do that, you'll have to share the server with everyone else. :)</p>
</div>
<div id="comment-47509-info" class="comment-info">
<span class="comment-age">(14 Jan '16, 09:04)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
</div>
<div id="comment-tools-47322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47322-form-container" class="comment-form-container">
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

