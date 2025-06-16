+++
type = "question"
title = "Erreur 405 - Requête POST"
description = '''Bonjour, Nous avons une erreur 405 lors d&#x27;une requête POST vers l&#x27;API OpenStreetMap à l&#x27;aide de l&#x27;URL : &#x27;http://nominatim.openstreetmap.org/search?q=CODE POSTAL&amp;amp;format=json&amp;amp;polygon=0&amp;amp;addressdetails=1&#x27;. L&#x27;appel a toujours fonctionné sauf depuis le 31/07 à partir de 12h~12h30 où son foncti...'''
date = "2023-08-02T15:35:00Z"
lastmod = "2023-08-04T10:47:00Z"
weight = 87590
keywords = [ "http_status_code_405" ]
aliases = [ "/questions/87590" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Erreur 405 - Requête POST](/questions/87590/erreur-405-requete-post)

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
<span id="post-87590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87590-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Bonjour,</p>
<p>Nous avons une erreur 405 lors d'une requête POST vers l'API OpenStreetMap à l'aide de l'URL : 'http://nominatim.openstreetmap.org/search?q=<strong>CODE POSTAL</strong>&amp;format=json&amp;polygon=0&amp;addressdetails=1'.</p>
<p>L'appel a toujours fonctionné sauf depuis le 31/07 à partir de 12h~12h30 où son fonctionnement alterne entre KO et OK. Sauriez-vous d'où cela peut venir ? Merci :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-http_status_code_405" rel="tag" title="see questions tagged &#39;http_status_code_405&#39;">http_status_code_405</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '23, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/1aac18a64e06a73949d89486090b3581?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sylvain_1633&#39;s gravatar image" />
<p><span>Sylvain_1633</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sylvain_1633 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87590" class="comments-container">
&#10;</div>
<div id="comment-tools-87590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87590-form-container" class="comment-form-container">
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

<span id="87597"></span>

<div id="answer-container-87597" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87597-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-87597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should be sending a GET request.</p>
<p>Sending a POST request was never documented and only worked incidentally. The new frontend implementation is more strict and will not allow POST anymore.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '23, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-87597" class="comments-container">
<span id="87603"></span>
<div id="comment-87603" class="comment">
<div id="post-87603-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot ! It works now !</p>
</div>
<div id="comment-87603-info" class="comment-info">
<span class="comment-age">(04 Aug '23, 10:47)</span> <span class="comment-user userinfo">Sylvain_1633</span>
</div>
</div>
</div>
<div id="comment-tools-87597" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87597-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87591"></span>

<div id="answer-container-87591" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87591-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <a href="/questions/87587/suddenly-throwing-cors-error-on-open-street-map-api-calls">https://help.openstreetmap.org/questions/87587/suddenly-throwing-cors-error-on-open-street-map-api-calls</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '23, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-87591" class="comments-container">
&#10;</div>
<div id="comment-tools-87591" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87591-form-container" class="comment-form-container">
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

