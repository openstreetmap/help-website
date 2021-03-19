+++
type = "question"
title = "Get Vendor OUI with tshark"
description = '''Hey experts, I&#x27;m analyzing traffic on some networks with dumpcap/tshark (Linux and command line environment). I would like to simply get the OUI info per MAC address listed in a CSV file, like: aa:bb:cc:dd:11:22, VendorX bb:cc:aa:44:55:44, VendorY I know that a MAC -&amp;gt; OUI translation table exist ...'''
date = "2017-04-01T14:41:00Z"
lastmod = "2017-04-05T13:49:00Z"
weight = 60511
keywords = [ "oui", "tshark", "linux" ]
aliases = [ "/questions/60511" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Get Vendor OUI with tshark](/questions/60511/get-vendor-oui-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60511-score" class="post-score" title="current number of votes">0</div><span id="post-60511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey experts, I'm analyzing traffic on some networks with dumpcap/tshark (Linux and command line environment). I would like to simply get the OUI info per MAC address listed in a CSV file, like:</p><p>aa:bb:cc:dd:11:22, VendorX</p><p>bb:cc:aa:44:55:44, VendorY</p><p>I know that a MAC -&gt; OUI translation table exist in tshark as the OUI info can be displayed (with tons of other data) with for example the -V switch, but I just want the specific vemdor info and no other junk. Anyone who knows the trick? Have tried using the same read filter as is used in Wireshark, but it's not recognized by tshark.</p><p>Cheers, Sam</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-oui" rel="tag" title="see questions tagged &#39;oui&#39;">oui</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '17, 14:41</strong></p><img src="https://secure.gravatar.com/avatar/c19324dc35615378dc81ba8a3d71b0b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SamA&#39;s gravatar image" /><p><span>SamA</span><br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SamA has no accepted answers">0%</span></p></div></div><div id="comments-container-60511" class="comments-container"></div><div id="comment-tools-60511" class="comment-tools"></div><div class="clear"></div><div id="comment-60511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60521"></span>

<div id="answer-container-60521" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60521-score" class="post-score" title="current number of votes">1</div><span id="post-60521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the field name <code>eth.addr_resolved</code> with a little post-processing, i.e.</p><pre><code>tshark -r xxx.pcapng -T fields -e eth.addr_resolved</code></pre><p>gives output like this:</p><pre><code>Cisco-Li_78:70:c7,IntelCor_35:96:f0
IntelCor_35:96:f0,Cisco-Li_78:70:c7</code></pre><p>so post processing could split at the "_".</p><p>There are analogous fields for the source and destination addresses; <code>eth.src_resolved</code> and <code>eth.dst_resolved</code>.</p><p>You might need to enable the preference for MAC address resolution; `-o nameres.mac_name:TRUE</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '17, 04:31</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60521" class="comments-container"><span id="60591"></span><div id="comment-60591" class="comment"><div id="post-60591-score" class="comment-score"></div><div class="comment-text"><p>Thanks for suggestions. Forgot to write that I'm doing WLAN capture. I think the thark command should look like this:</p><pre><code>tshark -r xxx.pcap -T fields -e wlan.addr_resolved</code></pre><p>However, nothing is printed. I capture the packets like this:</p><pre><code>tshark -r xxx.pcap -T fields -e wlan.sa -e wlan.addr_resolved</code></pre><p>Have tried with the -o switch that grahamb suggests, but it doesn't seem to exist. Also tried various -N switches (that's what the help file for tshark suggests) but still nothing is printed out. Any suggestions?</p><p>Cheers! Sam</p></div><div id="comment-60591-info" class="comment-info"><span class="comment-age">(05 Apr '17, 10:56)</span> <span class="comment-user userinfo">SamA</span></div></div><span id="60596"></span><div id="comment-60596" class="comment"><div id="post-60596-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-60596-info" class="comment-info"><span class="comment-age">(05 Apr '17, 13:49)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-60521" class="comment-tools"></div><div class="clear"></div><div id="comment-60521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60518"></span>

<div id="answer-container-60518" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60518-score" class="post-score" title="current number of votes">0</div><span id="post-60518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Probably the best way to go about this is to post-process the tshark output into the form you need. You could select one of the more structured output types, like PDML or JSON, for this and feed that into your post processing script.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '17, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-60518" class="comments-container"></div><div id="comment-tools-60518" class="comment-tools"></div><div class="clear"></div><div id="comment-60518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

