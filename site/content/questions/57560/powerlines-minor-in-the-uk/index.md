+++
type = "question"
title = "Powerlines (minor) in the UK"
description = '''Hi, I am a very new user, and was wondering how we could see power lines (under 132kV) over the UK. Is there a filter somewhere? Many thanks!'''
date = "2017-08-11T12:21:00Z"
lastmod = "2017-08-12T07:12:00Z"
weight = 57560
keywords = [ "power_lines" ]
aliases = [ "/questions/57560" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Powerlines (minor) in the UK](/questions/57560/powerlines-minor-in-the-uk)

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
<span id="post-57560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57560-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am a very new user, and was wondering how we could see power lines (under 132kV) over the UK. Is there a filter somewhere?</p>
<p>Many thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-power_lines" rel="tag" title="see questions tagged &#39;power_lines&#39;">power_lines</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Aug '17, 12:21</strong></p>
<img src="https://secure.gravatar.com/avatar/82e68350ac0a4b100c70b01d2199e8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashley94032&#39;s gravatar image" />
<p><span>Ashley94032</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashley94032 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57560" class="comments-container">
&#10;</div>
<div id="comment-tools-57560" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57560-form-container" class="comment-form-container">
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

<span id="57568"></span>

<div id="answer-container-57568" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57568-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try with overpass-turbo (example <a href="http://overpass-turbo.eu/s/qWN">here</a>).</p>
<p>Power lines may not have their voltage mapped, so you may need a mix of terms:</p>
<ul>
<li>power=minor_line : should be 11k or possibly 33k, but may include lower volatages.</li>
<li>power=line with voltage= (valid values under 132 Kv)</li>
<li>power=line with only one wire per cable.</li>
</ul>
<p>See the wiki for the likely values for these tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '17, 19:52</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-57568" class="comments-container">
<span id="58088"></span>
<div id="comment-58088" class="comment">
<div id="post-58088-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There is also the <a href="http://www.flosm.de/en/powergrid.html?lat=51.4913345&amp;lon=0.0671534157&amp;r=40718.748&amp;st=0&amp;sw=powerline380k,powerline400k,powerline420k,powerline750k,powerline765k,powerlinedchigh">Power Grid Map</a> from flosm.de but minor power lines are also shown on <a href="http://osm.org/go/0EpMcxjBF?m=">osm.org</a></p>
</div>
<div id="comment-58088-info" class="comment-info">
<span class="comment-age">(12 Aug '17, 07:12)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-57568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57568-form-container" class="comment-form-container">
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

