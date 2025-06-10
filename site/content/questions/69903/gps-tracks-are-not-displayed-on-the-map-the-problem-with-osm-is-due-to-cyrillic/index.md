+++
type = "question"
title = "GPS tracks are not displayed on the map, the problem with OSM is due to &quot;Cyrillic&quot;"
description = '''Problem number 1. If I load a gps-track (web browser), add it to Cyrillic (Russian), then the track after loading will not be displayed among the tracks on the OSM map layer. The problem is solved by changing the description from Cyrillic to Latin. But many know about it? (foreigners, please do not ...'''
date = "2019-07-06T09:37:00Z"
lastmod = "2019-07-13T10:06:00Z"
weight = 69903
keywords = [ "track", "bug" ]
aliases = [ "/questions/69903" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [GPS tracks are not displayed on the map, the problem with OSM is due to "Cyrillic"](/questions/69903/gps-tracks-are-not-displayed-on-the-map-the-problem-with-osm-is-due-to-cyrillic)

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
<span id="post-69903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69903-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Problem number 1</strong>. If I load a gps-track (web browser), add it to Cyrillic (Russian), then the track after loading will not be displayed among the tracks on the OSM map layer. The problem is solved by changing the description from <strong>Cyrillic</strong> to Latin. But many know about it? (foreigners, please do not write that en-international language is just your imagination).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jul '19, 09:37</strong></p>
<img src="https://secure.gravatar.com/avatar/2584287b803ca2fea70787a71ca8f88f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pangimun&#39;s gravatar image" />
<p><span>pangimun</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pangimun has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jul '19, 09:56</strong> </span></p>
</div>
</div>
<div id="comments-container-69903" class="comments-container">
<span id="69924"></span>
<div id="comment-69924" class="comment">
<div id="post-69924-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suspect this is something that has to be tackled by the website admins. Can you please report the issue on <a href="https://github.com/openstreetmap/openstreetmap-website/issues">the project's github page</a>.</p>
</div>
<div id="comment-69924-info" class="comment-info">
<span class="comment-age">(08 Jul '19, 07:43)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-69903" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69903-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="69927"></span>

<div id="answer-container-69927" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69927-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Problem solved. If someone will seek a solution ...</p>
<p>1) Cyrillic "does <strong>not kill</strong> the track" after it is downloaded to the server. 2) After successful processing of the track, the track is not immediately displayed on the map, but only at a scale of <strong>30m height.</strong> 3) The browser's cache hinders, instead of loading the track display, the "<strong>old maps</strong>" are shown (Chrome). 4) The track when loading must have the parameters <strong>"not anonymous"</strong></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '19, 12:16</strong></p>
<img src="https://secure.gravatar.com/avatar/2584287b803ca2fea70787a71ca8f88f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pangimun&#39;s gravatar image" />
<p><span>pangimun</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pangimun has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69927" class="comments-container">
&#10;</div>
<div id="comment-tools-69927" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69927-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70025"></span>

<div id="answer-container-70025" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70025-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Такой вопрос. Загрузил трек, отрисовал по нему дорогу. Настроил доступ всем.</p>
<p>При масштабе 300м дороги не видно: <a href="https://yadi.sk/i/U07s1SGmfC7ZQQ">https://yadi.sk/i/U07s1SGmfC7ZQQ</a></p>
<p>При масштабе 100м она появляется частично: <a href="https://yadi.sk/i/ppK_YRLId7tmkg">https://yadi.sk/i/ppK_YRLId7tmkg</a></p>
<p>И только при масштабе 50м она видна полностью: <a href="https://yadi.sk/i/6tEWlRlcciCHjA">https://yadi.sk/i/6tEWlRlcciCHjA</a></p>
<p>Почему так, почему моя дорога не вида как все остальные ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '19, 08:04</strong></p>
<img src="https://secure.gravatar.com/avatar/bf9fffeea0cb70ef4aacd557733f269d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dmitriy_S23&#39;s gravatar image" />
<p><span>Dmitriy_S23</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dmitriy_S23 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70025" class="comments-container">
<span id="70026"></span>
<div id="comment-70026" class="comment">
<div id="post-70026-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ждите.Трек отобразиться на карте полностью лишь ~через сутки (обработка отображения занимает время без какого-либо уведомления).</p>
</div>
<div id="comment-70026-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 08:08)</span> <span class="comment-user userinfo">pangimun</span>
</div>
</div>
</div>
<div id="comment-tools-70025" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70025-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70032"></span>

<div id="answer-container-70032" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70032-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Еще тогда прошу подсказать по следующему вопросу:</p>
<p>Нанес точку (водяная скважина): <a href="https://yadi.sk/i/vBQhDPDH9mNMIQ">https://yadi.sk/i/vBQhDPDH9mNMIQ</a></p>
<p>На карте её вообще не видно, никак: <a href="https://yadi.sk/i/ZiltOXtgRXu7Fg">https://yadi.sk/i/ZiltOXtgRXu7Fg</a></p>
<p>Вносил вчера</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '19, 09:52</strong></p>
<img src="https://secure.gravatar.com/avatar/bf9fffeea0cb70ef4aacd557733f269d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dmitriy_S23&#39;s gravatar image" />
<p><span>Dmitriy_S23</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dmitriy_S23 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '19, 09:53</strong> </span></p>
</div>
</div>
<div id="comments-container-70032" class="comments-container">
<span id="70034"></span>
<div id="comment-70034" class="comment">
<div id="post-70034-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Это не для обсуждения в этой ветке.</p>
<p>Посмотрите вашу точку слой "гумманитарный" Отображение зависит от расставляемых тегов, изучите тему.</p>
</div>
<div id="comment-70034-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 10:06)</span> <span class="comment-user userinfo">pangimun</span>
</div>
</div>
</div>
<div id="comment-tools-70032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70032-form-container" class="comment-form-container">
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

