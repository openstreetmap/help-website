+++
type = "question"
title = "planning Application"
description = '''How do I get scale 1250:1 for planning application'''
date = "2017-02-05T17:44:00Z"
lastmod = "2017-02-07T06:42:00Z"
weight = 54479
keywords = [ "planning" ]
aliases = [ "/questions/54479" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [planning Application](/questions/54479/planning-application)

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
<span id="post-54479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54479-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I get scale 1250:1 for planning application</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planning" rel="tag" title="see questions tagged &#39;planning&#39;">planning</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '17, 17:44</strong></p>
<img src="https://secure.gravatar.com/avatar/18d06a4a0eaa058029095bd3b0582c13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ray%20Moore&#39;s gravatar image" />
<p><span>Ray Moore</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ray Moore has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54479" class="comments-container">
<span id="54482"></span>
<div id="comment-54482" class="comment">
<div id="post-54482-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>please tell us a bit more. What do you want? A map? Which format? Which use?</p>
</div>
<div id="comment-54482-info" class="comment-info">
<span class="comment-age">(05 Feb '17, 19:34)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="54525"></span>
<div id="comment-54525" class="comment">
<div id="post-54525-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This should explain a bit more. If you are interested UK planning requirements <a href="https://www.planningportal.co.uk/applications">https://www.planningportal.co.uk/applications</a></p>
</div>
<div id="comment-54525-info" class="comment-info">
<span class="comment-age">(07 Feb '17, 06:37)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-54479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54479-form-container" class="comment-form-container">
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

<span id="54485"></span>

<div id="answer-container-54485" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54485-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-54485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will have to use a GIS tool. I would recommend QGIS. The Composer tool allows an A4 sheet to be laid out with the typical contents expected for this sort of thing &amp; you have good control over scale.</p>
<p>If incorporating an exported image into another document set the dpi to 254 and then there will be a straightforward relationship between metres on the ground to pixels in the image.</p>
<p>However, the available raster tiles will probably not be suitable (for instance text will be difficult to read), so you may need to use OSM vector data and style it yourself.</p>
<p>OSM has been used for at least one planning application in England &amp; Wales. Whether OSM data are suitable will depend on the nature of your application.</p>
<p>I personally have not created maps at this scale with OSM data, but I have made maps at 1:5000. I started with OSGB Open Data Local (which has style sheets <a href="https://www.ordnancesurvey.co.uk/resources/carto-design/cartographic-stylesheets.html">available</a> for QGIS), but relatively quickly found that OSM data were preferable for many features (largely because they are better attributed).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '17, 20:15</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-54485" class="comments-container">
<span id="54514"></span>
<div id="comment-54514" class="comment">
<div id="post-54514-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, very helpful</p>
</div>
<div id="comment-54514-info" class="comment-info">
<span class="comment-age">(06 Feb '17, 12:40)</span> <span class="comment-user userinfo">Ray Moore</span>
</div>
</div>
<span id="54526"></span>
<div id="comment-54526" class="comment">
<div id="post-54526-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It would be useful to know if you manage to create plans in an acceptable format, at some time.</p>
</div>
<div id="comment-54526-info" class="comment-info">
<span class="comment-age">(07 Feb '17, 06:42)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-54485" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54485-form-container" class="comment-form-container">
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

