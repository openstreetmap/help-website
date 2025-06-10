+++
type = "question"
title = "OpenStreetMap inside a WebApp built in reactJS"
description = '''I want to show a Highway on OpenStreetMap on my React Web App and then Mark Toll Booths, Petrol Pumps, Highway Malls etc on that highway on OpenSteetMap. When I click on the marker for a particular Toll Booth or Petrol Pump I want to show a Modal and show details of the place. Also, I want to add hi...'''
date = "2020-07-15T20:25:00Z"
lastmod = "2020-07-16T19:45:00Z"
weight = 75735
keywords = [ "reactjs" ]
aliases = [ "/questions/75735" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OpenStreetMap inside a WebApp built in reactJS](/questions/75735/openstreetmap-inside-a-webapp-built-in-reactjs)

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
<span id="post-75735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75735-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to show a Highway on OpenStreetMap on my React Web App and then Mark Toll Booths, Petrol Pumps, Highway Malls etc on that highway on OpenSteetMap. When I click on the marker for a particular Toll Booth or Petrol Pump I want to show a Modal and show details of the place.</p>
<p>Also, I want to add highway CCTV locations on the opensteetmap and when clicked on that CCTV icon I want to show a Modal and show the CCTV details from my Database.</p>
<p>I am looking for a article which explains the development of above type of feature in ReactJS with OpenStreetMap</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reactjs" rel="tag" title="see questions tagged &#39;reactjs&#39;">reactjs</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jul '20, 20:25</strong></p>
<img src="https://secure.gravatar.com/avatar/6bbf789fb08a58eb5b79278798fd635c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="omkarl&#39;s gravatar image" />
<p><span>omkarl</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="omkarl has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75735" class="comments-container">
&#10;</div>
<div id="comment-tools-75735" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75735-form-container" class="comment-form-container">
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

<span id="75747"></span>

<div id="answer-container-75747" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75747-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need a slippy map component for that. The most popular one at the moment is probably Leaflet, and it also offers itself as a react component</p>
<p>See these sites to get started:</p>
<ul>
<li><a href="https://react-leaflet.js.org/">https://react-leaflet.js.org/</a></li>
<li><a href="https://leafletjs.com/">https://leafletjs.com/</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '20, 14:04</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-75747" class="comments-container">
<span id="75753"></span>
<div id="comment-75753" class="comment">
<div id="post-75753-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/280/sanderd17">@sanderd</a>. What is a slippy map in between?</p>
</div>
<div id="comment-75753-info" class="comment-info">
<span class="comment-age">(16 Jul '20, 19:45)</span> <span class="comment-user userinfo">omkarl</span>
</div>
</div>
</div>
<div id="comment-tools-75747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75747-form-container" class="comment-form-container">
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

