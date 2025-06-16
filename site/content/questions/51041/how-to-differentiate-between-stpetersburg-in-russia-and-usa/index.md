+++
type = "question"
title = "how to differentiate between ST.PETERSBURG in Russia and USA."
description = '''how to differentiate between ST.PETERSBURG in Russia and USA, I just want to use the name.'''
date = "2016-07-21T17:00:00Z"
lastmod = "2016-07-21T20:56:00Z"
weight = 51041
keywords = [ "st.petersburg" ]
aliases = [ "/questions/51041" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to differentiate between ST.PETERSBURG in Russia and USA.](/questions/51041/how-to-differentiate-between-stpetersburg-in-russia-and-usa)

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
<span id="post-51041-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51041-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51041-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>how to differentiate between ST.PETERSBURG in Russia and USA, I just want to use the name.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-st.petersburg" rel="tag" title="see questions tagged &#39;st.petersburg&#39;">st.petersburg</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '16, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/0782882fa7cf398c854e163391c46d58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srikanth18&#39;s gravatar image" />
<p><span>srikanth18</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srikanth18 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51041" class="comments-container">
<span id="51048"></span>
<div id="comment-51048" class="comment">
<div id="post-51048-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>about which website/service/whatever is your question? What are you using and doing?</p>
</div>
<div id="comment-51048-info" class="comment-info">
<span class="comment-age">(21 Jul '16, 20:56)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51041" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51041-form-container" class="comment-form-container">
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

<span id="51043"></span>

<div id="answer-container-51043" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51043-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The response from Nominatim has the <code>importance</code> field - essentially the "bigger" the place, the higher it scores. The Russian Petersburg is rated higher than the others.</p>
<p>Also, if you're expecting results to come <em>primarily</em> from a specific area, you set the <code>viewbox</code> request field; or even set <code>bounded=1</code> if you <em>only</em> want your results to come from the viewbox area.</p>
<p>As for detecting "which of the Petersburgs is where": you can check the coordinates, which is not very precise.</p>
<p>Alternatively, you can pass the request field <code>addressdetails=1</code>, which will give you a hierarchy - checking the <code>address.country_code</code> might be sufficient here.</p>
<p>See the documentation at <a href="https://wiki.openstreetmap.org/wiki/Nominatim">https://wiki.openstreetmap.org/wiki/Nominatim</a> for more options.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '16, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jul '16, 17:11</strong> </span></p>
</div>
</div>
<div id="comments-container-51043" class="comments-container">
&#10;</div>
<div id="comment-tools-51043" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51043-form-container" class="comment-form-container">
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

