+++
type = "question"
title = "Tagging single rentable cargo bikes"
description = '''The city of Vienna has a program that aims to provide cargo bikes for free use in as many areas of the city as possible. These are usually stationed at some shop, and as far as I have seen so far, there is only one available per location. I&#x27;m wondering how to tag these locations. I found service:bic...'''
date = "2020-12-03T12:09:00Z"
lastmod = "2020-12-03T13:17:00Z"
weight = 77840
keywords = [ "rental", "bike", "bicycle", "cargo" ]
aliases = [ "/questions/77840" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tagging single rentable cargo bikes](/questions/77840/tagging-single-rentable-cargo-bikes)

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
<span id="post-77840-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77840-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77840-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The city of Vienna has a <a href="https://www.graetzlrad.wien/">program</a> that aims to provide cargo bikes for free use in as many areas of the city as possible. These are usually stationed at some shop, and as far as I have seen so far, there is only one available per location.</p>
<p>I'm wondering how to tag these locations. I found <a href="https://wiki.openstreetmap.org/wiki/Key:service:bicycle:rental"><code>service:bicycle:rental=yes</code></a>, but I'm missing some bits and pieces:</p>
<ul>
<li>How do I mark that these are cargo bikes?</li>
</ul>
<p>edit: I saw on taginfo that tags like <code>service:bicycle:rental:mtb</code> are used sometimes, so I figure I could use <code>service:bicycle:rental:cargo=yes</code>?</p>
<p>edit2: or <code>service:bicycle:rental:type=cargo</code>, looks neater to me.</p>
<ul>
<li>That there is only one available at a location?</li>
<li>That they are part of the Grätzlrad program?</li>
</ul>
<p>edit: I found <code>service:bicycle:rental:operator</code>, so maybe <code>service:bicycle:rental:operator=Grätzlrad</code>?</p>
<ul>
<li>Each location has an info page (<a href="https://www.graetzlrad.wien/bike/das-wuk/">like this</a>) where the bike can be booked, too. Ideally I'd like to link to it.</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rental" rel="tag" title="see questions tagged &#39;rental&#39;">rental</span> <span class="post-tag tag-link-bike" rel="tag" title="see questions tagged &#39;bike&#39;">bike</span> <span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span> <span class="post-tag tag-link-cargo" rel="tag" title="see questions tagged &#39;cargo&#39;">cargo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '20, 12:09</strong></p>
<img src="https://secure.gravatar.com/avatar/e7687474f445a58615ccf4e3c4dc7265?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zoosh&#39;s gravatar image" />
<p><span>zoosh</span><br />
<span class="score" title="121 reputation points">121</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zoosh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Dec '20, 12:33</strong> </span></p>
</div>
</div>
<div id="comments-container-77840" class="comments-container">
&#10;</div>
<div id="comment-tools-77840" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77840-form-container" class="comment-form-container">
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

<span id="77841"></span>

<div id="answer-container-77841" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77841-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Based on what is described in the <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dbicycle_rental">wiki</a> I would suggest:</p>
<p><code>amenity=bicycle_rental</code><br />
<code>name=Wiener Börse</code><br />
<code>capacity=1</code><br />
<code>capacity:cargo_bike=1</code><br />
<code>network=Grätzlrad</code><br />
<code>operator=Die Wiener Börse</code><br />
<code>fee=no</code><br />
<code>website=</code><a href="https://www.graetzlrad.wien/bike/wiener-boerse/"><code>https://www.graetzlrad.wien/bike/wiener-boerse/</code></a></p>
<p>The <code>service</code> key should be used to qualify other objects (e.g. bicycle shops) that also rent bicycles. You could use that if you wanted to add the service to the operator (e.g. Wiener Börse) directly.</p>
<p>I also struggle a bit how to indicate that there is a cargo bike only. I would probably go for something like<br />
<code>bicycle_rental=cargo_bike</code><br />
added as a subkey of <code>amenity=bicycle_rental</code>. Deeper discussion on this topic should probably taken to the <em>Tagging</em> mailing list.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '20, 13:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Dec '20, 13:48</strong> </span></p>
</div>
</div>
<div id="comments-container-77841" class="comments-container">
&#10;</div>
<div id="comment-tools-77841" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77841-form-container" class="comment-form-container">
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

