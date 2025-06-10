+++
type = "question"
title = "Are there any statistics about how often manually dirtying of tiles occurs per day?"
description = '''Are there any statistics about how often manually dirtying to initiate a re-rendering of tiles occurs per day? If it would occur just once in a while (1 time per minute?) would it make sense to set a higher priority to render these tiles earlier than normal tiles in the render queue?'''
date = "2016-12-18T17:18:00Z"
lastmod = "2016-12-19T12:31:00Z"
weight = 53598
keywords = [ "rendering", "tiles", "statistics", "dirty" ]
aliases = [ "/questions/53598" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Are there any statistics about how often manually dirtying of tiles occurs per day?](/questions/53598/are-there-any-statistics-about-how-often-manually-dirtying-of-tiles-occurs-per-day)

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
<span id="post-53598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53598-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Are there any statistics about how often manually dirtying to initiate a re-rendering of tiles occurs per day? If it would occur just once in a while (1 time per minute?) would it make sense to set a higher priority to render these tiles earlier than <em>normal</em> tiles in the render queue?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-dirty" rel="tag" title="see questions tagged &#39;dirty&#39;">dirty</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '16, 17:18</strong></p>
<img src="https://secure.gravatar.com/avatar/bc6d0b055d631830f7891d3f89edb66b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="katpatuka&#39;s gravatar image" />
<p><span>katpatuka</span><br />
<span class="score" title="1041 reputation points"><span>1.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="katpatuka has 2 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-53598" class="comments-container">
&#10;</div>
<div id="comment-tools-53598" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53598-form-container" class="comment-form-container">
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

<span id="53607"></span>

<div id="answer-container-53607" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53607-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I cannot answer the first question, but to answer second ("<em>would it make sense to set a higher priority to render these tiles earlier than normal tiles in the render queue?</em>"): From my point of view NO, dirty tiles should be rendered with lower priority than regular rendering requests, since many tiles for map viewing are rendered on the fly. This means that someone, who is browsing an area that didn't have tiles already rendered, needs them ASAP when viewing the area. It would have a very bad impact on user experience if users are sitting in front of a white map, waiting for their on-the-fly tiles to be rendered, while the server is busy with rendering tiles that where tagged dirty - a dirty map tile is better than no tile at all.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '16, 12:31</strong></p>
<img src="https://secure.gravatar.com/avatar/2ab3f311e46e4ba07af9ad75d4a3dc31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jot&#39;s gravatar image" />
<p><span>jot</span><br />
<span class="score" title="511 reputation points">511</span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jot has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-53607" class="comments-container">
&#10;</div>
<div id="comment-tools-53607" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53607-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53601"></span>

<div id="answer-container-53601" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53601-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-53601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi katpatuka, the first question could be answered by the OSM statistics builder Pascal Neis, he can be reached here <a href="http://neis-one.org/">http://neis-one.org/</a> He might be able to answer the second question. But for starters you should not ask 2 questions in one question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '16, 22:00</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-53601" class="comments-container">
<span id="53604"></span>
<div id="comment-53604" class="comment">
<div id="post-53604-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I do not think Pascal Neis keeps statistics on the number of webserver requests. This data is not available in the data dumps he uses in his typical analysis.</p>
</div>
<div id="comment-53604-info" class="comment-info">
<span class="comment-age">(19 Dec '16, 06:47)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-53601" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53601-form-container" class="comment-form-container">
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

