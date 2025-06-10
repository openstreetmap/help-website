+++
type = "question"
title = "Roof thickness"
description = '''Hey, I&#x27;m working on drawing a building like this in 3D:  https://emoweb.dk/EMODigital/EMODigital.svc/Picture/100159308 Is there a way to define the thickness of a roof as a way to show the verges on a roof? I&#x27;ve tried roof:thickness:parallel + thickness in meters but it doesn&#x27;t seem to work or me. B...'''
date = "2021-10-21T22:58:00Z"
lastmod = "2021-10-24T14:53:00Z"
weight = 82301
keywords = [ "verges", "roof", "thickness" ]
aliases = [ "/questions/82301" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Roof thickness](/questions/82301/roof-thickness)

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
<span id="post-82301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82301-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey,</p>
<p>I'm working on drawing a building like this in 3D: <a href="https://emoweb.dk/EMODigital/EMODigital.svc/Picture/100159308">https://emoweb.dk/EMODigital/EMODigital.svc/Picture/100159308</a></p>
<p>Is there a way to define the thickness of a roof as a way to show the verges on a roof?</p>
<p>I've tried roof:thickness:parallel + thickness in meters but it doesn't seem to work or me.</p>
<p>Best regards Michael</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-verges" rel="tag" title="see questions tagged &#39;verges&#39;">verges</span> <span class="post-tag tag-link-roof" rel="tag" title="see questions tagged &#39;roof&#39;">roof</span> <span class="post-tag tag-link-thickness" rel="tag" title="see questions tagged &#39;thickness&#39;">thickness</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Oct '21, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/cd1fd455bb8e30ae1225ae9847366beb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MicDK&#39;s gravatar image" />
<p><span>MicDK</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MicDK has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82301" class="comments-container">
<span id="82316"></span>
<div id="comment-82316" class="comment">
<div id="post-82316-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What are you trying to render this with?</p>
<p>Do you want to map the overhang or the actual thickness?</p>
</div>
<div id="comment-82316-info" class="comment-info">
<span class="comment-age">(23 Oct '21, 14:09)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="82341"></span>
<div id="comment-82341" class="comment">
<div id="post-82341-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello InsertUser,</p>
<p>The overhang is no big problem when placing a separate roof with an overhang on top of a separate building. Needs a litte fixing of the height and that's all.</p>
<p>My problem is the verges which I think could be drawn as thicker roof that matches the width of the verges. There could be some tricky fixing of differrent roof and verge colours but anyway the house would look more realistic.</p>
</div>
<div id="comment-82341-info" class="comment-info">
<span class="comment-age">(24 Oct '21, 11:59)</span> <span class="comment-user userinfo">MicDK</span>
</div>
</div>
<span id="82342"></span>
<div id="comment-82342" class="comment">
<div id="post-82342-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the overhanging roof and main structure are part of the same building then they should probably only have on <code>building</code> outline and two (or more) <code>building: parts</code>. I'm not aware of a way of tagging the depth of the fascia or soffits. 3D mapping itself is still a little niche so there are quite a few areas of refinement we don't have tags for yet. Many of the finer details on 3D stuff are just too hard for hobbyists to get accurate information.</p>
</div>
<div id="comment-82342-info" class="comment-info">
<span class="comment-age">(24 Oct '21, 14:43)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="82344"></span>
<div id="comment-82344" class="comment">
<div id="post-82344-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Helle again,</p>
<p>That's how I'm doing it. The problem is that you - as far as I know - also can't operate with two min_heigts one a building and make a sloping building on the downside between them.</p>
</div>
<div id="comment-82344-info" class="comment-info">
<span class="comment-age">(24 Oct '21, 14:53)</span> <span class="comment-user userinfo">MicDK</span>
</div>
</div>
</div>
<div id="comment-tools-82301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82301-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

