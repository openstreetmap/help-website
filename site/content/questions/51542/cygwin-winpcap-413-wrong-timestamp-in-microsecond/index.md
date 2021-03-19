+++
type = "question"
title = "Cygwin + WinPcap 4.1.3 - Wrong Timestamp in Microsecond"
description = '''Hi, I am working on developing a customized packet sniffer for Windows 7 64 bit host system (NIC card is Realtek PCIe GBE Family Controller) and am using WinPcap 4.3.1 library using C programming and Cygwin development platform. I am able to read outgoing and incoming TCP and UDP packets through my ...'''
date = "2016-04-09T22:24:00Z"
lastmod = "2016-04-11T15:49:00Z"
weight = 51542
keywords = [ "winpcap", "cygwin", "microsecond", "pcap_pkthdr", "wrongtimestamp" ]
aliases = [ "/questions/51542" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Cygwin + WinPcap 4.1.3 - Wrong Timestamp in Microsecond](/questions/51542/cygwin-winpcap-413-wrong-timestamp-in-microsecond)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51542-score" class="post-score" title="current number of votes">0</div><span id="post-51542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am working on developing a customized packet sniffer for Windows 7 64 bit host system (NIC card is Realtek PCIe GBE Family Controller) and am using WinPcap 4.3.1 library using C programming and Cygwin development platform. I am able to read outgoing and incoming TCP and UDP packets through my program. However, I am stuck in a problem of not able to get correct timestamp in microsecond from the <strong>struct pcap_pkthdr</strong> structure. Following is the code snippet from the program where the problem exists:</p><pre><code>...

int getPacket; 
struct pcap_pkthdr *header;  
const u_char *pkt_data;  
/* Sniff the packets */  
while((getPacket= pcap_next_ex(handle, &amp;header, &amp;pkt_data)) &gt;= 0)   
{      
printf(&quot;\n 1) Epoch is: %ld&quot;,header-&gt;ts.tv_sec&amp;0x00000000ffffffff);     
printf(&quot;\n 2) Microsecond is:  %ld&quot;,header-&gt;ts.tv_usec);

...</code></pre><p>Following is the <strong>console output</strong> that I got for these 2 printf() statements in a run:<br />
</p><p>1) Epoch is: 1460262399<br />
2) Microsecond is: 1576252997999<br />
</p><p>Time in seconds (header-&gt;ts.tv_sec&amp;0x00000000ffffffff) is correct as it translates to 2016-04-09::23:26:39 (<strong>yy-mm-dd::hh-mm-ss</strong> format)<br />
</p><p>However, the Microsecond (header-&gt;ts.tv_usec) is not correct as the hex value of Microsecond is <strong>0x16F0000016F</strong> that always shows this kind of repeating pattern (with different values) at the low and high octet positions. I have analyzed memory dumps and found the same values that makes me believe that the <strong>header-&gt;ts.tv_usec</strong> is not filled correctly by the NPF driver.<br />
</p><p>I did a lot of search and could not find this issue reported anywhere. Also, I tested the code on separate AMD and Intel machines and the issue seems to linger.<br />
</p><p>Any suggestion(s) to solve this problem would be highly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span> <span class="post-tag tag-link-cygwin" rel="tag" title="see questions tagged &#39;cygwin&#39;">cygwin</span> <span class="post-tag tag-link-microsecond" rel="tag" title="see questions tagged &#39;microsecond&#39;">microsecond</span> <span class="post-tag tag-link-pcap_pkthdr" rel="tag" title="see questions tagged &#39;pcap_pkthdr&#39;">pcap_pkthdr</span> <span class="post-tag tag-link-wrongtimestamp" rel="tag" title="see questions tagged &#39;wrongtimestamp&#39;">wrongtimestamp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '16, 22:24</strong></p><img src="https://secure.gravatar.com/avatar/daadfa96cddb86e4d6cff5f022b0dd7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Han&#39;s gravatar image" /><p><span>Han</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Han has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Apr '16, 15:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></br></p></div></div><div id="comments-container-51542" class="comments-container"><span id="51543"></span><div id="comment-51543" class="comment"><div id="post-51543-score" class="comment-score">1</div><div class="comment-text"><p>Not really an Ask Wireshark question, but anyway.</p><p>Presumably you mean WinPcap 4.1.3. You say you're using Cygwin, I'm not sure mixing Cygwin and WinPcap works.</p><p>Wireshark seems to be able to use WinPcap to retrieve packets with microsecond precision, unless it's just making them up, and it uses the same field in the packet header.</p><p>dumpcap is the Wireshark process that interfaces with WinPcap, maybe looking at the code in <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=dumpcap.c;h=a44d4f0d3627f1a39c659136e636fd4564704524;hb=HEAD">dumpcap.c</a> might help.</p></div><div id="comment-51543-info" class="comment-info"><span class="comment-age">(10 Apr '16, 04:39)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51561"></span><div id="comment-51561" class="comment"><div id="post-51561-score" class="comment-score"></div><div class="comment-text"><p>Thanks Grahamb. I posted this question because there is no help available on this behavior anywhere and as Wireshark is using WinPcap therefore, I though it might be a good idea to ask folks here. Sorry for the typo that is corrected. I am getting other fields correctly from Cygwin based C code so I believe it works fine with other packet data structures but microsecond field is not correct. I checked dumpcap.c but they seem to use the same functions which kind of perplexes me more. I need microsecond stamp for my task and still not sure how to debug it. NPF driver works fine for other data fields but somehow fills microseconds incorrectly (as I figured out).</p></div><div id="comment-51561-info" class="comment-info"><span class="comment-age">(11 Apr '16, 12:52)</span> <span class="comment-user userinfo">Han</span></div></div><span id="51563"></span><div id="comment-51563" class="comment"><div id="post-51563-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Not really an Ask Wireshark question</p></blockquote><p>Yes, it's more of a <a href="http://stackoverflow.com/questions/36526071/winpcap-4-1-3-timestamp-microsecond-issue-header-ts-tv-usec-not-correct-c">stackoverflow question</a>.</p><blockquote><p>I'm not sure mixing Cygwin and WinPcap works</p></blockquote><p>I'm not sure, either. WinPcap expects <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/ms740560(v=vs.85).aspx">MSVC's definition of struct timeval</a>, and Cygwin's might be different.</p></div><div id="comment-51563-info" class="comment-info"><span class="comment-age">(11 Apr '16, 14:40)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-51542" class="comment-tools"></div><div class="clear"></div><div id="comment-51542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51567"></span>

<div id="answer-container-51567" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51567-score" class="post-score" title="current number of votes">1</div><span id="post-51567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Han has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://stackoverflow.com/questions/36526071/winpcap-4-1-3-timestamp-microsecond-issue-header-ts-tv-usec-not-correct-c">Cygwin issue</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '16, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-51567" class="comments-container"></div><div id="comment-tools-51567" class="comment-tools"></div><div class="clear"></div><div id="comment-51567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

