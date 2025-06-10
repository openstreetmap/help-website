+++
type = "question"
title = "Video mapping plugin problem with VLC player?"
description = '''I&#x27;m trying to use the videomapping plugin in josm, to view and sync a video with a gpx track. When I try to import the video I get this error message: &quot;VLC library is not correctly initialized. Please check that VLC 2.0.X is correctly installed on your system. Its architecture (32/64 bits) must also...'''
date = "2013-12-01T12:15:00Z"
lastmod = "2013-12-01T12:31:00Z"
weight = 28651
keywords = [ "josm", "video", "plugin" ]
aliases = [ "/questions/28651" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Video mapping plugin problem with VLC player?](/questions/28651/video-mapping-plugin-problem-with-vlc-player)

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
<span id="post-28651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28651-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to use the videomapping plugin in josm, to view and sync a video with a gpx track.</p>
<p>When I try to import the video I get this error message:</p>
<p>"VLC library is not correctly initialized. Please check that VLC 2.0.X is correctly installed on your system. Its architecture (32/64 bits) must also be the same as the JRE that runs JOSM."</p>
<p>I'mworking in Ubuntu 12.04 64 bit, The VLC player installed is 2.0.8 64 bit (from ubuntu software center). JOSM is running on 1.6.0_27. If I do "java -version" I get:</p>
<p>java version "1.6.0_27" OpenJDK Runtime Environment (IcedTea6 1.12.6) (6b27-1.12.6-1ubuntu0.12.04.4) OpenJDK 64-Bit Server VM (build 20.0-b12, mixed mode)</p>
<p>Any hint?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-video" rel="tag" title="see questions tagged &#39;video&#39;">video</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '13, 12:15</strong></p>
<img src="https://secure.gravatar.com/avatar/bcce6e29a8bf37a2008f957238d69feb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexandre%20Neto&#39;s gravatar image" />
<p><span>Alexandre Neto</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexandre Neto has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28651" class="comments-container">
&#10;</div>
<div id="comment-tools-28651" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28651-form-container" class="comment-form-container">
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

<span id="28652"></span>

<div id="answer-container-28652" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28652-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>IMHO the video plugin has never really worked (in particular it has a build in assumption that trackpoints are in fixed 1 second intervalls). If you are not a developer and can fix the issues yourself I don't think it makes sense to spend any time trying to get it running (which is likely not going to be sucessful).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '13, 12:31</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-28652" class="comments-container">
&#10;</div>
<div id="comment-tools-28652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28652-form-container" class="comment-form-container">
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

