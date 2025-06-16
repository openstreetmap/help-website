+++
type = "question"
title = "Do I need an API key for my project?"
description = '''I&#x27;m a Computer Science student at the University of Nottingham, in my third year, developing an Android app as my dissertation project.  I want to use OSM, instead of the standard googlemapview.  Do I need an API key to do this?  The app is my dissertation, and will never be distributed commercially...'''
date = "2011-12-12T11:16:00Z"
lastmod = "2011-12-12T13:17:00Z"
weight = 9453
keywords = [ "usage", "editing", "api" ]
aliases = [ "/questions/9453" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Do I need an API key for my project?](/questions/9453/do-i-need-an-api-key-for-my-project)

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
<span id="post-9453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9453-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-9453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm a Computer Science student at the University of Nottingham, in my third year, developing an Android app as my dissertation project.<br />
I want to use OSM, instead of the standard googlemapview.<br />
Do I need an API key to do this?<br />
</p>
<p>The app is my dissertation, and will never be distributed commercially.</p>
<p>Edit; I want to add data to the map, not only view it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Dec '11, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/4827d40b3569fb5f9c7d0888c1da6197?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ephemeros&#39;s gravatar image" />
<p><span>Ephemeros</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ephemeros has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '13, 14:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></br></p>
</div>
</div>
<div id="comments-container-9453" class="comments-container">
&#10;</div>
<div id="comment-tools-9453" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9453-form-container" class="comment-form-container">
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

<span id="9455"></span>

<div id="answer-container-9455" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9455-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-9455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a few APIs to consider:</p>
<p>The <a href="https://wiki.openstreetmap.org/wiki/API_v0.6">editing api</a> lets you retrieve and edit raw data (including history). It require no "API key" but it requires a registered OSM user for any editing, and it probably looks at your http user agent.</p>
<p>The other apis are the generated-tiles viewing apis similar to googlemapview. A few exist, two popular ones being <a href="https://wiki.openstreetmap.org/wiki/Openlayers">openlayers</a> and <a href="http://leaflet.cloudmade.com/">leaflet</a>. There are also special-purpose apis like <a href="https://wiki.openstreetmap.org/wiki/Nominatim">nominatim</a>. All of these usually require no more than a properly-setup http user agent (and reasonable usage of resources, but that should be no problem for a dissertation project).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '11, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Dec '11, 13:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-9455" class="comments-container">
&#10;</div>
<div id="comment-tools-9455" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9455-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9456"></span>

<div id="answer-container-9456" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9456-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See the answers to <a href="/questions/9367/can-i-use-openstreetmaps-openstreetmaps-api-for-commercial-apps-on-android">this question</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '11, 13:17</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-9456" class="comments-container">
&#10;</div>
<div id="comment-tools-9456" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9456-form-container" class="comment-form-container">
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

