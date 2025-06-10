+++
type = "question"
title = "Maperitive - Problem for exporting to SVG (access denied)"
description = '''Hello,  I&#x27;m using Maperitive through Parallels Desktop. When I want to export the map into a SVG file, the export fails :  &amp;gt; export-svg compatibility=illustrator  Preparing the SVG...  Access to the path &#x27;C:&#92;Windows&#92;output&#x27; is denied. Do you know what can I do against this problem ? How can I red...'''
date = "2012-11-27T15:45:00Z"
lastmod = "2012-11-29T13:56:00Z"
weight = 18031
keywords = [ "svg", "export", "parallels", "maperitive", "desktop" ]
aliases = [ "/questions/18031" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Maperitive - Problem for exporting to SVG (access denied)](/questions/18031/maperitive-problem-for-exporting-to-svg-access-denied)

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
<span id="post-18031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18031-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm using <span>Maperitive</span> through Parallels Desktop. When I want to export the map into a SVG file, the export fails :</p>
<p><strong>&gt; export-svg compatibility=illustrator Preparing the SVG... Access to the path 'C:\Windows\output' is denied.</strong></p>
<p>Do you know what can I do against this problem ? How can I redefine the path ?</p>
<p>Thanks a lot</p>
<p>Antoine</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-parallels" rel="tag" title="see questions tagged &#39;parallels&#39;">parallels</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span> <span class="post-tag tag-link-desktop" rel="tag" title="see questions tagged &#39;desktop&#39;">desktop</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Nov '12, 15:45</strong></p>
<img src="https://secure.gravatar.com/avatar/8c7680a6eb0c648643862f24ae87132e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cosmicgarden&#39;s gravatar image" />
<p><span>Cosmicgarden</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cosmicgarden has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Apr '13, 00:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-18031" class="comments-container">
&#10;</div>
<div id="comment-tools-18031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18031-form-container" class="comment-form-container">
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

<span id="18036"></span>

<div id="answer-container-18036" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18036-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-18036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know about Parallels Desktop, but it looks like Maperitive is running in C:\Windows as the default working directory, and that is a protected directory under Windows. export-svg command generates SVG files inside output directory of the current working dir.</p>
<p>I suggest using the <a href="http://maperitive.net/docs/Commands/ChangeDirectory.html">change-dir command</a> to move to somewhere else or specifying the output file explicitly int the <a href="http://maperitive.net/docs/Commands/ExportSvg.html">export-svg command</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Nov '12, 17:41</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-18036" class="comments-container">
<span id="18097"></span>
<div id="comment-18097" class="comment">
<div id="post-18097-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hi Breki,</p>
<p>Thanks a lot for your quick answer. The advice you suggested worked well !</p>
<p>Best,</p>
<p>Antoine</p>
</div>
<div id="comment-18097-info" class="comment-info">
<span class="comment-age">(29 Nov '12, 13:56)</span> <span class="comment-user userinfo">Cosmicgarden</span>
</div>
</div>
</div>
<div id="comment-tools-18036" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18036-form-container" class="comment-form-container">
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

