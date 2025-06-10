+++
type = "question"
title = "Josm: Mapcss, two icons next to each other, possible?"
description = '''Version 10966, not the latest because a plugin do not work with this latest. I want two icons next to each other or partly over each other. Icons are 30x30px. Tags placed on the same node. wpt=yes fee=no This in the mapcss. node|z14-[wpt=yes] {  icon-offset-x:0;   icon-offset-y:0;  icon-image: &quot;wptn...'''
date = "2016-12-06T22:02:00Z"
lastmod = "2016-12-08T12:44:00Z"
weight = 53267
keywords = [ "josm", "mapcss" ]
aliases = [ "/questions/53267" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Josm: Mapcss, two icons next to each other, possible?](/questions/53267/josm-mapcss-two-icons-next-to-each-other-possible)

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
<span id="post-53267-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53267-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53267-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Version 10966, not the latest because a plugin do not work with this latest.</p>
<p>I want two icons next to each other or partly over each other. Icons are 30x30px.</p>
<p>Tags placed on the same node. wpt=yes fee=no</p>
<p>This in the mapcss.</p>
<p>node|z14-[wpt=yes] { icon-offset-x:0;<br />
icon-offset-y:0; icon-image: "wptn.png"; }</p>
<p>node|z14-[wpt=yes] { icon-offset-x:30;<br />
icon-offset-y:0; icon-image: "feen.png"; }</p>
<p>Just a example for tags.<br />
I do not want to make feen.png 60x30 px and leave one half transparent. I did see the trafficsign finish mapcss example.</p>
<p>I want the fee icon(30x30) next to wpt icon(30x30).</p>
<p>If you have icon-offset-x set on both, it uses the last one in the table to set both icons off. They stay always over each other, I think.</p>
<p>Edit: When one node and two icons, 1 appears, the last one writing in line on the mapcss file. I want to see them both.</p>
<p>The same problem with text 1 node with multiple tags, from two tags I want to see the value's. 1 tag, I want the value number above the node. 1 tag, I want the value under the node. when using</p>
<p>1. text-offset-x: -30; text-offset-y: 10;</p>
<p>2. text-offset-x: -30; text-offset-y: -10;</p>
<p>for two tags on the same node.</p>
<p>Here also the last one in the table, appears.</p>
<p>What am I doing wrong. Or is it a bug?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-mapcss" rel="tag" title="see questions tagged &#39;mapcss&#39;">mapcss</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '16, 22:02</strong></p>
<img src="https://secure.gravatar.com/avatar/6c5dc0fc3be6786b643d15ec99ba3e3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Allroads&#39;s gravatar image" />
<p><span>Allroads</span><br />
<span class="score" title="222 reputation points">222</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Allroads has one accepted answer">10%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '16, 20:34</strong> </span></p>
</div>
</div>
<div id="comments-container-53267" class="comments-container">
&#10;</div>
<div id="comment-tools-53267" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53267-form-container" class="comment-form-container">
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

<span id="53317"></span>

<div id="answer-container-53317" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53317-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>answered in <a href="https://josm.openstreetmap.de/ticket/14098">https://josm.openstreetmap.de/ticket/14098</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '16, 22:21</strong></p>
<img src="https://secure.gravatar.com/avatar/b904d75b8ea950f64710d2a8303cead7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Klumbumbus&#39;s gravatar image" />
<p><span>Klumbumbus</span><br />
<span class="score" title="543 reputation points">543</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Klumbumbus has one accepted answer">8%</span> </br></p>
</div>
</div>
<div id="comments-container-53317" class="comments-container">
<span id="53377"></span>
<div id="comment-53377" class="comment">
<div id="post-53377-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, to late here to fill it in as the answer.</p>
</div>
<div id="comment-53377-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 12:44)</span> <span class="comment-user userinfo">Allroads</span>
</div>
</div>
</div>
<div id="comment-tools-53317" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53317-form-container" class="comment-form-container">
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

