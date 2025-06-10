+++
type = "question"
title = "Que sistema de referencias de coordenadas de bo usar?"
description = '''Holaaa, saludos desde Costa Rica. Que sistema de coordenadas debo usar en QGIS en lugar de Google Mercator? Muchas gracias a todos!'''
date = "2014-05-10T19:47:00Z"
lastmod = "2014-05-15T23:16:00Z"
weight = 33066
keywords = [ "qgis", "google", "lang-es", "mercator" ]
aliases = [ "/questions/33066" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Que sistema de referencias de coordenadas de bo usar?](/questions/33066/que-sistema-de-referencias-de-coordenadas-de-bo-usar)

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
<span id="post-33066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33066-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Holaaa, saludos desde Costa Rica. Que sistema de coordenadas debo usar en QGIS en lugar de Google Mercator?</p>
<p>Muchas gracias a todos!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-google" rel="tag" title="see questions tagged &#39;google&#39;">google</span> <span class="post-tag tag-link-lang-es" rel="tag" title="see questions tagged &#39;lang-es&#39;">lang-es</span> <span class="post-tag tag-link-mercator" rel="tag" title="see questions tagged &#39;mercator&#39;">mercator</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 May '14, 19:47</strong></p>
<img src="https://secure.gravatar.com/avatar/9bb44954675db1e26786d2da5b71f6a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jerry%20Alonso&#39;s gravatar image" />
<p><span>Jerry Alonso</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jerry Alonso has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 May '14, 21:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-33066" class="comments-container">
<span id="33067"></span>
<div id="comment-33067" class="comment">
<div id="post-33067-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>just for info, for those who do not know the program: the question seems to be about <span>QGIS</span>.</p>
</div>
<div id="comment-33067-info" class="comment-info">
<span class="comment-age">(10 May '14, 21:24)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33066-form-container" class="comment-form-container">
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

<span id="33073"></span>

<div id="answer-container-33073" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33073-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33073-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33073-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Oi! If you add a WGS-84 dataset, you should specify this source also as WGS-84(EPSG:4326). Then if you want do add an rendered OSM Online-Map as baselayer (via TMS or WMS layer), you can try to pick already Google Pseudeo Mercator (EPSG:3857) if supported, or also WGS-84.</p>
<p>Then most important step: You enable <strong>'On the fly CRS transformation'</strong> in your project properties (e.g. by picking the globe button at the right side of the status bar in the QGIS window). There you set the project CRS to Google Mercator. E voila, the basemap looks right again :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '14, 08:47</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-33073" class="comments-container">
<span id="33213"></span>
<div id="comment-33213" class="comment">
<div id="post-33213-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Muchisimas Gracias! Thanks very much!</p>
</div>
<div id="comment-33213-info" class="comment-info">
<span class="comment-age">(15 May '14, 23:16)</span> <span class="comment-user userinfo">Jerry Alonso</span>
</div>
</div>
</div>
<div id="comment-tools-33073" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33073-form-container" class="comment-form-container">
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

