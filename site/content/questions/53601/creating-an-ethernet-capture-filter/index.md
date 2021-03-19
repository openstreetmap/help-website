+++
type = "question"
title = "Creating an ethernet capture filter"
description = '''I am new to wireshark filtering. I didn&#x27;t found any serious wireshark filtering tutorial. I want to create a capture filter every frames sent by 192.168.1.100 to 192.168.1.44 by Ethernet using http protocol. I tried: http eth source 192.168.1.100 dest 192.168.1.44  Yet, It didn&#x27;t worked and was turn...'''
date = "2016-06-22T01:19:00Z"
lastmod = "2016-06-22T04:08:00Z"
weight = 53601
keywords = [ "ethernet", "capture-filter" ]
aliases = [ "/questions/53601" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Creating an ethernet capture filter](/questions/53601/creating-an-ethernet-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53601-score" class="post-score" title="current number of votes">0</div><span id="post-53601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to wireshark filtering. I didn't found any serious wireshark filtering tutorial. I want to create a capture filter every frames sent by 192.168.1.100 to 192.168.1.44 by Ethernet using http protocol.</p><p>I tried:</p><pre><code>http eth source 192.168.1.100 dest 192.168.1.44</code></pre><p>Yet, It didn't worked and was turn to red. CCan you help me write this command? If you have any link about a serious wireshark filtering commands I would be ery glad to hear about it!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '16, 01:19</strong></p><img src="https://secure.gravatar.com/avatar/d32d77756fa16593e0801f5fffb2b1ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AntoineKRA&#39;s gravatar image" /><p><span>AntoineKRA</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AntoineKRA has no accepted answers">0%</span></p></div></div><div id="comments-container-53601" class="comments-container"></div><div id="comment-tools-53601" class="comment-tools"></div><div class="clear"></div><div id="comment-53601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53603"></span>

<div id="answer-container-53603" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53603-score" class="post-score" title="current number of votes">0</div><span id="post-53603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As the capture filter is "executed" by the libpcap/WinPcap/NPcap module, the documentation (not exactly a tutorial) is <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">here</a>, not at the Wireshark wiki.</p><p>In your case, the correct syntax would be <code>ip and src host 192.168.1.100 and dst host 192.168.1.44 and tcp port 80</code>, where <code>ip</code> is a shortcut for <code>ether proto ip</code>.</p><p>Beware - in Qt version of Wireshark (the default one since 2.0.x), you have to choose an interface before starting to fill in the capture filter field, otherwise the field will be red even if the syntax is correct.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '16, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53603" class="comments-container"></div><div id="comment-tools-53603" class="comment-tools"></div><div class="clear"></div><div id="comment-53603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

