+++
type = "question"
title = "OSM renderd crashing because of memory usage"
description = '''Hello, So we have a setup where we&#x27;re running a bunch of servers from which we generate a map that gets displayed on our website. The setup uses a &#x27;master&#x27; server which runs mapnick, renderd, an apache 2 server and a postgres database, plus at least 2 slave servers that only run the mapnick,renderd ...'''
date = "2016-06-10T14:03:00Z"
lastmod = "2019-09-16T08:54:00Z"
weight = 50123
keywords = [ "renderd", "crash", "memory" ]
aliases = [ "/questions/50123" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [OSM renderd crashing because of memory usage](/questions/50123/osm-renderd-crashing-because-of-memory-usage)

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
<span id="post-50123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50123-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>So we have a setup where we're running a bunch of servers from which we generate a map that gets displayed on our website.</p>
<p>The setup uses a 'master' server which runs mapnick, renderd, an apache 2 server and a postgres database, plus at least 2 slave servers that only run the mapnick,renderd and apache2 server and we have them using the postgres database found on the master server. All servers running ubuntu, the slaves have a 4 cpu cores and 8 gb of ram.</p>
<p>Lately we've been seeing the slave servers using up all the memory, the unix kernel kills the renderd process (which is the one using the most memory). And then we have a monit process that restarts it, so the servers keep going. Tried to change the number of threads used in rederd.conf down to only 1 thread, but that just made the memory usage go down slower.</p>
<p>This is the graph we see on our servers: <a href="https://dl.dropboxusercontent.com/content_link/6GHw57e25indiTnh5O3WuSM6ITMKGdbLq8iW0mvjeT4UxbQraMolPkTRbJc8meXT/file">https://dl.dropboxusercontent.com/content_link/6GHw57e25indiTnh5O3WuSM6ITMKGdbLq8iW0mvjeT4UxbQraMolPkTRbJc8meXT/file</a></p>
<p>The one on the left is using 1 thread, and the one on the right 2 threads.</p>
<p>Any ideas what might be causing this? From the graphs we see that the memory usage suddenly spikes, can this be caused by some cached tiles expiring or something similar to that?</p>
<p>Kind regards,</p>
<p>Tiberiu Ionescu</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jun '16, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/f01b4a26405366c3dc7ddebf9ce1bee9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tiberiu22&#39;s gravatar image" />
<p><span>Tiberiu22</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tiberiu22 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jun '16, 08:27</strong> </span></p>
</div>
</div>
<div id="comments-container-50123" class="comments-container">
<span id="50132"></span>
<div id="comment-50132" class="comment">
<div id="post-50132-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>meta: could you please link to an image instead of a html page with dozens of necessary (third-party) scripts? Best would be to upload here. If you do not have enough rights for this yet, just give us the permission to re-upload here, then someone can replace the externally hosted image.</p>
</div>
<div id="comment-50132-info" class="comment-info">
<span class="comment-age">(10 Jun '16, 19:45)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50123-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="65707"></span>

<div id="answer-container-65707" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65707-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>Did you find any solution since then ? I am having the same issue:</p>
<ul>
<li>renderd works fine and renders about a dozen of tiles</li>
<li>suddenly the unix kernel kills the renderd process because of excessive memory usage</li>
</ul>
<p>I tried using a very small database and reduced the number of threads to 1 in renderd.conf but the problem is still there.</p>
<p>Any idea where this might come from ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '18, 13:20</strong></p>
<img src="https://secure.gravatar.com/avatar/85d01114a7fa06ea0e51ec708f0d88a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sammy&#39;s gravatar image" />
<p><span>sammy</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sammy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65707" class="comments-container">
&#10;</div>
<div id="comment-tools-65707" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65707-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50130"></span>

<div id="answer-container-50130" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50130-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would have suggested reducing "<code>num_threads</code>" in your "<code>renderd.conf</code>". However you've already done that...</p>
<p>I'd have a look at what's using the memory when it runs out. If 1 renderd process is using 8Gb, then I wonder if there's a leak somewhere - maybe check versions of things to see if something needs updating?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '16, 17:26</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jun '16, 17:29</strong> </span></p>
</div>
</div>
<div id="comments-container-50130" class="comments-container">
<span id="50173"></span>
<div id="comment-50173" class="comment">
<div id="post-50173-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey! Thanks for the suggestions. Any suggestions on how I can do this? Can I see the operations that renderd is doing and how much memory they're using?</p>
</div>
<div id="comment-50173-info" class="comment-info">
<span class="comment-age">(13 Jun '16, 10:24)</span> <span class="comment-user userinfo">Tiberiu22</span>
</div>
</div>
</div>
<div id="comment-tools-50130" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50130-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70799"></span>

<div id="answer-container-70799" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70799-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I reported similar problem here: <a href="https://github.com/openstreetmap/mod_tile/issues/181">https://github.com/openstreetmap/mod_tile/issues/181</a> and here <a href="https://help.openstreetmap.org/questions/70490/renderd-out-of-memory.">https://help.openstreetmap.org/questions/70490/renderd-out-of-memory.</a> Unfortunately without any feedback...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '19, 08:54</strong></p>
<img src="https://secure.gravatar.com/avatar/7299031d06e3c25e516216b6bbac6271?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stevo_001&#39;s gravatar image" />
<p><span>stevo_001</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stevo_001 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70799" class="comments-container">
&#10;</div>
<div id="comment-tools-70799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70799-form-container" class="comment-form-container">
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

