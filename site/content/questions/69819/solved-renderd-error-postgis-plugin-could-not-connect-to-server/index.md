+++
type = "question"
title = "[solved] renderd error: postgis plugin: could not connect to server"
description = '''My tileserver worked perfectly fine but my disk space went full. So I gave my VM more capacity, rebooted it and after I did everything I usually do I got that renderd error: An error occurred while loading the map layer &#x27;default&#x27;: Postgis Plugin: could not connect to server: No such file or director...'''
date = "2019-07-01T09:12:00Z"
lastmod = "2019-12-10T11:22:00Z"
weight = 69819
keywords = [ "renderd", "postgresql", "postgis" ]
aliases = [ "/questions/69819" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[solved\] renderd error: postgis plugin: could not connect to server](/questions/69819/solved-renderd-error-postgis-plugin-could-not-connect-to-server)

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
<span id="post-69819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69819-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My tileserver worked perfectly fine but my disk space went full. So I gave my VM more capacity, rebooted it and after I did everything I usually do I got that renderd error:</p>
<p><code>An error occurred while loading the map layer 'default': Postgis Plugin: could not connect to server: No such file or directory Is the server running locally and accepting connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"? Connection string: ' dbname=gis connect_timeout=4' encountered during parsing of layer 'landcover-low-zoom' in Layer at line 755 of '/home/betrieb /src/openstreetmap-carto/mapnik.xml'</code></p>
<p>How can I fix this that my tileserver runs fine again?<br />
Thanks in advance :)</p>
<p>(correct my tags if they are wrong)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jul '19, 09:12</strong></p>
<img src="https://secure.gravatar.com/avatar/cac02e7bc318c8ceefa4f9eb1cd7b379?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="N3x&#39;s gravatar image" />
<p><span>N3x</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="N3x has one accepted answer">33%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '19, 10:22</strong> </span></p>
</div>
</div>
<div id="comments-container-69819" class="comments-container">
<span id="69820"></span>
<div id="comment-69820" class="comment">
<div id="post-69820-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A bit more info would help:</p>
<blockquote>
<p>So I gave my VM more capacity,</p>
</blockquote>
<p>What exactly did you do?</p>
<blockquote>
<p>rebooted it</p>
</blockquote>
<p>Have you rebooted it successfully before?</p>
<blockquote>
<p>and after I did everything I usually do I got that renderd error ...</p>
</blockquote>
<p>Also, while people here may be able to help, it doesn't look like your problem is really an OSM specific one, so one of <a href="https://stackoverflow.com/questions">https://stackoverflow.com/questions</a> 's family of sites might get more responses.</p>
</div>
<div id="comment-69820-info" class="comment-info">
<span class="comment-age">(01 Jul '19, 09:49)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69821"></span>
<div id="comment-69821" class="comment">
<div id="post-69821-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Capacity: shutdown -&gt; 140G to 160G -&gt; start -&gt; expand /dev/sda1<br />
Yes, reboot worked fine before.<br />
Asked it there. Still waiting</p>
</div>
<div id="comment-69821-info" class="comment-info">
<span class="comment-age">(01 Jul '19, 09:51)</span> <span class="comment-user userinfo">N3x</span>
</div>
</div>
</div>
<div id="comment-tools-69819" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69819-form-container" class="comment-form-container">
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

<span id="69823"></span>

<div id="answer-container-69823" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69823-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Fixed. Answer: Running <code>sudo dpkg-reconfigure postgresql</code> and <code>sudo systemctl restart renderd</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '19, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/cac02e7bc318c8ceefa4f9eb1cd7b379?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="N3x&#39;s gravatar image" />
<p><span>N3x</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="N3x has one accepted answer">33%</span> </br></br></p>
</div>
</div>
<div id="comments-container-69823" class="comments-container">
&#10;</div>
<div id="comment-tools-69823" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69823-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72062"></span>

<div id="answer-container-72062" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72062-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>Start your postgresql server</strong> - sudo /etc/init.d/postgresql start</p>
<p><strong>Enable starting the server at startup</strong> - sudo systemctl enable postgresql</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '19, 11:22</strong></p>
<img src="https://secure.gravatar.com/avatar/33bf3b4900509a17d8860c4b8406a952?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Luisa&#39;s gravatar image" />
<p><span>Luisa</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Luisa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72062" class="comments-container">
&#10;</div>
<div id="comment-tools-72062" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72062-form-container" class="comment-form-container">
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

