+++
type = "question"
title = "How to convert .osm to .shp files?"
description = '''I have used a soft called osm2shp, but when I converting, some bugs popup, so I need an effective way to solve the problem.I will be grateful for your help!'''
date = "2012-01-03T06:46:00Z"
lastmod = "2012-01-03T21:48:00Z"
weight = 9759
keywords = [ ".shp" ]
aliases = [ "/questions/9759" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to convert .osm to .shp files?](/questions/9759/how-to-convert-osm-to-shp-files)

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
<span id="post-9759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9759-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have used a soft called osm2shp, but when I converting, some bugs popup, so I need an effective way to solve the problem.I will be grateful for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-.shp" rel="tag" title="see questions tagged &#39;.shp&#39;">.shp</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jan '12, 06:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f37df82f57e7fda9991c18fa6c7a9158?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Silian1988&#39;s gravatar image" />
<p><span>Silian1988</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Silian1988 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9759" class="comments-container">
<span id="9764"></span>
<div id="comment-9764" class="comment">
<div id="post-9764-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Please explain what you mean by "some bugs popup". What input files did you try to process, what was the expected outcome, and what did you get instead?</p>
</div>
<div id="comment-9764-info" class="comment-info">
<span class="comment-age">(03 Jan '12, 08:38)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="9779"></span>
<div id="comment-9779" class="comment">
<div id="post-9779-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To Frederik Ramm, I'm sorry I didn't explain my question clearly. I want to get the world map of shape files(.shp), but now I only have OSM file(.osm format), I have used a soft called OSM2SHP,but when I converting, a dialog saying “Exception of type 'System.OutOfMemoryException' was thrown.” pops up, the system I used is windows xp.</p>
</div>
<div id="comment-9779-info" class="comment-info">
<span class="comment-age">(03 Jan '12, 15:11)</span> <span class="comment-user userinfo">Silian1988</span>
</div>
</div>
</div>
<div id="comment-tools-9759" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9759-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="9780"></span>

<div id="answer-container-9780" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9780-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For the first there are several programs named osm2shp. I do not know what you have problems with. There is an overview of different programs on <a href="https://wiki.openstreetmap.org/wiki/Shapefiles">the wiki</a>.</p>
<p>The error message <em>System.OutOfMemoryException</em> indicates that this is a <em>.net</em> application. You may find information on how to resolve it by <a href="https://duckduckgo.com/?q=System.OutOfMemoryException">searching</a> the error. Or try another application based on a better framework.</p>
<p>Whenever you are working with big amounts of data like the planet file, you are going to use a lot of memmory. Use a computer with enough memmory and a 64-bit address space.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '12, 17:25</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-9780" class="comments-container">
&#10;</div>
<div id="comment-tools-9780" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9780-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9786"></span>

<div id="answer-container-9786" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9786-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try using QGIS - Just import osm file using OpenStreetMap plugin (which comes with the default QGIS software).</p>
<p>Then left click the layers and save as shp files.</p>
<p>The only problem I've found is that some tags I think are truncated to 256 characters I think. But most tags aren't this long anyway.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '12, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/aefd12236ce046b3929cb63fca818119?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hawkeye&#39;s gravatar image" />
<p><span>Hawkeye</span><br />
<span class="score" title="241 reputation points">241</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hawkeye has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9786" class="comments-container">
&#10;</div>
<div id="comment-tools-9786" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9786-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9781"></span>

<div id="answer-container-9781" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9781-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm guessing (from the .NET error) that you're using the Google Code <a href="http://code.google.com/p/osm2shp/">osm2shp</a> and (from the fact that you're running Windows XP) that you haven't got much memory on your PC. The <a href="https://wiki.openstreetmap.org/wiki/Shapefiles#Making_shapefiles_from_OpenStreetMap_data">page</a> that <a href="https://help.openstreetmap.org/users/131/gnonthgol">Gnonthgol</a> referred to describes several alternatives - I'd read up about those and use one of them instead (at least one seems to support a temporary local database rather than in-memory storage which might be better for you).</p>
<p>You'll also probably need to think about what features you want in the resulting shapefiles, and try a small area first.</p>
<p>One final question - have you checked that the zipped shapefiles that are available for areas from e.g. <a href="http://download.geofabrik.de/osm/">here</a> don't do what you want?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '12, 18:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-9781" class="comments-container">
&#10;</div>
<div id="comment-tools-9781" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9781-form-container" class="comment-form-container">
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

