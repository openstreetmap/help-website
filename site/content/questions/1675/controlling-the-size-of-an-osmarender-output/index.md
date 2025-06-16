+++
type = "question"
title = "Controlling the size of an Osmarender output"
description = '''I have exported a section of map from OSM, and wish to render it as an SVG to use with Inkscape. I am able to do that (though it takes &amp;gt;18 hours... :S), but the size of the map in Inkscape is too small (I want it to be 42&quot; x 42&quot;), but when I select all elements &amp;amp; re-scale them, not everything...'''
date = "2010-11-29T20:00:00Z"
lastmod = "2010-12-19T20:32:00Z"
weight = 1675
keywords = [ "osmarender" ]
aliases = [ "/questions/1675" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Controlling the size of an Osmarender output](/questions/1675/controlling-the-size-of-an-osmarender-output)

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
<span id="post-1675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1675-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have exported a section of map from OSM, and wish to render it as an SVG to use with Inkscape. I am able to do that (though it takes &gt;18 hours... :S), but the size of the map in Inkscape is too small (I want it to be 42" x 42"), but when I select all elements &amp; re-scale them, not everything gets selected / rescaled for some reason.</p>
<p>I was wondering if there is a direct way to make Osmarender make a 42" map out of the source file?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmarender" rel="tag" title="see questions tagged &#39;osmarender&#39;">osmarender</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Nov '10, 20:00</strong></p>
<img src="https://secure.gravatar.com/avatar/2aa9ceb65e360dff3c683b0c721fa2e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rrands1&#39;s gravatar image" />
<p><span>rrands1</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rrands1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Dec '10, 10:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-1675" class="comments-container">
&#10;</div>
<div id="comment-tools-1675" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1675-form-container" class="comment-form-container">
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

<span id="1866"></span>

<div id="answer-container-1866" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1866-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You might want to check out the <code>scale</code> and <code>symbolScale</code> option at the start of the rule file. You also might want to change the font sizes inside the rule file. See <a href="https://wiki.openstreetmap.org/wiki/Osmarender"></a><a href="https://wiki.openstreetmap.org/wiki/Osmarender"></a><a href="https://wiki.openstreetmap.org/wiki/Osmarender">https://wiki.openstreetmap.org/wiki/Osmarender</a> for documentation on osmarender.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '10, 20:32</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Dec '10, 10:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-1866" class="comments-container">
&#10;</div>
<div id="comment-tools-1866" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1866-form-container" class="comment-form-container">
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

