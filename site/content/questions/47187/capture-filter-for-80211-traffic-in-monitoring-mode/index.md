+++
type = "question"
title = "Capture filter for 802.11 traffic in monitoring mode"
description = '''I&#x27;m currently capturing traffic in tshark and applying a display filter like to capture only probe request: tshark -n -l -i wlan0 -R &#x27;wlan.fc.type_subtype == 0x0004 &amp;amp;&amp;amp; wlan_mgt.ssid != &quot;&quot; &amp;amp;&amp;amp; wlan.fcs_good == 1&#x27; -T fields -e wlan.sa -e wlan_mgt.ssid My trace are so huge as there&#x27;s no ...'''
date = "2015-11-03T10:08:00Z"
lastmod = "2016-02-05T01:26:00Z"
weight = 47187
keywords = [ "capture-filter", "wifi", "802.11", "tshark" ]
aliases = [ "/questions/47187" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Capture filter for 802.11 traffic in monitoring mode](/questions/47187/capture-filter-for-80211-traffic-in-monitoring-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47187-score" class="post-score" title="current number of votes">0</div><span id="post-47187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm currently capturing traffic in tshark and applying a display filter like to capture only probe request: tshark -n -l -i wlan0 -R 'wlan.fc.type_subtype == 0x0004 &amp;&amp; wlan_mgt.ssid != "" &amp;&amp; wlan.fcs_good == 1' -T fields -e wlan.sa -e wlan_mgt.ssid</p><p>My trace are so huge as there's no capture filter, in tcpdump style, but I can't find anything for 802.11 How can I create a capture filter that would limit my traffic to Probe request only? Or at least management frames or ...</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '15, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p><span>TomLaBaude</span><br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div></div><div id="comments-container-47187" class="comments-container"></div><div id="comment-tools-47187" class="comment-tools"></div><div class="clear"></div><div id="comment-47187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47200"></span>

<div id="answer-container-47200" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47200-score" class="post-score" title="current number of votes">1</div><span id="post-47200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TomLaBaude has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How can I create a capture filter that would limit my traffic to Probe request only?</p></blockquote><p>By reading <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">the pcap-filter man page</a>, which documents the syntax of libpcap/WinPcap capture filters as used by tcpdump/WinDump, Wireshark, etc., in particular the part describing the "type" and "subtype" keywords, and then noticing that one of the possible "subtype" values is "probe-req", so that "subtype probe-req" would be the filter.</p><blockquote><p>Or at least management frames</p></blockquote><p>If you want management frames in general, that'd be "type mgt", as per that man page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '15, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-47200" class="comments-container"></div><div id="comment-tools-47200" class="comment-tools"></div><div class="clear"></div><div id="comment-47200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49862"></span>

<div id="answer-container-49862" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49862-score" class="post-score" title="current number of votes">-1</div><span id="post-49862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Add wlan.fc.type == 0 to your filter to only get management frames. Null data frames also have subtype of 4.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '16, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/ccc3f50ef99e10e348a902ee8483f93c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ted%20Wards&#39;s gravatar image" /><p><span>Ted Wards</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ted Wards has no accepted answers">0%</span></p></div></div><div id="comments-container-49862" class="comments-container"><span id="49887"></span><div id="comment-49887" class="comment"><div id="post-49887-score" class="comment-score"></div><div class="comment-text"><p>Hi Ted, thanks for answering, but this is a display filter, not a capture filter. Guy gave me the answer.</p></div><div id="comment-49887-info" class="comment-info"><span class="comment-age">(05 Feb '16, 01:26)</span> <span class="comment-user userinfo">TomLaBaude</span></div></div></div><div id="comment-tools-49862" class="comment-tools"></div><div class="clear"></div><div id="comment-49862-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

