+++
type = "question"
title = "overpass api : very slow process"
description = '''Hi to all, I feel overpass API is very very slow.  http://overpass-api.de/api/interpreter?data=[out:json];way%28around:5000,13.0236291,%2080.2652704%29;out;node%28around:5000,13.0236291,%2080.2652704%29[%27addr:street%27];out%20; I was setup in my system, but still very slow in my local server too. ...'''
date = "2016-02-03T12:42:00Z"
lastmod = "2016-02-04T16:32:00Z"
weight = 47863
keywords = [ "overpassapi", "overpass" ]
aliases = [ "/questions/47863" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [overpass api : very slow process](/questions/47863/overpass-api-very-slow-process)

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
<span id="post-47863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47863-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to all,</p>
<p>I feel overpass API is very very slow.</p>
<p><a href="http://overpass-api.de/api/interpreter?data=%5Bout:json%5D;way%28around:5000,13.0236291,%2080.2652704%29;out;node%28around:5000,13.0236291,%2080.2652704%29%5B%27addr:street%27%5D;out%20;">http://overpass-api.de/api/interpreter?data=[out:json];way%28around:5000,13.0236291,%2080.2652704%29;out;node%28around:5000,13.0236291,%2080.2652704%29[%27addr:street%27];out%20;</a></p>
<p>I was setup in my system, but still very slow in my local server too. Any suggestion to improve speed &amp; performance ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Feb '16, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Feb '16, 09:02</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-47863" class="comments-container">
<span id="47876"></span>
<div id="comment-47876" class="comment">
<div id="post-47876-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please clarify what do you want your query to return.</p>
</div>
<div id="comment-47876-info" class="comment-info">
<span class="comment-age">(03 Feb '16, 17:05)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="47889"></span>
<div id="comment-47889" class="comment">
<div id="post-47889-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That query returns a lot of data (9+ MB). What is your goal? Maybe try with a smaller <code>around</code> radius?</p>
</div>
<div id="comment-47889-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 08:25)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
<span id="47903"></span>
<div id="comment-47903" class="comment">
<div id="post-47903-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/268/rm87">@RM87</a>: I want to get all streets from a region/radius. If i get from node only, i got very few data only. So I want to retrieve ways too from that region (from ways also i can get some living streets).</p>
<p><a href="https://help.openstreetmap.org/users/191/ivanatora">@ivanatora</a>: Yes. If i give around 500 meter, then its working little bit better. But I need to get all streets in a small town or around 5kms.</p>
</div>
<div id="comment-47903-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 11:13)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
</div>
<div id="comment-tools-47863" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47863-form-container" class="comment-form-container">
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

<span id="47916"></span>

<div id="answer-container-47916" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47916-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your current query returns all ways within 5km radius + nodes tagged addr:street within 5km radius.</p>
<p><a href="http://overpass-turbo.eu/s/ebQ">This query</a> would get you only the streets resulting in ~2MB of data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '16, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RM87 has 20 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-47916" class="comments-container">
&#10;</div>
<div id="comment-tools-47916" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47916-form-container" class="comment-form-container">
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

