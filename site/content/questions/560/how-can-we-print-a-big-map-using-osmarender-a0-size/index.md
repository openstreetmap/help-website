+++
type = "question"
title = "How can we print a big map using OSMArender (A0 size) ?"
description = '''We already tried that but had the problem that the computer stucks or the fonts are to small to read. The map would cover a full capital city (Addis Ababa).'''
date = "2010-08-03T18:02:00Z"
lastmod = "2010-08-16T17:22:00Z"
weight = 560
keywords = [ "printing" ]
aliases = [ "/questions/560" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How can we print a big map using OSMArender (A0 size) ?](/questions/560/how-can-we-print-a-big-map-using-osmarender-a0-size)

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
<span id="post-560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-560-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We already tried that but had the problem that the computer stucks or the fonts are to small to read.</p>
<p>The map would cover a full capital city (Addis Ababa).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-printing" rel="tag" title="see questions tagged &#39;printing&#39;">printing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '10, 18:02</strong></p>
<img src="https://secure.gravatar.com/avatar/c283009948b4e8f8c278c417d68b641e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alazar%20AddisMap&#39;s gravatar image" />
<p><span>Alazar AddisMap</span><br />
<span class="score" title="90 reputation points">90</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alazar AddisMap has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-560" class="comments-container">
<span id="581"></span>
<div id="comment-581" class="comment">
<div id="post-581-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does the computer get stuck during rendering or when you open the resulting SVG in Inkscape?</p>
</div>
<div id="comment-581-info" class="comment-info">
<span class="comment-age">(06 Aug '10, 12:17)</span> <span class="comment-user userinfo">Alex_AddisMap</span>
</div>
</div>
<span id="658"></span>
<div id="comment-658" class="comment">
<div id="post-658-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Usually when rendering it takes more than half day. But the biggest problem is when I try to open the final SVG file that my PC gets stuck. But even after restarting my PC if I accidentally open the folder containing this SVG file it gets stuck again even if I don't try to open the SVG.</p>
</div>
<div id="comment-658-info" class="comment-info">
<span class="comment-age">(13 Aug '10, 13:58)</span> <span class="comment-user userinfo">Alazar AddisMap</span>
</div>
</div>
</div>
<div id="comment-tools-560" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-560-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="576"></span>

<div id="answer-container-576" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-576-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Osmarender uses CSS classes to format the map features. You will find the style rules contained in the rule file and could change the font size there. As soon as you run Osmarender to generate the map, it will put those style rules within the generated SVG file what results in the desired font size.</p>
<p>When your computer has problems processing the data this is not caused by an altered font size. Try the following depending on your problem:</p>
<ul>
<li><strong>Gets stuck while Osmarender runs:</strong> Try another XSL processor</li>
<li><strong>Gets stuck while displaying or printing the generated SVG:</strong> Try another vector graphics software or try the wireframe mode (if supported by your software)</li>
</ul>
<p>If there is no need to do the job using Osmarender it might be worth looking at other renders such as <a href="https://wiki.openstreetmap.org/wiki/Maperitive">Maperitive</a> or <a href="https://wiki.openstreetmap.org/wiki/Mapgen.pl">Mapgen</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '10, 00:58</strong></p>
<img src="https://secure.gravatar.com/avatar/0c84690144aa89b47bbdd1395cd36f01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Augustus%20Kling&#39;s gravatar image" />
<p><span>Augustus Kling</span><br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Augustus Kling has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-576" class="comments-container">
<span id="580"></span>
<div id="comment-580" class="comment">
<div id="post-580-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you have any suggestion for such a capable/fast XSL processor? (for Ubuntu)</p>
</div>
<div id="comment-580-info" class="comment-info">
<span class="comment-age">(06 Aug '10, 12:16)</span> <span class="comment-user userinfo">Alex_AddisMap</span>
</div>
</div>
<span id="593"></span>
<div id="comment-593" class="comment">
<div id="post-593-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm using xsltproc at the moment on Ubuntu which works fine for me. Wikipedia has a long list of other processors at <a href="http://en.wikipedia.org/wiki/XSLT_processor#Implementations">http://en.wikipedia.org/wiki/XSLT_processor#Implementations</a> . You might also want to try out <a href="https://wiki.openstreetmap.org/wiki/Orp">https://wiki.openstreetmap.org/wiki/Orp</a> that is a reimplementation of Osmarender without using XSLT but Perl instead.</p>
<p>For a more general explanation see also <a href="/questions/136/how-do-i-render-my-own-maps-for-my-website/207">https://help.openstreetmap.org/questions/136/how-do-i-render-my-own-maps-for-my-website/207</a> and the links mentioned there.</p>
</div>
<div id="comment-593-info" class="comment-info">
<span class="comment-age">(07 Aug '10, 23:10)</span> <span class="comment-user userinfo">Augustus Kling</span>
</div>
</div>
</div>
<div id="comment-tools-576" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-576-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="572"></span>

<div id="answer-container-572" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-572-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've only ever used a tile stitching approach using adapted versions of <a href="https://wiki.openstreetmap.org/wiki/BigMap">BigMap</a>. It's easy enough to point that script at osmarender tiles. But this is a raster printout, with the same problem of fonts being too small if you want to go for a high-res printout. Some more thoughts on this on <a href="http://www.harrywood.co.uk/blog/2009/12/10/openstreetmap-jigsaw/">my OSM jigsaw blog post</a>. This is also the approach used by Frederick when he does his big poster printouts. Vector is indeed problematic when it comes to printing a big complex city map without crashing your computer!</p>
<p>The font size problem seems to be tackled nicely for Mapnik if you scroll down to <a href="http://lorien.ancalime.de/demo.html">'Mapnik maps for other resolutions' on this page</a>. Not tried it myself, but it looks neat. It seems like you need to do a similar style transformation for osmarender. Not sure how you would go about that though.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Aug '10, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '10, 14:50</strong> </span></p>
</div>
</div>
<div id="comments-container-572" class="comments-container">
&#10;</div>
<div id="comment-tools-572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-572-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="578"></span>

<div id="answer-container-578" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-578-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do check out my responses to "<a href="/questions/22/how-do-i-export-map-images-of-larger-areas/23">how-do-i-export-map-images-of-larger-areas</a>". If you don't need customization those options should be easier to get large images. With osmarender and A0 sizes your are likely going to run into performance problems if you don't split up the area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '10, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/278e1af65e82993efd0ba7bbbacf6435?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spaetz&#39;s gravatar image" />
<p><span>spaetz</span><br />
<span class="score" title="853 reputation points">853</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spaetz has 2 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '10, 11:11</strong> </span></p>
</div>
</div>
<div id="comments-container-578" class="comments-container">
&#10;</div>
<div id="comment-tools-578" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-578-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="677"></span>

<div id="answer-container-677" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-677-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What zoom level do you need?</p>
<p>I've just tried exporting Addis Ababa using <a href="http://maperitive.net/">Maperitive</a> on zoom level 15 on my netbook and it produces a 1 MB SVG which I think shouldn't be a problem for processing on a normal PC . Exporting on zoom level 17 produces 1.4 MB.</p>
<p>If you want, I can send you the produced SVG to try it out on your machine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '10, 17:22</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-677" class="comments-container">
&#10;</div>
<div id="comment-tools-677" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-677-form-container" class="comment-form-container">
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

