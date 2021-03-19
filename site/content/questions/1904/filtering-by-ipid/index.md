+++
type = "question"
title = "filtering by ip.id"
description = '''i want to build a filter which filters duplicated frames in a capture i want to filter it bi ip.identification number. for example if i have 5 frames with ip.id = 1000 i would like that after applying the filter only 1 frame will stay thank you'''
date = "2011-01-24T07:11:00Z"
lastmod = "2014-01-27T14:51:00Z"
weight = 1904
keywords = [ "filter", "ip.id" ]
aliases = [ "/questions/1904" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [filtering by ip.id](/questions/1904/filtering-by-ipid)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1904-score" class="post-score" title="current number of votes">0</div><span id="post-1904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>i want to build a filter which filters duplicated frames in a capture i want to filter it bi ip.identification number. for example if i have 5 frames with ip.id = 1000 i would like that after applying the filter only 1 frame will stay thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ip.id" rel="tag" title="see questions tagged &#39;ip.id&#39;">ip.id</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '11, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/353a2ff67b3cf198e82f93399b74f097?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dima&#39;s gravatar image" /><p><span>Dima</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dima has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jan '11, 07:14</strong> </span></p></div></div><div id="comments-container-1904" class="comments-container"></div><div id="comment-tools-1904" class="comment-tools"></div><div class="clear"></div><div id="comment-1904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1906"></span>

<div id="answer-container-1906" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1906-score" class="post-score" title="current number of votes">3</div><span id="post-1906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to filter (delete) duplicate frames, the ip.id is not sufficient as the same ip.id can be used for different IP addresses without being a duplicate.</p><p>You can use editcap to delete duplicate packets (from "editcap -h"):</p><pre><code>Duplicate packet removal:
  -d                     remove packet if duplicate (window == 5).
  -D &lt;dup window&gt;        remove packet if duplicate; configurable &lt;dup window&gt;
                         Valid &lt;dup window&gt; values are 0 to 1000000.
                         NOTE: A &lt;dup window&gt; of 0 with -v (verbose option) is
                         useful to print MD5 hashes.
  -w &lt;dup time window&gt;   remove packet if duplicate packet is found EQUAL TO OR
                         LESS THAN &lt;dup time window&gt; prior to current packet.
                         A &lt;dup time window&gt; is specified in relative seconds
                         (e.g. 0.000001).</code></pre><p>Hope this helps, Cheers,</p><p>Sake</p><p>PS Editcap is a command line tool and part of the Wireshark "suite"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '11, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jan '11, 07:31</strong> </span></p></div></div><div id="comments-container-1906" class="comments-container"><span id="1941"></span><div id="comment-1941" class="comment"><div id="post-1941-score" class="comment-score"></div><div class="comment-text"><p>thank you very much it did help me what a pity that i can't use this while live capture but it's enough for now</p><p>10x again</p></div><div id="comment-1941-info" class="comment-info"><span class="comment-age">(26 Jan '11, 04:25)</span> <span class="comment-user userinfo">Dima</span></div></div><span id="1942"></span><div id="comment-1942" class="comment"><div id="post-1942-score" class="comment-score"></div><div class="comment-text"><p>At capture time you want to make sure the mirroring configuration just gives you each packet once. You did not mention how you capture the packets, but the most likely source for duplicates is when you capture traffic on a vlan in both directions (as each frame enters the vlan and will also leave the vlan).</p><p>If that's the case, limit the capture to RX-only so that you capture only traffic that enters the vlan.</p></div><div id="comment-1942-info" class="comment-info"><span class="comment-age">(26 Jan '11, 06:12)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="29177"></span><div id="comment-29177" class="comment"><div id="post-29177-score" class="comment-score"></div><div class="comment-text"><p>What is the filter to find duplicate "ip id" in this case?</p></div><div id="comment-29177-info" class="comment-info"><span class="comment-age">(27 Jan '14, 02:43)</span> <span class="comment-user userinfo">gamermic</span></div></div><span id="29206"></span><div id="comment-29206" class="comment"><div id="post-29206-score" class="comment-score"></div><div class="comment-text"><p>There isn't one.</p><p>Packet filters act only on fields within a single packet; there is, unfortunately, no way to say, for example, "match packets where the value of this field is equal to the value of that field in some previous packet".</p><p>That's also true of capture filters, and, while we might be able to support packet filters that can match fields in previous packets, by adding new syntax for that and new code for that, the way capture filters work inherently makes them stateless (the BPF engine does not keep state between packets), so neither we nor the libpcap/WinPcap developers can make it filter out duplicate IP IDs.</p><p>(And, of course, just because two packets from one IP address to another have the same IP ID, that doesn't mean they're duplicates, and, as Sake noted, that's even <em>more</em> true if the packets didn't all go from host A to host B.)</p></div><div id="comment-29206-info" class="comment-info"><span class="comment-age">(27 Jan '14, 14:51)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-1906" class="comment-tools"></div><div class="clear"></div><div id="comment-1906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

