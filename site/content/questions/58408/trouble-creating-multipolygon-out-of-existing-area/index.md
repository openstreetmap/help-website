+++
type = "question"
title = "Trouble creating multipolygon out of existing area"
description = '''I am trying to edit the lake/wood in this part of the map https://www.openstreetmap.org/#map=17/41.42816/-96.58204 I have figured out how to create multipolygons to create &quot;holes&quot; in the wood, but I can&#x27;t find a way to merge the lake and wood to make them exclusive. Every time I merge them I get eit...'''
date = "2017-08-19T21:57:00Z"
lastmod = "2017-08-22T21:45:00Z"
weight = 58408
keywords = [ "ideditor", "editing", "multipolygon" ]
aliases = [ "/questions/58408" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Trouble creating multipolygon out of existing area](/questions/58408/trouble-creating-multipolygon-out-of-existing-area)

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
<span id="post-58408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58408-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to edit the lake/wood in this part of the map</p>
<p><a href="https://www.openstreetmap.org/#map=17/41.42816/-96.58204">https://www.openstreetmap.org/#map=17/41.42816/-96.58204</a></p>
<p>I have figured out how to create multipolygons to create "holes" in the wood, but I can't find a way to merge the lake and wood to make them exclusive. Every time I merge them I get either a giant lake/wood covering the entire area or a bunch of "lines" on the former lake area that I can't turn back into an area.</p>
<p>I'm using the iD editor.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '17, 21:57</strong></p>
<img src="https://secure.gravatar.com/avatar/8b07651d96eaa86616db040853ef6d45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lordgilman&#39;s gravatar image" />
<p><span>lordgilman</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lordgilman has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '17, 22:04</strong> </span></p>
</div>
</div>
<div id="comments-container-58408" class="comments-container">
&#10;</div>
<div id="comment-tools-58408" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58408-form-container" class="comment-form-container">
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

<span id="58415"></span>

<div id="answer-container-58415" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58415-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lordgilman has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>iD has support for editing the Wood relation directly rather than trying to use the merge tool (which seems to have difficulty with merging the relations). It seems the most difficult part is selecting the Dam, the only way I can figure how to do it is to first select another part of the lake, select the lake relation from there and then select the Dam from the relation members panel:</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screenshot_2017-08-20_09-57-47-dam.png" alt="alt text" /></p>
<p>Once the Dam is selected, use the "All relations" panel to add the Dam to the "Wood" relation with role inner:</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screenshot_2017-08-20_09-59-46-select-wood.png" alt="alt text" /></p>
<p>Then add the other two parts of the lake to the wood relation the same way.</p>
<p>If there are multiple wood relations, a temporary name on the relation of interest can make the whole process simpler, just make sure to delete the name before saving.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '17, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</img>
</div>
</div>
<div id="comments-container-58415" class="comments-container">
<span id="58470"></span>
<div id="comment-58470" class="comment">
<div id="post-58470-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Regarding the issue you mentioned with selection: in iD you can click on a node used by both ways, then use the \ key to cycle through the ways which use that node.</p>
</div>
<div id="comment-58470-info" class="comment-info">
<span class="comment-age">(22 Aug '17, 15:16)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="58476"></span>
<div id="comment-58476" class="comment">
<div id="post-58476-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Adding the wood relation by hand on all the parts worked great!</p>
</div>
<div id="comment-58476-info" class="comment-info">
<span class="comment-age">(22 Aug '17, 21:45)</span> <span class="comment-user userinfo">lordgilman</span>
</div>
</div>
</div>
<div id="comment-tools-58415" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58415-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="58412"></span>

<div id="answer-container-58412" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58412-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't use the iD editor preferring JOSM so can't comment directly about iD But, the difference between the lake and other areas added to the wood multipolygon, is that the lake is itself a multipolygon. The lake is made up of three parts, (two parts described by the multipolygon and one (the Dam) described on the individual way). One way over this problem is to delete the lake multipolygon, make the lake an area described/outlined by a single enclosing line with of course its own tagging, draw/keep the dam as a separate linear feature, (it can be on-top of the lake polygon. Then add the lake (now a single line polygon same as the other areas) to the wood multipolygon. This method works with JOSM, hope it helps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '17, 07:26</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</img>
</div>
</div>
<div id="comments-container-58412" class="comments-container">
&#10;</div>
<div id="comment-tools-58412" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58412-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="58413"></span>

<div id="answer-container-58413" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58413-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using Josm as I am unfamiliar with iD:<br />
If you wish to leave the reservoir multi-polygon as is you can:<br />
Open a relations window, select the wood multi-polygon, select the relations editor in the relations window, right-click on the Camp Red Cedars reservoir multi-polygon in the relations window and select relation, then in the relations editor add the reservoir to the left side panel, add an inner role to it, then ok and save. I didn't save the above to check but it should work ok.<br />
An image may help...<br />
<img src="https://help.openstreetmap.org/upfiles/Screen_Shot_2017-08-20_at_6.01.22_PM.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '17, 08:54</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Aug '17, 16:38</strong> </span></p>
</div>
</div>
<div id="comments-container-58413" class="comments-container">
&#10;</div>
<div id="comment-tools-58413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58413-form-container" class="comment-form-container">
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

