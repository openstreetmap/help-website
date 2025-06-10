+++
type = "question"
title = "Slow Apache while tirex-master running"
description = '''I currently have only Europe in the database plus contours. Rendering is fairly quick, even on the levels with contours. But when a tirex-master is running, apache becomes very slow. Not just mod_tile serving cached tiles, but also the web fronted of munin (e.g.). System: Hardware: IBM Blade x3650, ...'''
date = "2015-09-16T17:20:00Z"
lastmod = "2015-09-16T17:53:00Z"
weight = 45292
keywords = [ "apache", "tirex", "mapnik", "mod_tile" ]
aliases = [ "/questions/45292" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Slow Apache while tirex-master running](/questions/45292/slow-apache-while-tirex-master-running)

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
<span id="post-45292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45292-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I currently have only Europe in the database plus contours. Rendering is fairly quick, even on the levels with contours. But when a tirex-master is running, apache becomes very slow. Not just mod_tile serving cached tiles, but also the web fronted of munin (e.g.).</p>
<p>System: Hardware: IBM Blade x3650, 16 Cores Octa 2.4, 54GB Ram, 500GB SSDs, 5TB Raid HDs. Software: Debian Jessie, postgres 9.4, Mapnik 3.0.4, apache 2.4, latest postgis, mod_tile, tirex, etc.</p>
<p>Any pointers would be appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-tirex" rel="tag" title="see questions tagged &#39;tirex&#39;">tirex</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '15, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/19a86a52d87d89c5585abfc7c62159cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmyk&#39;s gravatar image" />
<p><span>cmyk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmyk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45292" class="comments-container">
<span id="45294"></span>
<div id="comment-45294" class="comment">
<div id="post-45294-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you at least narrow it down to whether it is CPU or I/O related? <code>top</code> should provide this information.</p>
</div>
<div id="comment-45294-info" class="comment-info">
<span class="comment-age">(16 Sep '15, 17:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45295"></span>
<div id="comment-45295" class="comment">
<div id="post-45295-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>CPU is not it. It's at 500% with 10 Cores. And I/O (iotop) doesn't look like it's bottlenecked.</p>
<p>top - 18:54:50 up 5 days, 10:04, 4 users, load average: 6.44, 6.24, 4.83 Tasks: 84 total, 7 running, 77 sleeping, 0 stopped, 0 zombie %Cpu(s): 50.1 us, 12.8 sy, 0.0 ni, 37.0 id, 0.0 wa, 0.0 hi, 0.0 si, 0.0 st KiB Mem: 56623104 total, 55610008 used, 1013096 free, 0 buffers KiB Swap: 1228800 total, 522032 used, 706768 free. 26371032 cached Mem</p>
</div>
<div id="comment-45295-info" class="comment-info">
<span class="comment-age">(16 Sep '15, 17:53)</span> <span class="comment-user userinfo">cmyk</span>
</div>
</div>
</div>
<div id="comment-tools-45292" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45292-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

