+++
type = "question"
title = "Can I HYPERLINK via Grid Reference"
description = '''In a Libre Office Calc sheet I am trying to gret this to work:- =HYPERLINK(&quot;https://www.openstreetmap.org/#map=19/&quot;&amp;amp;B1) Column B contains GRid References in the Format AANNNNNNNN e.g TQ43108150 At the moment clicking on the formular does nothing. Am I using thre correct formular and is B1 in the...'''
date = "2022-12-17T17:51:00Z"
lastmod = "2022-12-17T20:45:00Z"
weight = 86356
keywords = [ "spreadsheet", "gridreferance" ]
aliases = [ "/questions/86356" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I HYPERLINK via Grid Reference](/questions/86356/can-i-hyperlink-via-grid-reference)

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
<span id="post-86356-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86356-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86356-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In a Libre Office Calc sheet I am trying to gret this to work:-</p>
<p>=HYPERLINK("https://www.openstreetmap.org/#map=19/"&amp;B1)</p>
<p>Column B contains GRid References in the Format AANNNNNNNN e.g TQ43108150</p>
<p>At the moment clicking on the formular does nothing. Am I using thre correct formular and is B1 in the correct format for OPenStreetMap/</p>
<p>I have opened Openstreetmap an dtried entering the grid reference in the search box but this retrurns "No results Founs" so is my searching not correct either?</p>
<p>Any help appreciated</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-spreadsheet" rel="tag" title="see questions tagged &#39;spreadsheet&#39;">spreadsheet</span> <span class="post-tag tag-link-gridreferance" rel="tag" title="see questions tagged &#39;gridreferance&#39;">gridreferance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '22, 17:51</strong></p>
<img src="https://secure.gravatar.com/avatar/c08855d5982c74634062030663cae388?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="athegn1&#39;s gravatar image" />
<p><span>athegn1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="athegn1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86356" class="comments-container">
&#10;</div>
<div id="comment-tools-86356" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86356-form-container" class="comment-form-container">
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

<span id="86357"></span>

<div id="answer-container-86357" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86357-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM URLs are in this format <a href="https://www.openstreetmap.org/#map=19/51.85916/1.11641">https://www.openstreetmap.org/#map=19/51.85916/1.11641</a> Where 19 is the zoom level and the next two numbers are longitude and latitude. You can convert what I'm guessing is an OS Grid reference to lat long using a website such as <a href="https://webapps.bgs.ac.uk/data/webservices/convertForm.cfm">https://webapps.bgs.ac.uk/data/webservices/convertForm.cfm</a> Or <a href="https://www.movable-type.co.uk/scripts/latlong-os-gridref.html">https://www.movable-type.co.uk/scripts/latlong-os-gridref.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '22, 18:19</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-86357" class="comments-container">
&#10;</div>
<div id="comment-tools-86357" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86357-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86358"></span>

<div id="answer-container-86358" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86358-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you for your answer.</p>
<p>I have found:-</p>
<p><a href="https://gridreferencefinder.com/batchConvert/batchConvert.php">https://gridreferencefinder.com/batchConvert/batchConvert.php</a> that batch convert GRid Ref to Lat and Long.</p>
<p>I then pasted the results into columns L and M on my sheet.</p>
<p>I changed the formular to:-</p>
<p>=HYPERLINK("https://www.openstreetmap.org/#map=19/"&amp;L4&amp;"/"&amp;M4)</p>
<p>THed resulting value is:- <a href="https://www.openstreetmap.org/#map=19/51.824291/0.84851047">https://www.openstreetmap.org/#map=19/51.824291/0.84851047</a></p>
<p>However when double click on the cell M4 illuminates ib Red and Cell M4 is selected in Red, instaed of open OPenstreetmap.</p>
<p>Any advice please?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '22, 19:03</strong></p>
<img src="https://secure.gravatar.com/avatar/c08855d5982c74634062030663cae388?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="athegn1&#39;s gravatar image" />
<p><span>athegn1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="athegn1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86358" class="comments-container">
<span id="86359"></span>
<div id="comment-86359" class="comment">
<div id="post-86359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ctrl-click to activate the hyperlink, although it seems a bit fussy.</p>
</div>
<div id="comment-86359-info" class="comment-info">
<span class="comment-age">(17 Dec '22, 20:45)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-86358" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86358-form-container" class="comment-form-container">
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

