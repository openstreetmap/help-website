+++
type = "question"
title = "How to categorize Island names"
description = '''I need help with a scheme to categorize islands, the problem is that Stockholm Archipelago looks very crowded, I don&#x27;t think natural=island was ment to handle the 200k islands of Sweden. These islands are of course of different importance, and we could probably use the same scheme as the place=* sin...'''
date = "2011-02-12T00:56:00Z"
lastmod = "2011-02-16T19:44:00Z"
weight = 2977
keywords = [ "islands", "name", "tagging" ]
aliases = [ "/questions/2977" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to categorize Island names](/questions/2977/how-to-categorize-island-names)

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
<span id="post-2977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2977-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need help with a scheme to categorize islands, the problem is that <a href="http://osm.org/go/0bIe8O">Stockholm Archipelago looks</a> very crowded, I don't think <code>natural=island</code> was ment to handle the 200k islands of Sweden. These islands are of course of different importance, and we could probably use the same scheme as the <code>place=*</code> since these islands actually work like small cities and suburbs..</p>
<p>Some of the islands are more important than the near by suburbs, but most are unimportant?</p>
<p>PS. This is marked as Community wiki since it's very hard to give an answer to this question.</p>
<p>PPS Should I just use <code>important=not_very</code>? :-)</p>
<p><img src="/upfiles/archipelago.png" alt="Stockholm Archipelago" /></p>
<p>From <a href="http://osm.org/go/0bIe8O"></a><a href="http://osm.org/go/0bIe8O"></a><a href="http://osm.org/go/0bIe8O">http://osm.org/go/0bIe8O</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-islands" rel="tag" title="see questions tagged &#39;islands&#39;">islands</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '11, 00:56</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '11, 00:57</strong> </span></p>
</div>
</div>
<div id="comments-container-2977" class="comments-container">
&#10;</div>
<div id="comment-tools-2977" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2977-form-container" class="comment-form-container">
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

<span id="2978"></span>

<div id="answer-container-2978" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2978-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-2978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As the islands are mapped as areas, the renderer could use the size/surface area of each island to control the rendering. So only the names of the larger islands appear at low zooms. Though I don't know if any renderers currently do this, or if it is actually possible with Mapnik etc. It may require some pre-processing, to calculate the size of each island.</p>
<p>Or you could tag the islands with their population (if that data is available), then render based on that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '11, 02:13</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-2978" class="comments-container">
<span id="2989"></span>
<div id="comment-2989" class="comment">
<div id="post-2989-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Bad idea, the size of an island is very unrelated to it's "importantness". I think the most well known island name in there is Grinda and it's pretty small.</p>
</div>
<div id="comment-2989-info" class="comment-info">
<span class="comment-age">(12 Feb '11, 18:54)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="2995"></span>
<div id="comment-2995" class="comment">
<div id="post-2995-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why is that island 'important'? Important to whom?</p>
</div>
<div id="comment-2995-info" class="comment-info">
<span class="comment-age">(12 Feb '11, 22:53)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
<span id="3117"></span>
<div id="comment-3117" class="comment">
<div id="post-3117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why is a city or suburb more important than the name of a place nearby? Sure <code>place=*</code> categories are hard to use to judge importantness, but they are one way to do it.</p>
</div>
<div id="comment-3117-info" class="comment-info">
<span class="comment-age">(16 Feb '11, 19:44)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
</div>
<div id="comment-tools-2978" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2978-form-container" class="comment-form-container">
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

