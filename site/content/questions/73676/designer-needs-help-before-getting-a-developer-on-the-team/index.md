+++
type = "question"
title = "Designer needs help before getting a developer on the team"
description = '''Hi, I am creating a WordPress site that let users:  Create ads: each user has a spanish postal code on profile page that gives location to all his ads Search ads: users can enter a postal code to filter results by distance from that input postal code to ad’s postal code. Showing near ones first  I h...'''
date = "2020-03-21T18:02:00Z"
lastmod = "2020-03-23T14:48:00Z"
weight = 73676
keywords = [ "free" ]
aliases = [ "/questions/73676" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Designer needs help before getting a developer on the team](/questions/73676/designer-needs-help-before-getting-a-developer-on-the-team)

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
<span id="post-73676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73676-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am creating a WordPress site that let users:</p>
<ol>
<li>Create ads: each user has a spanish postal code on profile page that gives location to all his ads</li>
<li>Search ads: users can enter a postal code to filter results by distance from that input postal code to ad’s postal code. Showing near ones first</li>
</ol>
<p>I have a database with latitude/longitude for each postal code, and my project do not have big economy, so <strong>I am afraid of having good results and die because route costs</strong>.</p>
<p>I am the founder and designer, without backend programmer yet, so I don’t understand good the documentation, sorry about that,</p>
<p><strong>I need to know what free options I can choose to provide that service, forgeting about number of distance requests</strong></p>
<p>Thanks for your time,</p>
<p>Raul</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-free" rel="tag" title="see questions tagged &#39;free&#39;">free</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Mar '20, 18:02</strong></p>
<img src="https://secure.gravatar.com/avatar/60f4c60958c8cb894842de53dd581eef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raulserrano&#39;s gravatar image" />
<p><span>raulserrano</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raulserrano has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73676" class="comments-container">
&#10;</div>
<div id="comment-tools-73676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73676-form-container" class="comment-form-container">
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

<span id="73677"></span>

<div id="answer-container-73677" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73677-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-73677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="raulserrano has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no service that will give unlimited free CPU power to your commercial enterprise. However, OpenStreetMap data is openly licensed and good Open Source routing software is available too; you could for example install <code>Graphhopper</code>, <code>OSRM</code>, or <code>Valhalla</code> on your own server machine, and then make as many requests as you want without paying anyone (except of course your hosting provider for your own server). <code>Graphhopper</code> probably offers the easiest start, just follow <a href="https://www.graphhopper.com/blog/2018/09/25/getting-started-with-graphhopper-0-11-and-jdk-11/">https://www.graphhopper.com/blog/2018/09/25/getting-started-with-graphhopper-0-11-and-jdk-11/</a> (and download data for Spain instead of Berlin).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Mar '20, 18:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Mar '20, 18:18</strong> </span></p>
</div>
</div>
<div id="comments-container-73677" class="comments-container">
<span id="73678"></span>
<div id="comment-73678" class="comment">
<div id="post-73678-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That sounds as a really good option! — Thanks Frederik!</p>
<hr />
<p>ps: This forum is OSQA? their website looks like dead...</p>
</div>
<div id="comment-73678-info" class="comment-info">
<span class="comment-age">(21 Mar '20, 18:34)</span> <span class="comment-user userinfo">raulserrano</span>
</div>
</div>
<span id="73705"></span>
<div id="comment-73705" class="comment">
<div id="post-73705-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/18068/raulserrano">@raulserrano</a>: Yes, this forum is OSQA, and we would like to switch to something that's actively maintained, but haven't found a replacement yet which has the necessary featuers (i.e. voting-based Q&amp;A platform, rather than regular discussions). See: <a href="https://github.com/openstreetmap/operations/issues/149">https://github.com/openstreetmap/operations/issues/149</a></p>
</div>
<div id="comment-73705-info" class="comment-info">
<span class="comment-age">(23 Mar '20, 14:03)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="73707"></span>
<div id="comment-73707" class="comment">
<div id="post-73707-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14/tordanik">@tordanik</a> I was thinking about <a href="https://github.com/discourse/discourse">https://github.com/discourse/discourse</a> and it looks like is already contemplated</p>
</div>
<div id="comment-73707-info" class="comment-info">
<span class="comment-age">(23 Mar '20, 14:48)</span> <span class="comment-user userinfo">raulserrano</span>
</div>
</div>
</div>
<div id="comment-tools-73677" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73677-form-container" class="comment-form-container">
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

