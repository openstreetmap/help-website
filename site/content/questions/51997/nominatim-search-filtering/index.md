+++
type = "question"
title = "Nominatim search filtering"
description = '''I have task - finding coordinate for address, and i always know city for address. How i can filter search for one city? Documentation indicated request parameters city and country ( http://wiki.openstreetmap.org/wiki/Nominatim#Parameters ), but when i use it, result of search does not depend on it. ...'''
date = "2016-09-12T08:29:00Z"
lastmod = "2016-09-14T00:38:00Z"
weight = 51997
keywords = [ "nominatim" ]
aliases = [ "/questions/51997" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim search filtering](/questions/51997/nominatim-search-filtering)

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
<span id="post-51997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51997-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have task - finding coordinate for address, and i always know city for address.</p>
<p>How i can filter search for one city? Documentation indicated request parameters city and country ( <a href="http://wiki.openstreetmap.org/wiki/Nominatim#Parameters">http://wiki.openstreetmap.org/wiki/Nominatim#Parameters</a> ), but when i use it, result of search does not depend on it.</p>
<p>For example: <a href="http://nominatim.openstreetmap.org/search?q=tower&amp;city=London&amp;format=json">http://nominatim.openstreetmap.org/search?q=tower&amp;city=London&amp;format=json</a></p>
<p>Where am I wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Sep '16, 08:29</strong></p>
<img src="https://secure.gravatar.com/avatar/964bd7d4d70a8bd28b222626ee69c6c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vnk&#39;s gravatar image" />
<p><span>vnk</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vnk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Sep '16, 08:32</strong> </span></p>
</div>
</div>
<div id="comments-container-51997" class="comments-container">
&#10;</div>
<div id="comment-tools-51997" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51997-form-container" class="comment-form-container">
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

<span id="52000"></span>

<div id="answer-container-52000" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52000-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="vnk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The documentation also says "DO NOT COMBINE WITH q=&lt;query&gt; PARAMETER." :)</p>
<p>This should work:</p>
<p><a href="http://nominatim.openstreetmap.org/search?street=tower&amp;city=London&amp;countrycodes=GB&amp;format=json">http://nominatim.openstreetmap.org/search?street=tower&amp;city=London&amp;countrycodes=GB&amp;format=json</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '16, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-52000" class="comments-container">
<span id="52002"></span>
<div id="comment-52002" class="comment">
<div id="post-52002-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oops.. Thanks, I didn't notice..</p>
<p>But is there a way to filter the results not strictly comply with the required city?</p>
<p>For example <a href="http://nominatim.openstreetmap.org/search?street=place&amp;city=Washington&amp;countrycodes=US&amp;format=html">http://nominatim.openstreetmap.org/search?street=place&amp;city=Washington&amp;countrycodes=US&amp;format=html</a></p>
<p>return results from more then one city</p>
</div>
<div id="comment-52002-info" class="comment-info">
<span class="comment-age">(12 Sep '16, 12:21)</span> <span class="comment-user userinfo">vnk</span>
</div>
</div>
<span id="52004"></span>
<div id="comment-52004" class="comment">
<div id="post-52004-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm afraid not. Your best alternative is to either set &amp;viewbox and &amp;bounded=1 (of course that requires you know the location and size of the city first). Or look at all results to see how close they are to the desired city.</p>
</div>
<div id="comment-52004-info" class="comment-info">
<span class="comment-age">(12 Sep '16, 13:49)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="52019"></span>
<div id="comment-52019" class="comment">
<div id="post-52019-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And new problem, I don't understand how it works or it does not work properly?</p>
<p>viewbox without restrict: <a href="http://nominatim.openstreetmap.org/search?street=place&amp;city=Washington&amp;countrycodes=US&amp;viewbox=44.86366%2C-127.01294%2C50.05714%2C-111.41235&amp;format=html">http://nominatim.openstreetmap.org/search?street=place&amp;city=Washington&amp;countrycodes=US&amp;viewbox=44.86366%2C-127.01294%2C50.05714%2C-111.41235&amp;format=html</a> Four results, but first not in viewbox.</p>
<p>restrict query with bounded=1 <a href="http://nominatim.openstreetmap.org/search?street=place&amp;city=Washington&amp;countrycodes=US&amp;viewbox=44.86366%2C-127.01294%2C50.05714%2C-111.41235&amp;bounded=1&amp;format=html">http://nominatim.openstreetmap.org/search?street=place&amp;city=Washington&amp;countrycodes=US&amp;viewbox=44.86366%2C-127.01294%2C50.05714%2C-111.41235&amp;bounded=1&amp;format=html</a> and nothing result :(</p>
<p>And same behavior when i use query: <a href="http://nominatim.openstreetmap.org/search?q=place%2C+Washington&amp;viewbox=44.86366%2C-127.01294%2C50.05714%2C-111.41235&amp;bounded=1&amp;format=html">http://nominatim.openstreetmap.org/search?q=place%2C+Washington&amp;viewbox=44.86366%2C-127.01294%2C50.05714%2C-111.41235&amp;bounded=1&amp;format=html</a> in this request search results wihout bounded working good, but some other requests without bounded restrict return results also with data out of the viewbox :(</p>
</div>
<div id="comment-52019-info" class="comment-info">
<span class="comment-age">(13 Sep '16, 01:12)</span> <span class="comment-user userinfo">vnk</span>
</div>
</div>
<span id="52038"></span>
<div id="comment-52038" class="comment">
<div id="post-52038-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You mixed up latitude and longitude here. The viewbox parameter requires &lt;left&gt;,&lt;top&gt;,&lt;right&gt;,&lt;bottom&gt;. <a href="http://nominatim.openstreetmap.org/search?street=place&amp;city=Washington&amp;countrycodes=US&amp;viewbox=-127.012940,50.057140,-111.412350,44.863660&amp;bounded=1">http://nominatim.openstreetmap.org/search?street=place&amp;city=Washington&amp;countrycodes=US&amp;viewbox=-127.012940,50.057140,-111.412350,44.863660&amp;bounded=1</a></p>
</div>
<div id="comment-52038-info" class="comment-info">
<span class="comment-age">(13 Sep '16, 12:57)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="52039"></span>
<div id="comment-52039" class="comment">
<div id="post-52039-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Actually the user interface on that page is misleading. We'll change that now <a href="https://trac.openstreetmap.org/ticket/5422">https://trac.openstreetmap.org/ticket/5422</a></p>
</div>
<div id="comment-52039-info" class="comment-info">
<span class="comment-age">(13 Sep '16, 13:22)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="52040"></span>
<div id="comment-52040" class="comment not_top_scorer">
<div id="post-52040-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great! Big thanks!</p>
</div>
<div id="comment-52040-info" class="comment-info">
<span class="comment-age">(14 Sep '16, 00:38)</span> <span class="comment-user userinfo">vnk</span>
</div>
</div>
</div>
<div id="comment-tools-52000" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-52000-form-container" class="comment-form-container">
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

