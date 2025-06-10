+++
type = "question"
title = "House numbers don&#x27;t work when routing"
description = '''I downloaded OpenStreetMap maps from http://garmin.openstreetmap.nl and put them on my Garmin GPS. Everything works except for routing to house numbers. It can only route to the street itself, not to an actual address. So, if I were to enter 1221 Main St, the GPS would take me to Main St, but not to...'''
date = "2013-12-26T15:35:00Z"
lastmod = "2013-12-26T16:45:00Z"
weight = 29340
keywords = [ "housenumbers", "garmin", "routing" ]
aliases = [ "/questions/29340" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [House numbers don't work when routing](/questions/29340/house-numbers-dont-work-when-routing)

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
<span id="post-29340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29340-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I downloaded OpenStreetMap maps from <a href="http://garmin.openstreetmap.nl">http://garmin.openstreetmap.nl</a> and put them on my Garmin GPS. Everything works except for routing to house numbers. It can only route to the street itself, not to an actual address. So, if I were to enter 1221 Main St, the GPS would take me to Main St, but not to the 1221 address. This is a major problem if I can't enter a full address in to route! If the house numbers show up in Nominatim, then why do they not show up on the GPS? Should use another site for OSM Maps?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Dec '13, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/b8f0abc33b0497474371dd84d9287786?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="auser1000&#39;s gravatar image" />
<p><span>auser1000</span><br />
<span class="score" title="56 reputation points">56</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="auser1000 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29340" class="comments-container">
<span id="29343"></span>
<div id="comment-29343" class="comment">
<div id="post-29343-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would find out first whether the addresses are mapped in the area You are interested in. It might be that there is simply no address data. If you need help checking the address data, then please specify which Main street it is (there are some 20 000+ ways named Main street).</p>
<p>It might be that <a href="http://garmin.openstreetmap.nl">http://garmin.openstreetmap.nl</a> does not support house numbers, but I doubt it.</p>
</div>
<div id="comment-29343-info" class="comment-info">
<span class="comment-age">(26 Dec '13, 16:45)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
</div>
<div id="comment-tools-29340" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29340-form-container" class="comment-form-container">
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

<span id="29342"></span>

<div id="answer-container-29342" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29342-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I haven't use OSM data on a Garmin device, so I can't say for sure what the issue is. But there are two things that come to mind:</p>
<ol>
<li>Is the addr:housenumber=1221 tag set on your destination in OSM? It is my understanding that Nominatim will fall back to using TIGER based address number estimates if it can't find the actual number in the OSM database. I know for a fact that OsmAnd only uses OSM data and ends up with the same problem you describe if the address is not in OSM.</li>
<li>It might be that the Garmin downloads being generated by Dave Hansen for the US (I assume a US location based on your 1221 Main St example) will extract and package the information differently. See <a href="https://lists.openstreetmap.org/pipermail/talk-us/2013-December/012333.html">https://lists.openstreetmap.org/pipermail/talk-us/2013-December/012333.html</a></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Dec '13, 16:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-29342" class="comments-container">
&#10;</div>
<div id="comment-tools-29342" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29342-form-container" class="comment-form-container">
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

