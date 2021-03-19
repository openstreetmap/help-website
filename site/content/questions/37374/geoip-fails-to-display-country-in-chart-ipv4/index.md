+++
type = "question"
title = "Geoip fails to display country in chart IPv4"
description = '''Geoip fails to display country in chart IPv4, fails to display City, Country, &amp;amp; AS Number on map. IPv6 works fine. I have tried ver 1.10 &amp;amp; 1.12.1 Any suggestions? '''
date = "2014-10-27T08:54:00Z"
lastmod = "2014-10-30T04:24:00Z"
weight = 37374
keywords = [ "geoip" ]
aliases = [ "/questions/37374" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Geoip fails to display country in chart IPv4](/questions/37374/geoip-fails-to-display-country-in-chart-ipv4)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37374-score" class="post-score" title="current number of votes">0</div><span id="post-37374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Geoip fails to display country in chart IPv4, fails to display City, Country, &amp; AS Number on map. IPv6 works fine. I have tried ver 1.10 &amp; 1.12.1<br />
Any suggestions?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-geoip" rel="tag" title="see questions tagged &#39;geoip&#39;">geoip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '14, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/459a04f2fbe838acc644e07c30d8ded3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lewis15&#39;s gravatar image" /><p><span>lewis15</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lewis15 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-37374" class="comments-container"><span id="37445"></span><div id="comment-37445" class="comment"><div id="post-37445-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/2014-10-29_15_37_34-Endpoints__Test20141010V4.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/2014-10-29_15_40_04-Wireshark__IP_Location_MapV4.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/2014-10-29_15_35_31-Endpoints__Test20141010V6.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/2014-10-29_15_38_55-Wireshark__IP_Location_MapV6.png" alt="alt text" /></p></div><div id="comment-37445-info" class="comment-info"><span class="comment-age">(29 Oct '14, 12:50)</span> <span class="comment-user userinfo">lewis15</span></div></div></div><div id="comment-tools-37374" class="comment-tools"></div><div class="clear"></div><div id="comment-37374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37457"></span>

<div id="answer-container-37457" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37457-score" class="post-score" title="current number of votes">0</div><span id="post-37457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The fact that City, Country, and AS Number fail to display on the map for IPv4 is a known bug. Nothing you can do about it.</p><p>Country does display on the Endpoints dialog. Notice that there are TWO columns for Country, for AS Number, and for City. One is populated and the other is blank. On your IPv4 screen shot, the Country column that is between the second AS Number column and the first City column is blank, but there is another Country column to the left of the first AS Number column. At the left edge of the screen shot, you can just see the "es" of "United States."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '14, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></img></div></div><div id="comments-container-37457" class="comments-container"></div><div id="comment-tools-37457" class="comment-tools"></div><div class="clear"></div><div id="comment-37457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

