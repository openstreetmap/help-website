+++
type = "question"
title = "How to show the ship&#x27;s course"
description = '''I have a ship with course (for instance) : 284.7° (degree) Is it possible to show an arrow marker with the right direction?'''
date = "2012-05-23T10:02:00Z"
lastmod = "2012-05-23T11:41:00Z"
weight = 12888
keywords = [ "marker", "course", "degree", "arrow" ]
aliases = [ "/questions/12888" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to show the ship's course](/questions/12888/how-to-show-the-ships-course)

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
<span id="post-12888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12888-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a ship with course (for instance) : 284.7° (degree) Is it possible to show an arrow marker with the right direction?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-course" rel="tag" title="see questions tagged &#39;course&#39;">course</span> <span class="post-tag tag-link-degree" rel="tag" title="see questions tagged &#39;degree&#39;">degree</span> <span class="post-tag tag-link-arrow" rel="tag" title="see questions tagged &#39;arrow&#39;">arrow</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '12, 10:02</strong></p>
<img src="https://secure.gravatar.com/avatar/53ae7305bc592263d95a183ce4f90fde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="afterbit&#39;s gravatar image" />
<p><span>afterbit</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="afterbit has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12888" class="comments-container">
&#10;</div>
<div id="comment-tools-12888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12888-form-container" class="comment-form-container">
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

<span id="12889"></span>

<div id="answer-container-12889" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12889-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You would probably want to look at using Openlayers to add your own custom defined markers, I think?</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Openlayers_POI_layer_example">this example</a> as a very basic example for displaying your own markers. You would need to define the icons and update the textfile.txt as the direction of the ship changes to refer to the new icon. There are other examples <a href="https://wiki.openstreetmap.org/wiki/OpenLayers">on the wiki</a> and on the <a href="http://openlayers.org/dev/examples/">OpenLayers site</a> (although the latter aren't Openstreetmap specific).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '12, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-12889" class="comments-container">
<span id="12891"></span>
<div id="comment-12891" class="comment">
<div id="post-12891-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes.. i have to deal with custom markers.. i didn't found anything in the openstreemap examples.. but i think that i can do what i want, doing several markers (arrow markers) each one with a particular direction (in example : up arrow, down arrow, left.. right..) and then, depending on the ship course degree, load the right arrow..</p>
</div>
<div id="comment-12891-info" class="comment-info">
<span class="comment-age">(23 May '12, 11:04)</span> <span class="comment-user userinfo">afterbit</span>
</div>
</div>
<span id="12892"></span>
<div id="comment-12892" class="comment">
<div id="post-12892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I used custom markers once for a local pub map, with different markers for open, closed and for sale. I didn't have to update quite so often as you will though, so there may be better ways than that first example I mentioned.</p>
</div>
<div id="comment-12892-info" class="comment-info">
<span class="comment-age">(23 May '12, 11:11)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="12895"></span>
<div id="comment-12895" class="comment">
<div id="post-12895-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it would be enough, if there was a method to rotate the arrow marker icon.. so.. i should create only one arrow icon!!</p>
</div>
<div id="comment-12895-info" class="comment-info">
<span class="comment-age">(23 May '12, 11:41)</span> <span class="comment-user userinfo">afterbit</span>
</div>
</div>
</div>
<div id="comment-tools-12889" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12889-form-container" class="comment-form-container">
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

