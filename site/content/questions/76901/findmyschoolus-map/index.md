+++
type = "question"
title = "Findmyschool.us map"
description = '''Good Morning. I am new to this map editing and I wanted to see if I could get some guidance or assistance.  We are a school district and are using the website Findmyschool.us (which gets its information from openstreetmap.org) for our campuses to verify which campuses students go to when they come i...'''
date = "2020-09-30T13:34:00Z"
lastmod = "2020-09-30T14:18:00Z"
weight = 76901
keywords = [ "school" ]
aliases = [ "/questions/76901" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Findmyschool.us map](/questions/76901/findmyschoolus-map)

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
<span id="post-76901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76901-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good Morning. I am new to this map editing and I wanted to see if I could get some guidance or assistance.</p>
<p>We are a school district and are using the website Findmyschool.us (which gets its information from openstreetmap.org) for our campuses to verify which campuses students go to when they come in to register. One of our schools in not in the map and when our routing program tries to upload the boundaries to findmyschool.us, it won't upload those boundaries because there is no school attached to it. I know that we asked our routing program to help us figure this out, but I thought I would ask here as well to see if anyone else could give me any assistance.</p>
<p>School is Newton Collins Elementary at 7609 APOGEE BLVD, AUSTIN, TX with Federal ID #481662013609. I was able to add the building on the map, however, i dont see any difference in my routing program to be able to add the school and upload the boundaries.</p>
<p>Thank you in advance for any thoughts or ideas on what we can do to add this campus to the map.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-school" rel="tag" title="see questions tagged &#39;school&#39;">school</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Sep '20, 13:34</strong></p>
<img src="https://secure.gravatar.com/avatar/9e9c6aa4ae85d955e9c77ab018079d23?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="clbbus&#39;s gravatar image" />
<p><span>clbbus</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="clbbus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76901" class="comments-container">
&#10;</div>
<div id="comment-tools-76901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76901-form-container" class="comment-form-container">
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

<span id="76902"></span>

<div id="answer-container-76902" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76902-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think your problem is that external sites (FindMySchool, routers) may only refresh their data from OSM periodically.</p>
<p>Routing programs tend to take a little while to get the latest data from OSM. This is a common issue. Each router will update on their own timescale: the ones directly available on the OSM site may update every week or so, but many will have a monthly refresh (building the routing graph can be extremely compute intensive).</p>
<p>The Find My School site will also update on a periodic basis, which may be daily, weekly or monthly. Unfortunately it doesn't seem to have much additional information that I can see, but determining their refresh period would probably help your planning.</p>
<p>The school is accurately mapped, thanks for that, however I have one minor remark: in OSM we spell names out in full (so Newton Collins Elementary School, Apogee Boulevard etc) - it's relatively easy to contract names, but much harder to correctly expand them, particularly when contractions differ even within a language.</p>
<p>Finally, it's a real pleasure to discover another way in which OSM data has been used in earnest.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Sep '20, 14:12</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-76902" class="comments-container">
<span id="76903"></span>
<div id="comment-76903" class="comment">
<div id="post-76903-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you for this insight. I have updated the school name appropriately so it shows up correctly. I have reached out to our routing program to see if they can get in contact with anyone at findmyschool.us to help us get this corrected ASAP, especially since this school has now been here for two years.</p>
</div>
<div id="comment-76903-info" class="comment-info">
<span class="comment-age">(30 Sep '20, 14:18)</span> <span class="comment-user userinfo">clbbus</span>
</div>
</div>
</div>
<div id="comment-tools-76902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76902-form-container" class="comment-form-container">
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

