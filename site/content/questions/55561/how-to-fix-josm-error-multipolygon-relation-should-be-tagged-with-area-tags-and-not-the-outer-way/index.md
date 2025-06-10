+++
type = "question"
title = "How to fix josm error Multipolygon relation should be tagged with area tags and not the outer way"
description = '''Hi, I was verifying the Josm validation of an area and I get the error &quot;Multipolygon relation should be tagged with area tags and not the outer way&quot; with the relation 2678858. Tried adding area tags like natural=water to the relation but it still gives me the error.'''
date = "2017-04-11T15:05:00Z"
lastmod = "2017-04-16T13:46:00Z"
weight = 55561
keywords = [ "validation", "josm", "mutlpolygon", "relations", "error" ]
aliases = [ "/questions/55561" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to fix josm error Multipolygon relation should be tagged with area tags and not the outer way](/questions/55561/how-to-fix-josm-error-multipolygon-relation-should-be-tagged-with-area-tags-and-not-the-outer-way)

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
<span id="post-55561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55561-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I was verifying the Josm validation of an area and I get the error "Multipolygon relation should be tagged with area tags and not the outer way" with the <a href="http://www.openstreetmap.org/relation/2678858">relation 2678858</a>. Tried adding area tags like <code>natural=water</code> to the relation but it still gives me the error.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-validation" rel="tag" title="see questions tagged &#39;validation&#39;">validation</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-mutlpolygon" rel="tag" title="see questions tagged &#39;mutlpolygon&#39;">mutlpolygon</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '17, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/c00d824b35f2315d60ff827eee2a93d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="persep&#39;s gravatar image" />
<p><span>persep</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="persep has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55561" class="comments-container">
<span id="55565"></span>
<div id="comment-55565" class="comment">
<div id="post-55565-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>On your particular relation you need to add natural=water to the relation tags and delete that tag from the outer way. The place=islet tag is correctly placed on the inner way.</p>
</div>
<div id="comment-55565-info" class="comment-info">
<span class="comment-age">(11 Apr '17, 15:52)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-55561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55561-form-container" class="comment-form-container">
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

<span id="55627"></span>

<div id="answer-container-55627" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55627-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You must removed the natural=water from the way that forms the outline of the polygon.</p>
<p>The natural=water-tag should only be on the relation.</p>
<p>The tagging scheme with tags on the outer way AND the relation is called "old style" and this is now deprecated. They stopped rendering these polygons recently. <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon#Legacy_Data">wiki.openstreetmap.org/wiki/Relation:multipolygon#Legacy_Data</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '17, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikLindseth has 2 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '17, 13:53</strong> </span></p>
</div>
</div>
<div id="comments-container-55627" class="comments-container">
&#10;</div>
<div id="comment-tools-55627" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55627-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55563"></span>

<div id="answer-container-55563" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55563-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello, this problem will show up if you are not properly tagging the features. For example, if you want to draw a courtyard inside a building, you need to draw two buildings, one inside the other. When you create the multipolygon from going to Preset --&gt; Relations --&gt; Multipolygon, it will provide you with option to name your multipolygon and choose roles for each of the buildings. The individual features cannot have buildings tags anymore if they are in a multipolygon. What you have to do is, create two blocks with no tags, create the multipolygon and then edit the multipolygon itself and tag them properly. There is another way where you can create the features and then create the multipolygon. Do this: Select the features, then press Ctrl + B, that will create the multipolygon with the necessary tags and roles. If you find any roles not proper, then you can edit the role from Tags tab. Following link will help you a lot on this: <a href="http://wiki.openstreetmap.org/wiki/Relation:multipolygon">http://wiki.openstreetmap.org/wiki/Relation:multipolygon</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '17, 15:25</strong></p>
<img src="https://secure.gravatar.com/avatar/c482180b767d07897d150d7b426ca4e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmahmud&#39;s gravatar image" />
<p><span>mmahmud</span><br />
<span class="score" title="638 reputation points">638</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmahmud has one accepted answer">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '17, 15:34</strong> </span></p>
</div>
</div>
<div id="comments-container-55563" class="comments-container">
&#10;</div>
<div id="comment-tools-55563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55563-form-container" class="comment-form-container">
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

