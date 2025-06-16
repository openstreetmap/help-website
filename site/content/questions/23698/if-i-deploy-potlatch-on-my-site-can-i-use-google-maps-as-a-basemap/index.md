+++
type = "question"
title = "If I deploy Potlatch on my site, can I use google maps as a basemap?"
description = '''I&#x27;m working on a project on HistoryPin, which already has google base maps uploaded to its site. I want to allow people to draw old railroad lines on the base map using Potlatch, and also upload GPS traces if possible. '''
date = "2013-06-25T19:10:00Z"
lastmod = "2013-06-25T22:41:00Z"
weight = 23698
keywords = [ "potlatch2", "railroad", "google", "gps" ]
aliases = [ "/questions/23698" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [If I deploy Potlatch on my site, can I use google maps as a basemap?](/questions/23698/if-i-deploy-potlatch-on-my-site-can-i-use-google-maps-as-a-basemap)

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
<span id="post-23698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23698-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm working on a project on HistoryPin, which already has google base maps uploaded to its site. I want to allow people to draw old railroad lines on the base map using Potlatch, and also upload GPS traces if possible.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-railroad" rel="tag" title="see questions tagged &#39;railroad&#39;">railroad</span> <span class="post-tag tag-link-google" rel="tag" title="see questions tagged &#39;google&#39;">google</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jun '13, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/d551f56884954e99919800fa6019f4e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yankwich&#39;s gravatar image" />
<p><span>yankwich</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yankwich has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Apr '15, 04:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-23698" class="comments-container">
&#10;</div>
<div id="comment-tools-23698" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23698-form-container" class="comment-form-container">
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

<span id="23699"></span>

<div id="answer-container-23699" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23699-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-23699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Potlatch_2">Potlatch</a> (1 and 2) is Free software, so you can <a href="https://github.com/systemed/potlatch2/blob/master/LICENCE.txt">do whatever you like with it</a> without breaking its licence conditions. However, Google's terms of service probably will not allow you to derive a separate database of information from its maps and imagery unless you use its Map API at least.</p>
<p>If you do deploy a version of Potlatch for this project, it must not connect to OSM in any way, so you would need to provide your own servers to store your data on. This would have to run the OSM "<a href="https://wiki.openstreetmap.org/wiki/The_Rails_Port">Rails Port</a>" as it's known, as Potlatch can't save data to any other type of server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '13, 19:42</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '13, 19:46</strong> </span></p>
</div>
</div>
<div id="comments-container-23699" class="comments-container">
<span id="23701"></span>
<div id="comment-23701" class="comment">
<div id="post-23701-score" class="comment-score">
6
</div>
<div class="comment-text">
<p><a href="http://www.google.co.uk/permissions/geoguidelines.html">http://www.google.co.uk/permissions/geoguidelines.html</a> states "You may not use Google Maps or Google Earth as the basis for tracing your own maps or other geographic content."</p>
</div>
<div id="comment-23701-info" class="comment-info">
<span class="comment-age">(25 Jun '13, 21:29)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23699" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23699-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23704"></span>

<div id="answer-container-23704" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23704-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-23704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Potlatch 2 has a hard-coded block on sources of imagery which contain the string 'google.'. You can remove this by taking the relevant line out of potlatch2.mxml and recompiling.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '13, 22:41</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-23704" class="comments-container">
&#10;</div>
<div id="comment-tools-23704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23704-form-container" class="comment-form-container">
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

