+++
type = "question"
title = "Using GPS traces for an application"
description = '''Hi, I&#x27;m a french student and I work with 6 other students on a project which aims at producing an application (for Android). This application would be based on OSMTracker (https://wiki.openstreetmap.org/wiki/OSMtracker) and would permit to upload GPS traces and to retrieve them later, considering the...'''
date = "2013-05-14T13:01:00Z"
lastmod = "2015-02-18T21:02:00Z"
weight = 22420
keywords = [ "application", "android", "traces", "gps" ]
aliases = [ "/questions/22420" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Using GPS traces for an application](/questions/22420/using-gps-traces-for-an-application)

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
<span id="post-22420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22420-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm a french student and I work with 6 other students on a project which aims at producing an application (for Android).</p>
<p>This application would be based on OSMTracker (<a href="https://wiki.openstreetmap.org/wiki/OSMtracker">https://wiki.openstreetmap.org/wiki/OSMtracker</a>) and would permit to upload GPS traces and to retrieve them later, considering the differents tags associated to these traces. We earlier saw that some bots are allowed to upload traces on openstreetmap.org however I didn't find how to get an authorization for such activities. Moreover, I searched on the wiki but I didn't find any information about how we can retrieve these traces once they're on OSM servers.</p>
<p>That's why I'm asking you if this kind of activities is possible or else who I should contact to get more informations about it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-application" rel="tag" title="see questions tagged &#39;application&#39;">application</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-traces" rel="tag" title="see questions tagged &#39;traces&#39;">traces</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '13, 13:01</strong></p>
<img src="https://secure.gravatar.com/avatar/2273223780316f1705472ddd3668bb20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vince4x4&#39;s gravatar image" />
<p><span>Vince4x4</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vince4x4 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22420" class="comments-container">
&#10;</div>
<div id="comment-tools-22420" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22420-form-container" class="comment-form-container">
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

<span id="22461"></span>

<div id="answer-container-22461" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22461-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>re: retrieving tracks: apparently, you need the GPS trace ID to download them through the API, see <a href="https://wiki.openstreetmap.org/wiki/Api06#GPS_traces">https://wiki.openstreetmap.org/wiki/Api06#GPS_traces</a> .</p>
<pre><code>GET /api/0.6/gpx/[id]/details
GET /api/0.6/gpx/[id]/data</code></pre>
<p>I am not aware of a method to search for GPS traces based on tags that is exposed through API v0.6 or XAPI.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '13, 21:57</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-22461" class="comments-container">
&#10;</div>
<div id="comment-tools-22461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22461-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41134"></span>

<div id="answer-container-41134" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41134-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Massive import of tracks is under the same regulations as data imports, see <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">this article</a>. Be careful, because smartphone tracks usually are low quality ones, pretty often they are almost unusable.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '15, 21:02</strong></p>
<img src="https://secure.gravatar.com/avatar/c7f2443ac02cb3e24f4df768eeb98933?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BushmanK&#39;s gravatar image" />
<p><span>BushmanK</span><br />
<span class="score" title="171 reputation points">171</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BushmanK has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-41134" class="comments-container">
&#10;</div>
<div id="comment-tools-41134" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41134-form-container" class="comment-form-container">
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

