+++
type = "question"
title = "country code in q= or in countryCodes="
description = '''For geocoding, to search for the Mainstreet 12, Amsterdam, Netherlands, (doesn&#x27;t exist) we can call either http://nominatim.openstreetmap.org/search?q=12,Mainstreet,Amsterdam,NL&amp;amp;format=xml  or http://nominatim.openstreetmap.org/search?q=12,Mainstreet,Amsterdam&amp;amp;countryCodes=NL&amp;amp;format=xml ...'''
date = "2012-02-24T08:38:00Z"
lastmod = "2012-02-26T21:06:00Z"
weight = 10757
keywords = [ "nominatim", "geocoding" ]
aliases = [ "/questions/10757" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [country code in q= or in countryCodes=](/questions/10757/country-code-in-q-or-in-countrycodes)

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
<span id="post-10757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10757-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For geocoding, to search for the Mainstreet 12, Amsterdam, Netherlands, (doesn't exist) we can call either</p>
<pre><code>http://nominatim.openstreetmap.org/search?q=12,Mainstreet,Amsterdam,NL&amp;format=xml</code></pre>
<p>or</p>
<pre><code>http://nominatim.openstreetmap.org/search?q=12,Mainstreet,Amsterdam&amp;countryCodes=NL&amp;format=xml</code></pre>
<p>Which format is preferred? With country code appended in the q=, or with using countryCodes=</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '12, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/b98e1f9c0bc31e2a0059d90912e27154?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msol&#39;s gravatar image" />
<p><span>msol</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msol has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '12, 08:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span></p>
</div>
</div>
<div id="comments-container-10757" class="comments-container">
&#10;</div>
<div id="comment-tools-10757" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10757-form-container" class="comment-form-container">
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

<span id="10819"></span>

<div id="answer-container-10819" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10819-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a slight difference in how Nominatim handles these two queries. In the first query, it will check for all occurrences of 'NL' in the database, so in very rare cases you may end up with unexpected results. Given the second form with the countryCodes parameter, it restricts the search to places within the country right from the start.</p>
<p>So, both query forms are perfectly legitimate and give the same results in most cases. If you know you have search requests for a specific country, the second form might be more efficient. But if you are not sure, there is no need to parse and format the query. Just go with the first form then.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '12, 21:06</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-10819" class="comments-container">
&#10;</div>
<div id="comment-tools-10819" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10819-form-container" class="comment-form-container">
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

