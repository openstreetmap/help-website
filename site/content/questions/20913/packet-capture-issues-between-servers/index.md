+++
type = "question"
title = "Packet capture issues between servers"
description = '''Hi, I am trying to capture traffic/dropped packets between two servers, I have wireshark installed on server1 (example; 192.168.1.1) I clicked on the interface I want to capture, and then in the filter box I put in the below... I have in there &quot;host 192.168.1.1 and host 192.168.1.2&quot; I tried it with ...'''
date = "2013-05-02T09:56:00Z"
lastmod = "2013-05-02T13:30:00Z"
weight = 20913
keywords = [ "capture", "packet", "servers" ]
aliases = [ "/questions/20913" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Packet capture issues between servers](/questions/20913/packet-capture-issues-between-servers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20913-score" class="post-score" title="current number of votes">0</div><span id="post-20913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to capture traffic/dropped packets between two servers, I have wireshark installed on server1 (example; 192.168.1.1)</p><p>I clicked on the interface I want to capture, and then in the filter box I put in the below...</p><p>I have in there "host 192.168.1.1 and host 192.168.1.2" I tried it with the "" and without</p><p>It gives me the error: "hostname 192.168.1.1 and hostname 192.168.1.2 is neither a field nor a protocal name. The following display filter isnt a valid display filter"</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-servers" rel="tag" title="see questions tagged &#39;servers&#39;">servers</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '13, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/908dce768dea1d7941aabe5e077e2748?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharwal&#39;s gravatar image" /><p><span>sharwal</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharwal has no accepted answers">0%</span></p></div></div><div id="comments-container-20913" class="comments-container"></div><div id="comment-tools-20913" class="comment-tools"></div><div class="clear"></div><div id="comment-20913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20914"></span>

<div id="answer-container-20914" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20914-score" class="post-score" title="current number of votes">0</div><span id="post-20914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark has two kinds of filters: display filters and capture filters. Obviously you tried to enter a capture filter into the display filter box, which doesn't work. If you want to use the filter you specified to limit what packets are captured you need to do it on the capture interface: open the capture options dialog, double click on the interface, and put your filter into the capture filter box.</p><p>If you want to capture everything and just display the two IPs you can use a display filter, in your case "ip.addr==192.168.1.1 and ip.addr==192.168.1.2".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '13, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20914" class="comments-container"><span id="20915"></span><div id="comment-20915" class="comment"><div id="post-20915-score" class="comment-score"></div><div class="comment-text"><p><span>@sharwal</span></p><p>FYI, there is info about capture and display filters in the user guide and on the wiki; <a href="http://wiki.wireshark.org/CaptureFilters">Capture Filters</a> <a href="http://wiki.wireshark.org/DisplayFilters">Display Filters</a></p></div><div id="comment-20915-info" class="comment-info"><span class="comment-age">(02 May '13, 10:07)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="20916"></span><div id="comment-20916" class="comment"><div id="post-20916-score" class="comment-score"></div><div class="comment-text"><p>I only want to capture traffic between the two servers.... where is the capture options? I click on Capture at the top and don't see any options field, do I click on Capture Filter and enter it under field string?</p></div><div id="comment-20916-info" class="comment-info"><span class="comment-age">(02 May '13, 10:14)</span> <span class="comment-user userinfo">sharwal</span></div></div><span id="20918"></span><div id="comment-20918" class="comment"><div id="post-20918-score" class="comment-score"></div><div class="comment-text"><p>Use the menu "Capture" -&gt; "Options" and you'll see a list of interfaces. Double click on the one you want to capture on (this is assuming you're using 1.8.x or later) and you'll see a field called "Capture Filter"</p></div><div id="comment-20918-info" class="comment-info"><span class="comment-age">(02 May '13, 13:30)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-20914" class="comment-tools"></div><div class="clear"></div><div id="comment-20914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

