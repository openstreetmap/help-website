+++
type = "question"
title = "tshark filters using &quot;and&quot; vs &quot;&amp;&amp;&quot;"
description = '''Hi,  I am trying to build a capture filter on some traffic which contains VLAN tags. The frames happen to contain two VLAN tags. I don&#x27;t really care what VLANs they are, as I am mainly interested in the destination IP and port number. If I use this capture filter below, I dont see any traffic:  tsha...'''
date = "2012-05-21T06:59:00Z"
lastmod = "2012-05-23T08:31:00Z"
weight = 11175
keywords = [ "capture-filter", "vlan" ]
aliases = [ "/questions/11175" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark filters using "and" vs "&&"](/questions/11175/tshark-filters-using-and-vs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11175-score" class="post-score" title="current number of votes">0</div><span id="post-11175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to build a capture filter on some traffic which contains VLAN tags. The frames happen to contain two VLAN tags. I don't really care what VLANs they are, as I am mainly interested in the destination IP and port number.</p><p>If I use this capture filter below, I dont see any traffic:</p><pre><code>tshark -i eth1 vlan and host 192.168.0.1</code></pre><p>However, if I change my filter to this:</p><pre><code>tshark -i eth1 vlan &amp;&amp; host 192.168.0.1</code></pre><p>everything works fine. Does anyone know the difference between using <code>"and"</code> vs <code>"&amp;&amp;"</code>? Does it have anything to do with the multiple VLAN tags?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '12, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/f2bbd13bf5334ec9e59716106e3a6542?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gian%20Sartor&#39;s gravatar image" /><p><span>Gian Sartor</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gian Sartor has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 May '12, 15:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11175" class="comments-container"></div><div id="comment-tools-11175" class="comment-tools"></div><div class="clear"></div><div id="comment-11175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11180"></span>

<div id="answer-container-11180" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11180-score" class="post-score" title="current number of votes">4</div><span id="post-11180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong><code>&amp;&amp;</code></strong> has a special meaning in your shell.</p><blockquote><p><code>command1 &amp;&amp; command2</code><br />
<code>command2 is executed if, and only if, command1 returns an exit status of zero.</code><br />
</p></blockquote><p>So, the difference between your two commands is:</p><p>The command:</p><blockquote><p><code>tshark -ni eth1 vlan and host 192.168.0.1</code><br />
</p></blockquote><p>shows only VLAN tagged traffic to and from host 192.168.0.1.</p><p>The command:</p><blockquote><p><code>tshark -ni eth1 vlan &amp;&amp; host 192.168.0.1</code></p></blockquote><p>runs actually just this command (due the the special meaning of &amp;&amp;):</p><blockquote><p><code>tshark -ni eth1 vlan</code><br />
</p></blockquote><p><code>tshark</code> will show any VLAN tagged traffic (without host filter). If that command exits with code 0, the shell would then run this command:</p><blockquote><p><code>host 192.168.0.1</code><br />
</p></blockquote><p>The result of the <code>host</code> command (if installed on your system) would be something like this:</p><blockquote><p><code>Host 1.0.168.192.in-addr.arpa. not found: 3(NXDOMAIN)</code><br />
</p></blockquote><p>BTW: If you want to use <code>&amp;&amp;</code> in the capture filter, you'll have to "escape" it for the shell with single quotes.</p><blockquote><p><code>tshark -ni eth1 'vlan &amp;&amp; host 192.168.0.1'</code><br />
</p></blockquote><p>This is identical to:</p><blockquote><p><code>tshark -ni eth1 'vlan and host 192.168.0.1'</code><br />
<code>tshark -ni eth1 vlan and host 192.168.0.1</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '12, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 May '12, 15:04</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></br></p></div></div><div id="comments-container-11180" class="comments-container"><span id="11185"></span><div id="comment-11185" class="comment"><div id="post-11185-score" class="comment-score"></div><div class="comment-text"><p>(Presumably, no vlan traffic is going to or from 192.168.0.1, so a filter that tests for both will see no packets, but a filter testing only for VLAN frames will see packets. From the point of view of libpcap/WnPcap, which both tcpdump and Wireshark use for capture filters, <code>and</code> and <code>&amp;&amp;</code> behave exactly the same.)</p></div><div id="comment-11185-info" class="comment-info"><span class="comment-age">(21 May '12, 09:55)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="11259"></span><div id="comment-11259" class="comment"><div id="post-11259-score" class="comment-score">1</div><div class="comment-text"><p>Kurt, thanks for your response. this makes perfect sense now. So although I was seeing traffic which contained vlan tags, the filter by host wasn't actually getting applied... gotcha!</p><p>Incidentally, I had a few more attempts on the filter for packets with multiple vlan tags and I think I got it working. This is what I ended up with -</p><p>tshark -i eth1 "vlan and (vlan and host 192.168.0.1)"</p><p>Thanks again Gian</p></div><div id="comment-11259-info" class="comment-info"><span class="comment-age">(23 May '12, 07:57)</span> <span class="comment-user userinfo">Gian Sartor</span></div></div><span id="11260"></span><div id="comment-11260" class="comment"><div id="post-11260-score" class="comment-score"></div><div class="comment-text"><p>Gian,</p><blockquote><p><code>tshark -i eth1 "vlan and (vlan and host 192.168.0.1)"</code></p></blockquote><p>you don't need vlan twice. This should be equivalent to your command:</p><blockquote><p><code>tshark -i eth1 "vlan and host 192.168.0.1"</code></p></blockquote></div><div id="comment-11260-info" class="comment-info"><span class="comment-age">(23 May '12, 08:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11261"></span><div id="comment-11261" class="comment"><div id="post-11261-score" class="comment-score">2</div><div class="comment-text"><p>Kurt,</p><pre><code>tshark -i eth1 &quot;vlan and (vlan and host 192.168.0.1)&quot;</code></pre><p>Will look for an IP address after <em>TWO</em> vlan headers (ie Q-in-Q), which is different from what happens when using the vlan directive once. As Gian said: "I had a few more attempts on the filter for packets with multiple vlan tags" :-)</p><p>(yes, my first reaction was also: "Hey, you don't need two vlan directives"!)</p></div><div id="comment-11261-info" class="comment-info"><span class="comment-age">(23 May '12, 08:19)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="11262"></span><div id="comment-11262" class="comment"><div id="post-11262-score" class="comment-score"></div><div class="comment-text"><blockquote><p>packets with multiple vlan tags</p></blockquote><p>Ah, good catch :-) Thanks for the hint...</p></div><div id="comment-11262-info" class="comment-info"><span class="comment-age">(23 May '12, 08:31)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-11180" class="comment-tools"></div><div class="clear"></div><div id="comment-11180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

