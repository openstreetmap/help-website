+++
type = "question"
title = "Why I receive Error 403 from API?"
description = '''Good morning.  I am a beginner of p.s.m. Firts I tried the following from the browser, and it worked and it still works: https://nominatim.openstreetmap.org/search?street=via+tolmezzo+15&amp;amp;postcode=20132&amp;amp;city=milano&amp;amp;county=MI&amp;amp;country_code=IT&amp;amp;format=json Then I tried with php, with ...'''
date = "2022-01-08T20:19:00Z"
lastmod = "2024-01-18T09:17:00Z"
weight = 83008
keywords = [ "nominatim", "browser", "server", "403", "error" ]
aliases = [ "/questions/83008" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why I receive Error 403 from API?](/questions/83008/why-i-receive-error-403-from-api)

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
<span id="post-83008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83008-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good morning. I am a beginner of p.s.m. Firts I tried the following from the browser, and it worked and it still works: <a href="https://nominatim.openstreetmap.org/search?street=via+tolmezzo+15&amp;postcode=20132&amp;city=milano&amp;county=MI&amp;country_code=IT&amp;format=json">https://nominatim.openstreetmap.org/search?street=via+tolmezzo+15&amp;postcode=20132&amp;city=milano&amp;county=MI&amp;country_code=IT&amp;format=json</a></p>
<p>Then I tried with php, with the following instructions, both from my pc that from a server, but it always return an Error 403. I read that this happens when there is an abuse, but it happened me from the very first submissmion. Thank you.</p>
<p>$data = array( 'street' =&gt; "via tolmezzo 15", 'postcode' =&gt; "20132", 'city' =&gt; "Milano", 'county' =&gt; "MI",<br />
'country_code' =&gt; "IT", 'format' =&gt; "json" ); $options = array ( 'http' =&gt; array ( 'header' =&gt; "Content-type: application/x-www-form-urlencoded\r\n", 'method' =&gt; 'GET', 'content' =&gt; http_build_query($data) ) ); $url="https://nominatim.openstreetmap.org/search"; $context = stream_context_create ($options); $result = file_get_contents ($url, false, $context);</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-browser" rel="tag" title="see questions tagged &#39;browser&#39;">browser</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-403" rel="tag" title="see questions tagged &#39;403&#39;">403</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '22, 20:19</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffad1b43f54e31b3ed388c9c078f610?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="enzovisk&#39;s gravatar image" />
<p><span>enzovisk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="enzovisk has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-83008" class="comments-container">
&#10;</div>
<div id="comment-tools-83008" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83008-form-container" class="comment-form-container">
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

<span id="83009"></span>

<div id="answer-container-83009" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83009-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-83009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are not following the Nominatim Usage policy, see here: <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a></p>
<p>You'll have to be esp. careful about including a unique user agent for your application ;)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '22, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '22, 10:12</strong> </span></p>
</div>
</div>
<div id="comments-container-83009" class="comments-container">
<span id="83014"></span>
<div id="comment-83014" class="comment">
<div id="post-83014-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your kind answer. I have read and I followed all these guidelines. It send me such response "error 43" since the first attempt, but all is right.</p>
<p>Afterwards,I tried from different servers and different connections. I also tried with curl. But It always gives me that answer.</p>
<p>Best regards. Vincent</p>
</div>
<div id="comment-83014-info" class="comment-info">
<span class="comment-age">(09 Jan '22, 09:57)</span> <span class="comment-user userinfo">enzovisk</span>
</div>
</div>
<span id="83016"></span>
<div id="comment-83016" class="comment">
<div id="post-83016-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, you did not follow the instructions as laid out by the usage policy. I've added another hint in my answer above.</p>
</div>
<div id="comment-83016-info" class="comment-info">
<span class="comment-age">(09 Jan '22, 10:13)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-83009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83009-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88166"></span>

<div id="answer-container-88166" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88166-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>you should use an UserAgent var httpClient = new HttpClient(); httpClient.DefaultRequestHeaders.UserAgent.ParseAdd("Mozilla/5.0 (compatible; AcmeInc/1.0)")</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '24, 09:17</strong></p>
<img src="https://secure.gravatar.com/avatar/faaba188ccb5db7c8f7766a3e3b70c82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nawar327&#39;s gravatar image" />
<p><span>Nawar327</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nawar327 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88166" class="comments-container">
&#10;</div>
<div id="comment-tools-88166" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88166-form-container" class="comment-form-container">
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

