+++
type = "question"
title = "Nominatim results priority."
description = '''Hello, I&#x27;m not sure if there is an issue with Nominatim or the tagging with these search results(the latter is a little poor) that have been reported to me, so I&#x27;m going to ask here before reporting or improving. Search for   &quot;Trelissick&quot; and you find a building (small residential cottage) in Porthl...'''
date = "2014-07-23T19:05:00Z"
lastmod = "2014-07-25T13:26:00Z"
weight = 35113
keywords = [ "search", "nominatim", "tagging" ]
aliases = [ "/questions/35113" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim results priority.](/questions/35113/nominatim-results-priority)

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
<span id="post-35113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35113-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm not sure if there is an issue with Nominatim or the tagging with these search results(the latter is a little poor) that have been reported to me, so I'm going to ask here before reporting or improving.</p>
<p>Search for</p>
<ul>
<li>"<a href="http://www.openstreetmap.org/search?query=Trelissick#map=16/50.0822/-5.3155">Trelissick</a>" and you find a building (small residential cottage) in Porthleven.</li>
<li>"<a href="http://www.openstreetmap.org/search?query=Trelissick%2C%20Coombe#map=14/50.2169/-5.0227">Trelissick, Coombe</a>" you find many things relating to the NT property, probably what you were looking for.</li>
<li>"<a href="http://www.openstreetmap.org/search?query=Trelissick%20Gardens#map=14/50.2169/-5.0227">Trelissick Gardens</a>" or "<a href="http://www.openstreetmap.org/search?query=Trelissick%20House#map=14/50.2169/-5.0227">Trelissick House</a>" and you find those objects which are NT properties.</li>
<li>"<a href="http://www.openstreetmap.org/search?query=Trelissick%2C%20Cornwall#map=16/50.0822/-5.3155">Trelissick, Cornwall</a>" you get the residential building in Porthleven again, although the NT objects are equally in Cornwall.</li>
</ul>
<p>I'm wondering if leisure=garden is not "of interest" enough and a relation object with tourism=attraction + name="Trelissick House and Gardens" would be better.</p>
<p>When I do this, I'll also want to get rid of all the (descriptions) in the name values and replace them with access or operator tags as appropriate.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '14, 19:05</strong></p>
<img src="https://secure.gravatar.com/avatar/f846f21cfbcf60a35e1f69c2cc74df77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LivingWithDragons&#39;s gravatar image" />
<p><span>LivingWithDr...</span><br />
<span class="score" title="524 reputation points">524</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LivingWithDragons has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-35113" class="comments-container">
&#10;</div>
<div id="comment-tools-35113" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35113-form-container" class="comment-form-container">
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

<span id="35177"></span>

<div id="answer-container-35177" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35177-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is happening because nominatim always shows exact matches before partial matches regardless of the relative importance of the different features. It is a known issue but very hard to resolve.</p>
<p>Within that the importance of a feature is mostly calculated via any wikipedia links. In general adding appropriate wikipedia links to the feature will resolve most problem - although not in this case due to the exact match issue.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '14, 13:26</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-35177" class="comments-container">
&#10;</div>
<div id="comment-tools-35177" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35177-form-container" class="comment-form-container">
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

