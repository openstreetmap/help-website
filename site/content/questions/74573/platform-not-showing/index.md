+++
type = "question"
title = "Platform not showing"
description = '''I edited the platform in Braunau (https://www.openstreetmap.org/#map=19/48.25909/13.04800) and now the platform disappeard from the map. It doesn&#x27;t show the dark grey area of a platform. Does anyone know what I did wrong?'''
date = "2020-05-03T18:34:00Z"
lastmod = "2020-05-04T08:25:00Z"
weight = 74573
keywords = [ "platform", "railwayplatform" ]
aliases = [ "/questions/74573" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Platform not showing](/questions/74573/platform-not-showing)

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
<span id="post-74573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74573-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I edited the platform in Braunau (<a href="https://www.openstreetmap.org/#map=19/48.25909/13.04800)">https://www.openstreetmap.org/#map=19/48.25909/13.04800)</a> and now the platform disappeard from the map. It doesn't show the dark grey area of a platform. Does anyone know what I did wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-platform" rel="tag" title="see questions tagged &#39;platform&#39;">platform</span> <span class="post-tag tag-link-railwayplatform" rel="tag" title="see questions tagged &#39;railwayplatform&#39;">railwayplatform</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '20, 18:34</strong></p>
<img src="https://secure.gravatar.com/avatar/9bd4f88705ca81217e71cf2e2ae54991?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaperYoshi&#39;s gravatar image" />
<p><span>PaperYoshi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaperYoshi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74573" class="comments-container">
<span id="74576"></span>
<div id="comment-74576" class="comment">
<div id="post-74576-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems to be showing on the transport layer.</p>
</div>
<div id="comment-74576-info" class="comment-info">
<span class="comment-age">(03 May '20, 19:31)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="74593"></span>
<div id="comment-74593" class="comment">
<div id="post-74593-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The platform in question: <a href="https://www.openstreetmap.org/way/746409238">https://www.openstreetmap.org/way/746409238</a> . Try touching (=modifying) it a second time. Maybe the rendering database had a hickup while importing your changes.</p>
</div>
<div id="comment-74593-info" class="comment-info">
<span class="comment-age">(04 May '20, 08:25)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74573-form-container" class="comment-form-container">
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

<span id="74579"></span>

<div id="answer-container-74579" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74579-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's probably a conflict with some tag you added. This much more simple <a href="https://www.openstreetmap.org/way/722717643">one</a> still show up.</p>
<p>It's not area=yes, even if it's <em>not</em> required per the <a href="https://wiki.openstreetmap.org/wiki/Tag:public_transport%3Dplatform">wiki</a>, this <a href="https://www.openstreetmap.org/way/136490437">one</a> is ok.</p>
<p>I could find others (like <a href="https://www.openstreetmap.org/way/126992250">this</a>) that fail to render, so I guess it's some trouble with the combination "covered=yes", "area=yes" and "train=yes" (it seems to work well for bus stops).</p>
<p>This <a href="https://www.openstreetmap.org/way/196930809">one</a>, with similar tags as yours, fails, but the <a href="https://www.openstreetmap.org/way/196930810">one</a> across, with covered=no, renders.</p>
<p>You can test by removing your tags one by one until it renders again, or better splitting the platform in segments with the various combinations and wait for re-rendering.</p>
<p>And then probably file an <a href="https://github.com/gravitystorm/openstreetmap-carto">issue</a>, because it clearly feels like a bug in the rendering.</p>
<p>Hope this helps.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '20, 20:36</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-74579" class="comments-container">
&#10;</div>
<div id="comment-tools-74579" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74579-form-container" class="comment-form-container">
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

