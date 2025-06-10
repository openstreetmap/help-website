+++
type = "question"
title = "How to use Osmium on Windows and extract pbf file"
description = '''Hi everyone, I&#x27;m a biginner to OSM, and I am working with OpenTripPlanner for my university research. I need a pbf file of my large study area, it&#x27;s Occitanie region in France. Unfortunately, I can&#x27;t use Geofabrik&#x27;s pbf download because Occitanie is divided into 2 differents pbf... I have read that ...'''
date = "2022-12-07T13:31:00Z"
lastmod = "2022-12-07T21:30:00Z"
weight = 86318
keywords = [ "osmium", "openstreetmap" ]
aliases = [ "/questions/86318" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to use Osmium on Windows and extract pbf file](/questions/86318/how-to-use-osmium-on-windows-and-extract-pbf-file)

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
<span id="post-86318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86318-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>I'm a biginner to OSM, and I am working with OpenTripPlanner for my university research. I need a pbf file of my large study area, it's Occitanie region in France. Unfortunately, I can't use Geofabrik's pbf download because Occitanie is divided into 2 differents pbf...</p>
<p>I have read that I have to use Osmium to extract my regional study. But I don't know how to launch Osmium in Windows 11. I downloaded the zip file called "osmium-tool-1.14.0" on github, but then I don't understand what to do... The documentation is unclear for me because I'm just beginning. How can I launch Osmium and extract my area in pbf file ?</p>
<p>Thanks a lot for your help ! JC</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Dec '22, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a3cd4a62b1cf11c6aeb18dc486a2848f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JC_ULLES&#39;s gravatar image" />
<p><span>JC_ULLES</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JC_ULLES has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86318" class="comments-container">
&#10;</div>
<div id="comment-tools-86318" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86318-form-container" class="comment-form-container">
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

<span id="86319"></span>

<div id="answer-container-86319" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86319-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osmium is developed on Linux and while there have been reports of people compiling it on Windows there's no ready-made binary that I know of that you could just use.</p>
<p>Instead, try using the Java-based "osmosis" which can also cut out polygons from OSM files (or merge two OSM files if you'd rather download the two small files from Geofabrik and combine them), or alternatively use "osmconvert" (<a href="https://wiki.openstreetmap.org/wiki/Osmconvert)">https://wiki.openstreetmap.org/wiki/Osmconvert)</a> which has a ready-made executable for Windows.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '22, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '22, 13:56</strong> </span></p>
</div>
</div>
<div id="comments-container-86319" class="comments-container">
<span id="86320"></span>
<div id="comment-86320" class="comment">
<div id="post-86320-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, Osmconvert is working well, thanks a lot !</p>
</div>
<div id="comment-86320-info" class="comment-info">
<span class="comment-age">(07 Dec '22, 15:48)</span> <span class="comment-user userinfo">JC_ULLES</span>
</div>
</div>
</div>
<div id="comment-tools-86319" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86319-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86321"></span>

<div id="answer-container-86321" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86321-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Other options for Osmium:</p>
<p><a href="https://learn.microsoft.com/en-us/windows/wsl/install">WSL</a>. Essentially this installs a Linux subsystem within Windows, which works surprisingly well.</p>
<p><a href="https://en.wikipedia.org/wiki/Docker_(software)">Docker</a> et al.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '22, 21:30</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-86321" class="comments-container">
&#10;</div>
<div id="comment-tools-86321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86321-form-container" class="comment-form-container">
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

