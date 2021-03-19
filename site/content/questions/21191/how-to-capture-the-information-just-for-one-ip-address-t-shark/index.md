+++
type = "question"
title = "How to capture the information just for one IP ADDRESS? (T-SHARK)"
description = '''Dears I need to capture just the traffic from one ip address in a network (in/out) I use this command in linux : tshark -i 3 -f &quot;host x.x.x.x&quot; -w test.pcap I capture all the traffic when i used that command without the -f &quot;host x.x.x.x&quot; Could you help me? Thanks in advance. BR'''
date = "2013-05-16T11:21:00Z"
lastmod = "2013-05-16T11:34:00Z"
weight = 21191
keywords = [ "ip.addr", "capture-filter", "tshark" ]
aliases = [ "/questions/21191" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture the information just for one IP ADDRESS? (T-SHARK)](/questions/21191/how-to-capture-the-information-just-for-one-ip-address-t-shark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21191-score" class="post-score" title="current number of votes">0</div><span id="post-21191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dears</p><p>I need to capture just the traffic from one ip address in a network (in/out)</p><p>I use this command in linux : tshark -i 3 -f "host x.x.x.x" -w test.pcap</p><p>I capture all the traffic when i used that command without the -f "host x.x.x.x"</p><p>Could you help me?</p><p>Thanks in advance.</p><p>BR</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip.addr" rel="tag" title="see questions tagged &#39;ip.addr&#39;">ip.addr</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '13, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/3198ef28ca50f21cf8dfc095c9b63161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pdrorp&#39;s gravatar image" /><p><span>pdrorp</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pdrorp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 May '13, 11:23</strong> </span></p></div></div><div id="comments-container-21191" class="comments-container"></div><div id="comment-tools-21191" class="comment-tools"></div><div class="clear"></div><div id="comment-21191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21192"></span>

<div id="answer-container-21192" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21192-score" class="post-score" title="current number of votes">1</div><span id="post-21192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As <code>tshark -i 3 -f "host x.x.x.x" -w test.pcap</code> is indeed the right syntax under normal circumstances, I assume this command is not working for you. As you are saying that with the filter you do see all traffic (including traffic to/from host x.x.x.x), there must be some form of encapsulation in your traffic.</p><p>Most likely your packets are vlan tagged, could you try the filter <code>"vlan and host x.x.x.x"</code>? If this does not work, could you capture all packets and then look in Wireshark at all the layers <em>before</em> the IP layer and tell us which protocols are listed before IP?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '13, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21192" class="comments-container"></div><div id="comment-tools-21192" class="comment-tools"></div><div class="clear"></div><div id="comment-21192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

