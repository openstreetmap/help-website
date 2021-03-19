+++
type = "question"
title = "how to let wireshark to demonstrates the country name when plot ip addresses"
description = '''As we know, Wireshark has the capability to plot ip addresses on the world map if we configured it with GEOIP database files. It does shows the ip addresses on the map when I click on Statistics-&amp;gt;Endpoints-&amp;gt;IPv4-&amp;gt;MAP, but it does not show country names for the specific ip addresses which it...'''
date = "2013-09-14T08:19:00Z"
lastmod = "2013-09-16T07:49:00Z"
weight = 24682
keywords = [ "geoip", "endpoints", "plot" ]
aliases = [ "/questions/24682" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [how to let wireshark to demonstrates the country name when plot ip addresses](/questions/24682/how-to-let-wireshark-to-demonstrates-the-country-name-when-plot-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24682-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As we know, Wireshark has the capability to plot ip addresses on the world map if we configured it with GEOIP database files. It does shows the ip addresses on the map when I click on Statistics-&gt;Endpoints-&gt;IPv4-&gt;MAP, but it does not show country names for the specific ip addresses which it has resolved successfully(I can see the exact country names in the country column of IPv4 tab), why doesn't it show that on the map too? Can I make it in Wireshark and how?</p></div><div id="question-tags" class="tags-container tags">geoip endpoints plot</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '13, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/3b74ebd1641529ce5e62bd27682ce59a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WeitaMilk&#39;s gravatar image" /><p>WeitaMilk<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WeitaMilk has no accepted answers">0%</span></p></div></div><div id="comments-container-24682" class="comments-container"></div><div id="comment-tools-24682" class="comment-tools"></div><div class="clear"></div><div id="comment-24682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24768"></span>

<div id="answer-container-24768" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24768-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are still some problems regarding GeoIP lookups, being tracked as <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=4030">Bug 4030</a>.</p><p>In this case, it's likely that you have both the IPv4 and IPv6 GeoIP databases in the same directory. If you move the IPv6 database files to another directory, then IPv4 lookups should work correctly. If you later want to map IPv6 addresses, then move the IPv6 database files back into your GeoIP directory and move the IPv4 database files to another directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '13, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24768" class="comments-container"><span id="24775"></span><div id="comment-24775" class="comment"><div id="post-24775-score" class="comment-score"></div><div class="comment-text"><p>Thank you cmaynard, your solution partially solved my problem. At least the map will show the geographic details when I click on any plot, but what I want is displaying the details of all the plots at the same time. Now, I click on one plot, the details show up, but when I click on another plot, the former details window vanished.</p><p>By the way, do you know how to let the map to show country names even there is no point on that country?</p></div><div id="comment-24775-info" class="comment-info"><span class="comment-age">(16 Sep '13, 09:53)</span> WeitaMilk</div></div><span id="24776"></span><div id="comment-24776" class="comment"><div id="post-24776-score" class="comment-score">1</div><div class="comment-text"><p>It is currently not possible to display the details of all the plots at the same time, nor is it possible to display the country names. It may be possible to do this with some code changes, especially the latter, by utilizing other map layers. Feel free to submit an enhancement bug request.</p><p>By the way, did you really intend to award me with 11 reputation points? That leaves you with none.</p><p>If an answer satisfies your question, you can click the "thumbs up" indicating that it's useful, and also accept it by clicking the checkmark. Perhaps that is what you intended to do?</p></div><div id="comment-24776-info" class="comment-info"><span class="comment-age">(16 Sep '13, 10:01)</span> cmaynard ♦♦</div></div><span id="24791"></span><div id="comment-24791" class="comment"><div id="post-24791-score" class="comment-score"></div><div class="comment-text"><p>cmaynard, thank you for your comment. I am not familiar with the site now, but you deserved that 11 points. I am a malware analyst, and that's why I want to show the details of all the plots. As you know, when I write a report regarding certain threat, such as an IRCBot, I want to display all of the detailed C&amp;C servers' locations on the map:)</p><p>Once again, thank you for your help.</p></div><div id="comment-24791-info" class="comment-info"><span class="comment-age">(16 Sep '13, 19:49)</span> WeitaMilk</div></div></div><div id="comment-tools-24768" class="comment-tools"></div><div class="clear"></div><div id="comment-24768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

