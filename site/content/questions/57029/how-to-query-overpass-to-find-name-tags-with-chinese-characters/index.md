+++
type = "question"
title = "How to query overpass to find name tags with Chinese characters?"
description = '''I was recently looking at the Indian state of Arunachal Pradesh, and noticed that many rivers had been provided with Chinese names. Soon I found Villages and lakes with Chinese names too.  This state has been administered by India, since India&#x27;s independence, but is claimed by China, as part of Tibe...'''
date = "2017-07-12T08:32:00Z"
lastmod = "2017-07-14T18:53:00Z"
weight = 57029
keywords = [ "overpass", "unicode", "name", "chinese", "query" ]
aliases = [ "/questions/57029" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to query overpass to find name tags with Chinese characters?](/questions/57029/how-to-query-overpass-to-find-name-tags-with-chinese-characters)

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
<span id="post-57029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57029-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was recently looking at the Indian state of Arunachal Pradesh, and noticed that many rivers had been provided with Chinese names. Soon I found Villages and lakes with Chinese names too.</p>
<p>This state has been administered by India, since India's independence, but is claimed by China, as part of Tibet, and therefore part of China. I suspect that this claim is related to the fact that some Chinese names have ended up on objects here.</p>
<p>I have been working on moving Chinese names to the <code>name:zh</code> tag, but it's hard to find everything. I would like to be able to construct a overpass query that only returned objects that have <code>name</code> tags with characters in unicode's Chinese range (or the CJK range, as this would be accurate enough).</p>
<p>This is way over my head, as I know next to nothing about overpass queries or character encoding. Can someone lend a hand?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-unicode" rel="tag" title="see questions tagged &#39;unicode&#39;">unicode</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-chinese" rel="tag" title="see questions tagged &#39;chinese&#39;">chinese</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '17, 08:32</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '17, 08:19</strong> </span></p>
</div>
</div>
<div id="comments-container-57029" class="comments-container">
<span id="57036"></span>
<div id="comment-57036" class="comment">
<div id="post-57036-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't see anything like that in the Overpass documentation. Could you just download objects with name tags and do the analysis yourself offline?</p>
</div>
<div id="comment-57036-info" class="comment-info">
<span class="comment-age">(12 Jul '17, 15:16)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="57037"></span>
<div id="comment-57037" class="comment">
<div id="post-57037-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Try to download all names, then sort them. This should lead to all Chinese names being next to each other. Maybe you can use the CSV output to generate a list with <code>name,type,OSM ID</code> or something similar.</p>
</div>
<div id="comment-57037-info" class="comment-info">
<span class="comment-age">(12 Jul '17, 15:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="57038"></span>
<div id="comment-57038" class="comment">
<div id="post-57038-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess you could find some of them with a regular expression that tests for some common characters in names of villages.</p>
</div>
<div id="comment-57038-info" class="comment-info">
<span class="comment-age">(12 Jul '17, 16:59)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-57029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57029-form-container" class="comment-form-container">
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

<span id="57040"></span>

<div id="answer-container-57040" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57040-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-57040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="keithonearth has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One of the Overpass-API developers runs a server with prototype support for ICU character ranges in regex:</p>
<p><a href="https://www.openstreetmap.org/user/mmd/diary/40197">https://www.openstreetmap.org/user/mmd/diary/40197</a></p>
<p>This makes the query straightforward:</p>
<p><a href="http://overpass-turbo.eu/s/qlv">http://overpass-turbo.eu/s/qlv</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '17, 18:00</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-57040" class="comments-container">
&#10;</div>
<div id="comment-tools-57040" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57040-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="57100"></span>

<div id="answer-container-57100" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57100-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Osmose-QA have check for this, look at: <a href="http://osmose.openstreetmap.fr/en/map/#zoom=7&amp;lat=27.858&amp;lon=94.465&amp;layer=Mapnik&amp;overlays=FFFFFFFFFFFFFFFFFFFFT&amp;item=5070&amp;level=1%2C2%2C3&amp;tags=&amp;fixable=">http://osmose.openstreetmap.fr/en/map/#zoom=7&amp;lat=27.858&amp;lon=94.465&amp;layer=Mapnik&amp;overlays=FFFFFFFFFFFFFFFFFFFFT&amp;item=5070&amp;level=1%2C2%2C3&amp;tags=&amp;fixable=</a></p>
<p>The check matchs the language, or the default for the country for "name" tag, with the content.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '17, 18:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0ca0ed82dfebe8539147e56d695aecfc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frodrigo&#39;s gravatar image" />
<p><span>frodrigo</span><br />
<span class="score" title="674 reputation points">674</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frodrigo has 4 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-57100" class="comments-container">
&#10;</div>
<div id="comment-tools-57100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57100-form-container" class="comment-form-container">
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

