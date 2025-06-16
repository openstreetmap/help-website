+++
type = "question"
title = "OSM map in my web application"
description = '''Hi, I have another question about OSM. On a server I have a system that tells me in which car park I can park if I give it an origin and a destination in coordinates. Now I would like a web application to have a visual representation of the use case. I&#x27;m using nodejs with express. For the moment I w...'''
date = "2018-07-12T08:49:00Z"
lastmod = "2018-07-14T07:04:00Z"
weight = 64670
keywords = [ "website", "map", "usage" ]
aliases = [ "/questions/64670" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [OSM map in my web application](/questions/64670/osm-map-in-my-web-application)

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
<span id="post-64670-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64670-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64670-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have another question about OSM. On a server I have a system that tells me in which car park I can park if I give it an origin and a destination in coordinates.</p>
<p>Now I would like a web application to have a visual representation of the use case. I'm using nodejs with express. For the moment I would like to know <em>how I can put a map on my site and add the points of origin and destination to it and then send it to my server</em> and tell me which parking lot to park.</p>
<p>Thank you very much.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '18, 08:49</strong></p>
<img src="https://secure.gravatar.com/avatar/12362b906d5b7ffd3bfbe8811ecd7c2c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wolfindel&#39;s gravatar image" />
<p><span>Wolfindel</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wolfindel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jul '18, 20:00</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-64670" class="comments-container">
&#10;</div>
<div id="comment-tools-64670" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64670-form-container" class="comment-form-container">
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

<span id="64711"></span>

<div id="answer-container-64711" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64711-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Deploying_your_own_Slippy_Map">https://wiki.openstreetmap.org/wiki/Deploying_your_own_Slippy_Map</a> may help you. I do not know which library has the option to let the user set markers whose coordinates will be transferred to the server afterwards. I guess your goal is similar to the routing interface on <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> or <a href="https://graphhopper.com/maps/">https://graphhopper.com/maps/</a> , so have a look at their code for inspiration.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '18, 21:25</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-64711" class="comments-container">
&#10;</div>
<div id="comment-tools-64711" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64711-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64718"></span>

<div id="answer-container-64718" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64718-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For a similar type project i used LeafletJS (<a href="https://leafletjs.com">https://leafletjs.com</a>). You can check their doc and examples. I hope it might help you to find a solution.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '18, 07:04</strong></p>
<img src="https://secure.gravatar.com/avatar/96bf4c3a8875db84432298eba29efbc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nasirkhan&#39;s gravatar image" />
<p><span>nasirkhan</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nasirkhan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64718" class="comments-container">
&#10;</div>
<div id="comment-tools-64718" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64718-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64697"></span>

<div id="answer-container-64697" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64697-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I answer myself because I have made progress on it. I am using <a href="https://wiki.openstreetmap.org/wiki/OpenLayers">OpenLayers</a> for this. There are a lot of examples for him, but you have to fight a little bit. Some explanations are not of high quality. Open layers has examples and API documentation. It is used together with HTML and CSS so some basic notions of these would be nice.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '18, 12:55</strong></p>
<img src="https://secure.gravatar.com/avatar/12362b906d5b7ffd3bfbe8811ecd7c2c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wolfindel&#39;s gravatar image" />
<p><span>Wolfindel</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wolfindel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '18, 21:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-64697" class="comments-container">
&#10;</div>
<div id="comment-tools-64697" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64697-form-container" class="comment-form-container">
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

