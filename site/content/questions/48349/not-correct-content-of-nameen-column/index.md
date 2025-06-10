+++
type = "question"
title = "Not correct content of &#x27;name:en&#x27; column"
description = '''Hello everyone. I have installed my own osm tile server. I osmcarto style and mapnik for rendering tiles. Now I want to add English names to the city, that are not in English. For example: from Chineese to English and Chineese. I know, that I need to create &#x27;name:en&#x27; column to take english names fro...'''
date = "2016-02-25T10:40:00Z"
lastmod = "2016-02-25T11:44:00Z"
weight = 48349
keywords = [ "import", "multilingual", "carto", "osm2pgsql", "english" ]
aliases = [ "/questions/48349" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Not correct content of 'name:en' column](/questions/48349/not-correct-content-of-nameen-column)

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
<span id="post-48349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48349-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone.</p>
<p>I have installed my own osm tile server. I osmcarto style and mapnik for rendering tiles.</p>
<p>Now I want to add English names to the city, that are not in English. For example: from <a href="http://www.openstreetmap.org/#map=6/29.191/112.291" title="title">Chineese</a> to <a href="http://www.openstreetmap.org/#map=6/29.191/112.291&amp;layers=Q" title="title">English and Chineese</a>.</p>
<p>I know, that I need to create <strong>'name:en' column</strong> to take english names from there.</p>
<p>For import I use osm2psql tool and there command is:</p>
<pre><code>osm2pgsql -z &#39;name:en&#39; -c --slim -d gis -C 1600 --number-processes 2 /path/to/file.</code></pre>
<p>After import I have <em>""=&gt;"Saint Petersburg"</em> in <strong>'name:en' column</strong> instead of <em>Saint Petersburg</em>.</p>
<p>If I use <em>'-k'</em> key while importing, I will get <strong>tags column</strong> with the following content:</p>
<p><em>"ref:en"=&gt;"SPE", "ref:ru"=&gt;"СПБ", "name:ab"=&gt;"Санқт-Петербург", "name:de"=&gt;"Sankt Petersburg", "name:en"=&gt;"Saint Petersburg", "name:os"=&gt;"Бетъырбух", "name:ru"=&gt;"Санкт-Петербург", "wikipedia"=&gt;"ru:Санкт-Петербург", "okato:user"=&gt;"40000000000", "official_status"=&gt;"ru:город федерального значения"</em></p>
<p>So, why in <strong>name:en</strong> column I've got some extra symbols?</p>
<p>And where I should make changes to see the both city names?</p>
<p>Thanks for help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-multilingual" rel="tag" title="see questions tagged &#39;multilingual&#39;">multilingual</span> <span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-english" rel="tag" title="see questions tagged &#39;english&#39;">english</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '16, 10:40</strong></p>
<img src="https://secure.gravatar.com/avatar/b747822a88415ab0a0e16accce9fa477?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bobinho&#39;s gravatar image" />
<p><span>Bobinho</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bobinho has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48349" class="comments-container">
&#10;</div>
<div id="comment-tools-48349" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48349-form-container" class="comment-form-container">
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

<span id="48350"></span>

<div id="answer-container-48350" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48350-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You appear to have misunderstood the -z flag. This merely allows one to rename the (or create an additional) hstore column. It does not add the requested tag. So what you are seeing is the raw hstore data (all tags as key=&gt;value pairs).</p>
<p>To achieve what you want it is necessary to edit the style files used by osm2pgsql. Normally you will use default.style (see here <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/default.style),">https://github.com/openstreetmap/osm2pgsql/blob/master/default.style),</a> and modify this to add an extra line similar to the one for "name" replacing "name" with "name:en".</p>
<p>It is probably best to create this as a distinct style and apply it using the -S flag when you execute osm2pgsql.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '16, 11:12</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-48350" class="comments-container">
<span id="48352"></span>
<div id="comment-48352" class="comment">
<div id="post-48352-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you! After using -S flag "name:en" column is correct. Where else I should make changes to display both city names like: Zürich (Zurich)?</p>
</div>
<div id="comment-48352-info" class="comment-info">
<span class="comment-age">(25 Feb '16, 11:44)</span> <span class="comment-user userinfo">Bobinho</span>
</div>
</div>
</div>
<div id="comment-tools-48350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48350-form-container" class="comment-form-container">
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

