+++
type = "question"
title = "JOSM mapcss, combine files into one, possible?"
description = '''When you have several mapcss files, you do not want to copy/paste it into one file. Can I make one file with all the url of the all these mapcss files in a particularly order. Can this work? mapcss url access.mapcss url vehicle.mapcss url foot.mapcss  How? '''
date = "2017-07-27T12:01:00Z"
lastmod = "2017-08-01T10:07:00Z"
weight = 57308
keywords = [ "josm", "mapcss" ]
aliases = [ "/questions/57308" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM mapcss, combine files into one, possible?](/questions/57308/josm-mapcss-combine-files-into-one-possible)

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
<span id="post-57308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57308-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When you have several mapcss files, you do not want to copy/paste it into one file. Can I make one file with all the url of the all these mapcss files in a particularly order.</p>
<p>Can this work?</p>
<pre><code>mapcss
url access.mapcss
url vehicle.mapcss
url foot.mapcss</code></pre>
<p>How?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-mapcss" rel="tag" title="see questions tagged &#39;mapcss&#39;">mapcss</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '17, 12:01</strong></p>
<img src="https://secure.gravatar.com/avatar/6c5dc0fc3be6786b643d15ec99ba3e3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Allroads&#39;s gravatar image" />
<p><span>Allroads</span><br />
<span class="score" title="222 reputation points">222</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Allroads has one accepted answer">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jul '17, 12:02</strong> </span></p>
</div>
</div>
<div id="comments-container-57308" class="comments-container">
&#10;</div>
<div id="comment-tools-57308" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57308-form-container" class="comment-form-container">
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

<span id="57404"></span>

<div id="answer-container-57404" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57404-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57404-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57404-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As maxerickson already pointed out JOSM does not support @import. But you can use the awk command line tool to do that in a compilation-like step. (If your styles use icons, you might already distribute them as ZIP files).</p>
<p>See the <a href="https://github.com/OpenRailwayMap/OpenRailwayMap/blob/master/styles/Makefile#L16">makefile of OpenRailwayMap</a> for further information. It executes an awk script which replaces the line</p>
<pre><code>@import url(&#39;myFunnyFilename.mapcss&#39;);</code></pre>
<p>by the content of myFunnyFilename.mapcss.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '17, 10:07</strong></p>
<img src="https://secure.gravatar.com/avatar/d2a3b905e2632430b47dd9b8de3d8ba0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nakaner&#39;s gravatar image" />
<p><span>Nakaner</span><br />
<span class="score" title="610 reputation points">610</span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nakaner has 3 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-57404" class="comments-container">
&#10;</div>
<div id="comment-tools-57404" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57404-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="57318"></span>

<div id="answer-container-57318" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57318-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No. See the comment about @import at <a href="https://josm.openstreetmap.de/wiki/Help/Styles/MapCSSImplementation#Compatibilitynotes">https://josm.openstreetmap.de/wiki/Help/Styles/MapCSSImplementation#Compatibilitynotes</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '17, 19:05</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-57318" class="comments-container">
<span id="57319"></span>
<div id="comment-57319" class="comment">
<div id="post-57319-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks such short sentence and to understand what it means. •no @import</p>
</div>
<div id="comment-57319-info" class="comment-info">
<span class="comment-age">(27 Jul '17, 19:18)</span> <span class="comment-user userinfo">Allroads</span>
</div>
</div>
</div>
<div id="comment-tools-57318" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57318-form-container" class="comment-form-container">
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

