+++
type = "question"
title = "Nominatim wildcards*"
description = '''Hi, using the search box at the left side of the main http://www.openstreetmap.org site to check that I could find a building I named yesterday I found that I was unable to find it unless I entered the complete title. I named it &#x27;Sesame Lane Childcare Centre&#x27; and thought that searching for &#x27;sesame&#x27;o...'''
date = "2013-10-16T02:00:00Z"
lastmod = "2013-10-17T02:16:00Z"
weight = 27216
keywords = [ "nominatim" ]
aliases = [ "/questions/27216" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim wildcards\*](/questions/27216/nominatim-wildcards)

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
<span id="post-27216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27216-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, using the search box at the left side of the main <a href="http://www.openstreetmap.org">http://www.openstreetmap.org</a> site to check that I could find a building I named yesterday I found that I was unable to find it unless I entered the complete title.</p>
<p>I named it 'Sesame Lane Childcare Centre' and thought that searching for 'sesame'or 'sesame lane' would have found it. I would prefer to use the full title I chose instead of 'Sesame Lane'.</p>
<p>It does not seem to accept wildcards either. The '<a href="https://wiki.openstreetmap.org/wiki/Search">more examples</a>' link does not provide info on how to make such a search effective.</p>
<p>Is this search box very limited in it's capacity in this regard or is there something I've missed?</p>
<p>edit: Sesame Lane is the name of the childcare group. It is not a type of way.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '13, 02:00</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Oct '13, 03:56</strong> </span></p>
</div>
</div>
<div id="comments-container-27216" class="comments-container">
&#10;</div>
<div id="comment-tools-27216" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27216-form-container" class="comment-form-container">
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

<span id="27223"></span>

<div id="answer-container-27223" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27223-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-27223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as I know Nominatim does not do partial or wildcard searches.</p>
<p>Technically I am sure it is feasible, although there may be some issues with parsing given that Nominatim is designed to work across multiple languages.</p>
<p>I suspect that such a feature has not been implemetned for two good reasons:</p>
<ul>
<li>Developer time &amp; resources. Nominatim is developed by a small pool of people who undoubtedly have along list of things to sort out. Most of these things will be with what might be considered to be core functionality. Partial search is probably not in this core. Certainly fuzzy matching is not.</li>
<li>Performance. Partial and wildcard searches are likely to impose an unsupportable load on the Nominatim server. Only some queries would be supported by indexes with the very real risk that a single query could deny the service to everyone else through requiring table scans of the base data.</li>
</ul>
<p>In general I find the type of query you need to be met by the Nominatim using something like the following:<br />
`</p>
<pre><code>&lt; amenity &gt; near &lt; town|place &gt;</code></pre>
<p>`</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '13, 11:20</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span> </br></p>
</div>
</div>
<div id="comments-container-27223" class="comments-container">
&#10;</div>
<div id="comment-tools-27223" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27223-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27231"></span>

<div id="answer-container-27231" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27231-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-27231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim has very limited partial search support. You'll find that searching for <a href="http://nominatim.openstreetmap.org/search.php?q=Sesame%2C+north+lakes">Sesame, North Lakes</a> actually returns the expected object. (There are simply too many places named <code>Sesame</code> on this planet for an unrestricted search to work out.)</p>
<p>Searching for <code>Sesame Lane</code>, you will run into <a href="https://trac.openstreetmap.org/ticket/4971">this bug</a>. Once the bug is fixed you should get results for it, too, but don't expect miracles. SK53's answer as to why partial search works badly is spot-on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '13, 15:12</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-27231" class="comments-container">
<span id="27252"></span>
<div id="comment-27252" class="comment">
<div id="post-27252-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for those 2 informative and helpful replies.</p>
</div>
<div id="comment-27252-info" class="comment-info">
<span class="comment-age">(17 Oct '13, 02:16)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-27231" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27231-form-container" class="comment-form-container">
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

