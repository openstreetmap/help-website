+++
type = "question"
title = "JOSM Search function: Regex use and samples"
description = '''I need some info how to use &quot;regular expression&quot; here. JOSM site is lacking help on this topic. For example what to enter in the search box to look for names starting with a particular string.'''
date = "2015-12-01T08:51:00Z"
lastmod = "2015-12-01T13:25:00Z"
weight = 46917
keywords = [ "regex", "josm", "search" ]
aliases = [ "/questions/46917" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM Search function: Regex use and samples](/questions/46917/josm-search-function-regex-use-and-samples)

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
<span id="post-46917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46917-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need some info how to use "regular expression" here. JOSM site is lacking help on this topic. For example what to enter in the search box to look for names starting with a particular string.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-regex" rel="tag" title="see questions tagged &#39;regex&#39;">regex</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '15, 08:51</strong></p>
<img src="https://secure.gravatar.com/avatar/d1495190e346c0c530fd7205883b55c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Plamen&#39;s gravatar image" />
<p><span>Plamen</span><br />
<span class="score" title="151 reputation points">151</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Plamen has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Dec '15, 10:43</strong> </span></p>
</div>
</div>
<div id="comments-container-46917" class="comments-container">
&#10;</div>
<div id="comment-tools-46917" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46917-form-container" class="comment-form-container">
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

<span id="46919"></span>

<div id="answer-container-46919" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46919-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-46919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Plamen has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, you have to enable <a href="https://josm.openstreetmap.de/wiki/Help/ExpertMode">expert mode</a>. Then just open the <a href="https://josm.openstreetmap.de/wiki/Help/Action/Search">search tool</a> and enable <em>regular expression</em>. Now you can enter regular expressions enclosed in quotes, like "^Park" for selecting any "Park Avenue", "Park Lane" and so on. According to <a href="https://josm.openstreetmap.de/wiki/Help/Action/Search#Seealso">this page</a> JOSM uses <a href="http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html">Java Regex</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '15, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Dec '15, 12:14</strong> </span></p>
</div>
</div>
<div id="comments-container-46919" class="comments-container">
<span id="46920"></span>
<div id="comment-46920" class="comment">
<div id="post-46920-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, <code>name:"^Park"</code> is OK, but also return <code>name:en=Park</code> when <code>name=Something_else</code>. Is it possible <code>name:en:"^Park"</code>?</p>
</div>
<div id="comment-46920-info" class="comment-info">
<span class="comment-age">(01 Dec '15, 13:03)</span> <span class="comment-user userinfo">Plamen</span>
</div>
</div>
<span id="46921"></span>
<div id="comment-46921" class="comment">
<div id="post-46921-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Oh, that's interesting. "name"="value" doesn't seem to work when using regular expressions for <em>value</em>. This could be a bug. However "^name$":"^Park" seems to perform an exact match and ignores keys with <em>name:en</em>, <em>disused:name</em> (bad example) and so on.</p>
</div>
<div id="comment-46921-info" class="comment-info">
<span class="comment-age">(01 Dec '15, 13:25)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46919-form-container" class="comment-form-container">
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

