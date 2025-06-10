+++
type = "question"
title = "placex not all elements in map osm"
description = '''Hi all I install nominatim in a pc, with import osm dat with roads. The &quot;placex&quot; has less elements with a &quot;place&quot;, it&#x27;s like random elements loaded. Is it possible to allow placex load all elements, is possible change config of nominatim? thank you very much for your attention '''
date = "2013-11-01T19:47:00Z"
lastmod = "2013-11-15T17:31:00Z"
weight = 27700
keywords = [ "index", "nominatim", "placex" ]
aliases = [ "/questions/27700" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [placex not all elements in map osm](/questions/27700/placex-not-all-elements-in-map-osm)

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
<span id="post-27700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27700-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all</p>
<p>I install nominatim in a pc, with import osm dat with roads.</p>
<p>The "placex" has less elements with a "place", it's like random elements loaded.</p>
<p>Is it possible to allow placex load all elements, is possible change config of nominatim?</p>
<p>thank you very much for your attention</p>
<p><img src="http://help.openstreetmap.org/upfiles/screenshot_2.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-index" rel="tag" title="see questions tagged &#39;index&#39;">index</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-placex" rel="tag" title="see questions tagged &#39;placex&#39;">placex</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Nov '13, 19:47</strong></p>
<img src="https://secure.gravatar.com/avatar/8151a2cd9f1041f10b62d8ca446d3b2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alveniz&#39;s gravatar image" />
<p><span>alveniz</span><br />
<span class="score" title="51 reputation points">51</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alveniz has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-27700" class="comments-container">
&#10;</div>
<div id="comment-tools-27700" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27700-form-container" class="comment-form-container">
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

<span id="27755"></span>

<div id="answer-container-27755" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27755-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Nominatim database schema is optimised for Nominatim use. The contents of place/placex are an internal implementation detail. If you want a generic database import that you can use for other purposes than running Nomiatim on it, try a manual <a href="http://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a> import (or try <a href="http://wiki.openstreetmap.org/wiki/Imposm">imposm).</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '13, 21:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-27755" class="comments-container">
&#10;</div>
<div id="comment-tools-27755" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27755-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28138"></span>

<div id="answer-container-28138" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28138-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, solution a problem indexed in: <a href="https://help.openstreetmap.org/questions/13870/different-result-of-nominatim-on-my-server-while-comparing-with-original?page=1&amp;focusedAnswerId=28137#28137">https://help.openstreetmap.org/questions/13870/different-result-of-nominatim-on-my-server-while-comparing-with-original?page=1&amp;focusedAnswerId=28137#28137</a></p>
<p>Gracias</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '13, 17:31</strong></p>
<img src="https://secure.gravatar.com/avatar/8151a2cd9f1041f10b62d8ca446d3b2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alveniz&#39;s gravatar image" />
<p><span>alveniz</span><br />
<span class="score" title="51 reputation points">51</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alveniz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28138" class="comments-container">
&#10;</div>
<div id="comment-tools-28138" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28138-form-container" class="comment-form-container">
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

