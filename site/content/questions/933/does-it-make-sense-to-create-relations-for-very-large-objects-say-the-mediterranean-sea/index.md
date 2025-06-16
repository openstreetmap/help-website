+++
type = "question"
title = "Does it make sense to create relations for very large objects - say: the Mediterranean Sea?"
description = '''Does it make sense to create relations for very large objects? Let&#x27;s say the Mediterranean Sea...!?'''
date = "2010-09-27T11:38:00Z"
lastmod = "2010-09-29T11:22:00Z"
weight = 933
keywords = [ "very", "large", "objects", "relation", "overhead" ]
aliases = [ "/questions/933" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Does it make sense to create relations for very large objects - say: the Mediterranean Sea?](/questions/933/does-it-make-sense-to-create-relations-for-very-large-objects-say-the-mediterranean-sea)

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
<span id="post-933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-933-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Does it make sense to create relations for very large objects? Let's say the Mediterranean Sea...!?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-very" rel="tag" title="see questions tagged &#39;very&#39;">very</span> <span class="post-tag tag-link-large" rel="tag" title="see questions tagged &#39;large&#39;">large</span> <span class="post-tag tag-link-objects" rel="tag" title="see questions tagged &#39;objects&#39;">objects</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-overhead" rel="tag" title="see questions tagged &#39;overhead&#39;">overhead</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Sep '10, 11:38</strong></p>
<img src="https://secure.gravatar.com/avatar/bc6d0b055d631830f7891d3f89edb66b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="katpatuka&#39;s gravatar image" />
<p><span>katpatuka</span><br />
<span class="score" title="1041 reputation points"><span>1.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="katpatuka has 2 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Sep '10, 14:13</strong> </span></p>
</div>
</div>
<div id="comments-container-933" class="comments-container">
&#10;</div>
<div id="comment-tools-933" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-933-form-container" class="comment-form-container">
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

<span id="961"></span>

<div id="answer-container-961" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-961-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>They are already very large relations in OSM. For instance, countries boundaries (Germany, France but also probably Australia, USA, China, etc) or inter-states routes (highways/freeways). So, the question is not if it make sense but if you need them. You just have to know that very large objects imply very large relations which are not easy to create and maintain. For this reason, some relations are collecting sub-relations (for instance, the french boundary is composed of sub-relations containing the boundaries of each adjacent country). The OSM API is allowing this but then, the applications consuming OSM data (like renderers, routing apps, statistic tools, etc) have to correctly handle such special relations (having other relations as members) which is not the case today.<br />
They are also very large objects where the outlines are not well defined (valleys, massif). You can find some proposals on the wiki about such things like <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Valley"></a><a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Valley"></a><a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Valley">https://wiki.openstreetmap.org/wiki/Proposed_features/Valley</a>, <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Massif"></a><a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Massif"></a><a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Massif">https://wiki.openstreetmap.org/wiki/Proposed_features/Massif</a> or <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Sea"></a><a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Sea"></a><a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Sea">https://wiki.openstreetmap.org/wiki/Proposed_features/Sea</a> using nodes (so it's more placing a label) or even this relation proposal : <a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Region"></a><a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Region"></a><a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Region">https://wiki.openstreetmap.org/wiki/Relations/Proposed/Region</a> but I don't know it's widely used today.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Sep '10, 11:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></p>
</div>
</div>
<div id="comments-container-961" class="comments-container">
&#10;</div>
<div id="comment-tools-961" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-961-form-container" class="comment-form-container">
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

