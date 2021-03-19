+++
type = "question"
title = "Merging captures on 1.99.5"
description = '''I&#x27;m looking into merging two captures of different encapsulation type for chronological packet analysis. On the current stable version of Wireshark (1.12.4), you are unable to do this via the GUI OR the CLI using mergecap (as mentioned, only if the encap type is different).  When using the devel ver...'''
date = "2015-05-04T10:59:00Z"
lastmod = "2015-05-04T14:14:00Z"
weight = 42061
keywords = [ "development", "merge", "mergecap", "captures", "wireshark" ]
aliases = [ "/questions/42061" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Merging captures on 1.99.5](/questions/42061/merging-captures-on-1995)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42061-score" class="post-score" title="current number of votes">0</div><span id="post-42061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking into merging two captures of different encapsulation type for chronological packet analysis. On the current stable version of Wireshark (1.12.4), you are unable to do this via the GUI OR the CLI using mergecap (as mentioned, only if the encap type is different).</p><p>When using the devel version (1.99.5), I am able to successfully merge two different encapsualtion type captures (802.11+radiotap &amp;&amp; ethernet) when using the GUI only. When using mergecap, I obtain the following:</p><pre><code>$ mergecap -w &quot;testmergefile.pcapng&quot; wired.pcap wireless.pcap -vvv
mergecap: wired.pcap is type Wireshark/... - pcapng.
mergecap: wireless.pcap is type Wireshark/tcpdump/... - pcap.
mergecap: multiple frame encapsulation types detected
          defaulting to WTAP_ENCAP_PER_PACKET
          wired.pcap had type Ethernet (ether)
          wireless.pcap had type IEEE 802.11 plus radiotap radio header (ieee-802-11-radiotap)
mergecap: selected frame_type Per packet (per-packet)
mergecap: Can&#39;t open or create testmergefile.pcapng: Files from that network type can&#39;t be saved in that format

$ mergecap --version
Mergecap (Wireshark) 1.99.5 (v1.99.5-0-g7e8595c from master)</code></pre><p>As mentioned, this works fine from the GUI, so I'm not sure if devel version uses mergecap in the background for merges, or something else? If it is something else, do we have the ability to invoke this via CLI for automation purposes?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-mergecap" rel="tag" title="see questions tagged &#39;mergecap&#39;">mergecap</span> <span class="post-tag tag-link-captures" rel="tag" title="see questions tagged &#39;captures&#39;">captures</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 May '15, 10:59</strong></p><img src="https://secure.gravatar.com/avatar/8a657a3bbf2e6d9d371ef609039621bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thisisatestcaptures&#39;s gravatar image" /><p><span>thisisatestc...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thisisatestcaptures has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 May '15, 13:15</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-42061" class="comments-container"></div><div id="comment-tools-42061" class="comment-tools"></div><div class="clear"></div><div id="comment-42061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42066"></span>

<div id="answer-container-42066" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42066-score" class="post-score" title="current number of votes">0</div><span id="post-42066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a bug, for which an ongoing patch is under review here: <a href="https://code.wireshark.org/review/#/c/8293/">https://code.wireshark.org/review/#/c/8293/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '15, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-42066" class="comments-container"></div><div id="comment-tools-42066" class="comment-tools"></div><div class="clear"></div><div id="comment-42066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

