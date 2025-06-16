+++
type = "question"
title = "Overpass output to kml = shape zigzagged"
description = '''I&#x27;m producing an interpreter file using the command from another question. That file I then parse with php...  Iterate relation, then in the order the ways are printed I read their ref, take the referenced way, then I iterate the nodes of the way and read each node in the order it was printed.  The ...'''
date = "2013-04-16T23:06:00Z"
lastmod = "2013-04-17T07:37:00Z"
weight = 21613
keywords = [ "overpass", "kml", "order", "coordinates" ]
aliases = [ "/questions/21613" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass output to kml = shape zigzagged](/questions/21613/overpass-output-to-kml-shape-zigzagged)

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
<span id="post-21613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21613-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm producing an interpreter file using the command from <a href="/questions/21555/overpass-get-output-structured-with-hierarchy-not-flat">another question</a>.</p>
<p>That file I then parse with php... Iterate relation, then in the order the ways are printed I read their ref, take the referenced way, then I iterate the nodes of the way and read each node in the order it was printed.</p>
<p>The lon and lat of each node I then put into a string like that</p>
<pre><code>lon1,lat1,0
lon2,lat2,0 
lon3,lat3,0</code></pre>
<p>and so forth</p>
<p>This I then put into the coordinates tag of a kml file.</p>
<p>Now it seems that the order of the coordinates isn't correct, because the created shape in google maps is not closed but zigzagged :( (not all of it though, most part is correct)</p>
<p>Is this normal ? What should I do ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span> <span class="post-tag tag-link-order" rel="tag" title="see questions tagged &#39;order&#39;">order</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Apr '13, 23:06</strong></p>
<img src="https://secure.gravatar.com/avatar/889a2f870eec6bc61e706e0de1645b6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SeWo&#39;s gravatar image" />
<p><span>SeWo</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SeWo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '13, 23:11</strong> </span></p>
</div>
</div>
<div id="comments-container-21613" class="comments-container">
&#10;</div>
<div id="comment-tools-21613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21613-form-container" class="comment-form-container">
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

<span id="21618"></span>

<div id="answer-container-21618" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21618-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SeWo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general, you first must stich the ways one to another. One possible way to do so is to keep an associative array of all first and last node ids in each way and to construct a single consecutive path by traversing the nodes of the ways this way. It is in general not guaranteed that the ways are in order or have the right orientation, but it is quite safe to assume that a valid area passes each node only once.</p>
<p>I'm sorry that this is somehow vague, but I'm not familiar with PHP. But as even JavaScript has associative arrays, I'm quite sure they exist in PHP.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Apr '13, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-21618" class="comments-container">
&#10;</div>
<div id="comment-tools-21618" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21618-form-container" class="comment-form-container">
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

