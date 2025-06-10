+++
type = "question"
title = "Can I differentiate between no-data and no-results with the Overpass API?"
description = '''I&#x27;m using an API query to find out whether a small bounding box point contains:  - one way (a regular point on a road)  - no ways (e.g. the middle of a field, or a building)  - multiple ways (e.g. a bridge or a crossing) I&#x27;m using a self-hosting database, so I&#x27;ve only got the data I&#x27;ve loaded (e.g. ...'''
date = "2020-06-30T18:48:00Z"
lastmod = "2020-06-30T20:59:00Z"
weight = 75483
keywords = [ "self-hosted", "api", "data", "overpass-api", "overpass" ]
aliases = [ "/questions/75483" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Can I differentiate between no-data and no-results with the Overpass API?](/questions/75483/can-i-differentiate-between-no-data-and-no-results-with-the-overpass-api)

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
<span id="post-75483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75483-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using an API query to find out whether a small bounding box point contains: - one way (a regular point on a road) - no ways (e.g. the middle of a field, or a building) - multiple ways (e.g. a bridge or a crossing)</p>
<p>I'm using a self-hosting database, so I've only got the data I've loaded (e.g. not the entire world, just one city and eventually the country).</p>
<p>If I make a request such as this, which is a road under a bridge in London:</p>
<p>[out:json][timeout:10];(way(51.5994,-0.23376,51.5996,-0.23356)[!"landuse"];);out count;&gt;; <a href="https://overpass-turbo.eu/s/VCE">https://overpass-turbo.eu/s/VCE</a></p>
<p>(Note this query intentionally returns no nodes, but the counts of data found. Focus on elements.0.ways figure.)</p>
<p>but the data for London has not been loaded - it returns 0 ways.</p>
<p>Equally a query where there are actually no ways returns the same information: <a href="https://overpass-turbo.eu/">https://overpass-turbo.eu/</a></p>
<p>I get that it's difficult for a system to know <em>why</em> there are no results, but in the hope there's a way:</p>
<p>Is there a way to find out whether data for that region hasn't been loaded, or whether there's plenty of data nearby just not results for that in particular?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-self-hosted" rel="tag" title="see questions tagged &#39;self-hosted&#39;">self-hosted</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jun '20, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/ecd7f35230124b6353b01fbae53eaa4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Patabugen&#39;s gravatar image" />
<p><span>Patabugen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Patabugen has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jun '20, 18:48</strong> </span></p>
</div>
</div>
<div id="comments-container-75483" class="comments-container">
&#10;</div>
<div id="comment-tools-75483" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75483-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="75484"></span>

<div id="answer-container-75484" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75484-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unsure whether you're asking why "it returns 0 ways." as it does for me: <a href="https://overpass-turbo.eu/s/VCY">https://overpass-turbo.eu/s/VCY</a></p>
<p>out count; on its own will always display the 'This map intentionally left blank' message</p>
<p>or how you can test for an empty return set: (if:count(ways) == 0);</p>
<p>Which city have you got loaded in your self-hosting database,? Rome or London?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '20, 20:03</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jun '20, 20:13</strong> </span></p>
</div>
</div>
<div id="comments-container-75484" class="comments-container">
&#10;</div>
<div id="comment-tools-75484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75484-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75485"></span>

<div id="answer-container-75485" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75485-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm asking how I can test for an "empty return set" vs "server hasn't got data for that region".</p>
<p>I've got Greater London loaded.</p>
<p>Actually I thought I had London loaded until my queries all returned 0 ways, which lead me to see that I've not loaded it properly and so I want to protect against that in future.</p>
<p>The workaround I've implemented so far - which works for me - is that if the waypoint returns 0 ways I double check it against the demo serer. My waypoints are all tracking drivers driving cars down roads, so I should never have 0. By double checking against the demo server I can throw an error if my server and the demo server disagree.</p>
<p>But I'd like to do it all on my server if possible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '20, 20:28</strong></p>
<img src="https://secure.gravatar.com/avatar/ecd7f35230124b6353b01fbae53eaa4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Patabugen&#39;s gravatar image" />
<p><span>Patabugen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Patabugen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75485" class="comments-container">
&#10;</div>
<div id="comment-tools-75485" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75485-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75486"></span>

<div id="answer-container-75486" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75486-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"I'm asking how I can test for an "empty return set" vs "server hasn't got data for that region"."</p>
<p>I've reread your original post &amp; I'm at a loss how that was to be determined. Please be clearer when asking questions. This is a server side problem. Nothing to do with OP.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '20, 20:54</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-75486" class="comments-container">
&#10;</div>
<div id="comment-tools-75486" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75486-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75487"></span>

<div id="answer-container-75487" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75487-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I do apologise if my initial question wasn't clear enough.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '20, 20:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ecd7f35230124b6353b01fbae53eaa4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Patabugen&#39;s gravatar image" />
<p><span>Patabugen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Patabugen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75487" class="comments-container">
&#10;</div>
<div id="comment-tools-75487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75487-form-container" class="comment-form-container">
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

