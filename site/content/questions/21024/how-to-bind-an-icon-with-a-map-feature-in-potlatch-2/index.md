+++
type = "question"
title = "How to bind an icon with a map feature in potlatch 2"
description = '''Is there any way by which I can use icons available in the SJJB SVG Map Icons library to bind them with Map features which don&#x27;t have any icons and are represented by a green dot in potlatch2?'''
date = "2013-03-27T12:09:00Z"
lastmod = "2013-03-28T00:32:00Z"
weight = 21024
keywords = [ "potlatch2", "map_features", "icon" ]
aliases = [ "/questions/21024" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to bind an icon with a map feature in potlatch 2](/questions/21024/how-to-bind-an-icon-with-a-map-feature-in-potlatch-2)

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
<span id="post-21024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21024-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-21024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there any way by which I can use icons available in the SJJB SVG Map Icons library to bind them with Map features which don't have any icons and are represented by a green dot in potlatch2?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-map_features" rel="tag" title="see questions tagged &#39;map_features&#39;">map_features</span> <span class="post-tag tag-link-icon" rel="tag" title="see questions tagged &#39;icon&#39;">icon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Mar '13, 12:09</strong></p>
<img src="https://secure.gravatar.com/avatar/4b30e201e971cc9afea52a9a436b0b9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ritwick&#39;s gravatar image" />
<p><span>Ritwick</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ritwick has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21024" class="comments-container">
<span id="21033"></span>
<div id="comment-21033" class="comment">
<div id="post-21033-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://www.sjjb.co.uk/mapicons/">http://www.sjjb.co.uk/mapicons/</a></p>
</div>
<div id="comment-21033-info" class="comment-info">
<span class="comment-age">(27 Mar '13, 18:48)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-21024" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21024-form-container" class="comment-form-container">
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

<span id="21040"></span>

<div id="answer-container-21040" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21040-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-21040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes!</p>
<p>However amending Potlatch2, will fix only Potlatch2 - it will have no effect on the maps rendered on <a href="http://openstreetmap.org/">http://openstreetmap.org/</a></p>
<p>To adjust just Potlatch2 you will have to run your own instance of Potlatch2, see:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Potlatch_2/Developer_Documentation">https://wiki.openstreetmap.org/wiki/Potlatch_2/Developer_Documentation</a></p>
<p>You will need to make amendments to the file: resources/stylesheets/core_pois.css</p>
<p>Looking at the code history within git, you should be able to see the way to amend Potlatch2. Such as my commit SHA1: ab28e8c69ee6e3091a01d8ab9bf276df5f974e6d</p>
<p>Having said that - development focus especially for 'simple' editing has shifted to the pure javascript iD editor: <a href="http://ideditor.com/">http://ideditor.com/</a></p>
<p>Thus you many need to reconsider your goals of what adding an icon in Potlatch2 will actually achieve.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '13, 00:32</strong></p>
<img src="https://secure.gravatar.com/avatar/074785ea4eae108f0e4e89456bf74737?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robbieonsea&#39;s gravatar image" />
<p><span>robbieonsea</span><br />
<span class="score" title="904 reputation points">904</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robbieonsea has 4 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '13, 00:34</strong> </span></p>
</div>
</div>
<div id="comments-container-21040" class="comments-container">
&#10;</div>
<div id="comment-tools-21040" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21040-form-container" class="comment-form-container">
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

