+++
type = "question"
title = "In local tile server I have strange text in Russia for low zoom map."
description = '''Text like RU-MUR, RU-KR and etc. How can I turn it off ? I tried to find it in style.xml, but it&#x27;s nothing here about it. Map images with strange text'''
date = "2017-05-02T10:35:00Z"
lastmod = "2017-05-02T10:40:00Z"
weight = 55988
keywords = [ "russian", "osm", "rm-mur" ]
aliases = [ "/questions/55988" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [In local tile server I have strange text in Russia for low zoom map.](/questions/55988/in-local-tile-server-i-have-strange-text-in-russia-for-low-zoom-map)

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
<span id="post-55988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55988-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Text like RU-MUR, RU-KR and etc. How can I turn it off ? I tried to find it in style.xml, but it's nothing here about it. <a href="https://ibb.co/gB4Gqk">Map images with strange text</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-russian" rel="tag" title="see questions tagged &#39;russian&#39;">russian</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-rm-mur" rel="tag" title="see questions tagged &#39;rm-mur&#39;">rm-mur</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 May '17, 10:35</strong></p>
<img src="https://secure.gravatar.com/avatar/edd40901ff8584edb6adcb8b3b570401?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osm_russia&#39;s gravatar image" />
<p><span>osm_russia</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osm_russia has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55988" class="comments-container">
&#10;</div>
<div id="comment-tools-55988" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55988-form-container" class="comment-form-container">
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

<span id="55989"></span>

<div id="answer-container-55989" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55989-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="osm_russia has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have an openstreetmap-carto variant from before December 2016 where the <code>placenames.mss</code> file used the <code>ref</code> tag of states for labelling on lower zoom levels. See this commit which removed the feature: <a href="https://github.com/gravitystorm/openstreetmap-carto/commit/df45b20f2621b0aa6f34d31b01a086f22058a69c">https://github.com/gravitystorm/openstreetmap-carto/commit/df45b20f2621b0aa6f34d31b01a086f22058a69c</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '17, 10:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-55989" class="comments-container">
&#10;</div>
<div id="comment-tools-55989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55989-form-container" class="comment-form-container">
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

