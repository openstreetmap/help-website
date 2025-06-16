+++
type = "question"
title = "export or generate XML file to import in Maperitive"
description = '''I opened in www.openstreetmap a map,selected a custom part and selected export. I did not find the option to preselect XML output. The example on https://wiki.openstreetmap.org/wiki/Export shows the option in the left sided part of the screenshot which does not pop-up on my system. What happens is th...'''
date = "2013-08-13T22:52:00Z"
lastmod = "2013-08-15T10:34:00Z"
weight = 25342
keywords = [ "xml", "maperitive", "export", "generate" ]
aliases = [ "/questions/25342" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [export or generate XML file to import in Maperitive](/questions/25342/export-or-generate-xml-file-to-import-in-maperitive)

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
<span id="post-25342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25342-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I opened in www.openstreetmap a map,selected a custom part and selected export. I did not find the option to preselect XML output.</p>
<p>The example on <a href="https://wiki.openstreetmap.org/wiki/Export">https://wiki.openstreetmap.org/wiki/Export</a> shows the option in the left sided part of the screenshot which does not pop-up on my system.</p>
<p>What happens is that my browser opens with <a href="http://api.openstreetmap.org/api/0.6/map?bbox=4.6297,51.9346,4.743,52.0031.">http://api.openstreetmap.org/api/0.6/map?bbox=4.6297,51.9346,4.743,52.0031.</a> Nothing happens anymore.</p>
<p>What did I do wrong? Please advise me for a remedy.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-generate" rel="tag" title="see questions tagged &#39;generate&#39;">generate</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '13, 22:52</strong></p>
<img src="https://secure.gravatar.com/avatar/972abfdf2050bb9ea7be5cd3f5f1489b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Goudkust&#39;s gravatar image" />
<p><span>Goudkust</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Goudkust has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25342" class="comments-container">
&#10;</div>
<div id="comment-tools-25342" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25342-form-container" class="comment-form-container">
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

<span id="25356"></span>

<div id="answer-container-25356" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25356-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25356-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-25356-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please use a read-only mirror, for example <a href="http://overpass-api.de/api/map?bbox=4.6297,51.9346,4.743,52.0031">http://overpass-api.de/api/map?bbox=4.6297,51.9346,4.743,52.0031</a> The download then takes around 30 seconds.</p>
<p>Read-only mirrors deliver the same data like the main API, but are optimized for larger downloads, while the main API is geared towards performant editing.</p>
<p>Your region contains about 134'000 elements, and the export tab of the main API only allows up to 50'000 elements.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '13, 08:10</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Aug '13, 08:16</strong> </span></p>
</div>
</div>
<div id="comments-container-25356" class="comments-container">
&#10;</div>
<div id="comment-tools-25356" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25356-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25343"></span>

<div id="answer-container-25343" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25343-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See question <a href="/questions/25303/howwhere-to-download-osm-file-on-the-website?page=1&amp;focusedAnswerId=25305#25305">How/where to download osm file on the website.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '13, 23:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-25343" class="comments-container">
<span id="25385"></span>
<div id="comment-25385" class="comment">
<div id="post-25385-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have to produce a simple map for a 1-2 hour walking trail to include in a booklet. Maperitive looks fine to do With your solution I could download the file. Maperitive does not recognize this file as XML</p>
<p>What did I do wrong? Solutions are often simple, when you know the clue.</p>
<p>Peter.</p>
</div>
<div id="comment-25385-info" class="comment-info">
<span class="comment-age">(14 Aug '13, 19:59)</span> <span class="comment-user userinfo">Goudkust</span>
</div>
</div>
<span id="25410"></span>
<div id="comment-25410" class="comment">
<div id="post-25410-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>What is the filename of the file you downloaded and where exactly (please provide a link) did you get it? My guess is that you downloaded a compressed .osm.bz2 file from geofabrik, and need to unzip it with e.g. winrar or 7-zip so maperitive is able to read it.</p>
</div>
<div id="comment-25410-info" class="comment-info">
<span class="comment-age">(15 Aug '13, 10:34)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-25343" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25343-form-container" class="comment-form-container">
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

