+++
type = "question"
title = "Which Mapnik version do I have and why Mapnik doesn&#x27;t work with python"
description = '''Hi, I have two questions. My operating system is Ubuntu 12.04 and I followed the tutorial Building a tile server from packages from switch2osm.org. My first question: How can I found out which version of mapnik is installed or do you know which version is installed by this package (I installed it 2 ...'''
date = "2014-08-17T03:00:00Z"
lastmod = "2016-10-10T07:32:00Z"
weight = 35906
keywords = [ "python", "installation", "mapnik", "error" ]
aliases = [ "/questions/35906" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Which Mapnik version do I have and why Mapnik doesn't work with python](/questions/35906/which-mapnik-version-do-i-have-and-why-mapnik-doesnt-work-with-python)

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
<span id="post-35906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35906-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have two questions. My operating system is Ubuntu 12.04 and I followed the tutorial <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">Building a tile server from packages</a> from switch2osm.org.</p>
<p>My first question: How can I found out which version of mapnik is installed or do you know which version is installed by this package (I installed it 2 weeks ago)? in mapnik tutorial I found the command <code>mapnik-config -v</code> for checking the mapnik version, but that throws an error:</p>
<p><code>The program 'mapnik-config' is currently not installed. You can install it by typing: sudo apt-get install libmapnik2-dev</code></p>
<p>But mapnik is installed and works with mod_tile. On one webpage I readed that mapnik-config only exists if you have a mapnik version 2.x, but on my server I found a diretory /usr/lib/mapnik/2.0/</p>
<p>My second question: I would execute mapnik on command line to see debug informations to develop my own mapnik style. But But if I execute the following command in python <code>import mapnik</code>, it throws the following error:</p>
<p><code>Traceback (most recent call last): File "&lt;stdin&gt;", line 1, in &lt;module&gt; ImportError: No module named mapnik</code></p>
<p>I also tried it with <code>import mapnik2</code>, but same error. (mapnik is installed and works finde with mod_tile)</p>
<p>Anybody has an idea?</p>
<p>Thanks, Klaus</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '14, 03:00</strong></p>
<img src="https://secure.gravatar.com/avatar/3b8f786d0ebd6fc4bc80a77b28880bd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="klausschreiber&#39;s gravatar image" />
<p><span>klausschreiber</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="klausschreiber has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '14, 13:45</strong> </span></p>
</div>
</div>
<div id="comments-container-35906" class="comments-container">
&#10;</div>
<div id="comment-tools-35906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35906-form-container" class="comment-form-container">
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

<span id="35945"></span>

<div id="answer-container-35945" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35945-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try <code>import mapnik2</code>. Some versions of mapnik use this name instead.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '14, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-35945" class="comments-container">
<span id="35955"></span>
<div id="comment-35955" class="comment">
<div id="post-35955-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Thanks for your answer. I already tried this but the error was the same</p>
<p><code>Traceback (most recent call last): File "&lt;stdin&gt;", line 1, in &lt;module&gt; ImportError: No module named mapnik2</code></p>
</div>
<div id="comment-35955-info" class="comment-info">
<span class="comment-age">(18 Aug '14, 13:45)</span> <span class="comment-user userinfo">klausschreiber</span>
</div>
</div>
</div>
<div id="comment-tools-35945" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35945-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52434"></span>

<div id="answer-container-52434" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52434-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The issue was with version of Mapnik, Please look at</p>
<ol>
<li><a href="https://github.com/mapnik/mapnik/wiki/UbuntuInstallation">https://github.com/mapnik/mapnik/wiki/UbuntuInstallation</a></li>
</ol>
<p>for the required informations</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '16, 07:32</strong></p>
<img src="https://secure.gravatar.com/avatar/46fe2c2acfb7bcb45ce82c411406d2e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SUKHJIT%20SINGH%20SEHRA&#39;s gravatar image" />
<p><span>SUKHJIT SING...</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SUKHJIT SINGH SEHRA has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52434" class="comments-container">
&#10;</div>
<div id="comment-tools-52434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52434-form-container" class="comment-form-container">
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

