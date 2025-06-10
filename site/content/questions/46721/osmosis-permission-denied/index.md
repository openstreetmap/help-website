+++
type = "question"
title = "Osmosis permission denied"
description = '''Hello friends, good afternoon  I want to configure osmosis to get updates, but shows error: ./utils/update.php --import-osmosis-all --no-npi WARNING: resetting cache memory to 686 sh: 1: /home/ubuntu/osmosis: Permission denied Error: 126. Re-trying: /home/ubuntu/osmosis -q --read-replication-lag wor...'''
date = "2015-11-19T18:49:00Z"
lastmod = "2015-11-20T14:53:00Z"
weight = 46721
keywords = [ "osmosis" ]
aliases = [ "/questions/46721" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Osmosis permission denied](/questions/46721/osmosis-permission-denied)

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
<span id="post-46721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46721-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello friends, good afternoon</p>
<p>I want to configure osmosis to get updates, but shows error:</p>
<pre><code>./utils/update.php --import-osmosis-all --no-npi
WARNING: resetting cache memory to 686
sh: 1: /home/ubuntu/osmosis: Permission denied
Error: 126. Re-trying: /home/ubuntu/osmosis -q --read-replication-lag workingDirectory=/home/ubuntu/Nominatim/settings in 900 secs</code></pre>
<ol>
<li>I did download the latest osmosis, put in &lt;home&gt;/osmosis</li>
<li>Change CONST_Osmosis_Binary on settings.php and point to &lt;home&gt;/osmosis</li>
<li>Change replication params</li>
<li>Execute .<code>/utils/setup.php --osmosis-init</code></li>
<li>Execute <code>./utils/setup.php --create-functions --enable-diff-updates</code></li>
</ol>
<p>When I try to execute <code>./utils/update.php --import-osmosis-all --no-npi</code> then shows error.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '15, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/90d0aa1917d54b295653368c358c0359?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeancz&#39;s gravatar image" />
<p><span>jeancz</span><br />
<span class="score" title="47 reputation points">47</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeancz has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-46721" class="comments-container">
<span id="46722"></span>
<div id="comment-46722" class="comment">
<div id="post-46722-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Does it work after executing <code>chmod +x /home/ubuntu/osmosis</code>? I.e. is the execution mode bit set?</p>
</div>
<div id="comment-46722-info" class="comment-info">
<span class="comment-age">(19 Nov '15, 19:11)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="46723"></span>
<div id="comment-46723" class="comment">
<div id="post-46723-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I try change permission for all files, bus does not work. :(</p>
</div>
<div id="comment-46723-info" class="comment-info">
<span class="comment-age">(19 Nov '15, 19:24)</span> <span class="comment-user userinfo">jeancz</span>
</div>
</div>
</div>
<div id="comment-tools-46721" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46721-form-container" class="comment-form-container">
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

<span id="46724"></span>

<div id="answer-container-46724" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46724-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-46724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Frederik Ramm has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the binary that you need to configure is <code>/home/ubuntu/osmosis/bin/osmosis</code> - try it by entering this full path on the command line before, you should be greeted by an extensive help message. And if you've installed osmosis from zip and not from tar.gz, you will need the <code>chmod a+x /home/ubuntu/osmosis/bin/osmosis</code> too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '15, 20:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46724" class="comments-container">
<span id="46753"></span>
<div id="comment-46753" class="comment">
<div id="post-46753-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Works fine. Thats it. Thanks Frederik.</p>
</div>
<div id="comment-46753-info" class="comment-info">
<span class="comment-age">(20 Nov '15, 14:53)</span> <span class="comment-user userinfo">jeancz</span>
</div>
</div>
</div>
<div id="comment-tools-46724" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46724-form-container" class="comment-form-container">
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

