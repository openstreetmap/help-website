+++
type = "question"
title = "How to create a public transport route which only runs on a part of a street&#x27;s way? Divide the way?"
description = '''Hi, Guys Im working on the public transport routing service and found one weird thing with the bus route  here The problem is  after passing the street Rua Professor Milton Roque Ramos Krieger the bus turns right to Rua Lauro Linhares at this point. But if u take a look on the root details again u&#x27;l...'''
date = "2013-07-31T00:31:00Z"
lastmod = "2013-07-31T01:19:00Z"
weight = 24758
keywords = [ "public-transport", "route", "street", "relation", "divide" ]
aliases = [ "/questions/24758" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to create a public transport route which only runs on a part of a street's way? Divide the way?](/questions/24758/how-to-create-a-public-transport-route-which-only-runs-on-a-part-of-a-streets-way-divide-the-way)

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
<span id="post-24758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24758-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, Guys Im working on the public transport routing service and found one weird thing with the bus route <a href="http://www.openstreetmap.org/browse/relation/2521698">here</a></p>
<p>The problem is after passing the street Rua Professor Milton Roque Ramos Krieger the bus turns right to Rua Lauro Linhares at this <a href="http://www.openstreetmap.org/browse/node/1438405028">point</a>. But if u take a look on the root details again u'll notice that the route also goes to the left that is not true. This happens because the bus route goes through part of the street Rua Lauro Linhares and this full street (way) is included in route relation. Removing the street (way) from the path will cause a gap in the route.</p>
<p>Actually it does not hurt my application but it looks wrong on the map and may confuse users. How can I fix it gracefully? Maybe devide the street (way) Rua Lauro Linhares into smaller ways? Or maybe there is another better solution?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-divide" rel="tag" title="see questions tagged &#39;divide&#39;">divide</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '13, 00:31</strong></p>
<img src="https://secure.gravatar.com/avatar/4a71fa65192c7759fe3f7f1524054fcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbraginini&#39;s gravatar image" />
<p><span>mbraginini</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbraginini has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jul '13, 01:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-24758" class="comments-container">
&#10;</div>
<div id="comment-tools-24758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24758-form-container" class="comment-form-container">
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

<span id="24759"></span>

<div id="answer-container-24759" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24759-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-24759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mbraginini has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Divide the road, and include in the relation only that part which is actually used by the bus.</p>
<p>This is something that people often complain about - creating public transport relation unnecessarily fragments our streets - but currently there's no better solution. Maybe in the future we'll have an option to make only a <em>part</em> of a street a relation member.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '13, 01:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-24759" class="comments-container">
&#10;</div>
<div id="comment-tools-24759" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24759-form-container" class="comment-form-container">
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

