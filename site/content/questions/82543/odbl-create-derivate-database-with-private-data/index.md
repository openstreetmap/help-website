+++
type = "question"
title = "ODbL : Create derivate database with private data"
description = '''I am working on a search engine map project (It&#x27;s free access, but there are ads) that use a geocoder to search POI from text, and I would like to integrate partner private data to our database imported with Imposm. According to the ODBL licence, this database should be considered a Derivative Datab...'''
date = "2021-11-11T19:50:00Z"
lastmod = "2021-11-16T08:10:00Z"
weight = 82543
keywords = [ "copyright", "legal", "database" ]
aliases = [ "/questions/82543" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ODbL : Create derivate database with private data](/questions/82543/odbl-create-derivate-database-with-private-data)

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
<span id="post-82543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82543-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am working on a search engine map project (It's free access, but there are ads) that use a geocoder to search POI from text, and I would like to integrate partner private data to our database imported with Imposm.</p>
<p>According to the ODBL licence, this database should be considered a Derivative Database. However, it is not clear in my mind : can I enrich OSM POIs with our private partner data, or should I create two separate databases in order to not mix OSM and private partner data in our geocoder search?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-copyright" rel="tag" title="see questions tagged &#39;copyright&#39;">copyright</span> <span class="post-tag tag-link-legal" rel="tag" title="see questions tagged &#39;legal&#39;">legal</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Nov '21, 19:50</strong></p>
<img src="https://secure.gravatar.com/avatar/2b287dbe0941a7d8347309bf22887dfe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fatal69300&#39;s gravatar image" />
<p><span>fatal69300</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fatal69300 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Nov '21, 17:16</strong> </span></p>
</div>
</div>
<div id="comments-container-82543" class="comments-container">
&#10;</div>
<div id="comment-tools-82543" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82543-form-container" class="comment-form-container">
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

<span id="82548"></span>

<div id="answer-container-82548" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82548-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not a lawyer but when I had a similar situation I used two databases, one for the OSM data and one for the proprietary data. It meant that I had to do two queries and merge the results at run time which is less efficient but it also meant there was no doubt in my mind that I was properly following the OSM licensing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Nov '21, 16:00</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-82548" class="comments-container">
<span id="82549"></span>
<div id="comment-82549" class="comment">
<div id="post-82549-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. Indeed, I think I don't have the competency to understand ODBl licensing. I will keep the two database separate and ask a lawyer if necessary</p>
</div>
<div id="comment-82549-info" class="comment-info">
<span class="comment-age">(12 Nov '21, 17:40)</span> <span class="comment-user userinfo">fatal69300</span>
</div>
</div>
</div>
<div id="comment-tools-82548" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82548-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82595"></span>

<div id="answer-container-82595" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82595-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should have a look at the community guidelines <a href="https://wiki.osmfoundation.org/wiki/Licence/Community_Guidelines">https://wiki.osmfoundation.org/wiki/Licence/Community_Guidelines</a> in particular <a href="https://wiki.osmfoundation.org/wiki/Licence/Community_Guidelines/Collective_Database_Guideline_Guideline">https://wiki.osmfoundation.org/wiki/Licence/Community_Guidelines/Collective_Database_Guideline_Guideline</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '21, 08:10</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-82595" class="comments-container">
&#10;</div>
<div id="comment-tools-82595" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82595-form-container" class="comment-form-container">
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

