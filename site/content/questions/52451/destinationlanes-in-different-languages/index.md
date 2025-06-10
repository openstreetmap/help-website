+++
type = "question"
title = "destination:lanes in different languages"
description = '''Instead of  destination:lanes=Brussels;Bruxelles|none|...  is it possible (and better) to use destination:lanes:lang:en=Brussels|none|...  and destination:lanes:lang:fr=Bruxelles|none|...  Edit: Destination sign is bilingual - local language and transcription similar to English on the same way?'''
date = "2016-10-10T18:06:00Z"
lastmod = "2016-10-10T18:31:00Z"
weight = 52451
keywords = [ "destination", "lanes", "language" ]
aliases = [ "/questions/52451" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [destination:lanes in different languages](/questions/52451/destinationlanes-in-different-languages)

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
<span id="post-52451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52451-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Instead of</p>
<pre><code>destination:lanes=Brussels;Bruxelles|none|...</code></pre>
<p>is it possible (and better) to use</p>
<pre><code>destination:lanes:lang:en=Brussels|none|...</code></pre>
<p>and</p>
<pre><code>destination:lanes:lang:fr=Bruxelles|none|...</code></pre>
<p>Edit: Destination sign is bilingual - local language and transcription similar to English</p>
<p>on the same way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Oct '16, 18:06</strong></p>
<img src="https://secure.gravatar.com/avatar/d1495190e346c0c530fd7205883b55c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Plamen&#39;s gravatar image" />
<p><span>Plamen</span><br />
<span class="score" title="151 reputation points">151</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Plamen has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '16, 19:13</strong> </span></p>
</div>
</div>
<div id="comments-container-52451" class="comments-container">
&#10;</div>
<div id="comment-tools-52451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52451-form-container" class="comment-form-container">
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

<span id="52452"></span>

<div id="answer-container-52452" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52452-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Plamen has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Taking a <a href="http://taginfo.openstreetmap.org/search?q=%3Afr">quick look at taginfo</a> I don't thing the "lang" part is needed. So I'd do something like</p>
<pre><code>destination:lanes:fr=Bruxelles|none|...
destination:lanes:en=Brussels|none|...</code></pre>
<p>But I believe that the destination:lanes tag should reflect what is on any destination sign, so you would only use the language specific tagging if the sign is multilingual.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '16, 18:31</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-52452" class="comments-container">
&#10;</div>
<div id="comment-tools-52452" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52452-form-container" class="comment-form-container">
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

