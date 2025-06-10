+++
type = "question"
title = "graphhopper routing service does not return a result"
description = '''In my local openstreetmap which built under the instruction of install.md on the github. When i make a routing request using the graphhopper routing engine, it does not return me a result, even an error message, it shows a search.gif keep loading on the sidebar_content. But the OSRM engine can retur...'''
date = "2016-11-03T15:04:00Z"
lastmod = "2016-11-17T22:54:00Z"
weight = 52810
keywords = [ "graghhopper", "port", "rails" ]
aliases = [ "/questions/52810" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [graphhopper routing service does not return a result](/questions/52810/graphhopper-routing-service-does-not-return-a-result)

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
<span id="post-52810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52810-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my local openstreetmap which built under the instruction of <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md">install.md</a> on the github. When i make a routing request using the graphhopper routing engine, it does not return me a result, even an error message, it shows a search.gif keep loading on the sidebar_content.</p>
<p>But the OSRM engine can return a instruction message. I did not change any code related with direction .js file on the rails port. Do i lost some setting or otherthing important?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-graghhopper" rel="tag" title="see questions tagged &#39;graghhopper&#39;">graghhopper</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-rails" rel="tag" title="see questions tagged &#39;rails&#39;">rails</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Nov '16, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-52810" class="comments-container">
<span id="52811"></span>
<div id="comment-52811" class="comment">
<div id="post-52811-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>are those services free to use ? Or is there some IP-address or developer key restriction ?</p>
</div>
<div id="comment-52811-info" class="comment-info">
<span class="comment-age">(03 Nov '16, 16:33)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-52810" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52810-form-container" class="comment-form-container">
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

<span id="52870"></span>

<div id="answer-container-52870" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52870-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It should be the josnp disabled in my enviroment. I set up local graphhopper routing service under this <a href="https://github.com/graphhopper/graphhopper/blob/master/docs/core/quickstart-from-source.md">instruction</a>, and add <strong>web.jsonp_allowed=true</strong> in the config.properties. Then change the graphhopper routing api address to //localhost:8989/route in config/application.yml.The graphhopper routing service can return me the right result finally.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '16, 08:25</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-52870" class="comments-container">
<span id="53024"></span>
<div id="comment-53024" class="comment">
<div id="post-53024-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've accepted this as an answer for you - hope you don't mind! (OSQA doesn't let you accept your own answers).</p>
</div>
<div id="comment-53024-info" class="comment-info">
<span class="comment-age">(17 Nov '16, 22:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52870" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52870-form-container" class="comment-form-container">
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

