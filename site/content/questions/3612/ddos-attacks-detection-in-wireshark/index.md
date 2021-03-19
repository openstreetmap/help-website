+++
type = "question"
title = "DDoS attacks detection in wireshark"
description = '''Is it possible to detect ddos attacks with wireshark for group of servers?'''
date = "2011-04-19T08:26:00Z"
lastmod = "2011-04-19T08:40:00Z"
weight = 3612
keywords = [ "ddos" ]
aliases = [ "/questions/3612" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [DDoS attacks detection in wireshark](/questions/3612/ddos-attacks-detection-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3612-score" class="post-score" title="current number of votes">0</div><span id="post-3612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to detect ddos attacks with wireshark for group of servers?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ddos" rel="tag" title="see questions tagged &#39;ddos&#39;">ddos</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '11, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/d5352b436bf8a484e32225c91054f913?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dkorzhevin&#39;s gravatar image" /><p><span>dkorzhevin</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dkorzhevin has no accepted answers">0%</span></p></div></div><div id="comments-container-3612" class="comments-container"></div><div id="comment-tools-3612" class="comment-tools"></div><div class="clear"></div><div id="comment-3612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3613"></span>

<div id="answer-container-3613" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3613-score" class="post-score" title="current number of votes">3</div><span id="post-3613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it may be possible if you're capturing traffic to this group of servers. DDoS attacks often are "simple" SYN floods coming from apparently all over the world. To determine where a packet is coming from you can enable the GeoIP localisation in the Name Resolution settings in the Wireshark preferences after you've placed the according files (available for free from <a href="http://www.maxmind.com">www.maxmind.com</a>) in a directory.</p><p>After you've successfully pointed Wireshark to the database files you can see the location of IPs in the IP decode (you might need to enable this in the protocol preferences first) and in the Endpoint statistics. If you see many packets flooding your servers from seemingly random sources you're probably being DDoSed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '11, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3613" class="comments-container"></div><div id="comment-tools-3613" class="comment-tools"></div><div class="clear"></div><div id="comment-3613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

