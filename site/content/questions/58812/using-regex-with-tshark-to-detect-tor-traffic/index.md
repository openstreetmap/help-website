+++
type = "question"
title = "Using regex with tshark to detect tor traffic"
description = '''I&#x27;ve been playing around with tshark to detect tor traffic. In the article below I&#x27;ve found some interesting information with a tshark command that I&#x27;ve used: https://www.rsreese.com/detecting-tor-traffic-with-bro-network-traffic-analyzer/ tshark -r tor.pcap -T fields -Y &quot;ssl.handshake.certificate&quot; ...'''
date = "2017-01-16T07:38:00Z"
lastmod = "2017-01-19T06:49:00Z"
weight = 58812
keywords = [ "tor", "ssl", "handshake", "tshark", "regex" ]
aliases = [ "/questions/58812" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using regex with tshark to detect tor traffic](/questions/58812/using-regex-with-tshark-to-detect-tor-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58812-score" class="post-score" title="current number of votes">0</div><span id="post-58812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been playing around with tshark to detect tor traffic. In the article below I've found some interesting information with a tshark command that I've used:</p><p><a href="https://www.rsreese.com/detecting-tor-traffic-with-bro-network-traffic-analyzer/">https://www.rsreese.com/detecting-tor-traffic-with-bro-network-traffic-analyzer/</a></p><p><code>tshark -r tor.pcap -T fields -Y "ssl.handshake.certificate" -e x509af.utcTime -e x509sat.uTF8String</code></p><p>Then I noticed I also got to see a lot of non-tor related certificates. So I used the following display filter in Wireshark which worked fine. I only got to see the tor certificate (in this example, I haven't tested it on a large pcap with lots of other traffic):</p><p><code>ssl.handshake.certificate &amp;&amp; x509sat.uTF8String matches "www.[A-Za-z0-9.-]+.(com|net)"</code></p><p>Then I tried to combine the filter from the article on rsreese.com, with the regex mentioned before to apply an extra filter, since many address in that field just start with a dot (.) instead of 'www'. The line of code below is just one of many variations I tried, it just doesn't seem to work.</p><p><code>tshark.exe -r tor.pcap -T fields -Y "ssl.handshake.certificate" -e x509af.utcTime -e "x509sat.uTF8String matches "www\.[A-Za-z0-9.-]+\.(com|net)""</code></p><p>Then I got the following error:</p><pre><code>tshark: Some fields aren&#39;t valid
x509sat.uTF8String matches &quot;www\.[A-Za-z0-9.-]+\.(com|net)</code></pre><p>Does this mean that regex filters doesn't work with tshark or did I missed something else? Because the specific filter did worked in Wireshark itself. Thanks in advance for any input! :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tor" rel="tag" title="see questions tagged &#39;tor&#39;">tor</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-handshake" rel="tag" title="see questions tagged &#39;handshake&#39;">handshake</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-regex" rel="tag" title="see questions tagged &#39;regex&#39;">regex</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '17, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/1bd7aa9ec4636e9d234ddfb63bb15f85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r00t070&#39;s gravatar image" /><p><span>r00t070</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r00t070 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jan '17, 09:21</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-58812" class="comments-container"><span id="58813"></span><div id="comment-58813" class="comment"><div id="post-58813-score" class="comment-score"></div><div class="comment-text"><p>-e is not a filter, it's field extractor. Move it to -Y.</p></div><div id="comment-58813-info" class="comment-info"><span class="comment-age">(16 Jan '17, 08:31)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="58817"></span><div id="comment-58817" class="comment"><div id="post-58817-score" class="comment-score"></div><div class="comment-text"><p>That doesn't work either. I tried many variations of commands with the regex part (-Y, -R, -e), so that's why the example above is showing -e right now. Nothing worked so far. So that's why I'm wondering if searching using a regex even works in tshark?</p></div><div id="comment-58817-info" class="comment-info"><span class="comment-age">(16 Jan '17, 08:57)</span> <span class="comment-user userinfo">r00t070</span></div></div><span id="58818"></span><div id="comment-58818" class="comment"><div id="post-58818-score" class="comment-score"></div><div class="comment-text"><p>Is it a problem of quoting, not sure what shell you're using, try:</p><pre><code>tshark.exe -r tor.pcap -T fields -e x509af.utcTime -Y &quot;ssl.handshake.certificate and x509sat.uTF8String matches &#39;www\.[A-Za-z0-9.-]+\.(com|net)&#39;&quot;</code></pre></div><div id="comment-58818-info" class="comment-info"><span class="comment-age">(16 Jan '17, 09:37)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="58826"></span><div id="comment-58826" class="comment"><div id="post-58826-score" class="comment-score"></div><div class="comment-text"><p>I tried that as well. Using your example I get the error: - tshark: "www" was unexpected in this context. Then changing quotes again I got: - tshark: Display filters were specified both with "-d" and with additional command-line arguments. I'm working with Windows 7 command-prompt. I know there are probably other and easier ways to do this, but I need to do it this way because I can't use and install any other software.</p></div><div id="comment-58826-info" class="comment-info"><span class="comment-age">(16 Jan '17, 23:12)</span> <span class="comment-user userinfo">r00t070</span></div></div></div><div id="comment-tools-58812" class="comment-tools"></div><div class="clear"></div><div id="comment-58812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58840"></span>

<div id="answer-container-58840" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58840-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58840-score" class="post-score" title="current number of votes">2</div><span id="post-58840-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can try escaping the inner quotes instead:</p><pre><code>tshark.exe -r tor.pcap -T fields -e x509af.utcTime -Y &quot;ssl.handshake.certificate and x509sat.uTF8String matches \&quot;www\.[A-Za-z0-9.-]+\.(com|net)\&quot;&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '17, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-58840" class="comments-container"><span id="58843"></span><div id="comment-58843" class="comment"><div id="post-58843-score" class="comment-score"></div><div class="comment-text"><p>Chris's answer works for me in a Cmd shell, now that the OP has identified their shell so the correct quoting rules can be supplied.</p></div><div id="comment-58843-info" class="comment-info"><span class="comment-age">(17 Jan '17, 09:32)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="58883"></span><div id="comment-58883" class="comment"><div id="post-58883-score" class="comment-score"></div><div class="comment-text"><p>Chris, thanks for pointing out escaping the quotes. Although your answer didn't worked, I found out the answer was to use "double double-quotes to escape the double-quote" :P. Thanks for all the input everyone!</p><ul><li><a href="https://ask.wireshark.org/questions/5241/tshark-display-filter-in-windows-command-line-seems-not-support-special-characters">https://ask.wireshark.org/questions/5241/tshark-display-filter-in-windows-command-line-seems-not-support-special-characters</a></li></ul><p>The command below now semi-works. I don't get any errors and it creates some output. However it isn't quite doing what I'm looking for yet, so I still have to do some fine-tuning.</p><ul><li>tshark.exe -r tor.pcap -T fields -e x509af.utcTime -Y "ssl.handshake.certificate and x509sat.uTF8String matches ""www.[A-Za-z0-9.-]+.(com|net)"""</li></ul></div><div id="comment-58883-info" class="comment-info"><span class="comment-age">(19 Jan '17, 06:49)</span> <span class="comment-user userinfo">r00t070</span></div></div></div><div id="comment-tools-58840" class="comment-tools"></div><div class="clear"></div><div id="comment-58840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

