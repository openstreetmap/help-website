+++
type = "question"
title = "http:/localhost/0/0/0.png tiles not showing"
description = '''do I need to create a user from the _renderd group or do all the settings from the current user?'''
date = "2023-03-26T19:34:00Z"
lastmod = "2023-03-27T21:06:00Z"
weight = 86984
keywords = [ "apache", "page_not_found", "renderd" ]
aliases = [ "/questions/86984" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [http:/localhost/0/0/0.png tiles not showing](/questions/86984/httplocalhost000png-tiles-not-showing)

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
<span id="post-86984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86984-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>do I need to create a user from the _renderd group or do all the settings from the current user?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-page_not_found" rel="tag" title="see questions tagged &#39;page_not_found&#39;">page_not_found</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Mar '23, 19:34</strong></p>
<img src="https://secure.gravatar.com/avatar/e535815404b3510234cc354e76c5abd4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hidemyname5&#39;s gravatar image" />
<p><span>hidemyname5</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hidemyname5 has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-86984" class="comments-container">
<span id="86985"></span>
<div id="comment-86985" class="comment">
<div id="post-86985-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm guessing that you're following one of the "switch2osm" raster tile guides.</p>
<p>You'll probably need to provide a bit more information on what you have done so far.</p>
</div>
<div id="comment-86985-info" class="comment-info">
<span class="comment-age">(26 Mar '23, 20:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="86986"></span>
<div id="comment-86986" class="comment">
<div id="post-86986-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>this is true. <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/</a> tried to set up a server following these instructions. everything was without errors until the page <a href="http://yourserveripaddress/hot/0/0/0.png">http://yourserveripaddress/hot/0/0/0.png</a> was requested. the browser returns a 404 error. how can i diagnose the problem? there are no errors in the file /var/log/syslog</p>
</div>
<div id="comment-86986-info" class="comment-info">
<span class="comment-age">(26 Mar '23, 20:35)</span> <span class="comment-user userinfo">hidemyname5</span>
</div>
</div>
<span id="86987"></span>
<div id="comment-86987" class="comment">
<div id="post-86987-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A 404 error means that it is probably not a firewall issue, I think. There's an "access" logfile below /var/log/apache2 , I think, that should show an attempted access.</p>
<p>Try restarting apache2 and see what gets written to thelogs?</p>
</div>
<div id="comment-86987-info" class="comment-info">
<span class="comment-age">(26 Mar '23, 20:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-86984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86984-form-container" class="comment-form-container">
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

<span id="86989"></span>

<div id="answer-container-86989" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86989-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>i solved my problem. perhaps the reason was access to resources and inept use of the sudo instruction. exactly repeated all the commands and manuals <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/</a> and everything worked out.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '23, 21:06</strong></p>
<img src="https://secure.gravatar.com/avatar/e535815404b3510234cc354e76c5abd4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hidemyname5&#39;s gravatar image" />
<p><span>hidemyname5</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hidemyname5 has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-86989" class="comments-container">
&#10;</div>
<div id="comment-tools-86989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86989-form-container" class="comment-form-container">
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

