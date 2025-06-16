+++
type = "question"
title = "adding admin boundaries and multipolygons the fast way?"
description = '''I have a shapefile with Georgia&#x27;s admin boundaries (districts, regions and so on). It is Open Source. How can I add it to the database the easy way? I transformed some boundaries to ways in merkaator, uploaded them, then made changes in podlatch2 (admin_level, adding multipolygons and so on). But af...'''
date = "2012-01-29T12:00:00Z"
lastmod = "2012-01-30T20:16:00Z"
weight = 10311
keywords = [ "boundaries", "admin_boundary", "multipolygon" ]
aliases = [ "/questions/10311" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [adding admin boundaries and multipolygons the fast way?](/questions/10311/adding-admin-boundaries-and-multipolygons-the-fast-way)

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
<span id="post-10311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10311-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a shapefile with Georgia's admin boundaries (districts, regions and so on). It is Open Source.</p>
<p>How can I add it to the database the easy way? I transformed some boundaries to ways in merkaator, uploaded them, then made changes in podlatch2 (admin_level, adding multipolygons and so on). But after some time, I cannot "load the map" anymore. That makes editing very cumbersome.</p>
<p>I have now several unfinished multipolygons and it is quite annoying.</p>
<p>Maybe someone can help me to import the ways, and then I will edit them myself? Or any other suggestions what to do?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '12, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/139902838ec4406143a7d9f286419a52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moszkva%20ter&#39;s gravatar image" />
<p><span>moszkva ter</span><br />
<span class="score" title="2125 reputation points"><span>2.1k</span></span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moszkva ter has 8 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-10311" class="comments-container">
&#10;</div>
<div id="comment-tools-10311" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10311-form-container" class="comment-form-container">
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

<span id="10312"></span>

<div id="answer-container-10312" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10312-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Imports should be done with special accounts (one account per import). Usually a script is created to import the data.<br />
</p>
<p>Since you do it manually the problem with loading map (if you work in Potlatch as you mentioned) is probably that you downloaded too much data. You have to wait some time before you are allowed to download more or access the API from a different IP address.<br />
If your data is accurate and you will manually edit it later you can upload them without downloading the whole area and then download only the important places to connect them to existing boundaries or to remove any duplicated data or other problems. For editing of relations and other more complicated features I recommend using JOSM with relation toolbox plugin. It makes your life a lot easier.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '12, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></br></p>
</div>
</div>
<div id="comments-container-10312" class="comments-container">
<span id="10342"></span>
<div id="comment-10342" class="comment">
<div id="post-10342-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>... and have a detailed look at <a href="https://wiki.openstreetmap.org/wiki/Import">https://wiki.openstreetmap.org/wiki/Import</a> and all sub pages.</p>
</div>
<div id="comment-10342-info" class="comment-info">
<span class="comment-age">(30 Jan '12, 18:08)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="10348"></span>
<div id="comment-10348" class="comment">
<div id="post-10348-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer and the tip! I am so free to answer my own question. Not because I want to show how great I am ;) But it might be helpful for other users who face the same deed.</p>
</div>
<div id="comment-10348-info" class="comment-info">
<span class="comment-age">(30 Jan '12, 20:15)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
</div>
<div id="comment-tools-10312" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10312-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10349"></span>

<div id="answer-container-10349" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10349-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Actually, now I use Merkaator. I follow the border sections manually, the programme is snapping me to the shapefile's nodes, so editing is a breeze. There, I am also adding all attributes to the relations.</p>
<p>After it, I am manually editing and checking the intersections in Podlatch2, and add the relations to already existing borders (i.e. international borders).</p>
<p>Then I use this site to check if I did not make any mistakes: <a href="http://analyser.openstreetmap.fr/cgi-bin/index.py">http://analyser.openstreetmap.fr/cgi-bin/index.py</a></p>
<p>after some practice, it goes quite fast. Automatic import with cleanup afterwards would take approximately the same time, I guess...</p>
<p>So, check out Georgia and wait for admin_level 4 and 6 to be rendered ;)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '12, 20:16</strong></p>
<img src="https://secure.gravatar.com/avatar/139902838ec4406143a7d9f286419a52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moszkva%20ter&#39;s gravatar image" />
<p><span>moszkva ter</span><br />
<span class="score" title="2125 reputation points"><span>2.1k</span></span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moszkva ter has 8 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-10349" class="comments-container">
&#10;</div>
<div id="comment-tools-10349" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10349-form-container" class="comment-form-container">
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

