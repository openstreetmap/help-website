+++
type = "question"
title = "Failed to upload GPS track"
description = '''How do I get my trace into OSM? I&#x27;m using OMStracker on Android 1.5. I&#x27;ve been able to record a track and upload, but the upload fails with the error: &quot;Generic XML parse error / XML parser at line 1 column 0&quot; Opening the file in a text editor shows that indeed the file is not XML but some kind of en...'''
date = "2010-11-05T17:56:00Z"
lastmod = "2010-11-05T19:27:00Z"
weight = 1472
keywords = [ "android", "upload" ]
aliases = [ "/questions/1472" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Failed to upload GPS track](/questions/1472/failed-to-upload-gps-track)

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
<span id="post-1472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1472-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I get my trace into OSM? I'm using OMStracker on Android 1.5. I've been able to record a track and upload, but the upload fails with the error: "Generic XML parse error / XML parser at line 1 column 0"</p>
<p>Opening the file in a text editor shows that indeed the file is <em>not</em> XML but some kind of encoding mess of characters and gibberish. From what I've read, I'm not supposed to need to convert this file before uploading, but if that's the case, what's going on and how do I fix it so I can contribute?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Nov '10, 17:56</strong></p>
<img src="https://secure.gravatar.com/avatar/e1ea1ea74d1560fe7a71e436c2754bba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cnast&#39;s gravatar image" />
<p><span>cnast</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cnast has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Nov '10, 09:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-1472" class="comments-container">
&#10;</div>
<div id="comment-tools-1472" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1472-form-container" class="comment-form-container">
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

<span id="1473"></span>

<div id="answer-container-1473" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1473-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's odd, cnast.<br />
</p>
<p>OSM's track import is expecting track files in GPX format. Many devices are capable of saving in different formats, often including GPX. If your device won't save in GPX, a program called gpsbabel can convert many formats to and from GPX.<br />
</p>
<p>So check your program settings to see if GPX is an option in future and to get a hint of what your current format is. You should be able to convert and use the current file, rather than having to do it again.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Nov '10, 19:03</strong></p>
<img src="https://secure.gravatar.com/avatar/d90ea04df82d77f534659f08894dd889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Weait&#39;s gravatar image" />
<p><span>Richard Weait</span><br />
<span class="score" title="3044 reputation points"><span>3.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="34 badges"><span class="silver">●</span><span class="badgecount">34</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Weait has 8 accepted answers">17%</span> </br></br></p>
</div>
</div>
<div id="comments-container-1473" class="comments-container">
<span id="1474"></span>
<div id="comment-1474" class="comment">
<div id="post-1474-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Another usable program to convert tracklogs in many different formats to GPX format is Routeconverter which can be found at <a href="http://www.routeconverter.de">http://www.routeconverter.de</a> or in the OSM wiki.</p>
</div>
<div id="comment-1474-info" class="comment-info">
<span class="comment-age">(05 Nov '10, 19:27)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-1473" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1473-form-container" class="comment-form-container">
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

