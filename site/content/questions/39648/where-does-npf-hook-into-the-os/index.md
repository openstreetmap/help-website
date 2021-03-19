+++
type = "question"
title = "Where does npf hook into the OS ?"
description = '''I am troubleshooting a problem with lost syslog messages. The messages are sent via UDP. I run the current version of Wireshark 1.12.3 on W2K3 and can see 100% of the incoming messages. But the syslog receiver (in this case syslog4j) does only write about 80% of the messages to disk. Sidenote: there...'''
date = "2015-02-04T13:36:00Z"
lastmod = "2015-02-04T23:06:00Z"
weight = 39648
keywords = [ "npf.sys", "npf", "dropped" ]
aliases = [ "/questions/39648" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Where does npf hook into the OS ?](/questions/39648/where-does-npf-hook-into-the-os)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39648-score" class="post-score" title="current number of votes">0</div><span id="post-39648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am troubleshooting a problem with lost syslog messages. The messages are sent via UDP. I run the current version of Wireshark 1.12.3 on W2K3 and can see 100% of the incoming messages. But the syslog receiver (in this case syslog4j) does only write about 80% of the messages to disk. Sidenote: there is not much traffic on the wire only around 100 messages in 5 minutes.</p><p>Is the fact that I can see all messages in Wireshark a clue that all is sent to syslog4j and that one dropping packets ? Or might there be a firewall messing with the data ? How can I find out if the order is "npf -&gt; firewall -&gt; syslog4j" or "firewall -&gt; npf -&gt; syslog4j" ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-npf.sys" rel="tag" title="see questions tagged &#39;npf.sys&#39;">npf.sys</span> <span class="post-tag tag-link-npf" rel="tag" title="see questions tagged &#39;npf&#39;">npf</span> <span class="post-tag tag-link-dropped" rel="tag" title="see questions tagged &#39;dropped&#39;">dropped</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '15, 13:36</strong></p><img src="https://secure.gravatar.com/avatar/24aaaba3c6140eaef24f9ed711644033?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marged&#39;s gravatar image" /><p><span>marged</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marged has no accepted answers">0%</span></p></div></div><div id="comments-container-39648" class="comments-container"></div><div id="comment-tools-39648" class="comment-tools"></div><div class="clear"></div><div id="comment-39648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39651"></span>

<div id="answer-container-39651" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39651-score" class="post-score" title="current number of votes">1</div><span id="post-39651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://www.winpcap.org/docs/iscc01-wpcap.pdf">It plugs into NDIS</a>. There is no reason why syslog4j, or any <em>other</em> implementation of the syslog protocol, would need to use NPF or any other packet capture mechanism - it merely needs to have a UDP or TCP socket sending to (client) or receiving from (server) the appropriate port - so I would never expect to see either "npf -&gt; firewall -&gt; syslog4j" or "firewall -&gt; npf -&gt; syslog4j" or anything <em>else</em> containing both "npf" and "syslog4j".</p><p>Both NPF and a UDP socket will drop packets if they arrive faster than the consumer can process them.</p><p>If the steady-state arrival rate of packets is greater than the rate at which dumpcap (in the case of Wireshark) or syslog4j can write them to disk, the only thing you can do is probably to change the hardware or software so that packets can be written faster to disk.</p><p>At a rate of 1 message every 3 seconds, that's <em>probably</em> not what's happening. However, if that's just the steady-state rate, and the traffic is bursty, so that you get a burst with a <em>lot</em> of packets arriving in a short period of time and then no packets at all, <em>averaging</em> to 1 message every 3 seconds, if the program processing the messages can't write out the burst of packets fast enough, the buffer for NPF (in the case of dumpcap) or the UDP socket (in the case of syslog4j) could be overrun. Wireshark, and thus dumpcap, chooses a 2MB buffer by default; the UDP socket, however, probably has a smaller by default, although syslog4j might make the buffer bigger.</p><p>This all assumes that syslog4j isn't discarding the messages <em>itself</em> for some reason.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '15, 16:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-39651" class="comments-container"><span id="39654"></span><div id="comment-39654" class="comment"><div id="post-39654-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the detailed answer and the link provided. I had a look at the PDF, especially chapter 4.2 but I still have one question.</p><p>I did not mean to say that syslog4j needs the npf. I suppose that both npf and the firewall are hooking into NDIS. I used Wireshark/npf to check if the data is "on the wire". But what if npf comes before the firewall ? And the firewall before syslog4j ? Then I would see the packets but the firewall could remove/drop them afterwards and they would never reach syslog4j I don't know if hooking into NDIS means chaining or if all hooks get the data in parallel</p><p>And a sidenote: yes, the messages come in in bulk, the sender sends them every five minutes. But the message should perfectly fit into the 2MB buffer</p></div><div id="comment-39654-info" class="comment-info"><span class="comment-age">(04 Feb '15, 22:02)</span> <span class="comment-user userinfo">marged</span></div></div><span id="39655"></span><div id="comment-39655" class="comment"><div id="post-39655-score" class="comment-score"></div><div class="comment-text"><p>NPF does not come before the firewall, so that's not an issue.</p><p>NDIS can have multiple other protocols plugged into it, and, for each of the protocols, if a packet arrives, then, if the filter (not to be confused with, for example, a libpcap/WinPcap capture filter) the protocol specified accepts the packet, delivers a copy of the packet to that protocol. There's no chaining. I couldn't find a good discussion of this on the MSDN Web site, but <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff545179(v=vs.85).aspx">here's a picture that sort of shows it</a>.</p><p>And the 2MB buffer is for NPF, i.e. for dumpcap and thus Wireshark, as well as tcpdump etc.. I don't know what the default socket buffer size for a UDP socket is on Windows Server 2K3, but I wouldn't be surprised if it were less than 2MB.</p></div><div id="comment-39655-info" class="comment-info"><span class="comment-age">(04 Feb '15, 23:06)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-39651" class="comment-tools"></div><div class="clear"></div><div id="comment-39651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

