+++
type = "question"
title = "Merge two different planet osm files"
description = '''Hi, I am trying to merge two planet files which are North America OSM file and South America OSM file. I just need information whether two different planet files can be merged or not. As i came to know that different countries can be merged within same planet file. However, i need the other way arou...'''
date = "2018-10-30T13:16:00Z"
lastmod = "2018-11-13T14:36:00Z"
weight = 66555
keywords = [ "planet", "merging" ]
aliases = [ "/questions/66555" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Merge two different planet osm files](/questions/66555/merge-two-different-planet-osm-files)

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
<span id="post-66555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66555-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am trying to merge two planet files which are North America OSM file and South America OSM file. I just need information whether two different planet files can be merged or not. As i came to know that different countries can be merged within same planet file. However, i need the other way around.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-merging" rel="tag" title="see questions tagged &#39;merging&#39;">merging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '18, 13:16</strong></p>
<img src="https://secure.gravatar.com/avatar/4da2b35cc0754a85fdba1555cbe95a20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sumanosmxemplar&#39;s gravatar image" />
<p><span>sumanosmxemplar</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sumanosmxemplar has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Oct '18, 18:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-66555" class="comments-container">
&#10;</div>
<div id="comment-tools-66555" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66555-form-container" class="comment-form-container">
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

<span id="66556"></span>

<div id="answer-container-66556" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66556-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, you can merge them with something like "osmosis". <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh#L186">Here</a> is an example script that, among other things, merges some OSM .pbf files together before loading a database with them.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '18, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-66556" class="comments-container">
<span id="66557"></span>
<div id="comment-66557" class="comment">
<div id="post-66557-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When i see your script, the two locations what you have merged are both from Europe. My case is different. I want North America and South America Planet files merge.</p>
<p>Is that possible?</p>
</div>
<div id="comment-66557-info" class="comment-info">
<span class="comment-age">(30 Oct '18, 13:40)</span> <span class="comment-user userinfo">sumanosmxemplar</span>
</div>
</div>
<span id="66558"></span>
<div id="comment-66558" class="comment">
<div id="post-66558-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes. Why not try it?</p>
</div>
<div id="comment-66558-info" class="comment-info">
<span class="comment-age">(30 Oct '18, 13:52)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="66764"></span>
<div id="comment-66764" class="comment">
<div id="post-66764-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also, can i merge two bz2 files with osmosis?</p>
</div>
<div id="comment-66764-info" class="comment-info">
<span class="comment-age">(13 Nov '18, 14:36)</span> <span class="comment-user userinfo">sumanosmxemplar</span>
</div>
</div>
</div>
<div id="comment-tools-66556" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66556-form-container" class="comment-form-container">
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

