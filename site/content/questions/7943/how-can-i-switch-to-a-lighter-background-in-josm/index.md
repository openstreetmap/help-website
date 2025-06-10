+++
type = "question"
title = "How can I switch to a lighter background in JOSM?"
description = '''I tested JOSM for editing OpenStreetMap data. But the application has a black background and I would prefer a white or at least lighter background. Is there any setting where I can change to a white or lighter background (and the other colors)?'''
date = "2011-09-16T16:11:00Z"
lastmod = "2013-02-20T03:12:00Z"
weight = 7943
keywords = [ "josm", "colors" ]
aliases = [ "/questions/7943" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How can I switch to a lighter background in JOSM?](/questions/7943/how-can-i-switch-to-a-lighter-background-in-josm)

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
<span id="post-7943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7943-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I tested JOSM for editing OpenStreetMap data. But the application has a black background and I would prefer a white or at least lighter background. Is there any setting where I can change to a white or lighter background (and the other colors)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-colors" rel="tag" title="see questions tagged &#39;colors&#39;">colors</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '11, 16:11</strong></p>
<img src="https://secure.gravatar.com/avatar/b1d217a3a6e04cf4654372068beef20d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonas_&#39;s gravatar image" />
<p><span>Jonas_</span><br />
<span class="score" title="662 reputation points">662</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonas_ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7943" class="comments-container">
&#10;</div>
<div id="comment-tools-7943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7943-form-container" class="comment-form-container">
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

<span id="7944"></span>

<div id="answer-container-7944" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7944-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-7944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jonas_ has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Edit -&gt; Preferences -&gt; Display Settings -&gt; Colors tab -&gt; "background" table entry. Or, add a line with</p>
<pre><code> color.background=#ffffff</code></pre>
<p>to your <code>.josm/preferences</code> file. Changing the background might not be sufficient though; many other colours would probably have to be changed too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '11, 16:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-7944" class="comments-container">
<span id="7945"></span>
<div id="comment-7945" class="comment">
<div id="post-7945-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>JOSM now also supports MapCSS, so you can customise the appearance of the map that way. The latest builds come with the Potlatch 2 stylesheet.</p>
</div>
<div id="comment-7945-info" class="comment-info">
<span class="comment-age">(16 Sep '11, 16:51)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
<span id="7979"></span>
<div id="comment-7979" class="comment">
<div id="post-7979-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks! But it had been nice if JOSM had a built-in light color theme, so users could switch to that if needed (e.g. for usability).</p>
</div>
<div id="comment-7979-info" class="comment-info">
<span class="comment-age">(18 Sep '11, 17:58)</span> <span class="comment-user userinfo">Jonas_</span>
</div>
</div>
</div>
<div id="comment-tools-7944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7944-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20052"></span>

<div id="answer-container-20052" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20052-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can only change JOSM background, not that of a layer (an application on a server). But you may be able to request the server a transparent layer. If all the layers are transparent, the JOSM background is visible.<br />
A gray OSM background fairly fits layers made for white or black backgrounds.<br />
change Edit&gt;Preferences&gt;Display Settings&gt;Colors tab&gt;"background"<br />
or alternatively, create a style file ~/.josm/my_style.mapcss containing the following,<br />
Edit&gt;Preferences&gt;Map Projection&gt;Map Paint styles&gt; add and select this file<br />
control styles with with Windows&gt;Map paint styles<br />
"node" entry is to control the node appearances according to zoom level<br />
more <a href="http://josm.openstreetmap.de/wiki/Styles">styles</a> are <a href="http://josm.openstreetmap.de/wiki/Help/Styles/MapCSSImplementation">available here</a></p>
<pre><code>canvas {
    background-color: #202020;
    default-points: true;
    default-lines: true;
}
&#10;node|z1-16
  { symbol-shape: square; symbol-fill-opacity: 0; symbol-size: 1; z-index:-1}
&#10;node|z17-
  { symbol-shape: square; symbol-stroke-color: navy; symbol-fill-color: rosybrown; symbol-size:8;  z-index:1}</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '13, 03:12</strong></p>
<img src="https://secure.gravatar.com/avatar/22d0547d929d81aa90014a6f0aef484a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GentilPapou&#39;s gravatar image" />
<p><span>GentilPapou</span><br />
<span class="score" title="160 reputation points">160</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GentilPapou has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Feb '13, 03:39</strong> </span></p>
</div>
</div>
<div id="comments-container-20052" class="comments-container">
&#10;</div>
<div id="comment-tools-20052" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20052-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11063"></span>

<div id="answer-container-11063" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11063-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I meet the case where all layers are transparent and one uses black, hence invisible, lines. I suppose it's possible to have a blank layer serve as non-black background. Unfortunately, the blank layer is black too. Is there a way to configure and save a non-black blank layer? How does one save a set of layers to be reloaded at startup? Please explain with enough details. Thanks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '12, 01:00</strong></p>
<img src="https://secure.gravatar.com/avatar/22d0547d929d81aa90014a6f0aef484a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GentilPapou&#39;s gravatar image" />
<p><span>GentilPapou</span><br />
<span class="score" title="160 reputation points">160</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GentilPapou has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-11063" class="comments-container">
&#10;</div>
<div id="comment-tools-11063" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11063-form-container" class="comment-form-container">
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

