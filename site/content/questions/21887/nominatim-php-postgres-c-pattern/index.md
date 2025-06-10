+++
type = "question"
title = "Nominatim: PHP - Postgres - C pattern"
description = '''Hi, as there&#x27;s no documentation on Nominatim&#x27;s search.php, I&#x27;m trying to make sense of the code myself. I noticed that for tokenizing search queries PHP code invokes a stored procedure in Postgresql, which in turn invokes a Nominatim custom module compiled from C code. Coming from the Java world I a...'''
date = "2013-04-26T15:14:00Z"
lastmod = "2013-04-26T16:18:00Z"
weight = 21887
keywords = [ "implementation", "c", "nominatim", "postgresql", "php" ]
aliases = [ "/questions/21887" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim: PHP - Postgres - C pattern](/questions/21887/nominatim-php-postgres-c-pattern)

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
<span id="post-21887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21887-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>as there's no documentation on Nominatim's search.php, I'm trying to make sense of the code myself. I noticed that for tokenizing search queries PHP code invokes a stored procedure in Postgresql, which in turn invokes a Nominatim custom module compiled from C code. Coming from the Java world I am wondering:</p>
<p>Is that a common LAPP-pattern?</p>
<p>I understand that string-crunching is faster in C than in an interpreted language, still many things happen in PHP in the Nominatim implementation. What's the reason for invoking such a tool-chain? Google didn't help me finding an explanation for that so I thought I'd just ask.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-implementation" rel="tag" title="see questions tagged &#39;implementation&#39;">implementation</span> <span class="post-tag tag-link-c" rel="tag" title="see questions tagged &#39;c&#39;">c</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Apr '13, 15:14</strong></p>
<img src="https://secure.gravatar.com/avatar/680bc1d9127776b4acb2e6af485a6869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="konstantin&#39;s gravatar image" />
<p><span>konstantin</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="konstantin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21887" class="comments-container">
&#10;</div>
<div id="comment-tools-21887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21887-form-container" class="comment-form-container">
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

<span id="21892"></span>

<div id="answer-container-21892" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21892-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The string standardisation and tokenising are all also required during indexing of data and that is almost entirely done in plpgsql and c. For consistency the php search code then accesses those same functions.</p>
<p>So, the postgresql module acts as a common point between the indexing and search code.</p>
<p>The other reason is as you suggest - there is a significant speed gain from writing this frequent operation in c. During the search phase this speed is less important but during indexing it is essential.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '13, 16:05</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '13, 16:19</strong> </span></p>
</div>
</div>
<div id="comments-container-21892" class="comments-container">
&#10;</div>
<div id="comment-tools-21892" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21892-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21890"></span>

<div id="answer-container-21890" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21890-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I haven't looked at the nominatim code, but the pattern doesn't seem wrong to me :</p>
<p>While it may look like "just a string tokenizer", chances are that some complicated logic like word stemming is necessary. Two reasons for doing that inside the database come to mind: either we want to use the exact same algorithm as the database is using (so reusing code that's available in the db makes sense), or the process requires fectching data from the db (so going back and forth between php and postgres would kill performance).</p>
<p>The richness and ease of use of server-side languages and extenstion is actually one of postgresql's killer feature compared to other databases. It's a great tool that can make postgres look more like a software platform than an RDBMS. Learn to love it :)</p>
<p>Concerning the idea that string-crunching is better done in C than an interpreted language, it is generaly false. Interpreted languages are often <em>very</em> good at string-crunching, and beating that in C can take enormous effort. I doubt this is the reason for nominatim's pattern.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '13, 15:54</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-21890" class="comments-container">
<span id="21893"></span>
<div id="comment-21893" class="comment">
<div id="post-21893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Having looked at the code I assure you: There's nothing complicated in that c module invoked. Also no data is fetched from the DB itself.</p>
<p>Twain's explanation sounds reasonable to me: The same logic used at indexing time needs to be invoked during search. Thanks!</p>
</div>
<div id="comment-21893-info" class="comment-info">
<span class="comment-age">(26 Apr '13, 16:12)</span> <span class="comment-user userinfo">konstantin</span>
</div>
</div>
<span id="21894"></span>
<div id="comment-21894" class="comment">
<div id="post-21894-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>While you are entirely right about string handling and C vs interpreted in the general case in this particular case plpgsql string handling is particularly poor and the operations involved (character table lookups and reductions in simple ascii) are particularly well suited to c.</p>
</div>
<div id="comment-21894-info" class="comment-info">
<span class="comment-age">(26 Apr '13, 16:18)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
</div>
<div id="comment-tools-21890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21890-form-container" class="comment-form-container">
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

