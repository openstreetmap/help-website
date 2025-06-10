+++
type = "question"
title = "Help/Suggestions required for School routing system"
description = '''I am trying to create a routing system for a school using a minimum number of vehicles. But the problem is that it not only involves time windows but also capacity constraints. Also starting no. of vehicles and location is unknown. So, I have to just work with customer locations and the time by whic...'''
date = "2021-07-07T11:24:00Z"
lastmod = "2021-09-06T10:17:00Z"
weight = 80848
keywords = [ "openstreetmap", "school", "routing" ]
aliases = [ "/questions/80848" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Help/Suggestions required for School routing system](/questions/80848/helpsuggestions-required-for-school-routing-system)

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
<span id="post-80848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80848-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to create a routing system for a school using a minimum number of vehicles. But the problem is that it not only involves time windows but also capacity constraints. Also starting no. of vehicles and location is unknown. So, I have to just work with customer locations and the time by which they should reach the school.</p>
<p>I wanted to know if someone has worked on something similar before or any open-source solution is available to resolve this issue that resembles mine like google OR-Tools etc.</p>
<p>Edit I am looking for an opensource python-based solution</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-school" rel="tag" title="see questions tagged &#39;school&#39;">school</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '21, 11:24</strong></p>
<img src="https://secure.gravatar.com/avatar/45c1cced3ea049e72e23496b4715be45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vsaadnet&#39;s gravatar image" />
<p><span>vsaadnet</span><br />
<span class="score" title="45 reputation points">45</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vsaadnet has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jul '21, 13:46</strong> </span></p>
</div>
</div>
<div id="comments-container-80848" class="comments-container">
&#10;</div>
<div id="comment-tools-80848" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80848-form-container" class="comment-form-container">
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

<span id="80849"></span>

<div id="answer-container-80849" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80849-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at jsprit, the optimisation component of Graphhopper.</p>
<p><a href="https://github.com/graphhopper/jsprit">https://github.com/graphhopper/jsprit</a></p>
<p><a href="https://jsprit.github.io">https://jsprit.github.io</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '21, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-80849" class="comments-container">
<span id="80864"></span>
<div id="comment-80864" class="comment">
<div id="post-80864-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>sorry, I couldn't mention earlier, that I am looking for something in python</p>
</div>
<div id="comment-80864-info" class="comment-info">
<span class="comment-age">(08 Jul '21, 13:44)</span> <span class="comment-user userinfo">vsaadnet</span>
</div>
</div>
</div>
<div id="comment-tools-80849" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80849-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80850"></span>

<div id="answer-container-80850" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80850-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://www.mapotempo.com/">Mapotempo</a> might help you. It's commercial and opensource.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '21, 13:37</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-80850" class="comments-container">
<span id="80865"></span>
<div id="comment-80865" class="comment">
<div id="post-80865-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it's not opensource</p>
</div>
<div id="comment-80865-info" class="comment-info">
<span class="comment-age">(08 Jul '21, 13:46)</span> <span class="comment-user userinfo">vsaadnet</span>
</div>
</div>
<span id="80866"></span>
<div id="comment-80866" class="comment">
<div id="post-80866-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>They <a href="https://www.mapotempo.com/en/about/">claim otherwise</a>. And they <a href="https://github.com/Mapotempo">share their code</a> on Github.</p>
</div>
<div id="comment-80866-info" class="comment-info">
<span class="comment-age">(08 Jul '21, 15:08)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="81632"></span>
<div id="comment-81632" class="comment">
<div id="post-81632-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for pointing out Mapotempo. If I may bring more precision, We have multiple projects which are or were open source.</p>
<p>First, Mapotempo-Web is a web application. It was open-source, but it is not anymore as we focus on sharing general purpose micro-services instead.</p>
<p>In your case <a href="https://help.openstreetmap.org/users/17232/vsaadnet">@vsaadnet</a>, you probably need <a href="https://github.com/Mapotempo/optimizer-api">Optimizer-API</a> which provide a wrapper towards <a href="https://github.com/google/or-tools">OR-Tools</a> and <a href="https://github.com/VROOM-Project/vroom">VROOM</a>. It also provides multiple internal resolution methods. This project in entirely open source. You can transmit your problem in JSON</p>
<p>If you only need a wrapper to use OR-Tools, we also provide this project <a href="https://github.com/Mapotempo/optimizer-ortools">https://github.com/Mapotempo/optimizer-ortools</a> The exchange format is in Protobuf</p>
</div>
<div id="comment-81632-info" class="comment-info">
<span class="comment-age">(06 Sep '21, 10:17)</span> <span class="comment-user userinfo">Sheeplieder</span>
</div>
</div>
</div>
<div id="comment-tools-80850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80850-form-container" class="comment-form-container">
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

