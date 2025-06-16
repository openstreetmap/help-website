+++
type = "question"
title = "How does tilesAtHome (t@h) work?"
description = '''What is that tilesAtHome (t@h) system that provides the osmarender layer on the openstreetmap.org frontpage and how does it work?'''
date = "2010-07-07T13:29:00Z"
lastmod = "2010-09-13T22:28:00Z"
weight = 24
keywords = [ "newbie", "tah", "renderer" ]
aliases = [ "/questions/24" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How does tilesAtHome (t@h) work?](/questions/24/how-does-tilesathome-th-work)

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
<span id="post-24-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is that tilesAtHome (t@h) system that provides the osmarender layer on the <a href="http://openstreetmap.org">openstreetmap.org</a> frontpage and how does it work?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-tah" rel="tag" title="see questions tagged &#39;tah&#39;">tah</span> <span class="post-tag tag-link-renderer" rel="tag" title="see questions tagged &#39;renderer&#39;">renderer</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '10, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/278e1af65e82993efd0ba7bbbacf6435?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spaetz&#39;s gravatar image" />
<p><span>spaetz</span><br />
<span class="score" title="853 reputation points">853</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spaetz has 2 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-24" class="comments-container">
&#10;</div>
<div id="comment-tools-24" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24-form-container" class="comment-form-container">
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

<span id="26"></span>

<div id="answer-container-26" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-26-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="spaetz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A central server tracks tiles (a portion of the map consisting of PNG images for the different zoom levels) that need to be rerender. Client computers running the t@h software connect to the server and ask for a tile they should render. They then connect to a TRAPI server and download the map data for that tile. Using osmarender the map data is converted to a SVG image which is then rasterized using inskcape or batik. The rendered images are packed into a tileset and uploaded to the server where they are stored until someone wants to look at the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '10, 16:11</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-26" class="comments-container">
&#10;</div>
<div id="comment-tools-26" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="793"></span>

<div id="answer-container-793" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-793-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at the wiki <a href="https://wiki.openstreetmap.org/wiki/Tah"></a><a href="https://wiki.openstreetmap.org/wiki/Tah"></a><a href="https://wiki.openstreetmap.org/wiki/Tah">https://wiki.openstreetmap.org/wiki/Tah</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '10, 22:28</strong></p>
<img src="https://secure.gravatar.com/avatar/55d5ae1382a7ca891bfb18ebcbecdb60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HB9DTX&#39;s gravatar image" />
<p><span>HB9DTX</span><br />
<span class="score" title="15 reputation points">15</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HB9DTX has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-793" class="comments-container">
&#10;</div>
<div id="comment-tools-793" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-793-form-container" class="comment-form-container">
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

