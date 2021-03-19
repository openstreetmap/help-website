+++
type = "question"
title = "How to filter for Out of Sequence packets based on IP Identification number?"
description = '''Hi I&#x27;ve currently got a problem where traffic is being delivered out of sequence over an MPLS link. The traffic is UDP and the only way that I can see the OOS packets is by the IP Identification field. However as the link is a WAN link and the problem is intermitent then there is a lot a lot of traf...'''
date = "2013-06-14T03:36:00Z"
lastmod = "2013-06-14T11:18:00Z"
weight = 22052
keywords = [ "ip", "mpls", "identification", "sequence", "display-filter" ]
aliases = [ "/questions/22052" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter for Out of Sequence packets based on IP Identification number?](/questions/22052/how-to-filter-for-out-of-sequence-packets-based-on-ip-identification-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22052-score" class="post-score" title="current number of votes">0</div><span id="post-22052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I've currently got a problem where traffic is being delivered out of sequence over an MPLS link. The traffic is UDP and the only way that I can see the OOS packets is by the IP Identification field. However as the link is a WAN link and the problem is intermitent then there is a lot a lot of traffic to work through. Therefore does anyone now how to apply a display filter that will identify any OOS packets based on the IP Identification number?</p><p>Any thoughts appreciated.</p><p>Thanks</p><p>Malcolm</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-mpls" rel="tag" title="see questions tagged &#39;mpls&#39;">mpls</span> <span class="post-tag tag-link-identification" rel="tag" title="see questions tagged &#39;identification&#39;">identification</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '13, 03:36</strong></p><img src="https://secure.gravatar.com/avatar/ebc254212328da771cca6c07e91c9ef8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Malcolm&#39;s gravatar image" /><p><span>Malcolm</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Malcolm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jun '13, 20:11</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-22052" class="comments-container"><span id="22065"></span><div id="comment-22065" class="comment"><div id="post-22065-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>Thanks for your responses. I used the CSV approach and exported it excel and then looked for differences and it worked really well.</p><p>Thanks again for your help.</p><p>Malcolm</p></div><div id="comment-22065-info" class="comment-info"><span class="comment-age">(14 Jun '13, 08:36)</span> <span class="comment-user userinfo">Malcolm</span></div></div><span id="22071"></span><div id="comment-22071" class="comment"><div id="post-22071-score" class="comment-score"></div><div class="comment-text"><p>If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-22071-info" class="comment-info"><span class="comment-age">(14 Jun '13, 11:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-22052" class="comment-tools"></div><div class="clear"></div><div id="comment-22052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="22053"></span>

<div id="answer-container-22053" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22053-score" class="post-score" title="current number of votes">2</div><span id="post-22053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Malcolm has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If I get you right, you want to have a display filter for packets having OOS IP ID right? I'm not aware of anything like that due to wireshark being unable to filter for something like "ip.id &lt; (lastframe ip.id)" or other conditional stuff.</p><p>As a quick workaround for those cases, I always filter for the source IP I'm interested in, apply a coloumn for IP ID in that case -&gt; and export the whole bunch to a .csv file.</p><p>With this one you can use e.g. excel to quickly build a "delta" coloumn for IP IDs, displaying the difference to the line above and by that spot OOS very quickly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '13, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-22053" class="comments-container"></div><div id="comment-tools-22053" class="comment-tools"></div><div class="clear"></div><div id="comment-22053-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22054"></span>

<div id="answer-container-22054" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22054-score" class="post-score" title="current number of votes">2</div><span id="post-22054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A Lua script might be able to do that.</p><p>Or tshark with some cli-fu:</p><pre><code>tshark -r &lt;file&gt; -R &quot;udp.port==xxx&quot; -T fields -e frame.number -e ip.id  |\
    awk --non-decimal-data &#39;$1&gt;1 &amp;&amp; ($2&lt;lastipid || $2+64512&lt;lastipid) {printf &quot;%d : %d (last %d)\n&quot;,$1,$2,lastipid} {lastipid=$2}&#39;</code></pre><p>Running this on an UDP trace I have results in output like this:</p><pre><code>761 : 8441 (last 44316)
1430 : 18630 (last 44560)
1854 : 6376 (last 44796)
2658 : 45035 (last 58035)</code></pre><p>Of course if you have multiple sessions in your trace, you either need to do some session housekeeping in awk or you can loop over all sessions with a little script.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '13, 04:46</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jun '13, 04:47</strong> </span></p></div></div><div id="comments-container-22054" class="comments-container"></div><div id="comment-tools-22054" class="comment-tools"></div><div class="clear"></div><div id="comment-22054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22056"></span>

<div id="answer-container-22056" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22056-score" class="post-score" title="current number of votes">1</div><span id="post-22056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Either use one of the already mentioned methods (<span><span>@Landi</span></span> or <span><span>@SYN-bit</span></span>), or capture at both sides of the MPLS (you just need the IP header, not the full payload), then run tshark (command below) and compare the tshark output with diff (Linux) or <a href="http://winmerge.org/">WinMerge</a> (OpenSource Windows tool).</p><blockquote><p><code>tshark -nr site-a.pcap -T fields -e frame.number -e ip.id &gt; site-a.txt</code><br />
<code>tshark -nr site-b.pcap -T fields -e frame.number -e ip.id &gt; site-b.txt</code><br />
</p></blockquote><p>Then compare the files site-a.txt and site-b.txt.</p><blockquote><p><code>diff site-a.txt site-b.txt</code><br />
</p></blockquote><p>Or use <a href="http://winmerge.org/">WinMerge</a> on Windows.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '13, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jun '13, 06:28</strong> </span></p></div></div><div id="comments-container-22056" class="comments-container"></div><div id="comment-tools-22056" class="comment-tools"></div><div class="clear"></div><div id="comment-22056-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

