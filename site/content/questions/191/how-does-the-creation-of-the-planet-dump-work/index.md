+++
type = "question"
title = "How does the creation of the Planet dump work?"
description = '''There is a weekly database dump called Planet.osm. How is it created? The answer could include details like former anonymous edits, referential integrity, etc.'''
date = "2010-07-14T15:49:00Z"
lastmod = "2010-07-14T16:34:00Z"
weight = 191
keywords = [ "planet", "technical", "data", "dump" ]
aliases = [ "/questions/191" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How does the creation of the Planet dump work?](/questions/191/how-does-the-creation-of-the-planet-dump-work)

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
<span id="post-191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-191-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is a weekly database dump called Planet.osm. How is it created?</p>
<p>The answer could include details like former anonymous edits, referential integrity, etc.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-technical" rel="tag" title="see questions tagged &#39;technical&#39;">technical</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-dump" rel="tag" title="see questions tagged &#39;dump&#39;">dump</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jul '10, 15:49</strong></p>
<img src="https://secure.gravatar.com/avatar/5c9aa062fed08c7962c88bd21cc62f93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emka&#39;s gravatar image" />
<p><span>emka</span><br />
<span class="score" title="95 reputation points">95</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emka has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>14 Jul '10, 16:28</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span></p>
</div>
</div>
<div id="comments-container-191" class="comments-container">
&#10;</div>
<div id="comment-tools-191" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-191-form-container" class="comment-form-container">
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

<span id="196"></span>

<div id="answer-container-196" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-196-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="emka has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's created using a custom C program called planetdump. You can find the source here:</p>
<p><a href="http://trac.openstreetmap.org/browser/applications/utils/planet.osm/C"></a><a href="http://trac.openstreetmap.org/browser/applications/utils/planet.osm/C"></a><a href="http://trac.openstreetmap.org/browser/applications/utils/planet.osm/C">http://trac.openstreetmap.org/browser/applications/utils/planet.osm/C</a></p>
<p>It runs inside a transaction so should provide a snapshot and have the same level of referential integrity as the database.</p>
<p>There is no such thing as a "former anonymous edit" as far as I know. Any user whose edits are public will be identified in the dump and any user whose edits are not public will not be identified.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '10, 16:26</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-196" class="comments-container">
&#10;</div>
<div id="comment-tools-196" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-196-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="198"></span>

<div id="answer-container-198" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-198-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The planet dump is created by running the <a href="http://svn.openstreetmap.org/applications/utils/planet.osm/C/">planet dump program</a> against the OpenStreetMap database. The run is started at 1:11am UK local time, and the exact time is available in the timestamp attribute of the &lt;osm&gt; element at the beginning of the file. Planet files are compressed with <a href="http://compression.ca/pbzip2/">pbzip2</a>, which makes them unsuitable for some decompressors, notably the Java native bzip2 implementation.</p>
<p>Planet files may contain ways which reference nodes which have been deleted, or relations which reference members which have been deleted. In planet files generated since March 2010 this is due to errors in the database, not with the dump process, and these errors can be found and fixed. In planet files generated before March 2010 this is due to the dump process not being run in a sufficiently isolated transaction.</p>
<p>Planet files are in the standard <a href="http://wiki.openstreetmap.org/wiki/.osm">OSM XML format</a>, and only contain visible (not deleted) elements. Anonymous edits are present, but lacking the uid and user attributes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '10, 16:34</strong></p>
<img src="https://secure.gravatar.com/avatar/d53ec2d1ec832fdf10f72222db4fa710?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matt&#39;s gravatar image" />
<p><span>Matt</span><br />
<span class="score" title="1161 reputation points"><span>1.2k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matt has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-198" class="comments-container">
&#10;</div>
<div id="comment-tools-198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-198-form-container" class="comment-form-container">
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

