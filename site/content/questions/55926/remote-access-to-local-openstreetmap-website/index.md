+++
type = "question"
title = "Remote access to local openstreetmap-website"
description = '''Im trying to setup local version of openstreetmap-website on my VPS with ubuntu 16.04 installed. I did like it says in https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md . Seems like everything passed good, no errors in db migrate and test (1087 runs, 327227 assertions, 0 ...'''
date = "2017-04-28T08:45:00Z"
lastmod = "2017-12-21T01:03:00Z"
weight = 55926
keywords = [ "railsport", "api", "installation", "server" ]
aliases = [ "/questions/55926" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Remote access to local openstreetmap-website](/questions/55926/remote-access-to-local-openstreetmap-website)

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
<span id="post-55926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55926-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Im trying to setup local version of openstreetmap-website on my VPS with ubuntu 16.04 installed. I did like it says in <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md">https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md</a> . Seems like everything passed good, no errors in db migrate and test (1087 runs, 327227 assertions, 0 failures, 0 errors, 0 skips). I start server by running command "bundle exec rails server", here is the output:<br />
=&gt; Booting WEBrick<br />
=&gt; Rails 4.2.8 application starting in development on <a href="http://localhost:3000">http://localhost:3000</a><br />
=&gt; Run <code>rails server -h</code> for more startup options<br />
=&gt; Ctrl-C to shutdown server<br />
svgo worker: <code>svgo</code> not found; please provide proper binary or disable this worker (--no-svgo argument or <code>:svgo =&gt; false</code> through options)<br />
[2017-04-28 09:30:21] INFO WEBrick 1.3.1<br />
[2017-04-28 09:30:21] INFO ruby 2.3.1 (2016-04-26) [x86_64-linux-gnu]<br />
[2017-04-28 09:30:21] INFO WEBrick::HTTPServer#start: pid=11827 port=3000</p>
<p>So it seems like server starts, and running. But i cannot access it throught browser, either by ip or domain, with port 3000, no connection. So how can i solve this problem, do i need to change any config, or how else i can start this API, to be accessible through internet?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Apr '17, 08:45</strong></p>
<img src="https://secure.gravatar.com/avatar/f67d8f5990adcdd4361304875f36c672?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dezurat&#39;s gravatar image" />
<p><span>Dezurat</span><br />
<span class="score" title="30 reputation points">30</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dezurat has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Apr '17, 00:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></br></p>
</div>
</div>
<div id="comments-container-55926" class="comments-container">
&#10;</div>
<div id="comment-tools-55926" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55926-form-container" class="comment-form-container">
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

<span id="55927"></span>

<div id="answer-container-55927" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55927-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dezurat has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As the instructions say running: "bundle exec rails server" starts the server listening on localhost (port 3000).</p>
<p>Run "bundle exec rails server -help" to get all options, as you will see you need the "-b" to specify a different address to listen on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '17, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Apr '17, 09:56</strong> </span></p>
</div>
</div>
<div id="comments-container-55927" class="comments-container">
&#10;</div>
<div id="comment-tools-55927" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55927-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61308"></span>

<div id="answer-container-61308" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61308-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To Start the Server use</p>
<pre><code>rails server --binding=YOUR_IP_ADDRESS</code></pre>
<p>not</p>
<pre><code>bundle exec rails server</code></pre>
<p>I found this soulution somewhere in the www and it works</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Dec '17, 01:03</strong></p>
<img src="https://secure.gravatar.com/avatar/8ccc4352aaf4f031b5ade9a9b7410964?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MagSungam&#39;s gravatar image" />
<p><span>MagSungam</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MagSungam has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Dec '17, 10:39</strong> </span></p>
</div>
</div>
<div id="comments-container-61308" class="comments-container">
&#10;</div>
<div id="comment-tools-61308" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61308-form-container" class="comment-form-container">
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

