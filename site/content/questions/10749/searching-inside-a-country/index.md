+++
type = "question"
title = "Searching inside a country"
description = '''The geocoder in our software suddenly stopped working and we have analyzed this to the following cause: To search for the Mainstreet 12, Amsterdam, Netherlands, (doesn&#x27;t exist) we used the following call: http://nominatim.openstreetmap.org/search?q=12,Mainstreet,Amsterdam,NL&amp;amp;format=xml  This for...'''
date = "2012-02-23T13:37:00Z"
lastmod = "2012-02-23T14:32:00Z"
weight = 10749
keywords = [ "country", "code", "geocoding", "trac", "nominatim" ]
aliases = [ "/questions/10749" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Searching inside a country](/questions/10749/searching-inside-a-country)

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
<span id="post-10749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10749-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The geocoder in our software suddenly stopped working and we have analyzed this to the following cause: To search for the Mainstreet 12, Amsterdam, Netherlands, (doesn't exist) we used the following call:</p>
<pre><code>http://nominatim.openstreetmap.org/search?q=12,Mainstreet,Amsterdam,NL&amp;format=xml</code></pre>
<p>This format used to work but no longer returns results. I noticed that it does work with the full country name appended to the address</p>
<pre><code>http://nominatim.openstreetmap.org/search?q=12,Mainstreet,Amsterdam,Nederland&amp;format=xml</code></pre>
<p>but we don't have the country name available in our software. So, now I plan to change our code to</p>
<pre><code>http://nominatim.openstreetmap.org/search?q=12,Mainstreet,Amsterdam&amp;countryCodes=NL&amp;format=xml</code></pre>
<p>Since that is in line with the wiki description.</p>
<p>My main questions are. Did the API indeed change? How could I have known this upfront, so where should I register to be warned for such changes before they become effective?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-code" rel="tag" title="see questions tagged &#39;code&#39;">code</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-trac" rel="tag" title="see questions tagged &#39;trac&#39;">trac</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Feb '12, 13:37</strong></p>
<img src="https://secure.gravatar.com/avatar/b98e1f9c0bc31e2a0059d90912e27154?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msol&#39;s gravatar image" />
<p><span>msol</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msol has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '12, 08:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span></p>
</div>
</div>
<div id="comments-container-10749" class="comments-container">
&#10;</div>
<div id="comment-tools-10749" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10749-form-container" class="comment-form-container">
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

<span id="10753"></span>

<div id="answer-container-10753" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10753-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please open a ticket in the nominatim trac:</p>
<p><a href="http://trac.openstreetmap.org/newticket?component=nominatim">http://trac.openstreetmap.org/newticket?component=nominatim</a></p>
<p>Thank you</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '12, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-10753" class="comments-container">
&#10;</div>
<div id="comment-tools-10753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10753-form-container" class="comment-form-container">
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

