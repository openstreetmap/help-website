+++
type = "question"
title = "How to link ways to form the bigger road"
description = '''I&#x27;m using OSM API (overpy and overpass using Python3) to extract toll roads &quot;toll=yes&quot; in a certain search area (e.g. searchArea = California). The API spits out all the tolled ways in CA split into ways. What I&#x27;d like to see is each toll road as a whole, i.e. not split into ways. Is there a way to ...'''
date = "2017-12-25T20:37:00Z"
lastmod = "2017-12-29T04:35:00Z"
weight = 61358
keywords = [ "ways", "overpass", "osm", "overpy" ]
aliases = [ "/questions/61358" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to link ways to form the bigger road](/questions/61358/how-to-link-ways-to-form-the-bigger-road)

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
<span id="post-61358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61358-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using OSM API (overpy and overpass using Python3) to extract toll roads "toll=yes" in a certain search area (e.g. searchArea = California). The API spits out all the tolled ways in CA split into ways. What I'd like to see is each toll road as a whole, i.e. not split into ways.</p>
<p>Is there a way to regroup all the tiny ways back into the bigger road? How are ways linked in OSM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-overpy" rel="tag" title="see questions tagged &#39;overpy&#39;">overpy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Dec '17, 20:37</strong></p>
<img src="https://secure.gravatar.com/avatar/6c5c32c4fec74724101a722311f79772?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="omarfaskar&#39;s gravatar image" />
<p><span>omarfaskar</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="omarfaskar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61358" class="comments-container">
&#10;</div>
<div id="comment-tools-61358" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61358-form-container" class="comment-form-container">
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

<span id="61372"></span>

<div id="answer-container-61372" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61372-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The ways are linked via common/shared end nodes. Essentially you need to define which properties/tags should be the same over a "bigger road" (for example the name tag) and create one geometry our of the segments by joining them at the end nodes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Dec '17, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Dec '17, 16:00</strong> </span></p>
</div>
</div>
<div id="comments-container-61372" class="comments-container">
&#10;</div>
<div id="comment-tools-61372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61372-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61409"></span>

<div id="answer-container-61409" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61409-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>First extract all &lt;nd ref=""/&gt; tags</li>
<li>Remove duplicate tags with uniq -u</li>
<li>Reassemble into a way with &lt;way&gt;&lt;/way&gt;</li>
<li>Done!</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '17, 04:35</strong></p>
<img src="https://secure.gravatar.com/avatar/100f8ccde5e9799707a5056f94fe183f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wetitpig0&#39;s gravatar image" />
<p><span>Wetitpig0</span><br />
<span class="score" title="307 reputation points">307</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wetitpig0 has 2 accepted answers">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Dec '17, 04:35</strong> </span></p>
</div>
</div>
<div id="comments-container-61409" class="comments-container">
&#10;</div>
<div id="comment-tools-61409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61409-form-container" class="comment-form-container">
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

