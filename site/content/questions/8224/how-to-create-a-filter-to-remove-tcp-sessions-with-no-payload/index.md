+++
type = "question"
title = "How to create a filter to remove TCP sessions with no payload"
description = '''Hi all, I haven&#x27;t found a good way to do this yet. Is there a way to filter out TCP sessions that have no payload? (Basically, sessions that have the 3-way handshake and then immediately close via FIN or RST that didn&#x27;t actually transmit any meaningful data). Thanks -VK'''
date = "2012-01-04T13:04:00Z"
lastmod = "2012-01-05T03:33:00Z"
weight = 8224
keywords = [ "filter", "tcp", "payload", "empty" ]
aliases = [ "/questions/8224" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to create a filter to remove TCP sessions with no payload](/questions/8224/how-to-create-a-filter-to-remove-tcp-sessions-with-no-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8224-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I haven't found a good way to do this yet. Is there a way to filter out TCP sessions that have no payload? (Basically, sessions that have the 3-way handshake and then immediately close via FIN or RST that didn't actually transmit any meaningful data).</p><p>Thanks</p><p>-VK</p></div><div id="question-tags" class="tags-container tags">filter tcp payload empty</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '12, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/0509ca4ad1d73368f6fbc1f4f0134c0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VaporKnight&#39;s gravatar image" /><p>VaporKnight<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VaporKnight has no accepted answers">0%</span></p></div></div><div id="comments-container-8224" class="comments-container"></div><div id="comment-tools-8224" class="comment-tools"></div><div class="clear"></div><div id="comment-8224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8225"></span>

<div id="answer-container-8225" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8225-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, display filters work on individual packets, and have no state, so there's no simple display filter to do that. I don't know enough about <a href="http://wiki.wireshark.org/Mate">MATE</a> to say whether it would support that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '12, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8225" class="comments-container"></div><div id="comment-tools-8225" class="comment-tools"></div><div class="clear"></div><div id="comment-8225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8228"></span>

<div id="answer-container-8228" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8228-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could use tshark to create that filter for you :-)</p><p>To find all TCP packets with data, use:</p><pre><code>tshark -r &lt;file&gt; -R &quot;tcp.len&gt;0&quot;</code></pre><p>... we're only interested in the ID's of the TCP sessions that contain data:</p><pre><code>tshark -r &lt;file&gt; -R &quot;tcp.len&gt;0&quot; -T fields -e tcp.stream</code></pre><p>Then use some shell magic to create a list of all these session ID's:</p><pre><code>tshark -r &lt;file&gt; -R &quot;tcp.len&gt;0&quot; -T fields -e tcp.stream |\
    sort -n | uniq</code></pre><p>... and transform it into a display filter:</p><pre><code>tshark -r &lt;file&gt; -R &quot;tcp.len&gt;0&quot; -T fields -e tcp.stream |\
    sort -n | uniq |\
    awk &#39;{printf(&quot;%stcp.stream==%d&quot;,sep,$1);sep=&quot;||&quot;}&#39;</code></pre><p>You can then use that filter in Wireshark. Or you can create a new tracefile with only the sessions containing data in one run with:</p><pre><code>tshark -r &lt;file&gt; - w &lt;newfile&gt; -R $(\
    tshark -r &lt;file&gt; -R &quot;tcp.len&gt;0&quot; -T fields -e tcp.stream |\
        sort -n | uniq |\
        awk &#39;{printf(&quot;%stcp.stream==%d&quot;,sep,$1);sep=&quot;||&quot;}&#39;\
)</code></pre><p>Hope this helps!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '12, 03:33</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-8228" class="comments-container"><span id="8231"></span><div id="comment-8231" class="comment"><div id="post-8231-score" class="comment-score"></div><div class="comment-text"><p>That will work for me!</p><p>Thanks!</p><p>-VK</p></div><div id="comment-8231-info" class="comment-info"><span class="comment-age">(05 Jan '12, 08:22)</span> VaporKnight</div></div><span id="8237"></span><div id="comment-8237" class="comment"><div id="post-8237-score" class="comment-score"></div><div class="comment-text"><p>Hmm.. Actually this didn't work. When I do the -e tcp.stream I don't get Stream ID's returned. I just get a lot of empty lines.</p><p>When I do things like tcp.seq or tcp.ack I do see some values. So this seems specific to tcp.stream. In wireshark I can see the steam IDs.</p><p>-VK</p></div><div id="comment-8237-info" class="comment-info"><span class="comment-age">(05 Jan '12, 11:38)</span> VaporKnight</div></div><span id="8238"></span><div id="comment-8238" class="comment"><div id="post-8238-score" class="comment-score"></div><div class="comment-text"><p>This works for me with TShark 1.7.0 (SVN 39768) in Windows 7 (64-bit). I ran:</p><pre><code>tshark -r nfs_bad_stalls.cap -R &quot;tcp.len&gt;0&quot; -T fields -e tcp.stream |\
        sort -n | uniq |\
        awk &#39;{printf(&quot;%stcp.stream==%d&quot;,sep,$1);sep=&quot;||&quot;}&#39;</code></pre><p>which yields:</p><pre><code>tcp.stream==0||tcp.stream==1||tcp.stream==2||tcp.stream==3</code></pre></div><div id="comment-8238-info" class="comment-info"><span class="comment-age">(05 Jan '12, 12:06)</span> bstn</div></div><span id="8239"></span><div id="comment-8239" class="comment"><div id="post-8239-score" class="comment-score"></div><div class="comment-text"><p>Hmm.. maybe need to update then.</p><p>Running tshark 1.0.2 on Linux. I'll try that.</p><p>-VK</p></div><div id="comment-8239-info" class="comment-info"><span class="comment-age">(05 Jan '12, 12:09)</span> VaporKnight</div></div><span id="8240"></span><div id="comment-8240" class="comment"><div id="post-8240-score" class="comment-score"></div><div class="comment-text"><p>Works on 1.6.0 Thanks!</p><p>-VK</p></div><div id="comment-8240-info" class="comment-info"><span class="comment-age">(05 Jan '12, 12:16)</span> VaporKnight</div></div><span id="8241"></span><div id="comment-8241" class="comment not_top_scorer"><div id="post-8241-score" class="comment-score"></div><div class="comment-text"><p>Yes, the <code>tcp.stream</code> field may not have existed in Wireshark 1.0.x.</p></div><div id="comment-8241-info" class="comment-info"><span class="comment-age">(05 Jan '12, 12:24)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-8228" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-8228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

