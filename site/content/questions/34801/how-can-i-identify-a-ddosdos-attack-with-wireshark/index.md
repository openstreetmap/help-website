+++
type = "question"
title = "How can I identify a DDoS/DoS attack with wireshark"
description = ''' I am using wireshark to analyse traffic that I captured with tcpdump but I am not sure if what I see is a DoS attack or port scanning. The file used can be downloaded from here'''
date = "2014-07-21T08:34:00Z"
lastmod = "2014-07-22T03:48:00Z"
weight = 34801
keywords = [ "dos", "ddos", "wireshark", "port", "port-scanning" ]
aliases = [ "/questions/34801" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How can I identify a DDoS/DoS attack with wireshark](/questions/34801/how-can-i-identify-a-ddosdos-attack-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34801-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">2</div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2014-07-21_at_5.20.02_PM.png" alt="alt text" /> I am using wireshark to analyse traffic that I captured with tcpdump but I am not sure if what I see is a DoS attack or port scanning. The file used can be downloaded from <a href="https://dl.dropboxusercontent.com/u/4352965/trafficVN1_245">here</a></p></div><div id="question-tags" class="tags-container tags">dos ddos wireshark port port-scanning</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '14, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/693d320356a3e5d8510f7deaad56a191?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miky7&#39;s gravatar image" /><p>miky7<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miky7 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jul '14, 04:16</p></div></div><div id="comments-container-34801" class="comments-container"></div><div id="comment-tools-34801" class="comment-tools"></div><div class="clear"></div><div id="comment-34801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34820"></span>

<div id="answer-container-34820" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34820-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, doing packet analysis based on a 'blackened' screenshot is nearly impossible! If you want an answer that is even close to the reality, you should post a capture file somewhere (google drive, dropbox, cloudshark.org). If you have any concerns regarding privacy issues, you can anonymize the file with <a href="http://tracewrangler.com/">TraceWrangler</a>, a tool of our member @Jasper.</p><p>Now, based on the screenshot, I don't see any sign for a DDoS (distributed DoS), as there is only <strong>one</strong> IP address <strong>shown</strong> on the screenshot, which is not enough the talk about a <strong>distrubted</strong> DoS (DDoS).</p><p>Regarding a DoS: The screenshot hides the time stamps and there is no information at all what the IO graph is showing. So, it's impossible to tell if this is a DoS or a port scan.</p><p>However, based on my experience with DoS attacks, I'm almost sure that this is <strong>not</strong> a DoS attack, at least not an attack at the protocol level, as the IO graph would look different ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '14, 03:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jul '14, 04:35</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-34820" class="comments-container"><span id="34822"></span><div id="comment-34822" class="comment"><div id="post-34822-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the reply. I will edit the post to include the file</p></div><div id="comment-34822-info" class="comment-info"><span class="comment-age">(22 Jul '14, 04:11)</span> miky7</div></div><span id="34830"></span><div id="comment-34830" class="comment"><div id="post-34830-score" class="comment-score">2</div><div class="comment-text"><p>O.K., with access to the capture file (updated question), this looks much more like an attack, even a bit like an attempt to run a DDoS.</p><p>Reason:</p><ul><li>There are different IP addresses, all trying the same. Not that much addresses, but still</li><li>They are not scanning different ports, they are 'hammering' all on the same ports (DNS, 445, 139, usw.). There is also mostly one target (80.237.252.245), not a range of systems, so this is not a port scan.</li><li>They are sending the same DNS request again and again from different IP addresses (for: lalka.com.ru), which (sometimes) causes a server failure on your server</li></ul><p>So, actually it looks like a DDoS, even though the frequency of the packets is not very high. However: sometimes it's enough to make your DNS server fail, for whatever reason (please check the logs).</p><p>To answer you question in the title:</p><blockquote><p>How can I identify a DDoS/DoS attack with wireshark</p></blockquote><p>I used the function</p><blockquote><p>Statistics -&gt; Conversations</p></blockquote><p>and then I did some sorting in the TCP and UDP tabs. Then, with a bit of experience, you'll easily figure out if it's a port scan or an attempt to run a DDoS attack. See my explanations above.</p></div><div id="comment-34830-info" class="comment-info"><span class="comment-age">(22 Jul '14, 09:00)</span> Kurt Knochner ♦</div></div><span id="34844"></span><div id="comment-34844" class="comment"><div id="post-34844-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for the reply! I also had the same impression but since it is the first time I saw a pcap capture, I was not sure. I also have some SYN flooding from a specific IP but the frequency is still quite low and the number of packets not that high. Perhaps an attempt to fool any IDS software?</p></div><div id="comment-34844-info" class="comment-info"><span class="comment-age">(23 Jul '14, 03:16)</span> miky7</div></div><span id="34863"></span><div id="comment-34863" class="comment"><div id="post-34863-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Perhaps an attempt to fool any IDS software?</p></blockquote><p>maybe.</p><p>Or a test of a new tool. Or the preparation for the 'real' attack. Or kids playing with tools. Impossible to know ...</p></div><div id="comment-34863-info" class="comment-info"><span class="comment-age">(23 Jul '14, 16:30)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-34820" class="comment-tools"></div><div class="clear"></div><div id="comment-34820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

