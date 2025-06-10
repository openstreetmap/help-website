+++
type = "question"
title = "How to add only a few selected countries?"
description = '''Hello, How do I add a few selected countries only instead of adding the planet data? I used the following to add one, osm2pgsql --slim -d gis --hstore --multi-geometry --number-processes 10 --tag-transform-script /home/osm/openstreetmap-carto/openstreetmap-carto.lua --style /home/osm/openstreetmap-c...'''
date = "2022-07-28T09:21:00Z"
lastmod = "2022-07-28T10:35:00Z"
weight = 85240
keywords = [ "pbf", "osm", "osm2pgsql" ]
aliases = [ "/questions/85240" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to add only a few selected countries?](/questions/85240/how-to-add-only-a-few-selected-countries)

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
<span id="post-85240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85240-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>How do I add a few selected countries only instead of adding the planet data? I used the following to add one,</p>
<pre><code>osm2pgsql --slim -d gis --hstore --multi-geometry --number-processes 10 --tag-transform-script /home/osm/openstreetmap-carto/openstreetmap-carto.lua --style /home/osm/openstreetmap-carto/openstreetmap-carto.style -C 32000 /home/osm/qatar-latest.osm.pbf</code></pre>
<p>Can I use the same command and add another one or am I doing something wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jul '22, 09:21</strong></p>
<img src="https://secure.gravatar.com/avatar/8b0a55c52c5b269d33ab8ae812a90f4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="praveen_aps&#39;s gravatar image" />
<p><span>praveen_aps</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="praveen_aps has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jul '22, 05:13</strong> </span></p>
</div>
</div>
<div id="comments-container-85240" class="comments-container">
&#10;</div>
<div id="comment-tools-85240" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85240-form-container" class="comment-form-container">
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

<span id="85243"></span>

<div id="answer-container-85243" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85243-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-85243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="praveen_aps has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The safest approach is downloading a continent or planet file, then using <code>osmium</code> to cut out the area that interests you, resulting in one single file to import, then import that.</p>
<p>Alternatively, download individual countries, merge them with <code>osmium</code>, resulting in one single file, then import that.</p>
<p>Importing individual countries one after the other is not recommended, it is much slower than the approaches above.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '22, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-85243" class="comments-container">
<span id="85249"></span>
<div id="comment-85249" class="comment">
<div id="post-85249-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your response, although may I ask if there's any drawback to doing so apart from it being slower? because we'd like to add more countries as and when required.</p>
</div>
<div id="comment-85249-info" class="comment-info">
<span class="comment-age">(28 Jul '22, 09:57)</span> <span class="comment-user userinfo">praveen_aps</span>
</div>
</div>
<span id="85250"></span>
<div id="comment-85250" class="comment">
<div id="post-85250-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Being slower is the only drawback but depending on your setup you will find that it can take two weeks to add a country that way when it would take two hours to do a full import on a clean database. Just try it out, maybe you'll be lucky. What you need to do is convert the .osm.pbf that you want to add to an .osc file by using <code>osmium --derive-changes</code> to compute the changes between an empty file and the .osm.pbf you want to add. Then use <code>osm2pgsql --append</code> to append the .osc file to your database.</p>
</div>
<div id="comment-85250-info" class="comment-info">
<span class="comment-age">(28 Jul '22, 10:13)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="85252"></span>
<div id="comment-85252" class="comment">
<div id="post-85252-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, I'll try that out</p>
</div>
<div id="comment-85252-info" class="comment-info">
<span class="comment-age">(28 Jul '22, 10:35)</span> <span class="comment-user userinfo">praveen_aps</span>
</div>
</div>
</div>
<div id="comment-tools-85243" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85243-form-container" class="comment-form-container">
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

