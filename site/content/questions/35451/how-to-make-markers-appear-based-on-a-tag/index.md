+++
type = "question"
title = "How to make markers appear based on a tag?"
description = '''I don&#x27;t know how to make markers appear based on tag. For example, when I go to www.openstreetmap.org , how do I make it to show all the markers which have a particular tag? If I wanted to see all the places which have the &quot;payment:bitcoin=yes&quot; tag (as on coinmap.org), how would I do that on www.ope...'''
date = "2014-08-02T21:42:00Z"
lastmod = "2014-11-27T17:22:00Z"
weight = 35451
keywords = [ "osm.org", "tag", "markers" ]
aliases = [ "/questions/35451" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to make markers appear based on a tag?](/questions/35451/how-to-make-markers-appear-based-on-a-tag)

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
<span id="post-35451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35451-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I don't know how to make markers appear based on tag. For example, when I go to www.openstreetmap.org , how do I make it to show all the markers which have a particular tag? If I wanted to see all the places which have the "payment:bitcoin=yes" tag (as on coinmap.org), how would I do that on www.openstreetmap.org ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-markers" rel="tag" title="see questions tagged &#39;markers&#39;">markers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '14, 21:42</strong></p>
<img src="https://secure.gravatar.com/avatar/50fe91b92700501c70ca25c114030e44?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bitcoinLTorg&#39;s gravatar image" />
<p><span>bitcoinLTorg</span><br />
<span class="score" title="5 reputation points">5</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bitcoinLTorg has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Aug '14, 01:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-35451" class="comments-container">
&#10;</div>
<div id="comment-tools-35451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35451-form-container" class="comment-form-container">
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

<span id="35452"></span>

<div id="answer-container-35452" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35452-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-35452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bitcoinLTorg has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The OpenStreetMap web site does not offer such functionality. You need your own database with OSM data which you can then query to your heart's content and display the results using a library like Leaftlet or OpenLayers - or you use a database supplied by someone else, e.g. the Overpass API or its easy-to-use web interface, <a href="http://overpass-turbo.eu">Overpass Turbo</a>.</p>
<p>Note that if you use public resources like the OSM tile server or the Overpass search engine, you are expected to use these responsibly, and if you plan to set up a site that attracts many views, it might be advisable to have your own database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '14, 22:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-35452" class="comments-container">
<span id="35454"></span>
<div id="comment-35454" class="comment">
<div id="post-35454-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>A ready made solution is to use umap.openstreetmap.org together with data obtained from an OverPass instance. Frederiks observations wrt using shared public resources naturally apply in this scenario too.</p>
</div>
<div id="comment-35454-info" class="comment-info">
<span class="comment-age">(03 Aug '14, 01:16)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="38885"></span>
<div id="comment-38885" class="comment">
<div id="post-38885-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>… that instance seems to be down (was this existing ever?). See <span>uMap in our docu wiki</span> for other uMap instances.</p>
</div>
<div id="comment-38885-info" class="comment-info">
<span class="comment-age">(27 Nov '14, 17:22)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-35452" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35452-form-container" class="comment-form-container">
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

