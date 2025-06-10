+++
type = "question"
title = "Broken track"
description = '''If I upload a GPX track, it is shown in parts in potlatch2 if I want to edit it. I expect one line representing the track. But now I see a kind of dashed line, some parts of the track are missing. What is going wrong? I have checked the GPX file. All the track points are in it. Potlatch is not showi...'''
date = "2011-11-04T08:52:00Z"
lastmod = "2011-11-06T16:35:00Z"
weight = 8795
keywords = [ "track", "broken" ]
aliases = [ "/questions/8795" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Broken track](/questions/8795/broken-track)

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
<span id="post-8795-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8795-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8795-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If I upload a GPX track, it is shown in parts in potlatch2 if I want to edit it. I expect one line representing the track. But now I see a kind of dashed line, some parts of the track are missing. What is going wrong?</p>
<p>I have checked the GPX file. All the track points are in it. Potlatch is not showing some of them and splits up the track in several separate tracks. JOSM and other GPS programms show the track correctly. This seems to be a Potlatch problem.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-broken" rel="tag" title="see questions tagged &#39;broken&#39;">broken</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Nov '11, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/7a18c056063a165f36376a9288221284?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JavierP&#39;s gravatar image" />
<p><span>JavierP</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JavierP has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Nov '11, 18:59</strong> </span></p>
</div>
</div>
<div id="comments-container-8795" class="comments-container">
<span id="8820"></span>
<div id="comment-8820" class="comment">
<div id="post-8820-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Perhaps your problem the same as the one described here:</p>
<p><a href="http://help.openstreetmap.org/questions/7968/only-small-parts-of-my-gpx-track-is-visible-in-potlatch">http://help.openstreetmap.org/questions/7968/only-small-parts-of-my-gpx-track-is-visible-in-potlatch</a></p>
<p>In my case I've not seen this when editing traces from the GPS trace list, but have seen it when selecting "GPS Data / GPS Data" from within Potlatch2. Do you get the same effect?</p>
</div>
<div id="comment-8820-info" class="comment-info">
<span class="comment-age">(04 Nov '11, 15:15)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="8832"></span>
<div id="comment-8832" class="comment">
<div id="post-8832-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, this is the same problem. There is nothing wrong with the GPS. In Mapsoure the track is OK. Also uploading the track in JOSM gives a good result.</p>
</div>
<div id="comment-8832-info" class="comment-info">
<span class="comment-age">(04 Nov '11, 16:32)</span> <span class="comment-user userinfo">JavierP</span>
</div>
</div>
</div>
<div id="comment-tools-8795" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8795-form-container" class="comment-form-container">
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

<span id="8854"></span>

<div id="answer-container-8854" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8854-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At present Potlatch 2 will break up tracks where the timestamps are more than a certain distance apart. This is a known issue.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '11, 16:35</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-8854" class="comments-container">
&#10;</div>
<div id="comment-tools-8854" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8854-form-container" class="comment-form-container">
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

