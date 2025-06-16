+++
type = "question"
title = "I added some road name and are not found on nominatim"
description = '''After 6 days since I inserted the street names I still can&#x27;t search for this street information. I visited this page https://wiki.openstreetmap.org/wiki/Nominatim/FAQ  My data is still missing and it&#x27;s been several days Check the date of the latest data refresh at the top of http://nominatim.openstre...'''
date = "2011-01-30T20:56:00Z"
lastmod = "2011-01-31T04:19:00Z"
weight = 2572
keywords = [ "nominatim" ]
aliases = [ "/questions/2572" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [I added some road name and are not found on nominatim](/questions/2572/i-added-some-road-name-and-are-not-found-on-nominatim)

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
<span id="post-2572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2572-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After 6 days since I inserted the street names I still can't search for this street information. I visited this page <a href="https://wiki.openstreetmap.org/wiki/Nominatim/FAQ"></a><a href="https://wiki.openstreetmap.org/wiki/Nominatim/FAQ"></a><a href="https://wiki.openstreetmap.org/wiki/Nominatim/FAQ">https://wiki.openstreetmap.org/wiki/Nominatim/FAQ</a></p>
<blockquote>
My data is still missing and it's been several days Check the date of the latest data refresh at the top of <a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a> as there may be a delay with the refresh. If it's up to date, you can verify if your data has been loaded and force it to be indexed using the following url <a href="http://nominatim.openstreetmap.org/details?osmtype=%5BN%7CW%7CR%5D&amp;osmid=">http://nominatim.openstreetmap.org/details?osmtype=[N|W|R]&amp;osmid=</a>&lt;idnumber&gt; If no item is found then your data has not been loaded, please report the problem and the osm id number of the feature using <a href="http://trac.openstreetmap.org">trac.openstreetmap.org</a>.
</blockquote>
<p>I tried to use this information but got stuck. what information do I enter in this parameters ?osmtype=[N|W|R]&amp;osmid=&lt;idnumber&gt;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '11, 20:56</strong></p>
<img src="https://secure.gravatar.com/avatar/7277cb62366f65edf6965af6dcdd5458?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trumbun&#39;s gravatar image" />
<p><span>Trumbun</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trumbun has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2572" class="comments-container">
&#10;</div>
<div id="comment-tools-2572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2572-form-container" class="comment-form-container">
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

<span id="2576"></span>

<div id="answer-container-2576" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2576-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Trumbun has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The [N|W|R] is wanting N for node, or W for way, or R for relation (depending on the type of thing you are searching for). The idnumber is the ID of the thing you are checking.</p>
<p>Suppose I added a new way, and the ID of that way is 28523243. Thus I would use the URL:</p>
<p><a href="http://nominatim.openstreetmap.org/details?osmtype=W&amp;osmid=28523243"></a><a href="http://nominatim.openstreetmap.org/details?osmtype=W&amp;osmid=28523243"></a><a href="http://nominatim.openstreetmap.org/details?osmtype=W&amp;osmid=28523243">http://nominatim.openstreetmap.org/details?osmtype=W&amp;osmid=28523243</a></p>
<p>(Alas I get an error about being unable to connect to the database for that URL, but you get the idea.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '11, 04:17</strong></p>
<img src="https://secure.gravatar.com/avatar/f075add936ab95d2d368f2e48f5ddc22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ebenezer&#39;s gravatar image" />
<p><span>Ebenezer</span><br />
<span class="score" title="948 reputation points">948</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ebenezer has 2 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-2576" class="comments-container">
<span id="2577"></span>
<div id="comment-2577" class="comment">
<div id="post-2577-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The talk page for Nominatim seems to suggest that it is not currently updating. <a href="https://wiki.openstreetmap.org/wiki/Talk:Nominatim#nominatim_not_up_to_date_.28january_2011.29">https://wiki.openstreetmap.org/wiki/Talk:Nominatim#nominatim_not_up_to_date_.28january_2011.29</a></p>
</div>
<div id="comment-2577-info" class="comment-info">
<span class="comment-age">(31 Jan '11, 04:19)</span> <span class="comment-user userinfo">Ebenezer</span>
</div>
</div>
</div>
<div id="comment-tools-2576" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2576-form-container" class="comment-form-container">
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

