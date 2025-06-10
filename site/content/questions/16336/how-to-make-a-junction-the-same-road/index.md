+++
type = "question"
title = "How to make a junction the same road"
description = '''Hi I am trying to make this junction the same road (for naming purposes), whatever i do OSM is treating them as two distinct roads. Do I need to go with it and name the two distinct roads the same? '''
date = "2012-09-22T08:16:00Z"
lastmod = "2012-09-22T09:27:00Z"
weight = 16336
keywords = [ "junction" ]
aliases = [ "/questions/16336" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to make a junction the same road](/questions/16336/how-to-make-a-junction-the-same-road)

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
<span id="post-16336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16336-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I am trying to make this junction the same road (for naming purposes), whatever i do OSM is treating them as two distinct roads.</p>
<p>Do I need to go with it and name the two distinct roads the same?</p>
<p><img src="http://help.openstreetmap.org/upfiles/street_1.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-junction" rel="tag" title="see questions tagged &#39;junction&#39;">junction</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '12, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/5db419541220e06ec64e2a3b2abfe1c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FranklyPop&#39;s gravatar image" />
<p><span>FranklyPop</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FranklyPop has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Sep '12, 08:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span></p>
</div>
</div>
<div id="comments-container-16336" class="comments-container">
&#10;</div>
<div id="comment-tools-16336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16336-form-container" class="comment-form-container">
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

<span id="16338"></span>

<div id="answer-container-16338" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16338-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="http://www.openstreetmap.org/browse/way/182321711">way to the left</a> is a strange t-shaped way, rather than a straight way.</p>
<p><img src="http://farm9.staticflickr.com/8035/8011359922_8568a733b9_o_d.jpg" alt="182321711" /></p>
<p>This is because when originally drawn the way went back on itself. I would delete <a href="http://www.openstreetmap.org/browse/node/1926740093">the node</a> where the two ways join, and then extend what remains of <a href="http://www.openstreetmap.org/browse/way/182321713">this way</a> to join the original one.</p>
<p>As they have the same name as each other, as Andy says you can use R to copy the tags from one way to the other; they will need tagging separately and be treated as separate ways though because of the geometry.</p>
<p>I also notice <a href="http://www.openstreetmap.org/browse/way/182321712">this short untagged way</a> that shows as a black line in my image below. You might just want to delete that as it is on top of the first way mentioned above.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '12, 08:45</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</img>
</div>
</div>
<div id="comments-container-16338" class="comments-container">
&#10;</div>
<div id="comment-tools-16338" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16338-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16339"></span>

<div id="answer-container-16339" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16339-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On a general level, you shouldn't worry about concepts of "the same road".</p>
<p>If two roads join and have the same name, that's enough. They might be different in other ways: one might have a road number, the other might not; one might be a bridge, the other might not; one might be on a cycle route, the other might not.</p>
<p>So just make sure the name is right and don't worry about joining the roads.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '12, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-16339" class="comments-container">
&#10;</div>
<div id="comment-tools-16339" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16339-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16337"></span>

<div id="answer-container-16337" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16337-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Potlatch2 as an "R" function which will copy the lasts tags to the next. or highlight the first bit hold Ctrl and click on next bit and that should join then into one.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '12, 08:36</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Sep '12, 08:40</strong> </span></p>
</div>
</div>
<div id="comments-container-16337" class="comments-container">
&#10;</div>
<div id="comment-tools-16337" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16337-form-container" class="comment-form-container">
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

