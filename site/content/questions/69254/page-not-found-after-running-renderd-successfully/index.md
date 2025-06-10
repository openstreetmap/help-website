+++
type = "question"
title = "Page not found after running renderd successfully"
description = '''I&#x27;ve been trying to set up a tileserver for a few weeks now using this instruction. Yes, I&#x27;m using 18.04 if that will be a question. Had some other issues but now everything seems fine. Or doesn&#x27;t it? I managed to run renderd without errors. But now when I open my browser and try to get on the page ...'''
date = "2019-05-21T07:26:00Z"
lastmod = "2019-05-23T15:36:00Z"
weight = 69254
keywords = [ "apache", "renderd", "mapnik", "tileserver" ]
aliases = [ "/questions/69254" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Page not found after running renderd successfully](/questions/69254/page-not-found-after-running-renderd-successfully)

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
<span id="post-69254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69254-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been trying to set up a tileserver for a few weeks now using <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">this instruction</a>. Yes, I'm using 18.04 if that will be a question. Had some other issues but now everything seems fine. Or doesn't it?<br />
I managed to run renderd without errors. But now when I open my browser and try to get on the page where I should see my tiles it says "404 Not Found".<br />
Here you can see my <a href="https://pastebin.com/tbqDF0K0">Logs which belong to renderd</a>.<br />
Command I ran: <code>renderd -f -c /usr/local/etc/renderd.conf</code></p>
<p>That's that my debug says:<br />
<code>renderd[2107]: DEBUG: Got incoming connection, fd 23, number 9 renderd[2107]: DEBUG: Got incoming request with protocol version 2 renderd[2107]: DEBUG: Got command RenderPrio fd(23) xml(default), z(0), x(0), y(0), mime(image/png), options() renderd[2107]: Dispatching request to slave thread on fd 7 renderd[2107]: DEBUG: Sending render cmd(1 default 0/0/0) with protocol version 3 to fd 7 renderd[2107]: DEBUG: Got incoming request with protocol version 3 renderd[2107]: DEBUG: Got command Render fd(8) xml(default), z(0), x(0), y(0), mime(image/png), options() renderd[2107]: DEBUG: Failed to read cmd on fd 23 renderd[2107]: DEBUG: Connection 8, fd 23 closed, now 8 left</code></p>
<p>Has anyone got an idea what could be the reason why it won't work?<br />
Also, <a href="https://help.openstreetmap.org/questions/35317/local-tile-server-from-packages-404-when-displaying-tiles">this answer</a> didn't help me :/</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 May '19, 07:26</strong></p>
<img src="https://secure.gravatar.com/avatar/cac02e7bc318c8ceefa4f9eb1cd7b379?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="N3x&#39;s gravatar image" />
<p><span>N3x</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="N3x has one accepted answer">33%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '19, 07:29</strong> </span></p>
</div>
</div>
<div id="comments-container-69254" class="comments-container">
<span id="69281"></span>
<div id="comment-69281" class="comment">
<div id="post-69281-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There's not enough information in that logfile to comment. Ignore "DEBUG: Failed to read cmd on fd 23" - that is not in itself an error.</p>
</div>
<div id="comment-69281-info" class="comment-info">
<span class="comment-age">(23 May '19, 13:37)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69254-form-container" class="comment-form-container">
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

<span id="69283"></span>

<div id="answer-container-69283" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69283-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>Problem fixed - no answers needed anymore</strong></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '19, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/cac02e7bc318c8ceefa4f9eb1cd7b379?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="N3x&#39;s gravatar image" />
<p><span>N3x</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="N3x has one accepted answer">33%</span> </br></br></p>
</div>
</div>
<div id="comments-container-69283" class="comments-container">
<span id="69285"></span>
<div id="comment-69285" class="comment">
<div id="post-69285-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So what was it in the end?</p>
</div>
<div id="comment-69285-info" class="comment-info">
<span class="comment-age">(23 May '19, 15:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69287"></span>
<div id="comment-69287" class="comment">
<div id="post-69287-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To be honest I don't know. Accidently deleted my first VM, created a new one and then it worked haha</p>
</div>
<div id="comment-69287-info" class="comment-info">
<span class="comment-age">(23 May '19, 15:36)</span> <span class="comment-user userinfo">N3x</span>
</div>
</div>
</div>
<div id="comment-tools-69283" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69283-form-container" class="comment-form-container">
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

