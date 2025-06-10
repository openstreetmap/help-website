+++
type = "question"
title = "Determining speed limits for given route"
description = '''I am trying to develop an application, which finds a route between two points, and displays current speed limits as you drive. So far I managed to use OSRM API ( http://project-osrm.org/ ) to get a route geometry (as a list of coordinates) and driving directions (as simple instructions, not correlat...'''
date = "2014-04-25T23:13:00Z"
lastmod = "2018-04-03T19:19:00Z"
weight = 32644
keywords = [ "ways", "osrm", "maxspeed", "limit", "routing" ]
aliases = [ "/questions/32644" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Determining speed limits for given route](/questions/32644/determining-speed-limits-for-given-route)

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
<span id="post-32644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32644-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to develop an application, which finds a route between two points, and displays current speed limits as you drive.</p>
<p>So far I managed to use OSRM API ( <a href="http://project-osrm.org/">http://project-osrm.org/</a> ) to get a route geometry (as a list of coordinates) and driving directions (as simple instructions, not correlated with OSM objects). I am also aware, that some ways in OSM provide numeric values of speed limits in their tags. What I don't know is how to cherry-pick the needed ways from Overpass API (ideally without any excessive data) and how to associate my route geometry with proper limits. Or maybe there is an other, more comprehensive tool capable of satisfying my needs?</p>
<p>Thank you in advance for any help!</p>
<p><strong>EDIT: I already received a great answer for my problem, but out of curiosity I would also appreciate a solution which does not involve interfering in OSRM API</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-limit" rel="tag" title="see questions tagged &#39;limit&#39;">limit</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '14, 23:13</strong></p>
<img src="https://secure.gravatar.com/avatar/f436d9f64b0c453c0186ba7ba1517e0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="soul123&#39;s gravatar image" />
<p><span>soul123</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="soul123 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Sep '16, 09:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span></p>
</div>
</div>
<div id="comments-container-32644" class="comments-container">
&#10;</div>
<div id="comment-tools-32644" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32644-form-container" class="comment-form-container">
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

<span id="32648"></span>

<div id="answer-container-32648" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32648-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="soul123 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It may be easier to do this by setting up your own instance of OSRM. You can then return the speed limit as part of the turn-by-turn directions, rather than just the road number.</p>
<p>You would typically do this in the Lua profile of your OSRM instance. In way_function, after way.name has been set to the ref/name, add code such as this:</p>
<pre><code>if maxspeed&gt;0 then way.name=way.name..&quot;|&quot;..maxspeed end</code></pre>
<p>In other words, if there's a maxspeed value for the way, append it to the way name, separated by a | symbol.</p>
<p>You can then parse this value in your JavaScript (or other) client.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '14, 12:18</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '14, 12:18</strong> </span></p>
</div>
</div>
<div id="comments-container-32648" class="comments-container">
<span id="32659"></span>
<div id="comment-32659" class="comment">
<div id="post-32659-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for this answer, it's great and accurate!</p>
</div>
<div id="comment-32659-info" class="comment-info">
<span class="comment-age">(26 Apr '14, 13:22)</span> <span class="comment-user userinfo">soul123</span>
</div>
</div>
<span id="52224"></span>
<div id="comment-52224" class="comment">
<div id="post-52224-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How is this solved in the last version of API (Version 5). Let's say if we want to use the default car profile, what exactly should be changed to get the speed limits too? Where exactly should the speed limits appear in the resulting JSON? Thanks</p>
</div>
<div id="comment-52224-info" class="comment-info">
<span class="comment-age">(26 Sep '16, 16:50)</span> <span class="comment-user userinfo">pksk88</span>
</div>
</div>
<span id="54887"></span>
<div id="comment-54887" class="comment">
<div id="post-54887-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi - sorry to "me too", but I'm also looking for a method to do this in the current API. The car.lua profile files appear to be substantially different from the those in the answers suggested so far. Many thanks.</p>
</div>
<div id="comment-54887-info" class="comment-info">
<span class="comment-age">(02 Mar '17, 14:05)</span> <span class="comment-user userinfo">AndyC</span>
</div>
</div>
</div>
<div id="comment-tools-32648" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32648-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52295"></span>

<div id="answer-container-52295" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52295-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For the current version of API I used this temporary solution, analogous to the above mentioned. Using the car.lua profile you may insert the maxspeed attribute as part of other attributes. This could be done on multiple places. I added the</p>
<pre><code>local maxspeed = parse_maxspeed( way:get_value_by_key(&quot;maxspeed&quot;) )</code></pre>
<p>on line 430 and then on line 446 changed the code to</p>
<pre><code>result.ref = ref..&quot;|&quot;..maxspeed</code></pre>
<p>This is a very simple way but not really standard. I would like to create a separate JSON attribute for maxspeed in the response of API.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Sep '16, 08:05</strong></p>
<img src="https://secure.gravatar.com/avatar/e7b6aab57b354bb4867304cd404610f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pksk88&#39;s gravatar image" />
<p><span>pksk88</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pksk88 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52295" class="comments-container">
&#10;</div>
<div id="comment-tools-52295" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52295-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62892"></span>

<div id="answer-container-62892" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62892-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hey! Is there a similar solution for the current version? I really don't know where to put the suggested lines of code. Or respectively how to modify them to either adding the maxspeed attribute to another attribute or creating a new attribute in the output. That would be of great help for me - many thanks in advance.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Apr '18, 19:12</strong></p>
<img src="https://secure.gravatar.com/avatar/154d82054ffb4710f4c703546505f04c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jandoh&#39;s gravatar image" />
<p><span>jandoh</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jandoh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62892" class="comments-container">
<span id="62893"></span>
<div id="comment-62893" class="comment">
<div id="post-62893-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm not an expert on the current OSRM API profiles, but it might be worth asking the developers at <a href="https://github.com/Project-OSRM/osrm-backend/issues">https://github.com/Project-OSRM/osrm-backend/issues</a> (you'll need a Github account).</p>
</div>
<div id="comment-62893-info" class="comment-info">
<span class="comment-age">(03 Apr '18, 19:19)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62892" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62892-form-container" class="comment-form-container">
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

