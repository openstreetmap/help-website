+++
type = "question"
title = "How can I make a map showing parking in an area?"
description = '''Hi, I am trying to make a map showing all of the parking garages in an area (Los Angeles). When I search parking in the OSM search box it goes to a place in France. What am I missing here? I&#x27;ve done a google search and can&#x27;t seem to find an answer. Ideally I would like to be able to download a vecto...'''
date = "2017-09-03T02:08:00Z"
lastmod = "2017-09-03T14:30:00Z"
weight = 58933
keywords = [ "filter", "tags", "parking" ]
aliases = [ "/questions/58933" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I make a map showing parking in an area?](/questions/58933/how-can-i-make-a-map-showing-parking-in-an-area)

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
<span id="post-58933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58933-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am trying to make a map showing all of the parking garages in an area (Los Angeles). When I search parking in the OSM search box it goes to a place in France. What am I missing here? I've done a google search and can't seem to find an answer. Ideally I would like to be able to download a vector map of garages but I could also just grab a screenshot and trace over it.</p>
<p>Also, is there a way to filter for different types of parking? Open, above ground, below ground etc.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Sep '17, 02:08</strong></p>
<img src="https://secure.gravatar.com/avatar/82161eeb4e69e94af04863e7bd0cfb1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20C%20K&#39;s gravatar image" />
<p><span>David C K</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David C K has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58933" class="comments-container">
&#10;</div>
<div id="comment-tools-58933" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58933-form-container" class="comment-form-container">
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

<span id="58941"></span>

<div id="answer-container-58941" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58941-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-58941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not exactly what you asked for but may help:<br />
You could use <a href="http://overpass-turbo.eu">overpass turbo</a> . Select the wizard and type amenity=parking , zoom in close initially to an area to check if output is ok and build and run the query and you will see those on the map. You can export the data. You can also output meta which I think may give all tags of each element. By reading the documentation you should figure out how to extract various types of parking. You can get fancy and output differing colours to results.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '17, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Sep '17, 14:38</strong> </span></p>
</div>
</div>
<div id="comments-container-58941" class="comments-container">
&#10;</div>
<div id="comment-tools-58941" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58941-form-container" class="comment-form-container">
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

