+++
type = "question"
title = "How to set name of way based on ref of relations?"
description = '''Hi. My question is probably odd, so let me elaborate. I am interested in creating tram and bus map, like opnvkarte: http://img706.imageshack.us/img706/2911/opnvkarte.png Unfortunately, they do not allow me to download whole Krakow, so I am forced to generate my own map. I have managed to do somethin...'''
date = "2012-08-03T14:05:00Z"
lastmod = "2012-08-03T16:06:00Z"
weight = 14808
keywords = [ "tram", "opnvkarte" ]
aliases = [ "/questions/14808" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to set name of way based on ref of relations?](/questions/14808/how-to-set-name-of-way-based-on-ref-of-relations)

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
<span id="post-14808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14808-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. My question is probably odd, so let me elaborate. I am interested in creating tram and bus map, like opnvkarte: <a href="http://img706.imageshack.us/img706/2911/opnvkarte.png">http://img706.imageshack.us/img706/2911/opnvkarte.png</a></p>
<p>Unfortunately, they do not allow me to download whole Krakow, so I am forced to generate my own map. I have managed to do something like that: <a href="http://img849.imageshack.us/img849/5830/36296467.png">http://img849.imageshack.us/img849/5830/36296467.png</a></p>
<p>So, here is my question: How to set (locally) name of ways, so it would contain ref separated (like in opnvkarte) of tram routes?</p>
<p>Sorry for my English and lack of knowledge - I didn't know anything about OpenStreetMap until yesterday.</p>
<p>Cheers!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tram" rel="tag" title="see questions tagged &#39;tram&#39;">tram</span> <span class="post-tag tag-link-opnvkarte" rel="tag" title="see questions tagged &#39;opnvkarte&#39;">opnvkarte</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '12, 14:05</strong></p>
<img src="https://secure.gravatar.com/avatar/9aed0ffd0a1c490a0f168cb19f82e759?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="michal_wawrz&#39;s gravatar image" />
<p><span>michal_wawrz</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="michal_wawrz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Aug '12, 14:06</strong> </span></p>
</div>
</div>
<div id="comments-container-14808" class="comments-container">
<span id="14813"></span>
<div id="comment-14813" class="comment">
<div id="post-14813-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Since I don't quite understand your answer yet, here is better image of what I am trying to accomplish: <a href="http://img815.imageshack.us/img815/8802/zblk.png">http://img815.imageshack.us/img815/8802/zblk.png</a> (refs of relations containing specific way separated by coma)</p>
</div>
<div id="comment-14813-info" class="comment-info">
<span class="comment-age">(03 Aug '12, 16:06)</span> <span class="comment-user userinfo">michal_wawrz</span>
</div>
</div>
</div>
<div id="comment-tools-14808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14808-form-container" class="comment-form-container">
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

<span id="14809"></span>

<div id="answer-container-14809" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14809-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You would normally import your data into a database prior to rendering it. The <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a> tool - one of several tools that can do this - can generate linestring geometries for relations which you can then draw.</p>
<p>You could also check out Maperitive which works on raw OSM data, without database import, and it has relation support as well: <a href="http://maperitive.net/docs/manual/FAQ.html#How%20do%20I%20define%20a%20relation%20rule?">http://maperitive.net/docs/manual/FAQ.html#How%20do%20I%20define%20a%20relation%20rule?</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '12, 14:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Aug '12, 18:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span></p>
</div>
</div>
<div id="comments-container-14809" class="comments-container">
&#10;</div>
<div id="comment-tools-14809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14809-form-container" class="comment-form-container">
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

