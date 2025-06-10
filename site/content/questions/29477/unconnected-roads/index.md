+++
type = "question"
title = "Unconnected Roads"
description = '''I&#x27;m trying to correct several mistakes in my area, but there&#x27;s something giving me trouble: some streets/roads aren&#x27;t &quot;connected&quot; and it&#x27;s almost impossible to connect them, especially, when more than 4 roads come together. They snap together and if I drag the node, everything&#x27;s connected. But when ...'''
date = "2013-12-30T20:06:00Z"
lastmod = "2013-12-30T20:57:00Z"
weight = 29477
keywords = [ "roads", "unconnected", "connected" ]
aliases = [ "/questions/29477" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Unconnected Roads](/questions/29477/unconnected-roads)

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
<span id="post-29477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29477-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to correct several mistakes in my area, but there's something giving me trouble: some streets/roads aren't "connected" and it's almost impossible to connect them, especially, when more than 4 roads come together. They snap together and if I drag the node, everything's connected. But when I test the outcome in yournavigation.org it's not correct. You can't turn from road A to B In some cases streets continue with district boundaries (as it was the case at the ferry terminal in Dublin) instead of the street and others just go to some tertiary roads. Is there any quick fix to connect several roads, so the system identifies them as roads that continue (for driving directions)? So far I usually have to delete the existing roads (partially) and redraw them, however, even this way sometimes it doesn't work.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-unconnected" rel="tag" title="see questions tagged &#39;unconnected&#39;">unconnected</span> <span class="post-tag tag-link-connected" rel="tag" title="see questions tagged &#39;connected&#39;">connected</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '13, 20:06</strong></p>
<img src="https://secure.gravatar.com/avatar/43acae1e517b1a40c05d80314748717d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="willi_rec&#39;s gravatar image" />
<p><span>willi_rec</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="willi_rec has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29477" class="comments-container">
&#10;</div>
<div id="comment-tools-29477" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29477-form-container" class="comment-form-container">
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

<span id="29481"></span>

<div id="answer-container-29481" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29481-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-29481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Consider what <a href="http://yournavigation.org/">http://yournavigation.org/</a> writes below the map:<br />
<em>Routing data from planet file: 2013-05-21</em><br />
This means they use data from May 2013 which doesn't reflect your latest edits.</p>
<p>Try <a href="http://www.map.project-osrm.org/">osrm</a> which has up-to-date data.</p>
<p>Since you edit with using iD I had a try with that editor doing what you try to do and was successful. I could connect ways I wanted to connect and unglue/disconnect ways, too. Though it is a little more tedious and slower than in my preferred editor I was satisfied.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '13, 20:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span> </br></br></p>
</div>
</div>
<div id="comments-container-29481" class="comments-container">
<span id="29483"></span>
<div id="comment-29483" class="comment">
<div id="post-29483-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the link, good site! I will do some testing, if the problem also occurs or if it's a problem of yournavigation.org interpreting the data (however, also pocketearth does this). Anyway, at least it helps me check if the connection is finally working. Thanks!</p>
</div>
<div id="comment-29483-info" class="comment-info">
<span class="comment-age">(30 Dec '13, 20:57)</span> <span class="comment-user userinfo">willi_rec</span>
</div>
</div>
</div>
<div id="comment-tools-29481" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29481-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29480"></span>

<div id="answer-container-29480" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29480-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-29480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you aware that yournavigation.org does not use "live" data but a canned version of the database that can be multiple months old? Currently (at the time of writing this) it says, under the map, that it is using data from 2013-05-21. So don't expect your changes to influence yournavigation.org immediately. If everything moves with the intersection node in the editor, that's a good sign.</p>
<p>You might want to check out project-osrm.org which has a faster update cycle (but even there, don't expect your changes to be effective immediately).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '13, 20:33</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-29480" class="comments-container">
<span id="29482"></span>
<div id="comment-29482" class="comment">
<div id="post-29482-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually, they use newer data. I added some roads where I live (Recife, Brazil) and they show up. I know, it's not immediately, but some hours later. In my case, it wasn't possible to get from the terminal (T2) to the ferry line in Dublin, now it's possible. But it wasn't easy to do the trick. I don't know, if it's a bug or if I'm not getting something, but points snap together and create crossings where they shouldn't (district lines) and sometimes they don't form a crossing, even if there's a point connecting two roads.</p>
</div>
<div id="comment-29482-info" class="comment-info">
<span class="comment-age">(30 Dec '13, 20:42)</span> <span class="comment-user userinfo">willi_rec</span>
</div>
</div>
</div>
<div id="comment-tools-29480" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29480-form-container" class="comment-form-container">
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

