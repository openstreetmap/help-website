+++
type = "question"
title = "Структура OSM файла / Structure of the OSM file"
description = '''Уважаемые коллеги! Я хочу сделать парсер и получить из OSM-файла связанную информацию типа Область/Район/Населенный пункт/Улица/Дом. Можно ли считать, что если начать с корневого relation страны, то спускаясь вниз по вложенным relation и далее по их way и node, я смогу получить всю информацию? Прост...'''
date = "2011-01-31T19:12:00Z"
lastmod = "2011-02-01T09:07:00Z"
weight = 2621
keywords = [ "node", "lang-ru", "parser", "relation", "way" ]
aliases = [ "/questions/2621" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Структура OSM файла / Structure of the OSM file](/questions/2621/osm-structure-of-the-osm-file)

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
<span id="post-2621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2621-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Уважаемые коллеги!</strong></p>
<p>Я хочу сделать парсер и получить из OSM-файла связанную информацию типа Область/Район/Населенный пункт/Улица/Дом. Можно ли считать, что если начать с корневого relation страны, то спускаясь вниз по вложенным relation и далее по их way и node, я смогу получить всю информацию? Просто эксперименты показали, что в OSM-файле имеются "висящие" way и node. Т.е. например node входит в состав way, а way никуда не входит. Попытки в таком случае определить принадлежность по координатам (вхождение внутрь полигона) тоже не всегда дает результат, т.к. многие населенные пункты (в основном деревни) вообще не имеют границ (way с ролью border). Хочется знать, на какие вещи можно 100% полагаться.</p>
<p>Спасибо.</p>
<p>[ English translation via Google Translate ]</p>
<p>I want to make the parser and get the file from the OSM-related information such as State / District / Town / Street / House. Can I assume that if we start from the root relation of the country, descended down the nested relation and continue on their way and node, I can get all the information? Simple experiments showed that the OSM-file are "hanging" way and the node. Ie such node is part of the way, a way will not enter. Attempts in this case to determine the membership of the coordinates (entering into the landfill) do not always produce the result, because many communities (mostly villages) have no boundaries (way the role of the border). Want to know which things can be 100% relied upon.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-lang-ru" rel="tag" title="see questions tagged &#39;lang-ru&#39;">lang-ru</span> <span class="post-tag tag-link-parser" rel="tag" title="see questions tagged &#39;parser&#39;">parser</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jan '11, 19:12</strong></p>
<img src="https://secure.gravatar.com/avatar/b26842858cd8146631c18952f308ded4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="askokov&#39;s gravatar image" />
<p><span>askokov</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="askokov has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jul '13, 21:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-2621" class="comments-container">
&#10;</div>
<div id="comment-tools-2621" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2621-form-container" class="comment-form-container">
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

<span id="2640"></span>

<div id="answer-container-2640" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2640-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-2640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The only reliable way to find all the towns and villages in a particular area is to treat the data as a <a href="http://en.wikipedia.org/wiki/Spatial_analysis">spatial dataset</a> and calculate the results using the coordinates. OSM data does not, and usually <em>should</em> not, have a hierarchy of places like you describe.</p>
<p>You should first describe the area that you are interested in in terms of a polygon of coordinates, then use that polygon with a suitable <a href="http://wiki.openstreetmap.org/wiki/Planet.osm#Extracts">planet file extract</a> and <a href="http://wiki.openstreetmap.org/wiki/Osmosis">osmosis</a> to generate data within that polygon. You can then find all the towns, villages etc by filtering for the nodes, and ways containing nodes, that you have within your area.</p>
<p>For most search / hierarchy challenges like this I would suggest starting with the <a href="http://wiki.openstreetmap.org/wiki/Nominatim">nominatim</a> software, which does all this processing for you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '11, 09:07</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-2640" class="comments-container">
&#10;</div>
<div id="comment-tools-2640" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2640-form-container" class="comment-form-container">
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

