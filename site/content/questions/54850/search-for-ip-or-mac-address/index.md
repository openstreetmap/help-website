+++
type = "question"
title = "Search for IP or Mac address"
description = '''Hello there I am using Wireshark for the first time and I am trying to monitor my own network seeing the information that goes between my ip &amp;amp; my console. Is there a search functionality that will allow me to find my console by inputting its ip address or mac address as the search query after us...'''
date = "2016-08-16T01:33:00Z"
lastmod = "2016-08-20T11:24:00Z"
weight = 54850
keywords = [ "function", "search" ]
aliases = [ "/questions/54850" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Search for IP or Mac address](/questions/54850/search-for-ip-or-mac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54850-score" class="post-score" title="current number of votes">0</div><span id="post-54850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello there I am using Wireshark for the first time and I am trying to monitor my own network seeing the information that goes between my ip &amp; my console. Is there a search functionality that will allow me to find my console by inputting its ip address or mac address as the search query after using the capture function?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-function" rel="tag" title="see questions tagged &#39;function&#39;">function</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '16, 01:33</strong></p><img src="https://secure.gravatar.com/avatar/24b6aa04ad9a65a0ec54bc07894a78a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xzane&#39;s gravatar image" /><p><span>xzane</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xzane has no accepted answers">0%</span></p></div></div><div id="comments-container-54850" class="comments-container"></div><div id="comment-tools-54850" class="comment-tools"></div><div class="clear"></div><div id="comment-54850-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54856"></span>

<div id="answer-container-54856" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54856-score" class="post-score" title="current number of votes">0</div><span id="post-54856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You may want to look into using <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChWorkDisplayFilterSection.html">display filters</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '16, 04:49</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54856" class="comments-container"><span id="54961"></span><div id="comment-54961" class="comment"><div id="post-54961-score" class="comment-score"></div><div class="comment-text"><p>I have tried using this but the filters does not filter out all ips except for the one you type in. It goes by either TCP, UDP etc. If I was looking for for example 85.63.22.46 &lt;&lt;&lt;Made up ip the filter does not allow me to filter out my resullts by ip. If I was looking for example my PS4 by mac address. I was unable to use the filter to show a specific mac address by me typing that mac address into the filter. Unless theres some configurations I have to make it does not work for me.</p></div><div id="comment-54961-info" class="comment-info"><span class="comment-age">(18 Aug '16, 12:43)</span> <span class="comment-user userinfo">xzane</span></div></div><span id="55004"></span><div id="comment-55004" class="comment"><div id="post-55004-score" class="comment-score"></div><div class="comment-text"><p>Can you provide examples of the exact filter expressions you were using for IP and MAC?</p></div><div id="comment-55004-info" class="comment-info"><span class="comment-age">(20 Aug '16, 11:24)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-54856" class="comment-tools"></div><div class="clear"></div><div id="comment-54856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

