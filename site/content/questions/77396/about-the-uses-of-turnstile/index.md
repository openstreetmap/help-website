+++
type = "question"
title = "About the uses of Turnstile"
description = '''Hello!, I´m new to OSM and I´d like to know more about the allowed uses for the Turnstile Node. The Wiki page for Turnstile says that it is &quot;Also used for tagging some doors/gates/barriers where you validate your ticket, see Tag:railway=subway_entrance. &quot; So my questions are the following: 1- When i...'''
date = "2020-11-04T13:29:00Z"
lastmod = "2020-11-04T16:30:00Z"
weight = 77396
keywords = [ "turnstile", "airport" ]
aliases = [ "/questions/77396" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [About the uses of Turnstile](/questions/77396/about-the-uses-of-turnstile)

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
<span id="post-77396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77396-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello!, I´m new to OSM and I´d like to know more about the allowed uses for the Turnstile Node.</p>
<p>The Wiki page for <a href="https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dturnstile">Turnstile</a> says that it is "Also used for tagging some doors/gates/barriers where you validate your ticket, see Tag:railway=subway_entrance. "</p>
<p>So my questions are the following:</p>
<p>1- When it comes to adding the Turnstile node to a subway station, should I do it to the footpath way between the subway entrance and the subway plataform?</p>
<p>2- Can I use the Turnstile Node to mark a Boarding Pass Scanner Gate? A Boarding Pass Scanner Gate requires a passenger to have his air ticket scanned in order to allow this person to gain accese to the boarding area at an airport, as shown and described in <a href="https://www.thebridgechronicle.com/pune/aai-installs-boarding-pass-scanner-departure-area-12154">this News Article</a>. I believe this use is very simillar to the use described in the wiki quote above.</p>
<p>3- If the answer to question 2 is a yes, then can I use the same node to mark <a href="https://en.wikipedia.org/wiki/EGate_(Italy)">Egates</a> (Automatic Passport Check). One of the main differences from Egate to Boarding Pass Scanner Gate is the the former requires a picture of the person using it to be taken.</p>
<p>4- Can I use the Turnstile Node to mark the equipment at the entrance of some clubs, gyms, or commercial buildings where one has to scan a card, credential or fingerprint in order to gain acces to the facilities?</p>
<p>Sorry for all the questions, I Could not find answers anywhere and as a newbie here I want to be as within the rules as possible when it comes to tagging.</p>
<p>Thanks for any help, much appreciated</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-turnstile" rel="tag" title="see questions tagged &#39;turnstile&#39;">turnstile</span> <span class="post-tag tag-link-airport" rel="tag" title="see questions tagged &#39;airport&#39;">airport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Nov '20, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/1f86ebe2a7b0ff4ed23a37e7d61347a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="danireload&#39;s gravatar image" />
<p><span>danireload</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="danireload has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77396" class="comments-container">
&#10;</div>
<div id="comment-tools-77396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77396-form-container" class="comment-form-container">
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

<span id="77397"></span>

<div id="answer-container-77397" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77397-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The important bit with gates is that it is mapped correctly on the path it is blocking. So yes, you should put the turnstile on footpath way between the subway entrance and the subway platform. The second important point is that you explicitly tag the <a href="http://wiki.openstreetmap.org/wiki/Key:access">access rights</a> if they deviate from the standards that are listed in the respective wiki pages or if you want to make sure the access is correctly recognized by data consumers. Then you can add additional characteristics like <code>fee=*</code> or add a <code>description</code>.</p>
<p>The type of barrier is important if you don't explicitly tag access tags. Otherwise it does not matter that much to tag exactly what is on the ground and you could use turnstile for some of the uses you described above. There are other types of barriers commonly used, though, that might fit better to your physical objects. You may tag them even if the wiki does not mention the explicit uses you have in mind. Amongst those other barriers are <a href="https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dsliding_gate"><code>sliding_gate</code></a>, <a href="https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dfull-height_turnstile"><code>full-height_turnstile</code></a> or just <a href="https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dgate"><code>gate</code></a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '20, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-77397" class="comments-container">
&#10;</div>
<div id="comment-tools-77397" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77397-form-container" class="comment-form-container">
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

