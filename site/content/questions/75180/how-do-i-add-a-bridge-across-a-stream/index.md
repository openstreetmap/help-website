+++
type = "question"
title = "How do I add a BRIDGE across a stream?"
description = '''I am sure it is trivial but I have not yet been successful adding a &quot;bridge=yes&quot; across a stream. My best interpretation of the Wikis is to split the way for the road and create a way for the bridge between two Nodes. I do not want to create a more complex &quot;man_made&quot; bridge but would like to see a p...'''
date = "2020-06-07T17:46:00Z"
lastmod = "2020-06-07T21:03:00Z"
weight = 75180
keywords = [ "bridge" ]
aliases = [ "/questions/75180" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I add a BRIDGE across a stream?](/questions/75180/how-do-i-add-a-bridge-across-a-stream)

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
<span id="post-75180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75180-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am sure it is trivial but I have not yet been successful adding a "bridge=yes" across a stream. My best interpretation of the Wikis is to split the way for the road and create a way for the bridge between two Nodes. I do not want to create a more complex "man_made" bridge but would like to see a parallel line on each side of the road symbolizing a bridge when rendered. But, all I seem to get is a complete "interruption" of the road with no indication of any connection between the two road fragments. Is creating a simple bridge really that difficult? In my area, many true bridges are entered with the stream simply going under a road through a tunnel. Perhaps, these errors are due to remote "mappers" working from aerial imagery rather than from local knowledge? I would like to correct these errors and add additional information in OSM in my area if I am ever able to get a bridge to render correctly. Thank you, Harrison S</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '20, 17:46</strong></p>
<img src="https://secure.gravatar.com/avatar/00b5cb5e348abce5ef203604759f7428?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harrison%20S&#39;s gravatar image" />
<p><span>Harrison S</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harrison S has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75180" class="comments-container">
&#10;</div>
<div id="comment-tools-75180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75180-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="75182"></span>

<div id="answer-container-75182" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75182-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For a bridge you split the way at the start and end of the bridge portions and add the <a href="https://wiki.openstreetmap.org/wiki/Key:bridge"><code>bridge=*</code></a> tag to the bridge section. Other tags should be maintained where they remain the same as the main road segments.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Tag:tunnel%3Dculvert">Culverts</a> are added in a similar manner but by splitting the waterway. Large culverts and small bridges often looking very similar from a distance.</p>
<p>You should probably set an appropriate <a href="https://wiki.openstreetmap.org/wiki/Key:layer">layer</a> tag too. Don't be too concerned with the renderer's <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">output</a>.</p>
<p>For basic editing tasks like this you may want to refer to tutorials such as those on <a href="https://learnosm.org/en/">LearnOSM</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '20, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-75182" class="comments-container">
<span id="75183"></span>
<div id="comment-75183" class="comment">
<div id="post-75183-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just to add the the point above about "other tags should be maintained" is important - the "interruption" you describe sounds like you may have removed other tags. A highway=secondary, for example, is still tagged as highway=secondary when crossing a bridge.</p>
</div>
<div id="comment-75183-info" class="comment-info">
<span class="comment-age">(07 Jun '20, 18:45)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-75182" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75182-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75181"></span>

<div id="answer-container-75181" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75181-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are correct that you split the road way at either end of where the bridge is. Then on the segment that is the bridge, tag it with <code>bridge=yes</code> and <code>layer=1</code></p>
<p>I don't know what editor you are using, but it should be a pretty easy operation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '20, 17:55</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-75181" class="comments-container">
&#10;</div>
<div id="comment-tools-75181" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75181-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75188"></span>

<div id="answer-container-75188" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75188-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you alan_gr and stf: When I did it correctly, it even rendered as I wanted! I am sure it is unrelated but I did experience some JOSM "issues" when I added "lanes=" and "layer=" but was able to overcome them. Apparently, my initial error was basically leaving the "highway=residential" off the way I added for the "bridge=yes". Both must be required to render correctly. Thank you, Harrison S</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '20, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/00b5cb5e348abce5ef203604759f7428?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harrison%20S&#39;s gravatar image" />
<p><span>Harrison S</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harrison S has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75188" class="comments-container">
<span id="75190"></span>
<div id="comment-75190" class="comment">
<div id="post-75190-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ahhh. Using JOSM.</p>
<p>In JOSM you can add a point on the existing highway on either end of the bridge. Then shift-click to select both point. Once selected use the "p" short cut to split the way. Doing this will duplicated all the tags (lanes, surface, name, etc.) on the newly created way. The you can simply add the bridge and layer tag.</p>
<p>Doing it that way will also properly update any relations (bus routes, highway routes, etc.) that used the way.</p>
<p>Much easier and safer than creating a new way from scratch and then trying to get all the existing tags copied over and put the new way into all the various relations that use the existing road.</p>
</div>
<div id="comment-75190-info" class="comment-info">
<span class="comment-age">(07 Jun '20, 21:03)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
</div>
<div id="comment-tools-75188" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75188-form-container" class="comment-form-container">
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

