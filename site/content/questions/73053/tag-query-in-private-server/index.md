+++
type = "question"
title = "Tag query in private server"
description = '''I did setup a private OSM Website following https://github.com/openstreetmap/openstreetmap-website and also the editor iD. I will let people edit the data through the editor iD, so they will use the tags that are predefined in the editor. How could I know how many features of a specific tag (for exa...'''
date = "2020-02-13T21:40:00Z"
lastmod = "2020-02-21T19:21:00Z"
weight = 73053
keywords = [ "openstreetmap", "tags", "railsport" ]
aliases = [ "/questions/73053" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tag query in private server](/questions/73053/tag-query-in-private-server)

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
<span id="post-73053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73053-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I did setup a private OSM Website following <a href="https://github.com/openstreetmap/openstreetmap-website">https://github.com/openstreetmap/openstreetmap-website</a> and also the editor iD. I will let people edit the data through the editor iD, so they will use the tags that are predefined in the editor. How could I know how many features of a specific tag (for example highway) there are in the server? Can I do it through rails console or need another software? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '20, 21:40</strong></p>
<img src="https://secure.gravatar.com/avatar/5f1f061e7e81f0e885227d27d95752f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlosguedes&#39;s gravatar image" />
<p><span>carlosguedes</span><br />
<span class="score" title="91 reputation points">91</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlosguedes has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73053" class="comments-container">
&#10;</div>
<div id="comment-tools-73053" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73053-form-container" class="comment-form-container">
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

<span id="73055"></span>

<div id="answer-container-73055" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73055-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="carlosguedes has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can probably query the database through the console, but I wouldn't know how.</p>
<p>The usual tool for these stats is <a href="https://wiki.openstreetmap.org/wiki/Taginfo">taginfo</a>, so you could set up your own instance.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '20, 23:19</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73055" class="comments-container">
<span id="73188"></span>
<div id="comment-73188" class="comment">
<div id="post-73188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you, I just realized that the rails console is not the best way of doing it, but through the psql console. I will reformulate my question.</p>
</div>
<div id="comment-73188-info" class="comment-info">
<span class="comment-age">(21 Feb '20, 19:21)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
</div>
<div id="comment-tools-73055" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73055-form-container" class="comment-form-container">
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

