+++
type = "question"
title = "What file defines osm&#x27;s openlayers data style?"
description = '''Or said differently, where can i edit the style of my data in the view panel (i have a private osm server)? EDIT: It&#x27;s the openlayer&#x27;s color scheme file that i need, i think. For more explanation: it&#x27;s the lines that appear after you check the &quot;data&quot; layer in the top right panel.'''
date = "2011-11-15T11:10:00Z"
lastmod = "2011-11-15T13:47:00Z"
weight = 9005
keywords = [ "styles", "openlayers" ]
aliases = [ "/questions/9005" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What file defines osm's openlayers data style?](/questions/9005/what-file-defines-osms-openlayers-data-style)

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
<span id="post-9005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9005-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Or said differently, where can i edit the style of my data in the view panel (i have a private osm server)?</p>
<p>EDIT: It's the openlayer's color scheme file that i need, i think. For more explanation: it's the lines that appear after you check the "data" layer in the top right panel.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-styles" rel="tag" title="see questions tagged &#39;styles&#39;">styles</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '11, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/dc9b01669c0702f230fa57c384b947a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexz&#39;s gravatar image" />
<p><span>alexz</span><br />
<span class="score" title="225 reputation points">225</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '11, 09:02</strong> </span></p>
</div>
</div>
<div id="comments-container-9005" class="comments-container">
&#10;</div>
<div id="comment-tools-9005" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9005-form-container" class="comment-form-container">
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

<span id="9010"></span>

<div id="answer-container-9010" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9010-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming rendering is done with mapnik, you need to edit the <a href="http://wiki.openstreetmap.org/wiki/Mapnik#Customizing_the_rendering">xml style</a> file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '11, 13:33</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-9010" class="comments-container">
<span id="9012"></span>
<div id="comment-9012" class="comment">
<div id="post-9012-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No no, not rendering. The data layer wich is turned of by default in the view panel.</p>
</div>
<div id="comment-9012-info" class="comment-info">
<span class="comment-age">(15 Nov '11, 13:47)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
</div>
<div id="comment-tools-9010" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9010-form-container" class="comment-form-container">
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

