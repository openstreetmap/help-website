+++
type = "question"
title = "Is it possible to prepare a filter for TCPDUMP command in Linux Servers"
description = '''Dear Team, We have Linux OS installed on one of our nodes (which has SS7 stack) now if we want to filter packets which are submit towards network we use below command to do. tcpdump -ni any sctp s0 -w filename.pcap Now above command captures the all packets of ss7 layer, is it possible to prepare a ...'''
date = "2012-08-06T23:14:00Z"
lastmod = "2012-08-07T07:51:00Z"
weight = 13414
keywords = [ "tcpdump", "filtering", "remote", "filters", "linux" ]
aliases = [ "/questions/13414" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to prepare a filter for TCPDUMP command in Linux Servers](/questions/13414/is-it-possible-to-prepare-a-filter-for-tcpdump-command-in-linux-servers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13414-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Team,</p><p>We have Linux OS installed on one of our nodes (which has SS7 stack) now if we want to filter packets which are submit towards network we use below command to do.</p><p>tcpdump -ni any sctp s0 -w filename.pcap</p><p>Now above command captures the all packets of ss7 layer, is it possible to prepare a filter on command line itself like ((gsm_sms.tp-mti == 0) &amp;&amp; (gsm_map.imsi_digits == "404971026311824")) we do filtering in wireshark OR what type of filtering options are there.</p><p>Or can wireshark itself be helpful do so, because i tried using Interface remote but its not possible as server/node does have direct connectivity its via a different server.</p></div><div id="question-tags" class="tags-container tags">tcpdump filtering remote filters linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '12, 23:14</strong></p><img src="https://secure.gravatar.com/avatar/ea81afbd71dc63ea6a6506203bc83c3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="creative&#39;s gravatar image" /><p>creative<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="creative has no accepted answers">0%</span></p></div></div><div id="comments-container-13414" class="comments-container"></div><div id="comment-tools-13414" class="comment-tools"></div><div class="clear"></div><div id="comment-13414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13426"></span>

<div id="answer-container-13426" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13426-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>tcpdump only supports capture filters, not Wireshark's (far richer) display filters. As such, you can't filter for things like gsm_sms.tp-mti with tcpdump. With capture filters you're limited to the things that libpcap understands. See the manual page of pcap-filter(7) or, if that doesn't exist, tcpdump(8), or, if that doesn't exist, <a href="http://wiki.wireshark.org/CaptureFilters">http://wiki.wireshark.org/CaptureFilters</a> .</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '12, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-13426" class="comments-container"><span id="13438"></span><div id="comment-13438" class="comment"><div id="post-13438-score" class="comment-score"></div><div class="comment-text"><p>...and Wireshark's capture filters are the same as tcpdump's capture filters, with the same limitations.</p></div><div id="comment-13438-info" class="comment-info"><span class="comment-age">(07 Aug '12, 11:51)</span> Guy Harris ♦♦</div></div><span id="13447"></span><div id="comment-13447" class="comment"><div id="post-13447-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff for your answer.</p><p>@Harris...what ? How Wireshark filters are same as tcpdump filters ???</p></div><div id="comment-13447-info" class="comment-info"><span class="comment-age">(07 Aug '12, 19:22)</span> creative</div></div><span id="13449"></span><div id="comment-13449" class="comment"><div id="post-13449-score" class="comment-score">1</div><div class="comment-text"><p>There are <em>two</em> kinds of "Wireshark filters" - capture filters, which are what are specified when you start a capture, and "display filters" (which can also be used, for example, for colorizing packets), which are specified when you have a capture. Wireshark <em>capture</em> filters are implemented by libpcap/WinPcap, just as tcpdump's filters are, so they're exactly the same as tcpdump filters. Wireshark <em>display</em> filters are implemented by Wireshark, and are much more capable than capture filters.</p></div><div id="comment-13449-info" class="comment-info"><span class="comment-age">(08 Aug '12, 00:01)</span> Guy Harris ♦♦</div></div><span id="13460"></span><div id="comment-13460" class="comment"><div id="post-13460-score" class="comment-score"></div><div class="comment-text"><p>Thanks Harris :)</p></div><div id="comment-13460-info" class="comment-info"><span class="comment-age">(08 Aug '12, 03:20)</span> creative</div></div></div><div id="comment-tools-13426" class="comment-tools"></div><div class="clear"></div><div id="comment-13426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

