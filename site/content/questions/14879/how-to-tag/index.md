+++
type = "question"
title = "How to tag"
description = '''How to tag  A building with 3 floors and housenumbers depending on the floors e.g. first floor= 24 a, 24 b etc. second floor 25 a, b etc. An accountant wich is a tax advisor, too. A building wich has a shop in the ground floor and a dentist in the first floor.  Last question: How can i copy urls int...'''
date = "2012-08-07T09:48:00Z"
lastmod = "2012-08-07T23:26:00Z"
weight = 14879
keywords = [ "tags" ]
aliases = [ "/questions/14879" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag](/questions/14879/how-to-tag)

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
<span id="post-14879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14879-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How to tag</p>
<ol>
<li>A building with 3 floors and housenumbers depending on the floors e.g. first floor= 24 a, 24 b etc. second floor 25 a, b etc.</li>
<li>An accountant wich is a tax advisor, too.</li>
<li>A building wich has a shop in the ground floor and a dentist in the first floor.</li>
</ol>
<p>Last question: How can i copy urls into JOSM (Strg C/V isn't working ;)</p>
<p>Thank you Hno2</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '12, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0c43c2c53ad9723aa6598d37579b2bbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hno2&#39;s gravatar image" />
<p><span>hno2</span><br />
<span class="score" title="66 reputation points">66</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hno2 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14879" class="comments-container">
&#10;</div>
<div id="comment-tools-14879" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14879-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="14881"></span>

<div id="answer-container-14881" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14881-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li><p>Use the key 'level=x' (see <a href="https://wiki.openstreetmap.org/wiki/Level)">https://wiki.openstreetmap.org/wiki/Level)</a> The level=0 represents the ground floor (for historical reasons, we use British English in tags). Then, in your case, I would create 3 nodes, one per address, attached on the building way (my preference is to put them on the front side where main entrance(s) is(are)). Then add the tags for individual addresses and the corresponding floor with 'level'.</p></li>
<li><p>see answers on <a href="/questions/13483/how-to-tag-hr-block-a-tax-preparation-service">this identical question</a></p></li>
<li><p>again, create two elements e.g. two nodes inside the building area where you add the appropriate 'amenity', 'shop' or 'whatever' keys plus the 'level' for each of them.</p></li>
<li><p>if by "urls", you mean permalink when downloading a zone for edit, open the 'download' dialog then select the tab 'Bounding Box' and paste the url there.</p></li>
</ol>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '12, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Aug '12, 12:54</strong> </span></p>
</div>
</div>
<div id="comments-container-14881" class="comments-container">
<span id="14884"></span>
<div id="comment-14884" class="comment">
<div id="post-14884-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Re (2), <a href="/questions/13483/how-to-tag-hr-block-a-tax-preparation-service">this previous question</a> asked about tax preparation services; maybe it's related?</p>
</div>
<div id="comment-14884-info" class="comment-info">
<span class="comment-age">(07 Aug '12, 12:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="14893"></span>
<div id="comment-14893" class="comment">
<div id="post-14893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>With URL I mean websites wich belong to a building, a city etc. I can't simply copy it from my browser to JOSM.</p>
</div>
<div id="comment-14893-info" class="comment-info">
<span class="comment-age">(07 Aug '12, 16:04)</span> <span class="comment-user userinfo">hno2</span>
</div>
</div>
</div>
<div id="comment-tools-14881" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14881-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14901"></span>

<div id="answer-container-14901" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14901-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Personally when a building covers multiple address, unless they fit very well on the polygon, I always use a range, but then I live in a city (Montreal, Canada) where having 3 to 5 4-digit housenumbers on a small building is a common occurrence!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '12, 23:26</strong></p>
<img src="https://secure.gravatar.com/avatar/01d01832dff61a6bcf68913f1dc001bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Circeus&#39;s gravatar image" />
<p><span>Circeus</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Circeus has 2 accepted answers">7%</span></p>
</div>
</div>
<div id="comments-container-14901" class="comments-container">
&#10;</div>
<div id="comment-tools-14901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14901-form-container" class="comment-form-container">
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

