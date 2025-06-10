+++
type = "question"
title = "Curl gives empty response"
description = '''What am I doing wrong here? curl &#x27;http://nominatim.openstreetmap.org/?q=Wokingham,%20Berkshire,%20England&amp;amp;format=json&#x27; gives the empty response []'''
date = "2017-05-26T13:44:00Z"
lastmod = "2017-05-26T20:59:00Z"
weight = 56321
keywords = [ "json", "curl" ]
aliases = [ "/questions/56321" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Curl gives empty response](/questions/56321/curl-gives-empty-response)

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
<span id="post-56321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56321-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What am I doing wrong here?</p>
<p>curl 'http://nominatim.openstreetmap.org/?q=Wokingham,%20Berkshire,%20England&amp;format=json'</p>
<p>gives the empty response</p>
<p>[]</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-curl" rel="tag" title="see questions tagged &#39;curl&#39;">curl</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '17, 13:44</strong></p>
<img src="https://secure.gravatar.com/avatar/50bd0c9a0dfa7ded438dc5c77087d214?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nigelhorne&#39;s gravatar image" />
<p><span>nigelhorne</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nigelhorne has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56321" class="comments-container">
&#10;</div>
<div id="comment-tools-56321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56321-form-container" class="comment-form-container">
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

<span id="56324"></span>

<div id="answer-container-56324" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56324-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim does not calculate a relationship between Wokingham and Berkshire.</p>
<p>I don't know why that is but I think it must be the problem with <a href="http://nominatim.openstreetmap.org/?q=Wokingham,England&amp;format=json"><code>http://nominatim.openstreetmap.org/?q=Wokingham,England&amp;format=json</code></a> returning the reasonable result.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '17, 16:45</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-56324" class="comments-container">
<span id="56327"></span>
<div id="comment-56327" class="comment">
<div id="post-56327-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply. Wokingham is in Berkshire, so it should work.</p>
</div>
<div id="comment-56327-info" class="comment-info">
<span class="comment-age">(26 May '17, 17:25)</span> <span class="comment-user userinfo">nigelhorne</span>
</div>
</div>
<span id="56329"></span>
<div id="comment-56329" class="comment">
<div id="post-56329-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Berkshire no longer exists, and is certainly no longer a standard part of a postal address. Its possible that the ceremonial county of Berkshire (which does still have some role) has not been added to OSM, or that Nominatim does not use such information. Similar problems exist for places such as Hayes (Middlesex) and Kingston (Surrey). It is not clear that OSM can support older geographies such as these. Most countries tend to keep admin &amp; address geographies aligned, but not the UK.</p>
</div>
<div id="comment-56329-info" class="comment-info">
<span class="comment-age">(26 May '17, 20:41)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="56330"></span>
<div id="comment-56330" class="comment">
<div id="post-56330-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The ceremonial county is present: <a href="http://nominatim.openstreetmap.org/?q=Berkshire,England&amp;format=json">http://nominatim.openstreetmap.org/?q=Berkshire,England&amp;format=json</a></p>
<p>So that fills out the answer, Nominatim is not including the ceremonial county in the address hierarchy (and any query parsed as looking for 'children' of Berkshire will return 0 results).</p>
</div>
<div id="comment-56330-info" class="comment-info">
<span class="comment-age">(26 May '17, 20:59)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-56324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56324-form-container" class="comment-form-container">
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

