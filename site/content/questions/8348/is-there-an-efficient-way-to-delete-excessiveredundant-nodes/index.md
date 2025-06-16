+++
type = "question"
title = "[closed] Is there an efficient way to delete excessive/redundant nodes?"
description = '''I am using OSM-Inspector quite a lot nowadays to check/correct not only my contributions to the OSM-DB but also to correct other peoples errors. It is a great tool.  To me it has become apparent that there are many redundant/excessive nodes in many ways and if I see one I will eliminate it. It would...'''
date = "2011-10-08T15:08:00Z"
lastmod = "2011-10-08T17:27:00Z"
weight = 8348
keywords = [ "nodes", "excessive", "redundant" ]
aliases = [ "/questions/8348" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Is there an efficient way to delete excessive/redundant nodes?](/questions/8348/is-there-an-efficient-way-to-delete-excessiveredundant-nodes)

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
<span id="post-8348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8348-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using OSM-Inspector quite a lot nowadays to check/correct not only my contributions to the OSM-DB but also to correct other peoples errors. It is a great tool. To me it has become apparent that there are many redundant/excessive nodes in many ways and if I see one I will eliminate it. It would be nice to have a JOSM-Plug-in the checks a marked way for these excessive nodes, highlights them, allow a de-highlighting, and a general delete of those nodes left highlighted.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-excessive" rel="tag" title="see questions tagged &#39;excessive&#39;">excessive</span> <span class="post-tag tag-link-redundant" rel="tag" title="see questions tagged &#39;redundant&#39;">redundant</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Oct '11, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/cd4569f9fa1aac11eb6b19d6de309ea6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dcp&#39;s gravatar image" />
<p><span>dcp</span><br />
<span class="score" title="721 reputation points">721</span><span title="37 badges"><span class="badge1">●</span><span class="badgecount">37</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dcp has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>09 Oct '11, 07:37</strong> </span></p>
</div>
</div>
<div id="comments-container-8348" class="comments-container">
<span id="8349"></span>
<div id="comment-8349" class="comment">
<div id="post-8349-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What are you defining as "excessive"?</p>
</div>
<div id="comment-8349-info" class="comment-info">
<span class="comment-age">(08 Oct '11, 15:37)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="8350"></span>
<div id="comment-8350" class="comment">
<div id="post-8350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have a look at relation=1369789 for an example. My guess that in this case up to 50% of the nodes are not required i.e. redundant.</p>
<p>If a way is straight and has three nodes then the middle node is redundant/excessive. It contributes nothing to the DB but does cost time to download each time it is viewed,etc.</p>
<p>I have no idea how many nodes could be eliminated but in the light of what is happening, see: <a href="https://www.openstreetmap.org/user/!i!/diary/15046">https://www.openstreetmap.org/user/!i!/diary/15046</a> the reduction of redundant nodes should be considered with some priority.</p>
</div>
<div id="comment-8350-info" class="comment-info">
<span class="comment-age">(08 Oct '11, 15:51)</span> <span class="comment-user userinfo">dcp</span>
</div>
</div>
<span id="8351"></span>
<div id="comment-8351" class="comment">
<div id="post-8351-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are you familiar with the built-in Tools/Simplify Way?</p>
</div>
<div id="comment-8351-info" class="comment-info">
<span class="comment-age">(08 Oct '11, 15:55)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
<span id="8352"></span>
<div id="comment-8352" class="comment not_top_scorer">
<div id="post-8352-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>no. is it a JOSM-plug-in?</p>
</div>
<div id="comment-8352-info" class="comment-info">
<span class="comment-age">(08 Oct '11, 16:00)</span> <span class="comment-user userinfo">dcp</span>
</div>
</div>
<span id="8353"></span>
<div id="comment-8353" class="comment">
<div id="post-8353-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think Tools/Simplify Way is native. Don't you have it in your menu?</p>
</div>
<div id="comment-8353-info" class="comment-info">
<span class="comment-age">(08 Oct '11, 16:03)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
<span id="8354"></span>
<div id="comment-8354" class="comment not_top_scorer">
<div id="post-8354-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have a JOSM German version and it does have shift-Y tool and the translation would be "Simplify Way", so yes you are right and thank-you. Big Question: Does it work on areas and multipolygons?</p>
</div>
<div id="comment-8354-info" class="comment-info">
<span class="comment-age">(08 Oct '11, 16:14)</span> <span class="comment-user userinfo">dcp</span>
</div>
</div>
<span id="8356"></span>
<div id="comment-8356" class="comment not_top_scorer">
<div id="post-8356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There seems to be no problem to select multiple ways/areas and run Simplify Way, but as always you have to be careful and manually watch that Simplify Way doesn't remove details you don't want to be removed. Especially curved ways may suffer from this.</p>
<p>Another, potential, data loss may occur if a mapper has mapped a straight way and marked to-be-further-tracked-later-road-crossings as extra nodes on that way. But many times it's obvious that the extra nodes are just mapping noise.</p>
</div>
<div id="comment-8356-info" class="comment-info">
<span class="comment-age">(08 Oct '11, 16:41)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
<span id="8357"></span>
<div id="comment-8357" class="comment not_top_scorer">
<div id="post-8357-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have just tried the "Simplify Way" tool on a Multipolygon with 1977 nodes and it reduced the number to 1489 which is a saving of 488 nodes or about a 25% reduction. That is just great. But is it safe to use. Am I destroying something i.e. doing more harm than good for I cannot check those 488 nodes individually. And why is it not being widely applied. The reduction of redundant data should be a priority.</p>
</div>
<div id="comment-8357-info" class="comment-info">
<span class="comment-age">(08 Oct '11, 16:41)</span> <span class="comment-user userinfo">dcp</span>
</div>
</div>
<span id="8360"></span>
<div id="comment-8360" class="comment">
<div id="post-8360-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Personally I suspect the best answer is to tackle the problem at source: apply strict rules to imports (such as the Corine one you pointed to) and mercilessly revert those that fail to abide by them.</p>
</div>
<div id="comment-8360-info" class="comment-info">
<span class="comment-age">(08 Oct '11, 17:17)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8348" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-8348-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, right answer was accepted" by dcp 09 Oct '11, 07:37

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8358"></span>

<div id="answer-container-8358" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8358-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not everything that OSM Inspector highlights is necessarily an error. There is no need to split ways (creating complicated relations), just because the way has more than 1900 nodes.</p>
<p>The number of nodes in a way has nothing to do with load on the tile server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '11, 16:45</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-8358" class="comments-container">
<span id="8362"></span>
<div id="comment-8362" class="comment">
<div id="post-8362-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Then I just don't understand the logic of the program. OSM-Inspector should only show errors. If it highlights valid data as well as errors why should I take the time to look at it. It becomes a puzzle and not a tool. Obviously I am not qualified to make judgement on the tile server load. I did not know that the sum of all nodes has no effect on the on the tile server load. Sorry!</p>
</div>
<div id="comment-8362-info" class="comment-info">
<span class="comment-age">(08 Oct '11, 17:27)</span> <span class="comment-user userinfo">dcp</span>
</div>
</div>
</div>
<div id="comment-tools-8358" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8358-form-container" class="comment-form-container">
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

