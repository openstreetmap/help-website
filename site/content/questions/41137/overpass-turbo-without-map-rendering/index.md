+++
type = "question"
title = "overpass turbo without map rendering"
description = '''I&#x27;m trying to get all the paved roads in South America through an overpass-turbo query. To lighten the load, I split them into primary, trunk, etc. Here&#x27;s an example: http://overpass-turbo.eu/s/7JY This worked perfectly fine for trunk roads, but my browser crashes on the 80 mb generated for the prim...'''
date = "2015-02-18T23:55:00Z"
lastmod = "2016-03-09T09:05:00Z"
weight = 41137
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/41137" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [overpass turbo without map rendering](/questions/41137/overpass-turbo-without-map-rendering)

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
<span id="post-41137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41137-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to get all the paved roads in South America through an overpass-turbo query. To lighten the load, I split them into primary, trunk, etc. Here's an example: <a href="http://overpass-turbo.eu/s/7JY">http://overpass-turbo.eu/s/7JY</a></p>
<p>This worked perfectly fine for trunk roads, but my browser crashes on the 80 mb generated for the primary paved roads. I think it's just the rendering that causes the problem. I know there's a way to skip trying to render the generated data, but I can't find the info anywhere. I just need a gpx file of the data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Feb '15, 23:55</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-41137" class="comments-container">
<span id="48587"></span>
<div id="comment-48587" class="comment">
<div id="post-48587-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Now that's what I call Openstreetmap in action! Here's what it's useful for: <a href="http://www.openstreetmap.org/user/joost%20schouppe/diary/38103">http://www.openstreetmap.org/user/joost%20schouppe/diary/38103</a> :)</p>
</div>
<div id="comment-48587-info" class="comment-info">
<span class="comment-age">(09 Mar '16, 09:05)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
</div>
<div id="comment-tools-41137" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41137-form-container" class="comment-form-container">
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

<span id="41209"></span>

<div id="answer-container-41209" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41209-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-41209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joost schouppe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just click on "Export" -&gt; "raw data directly from Overpass API" in overpass turbo to download an .osm file (<em>don't</em> press run!). Then convert that .osm file into .gpx with whatever tool you have at hand.</p>
<p>I don't think JOSM or the query form will be needed in your case, unless you want to use JOSM for osm-&gt;gpx conversion.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '15, 16:23</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-41209" class="comments-container">
<span id="41225"></span>
<div id="comment-41225" class="comment">
<div id="post-41225-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, just what I needed. I did try some of the export functions, but most only work -after- you've run the query.</p>
<p>Funny bug though: the link refers to overpass-api.de , not www.overpass-api.de . And apparantly overpass-api.de only works with the www added. Now who to file this bug to? :)</p>
</div>
<div id="comment-41225-info" class="comment-info">
<span class="comment-age">(22 Feb '15, 00:49)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="41231"></span>
<div id="comment-41231" class="comment">
<div id="post-41231-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Overpass Turbo bug reports should go here: <a href="https://github.com/tyrasd/overpass-turbo">https://github.com/tyrasd/overpass-turbo</a> Overpass API bug reports should go here: <a href="https://github.com/drolbr/Overpass-API">https://github.com/drolbr/Overpass-API</a></p>
<p>In this case, as it's the connection between the two, you could choose where to file it. Roland can enable overpass-api.de to work, and tyr_asd can add the www I presume.</p>
</div>
<div id="comment-41231-info" class="comment-info">
<span class="comment-age">(22 Feb '15, 09:40)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
<span id="41234"></span>
<div id="comment-41234" class="comment">
<div id="post-41234-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I cannot reproduce this here. If overpass turbo works ok with the default setting "//overpass-api.de/api/", I don't see a reason, why the download shouldn't work. Maybe some funny antivirus/firewall/etc. thing?</p>
</div>
<div id="comment-41234-info" class="comment-info">
<span class="comment-age">(22 Feb '15, 09:54)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="48474"></span>
<div id="comment-48474" class="comment">
<div id="post-48474-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just a note: don't forget to set [out:xml] instead of the standard json.</p>
</div>
<div id="comment-48474-info" class="comment-info">
<span class="comment-age">(03 Mar '16, 08:20)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-41209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41209-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41141"></span>

<div id="answer-container-41141" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41141-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use "Download from Overpass API" function in JOSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '15, 06:05</strong></p>
<img src="https://secure.gravatar.com/avatar/c7f2443ac02cb3e24f4df768eeb98933?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BushmanK&#39;s gravatar image" />
<p><span>BushmanK</span><br />
<span class="score" title="171 reputation points">171</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BushmanK has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-41141" class="comments-container">
<span id="41224"></span>
<div id="comment-41224" class="comment">
<div id="post-41224-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This requires the mirrored_download plugin (nasty thing in JOSM is that plugins integrate so seamlesly that you would forget you're using them). Also, couldn't get it to work (though I quit trying when I saw mnd's answer)</p>
</div>
<div id="comment-41224-info" class="comment-info">
<span class="comment-age">(22 Feb '15, 00:43)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-41141" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41141-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41203"></span>

<div id="answer-container-41203" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41203-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The easiest is to get the file directly from the Overpass API query form: <a href="http://www.overpass-api.de/query_form.html">http://www.overpass-api.de/query_form.html</a></p>
<p>Just copy-paste your query in it, and press the "query" button.</p>
<p>This way, you get the raw file, which can be even bigger than the size JOSM can handle. It also avoids having to download the meta data, when you don't need it. Or it allows you to use non-osm formats.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '15, 10:54</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-41203" class="comments-container">
<span id="41214"></span>
<div id="comment-41214" class="comment">
<div id="post-41214-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you tried this out before? Copy-pasting the query won't work, as the original query has Overpass Turbo specific parts in it (like {{bbox}}). If you send that 'syntactic sugar' directly Overpass API, you'll get lots of error messages! Overpass API doesn't know about {{bbox}} and only overpass turbo will do a proper translation before sending it to Overpass API.</p>
<p>Besides, there's still the issue of large data volume in the browser, which this answer does not address.</p>
</div>
<div id="comment-41214-info" class="comment-info">
<span class="comment-age">(21 Feb '15, 19:19)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="41230"></span>
<div id="comment-41230" class="comment">
<div id="post-41230-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Right, missed the {{bbox}} in the query. I normally use boundary definitions to avoid that.</p>
<p>As for the large data volume in the browser, that's not true. The browser normally asks to store the file, so it gets written directly to the disk without sitting in browser ram.</p>
<p>I use this method almost always when I need more data out Overpass API.</p>
<p>Of course, your solution is nicer, as it's a link directly from Overpass turbo to Overpass API, so you don't have to remember different URLs and it requires less clicks.</p>
</div>
<div id="comment-41230-info" class="comment-info">
<span class="comment-age">(22 Feb '15, 09:37)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
<span id="41232"></span>
<div id="comment-41232" class="comment">
<div id="post-41232-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmmm. I tried this now in Firefox and Chrome and both would show the query form result right in the browser window (Test query: <a href="http://overpass-turbo.eu/s/7NN">http://overpass-turbo.eu/s/7NN</a> --&gt; copied over to query form).</p>
<p>That's where my browser gets very sluggish with a lot of data. For some reason I don't get a save as file dialog. Whereas in overpass turbo, I could right click on "raw data directly from Overpass API" and just save the result in a file, without bothering too much with rendering all that JSON/XML data in the browser.</p>
</div>
<div id="comment-41232-info" class="comment-info">
<span class="comment-age">(22 Feb '15, 09:50)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="41235"></span>
<div id="comment-41235" class="comment">
<div id="post-41235-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm, it seems to depend on the format too. Some formats are opened as text in the browser, others are treated as file.</p>
<p>So far, XML is treated as a file in FF, while JSON is treated as in-browser text.</p>
</div>
<div id="comment-41235-info" class="comment-info">
<span class="comment-age">(22 Feb '15, 10:01)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-41203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41203-form-container" class="comment-form-container">
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

