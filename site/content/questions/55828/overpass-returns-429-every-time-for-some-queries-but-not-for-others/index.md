+++
type = "question"
title = "Overpass returns 429 every time for some queries, but not for others"
description = '''I am trying to download streets from the Overpass API using a very simple Python script. This always worked just fine for me, until this morning when I started experiencing strange behavior. import requests url = &#x27;http://www.overpass-api.de/api/interpreter&#x27; timeout = 60 data = &#x27;[out:json][timeout:60...'''
date = "2017-04-24T18:08:00Z"
lastmod = "2020-11-30T16:30:00Z"
weight = 55828
keywords = [ "python", "overpass", "api", "server", "query" ]
aliases = [ "/questions/55828" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass returns 429 every time for some queries, but not for others](/questions/55828/overpass-returns-429-every-time-for-some-queries-but-not-for-others)

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
<span id="post-55828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55828-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to download streets from the Overpass API using a very simple Python script. This always worked just fine for me, until this morning when I started experiencing strange behavior.</p>
<pre><code>import requests
url = &#39;http://www.overpass-api.de/api/interpreter&#39;
timeout = 60
data = &#39;[out:json][timeout:60];(way[&quot;highway&quot;][&quot;area&quot;!~&quot;yes&quot;][&quot;highway&quot;!~&quot;cycleway|footway|path|pedestrian|steps|track|proposed|construction|bridleway|abandoned|platform|raceway|service&quot;][&quot;motor_vehicle&quot;!~&quot;no&quot;][&quot;motorcar&quot;!~&quot;no&quot;][&quot;access&quot;!~&quot;private&quot;][&quot;service&quot;!~&quot;parking|parking_aisle|driveway|private|emergency_access&quot;](poly:&quot;37.87539 -122.28873 37.87539 -122.26599 37.85736 -122.26599 37.85736 -122.28873 37.87539 -122.28873&quot;);&gt;;);out;&#39;</code></pre>
<p>When I post this request:</p>
<pre><code>response = requests.post(url, data=data, timeout=timeout)</code></pre>
<p>I receive status code 200 and the response data that I expect.</p>
<p>However, when I use a more complex polygon:</p>
<pre><code>url = &#39;http://www.overpass-api.de/api/interpreter&#39;
timeout = 60
data = &#39;[out:json][timeout:60];(way[&quot;highway&quot;][&quot;area&quot;!~&quot;yes&quot;][&quot;highway&quot;!~&quot;cycleway|footway|path|pedestrian|steps|track|proposed|construction|bridleway|abandoned|platform|raceway|service&quot;][&quot;motor_vehicle&quot;!~&quot;no&quot;][&quot;motorcar&quot;!~&quot;no&quot;][&quot;access&quot;!~&quot;private&quot;][&quot;service&quot;!~&quot;parking|parking_aisle|driveway|private|emergency_access&quot;](poly:&quot;37.82311 -122.25501 37.8232 -122.25503 37.82365 -122.25505 37.8241 -122.25503 37.82455 -122.25494 37.82499 -122.2548 37.82542 -122.2546 37.82582 -122.25435 37.82621 -122.25405 37.82657 -122.2537 37.8268 -122.25345 37.82692 -122.25333 37.82718 -122.25324 37.82738 -122.25318 37.8278 -122.25301 37.82821 -122.25279 37.8286 -122.25252 37.82896 -122.25221 37.8293 -122.25185 37.82961 -122.25145 37.82989 -122.25101 37.83014 -122.25057 37.8308 -122.24943 37.83084 -122.24941 37.8312 -122.24913 37.83129 -122.24905 37.83212 -122.24841 37.83239 -122.2482 37.83241 -122.24819 37.83245 -122.24816 37.8328 -122.24785 37.83313 -122.2475 37.83344 -122.24712 37.83371 -122.2467 37.83395 -122.24625 37.83415 -122.24577 37.83432 -122.24527 37.83445 -122.24475 37.83454 -122.24422 37.83458 -122.24369 37.83459 -122.24337 37.83468 -122.24304 37.83473 -122.24283 37.83476 -122.24268 37.83489 -122.24197 37.83491 -122.24182 37.83495 -122.24131 37.83496 -122.24115 37.83497 -122.24086 37.83498 -122.23985 37.83499 -122.23974 37.83501 -122.23956 37.83504 -122.23929 37.83506 -122.23923 37.83519 -122.23872 37.83528 -122.23821 37.83531 -122.23784 37.83535 -122.23772 37.83545 -122.23723 37.83548 -122.23703 37.83552 -122.2368 37.83555 -122.2366 37.83569 -122.23587 37.83574 -122.23562 37.83574 -122.23561 37.83597 -122.23434 37.83604 -122.23397 37.83645 -122.23263 37.83656 -122.23228 37.83684 -122.23138 37.83722 -122.23015 37.83736 -122.22962 37.83746 -122.22908 37.83752 -122.22853 37.83753 -122.22797 37.8375 -122.22742 37.83743 -122.22687 37.83731 -122.22633 37.83716 -122.22581 37.83696 -122.22531 37.83673 -122.22484 37.83646 -122.2244 37.83632 -122.22419 37.83591 -122.22358 37.8359 -122.22357 37.83586 -122.22351 37.83566 -122.22308 37.8356 -122.22298 37.83559 -122.22297 37.83558 -122.22295 37.83543 -122.22268 37.83543 -122.22268 37.83538 -122.22259 37.83537 -122.22257 37.83532 -122.22248 37.8353 -122.22243 37.83506 -122.22199 37.83505 -122.22198 37.83497 -122.22183 37.83472 -122.2214 37.83443 -122.221 37.83411 -122.22064 37.83377 -122.22032 37.8334 -122.22004 37.83301 -122.2198 37.83281 -122.21969 37.83227 -122.2194 37.83198 -122.21918 37.83161 -122.21891 37.83065 -122.21809 37.83065 -122.21809 37.83059 -122.21804 37.83052 -122.21798 37.8305 -122.21796 37.83041 -122.21789 37.83014 -122.21766 37.82981 -122.2174 37.82973 -122.21734 37.82963 -122.21728 37.8295 -122.21718 37.82943 -122.21713 37.82899 -122.21686 37.8287 -122.21671 37.82866 -122.21669 37.82838 -122.21654 37.82752 -122.21545 37.82743 -122.21535 37.8272 -122.21505 37.82719 -122.21504 37.82703 -122.21467 37.82687 -122.21431 37.8268 -122.21415 37.82674 -122.21404 37.82671 -122.21396 37.82664 -122.21379 37.82642 -122.21327 37.82615 -122.21279 37.82584 -122.21235 37.82575 -122.21223 37.82539 -122.21181 37.82501 -122.21145 37.825 -122.21145 37.82489 -122.21124 37.82476 -122.21101 37.8245 -122.21058 37.82373 -122.2093 37.82353 -122.20897 37.82349 -122.20889 37.82322 -122.20839 37.82315 -122.20826 37.82303 -122.20805 37.82262 -122.20727 37.82248 -122.20701 37.82223 -122.20657 37.82194 -122.20616 37.82162 -122.20579 37.82127 -122.20546 37.8209 -122.20517 37.82052 -122.20493 37.82011 -122.20474 37.81969 -122.2046 37.81926 -122.20451 37.81883 -122.20447 37.8184 -122.20448 37.81797 -122.20455 37.81755 -122.20467 37.81714 -122.20483 37.81674 -122.20505 37.81636 -122.20532 37.816 -122.20562 37.81567 -122.20598 37.81537 -122.20636 37.81496 -122.20694 37.81493 -122.20698 37.81467 -122.20735 37.81448 -122.20738 37.81434 -122.20741 37.81418 -122.20745 37.81403 -122.20748 37.81363 -122.20761 37.8135 -122.20766 37.81292 -122.20793 37.81291 -122.20793 37.81283 -122.20798 37.81269 -122.20807 37.81213 -122.20847 37.81198 -122.2086 37.81197 -122.2086 37.81158 -122.20882 37.81148 -122.20888 37.81124 -122.20904 37.81121 -122.20906 37.81119 -122.20908 37.81116 -122.2091 37.81114 -122.20912 37.81078 -122.20941 37.81073 -122.20945 37.81034 -122.20984 37.81021 -122.20999 37.81003 -122.2102 37.80994 -122.21031 37.80993 -122.21033 37.8096 -122.21061 37.80926 -122.21095 37.80895 -122.21134 37.80868 -122.21176 37.80843 -122.21221 37.80822 -122.21269 37.80805 -122.21319 37.80792 -122.21371 37.80783 -122.21424 37.80778 -122.21478 37.80777 -122.21533 37.8078 -122.21587 37.80788 -122.21641 37.80799 -122.21694 37.80815 -122.21745 37.80824 -122.21772 37.80841 -122.21822 37.8085 -122.21843 37.8085 -122.21843 37.80854 -122.21866 37.80855 -122.21873 37.80856 -122.2188 37.80859 -122.21897 37.80865 -122.21924 37.80874 -122.21966 37.80878 -122.21985 37.80908 -122.22122 37.80919 -122.2217 37.80926 -122.22199 37.80932 -122.22219 37.80932 -122.22221 37.80944 -122.22263 37.80955 -122.22334 37.80957 -122.22347 37.80958 -122.22351 37.80962 -122.22376 37.8097 -122.22421 37.80977 -122.22449 37.80996 -122.22531 37.80996 -122.22533 37.81002 -122.2256 37.81011 -122.22594 37.81018 -122.22618 37.81018 -122.22619 37.8104 -122.22693 37.81041 -122.22698 37.81052 -122.22747 37.81052 -122.22747 37.81098 -122.22949 37.8111 -122.23004 37.81114 -122.23025 37.81119 -122.23046 37.81126 -122.23079 37.81169 -122.23291 37.81169 -122.23292 37.81184 -122.23365 37.81203 -122.23437 37.8121 -122.23458 37.8121 -122.23461 37.81231 -122.23523 37.81233 -122.23531 37.81236 -122.23542 37.81251 -122.23596 37.81257 -122.23616 37.81262 -122.23634 37.81267 -122.2365 37.81269 -122.23659 37.8127 -122.23661 37.81277 -122.23685 37.81287 -122.23741 37.81292 -122.23796 37.81292 -122.23798 37.81294 -122.23821 37.81301 -122.23874 37.81311 -122.23927 37.8132 -122.23961 37.81345 -122.24064 37.81345 -122.24066 37.8135 -122.24084 37.81352 -122.24093 37.81367 -122.24171 37.81372 -122.24197 37.81377 -122.24219 37.81386 -122.24258 37.81413 -122.24377 37.81413 -122.24379 37.81423 -122.24418 37.81428 -122.2444 37.81432 -122.24455 37.81444 -122.245 37.81445 -122.24504 37.81449 -122.24519 37.81458 -122.2455 37.81463 -122.24566 37.81464 -122.24568 37.8148 -122.24618 37.81486 -122.24635 37.81501 -122.24677 37.81519 -122.24717 37.81523 -122.24726 37.81535 -122.24751 37.81541 -122.24763 37.81579 -122.2483 37.8159 -122.24847 37.81593 -122.2485 37.81606 -122.24881 37.81637 -122.24933 37.81641 -122.24939 37.81664 -122.24971 37.81667 -122.24975 37.81667 -122.24975 37.81672 -122.24981 37.81698 -122.25012 37.81711 -122.25027 37.81734 -122.25051 37.81748 -122.25064 37.81803 -122.25109 37.81811 -122.25115 37.81839 -122.25147 37.8184 -122.25148 37.81867 -122.25185 37.8196 -122.25315 37.8199 -122.25353 37.82023 -122.25388 37.82059 -122.25419 37.82097 -122.25445 37.82137 -122.25466 37.82178 -122.25483 37.8222 -122.25494 37.82263 -122.255 37.82306 -122.25501 37.82311 -122.25501&quot;);&gt;;);out;&#39;</code></pre>
<p>When I post this request:</p>
<pre><code>response = requests.post(url, data=data, timeout=timeout)</code></pre>
<p>This latter request used to work every single time (up to two days ago when I last tried it), but as of this morning I receive status code 429 (too many requests) every time I run it. I have tried this latter request from multiple computers and IP addresses, and I always get 429. While this response says "too many requests", I can immediately run the first request again and get status code 200 back. So it seems like I have indeed not actually made too many requests. Moreover, the API <a href="http://www.overpass-api.de/api/status">status page</a> tells me I have 2 slots available at all times throughout this process. I have also tried increasing/decreasing my timeouts but there is no change (in fact, the server responds with the 200 or the 429 within a second or two each time).</p>
<p><strong>Why am I suddenly receiving 429 for this query that always worked in the past?</strong></p>
<p>Edit: Every similarly complex polygon I try also returns a 429. Every simple polygon I try returns a 200. In the past, every polygon (simple or complex) returned a 200 with no problem.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '17, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/8eb28ad933ae655db57b6c6b8563eb67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gboeing&#39;s gravatar image" />
<p><span>gboeing</span><br />
<span class="score" title="136 reputation points">136</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gboeing has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '17, 18:16</strong> </span></p>
</div>
</div>
<div id="comments-container-55828" class="comments-container">
&#10;</div>
<div id="comment-tools-55828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55828-form-container" class="comment-form-container">
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

