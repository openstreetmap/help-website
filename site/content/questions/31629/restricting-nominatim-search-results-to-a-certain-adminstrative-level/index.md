+++
type = "question"
title = "Restricting nominatim search results to a certain adminstrative &quot;level&quot;"
description = '''Is it possible to restrict a query result with nominatim to say &quot;countries, counties and towns&quot;? I am not too interested in the roads or streets for example, rather the high level adminsitrative regions.'''
date = "2014-03-17T21:42:00Z"
lastmod = "2014-03-18T13:38:00Z"
weight = 31629
keywords = [ "nominatim" ]
aliases = [ "/questions/31629" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Restricting nominatim search results to a certain adminstrative "level"](/questions/31629/restricting-nominatim-search-results-to-a-certain-adminstrative-level)

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
<span id="post-31629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31629-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to restrict a query result with nominatim to say "countries, counties and towns"? I am not too interested in the roads or streets for example, rather the high level adminsitrative regions.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Mar '14, 21:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ee9b01cfe7104e9236bfbec854a5a5db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leforthomas&#39;s gravatar image" />
<p><span>leforthomas</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leforthomas has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31629" class="comments-container">
&#10;</div>
<div id="comment-tools-31629" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31629-form-container" class="comment-form-container">
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

<span id="31654"></span>

<div id="answer-container-31654" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31654-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-31654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="leforthomas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a currently undocumented parameter <code>featuretype</code> that might be useful for you. Adding a parameter <code>featuretype=settlement</code> to the query, e.g. <a href="http://nominatim.osm.org/search?q=paris&amp;featuretype=settlement">like this</a>, restricts the results to objects below country level and above street level. That means that results will include states, counties, cities and villages and also natural features like national parks and rivers, but they do not contain countries, streets or POIs.</p>
<p>Other possible values for <code>featuretype</code> are: <code>country</code>, <code>state</code>, <code>city</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '14, 12:40</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-31654" class="comments-container">
<span id="31656"></span>
<div id="comment-31656" class="comment">
<div id="post-31656-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>that sounds pretty much like what I need. Is it possible to include countries as well? eg can I do featuretype=settlement,country? (seems to work)</p>
</div>
<div id="comment-31656-info" class="comment-info">
<span class="comment-age">(18 Mar '14, 13:13)</span> <span class="comment-user userinfo">leforthomas</span>
</div>
</div>
<span id="31661"></span>
<div id="comment-31661" class="comment">
<div id="post-31661-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Multiple values are not supported, so including countries does not work. featuretype=settlement,country just works like you have not given any parameter at all.</p>
</div>
<div id="comment-31661-info" class="comment-info">
<span class="comment-age">(18 Mar '14, 13:38)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-31654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31654-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31630"></span>

<div id="answer-container-31630" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31630-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If I enter this "fish and chips huntingdon" that works and gives the three shops mapped in my town, is that to sort of restriction you wanted?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '14, 22:14</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-31630" class="comments-container">
<span id="31631"></span>
<div id="comment-31631" class="comment">
<div id="post-31631-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No. What I want is to type 'Paris' and only get the countries, counties or towns called Paris, but none of the streets or airpots (or fish and ship shops) that have Paris in their names.</p>
</div>
<div id="comment-31631-info" class="comment-info">
<span class="comment-age">(17 Mar '14, 22:17)</span> <span class="comment-user userinfo">leforthomas</span>
</div>
</div>
<span id="31649"></span>
<div id="comment-31649" class="comment">
<div id="post-31649-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Using my a Win7 PC "paris" search yields <span>this (screenshot)</span>.</p>
</div>
<div id="comment-31649-info" class="comment-info">
<span class="comment-age">(18 Mar '14, 09:08)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="31650"></span>
<div id="comment-31650" class="comment">
<div id="post-31650-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, look down in your list and you will find "Bus stop, Paris...". What I am asking is whether or not there is a way with the API to filter out these type of results (bus stops, etc...).</p>
</div>
<div id="comment-31650-info" class="comment-info">
<span class="comment-age">(18 Mar '14, 09:14)</span> <span class="comment-user userinfo">leforthomas</span>
</div>
</div>
</div>
<div id="comment-tools-31630" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31630-form-container" class="comment-form-container">
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

