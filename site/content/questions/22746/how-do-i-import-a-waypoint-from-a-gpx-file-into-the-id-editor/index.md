+++
type = "question"
title = "How do I import a waypoint from a gpx file into the iD editor"
description = '''When a gpx file is dragged onto the iD editor window, any tracks in it appear in the window. But waypoints in the file do not appear. How do I get them on to it? Thanks, Roger'''
date = "2013-05-24T21:01:00Z"
lastmod = "2013-10-18T01:37:00Z"
weight = 22746
keywords = [ "ideditor", "gpx", "waypoints" ]
aliases = [ "/questions/22746" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I import a waypoint from a gpx file into the iD editor](/questions/22746/how-do-i-import-a-waypoint-from-a-gpx-file-into-the-id-editor)

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
<span id="post-22746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22746-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-22746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When a gpx file is dragged onto the iD editor window, any tracks in it appear in the window. But waypoints in the file do not appear. How do I get them on to it?</p>
<p>Thanks,</p>
<p>Roger</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-waypoints" rel="tag" title="see questions tagged &#39;waypoints&#39;">waypoints</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '13, 21:01</strong></p>
<img src="https://secure.gravatar.com/avatar/64e0edfbd8e5011414d66969720d6b62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rogerc&#39;s gravatar image" />
<p><span>Rogerc</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rogerc has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '13, 00:02</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-22746" class="comments-container">
<span id="22763"></span>
<div id="comment-22763" class="comment">
<div id="post-22763-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Maybe you should open a feature request at the github page of the iD editor.</p>
</div>
<div id="comment-22763-info" class="comment-info">
<span class="comment-age">(25 May '13, 20:07)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="22771"></span>
<div id="comment-22771" class="comment">
<div id="post-22771-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>... that is here: <a href="https://github.com/systemed/iD/issues">https://github.com/systemed/iD/issues</a> . Indeed it is as far as I know not possible currently. Only tracks are shown.</p>
</div>
<div id="comment-22771-info" class="comment-info">
<span class="comment-age">(25 May '13, 23:38)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="27243"></span>
<div id="comment-27243" class="comment">
<div id="post-27243-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Today (oct.13) waypoints appear. However only one gpx-file is shown. That's not good because my garmin stores waypoints and tracks in different files.</p>
</div>
<div id="comment-27243-info" class="comment-info">
<span class="comment-age">(16 Oct '13, 21:22)</span> <span class="comment-user userinfo">hfst</span>
</div>
</div>
<span id="27253"></span>
<div id="comment-27253" class="comment">
<div id="post-27253-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span>@hfst</span>: As a workaround you could merge your gpx files for example in any text editor. For example copy the <code>&lt;wpt&gt;…&lt;/wpt&gt;</code> sections (one for each waypoint) into your track gpx file right before the <code>&lt;/gpx&gt;</code> at the end of the file.</p>
</div>
<div id="comment-27253-info" class="comment-info">
<span class="comment-age">(17 Oct '13, 02:24)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="27271"></span>
<div id="comment-27271" class="comment">
<div id="post-27271-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@aseerel4c26</span>: as potlatch2 is able to display more than one gpx-file I think that this should also work for ID</p>
</div>
<div id="comment-27271-info" class="comment-info">
<span class="comment-age">(17 Oct '13, 19:49)</span> <span class="comment-user userinfo">hfst</span>
</div>
</div>
<span id="27290"></span>
<div id="comment-27290" class="comment not_top_scorer">
<div id="post-27290-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@hfst</span>: to be clear, I did not mean to say the opposite. I only presented a workaround if you currently want to use iD (which this question is about).</p>
</div>
<div id="comment-27290-info" class="comment-info">
<span class="comment-age">(18 Oct '13, 01:37)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22746" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-22746-form-container" class="comment-form-container">
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

<span id="22901"></span>

<div id="answer-container-22901" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22901-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://github.com/systemed/iD/issues/1557">Created an issue for you on the iD issue tracker</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '13, 03:41</strong></p>
<img src="https://secure.gravatar.com/avatar/5eea0a101ed06779f56546479dcc80b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcw&#39;s gravatar image" />
<p><span>mcw</span><br />
<span class="score" title="416 reputation points">416</span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcw has one accepted answer">6%</span></p>
</div>
</div>
<div id="comments-container-22901" class="comments-container">
&#10;</div>
<div id="comment-tools-22901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22901-form-container" class="comment-form-container">
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