<span id="55845"></span>

<div id="answer-container-55845" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55845-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-55845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gboeing has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Short answer: Please set a Referer or change the User Agent to a less generic one. In Python, <a href="https://docs.python.org/3.5/library/urllib.request.html#urllib.request.Request">https://docs.python.org/3.5/library/urllib.request.html#urllib.request.Request</a> and there origin_req_host.</p>
<p>I'm sorry for the disruption.</p>
<p>Long answer: During the last week I have seen a massive overuse by a single user who has sent his/her requests from multiple IP addresses, but without useful information to figure out whom to contact. User agent is "Python-urllib/2.7", referer is null. Usually, I would prefer to block only single IP addresses, but this would end up blocking completely a large Czech carrier and a Czech university.</p>
<p>To keep damage to everybody else as low as possible, I have instead temporarily blocked requests that</p>
<ul>
<li>use POST</li>
<li>set no referer</li>
<li>have a request text that is longer than 2048 byte</li>
</ul>
<p>You have been hit accidentially by that block.</p>
<p>As the best solution in such cases is to contact the affected user to find a long term solution, my suggestion is to set a referer which will get your requests distinct from the problematic ones.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '17, 04:24</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-55845" class="comments-container">
&#10;</div>
<div id="comment-tools-55845" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55845-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77808"></span>

<div id="answer-container-77808" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77808-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I fear I have been running into the same issue. How can I set a new referrer in an AJAX call done by a Leaflet plugin <a href="https://github.com/GuillaumeAmat/leaflet-overpass-layer">https://github.com/GuillaumeAmat/leaflet-overpass-layer</a> ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '20, 15:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0782a57eca3816b0e7ee356a337fa2bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="underscore&#39;s gravatar image" />
<p><span>underscore</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="underscore has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77808" class="comments-container">
<span id="77809"></span>
<div id="comment-77809" class="comment">
<div id="post-77809-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's unlikely that peoople will see your question, because you'e placed it as an "answer" under the original question. I'd suggest asking it as a new question, but also linking to this question to make it clear what and why you are asking.</p>
</div>
<div id="comment-77809-info" class="comment-info">
<span class="comment-age">(30 Nov '20, 16:30)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-77808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77808-form-container" class="comment-form-container">
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

