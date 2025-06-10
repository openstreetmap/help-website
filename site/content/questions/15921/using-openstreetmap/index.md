+++
type = "question"
title = "Using Openstreetmap"
description = '''Hello, My name is ABHINAV. I am developing a web application for getting directions. I wanted to know how can I extract a particular part of a map from OPENSTREETMAP and accordingly program it for various purposes like: Intelligent Routing Cost and Time based calculations of the best. The app which ...'''
date = "2012-09-09T18:49:00Z"
lastmod = "2012-09-10T10:33:00Z"
weight = 15921
keywords = [ "directions", "howto", "routing", "webservice" ]
aliases = [ "/questions/15921" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using Openstreetmap](/questions/15921/using-openstreetmap)

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
<span id="post-15921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15921-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>My name is ABHINAV. I am developing a web application for getting directions. I wanted to know how can I extract a particular part of a map from OPENSTREETMAP and accordingly program it for various purposes like: Intelligent Routing Cost and Time based calculations of the best.</p>
<p>The app which I want to develop is on similar tracks with GOOGLE MAPS. So guys please help me and tell how can I program it according to my needs.</p>
<p>Thank You,</p>
<p>Abhinav</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span> <span class="post-tag tag-link-howto" rel="tag" title="see questions tagged &#39;howto&#39;">howto</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-webservice" rel="tag" title="see questions tagged &#39;webservice&#39;">webservice</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Sep '12, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a92363bb3658f63dd01149adacee4949?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ABHINAV%20SINGH&#39;s gravatar image" />
<p><span>ABHINAV SINGH</span><br />
<span class="score" title="25 reputation points">25</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ABHINAV SINGH has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Sep '12, 19:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span></p>
</div>
</div>
<div id="comments-container-15921" class="comments-container">
&#10;</div>
<div id="comment-tools-15921" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15921-form-container" class="comment-form-container">
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

<span id="15937"></span>

<div id="answer-container-15937" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15937-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First things first, you're going to need to find out about what OSM data contains. <a href="http://wiki.openstreetmap.org/wiki/Beginners_Guide_1.3">This page</a> from the beginners' guide is a simple introduction. Next, you're going to need to download some data. The XML data for the entire planet is huge, but there are links to some area-based extracts on <a href="http://wiki.openstreetmap.org/wiki/Planet.osm">this page</a>. To start with, you might just want to extract a very small amount of data locally to you - perhaps using <a href="http://wiki.openstreetmap.org/wiki/Xapi">XAPI</a> or <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass</a>.</p>
<p>Routing is a big topic in its own right and there are lots of issues to consider, but many of them are introduced <a href="http://wiki.openstreetmap.org/wiki/Routing">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Sep '12, 10:33</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-15937" class="comments-container">
&#10;</div>
<div id="comment-tools-15937" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15937-form-container" class="comment-form-container">
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

