+++
type = "question"
title = "JOSM: How to stretch a line, and keep the direction constant?"
description = '''Suppose you have two points A and B and a line l between them. Further suppose that the underlying &quot;real linear thing&quot; that should be represented in OSM is a bit longer (shorter) than the current line l and you want to stretch it a bit, but keeping the direction fixed. Speaking mathematically, you w...'''
date = "2015-12-30T22:17:00Z"
lastmod = "2016-01-04T19:56:00Z"
weight = 47337
keywords = [ "josm", "line", "editing", "linear" ]
aliases = [ "/questions/47337" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM: How to stretch a line, and keep the direction constant?](/questions/47337/josm-how-to-stretch-a-line-and-keep-the-direction-constant)

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
<span id="post-47337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47337-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Suppose you have two points A and B and a line l between them. Further suppose that the underlying "real linear thing" that should be represented in OSM is a bit longer (shorter) than the current line l and you want to stretch it a bit, but keeping the direction fixed.</p>
<p>Speaking mathematically, you want to move point B to a point B'= A + (B-A)*r, r being a real number, r&gt;0 (and r&lt;&gt;1 to exclude the identity transformation).</p>
<p>I don't care about r being too exact, but I want the direction (B-A) to be fixed. If I just move my point B with the mouse, it will always change the direction at least a bit. How can I keep it fixed?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-line" rel="tag" title="see questions tagged &#39;line&#39;">line</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-linear" rel="tag" title="see questions tagged &#39;linear&#39;">linear</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '15, 22:17</strong></p>
<img src="https://secure.gravatar.com/avatar/00e0d3bc884e0a083f0fc0aca5b9449f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Warden&#39;s gravatar image" />
<p><span>Warden</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Warden has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47337" class="comments-container">
&#10;</div>
<div id="comment-tools-47337" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47337-form-container" class="comment-form-container">
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

<span id="47369"></span>

<div id="answer-container-47369" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47369-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another solution, IMHO more straightforward than Hendrikklaas and aseerel4c26's, is to <a href="http://josm.openstreetmap.de/wiki/Help/Action/Extrude#Movenode">switch to extrude mode (x) and then move the node while pressing Ctrl</a>. Shows guidelines, and lets you choose between angles when the node is connected to more than one way segment.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '16, 17:40</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-47369" class="comments-container">
<span id="47370"></span>
<div id="comment-47370" class="comment">
<div id="post-47370-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are plenty of cool moves possible in extrude mode, check the docs :)</p>
</div>
<div id="comment-47370-info" class="comment-info">
<span class="comment-age">(04 Jan '16, 17:41)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="47371"></span>
<div id="comment-47371" class="comment">
<div id="post-47371-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I never really tried it – only switched it on sometimes accidentally. Thanks, this looks really useful! :-) Pressing Ctrl before moving the node is the key. The non-Ctrl moves never <em>seemed</em> that useful to me.</p>
</div>
<div id="comment-47371-info" class="comment-info">
<span class="comment-age">(04 Jan '16, 19:56)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47369" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47369-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47342"></span>

<div id="answer-container-47342" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47342-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>a bit of a workaround I use often:</p>
<ul>
<li>extension: select B and press key A on you keyboard twice. Then the <a href="https://josm.openstreetmap.de/wiki/Help/Action/Draw#Anglesnapping">angle snapping</a> is active - you can easily select the 0° for placement of a new node. If you want to eliminate the original node, move it to B' and press the M key to merge both (the node id of B should be kept automatically). <span>Screenshot</span> just before the addition of B'.</li>
<li>contraction: just insert a new node by clicking (in insert mode) on the line between A and B. Again, merge if necessary.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Dec '15, 00:26</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Dec '15, 00:29</strong> </span></p>
</div>
</div>
<div id="comments-container-47342" class="comments-container">
&#10;</div>
<div id="comment-tools-47342" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47342-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47341"></span>

<div id="answer-container-47341" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47341-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-47341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Warden, Use JOSM to make this happen. Copy the old line and drop it beside. Draw an extra line twice as long as you want the new one to be. Position the line by using control + shift + mouse pointer to match the direction of the old one. (try it) Draw the new one over the extra one and if it matches your desires, delete the extra one and the copy you’ve made for the original direction. Or copy and paste your old line in your usual programm, put them next to each other and join them into one line.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Dec '15, 00:24</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Dec '15, 00:30</strong> </span></p>
</div>
</div>
<div id="comments-container-47341" class="comments-container">
<span id="47343"></span>
<div id="comment-47343" class="comment">
<div id="post-47343-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the question <em>is</em> about JOSM (see the tags and title prefix) @ "Use JOSM to make this happen"</p>
</div>
<div id="comment-47343-info" class="comment-info">
<span class="comment-age">(31 Dec '15, 00:26)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47341" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47341-form-container" class="comment-form-container">
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

