+++
type = "question"
title = "Database reload for Special Phrases"
description = '''I wonder how often is the nominatim(.org) database reloaded for the Special Phrases. The Special Phrases-page says You should further be aware that Nominatim only reimports the phrases sporadically when the database is reloaded, so changes may take a long time before they appear.  Is there a place I...'''
date = "2018-10-21T13:56:00Z"
lastmod = "2018-10-21T15:13:00Z"
weight = 66405
keywords = [ "special-phrases", "nominatim" ]
aliases = [ "/questions/66405" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Database reload for Special Phrases](/questions/66405/database-reload-for-special-phrases)

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
<span id="post-66405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66405-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I wonder how often is the nominatim(.org) database reloaded for the Special Phrases.</p>
<p>The <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases">Special Phrases</a>-page says</p>
<p><code>You should further be aware that Nominatim only reimports the phrases sporadically when the database is reloaded, so changes may take a long time before they appear.</code></p>
<ol>
<li>Is there a place I can see the <code>"last updated"</code> for the special phrases?</li>
<li>Are the phrases updated on any regular schedule?</li>
<li>Is this <code>"database reload"</code> separate from the places-database-reload? The places seem to be reloading quickly and regularly</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-special-phrases" rel="tag" title="see questions tagged &#39;special-phrases&#39;">special-phrases</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Oct '18, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikLindseth has 2 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Oct '18, 14:10</strong> </span></p>
</div>
</div>
<div id="comments-container-66405" class="comments-container">
&#10;</div>
<div id="comment-tools-66405" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66405-form-container" class="comment-form-container">
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

<span id="66406"></span>

<div id="answer-container-66406" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66406-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="FredrikLindseth has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Special Phrases are not updated on any regular schedule and there is currently no indication when the last update was.</p>
<p>Rerunning the Special Phrase import on an existing database does work only partially. For example, existing phrases are not removed properly. This is the main stopper why the script is not run regularly. If there was an actual update script for phrases, there would be no larger obstacle to run it regularly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '18, 14:11</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-66406" class="comments-container">
<span id="66407"></span>
<div id="comment-66407" class="comment">
<div id="post-66407-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If at some point a Special Phrases for a new language is "complete", would it be possible to request an update for this language, i.e. <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/NO">Norwegian</a>?</p>
</div>
<div id="comment-66407-info" class="comment-info">
<span class="comment-age">(21 Oct '18, 15:13)</span> <span class="comment-user userinfo">FredrikLindseth</span>
</div>
</div>
</div>
<div id="comment-tools-66406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66406-form-container" class="comment-form-container">
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

