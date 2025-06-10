+++
type = "question"
title = "How to highlight country borders in HTML map embed"
description = '''When I type a name of a country in Open street Maps it shows this country with highlighted borders, here is an example screenshot: http://prntscr.com/qrvwlg But when I use HTML embed it never shows the country borders. I only have the option to place a marker on the map and change the layers, but it...'''
date = "2020-01-23T16:58:00Z"
lastmod = "2020-01-27T01:33:00Z"
weight = 72644
keywords = [ "country", "borders", "multipolygon", "lines", "highlight" ]
aliases = [ "/questions/72644" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to highlight country borders in HTML map embed](/questions/72644/how-to-highlight-country-borders-in-html-map-embed)

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
<span id="post-72644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72644-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I type a name of a country in Open street Maps it shows this country with highlighted borders, here is an example screenshot: <a href="http://prntscr.com/qrvwlg">http://prntscr.com/qrvwlg</a></p>
<p>But when I use HTML embed it never shows the country borders. I only have the option to place a marker on the map and change the layers, but it never shows the country border.</p>
<p>Please help me if you can</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-borders" rel="tag" title="see questions tagged &#39;borders&#39;">borders</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span> <span class="post-tag tag-link-lines" rel="tag" title="see questions tagged &#39;lines&#39;">lines</span> <span class="post-tag tag-link-highlight" rel="tag" title="see questions tagged &#39;highlight&#39;">highlight</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jan '20, 16:58</strong></p>
<img src="https://secure.gravatar.com/avatar/52107d8127a33ac27126bd38f77d34ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nexuso&#39;s gravatar image" />
<p><span>Nexuso</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nexuso has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72644" class="comments-container">
&#10;</div>
<div id="comment-tools-72644" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72644-form-container" class="comment-form-container">
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

<span id="72702"></span>

<div id="answer-container-72702" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72702-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should try using <a href="https://overpass-turbo.eu/">overpass-turbo</a>.</p>
<p><a href="https://overpass-turbo.eu/s/Q7P">This request</a> will load the "Belgium" relation, I've used wikidata keyword, but others will work.</p>
<p>And there's an Export - Map - interactive Map function, that generate a link that you will be able to embed properly, see <a href="https://overpass-turbo.eu/map.html?Q=%5Bout%3Ajson%5D%5Btimeout%3A25%5D%3B%0A%2F%2F%20gather%20results%0A(%0A%20%20relation%5B%22type%22%3D%22boundary%22%5D%5B%22wikidata%22%3D%22Q31%22%5D%3B%0A)%3B%0A%2F%2F%20print%20results%0Aout%20body%3B%0A%3E%3B%0Aout%20skel%20qt%3B">this link</a>. The URL is quite ugly as the overpass query is encoded in it, but the result is quite similar to your screenshot !</p>
<p>If you don't really need interactivity, you should just export an image, it will be nicer on the servers.</p>
<p>Overpass is great, and overpass-turbo is just awesome.</p>
<p>If you need a lot of customization, <a href="https://wiki.openstreetmap.org/wiki/UMap">uMap</a> will be the next step. You can use it to render overpass queries, with a lot of options.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '20, 01:33</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jan '20, 01:33</strong> </span></p>
</div>
</div>
<div id="comments-container-72702" class="comments-container">
&#10;</div>
<div id="comment-tools-72702" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72702-form-container" class="comment-form-container">
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

