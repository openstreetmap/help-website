+++
type = "question"
title = "Color road with slope gradient overlay"
description = '''Hello I would like to know if it is possible from OSM to create a map with road (not track) with a gradient color about how much the slop is. For example: color from 3% to 20% per 20m. I live in a place where it is very flat and I am looking to train more for climbing montain on my bike. I know few ...'''
date = "2022-05-16T09:29:00Z"
lastmod = "2022-05-16T22:47:00Z"
weight = 84488
keywords = [ "gradient", "style", "incline" ]
aliases = [ "/questions/84488" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Color road with slope gradient overlay](/questions/84488/color-road-with-slope-gradient-overlay)

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
<span id="post-84488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84488-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>I would like to know if it is possible from OSM to create a map with road (not track) with a gradient color about how much the slop is. For example: color from 3% to 20% per 20m.</p>
<p>I live in a place where it is very flat and I am looking to train more for climbing montain on my bike. I know few climb but I want to discover more.</p>
<p>I would love to have all road colored like this for example: <a href="https://help.locusmap.eu/public/attachments/54070186b043d0995b7137703d3b6e3f.png">https://help.locusmap.eu/public/attachments/54070186b043d0995b7137703d3b6e3f.png</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gradient" rel="tag" title="see questions tagged &#39;gradient&#39;">gradient</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-incline" rel="tag" title="see questions tagged &#39;incline&#39;">incline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 May '22, 09:29</strong></p>
<img src="https://secure.gravatar.com/avatar/55ac6839744d55b7067da8b212609f40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n3b&#39;s gravatar image" />
<p><span>n3b</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n3b has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 May '22, 10:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-84488" class="comments-container">
<span id="84489"></span>
<div id="comment-84489" class="comment">
<div id="post-84489-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you have access to the slope data or are you hoping to infer it from elsewhere? <a href="https://www.openstreetmap.org/way/232211240">https://www.openstreetmap.org/way/232211240</a> looks like one of your roads and it appears that the slope information isn't in OSM.</p>
</div>
<div id="comment-84489-info" class="comment-info">
<span class="comment-age">(16 May '22, 09:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="84491"></span>
<div id="comment-84491" class="comment">
<div id="post-84491-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I though OSM have elevation data :/ Maybe instead do something base on <a href="https://wiki.openstreetmap.org/wiki/Key:incline">https://wiki.openstreetmap.org/wiki/Key:incline</a> ?</p>
</div>
<div id="comment-84491-info" class="comment-info">
<span class="comment-age">(16 May '22, 11:00)</span> <span class="comment-user userinfo">n3b</span>
</div>
</div>
<span id="84492"></span>
<div id="comment-84492" class="comment">
<div id="post-84492-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>OSM doesn't have elevation data. The <code>incline</code> tag and similar is rarely used. You almost certainly want to look at SRTM or one of its many derivatives.</p>
</div>
<div id="comment-84492-info" class="comment-info">
<span class="comment-age">(16 May '22, 11:03)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84488-form-container" class="comment-form-container">
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

<span id="84495"></span>

<div id="answer-container-84495" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84495-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looks like other people have tried that before. E.g. <a href="https://ropensci.github.io/slopes/articles/roadnetworkcycling.html">https://ropensci.github.io/slopes/articles/roadnetworkcycling.html</a> looks like a comprehensive guide how to accomplish your task.</p>
<p>(I haven't tried it myself. Just found it by googling)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '22, 22:47</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-84495" class="comments-container">
&#10;</div>
<div id="comment-tools-84495" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84495-form-container" class="comment-form-container">
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

