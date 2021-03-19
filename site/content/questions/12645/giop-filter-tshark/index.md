+++
type = "question"
title = "GIOP filter - tshark"
description = '''Hi, im trying to filter all GIOP packets with a filter parameter.  I know it works in wireshark by just typing &quot;giop&quot; in the filter - but it wont work when i use it as a parameter?  tshark -i eth0 -f &quot;´ip --.--.--.-- proto giop´&quot; -w /---/---/---/file.log - wont work... I cant figure out the right sy...'''
date = "2012-07-12T00:02:00Z"
lastmod = "2012-07-12T05:38:00Z"
weight = 12645
keywords = [ "filter", "giop", "parameters", "tshark" ]
aliases = [ "/questions/12645" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [GIOP filter - tshark](/questions/12645/giop-filter-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12645-score" class="post-score" title="current number of votes">0</div><span id="post-12645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>im trying to filter all GIOP packets with a filter parameter. I know it works in wireshark by just typing "giop" in the filter - but it wont work when i use it as a parameter?</p><p><code>tshark -i eth0 -f "´ip --.--.--.-- proto giop´" -w /---/---/---/file.log</code> - wont work...</p><p>I cant figure out the right syntax for this filter. Can anyone help here?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-giop" rel="tag" title="see questions tagged &#39;giop&#39;">giop</span> <span class="post-tag tag-link-parameters" rel="tag" title="see questions tagged &#39;parameters&#39;">parameters</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '12, 00:02</strong></p><img src="https://secure.gravatar.com/avatar/91e61c966dc5c010206a140a84922525?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarkChaosRabbit&#39;s gravatar image" /><p><span>DarkChaosRabbit</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarkChaosRabbit has no accepted answers">0%</span></p></div></div><div id="comments-container-12645" class="comments-container"></div><div id="comment-tools-12645" class="comment-tools"></div><div class="clear"></div><div id="comment-12645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12648"></span>

<div id="answer-container-12648" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12648-score" class="post-score" title="current number of votes">0</div><span id="post-12648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <a href="http://www.wireshark.org/docs/man-pages/tshark.html#f_capture_filter"><code>-f</code></a> flag is used to specify a <a href="http://wiki.wireshark.org/CaptureFilters">capture filter</a> (in <a href="http://biot.com/capstats/bpf.html">BPF syntax</a>). I don't know what the capture filter would be for GIOP. Perhaps you meant to use a <a href="http://wiki.wireshark.org/DisplayFilters">display filter</a> (with the <a href="http://www.wireshark.org/docs/man-pages/tshark.html#read"><code>-R</code></a> flag), which in your case would be:</p><pre><code>tshark -i eth0 -R &quot;ip.addr==1.2.3.4 and giop&quot; -w /path/to/file.log</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '12, 00:44</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-12648" class="comments-container"></div><div id="comment-tools-12648" class="comment-tools"></div><div class="clear"></div><div id="comment-12648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12650"></span>

<div id="answer-container-12650" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12650-score" class="post-score" title="current number of votes">0</div><span id="post-12650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As HelloWorld mentioned, the "-f" is used for a BPF capture filter. Capture filters are much more limited in how they filter as they need to be as fast as possible to not drop packets while captureing due to filter processing overhead.</p><p>From the <a href="http://wiki.wireshark.org/GIOP">Wireshark Wiki</a>:</p><pre><code>Display Filter

A complete list of GIOP display filter fields can be found in the display filter reference

    Show only the GIOP based traffic:  giop

Capture Filter

You cannot directly filter GIOP protocols while capturing. However, if you know the TCP port used (see above), you can filter on that one.</code></pre><p>So if you know your GIOP traffic runs on tcp port 2107, you can use the command:</p><pre><code>tshark -i eth0 -s0 -w giop.pcap -f &quot;host x.x.x.x and tcp port 2107&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '12, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-12650" class="comments-container"><span id="12652"></span><div id="comment-12652" class="comment"><div id="post-12652-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>thanks for the explanation and the answers.</p><p>But neither of them worked :/</p><p><code>tshark -i eth0 -s0 -w giop.pcap -f "host x.x.x.x and tcp port 2107</code></p><p>its slightly wrong isn't it? "-w" is for writing in a file so i changed it to "-R". But the mainproblem is:</p><p>Helloworlds answer produces an Error "ip.addr==XX.XXX.X.XX: command not found"</p><p>Thats the syntax? "<code>ip.addr==1.2.3.4 and giop</code>" - like `+"+command...</p><p>If i try with "<code>-R giop.pcap</code>" its also a "command not found"</p></div><div id="comment-12652-info" class="comment-info"><span class="comment-age">(12 Jul '12, 04:44)</span> <span class="comment-user userinfo">DarkChaosRabbit</span></div></div><span id="12653"></span><div id="comment-12653" class="comment"><div id="post-12653-score" class="comment-score"></div><div class="comment-text"><p><span>@DarkChaosRabbit</span>, Can you post the exact commands you're entering and the resulting output? And fyi, <code>-R</code> specifies a display filter, as already mentioned. To read <code>giop.pcap</code>, use <code>-r giop.pcap</code>.</p></div><div id="comment-12653-info" class="comment-info"><span class="comment-age">(12 Jul '12, 05:01)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="12654"></span><div id="comment-12654" class="comment"><div id="post-12654-score" class="comment-score"></div><div class="comment-text"><p>Could you also explain what you try to do a bit more, because I think I am interpreting your question in a different way than the way you meant it.</p><p>My interpretation of your question:</p><p>I used wireshark and used a filter to only display giop traffic and now I want to use tshark on the CLI to <strong>capture</strong> only giop traffic from one particular host and save it to a file named /---/---/---/file.log</p></div><div id="comment-12654-info" class="comment-info"><span class="comment-age">(12 Jul '12, 05:06)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="12658"></span><div id="comment-12658" class="comment"><div id="post-12658-score" class="comment-score"></div><div class="comment-text"><p>I Will explain what i needed it for.</p><p>As a result, just as SYN-bit thought, i want a file with all the GIOP traffic between 2 specific hosts.</p><p>Now i tried and tried and i think i got a solution.</p><p>Like you said, it is not possible to filter giop while capturing. So i create a file with</p><p>"<code>tshark -i eth1 -f "src host XX.XX.XX.XXX or dst host XX.XX.XX.XXY" -w /file/path/..</code>"</p><p>after i got the file with only the packages of these two hosts:</p><p>"<code>tshark -R "ip.src==XX.XX.XX.XXX or ip.srcXX.XX.XX.XXY and giop" -r /file/path/..</code>"</p><p>i know i could just use "<code>giop</code>" in the second statement but just in case ...</p><p>Its as simple as that. But there were a few errors i just didn't understand because i dont work frequently with wireshark...</p><p>Thanks a lot! (I could say sorry for my english - but i cant do better - so that would be pointless ;) )</p></div><div id="comment-12658-info" class="comment-info"><span class="comment-age">(12 Jul '12, 05:38)</span> <span class="comment-user userinfo">DarkChaosRabbit</span></div></div></div><div id="comment-tools-12650" class="comment-tools"></div><div class="clear"></div><div id="comment-12650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

