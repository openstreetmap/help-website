+++
type = "question"
title = "How to disable shapefiles in OSM-Carto?"
description = '''Hi I am wanting to disable the shapefiles and all other external data needed for OSM-Carto. This is because I am rendering a fictional island I have made and don&#x27;t want the real shapefiles in there. I understand I will need to edit the project files and comment out some lines, but I am unsure what t...'''
date = "2020-12-05T19:55:00Z"
lastmod = "2020-12-05T20:22:00Z"
weight = 77855
keywords = [ "openstreetmap-carto", "rendering", "shapefile" ]
aliases = [ "/questions/77855" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to disable shapefiles in OSM-Carto?](/questions/77855/how-to-disable-shapefiles-in-osm-carto)

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
<span id="post-77855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77855-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I am wanting to disable the shapefiles and all other external data needed for OSM-Carto. This is because I am rendering a fictional island I have made and don't want the real shapefiles in there.</p>
<p>I understand I will need to edit the project files and comment out some lines, but I am unsure what to comment out as it is a bit confusing just from reading through the files.</p>
<p>I was suprised when my efforts searching for a solution resulted in finding none with a similar question.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap-carto" rel="tag" title="see questions tagged &#39;openstreetmap-carto&#39;">openstreetmap-carto</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Dec '20, 19:55</strong></p>
<img src="https://secure.gravatar.com/avatar/0eb8b6185698d38543e031bddff23878?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GoodClover&#39;s gravatar image" />
<p><span>GoodClover</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GoodClover has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77855" class="comments-container">
&#10;</div>
<div id="comment-tools-77855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77855-form-container" class="comment-form-container">
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

<span id="77856"></span>

<div id="answer-container-77856" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77856-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm guessing that you could just remove <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/project.mml#L37">this</a> line from the <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/project.mml">main project file</a>. That's what I'd try first, anyway.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '20, 20:11</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-77856" class="comments-container">
<span id="77857"></span>
<div id="comment-77857" class="comment">
<div id="post-77857-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>😅 That would have probably been way easier than what I figured out.</p>
<p>I ended up going through the <code>project.mml</code> file and commenting all sections out that didn't have <code>FROM planet_osm_xxxx</code> and had something else.</p>
</div>
<div id="comment-77857-info" class="comment-info">
<span class="comment-age">(05 Dec '20, 20:22)</span> <span class="comment-user userinfo">GoodClover</span>
</div>
</div>
</div>
<div id="comment-tools-77856" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77856-form-container" class="comment-form-container">
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

