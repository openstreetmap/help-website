+++
type = "question"
title = "How to get bots to fix things?"
description = '''Hey! I regularly find geometry in the map that has problems. How do I submit this geometry problem to get fixed by &#x27;bot? I realize someone has to write code to fix it, but if they don&#x27;t know about the problems, how will it ever get fixed? For instance:  https://www.openstreetmap.org/browse/way/231196...'''
date = "2010-07-10T21:55:00Z"
lastmod = "2010-07-11T21:39:00Z"
weight = 67
keywords = [ "geometry", "bot", "topology" ]
aliases = [ "/questions/67" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to get bots to fix things?](/questions/67/how-to-get-bots-to-fix-things)

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
<span id="post-67-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey!</p>
<p>I regularly find geometry in the map that has problems. How do I submit this geometry problem to get fixed by 'bot? I realize someone has to write code to fix it, but if they don't know about the problems, how will it ever get fixed?</p>
<p>For instance:</p>
<ul>
<li><a href="https://www.openstreetmap.org/browse/way/23119666"></a><a href="https://www.openstreetmap.org/browse/way/23119666"></a><a href="https://www.openstreetmap.org/browse/way/23119666">https://www.openstreetmap.org/browse/way/23119666</a></li>
<li>this way is self overlapping about 100 times.</li>
<li><a href="https://www.openstreetmap.org/browse/way/35354717"></a><a href="https://www.openstreetmap.org/browse/way/35354717"></a><a href="https://www.openstreetmap.org/browse/way/35354717">https://www.openstreetmap.org/browse/way/35354717</a></li>
<li>this way is self overlapping and should be cut into an outer/inner relation.</li>
<li><a href="https://www.openstreetmap.org/browse/way/35915907"></a><a href="https://www.openstreetmap.org/browse/way/35915907"></a><a href="https://www.openstreetmap.org/browse/way/35915907">https://www.openstreetmap.org/browse/way/35915907</a></li>
<li>this way crosses itself</li>
</ul>
<p>These are all fixable problems but I don't know how to write the bots to fix them. Where do I submit these issues?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geometry" rel="tag" title="see questions tagged &#39;geometry&#39;">geometry</span> <span class="post-tag tag-link-bot" rel="tag" title="see questions tagged &#39;bot&#39;">bot</span> <span class="post-tag tag-link-topology" rel="tag" title="see questions tagged &#39;topology&#39;">topology</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '10, 21:55</strong></p>
<img src="https://secure.gravatar.com/avatar/fcd603a0c14084fdd781fc5a925d6d7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jharvey&#39;s gravatar image" />
<p><span>jharvey</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jharvey has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67" class="comments-container">
&#10;</div>
<div id="comment-tools-67" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67-form-container" class="comment-form-container">
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

<span id="69"></span>

<div id="answer-container-69" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69-score" class="post-score" title="current number of votes">
14
</div>
<span id="post-69-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Automated edits have a great potential to screw things up very fast and very thoroughly. Therefore bots are not universally liked in the community. At the moment issues like the ones you present are mostly handled by websites finding and listing such errors and giving mappers easy access to them to fix them manually.</p>
<p>On the other hand, simpler mistakes like trailing or leading whitespace are fixed by bots. When ever a new bot is created it should be extensively tested against the API on the development server and the bot should be announced on suitable mailing lists as well as documented in the wiki.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '10, 22:02</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-69" class="comments-container">
&#10;</div>
<div id="comment-tools-69" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="98"></span>

<div id="answer-container-98" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-98-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-98-score" class="post-score" title="current number of votes">
12
</div>
<span id="post-98-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>the problems you discovered are quite easy to detect by a computer. Sites like <a href="http://keepright.ipax.at/"></a><a href="http://keepright.ipax.at/"></a><a href="http://keepright.ipax.at/">http://keepright.ipax.at/</a> or the <a href="http://tools.geofabrik.de/osmi/"></a><a href="http://tools.geofabrik.de/osmi/"></a><a href="http://tools.geofabrik.de/osmi/">http://tools.geofabrik.de/osmi/</a> help to detect those problems.</p>
<p>Writing a bot is a lot more difficult. There is no 100% right way for example to fix a self-intersecting way. Sometimes a node might have moved by accident. Other times the user connected ways that should not be connected. It needs a human to review these issues and choose the appropriate fix.</p>
<p>What you should do is to open these places in your editor and fix them (as long as it's obvious what is wrong).</p>
<p>In case you can't fix the situation without knowing the place in reality, then don't fix it.</p>
<p>You could file a report with OpenStreetBugs, but as other users can also use keepright or OSM Inspector it's not needed to duplicate the problem report. Just wait some time. That's how OSM is working, some user passes by that problem, knowing the situation and fixes it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '10, 20:37</strong></p>
<img src="https://secure.gravatar.com/avatar/09b2b8d17e144e0bf320379096429046?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stephan%20Knauss&#39;s gravatar image" />
<p><span>Stephan Knauss</span><br />
<span class="score" title="450 reputation points">450</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stephan Knauss has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-98" class="comments-container">
&#10;</div>
<div id="comment-tools-98" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-98-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="101"></span>

<div id="answer-container-101" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-101-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I doubt any user would intentionally introduce such an error. Its most likely an editor issue. To reduce errors like these to appear in the first place, it could be worth investigating how it happened. In the case with <a href="https://www.openstreetmap.org/browse/way/23119666">way 23119666</a>, you can see by the history that the error was introduced using the potlatch editor. Potlatch has as a "smoothing" function for straight roads and circles when you press 'T'. If you try to "smooth" a concave (shape of C) closed way, the function takes a 'crazy pill' and attempts to rectify this by creating "extra" loops of nodes. <a href="http://trac.openstreetmap.org/ticket/2489">The bug</a> has already been submitted to trac.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '10, 21:39</strong></p>
<img src="https://secure.gravatar.com/avatar/3a81ab306b6fa802db48cec4e8813c6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormur&#39;s gravatar image" />
<p><span>gormur</span><br />
<span class="score" title="100 reputation points">100</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormur has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Feb '11, 16:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span></p>
</div>
</div>
<div id="comments-container-101" class="comments-container">
&#10;</div>
<div id="comment-tools-101" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-101-form-container" class="comment-form-container">
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

