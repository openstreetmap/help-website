+++
type = "question"
title = "physical attributes by which map is rendered / please help !"
description = '''Hello,  I am working on a design/art project by which I seek to distort a map of a certain location by modifying, adding fictional attributes by which api renders a map; street, objects, boundaries?  How could I do that ? Thank you, Lukas'''
date = "2013-03-04T16:38:00Z"
lastmod = "2013-03-04T21:33:00Z"
weight = 20489
keywords = [ "api", "map", "physical", "design", "attributes" ]
aliases = [ "/questions/20489" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [physical attributes by which map is rendered / please help !](/questions/20489/physical-attributes-by-which-map-is-rendered-please-help)

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
<span id="post-20489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20489-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am working on a design/art project by which I seek to distort a map of a certain location by modifying, adding fictional attributes by which api renders a map; street, objects, boundaries?</p>
<p>How could I do that ? Thank you, Lukas</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-physical" rel="tag" title="see questions tagged &#39;physical&#39;">physical</span> <span class="post-tag tag-link-design" rel="tag" title="see questions tagged &#39;design&#39;">design</span> <span class="post-tag tag-link-attributes" rel="tag" title="see questions tagged &#39;attributes&#39;">attributes</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '13, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/7557743769253d5fb1be9e2df7972c1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lukasvaliauga&#39;s gravatar image" />
<p><span>lukasvaliauga</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lukasvaliauga has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20489" class="comments-container">
<span id="20493"></span>
<div id="comment-20493" class="comment">
<div id="post-20493-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sorry, your question is not very clear. Do you want to draw a fantasy map of some location? Do you want to use real data for a location and make a crazy map (with different colors)?</p>
</div>
<div id="comment-20493-info" class="comment-info">
<span class="comment-age">(04 Mar '13, 20:21)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-20489" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20489-form-container" class="comment-form-container">
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

<span id="20497"></span>

<div id="answer-container-20497" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20497-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(guessing a bit here, because as gormo says the question's not completely clear), but I suspect that you'll need to do the following:</p>
<ol>
<li>Download some data from OSM.</li>
<li>Edit that data locally using JOSM.</li>
<li>Render it locally (make a pretty picture from the raw data).</li>
</ol>
<p>Obviously it's important that you DON'T upload something that doesn't exist back to OSM, but as long as you don't do that, you can edit away to your heart's content.</p>
<p>For a brief introduction to how OSM data is structured, I'd start <a href="https://wiki.openstreetmap.org/wiki/Beginners_Guide_1.3">here</a>. The most used OSM offline editor is <a href="https://wiki.openstreetmap.org/wiki/Josm">JOSM</a>. It allows you to edit your local data and overlay the results over different background imagery, so you can compare your "imaginary" places to the real ones.</p>
<p>There are several <a href="https://wiki.openstreetmap.org/wiki/Rendering">rendering</a> options, one of which is <a href="https://wiki.openstreetmap.org/wiki/Maperitive">Maperitive</a>. Even if it isn't ideal for you, searching this site for <a href="https://help.openstreetmap.org/search/?q=maperitive&amp;Submit=Search&amp;t=question">Maperitive</a> will get you a list of answers to previous "how do I render my data" questions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '13, 21:33</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-20497" class="comments-container">
&#10;</div>
<div id="comment-tools-20497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20497-form-container" class="comment-form-container">
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

