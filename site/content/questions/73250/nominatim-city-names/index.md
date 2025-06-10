+++
type = "question"
title = "nominatim city names"
description = '''nominatim city names https://nominatim.openstreetmap.org/reverse gives me an xml with the city name of the location. In Bulgary the name is in correct Cyrillic characters but, unfortunately, de greek cities come in latin characters. Why? latin characters nominatim'''
date = "2020-02-26T23:47:00Z"
lastmod = "2020-03-01T22:11:00Z"
weight = 73250
keywords = [ "latin", "characters" ]
aliases = [ "/questions/73250" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [nominatim city names](/questions/73250/nominatim-city-names)

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
<span id="post-73250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73250-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>nominatim city names</p>
<p><a href="https://nominatim.openstreetmap.org/reverse">https://nominatim.openstreetmap.org/reverse</a> gives me an xml with the city name of the location. In Bulgary the name is in correct Cyrillic characters but, unfortunately, de greek cities come in latin characters. Why?</p>
<p>latin characters nominatim</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latin" rel="tag" title="see questions tagged &#39;latin&#39;">latin</span> <span class="post-tag tag-link-characters" rel="tag" title="see questions tagged &#39;characters&#39;">characters</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '20, 23:47</strong></p>
<img src="https://secure.gravatar.com/avatar/84b32bf3588a1c168afddd9ba46e5d1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nestos&#39;s gravatar image" />
<p><span>nestos</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nestos has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73250" class="comments-container">
&#10;</div>
<div id="comment-tools-73250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73250-form-container" class="comment-form-container">
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

<span id="73254"></span>

<div id="answer-container-73254" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73254-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do you query from the browser? If so, nominatim takes your browsers accept-language header and tries to serve that. So you have to change your browsers header to "el" or use the accept-language query param, e.g.:</p>
<p><a href="https://nominatim.openstreetmap.org/reverse.php?lat=37.98412&amp;lon=23.72831&amp;zoom=10&amp;format=xml&amp;accept-language=el">https://nominatim.openstreetmap.org/reverse.php?lat=37.98412&amp;lon=23.72831&amp;zoom=10&amp;format=xml&amp;accept-language=el</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '20, 07:13</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '20, 10:41</strong> </span></p>
</div>
</div>
<div id="comments-container-73254" class="comments-container">
&#10;</div>
<div id="comment-tools-73254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73254-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73300"></span>

<div id="answer-container-73300" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73300-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, I query from a c# program. I discoverd that the lager cities always come in latin (exonym), but small villages in local name and characters (endonym). But &amp;accept-language=el works for all! Thanks a lot!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '20, 20:06</strong></p>
<img src="https://secure.gravatar.com/avatar/84b32bf3588a1c168afddd9ba46e5d1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nestos&#39;s gravatar image" />
<p><span>nestos</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nestos has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73300" class="comments-container">
<span id="73301"></span>
<div id="comment-73301" class="comment">
<div id="post-73301-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For smaller cities and villages you normally don't have names in other languages in the data that's why the original is returned. As your C# program probably did not a include an accept language header, you'll have to add that either as a header or as a query param to get the desired language for larger places and cities where serveral options are present in the data.</p>
</div>
<div id="comment-73301-info" class="comment-info">
<span class="comment-age">(01 Mar '20, 22:11)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-73300" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73300-form-container" class="comment-form-container">
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

