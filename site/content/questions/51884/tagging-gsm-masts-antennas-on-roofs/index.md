+++
type = "question"
title = "Tagging GSM masts / antennas on roofs?"
description = ''' Hi, triggered by the newcloudatlas.org initiative I&#x27;m asking how do we map the usual mobile communication antennas that are mounted on roofs? I never found a good answer and in german lang pole / mast / antenna are pretty close and I&#x27;m not sure if we need (an full) technical term for tagging?  tele...'''
date = "2016-09-03T09:31:00Z"
lastmod = "2017-10-04T06:09:00Z"
weight = 51884
keywords = [ "mobile", "telecommunication", "antenna" ]
aliases = [ "/questions/51884" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tagging GSM masts / antennas on roofs?](/questions/51884/tagging-gsm-masts-antennas-on-roofs)

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
<span id="post-51884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51884-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><img src="https://wiki.openstreetmap.org/w/images/thumb/1/1a/Gsm_antenne.JPG/320px-Gsm_antenne.JPG" alt="alt text" /></p>
<p>Hi, triggered by the <a href="http://newcloudatlas.org">newcloudatlas.org</a> initiative <a href="https://wiki.openstreetmap.org/wiki/Talk:WikiProject_Telecoms#GSM_poles_masts_on_roof.3F">I'm asking</a> how do we map the usual mobile communication antennas that are mounted on roofs? I never found a good answer and in german lang pole / mast / antenna are pretty close and I'm not sure if we need (an full) technical term for tagging?</p>
<ul>
<li><code>telecom=antenna</code> - seems to be obvious, but this is (technically) only a single component of the setup. Also there other <a href="https://wiki.openstreetmap.org/wiki/Telecommunication#reality">other very big structures</a> which might be clother to this tag ?</li>
<li><code>man_made=mast, mast:type=communication, communication:mobile_phone=yes</code> - <a href="https://wiki.openstreetmap.org/wiki/WikiProject_Telecoms#Masts">wiki says</a> standalone, which isn't the case? (also rendered at osm.org which point that they are somewhat landmarks?)</li>
<li><code>man_made=tower, tower:type=communication, communication:mobile_phone=yes</code> - well it's not that a solid installation?</li>
</ul>
<p>So what do you choose or recommend?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mobile" rel="tag" title="see questions tagged &#39;mobile&#39;">mobile</span> <span class="post-tag tag-link-telecommunication" rel="tag" title="see questions tagged &#39;telecommunication&#39;">telecommunication</span> <span class="post-tag tag-link-antenna" rel="tag" title="see questions tagged &#39;antenna&#39;">antenna</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Sep '16, 09:31</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</img>
</div>
</div>
<div id="comments-container-51884" class="comments-container">
&#10;</div>
<div id="comment-tools-51884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51884-form-container" class="comment-form-container">
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

<span id="59940"></span>

<div id="answer-container-59940" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59940-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-59940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Also the folks of <a href="http://newcloudatlas.org/edit/">http://newcloudatlas.org/edit/</a> suggest to follow the <a href="https://wiki.openstreetmap.org/wiki/WikiProject_Telecoms">telecoms project tagging rules</a></p>
<pre><code>man_made=mast
mast:type=communication
communication:mobile_phone=yes|no</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '17, 06:09</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-59940" class="comments-container">
&#10;</div>
<div id="comment-tools-59940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59940-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51886"></span>

<div id="answer-container-51886" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51886-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi iii, read the Wiki, <a href="https://wiki.openstreetmap.org/wiki/Tag:man_made%3Dcommunications_tower">https://wiki.openstreetmap.org/wiki/Tag:man_made%3Dcommunications_tower</a> add those tags if useful and add height=5 for meters in height the length of the mast on top of a building. Don’t try to make another tag since there has been talked about these man-made mast since 2011. The recent result was a mast is no tower, cleared by pictures. A short mast remains a mast anyhow. Practically a mast on top of a roof is still a stand alone with or without guides, As soon as its build on to the walls surrounding the building or the elevator shaft there no guides needed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '16, 10:10</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Sep '16, 10:12</strong> </span></p>
</div>
</div>
<div id="comments-container-51886" class="comments-container">
&#10;</div>
<div id="comment-tools-51886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51886-form-container" class="comment-form-container">
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

