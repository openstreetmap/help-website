+++
type = "question"
title = "How do I preserve local data in my local OSM when receiving an update from OSM?"
description = '''I&#x27;d like to run a local instance of OSM with a local db and enable it for updating (adding location point information specific to my industry), but I also want to be able to update my local db with current information from OSM periodically. How do I do that without overwriting my local updates?  I f...'''
date = "2017-12-06T23:28:00Z"
lastmod = "2017-12-07T02:05:00Z"
weight = 61060
keywords = [ ".osc", "local", "update" ]
aliases = [ "/questions/61060" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I preserve local data in my local OSM when receiving an update from OSM?](/questions/61060/how-do-i-preserve-local-data-in-my-local-osm-when-receiving-an-update-from-osm)

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
<span id="post-61060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61060-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to run a local instance of OSM with a local db and enable it for updating (adding location point information specific to my industry), but I also want to be able to update my local db with current information from OSM periodically. How do I do that without overwriting my local updates?</p>
<p>I found this question, which seems related: <a href="/questions/54827/editing-osm-files-locally">https://help.openstreetmap.org/questions/54827/editing-osm-files-locally</a></p>
<p>It would seem I can saved my edits, and then use Osmosis, osmconvert, or osmium to create an .osc file. Can I then download a new JOSM file and apply the .osc file? Would it be feasible to then repeat this process, say, once a month?</p>
<p>If I'm wrong, is there another way to do this?</p>
<p>Not really asking right now for the instruction list on how to do all of this, just hoping someone can confirm this scenario is possible.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-.osc" rel="tag" title="see questions tagged &#39;.osc&#39;">.osc</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '17, 23:28</strong></p>
<img src="https://secure.gravatar.com/avatar/6adc2a8d32cda3e4558d888bbabcb8e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="drr37&#39;s gravatar image" />
<p><span>drr37</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="drr37 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '17, 23:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/8440750fd002fd989ab2e6b613ca3ccb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsh4&#39;s gravatar image" />
<p><span>dsh4</span><br />
<span class="score" title="867 reputation points">867</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span></p>
</div>
</div>
<div id="comments-container-61060" class="comments-container">
&#10;</div>
<div id="comment-tools-61060" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61060-form-container" class="comment-form-container">
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

<span id="61063"></span>

<div id="answer-container-61063" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61063-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-61063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When I had a similar issue I simply put the local data into a separate database. In my case I was rendering a map for printing and it was easy to setup the map rendering to apply the local data as layers on top of the OSM data. When I wanted to update the OSM data it was simple, just delete all the OSM tables, etc. and re-import the OSM data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '17, 02:05</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-61063" class="comments-container">
&#10;</div>
<div id="comment-tools-61063" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61063-form-container" class="comment-form-container">
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

