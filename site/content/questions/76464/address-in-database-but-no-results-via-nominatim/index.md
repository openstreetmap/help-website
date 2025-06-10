+++
type = "question"
title = "Address in database but no results via Nominatim"
description = '''I am not getting results when running the following query https://nominatim.openstreetmap.org/search?street=126+Sunfish+Drive&amp;amp;city=Moorsville&amp;amp;state=nc&amp;amp;postalCode=28117&amp;amp;format=geocodejson&amp;amp;addressdetails=1 But I can see the address is in the database https://www.openstreetmap.org/n...'''
date = "2020-09-05T19:30:00Z"
lastmod = "2020-09-06T15:24:00Z"
weight = 76464
keywords = [ "nominatim", "accuracy" ]
aliases = [ "/questions/76464" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Address in database but no results via Nominatim](/questions/76464/address-in-database-but-no-results-via-nominatim)

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
<span id="post-76464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76464-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am not getting results when running the following query</p>
<p><a href="https://nominatim.openstreetmap.org/search?street=126+Sunfish+Drive&amp;city=Moorsville&amp;state=nc&amp;postalCode=28117&amp;format=geocodejson&amp;addressdetails=1">https://nominatim.openstreetmap.org/search?street=126+Sunfish+Drive&amp;city=Moorsville&amp;state=nc&amp;postalCode=28117&amp;format=geocodejson&amp;addressdetails=1</a></p>
<p>But I can see the address is in the database</p>
<p><a href="https://www.openstreetmap.org/node/4059128182">https://www.openstreetmap.org/node/4059128182</a></p>
<p>Any idea why the address is not being found when I query it via Nominatim? Anything I can do to solve the issue?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-accuracy" rel="tag" title="see questions tagged &#39;accuracy&#39;">accuracy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '20, 19:30</strong></p>
<img src="https://secure.gravatar.com/avatar/fe6b19c8efa5f765b22f74a610c85678?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xpro6000&#39;s gravatar image" />
<p><span>xpro6000</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xpro6000 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76464" class="comments-container">
&#10;</div>
<div id="comment-tools-76464" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76464-form-container" class="comment-form-container">
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

<span id="76467"></span>

<div id="answer-container-76467" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76467-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Firstly, your query says "Moorsville" but the city is called "Mooresville".</p>
<p>Even that doesn't fix it though because the node lies outside the city boundary of Mooresville, something which Nominatim apparently considers more authoritative than the node's <code>addr:city</code> tag. If you leave out the <code>city=Mooresville</code> from your query then the node is found.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '20, 22:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Sep '20, 22:11</strong> </span></p>
</div>
</div>
<div id="comments-container-76467" class="comments-container">
<span id="76472"></span>
<div id="comment-76472" class="comment">
<div id="post-76472-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are right, leaving out the city works. However, I'm getting different results from my local Nominatim server which I installed about 3 weeks ago, compared to nominatim.openstreetmap.org</p>
<p>from openstreetmap I get this result <a href="https://pastebin.com/p24RYeGG">https://pastebin.com/p24RYeGG</a> which is listing the county correctly</p>
<p>but from my local install I see <a href="https://pastebin.com/cCmbHgfp">https://pastebin.com/cCmbHgfp</a> which lists county as "Halifax County" which is incorrect.</p>
<p>Any idea why I am getting different results?</p>
</div>
<div id="comment-76472-info" class="comment-info">
<span class="comment-age">(06 Sep '20, 04:12)</span> <span class="comment-user userinfo">xpro6000</span>
</div>
</div>
<span id="76478"></span>
<div id="comment-76478" class="comment">
<div id="post-76478-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>nominatim.openstreetmap.org database gets fully reindexed only once or twice per year so your installation is likely more up-to-date. With incremental (minutely) updates and regular changes to the index and search logic there will never be a 100% match between installations.</p>
</div>
<div id="comment-76478-info" class="comment-info">
<span class="comment-age">(06 Sep '20, 15:24)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-76467" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76467-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76468"></span>

<div id="answer-container-76468" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76468-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A search for "126 Sunfish Drive" by itself appears to show it.</p>
<p>Nominatim <a href="https://nominatim.openstreetmap.org/ui/details.html?osmtype=N&amp;osmid=4059128182&amp;class=place">thinks</a> the address is in Mount Mourne presumably because it is outside of the <a href="https://nominatim.openstreetmap.org/ui/details.html?osmtype=N&amp;osmid=4059128182&amp;class=place">Mooresville town relation</a>. Changing the border probably isn't a good idea unless you know it is out of date.</p>
<p>The Nominatim <a href="https://wiki.openstreetmap.org/wiki/Nominatim/FAQ#of_a_Street_.2F_City_.2F_County">FAQ</a> suggests adding an <a href="https://wiki.openstreetmap.org/wiki/Key:is_in"><code>is_in</code></a> tag but if that doesn't work the best alternative I can suggest is a rather unhelpful "be less specific".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '20, 22:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-76468" class="comments-container">
&#10;</div>
<div id="comment-tools-76468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76468-form-container" class="comment-form-container">
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

