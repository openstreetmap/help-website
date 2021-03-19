+++
type = "question"
title = "iptrace aix - editcap and tshark"
description = '''Hello, I often have to look at aix iptrace and cannot use editcap to split the trace unless I specify the -F nettl option. I prefer to use the pcapng format these days for its annotation features. Is there any reason why aic iptraces cannot be converted into pcapng?'''
date = "2013-04-03T09:39:00Z"
lastmod = "2013-04-11T19:06:00Z"
weight = 20062
keywords = [ "iptrace", "pcapng", "editcap", "aix", "tshark" ]
aliases = [ "/questions/20062" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [iptrace aix - editcap and tshark](/questions/20062/iptrace-aix-editcap-and-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20062-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I often have to look at aix iptrace and cannot use editcap to split the trace unless I specify the -F nettl option. I prefer to use the pcapng format these days for its annotation features. Is there any reason why aic iptraces cannot be converted into pcapng?</p></div><div id="question-tags" class="tags-container tags">iptrace pcapng editcap aix tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '13, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-20062" class="comments-container"></div><div id="comment-tools-20062" class="comment-tools"></div><div class="clear"></div><div id="comment-20062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20365"></span>

<div id="answer-container-20365" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20365-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As folks have already mentioned, the Wireshark suite doesn't handle the conversion of AIX <strong>iptrace</strong> format to pcap.</p><p>Newer releases of AIX do, however, support the <strong>-T</strong> option to <strong>iptrace</strong>, which will save the data as a "tcpdump-compatible dump file." Since it says that <strong>tcpdump</strong> can read these files, I'm guessing that the Wireshark suite will find them much more manageable as well.</p><p>Several caveats apply, depending on the version(s) of AIX in use. See the <a href="http://pic.dhe.ibm.com/infocenter/aix/v7r1/index.jsp?topic=%2Fcom.ibm.aix.cmds%2Fdoc%2Faixcmds3%2Fiptrace.htm">AIX Information Center <strong>iptrace</strong> page</a> for details.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '13, 19:06</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span> </br></p></div></div><div id="comments-container-20365" class="comments-container"></div><div id="comment-tools-20365" class="comment-tools"></div><div class="clear"></div><div id="comment-20365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20065"></span>

<div id="answer-container-20065" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20065-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The short answer would be "As it has not been implemented yet".</p><p>I have no experience with nettl formatted capture files, but from the code it seems there are extra headers which might make saving them in another format a little more complicated. I would have to load an actual nettl file to be able to check how difficult it would be to add support for writing pcapng files from nettl files. Could you provide some? Preferably from different kind of interfaces (not just ethernet, but ethernet is a nice start for the most common case I guess)?</p><p>Could you add the files to <a href="http://wiki.wireshark.org/nettl">the wireshark wiki page on nettl</a>?</p><p>(or use www.cloudshark.org, although I'm not sure if they take non-pcap(ng) files)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '13, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20065" class="comments-container"><span id="20106"></span><div id="comment-20106" class="comment"><div id="post-20106-score" class="comment-score"></div><div class="comment-text"><p>So, after having problems with login to this site I'm now back to continue... I put up a small sample AIX iptrace: <a href="http://www.cloudshark.org/captures/3479694a0772">http://www.cloudshark.org/captures/3479694a0772</a> My pain is, that I can't split those AIX traces using editcap unless I specify the -F nttl option. After doing that, I cannot save them into any other format but HP-UX. The wireshark Gui allows me to save as pcapng, but with large files the GUI won't be able to read the trace completely.</p></div><div id="comment-20106-info" class="comment-info"><span class="comment-age">(05 Apr '13, 01:08)</span> mrEEde2</div></div></div><div id="comment-tools-20065" class="comment-tools"></div><div class="clear"></div><div id="comment-20065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

