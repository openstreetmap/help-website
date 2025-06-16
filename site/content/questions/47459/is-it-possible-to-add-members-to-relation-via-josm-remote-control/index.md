+++
type = "question"
title = "Is it possible to add members to relation via JOSM remote control?"
description = '''I want to load a relation into JOSM via the remote control and add a node to it. I am able to load the relation, add the node, but I am not able to add node to the relation. Is there any possibility to do that?'''
date = "2016-01-12T01:00:00Z"
lastmod = "2017-11-19T13:51:00Z"
weight = 47459
keywords = [ "josm", "relations", "josm_remote_control" ]
aliases = [ "/questions/47459" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to add members to relation via JOSM remote control?](/questions/47459/is-it-possible-to-add-members-to-relation-via-josm-remote-control)

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
<span id="post-47459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47459-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to load a relation into JOSM via the remote control and add a node to it. I am able to load the relation, add the node, but I am not able to add node to the relation.</p>
<p>Is there any possibility to do that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-josm_remote_control" rel="tag" title="see questions tagged &#39;josm_remote_control&#39;">josm_remote_control</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jan '16, 01:00</strong></p>
<img src="https://secure.gravatar.com/avatar/e6dd88ec54643689069f97f0d52398ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gorn&#39;s gravatar image" />
<p><span>gorn</span><br />
<span class="score" title="542 reputation points">542</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gorn has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-47459" class="comments-container">
&#10;</div>
<div id="comment-tools-47459" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47459-form-container" class="comment-form-container">
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

<span id="47468"></span>

<div id="answer-container-47468" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47468-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm guessing a bit here, but you should be able to do this with the <a href="http://josm.openstreetmap.de/wiki/Help/Preferences/RemoteControl#load_data">load data</a> command. Build the new relation object in <a href="https://wiki.openstreetmap.org/wiki/JOSM_file_format">josm xml format</a>, url-encode it, and send it using remote control.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '16, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-47468" class="comments-container">
<span id="60696"></span>
<div id="comment-60696" class="comment">
<div id="post-60696-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, but there is no way to put the object INTO the relation.</p>
</div>
<div id="comment-60696-info" class="comment-info">
<span class="comment-age">(19 Nov '17, 12:29)</span> <span class="comment-user userinfo">gorn</span>
</div>
</div>
<span id="60698"></span>
<div id="comment-60698" class="comment">
<div id="post-60698-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If JOSM supports loading changes using the load data command, you should be able to (during preparation of the remote command) retrieve the current version of the relation and generate a JOSM format xml snippet that modifies the members of the relation.</p>
<p>To add the node to the relation you'd also have to include it in the snippet so that you could reference it in the new version of the relation. The id of the new object should just be a negative number, this tells JOSM to treat it as a new object in the layer.</p>
</div>
<div id="comment-60698-info" class="comment-info">
<span class="comment-age">(19 Nov '17, 13:51)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-47468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47468-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47831"></span>

<div id="answer-container-47831" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47831-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-47831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can load a relation via the <a href="https://josm.openstreetmap.de/wiki/Help/Preferences/RemoteControl#load_object">load_object</a> command.</p>
<p>In this page I also find <code>add_node</code> and <code>add_way</code>, but I can not find anything to add a member to a relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Feb '16, 21:44</strong></p>
<img src="https://secure.gravatar.com/avatar/2c370d6199fdd6ee986e81f5baa62d84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AnyFile&#39;s gravatar image" />
<p><span>AnyFile</span><br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AnyFile has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47831" class="comments-container">
<span id="60695"></span>
<div id="comment-60695" class="comment">
<div id="post-60695-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, this is why I ask the questino here in the first place. I could not find it either.</p>
</div>
<div id="comment-60695-info" class="comment-info">
<span class="comment-age">(19 Nov '17, 12:28)</span> <span class="comment-user userinfo">gorn</span>
</div>
</div>
</div>
<div id="comment-tools-47831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47831-form-container" class="comment-form-container">
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

