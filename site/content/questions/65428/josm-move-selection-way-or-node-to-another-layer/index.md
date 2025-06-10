+++
type = "question"
title = "JOSM - Move selection (way or node) to another layer"
description = '''I am currently working on a large area and have made temporary straight lines to mark areas that need drawing (like a road or river drawing continuation). I did this as I have very limited data right now and am trying to conserve it by not auto loading the imagery tiles. Now, I have decided to uploa...'''
date = "2018-08-18T20:13:00Z"
lastmod = "2018-08-19T18:39:00Z"
weight = 65428
keywords = [ "selection", "josm", "layer", "move" ]
aliases = [ "/questions/65428" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM - Move selection (way or node) to another layer](/questions/65428/josm-move-selection-way-or-node-to-another-layer)

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
<span id="post-65428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65428-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently working on a large area and have made temporary straight lines to mark areas that need drawing (like a road or river drawing continuation). I did this as I have very limited data right now and am trying to conserve it by not auto loading the imagery tiles.</p>
<p>Now, I have decided to upload a changeset containing just some of those drawn features, but have these temporary lines/markings within the same layer. I realize I should have made a separate layer for these markings/lines in the first place. As I plan to continue the unfinished road and river lines later on, I do not really want to delete these line markings, but just want to move them to another layer.</p>
<p>Problem is I cannot find any option to move a selection to another layer. Any help on this matter would be greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-selection" rel="tag" title="see questions tagged &#39;selection&#39;">selection</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-move" rel="tag" title="see questions tagged &#39;move&#39;">move</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '18, 20:13</strong></p>
<img src="https://secure.gravatar.com/avatar/fb34d7bed35464f64bba89dba8f34f95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JAT86&#39;s gravatar image" />
<p><span>JAT86</span><br />
<span class="score" title="240 reputation points">240</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JAT86 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65428" class="comments-container">
&#10;</div>
<div id="comment-tools-65428" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65428-form-container" class="comment-form-container">
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

<span id="65429"></span>

<div id="answer-container-65429" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65429-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-65429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JAT86 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For your newly (not uploaded yet) created "temporary lines/markings" I think these steps are most simple. Note that this requires that all <em>objects</em> which should be moved are in fact <em>new</em> (see comments).</p>
<ol>
<li>Select the objects,</li>
<li>copy them (ctrl+C or via edit menu),</li>
<li>create a new data layer via the file menu (it is selected as the active/edited layer automatically),</li>
<li>paste at source position (ctrl+alt+v) (or via edit menu)</li>
<li>activate the original layer (via <a href="https://josm.openstreetmap.de/wiki/Help/Dialog/LayerList">layer window</a>)</li>
<li>delete the selected objects</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '18, 22:21</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Aug '18, 18:56</strong> </span></p>
</div>
</div>
<div id="comments-container-65429" class="comments-container">
<span id="65430"></span>
<div id="comment-65430" class="comment">
<div id="post-65430-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Alternatively (not an answer to your question) you could only upload the currently selected objects (via the File menu).</p>
</div>
<div id="comment-65430-info" class="comment-info">
<span class="comment-age">(18 Aug '18, 22:22)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="65434"></span>
<div id="comment-65434" class="comment">
<div id="post-65434-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> note that copying will create new objects from any pre-existing objects. In general I would suggest that the Merge Selection option suggested by <a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a> is a better way of doing this.</p>
</div>
<div id="comment-65434-info" class="comment-info">
<span class="comment-age">(19 Aug '18, 11:15)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="65442"></span>
<div id="comment-65442" class="comment">
<div id="post-65442-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>shouldn’t you purge rather than delete, in step 6?</p>
</div>
<div id="comment-65442-info" class="comment-info">
<span class="comment-age">(19 Aug '18, 14:10)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="65451"></span>
<div id="comment-65451" class="comment">
<div id="post-65451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53"></a><a href="https://help.openstreetmap.org/users/647/sk53">@Sk53</a> and <a href="https://help.openstreetmap.org/users/936/dieterdreist"></a><a href="https://help.openstreetmap.org/users/936/dieterdreist">@dieterdreist</a>: thanks, you are both right - but we were talking about newly (not uploaded yet) created "temporary lines/markings", so in my opinion my suggested actions are a bit simpler, straight forward, and sufficient. Of course, this requires the assumption that all objects which should be moved are in fact <em>new</em>.</p>
</div>
<div id="comment-65451-info" class="comment-info">
<span class="comment-age">(19 Aug '18, 18:39)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65429" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65429-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65431"></span>

<div id="answer-container-65431" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65431-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-65431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If multiple layers are open: From the <em>Edit</em> menu select <em>Merge selection</em> (Ctrl+Shift+M) and select your construction layer as destination.</p>
<p>Once you check that everything made it across you can then go back to your main data layer and delete the items.</p>
<p>IIRC if you have saved a layer locally you can go into it in a text editor and flag it as being ineligible for upload so that JOSM doesn't nag you about non-uploaded changes on it when you exit (you will have to close and re-load it).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '18, 23:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-65431" class="comments-container">
&#10;</div>
<div id="comment-tools-65431" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65431-form-container" class="comment-form-container">
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

