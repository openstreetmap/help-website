+++
type = "question"
title = "How to cut out parts of an area"
description = '''I&#x27;m a beginner and starting little by little. I&#x27;ve simply started adding areas that are missing in my neighborhood, parks, playgrounds and such. But in many cases it&#x27;s not simply a case of drawing up an area. I&#x27;ll give a clear example: I have a park which covers an area, but there are portions insid...'''
date = "2018-05-23T11:30:00Z"
lastmod = "2018-05-23T12:54:00Z"
weight = 63646
keywords = [ "relation", "park", "inner", "way" ]
aliases = [ "/questions/63646" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to cut out parts of an area](/questions/63646/how-to-cut-out-parts-of-an-area)

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
<span id="post-63646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63646-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm a beginner and starting little by little. I've simply started adding areas that are missing in my neighborhood, parks, playgrounds and such. But in many cases it's not simply a case of drawing up an area. I'll give a clear example: I have a park which covers an area, but there are portions inside that are private and closed. I want to somehow exclude them from the park. Ideally I would like to eventually be able to do it to all the bigger parks in my area, because unfortunately many of them have had pieces cut out by land investors.</p>
<p>I have seen this done by somehow having the perimeter of the area marked as an outer line and than adding an inner line (and I think this way the simple area which was a way becomes a relation). Can this be done without JOSM? I've been trying to find info on this on my own but no luck</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-park" rel="tag" title="see questions tagged &#39;park&#39;">park</span> <span class="post-tag tag-link-inner" rel="tag" title="see questions tagged &#39;inner&#39;">inner</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '18, 11:30</strong></p>
<img src="https://secure.gravatar.com/avatar/fe2c941c194067f497be5654e097438b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AdrianIlie&#39;s gravatar image" />
<p><span>AdrianIlie</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AdrianIlie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63646" class="comments-container">
&#10;</div>
<div id="comment-tools-63646" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63646-form-container" class="comment-form-container">
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

<span id="63650"></span>

<div id="answer-container-63650" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63650-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The construct used in such cases are called <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">multipolygons</a></p>
<p>In <a href="https://wiki.openstreetmap.org/wiki/ID">iD</a> info on this can be found in the tutorial: press 'H' and then click 'Relations'</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '18, 12:54</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-63650" class="comments-container">
&#10;</div>
<div id="comment-tools-63650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63650-form-container" class="comment-form-container">
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

