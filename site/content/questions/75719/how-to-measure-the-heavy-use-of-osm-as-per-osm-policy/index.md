+++
type = "question"
title = "How to measure the &quot;Heavy use&quot; of OSM as per OSM policy"
description = '''In OSM policies,I saw &quot;Heavy use&quot; clause in policy Requirements. Could you please provide us some more details with respect to usage of MAP. How can we quantify or measure our usage and check our usage is heavy or not? So that OSM will not block our application. https://operations.osmfoundation.org/...'''
date = "2020-07-15T10:59:00Z"
lastmod = "2020-07-15T15:12:00Z"
weight = 75719
keywords = [ "heavy", "use" ]
aliases = [ "/questions/75719" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to measure the "Heavy use" of OSM as per OSM policy](/questions/75719/how-to-measure-the-heavy-use-of-osm-as-per-osm-policy)

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
<span id="post-75719-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75719-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75719-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In OSM policies,I saw "Heavy use" clause in policy Requirements. Could you please provide us some more details with respect to usage of MAP. How can we quantify or measure our usage and check our usage is heavy or not? So that OSM will not block our application. <a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-heavy" rel="tag" title="see questions tagged &#39;heavy&#39;">heavy</span> <span class="post-tag tag-link-use" rel="tag" title="see questions tagged &#39;use&#39;">use</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jul '20, 10:59</strong></p>
<img src="https://secure.gravatar.com/avatar/3d9b989785995a44bbb91888df7f0b28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashish_Walke&#39;s gravatar image" />
<p><span>Ashish_Walke</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashish_Walke has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75719" class="comments-container">
&#10;</div>
<div id="comment-tools-75719" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75719-form-container" class="comment-form-container">
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

<span id="75725"></span>

<div id="answer-container-75725" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75725-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-75725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The page that you link to says "heavy use" twice. One is in this sentence:</p>
<pre><code>Heavy use of OSM tiles adversely affects people’s ability to edit the map, and is an abuse of the individual donations and sponsorship which provide hardware and bandwidth</code></pre>
<p>and another is here:</p>
<pre><code>Heavy use (e.g. distributing an app that uses tiles from openstreetmap.org) is forbidden without prior permission from the Operations Working Group. See below for alternatives.</code></pre>
<p>Presumably it's the second one that you're referring to. The "e.g." part explains the sort of thing that might cause a problem - you distribute an app and encourage people to use it, so lots of people who you have no control of might download your app and try and download lots of data (until they are all blocked). For completeness, further down it also says:</p>
<pre><code>Bulk downloading is strongly discouraged. Do not download tiles unnecessarily.</code></pre>
<p>Can you explain what you are planning to do, and also perhaps why you are planning to use OSM's tile servers rather than <a href="https://switch2osm.org/serving-tiles/">creating your own</a>?</p>
<p>(edit)</p>
<p>After reading <a href="https://help.openstreetmap.org/questions/75718/what-is-ot-how-to-decide-valid-http-user-agent-application-name-to-avoid-osm-blockage">another question of yours</a> it would appear that "distributing an app that uses tiles from openstreetmap.org" is <em>exactly</em> what you are planning to do. Don't do that - you'll get blocked. Create your own tiles and use those instead.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '20, 15:12</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jul '20, 15:16</strong> </span></p>
</div>
</div>
<div id="comments-container-75725" class="comments-container">
&#10;</div>
<div id="comment-tools-75725" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75725-form-container" class="comment-form-container">
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

