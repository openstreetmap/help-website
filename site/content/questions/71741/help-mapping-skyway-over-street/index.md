+++
type = "question"
title = "Help mapping skyway over street"
description = '''The skyway in question is here. I searched here for skyway and found an old discussion of the famous Bridge of Sighs in Oxford. However, that bridge has the same problem. Despite the bridge:covered, layer=1, building:levels=3 and building:min_level=3, the feature warns that the footpath below and We...'''
date = "2019-11-19T22:13:00Z"
lastmod = "2019-11-21T12:34:00Z"
weight = 71741
keywords = [ "bridge", "skyway" ]
aliases = [ "/questions/71741" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Help mapping skyway over street](/questions/71741/help-mapping-skyway-over-street)

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
<span id="post-71741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71741-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The skyway in question is <a href="https://www.openstreetmap.org/way/426660134" title="skyway">here</a>.</p>
<p>I searched here for skyway and found an old discussion of the famous Bridge of Sighs in Oxford. However, that bridge has the same problem. Despite the bridge:covered, layer=1, building:levels=3 and building:min_level=3, the feature warns that the footpath below and West Church St both cross it without a proper junction. In other areas, naming something a bridge immediately cleared out this error. Is there a better way to map this so that it doesn't conflict with the ways below it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-skyway" rel="tag" title="see questions tagged &#39;skyway&#39;">skyway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '19, 22:13</strong></p>
<img src="https://secure.gravatar.com/avatar/2281ea962de38f5a54d199aa10202eca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tanderson92&#39;s gravatar image" />
<p><span>tanderson92</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tanderson92 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71741" class="comments-container">
&#10;</div>
<div id="comment-tools-71741" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71741-form-container" class="comment-form-container">
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

<span id="71742"></span>

<div id="answer-container-71742" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71742-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It isn't clear what's warning you about the crossing, but the JOSM validator is fine with it. The important tag is layer, which is correctly describing the vertical layout of the various ways (West Church Street and the sidewalks at the implied layer=0, and the bridge above them at layer=1).</p>
<p>One thing you should consider changing, though, is the highway tag. Currently, it's tagged as a pedestrianized road, which seems unlikely for an elevated walkway (unless vehicles do have access to that level and can use the bridge, in which case it's fine). However, if the bridge is only for foot traffic, then highway=footway would be the best tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '19, 23:36</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-71742" class="comments-container">
<span id="71745"></span>
<div id="comment-71745" class="comment">
<div id="post-71745-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would also say that the level tags are wrong. That shouldn't have any influence on the validator message, though. If the skyway is on the third level it should be building:levels=3 and Building:min_level=2. Have look at the illustration on the <a href="https://wiki.openstreetmap.org/wiki/Key:building:levels">wiki</a>.</p>
<p>Thinking about it I would probably separate the skyway structure as a building from the path leading trough it. Currently you have a highway=pedestrian that is not connected to any other navigable path or road.</p>
</div>
<div id="comment-71745-info" class="comment-info">
<span class="comment-age">(20 Nov '19, 08:25)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="71750"></span>
<div id="comment-71750" class="comment">
<div id="post-71750-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>IMO unless (until?) the bridge in question is actually routable -- ie, connected to other <code>highway=*</code> ways -- there's no reason to tag it as a highway at all. I'd suggest mapping it as a <code>layer=1</code> building (or making it a building:part of one or more of the buildings it connects to -- then those get the layer tag) and tagging it with <code>height=*</code>, <code>min_height=*</code>, and <code>indoor=corridor</code>.</p>
</div>
<div id="comment-71750-info" class="comment-info">
<span class="comment-age">(20 Nov '19, 18:44)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-71742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71742-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71749"></span>

<div id="answer-container-71749" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71749-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for the replies. I'm editing in ID and see the warnings there. I agree after reading the wiki that min_level=2 should apply.</p>
<p>I was trying to edit the original editor's work which was the pedestrian area with a disconnected footpath through it. It seems that isn't the best course of action.</p>
<p>Starting from scratch, then, how should I draw this building that connects the other two buildings on the third floor?</p>
<p>Thank you again for the assistance.</p>
<p><img src="https://i.postimg.cc/50F8LfVF/osm-error.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Nov '19, 15:21</strong></p>
<img src="https://secure.gravatar.com/avatar/2281ea962de38f5a54d199aa10202eca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tanderson92&#39;s gravatar image" />
<p><span>tanderson92</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tanderson92 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-71749" class="comments-container">
&#10;</div>
<div id="comment-tools-71749" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71749-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71759"></span>

<div id="answer-container-71759" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71759-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-71759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could add covered=yes to the ways running below. (Or, for more accuracy, split the ways and tag the parts under the bridge as covered=yes.)</p>
<p>That clears the warning, and provides a bit of extra detail to the database.</p>
<p>But it could be that iD is misbehaving a bit here in displaying these warnings in the first place.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '19, 11:18</strong></p>
<img src="https://secure.gravatar.com/avatar/b5c5070032df7883181003f187eacae0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spiregrain&#39;s gravatar image" />
<p><span>spiregrain</span><br />
<span class="score" title="183 reputation points">183</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spiregrain has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71759" class="comments-container">
<span id="71760"></span>
<div id="comment-71760" class="comment">
<div id="post-71760-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I wouldn't call a road or path where a buidling crosses two floors up "covered". So I discourage tagging it that way. In any case don't tag "something" to get rid of a warning. It's only a warning after all.</p>
</div>
<div id="comment-71760-info" class="comment-info">
<span class="comment-age">(21 Nov '19, 12:34)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-71759" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71759-form-container" class="comment-form-container">
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

