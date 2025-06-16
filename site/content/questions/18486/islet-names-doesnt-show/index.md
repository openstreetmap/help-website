+++
type = "question"
title = "Islet names doesn&#x27;t show"
description = '''Hi all, I have updated a lake, which has been restored to its original state. It was dried out for farmland use a long time ago, and is now being restored (almost). I have created the lake as a multipolygon and the islets ways with natural=coastline place=islet drawn counterclockwise. I have added n...'''
date = "2012-12-16T12:55:00Z"
lastmod = "2012-12-16T13:50:00Z"
weight = 18486
keywords = [ "islet", "place", "name" ]
aliases = [ "/questions/18486" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Islet names doesn't show](/questions/18486/islet-names-doesnt-show)

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
<span id="post-18486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18486-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I have updated a lake, which has been restored to its original state. It was dried out for farmland use a long time ago, and is now being restored (almost).</p>
<p>I have created the lake as a multipolygon and the islets ways with natural=coastline place=islet drawn counterclockwise. I have added name=(whatever their name is).</p>
<p>The lake is found <a href="https://www.openstreetmap.org/?lat=55.70696&amp;lon=8.24181&amp;zoom=15&amp;layers=M">here</a>.</p>
<p>However, their names does not appear. I have even tried to add a point with place=islet and name=(it's name), that doesn't show either.</p>
<p>I'm new to contributing and to asking questions, so I thought it would be wiser to reach out to you guys before I am getting this more complicated and erroneous than it has to be.</p>
<p>Thanks, Jesper</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-islet" rel="tag" title="see questions tagged &#39;islet&#39;">islet</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '12, 12:55</strong></p>
<img src="https://secure.gravatar.com/avatar/21fdb756f12afa15f29ba3a25f32619b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jesperd&#39;s gravatar image" />
<p><span>jesperd</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jesperd has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18486" class="comments-container">
&#10;</div>
<div id="comment-tools-18486" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18486-form-container" class="comment-form-container">
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

<span id="18487"></span>

<div id="answer-container-18487" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18487-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-18487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jesperd has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>Coastlines are only for coast (one of the big oceans), not for lakes, so pleas don't use that tagging. Including it as an inner way in the multipolygon is enough.</li>
<li>place=island makes more chance to be rendered, as it's for bigger islands. Mapnik doesn't render all names, only the important names. Islands are important, but islets are not very well known, and small, so probably not rendered.</li>
</ol>
<p>I hope this helped.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '12, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Dec '12, 13:53</strong> </span></p>
</div>
</div>
<div id="comments-container-18487" class="comments-container">
<span id="18488"></span>
<div id="comment-18488" class="comment">
<div id="post-18488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot for the feedback. No, I didn't invent Islet myself, I tried to follow the guidelines found here: <a href="https://wiki.openstreetmap.org/wiki/Tag:place%3Dislet">https://wiki.openstreetmap.org/wiki/Tag:place%3Dislet</a></p>
<p>I'll change it to Island, remove the coastline, see what happens.</p>
<p>Thanks!</p>
</div>
<div id="comment-18488-info" class="comment-info">
<span class="comment-age">(16 Dec '12, 13:36)</span> <span class="comment-user userinfo">jesperd</span>
</div>
</div>
<span id="18489"></span>
<div id="comment-18489" class="comment">
<div id="post-18489-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmmm, it seems to be a know tag indeed, I didn't know that. It must be that the Mapnik developers either don't think that tag is important (as it's for small islands), or don't know that tag too.</p>
</div>
<div id="comment-18489-info" class="comment-info">
<span class="comment-age">(16 Dec '12, 13:44)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
<span id="18490"></span>
<div id="comment-18490" class="comment">
<div id="post-18490-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I did help. Thanks a lot. I did both of your suggestions, so I don't know which it was that did the trick or if it was both. Before I tagged it as an "Islet", I read about the difference between Islands and Islets and found that there was no general concencus on when to use what although Islet was just a small Island</p>
</div>
<div id="comment-18490-info" class="comment-info">
<span class="comment-age">(16 Dec '12, 13:46)</span> <span class="comment-user userinfo">jesperd</span>
</div>
</div>
<span id="18491"></span>
<div id="comment-18491" class="comment">
<div id="post-18491-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>the coastline is only rendered once in a month or even less (it's not expected to change), so that won't affect the rendering immediately, but it could have given strange results when they tried to render it.</p>
<p>So it will be the changing to place=island that did it. I don't understand why you would need a tag for small islands anyway. Size is something that can be calculated, it shouldn't be in the definition of a tag.</p>
</div>
<div id="comment-18491-info" class="comment-info">
<span class="comment-age">(16 Dec '12, 13:50)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-18487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18487-form-container" class="comment-form-container">
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

