+++
type = "question"
title = "Empty response for few UK postal codes"
description = '''Most of the places in UK have common postal prefix. Example: (EX23, EX23 0AA, EX23 0AB,...), (DN15, DN15 0AA,...),.. When queried with common postal prefix like this, I am getting empty response. Whereas, when queried with their sub-categories like this, I am getting accurate results.  Out of nearly...'''
date = "2018-11-16T12:10:00Z"
lastmod = "2018-11-16T17:46:00Z"
weight = 66799
keywords = [ "gb" ]
aliases = [ "/questions/66799" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Empty response for few UK postal codes](/questions/66799/empty-response-for-few-uk-postal-codes)

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
<span id="post-66799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66799-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Most of the places in UK have <strong>common postal prefix</strong>. Example: (EX23, EX23 0AA, EX23 0AB,...), (DN15, DN15 0AA,...),..</p>
<p>When queried with common postal prefix like <a href="https://nominatim.openstreetmap.org/search?format=json&amp;country=United%20Kingdom&amp;state=Cornwall&amp;postalcode=EX23">this</a>, I am getting empty response. Whereas, when queried with their sub-categories like <a href="https://nominatim.openstreetmap.org/search?format=json&amp;country=United%20Kingdom&amp;state=Cornwall&amp;postalcode=EX23%200AB">this</a>, I am getting accurate results. Out of nearly 1500 UK postal codes, 300 suffer from this problem. Can someone please help me in this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gb" rel="tag" title="see questions tagged &#39;gb&#39;">gb</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '18, 12:10</strong></p>
<img src="https://secure.gravatar.com/avatar/455af0955423b60e9fa046ac3f1b046e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Priyalakshmi%20Sundaravel&#39;s gravatar image" />
<p><span>Priyalakshmi...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Priyalakshmi Sundaravel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '18, 12:17</strong> </span></p>
</div>
</div>
<div id="comments-container-66799" class="comments-container">
&#10;</div>
<div id="comment-tools-66799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66799-form-container" class="comment-form-container">
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

<span id="66800"></span>

<div id="answer-container-66800" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66800-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It probably means that the postcodes aren't mapped in OSM. You can download postcode centroids for free from the Codepoint Open dataset at <a href="https://www.ordnancesurvey.co.uk/business-and-government/products/finder.html">https://www.ordnancesurvey.co.uk/business-and-government/products/finder.html</a> which will be more complete than OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '18, 14:46</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-66800" class="comments-container">
&#10;</div>
<div id="comment-tools-66800" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66800-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66801"></span>

<div id="answer-container-66801" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66801-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In theory the first half of the postcode won't be mapped on anything in OpenStreetMap, as they aren't postcodes, though trying a postcode prefix local to me I find nominatim is finding it on a place node where someone has stuck a postal_code tag on containing it which I'll be removing now I've seen it, as the CO15 covers much more than just Jaywick <a href="https://www.openstreetmap.org/node/291718149">https://www.openstreetmap.org/node/291718149</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '18, 17:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-66801" class="comments-container">
&#10;</div>
<div id="comment-tools-66801" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66801-form-container" class="comment-form-container">
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

