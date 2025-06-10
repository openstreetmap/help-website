+++
type = "question"
title = "How and where are openstreetmap data stored?"
description = '''This could look like quite a basic question but I can&#x27;t find a clear answer on the Internet... I was simply wondering what DBMS was used to store OSM data. By entering such a question on Google, you get so many informations on how to extract data and import them into various DBMS, but no basic infor...'''
date = "2015-09-24T19:55:00Z"
lastmod = "2015-09-25T11:24:00Z"
weight = 45572
keywords = [ "development", "server", "database" ]
aliases = [ "/questions/45572" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How and where are openstreetmap data stored?](/questions/45572/how-and-where-are-openstreetmap-data-stored)

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
<span id="post-45572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45572-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-45572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This could look like quite a basic question but I can't find a clear answer on the Internet... I was simply wondering what DBMS was used to store OSM data. By entering such a question on Google, you get so many informations on how to extract data and import them into various DBMS, but no basic information (just for curious guys) about the way data are stored. I recently read about NoSQL that was based on Key-Value pairs, which reminded me the way OSM data are tagged. Is OSM on NoSQL? Or PostgreSQL? Or any other DBMS? Many thanks for your answers.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '15, 19:55</strong></p>
<img src="https://secure.gravatar.com/avatar/0392d1e09809dd296ca425cb4d5f9996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiltomap&#39;s gravatar image" />
<p><span>wiltomap</span><br />
<span class="score" title="111 reputation points">111</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiltomap has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Sep '15, 20:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45572" class="comments-container">
&#10;</div>
<div id="comment-tools-45572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45572-form-container" class="comment-form-container">
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

<span id="45573"></span>

<div id="answer-container-45573" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45573-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-45573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wiltomap has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM started out on MySQL but has changed to PostgreSQL (not PostGIS) in 2009 and that's what we still use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '15, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Sep '15, 20:10</strong> </span></p>
</div>
</div>
<div id="comments-container-45573" class="comments-container">
<span id="45596"></span>
<div id="comment-45596" class="comment">
<div id="post-45596-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Note that PostGIS is often used in derived databases, like rendering and geocoding.</p>
</div>
<div id="comment-45596-info" class="comment-info">
<span class="comment-age">(25 Sep '15, 11:24)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45573-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45574"></span>

<div id="answer-container-45574" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45574-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-45574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <a href="https://wiki.openstreetmap.org/wiki/Database">https://wiki.openstreetmap.org/wiki/Database</a> and see <a href="https://wiki.openstreetmap.org/wiki/Develop">https://wiki.openstreetmap.org/wiki/Develop</a> "for curious guys". :-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '15, 20:07</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Sep '15, 20:27</strong> </span></p>
</div>
</div>
<div id="comments-container-45574" class="comments-container">
<span id="45576"></span>
<div id="comment-45576" class="comment">
<div id="post-45576-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Many thanks to the both of you! I'm gonna have a closer look at it.</p>
</div>
<div id="comment-45576-info" class="comment-info">
<span class="comment-age">(24 Sep '15, 20:45)</span> <span class="comment-user userinfo">wiltomap</span>
</div>
</div>
</div>
<div id="comment-tools-45574" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45574-form-container" class="comment-form-container">
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

