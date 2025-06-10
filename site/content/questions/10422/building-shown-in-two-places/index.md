+++
type = "question"
title = "Building shown in two places"
description = '''The Schönwieshütte in Obergurgl, Austria, is shown in two places. A closed way (way 92335833, at N46.84755° E11.01670°) shows the outline of a building, in the position where I found the hut last week. A node named Schönwieshütte (node 476907198, at N46.84820°, E11.01563°) is about 100m away, but co...'''
date = "2012-02-05T16:03:00Z"
lastmod = "2012-02-08T22:39:00Z"
weight = 10422
keywords = [ "building", "twice", "shown" ]
aliases = [ "/questions/10422" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Building shown in two places](/questions/10422/building-shown-in-two-places)

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
<span id="post-10422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10422-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The Schönwieshütte in Obergurgl, Austria, is shown in two places. A closed way (way 92335833, at N46.84755° E11.01670°) shows the outline of a building, in the position where I found the hut last week. A node named Schönwieshütte (node 476907198, at N46.84820°, E11.01563°) is about 100m away, but contains a wealth of additional information that should not be lost. Can anyone advise me of tbe best way to resolve this inconsistency, bearing in mind that I am still a beginner and haven't mastered JOSM yet?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-twice" rel="tag" title="see questions tagged &#39;twice&#39;">twice</span> <span class="post-tag tag-link-shown" rel="tag" title="see questions tagged &#39;shown&#39;">shown</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '12, 16:03</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-10422" class="comments-container">
&#10;</div>
<div id="comment-tools-10422" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10422-form-container" class="comment-form-container">
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

<span id="10429"></span>

<div id="answer-container-10429" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10429-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Madryn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a better, easier, faster way than Vclaw's answer as of recently, thanks to the <strong>utilsplugin2</strong> plugin for JOSM.</p>
<p>Download and start JOSM from <a href="http://josm.openstreetmap.de/">here</a>, then:</p>
<ol>
<li>Install the <em>utilsplugins2</em> plugin and restart JOSM (<a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins#With_the_plugin_manager">help</a>)</li>
<li>Download the area which has the two objects (<a href="http://wiki.openstreetmap.org/wiki/JOSM/Guide#Download_data">help</a>)</li>
<li>Select both the node and the way using <strong><code>Shift+Click</code></strong> (<a href="http://josm.openstreetmap.de/wiki/Help/Action/Move/Move#Selectingsingleobjects">help</a>)</li>
<li>Go to the <strong>More tools</strong> menu, and select <strong>Replace Geometry</strong> ((<a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/utilsplugin2#Replace_Geometry">help</a>)</li>
<li>If both objects have tags, a dialog will appear so you can check and merge the differences (no help yet))</li>
</ol>
<p>The way Vclaw describes is how I used to do this, but I've recently added functionality to the utilsplugin2 to do this all in one step, with the addition of resolving tag conflicts and preserving history. Note that <strong>Replace Geometry</strong> can also replace or <em>upgrade</em> a node to a multipolygon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '12, 19:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ba99ad3778972fee07700e1eb36cc822?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoshD&#39;s gravatar image" />
<p><span>JoshD</span><br />
<span class="score" title="300 reputation points">300</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoshD has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-10429" class="comments-container">
&#10;</div>
<div id="comment-tools-10429" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10429-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10423"></span>

<div id="answer-container-10423" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10423-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In JOSM:</p>
<ol>
<li>Select the node for the building</li>
<li>Go to the Edit menu, and select <em>Copy</em> (or press Ctrl + C)</li>
<li>Select the way for the building outline</li>
<li>Go to the Edit menu, and select <em>Paste Tags</em> (or Ctrl + Shift + V)</li>
<li>You can then check all of the tags are correct, and delete the node</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '12, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-10423" class="comments-container">
<span id="10433"></span>
<div id="comment-10433" class="comment">
<div id="post-10433-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. The method that you described copied the tags from the isolated node to the building outline. However, I notice that the node is a member of a network, whereas the building outline is not. As I am not really sure what that means, I am reluctant to delete the original node, even though it is not quite in the right place. Further advice would be appreciated.</p>
</div>
<div id="comment-10433-info" class="comment-info">
<span class="comment-age">(05 Feb '12, 23:18)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
<span id="10436"></span>
<div id="comment-10436" class="comment">
<div id="post-10436-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It should be safe to transfer the relation membership from the node to the way. I need to modify the utilsplugin2 to allow replacing geometry with nodes that have relation memberships.</p>
</div>
<div id="comment-10436-info" class="comment-info">
<span class="comment-age">(06 Feb '12, 02:32)</span> <span class="comment-user userinfo">JoshD</span>
</div>
</div>
<span id="10437"></span>
<div id="comment-10437" class="comment">
<div id="post-10437-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just updated the Replace Geometry so it can now work in this situation. I tested it with the node and way you mentioned, and it seems to work well. I didn't upload the change as I thought you might want to do it. It might take a few hours to be available, but try updating plugins tomorrow and it should work.</p>
</div>
<div id="comment-10437-info" class="comment-info">
<span class="comment-age">(06 Feb '12, 03:25)</span> <span class="comment-user userinfo">JoshD</span>
</div>
</div>
<span id="10500"></span>
<div id="comment-10500" class="comment">
<div id="post-10500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again. It seems to have done what was wanted.</p>
</div>
<div id="comment-10500-info" class="comment-info">
<span class="comment-age">(08 Feb '12, 22:39)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
</div>
<div id="comment-tools-10423" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10423-form-container" class="comment-form-container">
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

