+++
type = "question"
title = "Overpass turbo regular expression with [] choice"
description = '''I&#x27;m trying to find peaks in an area where the elevation contains other characters than numbers and the decimal point. I started with the non-negated regexp to test and got quite far:   [out:csv(name,ele)];  area[name=&quot;Plzeň&quot;];  node(area)[natural=peak][ele][&quot;ele&quot;~&quot;^[[:digit:]]+$&quot;];  out;  But I can&#x27;...'''
date = "2019-12-30T18:35:00Z"
lastmod = "2019-12-31T08:43:00Z"
weight = 72289
keywords = [ "regexp", "overpass-turbo", "overpass" ]
aliases = [ "/questions/72289" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass turbo regular expression with \[\] choice](/questions/72289/overpass-turbo-regular-expression-with-choice)

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
<span id="post-72289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72289-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to find peaks in an area where the elevation contains other characters than numbers and the decimal point. I started with the non-negated regexp to test and got <a href="https://overpass-turbo.eu/s/Plv">quite far</a>: <code> [out:csv(name,ele)]; area[name="Plzeň"]; node(area)[natural=peak][ele]["ele"~"^[[:digit:]]+$"]; out; </code> But I can't find out how to add the decimal point to the regexp. The <a href="https://overpass-turbo.eu/">obvious thing</a> doesn't work: <code> [out:csv(name,ele)]; area[name="Plzeň"]; node(area)[natural=peak][ele]["ele"~"^[[[:digit:]]\.]+$"]; out; </code> How to do that? Does Overpass QL not support []s? Or am I just missing something? (The area specified does contain peaks with both decimal point and without.) Note: I could probably do <a href="https://overpass-turbo.eu/s/Plw">this</a>, although imperfect, but I'm still curious about how to do it properly.</p>
<p>Edit - examples of what I want to match: ele=123 ele=1.234</p>
<p>Examples of what I don't want to match: ele=123. ele=123m ele=123.45 m</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-regexp" rel="tag" title="see questions tagged &#39;regexp&#39;">regexp</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '19, 18:35</strong></p>
<img src="https://secure.gravatar.com/avatar/87a3753fcb288d735cda25a2806f2dd8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="V0174&#39;s gravatar image" />
<p><span>V0174</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="V0174 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Dec '19, 08:22</strong> </span></p>
</div>
</div>
<div id="comments-container-72289" class="comments-container">
<span id="72291"></span>
<div id="comment-72291" class="comment">
<div id="post-72291-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Can you put a couple examples in your text, of what you do want to match and what you don't want to match? I don't think I fully understand what you want, but I think <code>["ele"~"[0-9.]+"]</code> does the same thing as your queries.</p>
</div>
<div id="comment-72291-info" class="comment-info">
<span class="comment-age">(30 Dec '19, 23:05)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="72296"></span>
<div id="comment-72296" class="comment">
<div id="post-72296-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that helped me to find the problem - dot should not be escaped inside of square brackets in Overpass QL.</p>
</div>
<div id="comment-72296-info" class="comment-info">
<span class="comment-age">(31 Dec '19, 08:43)</span> <span class="comment-user userinfo">V0174</span>
</div>
</div>
</div>
<div id="comment-tools-72289" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72289-form-container" class="comment-form-container">
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

<span id="72295"></span>

<div id="answer-container-72295" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72295-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK, thanks to maxerickson helping me to got to the right path, it seems it was a regex issue - dot inside of [] [doesn't need to be escaped]<a href="https://stackoverflow.com/questions/19976018/does-a-dot-have-to-be-escaped-in-a-character-class-square-brackets-of-a-regula">1</a>. I would expect that it'd work with escaping too, but that's Overpass.</p>
<hr />
<p><a href="https://overpass-turbo.eu/s/PlW">Working example</a></p>
<p>An improved example of what I wanted to do - <a href="https://overpass-turbo.eu/s/PlX">list of peaks with potentially wrong elevation in France</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Dec '19, 08:40</strong></p>
<img src="https://secure.gravatar.com/avatar/87a3753fcb288d735cda25a2806f2dd8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="V0174&#39;s gravatar image" />
<p><span>V0174</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="V0174 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Dec '19, 08:41</strong> </span></p>
</div>
</div>
<div id="comments-container-72295" class="comments-container">
&#10;</div>
<div id="comment-tools-72295" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72295-form-container" class="comment-form-container">
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

