+++
type = "question"
title = "overpass query for sidewalks widths within a range"
description = '''Hello everybody, I want to make an overpass query which shows me the sidewalks which the width attribute is for example 0.80 m to 0.90 m for them.  (  way[&quot;footway&quot;=&quot;sidewalk&quot;]  [&quot;width&quot;=&quot;0.81 m&quot;]  ({{bbox}}); );  the above mentioned code shows only the side walks with the 0.81 m of width. how can I...'''
date = "2021-06-16T12:18:00Z"
lastmod = "2021-06-21T10:30:00Z"
weight = 80595
keywords = [ "overpass", "query", "sidewalk", "overpass-turbo", "width" ]
aliases = [ "/questions/80595" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [overpass query for sidewalks widths within a range](/questions/80595/overpass-query-for-sidewalks-widths-within-a-range)

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
<span id="post-80595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80595-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everybody, I want to make an overpass query which shows me the sidewalks which the width attribute is for example 0.80 m to 0.90 m for them.</p>
<hr />
<p>( way["footway"="sidewalk"] ["width"="0.81 m"] ({{bbox}}); );</p>
<hr />
<p>the above mentioned code shows only the side walks with the 0.81 m of width. how can I modify my code to search for a range of widths?</p>
<p>thank you in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-sidewalk" rel="tag" title="see questions tagged &#39;sidewalk&#39;">sidewalk</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-width" rel="tag" title="see questions tagged &#39;width&#39;">width</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jun '21, 12:18</strong></p>
<img src="https://secure.gravatar.com/avatar/c01a9b07d33813ce9ee9b3701d56445f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ahmad%20Ataei&#39;s gravatar image" />
<p><span>Ahmad Ataei</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ahmad Ataei has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80595" class="comments-container">
&#10;</div>
<div id="comment-tools-80595" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80595-form-container" class="comment-form-container">
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

<span id="80601"></span>

<div id="answer-container-80601" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80601-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-80601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ahmad Ataei has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://gis.stackexchange.com/questions/301365/overpass-query-search-range-of-integers-not-working-for-2-digit-numbers">https://gis.stackexchange.com/questions/301365/overpass-query-search-range-of-integers-not-working-for-2-digit-numbers</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '21, 01:03</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-80601" class="comments-container">
<span id="80642"></span>
<div id="comment-80642" class="comment">
<div id="post-80642-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Dave. I solved my problem using this link.</p>
<p>Best,,,</p>
</div>
<div id="comment-80642-info" class="comment-info">
<span class="comment-age">(21 Jun '21, 10:24)</span> <span class="comment-user userinfo">Ahmad Ataei</span>
</div>
</div>
</div>
<div id="comment-tools-80601" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80601-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80599"></span>

<div id="answer-container-80599" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80599-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not sure if there is something like range matching but I guess you could use a <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Value_matches_regular_expression_.28.7E.2C_.21.7E.29">regular expressio</a>n if you are not too picky about the ranges. To find 0.8 to 0.99m you could for example look for</p>
<pre><code>( way[&quot;footway&quot;=&quot;sidewalk&quot;][&quot;width&quot;~&quot;^0\.[89]&quot;] ({{bbox}}); );</code></pre>
<p>That would find all values starting with 0.8 or 0.9.</p>
<p>Unfortunately very few sidewalks around here have a width tagged at all so I could not test that expression. Can you point to the aeria you are exploring?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jun '21, 15:14</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-80599" class="comments-container">
<span id="80603"></span>
<div id="comment-80603" class="comment">
<div id="post-80603-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Dave's suggestion with the numerical evaluation is probably the better approach.</p>
</div>
<div id="comment-80603-info" class="comment-info">
<span class="comment-age">(17 Jun '21, 09:08)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="80643"></span>
<div id="comment-80643" class="comment">
<div id="post-80643-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. as you mentioned dave's suggestion is more precise and generalised but your suggestion was working in my case. I'm Workington this area: <a href="https://www.openstreetmap.org/way/404140219">https://www.openstreetmap.org/way/404140219</a></p>
<p>Best,,,</p>
</div>
<div id="comment-80643-info" class="comment-info">
<span class="comment-age">(21 Jun '21, 10:30)</span> <span class="comment-user userinfo">Ahmad Ataei</span>
</div>
</div>
</div>
<div id="comment-tools-80599" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80599-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

