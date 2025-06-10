+++
type = "question"
title = "Find total length of ways within a region, in Overpass Turbo"
description = '''For example, I can run the Wizard query in Overpass Turbo: &quot;highway=motorway AND oneway=yes in Chugoku&quot; which gives me all the dual-carriage ways in the Chugoku region of Japan. Is there a way that I can calculate the total length of all these paths? I tried exporting to a KML and running some scrip...'''
date = "2015-05-03T22:23:00Z"
lastmod = "2019-11-18T11:28:00Z"
weight = 42859
keywords = [ "ways", "length", "overpass-turbo" ]
aliases = [ "/questions/42859" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Find total length of ways within a region, in Overpass Turbo](/questions/42859/find-total-length-of-ways-within-a-region-in-overpass-turbo)

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
<span id="post-42859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42859-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For example, I can run the Wizard query in Overpass Turbo: "highway=motorway AND oneway=yes in Chugoku" which gives me all the dual-carriage ways in the Chugoku region of Japan. Is there a way that I can calculate the total length of all these paths?</p>
<p>I tried exporting to a KML and running some script but then I realized that the KML file was a folder that contained thousands of individual paths.</p>
<p>I imagine there has to be a better way of doing this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '15, 22:23</strong></p>
<img src="https://secure.gravatar.com/avatar/7237c6bae32589cacecece9810feb731?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trubetskoy&#39;s gravatar image" />
<p><span>trubetskoy</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trubetskoy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42859" class="comments-container">
<span id="42875"></span>
<div id="comment-42875" class="comment">
<div id="post-42875-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>try to type "length" in the search box of this FAQ site ... there are already some topics how to determine lengts of determined OSM way elements.</p>
</div>
<div id="comment-42875-info" class="comment-info">
<span class="comment-age">(04 May '15, 16:43)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-42859" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42859-form-container" class="comment-form-container">
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

<span id="42930"></span>

<div id="answer-container-42930" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42930-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Export to a format QGIS can handle. Then use a function of that program to calculate. <a href="http://www.qgistutorials.com/en/docs/3/calculating_line_lengths.html">Here's a tutorial</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '15, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Feb '20, 02:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/7284ad488e18a2b052a9c7b8fe1e3922?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aharvey&#39;s gravatar image" />
<p><span>aharvey</span><br />
<span class="score" title="523 reputation points">523</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span></p>
</div>
</div>
<div id="comments-container-42930" class="comments-container">
&#10;</div>
<div id="comment-tools-42930" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42930-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71692"></span>

<div id="answer-container-71692" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71692-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Length">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Length</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '19, 11:28</strong></p>
<img src="https://secure.gravatar.com/avatar/47edd1ee4d973c50bbe7991bb063d09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jidanni&#39;s gravatar image" />
<p><span>jidanni</span><br />
<span class="score" title="339 reputation points">339</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jidanni has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71692" class="comments-container">
&#10;</div>
<div id="comment-tools-71692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71692-form-container" class="comment-form-container">
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

