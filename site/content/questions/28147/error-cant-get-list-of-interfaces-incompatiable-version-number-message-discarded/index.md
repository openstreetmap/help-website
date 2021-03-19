+++
type = "question"
title = "Error: Can&#x27;t get list of interfaces: Incompatiable version number: message discarded"
description = '''Hi, I have installed Wireshark 1.10.3 and winpcap 4.1.3 in my local windows machine. Tried to add remote interfaces for the specific host name by specifying host name for host , port number for port, and username. password for password authentication. i am getting the error &quot;can&#x27;t get list of interf...'''
date = "2013-12-16T04:29:00Z"
lastmod = "2013-12-16T06:27:00Z"
weight = 28147
keywords = [ "usage", "tool", "wireshark" ]
aliases = [ "/questions/28147" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error: Can't get list of interfaces: Incompatiable version number: message discarded](/questions/28147/error-cant-get-list-of-interfaces-incompatiable-version-number-message-discarded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28147-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have installed Wireshark 1.10.3 and winpcap 4.1.3 in my local windows machine. Tried to add remote interfaces for the specific host name by specifying host name for host , port number for port, and username. password for password authentication. i am getting the error "can't get list of interfaces:incompatiable version number: message discarded.<br />
</p><p>I verified that remote host name is accesible from my local windows machine. I tried this by using ping command.</p><p>I'm not sure that what the reason for this. Help us to figure out reason for this error and share procedure for how to connect to remote hostname via wireshark.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">usage tool wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '13, 04:29</strong></p><img src="https://secure.gravatar.com/avatar/57906d92ff804f06bf0894e8a4b425ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manivas&#39;s gravatar image" /><p>Manivas<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manivas has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-28147" class="comments-container"></div><div id="comment-tools-28147" class="comment-tools"></div><div class="clear"></div><div id="comment-28147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28155"></span>

<div id="answer-container-28155" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28155-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like you did not install WinPcap on the remote host <strong>and/or</strong> did not start rpcapd (Remote Capturing Daemon) on that machine.</p><blockquote><p><a href="http://www.winpcap.org/docs/docs_40_2/html/group__remote.html">http://www.winpcap.org/docs/docs_40_2/html/group__remote.html</a><br />
</p></blockquote><p>Please search the site for 'rpcapd' to get similar questions and answers.</p><p>If you've installed and started rpcapd on the remote machine, please post the output of the following command (run it as Administrator in an elevated DOS box).</p><blockquote><p>netstat -nab</p></blockquote><p>In that output search for 'rpcapd' <strong>or</strong> '2002' and post the two lines before and after the line that contains those strings.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '13, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Dec '13, 03:02</p></div></div><div id="comments-container-28155" class="comments-container"><span id="28191"></span><div id="comment-28191" class="comment"><div id="post-28191-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Thanks for your support.</p><p>Executed command "netstat -nap", it's not giving any output values for Proto, Local Address, Foreign address and state.</p><p>I tried the command "rpcapd -a " command from winpcap installed location"C:\Program Files (x86)\WinPcap" to start, but its giving output as "rpcapd: option requires an argument --a , Press CTRL+C to stop the server". What it could means, whether server started or it required some other parameters.</p><p>Thanks in advance.</p></div><div id="comment-28191-info" class="comment-info"><span class="comment-age">(16 Dec '13, 23:06)</span> Manivas</div></div><span id="28210"></span><div id="comment-28210" class="comment"><div id="post-28210-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Executed command "netstat -nap", it's not giving any output values for Proto, Local Address, Foreign address and state.</p></blockquote><p>sorry, on Windows it's</p><blockquote><p>netstat -nab</p></blockquote><p>'b' instead of 'p'</p><blockquote><p>rpcapd: option requires an argument --a</p></blockquote><p>Please <strong>read</strong> the rpcapd documentation!</p><blockquote><p><a href="http://www.winpcap.org/docs/docs_40_2/html/group__remote.html">http://www.winpcap.org/docs/docs_40_2/html/group__remote.html</a></p></blockquote></div><div id="comment-28210-info" class="comment-info"><span class="comment-age">(17 Dec '13, 03:02)</span> Kurt Knochner ♦</div></div><span id="28292"></span><div id="comment-28292" class="comment"><div id="post-28292-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thanks for your support.</p><p>Can you please suggest the link for downloading wireshark install via RPM on Redhat Systems.</p><p>Wireshark software download for Redhat system.</p></div><div id="comment-28292-info" class="comment-info"><span class="comment-age">(19 Dec '13, 06:22)</span> Manivas</div></div><span id="28300"></span><div id="comment-28300" class="comment"><div id="post-28300-score" class="comment-score"></div><div class="comment-text"><p>There is only the repository of Red Hat, but they offer only an ancient version of Wireshark. So, if you want a recent version, you must compile it yourself.</p><p>BTW: If you want to run rpcapd on Red Hat, that won't be included in any Wireshark package. You can however compile it yourself from the sources of WinPcap.</p></div><div id="comment-28300-info" class="comment-info"><span class="comment-age">(19 Dec '13, 15:14)</span> Kurt Knochner ♦</div></div><span id="28303"></span><div id="comment-28303" class="comment not_top_scorer"><div id="post-28303-score" class="comment-score"></div><div class="comment-text"><p>Thanks,</p><p>Can you please share link to download Wireshare for Redhat systems to install in linux machines.</p></div><div id="comment-28303-info" class="comment-info"><span class="comment-age">(20 Dec '13, 00:45)</span> Manivas</div></div><span id="28309"></span><div id="comment-28309" class="comment not_top_scorer"><div id="post-28309-score" class="comment-score"></div><div class="comment-text"><p>As I said, it's in the repository of Red Hat.</p><blockquote><p>sudo yum install wireshark<br />
sudo yum install wireshark-gnome</p></blockquote></div><div id="comment-28309-info" class="comment-info"><span class="comment-age">(20 Dec '13, 10:41)</span> Kurt Knochner ♦</div></div><span id="28314"></span><div id="comment-28314" class="comment not_top_scorer"><div id="post-28314-score" class="comment-score"></div><div class="comment-text"><p>BTW: why are we talking about Red Hat? You started the question with WinPcap!?!</p></div><div id="comment-28314-info" class="comment-info"><span class="comment-age">(21 Dec '13, 10:30)</span> Kurt Knochner ♦</div></div><span id="28352"></span><div id="comment-28352" class="comment not_top_scorer"><div id="post-28352-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Could you please explain the difference between working nature of below two command.</p><p>tcpdump -w xpackets2.pcap -i eth0 src host-name</p><p>tcpdump -w xpackets2.pcap -i eth0 dst host-name</p><p>Thanks in advance.</p></div><div id="comment-28352-info" class="comment-info"><span class="comment-age">(23 Dec '13, 23:33)</span> Manivas</div></div><span id="28353"></span><div id="comment-28353" class="comment not_top_scorer"><div id="post-28353-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>could you please open a new question and close this one by accepting it, if the answer was helpful to you. This i a Q&amp;A site. Asking new questions in an existing one is undesirable.</p></div><div id="comment-28353-info" class="comment-info"><span class="comment-age">(23 Dec '13, 23:53)</span> Kurt Knochner ♦</div></div><span id="28357"></span><div id="comment-28357" class="comment not_top_scorer"><div id="post-28357-score" class="comment-score"></div><div class="comment-text"><p>Thanks,its helped me a lot.</p></div><div id="comment-28357-info" class="comment-info"><span class="comment-age">(24 Dec '13, 01:50)</span> Manivas</div></div><span id="28358"></span><div id="comment-28358" class="comment"><div id="post-28358-score" class="comment-score">1</div><div class="comment-text"><p>Good.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-28358-info" class="comment-info"><span class="comment-age">(24 Dec '13, 01:54)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28155" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-28155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

