+++
type = "question"
title = "How to output from TileMill in a format like openstreetmap.org standard"
description = ''' I want to generate maps in TileMill which look identical to the format produced by openstreetmap.org with the Standard setting. Where can I find the relevant config files?  Is it sufficient to replace the following files base.mss, labels.mss, palette.mss, project.mml and roads.mss, in my project fo...'''
date = "2012-09-07T07:42:00Z"
lastmod = "2013-11-20T22:08:00Z"
weight = 15875
keywords = [ "project", "tilemill", "mapnik", "format" ]
aliases = [ "/questions/15875" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to output from TileMill in a format like openstreetmap.org standard](/questions/15875/how-to-output-from-tilemill-in-a-format-like-openstreetmaporg-standard)

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
<span id="post-15875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15875-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<ol>
<li>I want to generate maps in TileMill which look identical to the format produced by openstreetmap.org with the Standard setting. Where can I find the relevant config files?</li>
<li>Is it sufficient to replace the following files base.mss, labels.mss, palette.mss, project.mml and roads.mss, in my project folder to get the style I need?</li>
</ol>
<p>I'm running TileMill on Ubuntu 12.04. I downloaded the OSM data for Spain and imported it into a Postgre database. All of this is running perfectly, my question is just about how to get the style used on the website.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-project" rel="tag" title="see questions tagged &#39;project&#39;">project</span> <span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-format" rel="tag" title="see questions tagged &#39;format&#39;">format</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Sep '12, 07:42</strong></p>
<img src="https://secure.gravatar.com/avatar/942ed86f749d81b670bc5d1fa3faf460?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ger%20Kelly&#39;s gravatar image" />
<p><span>Ger Kelly</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ger Kelly has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Nov '13, 23:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-15875" class="comments-container">
<span id="28323"></span>
<div id="comment-28323" class="comment">
<div id="post-28323-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I've resurrected and re-answered this question because it may still come up in response to searches. The original answer was correct at the time but has been overtaken by events.</p>
</div>
<div id="comment-28323-info" class="comment-info">
<span class="comment-age">(20 Nov '13, 22:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15875" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15875-form-container" class="comment-form-container">
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

<span id="15876"></span>

<div id="answer-container-15876" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15876-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>TileMill uses CartoCSS as a styling language, but the actual OSM.org Standard style is written in Mapnik XML and thus can't be used in TileMill directly. It is technically be possible to create a TileMill project that closely approximates the standard style, but as far as I know no one has created such a thing.</p>
<p>If you want tiles that look exactly like or very similar to those on OSM.org, it may be easiest to use something like generate_tiles.py with the standard Mapnik style. Otherwise you should see if playing around with the colours and style of the OSM Bright template (which it sounds like you already have set up?) to get close to what you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '12, 08:30</strong></p>
<img src="https://secure.gravatar.com/avatar/90af4b163a309869d590111d8114836a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajashton&#39;s gravatar image" />
<p><span>ajashton</span><br />
<span class="score" title="170 reputation points">170</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajashton has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-15876" class="comments-container">
&#10;</div>
<div id="comment-tools-15876" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15876-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28322"></span>

<div id="answer-container-28322" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28322-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-28322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap uses a <span>CartoCSS</span>-based stylesheet since August 2013: <a href="https://github.com/gravitystorm/openstreetmap-carto">openstreetmap-carto</a>. So you can load that directly into TileMill directly. You can then edit it as you wish, export a .xml stylesheet from TileMill, and use that with your main renderer.</p>
<p>If the machine that you use for rendering isn't the same as the one that you have TileMill installed you may need to check for renderd errors in its logfile (missing fonts, file paths not qualified, etc.) after transferring the stylesheet - files exported by TileMill may refer to components of the original TileMill project, and in turn (at least with OSMBright, but not with openstreetmap-carto) there may be references to TileMill's download cache.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Nov '13, 22:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Nov '13, 23:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-28322" class="comments-container">
&#10;</div>
<div id="comment-tools-28322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28322-form-container" class="comment-form-container">
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

