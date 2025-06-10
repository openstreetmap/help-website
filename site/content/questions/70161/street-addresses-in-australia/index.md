+++
type = "question"
title = "Street addresses in Australia..."
description = '''I have noticed that lots of streets have missing street numbers. The data for it is publicly available and I would like to update the maps with the addresses. The street numbers can easily be updated using the latitude and longitude. Can someone advise how to go about doing it?'''
date = "2019-07-22T22:36:00Z"
lastmod = "2019-07-23T02:58:00Z"
weight = 70161
keywords = [ "australia", "street", "addresses" ]
aliases = [ "/questions/70161" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Street addresses in Australia...](/questions/70161/street-addresses-in-australia)

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
<span id="post-70161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70161-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have noticed that lots of streets have missing street numbers. The data for it is publicly available and I would like to update the maps with the addresses.</p>
<p>The street numbers can easily be updated using the latitude and longitude. Can someone advise how to go about doing it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-australia" rel="tag" title="see questions tagged &#39;australia&#39;">australia</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-addresses" rel="tag" title="see questions tagged &#39;addresses&#39;">addresses</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '19, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/5b6f70bd2110230f7c749b8fffa62cc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MichaelSingh02&#39;s gravatar image" />
<p><span>MichaelSingh02</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MichaelSingh02 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70161" class="comments-container">
<span id="70163"></span>
<div id="comment-70163" class="comment">
<div id="post-70163-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As stf mentioned please reach out to the Aussie community on our mailing list <a href="https://lists.openstreetmap.org/listinfo/talk-au.">https://lists.openstreetmap.org/listinfo/talk-au.</a> In short you can't use GNAF but can use VicMap, ACTMapi, NSW Spatial Services data, and a few local councils in QLD. Even then you need to follow the import guidelines from the OSM wiki</p>
</div>
<div id="comment-70163-info" class="comment-info">
<span class="comment-age">(23 Jul '19, 02:58)</span> <span class="comment-user userinfo">aharvey</span>
</div>
</div>
</div>
<div id="comment-tools-70161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70161-form-container" class="comment-form-container">
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

<span id="70162"></span>

<div id="answer-container-70162" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70162-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-70162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This classifies, or at least it sounds to me like it classifies, as an import. Please read the wiki pages on importing data and involve your local Australian mappers in the process. First and foremost, you need to convince your fellow mappers that the copyright on the "publicly available" data is compatible with OSM. Lots of public data is not.</p>
<p>As to the mechanics: There is a plug-in for JOSM that allows you to load spreadsheet data in the form of a CSV file (and probably other formats). But you need to approach this systematically (tasking manager helps) as each and every point should be confirmed to be plausible and if there is any existing house numbers that the data is properly conflated. This is where having a team of your local mappers is vital!</p>
<p>To do any and all of this you need to involve the people on a couple of the email lists, many most of the key players for imports are not people who frequent this help web site.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '19, 01:47</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-70162" class="comments-container">
&#10;</div>
<div id="comment-tools-70162" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70162-form-container" class="comment-form-container">
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

