+++
type = "question"
title = "How to write an overpass request to get all the ways without name:en tag in a country?"
description = '''Hello Everyone, I am trying to download all the trunks, motorways and primary ways that don&#x27;t have name:en tag in Iran. Can someone help me write a query that can download these data from OSM server? Thanks.'''
date = "2016-09-03T07:12:00Z"
lastmod = "2016-09-03T13:49:00Z"
weight = 51882
keywords = [ "overpass", "iran", "name", "query" ]
aliases = [ "/questions/51882" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to write an overpass request to get all the ways without name:en tag in a country?](/questions/51882/how-to-write-an-overpass-request-to-get-all-the-ways-without-nameen-tag-in-a-country)

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
<span id="post-51882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51882-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Everyone,</p>
<p>I am trying to download all the trunks, motorways and primary ways that don't have name:en tag in Iran. Can someone help me write a query that can download these data from OSM server?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-iran" rel="tag" title="see questions tagged &#39;iran&#39;">iran</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Sep '16, 07:12</strong></p>
<img src="https://secure.gravatar.com/avatar/f7da215f2999ecac8d169e32e2c3502e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adib%20Yz&#39;s gravatar image" />
<p><span>Adib Yz</span><br />
<span class="score" title="291 reputation points">291</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adib Yz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Sep '16, 14:33</strong> </span></p>
</div>
</div>
<div id="comments-container-51882" class="comments-container">
&#10;</div>
<div id="comment-tools-51882" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51882-form-container" class="comment-form-container">
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

<span id="51890"></span>

<div id="answer-container-51890" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51890-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Adib Yz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you need is the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Negation">Overpass-API Negation</a> operator.</p>
<p>Here is <a href="http://overpass-turbo.eu/s/iaR">an example</a> for trunk roads. BEWARE it returns a lot of data, so it may be better to run through Overpass rather than Overpass-Turbo, or change the area constraint to limit the query to individual provinces.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '16, 13:15</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-51890" class="comments-container">
<span id="51891"></span>
<div id="comment-51891" class="comment">
<div id="post-51891-score" class="comment-score">
6
</div>
<div class="comment-text">
<p>BTW: we've changed the negation in the most recent release 0.7.53 to make it a bit more user friendly:</p>
<p>Instead of <code>["name:en"!~"."]</code> you can now also write <code>[!"name:en"]</code></p>
<p>This will be available on overpass-api.de in the near future.</p>
</div>
<div id="comment-51891-info" class="comment-info">
<span class="comment-age">(03 Sep '16, 13:49)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-51890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51890-form-container" class="comment-form-container">
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

