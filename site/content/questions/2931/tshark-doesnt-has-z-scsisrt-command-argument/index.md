+++
type = "question"
title = "tshark doesn&#x27;t has -z scsi,srt command argument"
description = '''Wireshark has this option to filter the scsi response time where as tshark doesn&#x27;t has this commandline argument option at all. Is there anything I&#x27;m missing -z scsi,srt,cmdset[,&amp;lt;filter&amp;gt;] Wireshark has this feature where as tshark doesn&#x27;t has this commandline option at all.'''
date = "2011-03-19T12:27:00Z"
lastmod = "2011-03-19T13:12:00Z"
weight = 2931
keywords = [ "scsi", "tshark", "srt" ]
aliases = [ "/questions/2931" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark doesn't has -z scsi,srt command argument](/questions/2931/tshark-doesnt-has-z-scsisrt-command-argument)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2931-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark has this option to filter the scsi response time where as tshark doesn't has this commandline argument option at all. Is there anything I'm missing</p><p>-z scsi,srt,cmdset[,&lt;filter&gt;]</p><p>Wireshark has this feature where as tshark doesn't has this commandline option at all.</p></div><div id="question-tags" class="tags-container tags">scsi tshark srt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '11, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/009622f35eab24cfbde3547b04a5bbea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="asif&#39;s gravatar image" /><p>asif<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="asif has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Mar '11, 15:20</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-2931" class="comments-container"><span id="3118"></span><div id="comment-3118" class="comment"><div id="post-3118-score" class="comment-score"></div><div class="comment-text"><p>FYI: For consistency between tshark and Wireshark, starting with 1.5.1 (whenever it is released), the syntax of the "-z &lt;proto&gt;,rtt" option will be changed to match Wireshark's syntax of "-z &lt;proto&gt;,srt". This is also true of the automated releases as of revision 36297. Automated releases are available from: http://www.wireshark.org/download/automated/.</p></div><div id="comment-3118-info" class="comment-info"><span class="comment-age">(25 Mar '11, 06:58)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-2931" class="comment-tools"></div><div class="clear"></div><div id="comment-2931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2932"></span>

<div id="answer-container-2932" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2932-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Which version are you using?<br />
$ tshark -v<br />
TShark 1.5.0 (SVN Rev 35637 from /trunk)<br />
</p><p>Download the <a href="http://www.wireshark.org/download.html">Development release</a> (1.5.0) or an <a href="http://www.wireshark.org/download/automated/">automated build</a>.<br />
</p><p>According to the <a href="http://www.wireshark.org/docs/man-pages/wireshark.html">man-page</a> you should use "-z scsi,srt,cmdset[,filter]", but I get an error:</p><pre><code>$ tshark -r test.pcap -q -z scsi,srt,0
tshark: invalid -z argument.
  -z argument must be one of :
     sametime,tree
     scsi,rtt,
     sctp,stat
     sip,stat</code></pre><p>Try this:<br />
<a href="http://wiki.wireshark.org/FrontPage">Wireshark Wiki</a>: <a href="http://wiki.wireshark.org/SampleCaptures#SAN_Protocol_Captures_.28iSCSI.2C_ATAoverEthernet.2C_FibreChannel.2C_SCSI-OSD_and_other_SAN_related_protocols.29">Sample Captures</a> - fcoe-drop-rddata.cap</p><pre><code>$ tshark -r fcoe-drop-rddata.cap -q -z scsi,rtt,0
===========================================================
SCSI SBC (disk) RTT Statistics:
Filter:
Procedure            Calls   Min RTT    Max RTT    Avg RTT
Read(6)                  2   0.039798   0.087864   0.063831
===========================================================</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '11, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Mar '11, 15:53</p></div></div><div id="comments-container-2932" class="comments-container"><span id="2933"></span><div id="comment-2933" class="comment"><div id="post-2933-score" class="comment-score"></div><div class="comment-text"><p>I've downloaded the latest stable build which is 1.4.4. Let me try the build you have pointed out. Thanks for the quick response.</p></div><div id="comment-2933-info" class="comment-info"><span class="comment-age">(19 Mar '11, 13:44)</span> asif</div></div><span id="2934"></span><div id="comment-2934" class="comment"><div id="post-2934-score" class="comment-score"></div><div class="comment-text"><p>(converted your "answer" to a "comment" to follow the Q&amp;A style of this site, please see the FAQ for more information)</p></div><div id="comment-2934-info" class="comment-info"><span class="comment-age">(19 Mar '11, 15:21)</span> SYN-bit ♦♦</div></div><span id="2948"></span><div id="comment-2948" class="comment"><div id="post-2948-score" class="comment-score"></div><div class="comment-text"><p>Installed the 1.5.0 build and I see scsi,rtt commandline arguments. There is a difference in the output compared to UI. Is this a known issue?</p><p>Via CLI started the capture trace: - tshark -S -i 2 -w capture_out.pcap - tshark -r capture_out.pcap -q -z scsi,rtt,0</p><p>returns avg SRT value: 0.021678.</p><p>Via UI capture, I get the avg SRT value: 0.081465.</p><p>Which avg SRT is correct? Yes, I've made sure I start the capture trace first before i send data.</p><p>Any help is appreciated.</p></div><div id="comment-2948-info" class="comment-info"><span class="comment-age">(20 Mar '11, 11:13)</span> asif</div></div><span id="3122"></span><div id="comment-3122" class="comment"><div id="post-3122-score" class="comment-score"></div><div class="comment-text"><p>FYI: This last question about the difference in tshark vs. Wireshark output was re-asked and answered here: http://ask.wireshark.org/questions/2961/difference-in-the-output-tshark-vs-wireshark-results</p></div><div id="comment-3122-info" class="comment-info"><span class="comment-age">(25 Mar '11, 07:22)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-2932" class="comment-tools"></div><div class="clear"></div><div id="comment-2932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

