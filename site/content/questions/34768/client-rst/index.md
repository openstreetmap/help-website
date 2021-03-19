+++
type = "question"
title = "client RST"
description = '''Hello, I have an application with a custom protocol running on a customer&#x27;s wireless network that connects via TCP to AWS. The client randomly disconnects with an RST. The customer tells me their wireless network is sketchy. Can any more information be gathered from the Wireshark trace? Before the d...'''
date = "2014-07-18T12:14:00Z"
lastmod = "2014-07-21T14:06:00Z"
weight = 34768
keywords = [ "rst" ]
aliases = [ "/questions/34768" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [client RST](/questions/34768/client-rst)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34768-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have an application with a custom protocol running on a customer's wireless network that connects via TCP to AWS. The client randomly disconnects with an RST. The customer tells me their wireless network is sketchy. Can any more information be gathered from the Wireshark trace? Before the disconnect I see a series of ACKs from the client for the last server communication, followed by a 70 second delay, then an RST from the client. In the cases I have traced, there is always about a 70 second delay between the last client ACK and the RST. Any thoughts on what is going on here? The Wireshark trace is below. Thanks in advance for your help! Regards, Cameron</p><p><a href="https://www.cloudshark.org/captures/faea872b7905">https://www.cloudshark.org/captures/faea872b7905</a></p></div><div id="question-tags" class="tags-container tags">rst</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '14, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/e8f820e9c6301dee30fcbc0bbce5cb28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dcdeheer&#39;s gravatar image" /><p>dcdeheer<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dcdeheer has no accepted answers">0%</span></p></div></div><div id="comments-container-34768" class="comments-container"><span id="34769"></span><div id="comment-34769" class="comment"><div id="post-34769-score" class="comment-score">1</div><div class="comment-text"><p>Your analysis looks right to me. That "series of ACKs" from the client is in response to a 65236-byte segment immediately followed by a 29809 segment from the server. That looks unusually large to me, but that might be normal in other people's networks.</p><p>In any case if you look at the sequence numbers, you'll see that the client finished successfully acknowledging all of the data sent by the server in packet #511. It looks to me like both the client and the server are satisified with what they received, and the 70 seconds is simply a idle timeout trigger on the client.</p><p>Was there an application-layer problem captured in this trace? I don't see anything wrong, outside some minor packet loss.</p></div><div id="comment-34769-info" class="comment-info"><span class="comment-age">(18 Jul '14, 13:04)</span> smp</div></div><span id="34770"></span><div id="comment-34770" class="comment"><div id="post-34770-score" class="comment-score"></div><div class="comment-text"><p>Hello, That is what I thought, thanks very much for your feedback. Nothing out of the ordinary is going on at the application level, and there is no application-level timeout for inactivity. I had them install another client on their primary network (no wireless) and we're seeing the same disconnect, after about 67 seconds. I am leaning toward a switch on their site with a 60 second inactivity timeout, or something along these lines. Thanks again for your help. Regards, Cameron</p></div><div id="comment-34770-info" class="comment-info"><span class="comment-age">(18 Jul '14, 13:16)</span> dcdeheer</div></div><span id="34771"></span><div id="comment-34771" class="comment"><div id="post-34771-score" class="comment-score">1</div><div class="comment-text"><p>TCP idle timeouts can vary widely, and so can the mechanisms to control them. You may not see timeout properties from an application perspective, but they're more likely somewhere in the TCP/IP properties on the client. These properties are not always easy to find - if they are even accessible. Some closed systems don't even provide a mechanism to adjust them.</p><p>I doubt it's a switch since that's a L2 device. But you're right, it could be a firewall, or any number of proxy-type devices sitting in the middle of the conversation. If there's no proxy intermediary, I'd suspect the idle timer is in the client TCP/IP stack somewhere.</p></div><div id="comment-34771-info" class="comment-info"><span class="comment-age">(18 Jul '14, 13:34)</span> smp</div></div><span id="34804"></span><div id="comment-34804" class="comment"><div id="post-34804-score" class="comment-score"></div><div class="comment-text"><p>Hello smp, Thanks so much for your help. Both client and server are Windows, I could not find any documentation on the Windows TCP/IP stack that indicated a configuration for idle timeout. The client is our software, and it does not have any idle timeout in its protocol. It sends a heartbeat message every 5 minutes to the server to keep the connection alive, the server stops listening if the heartbeat doesn't show up for a while (30 minutes). The disconnect we are seeing happens at one minute. I had the customer get me a wireshark capture of the client at the same time i was capturing the server:</p><p>client: <a href="https://www.cloudshark.org/captures/b5fce301d9e1">https://www.cloudshark.org/captures/b5fce301d9e1</a> server: <a href="https://www.cloudshark.org/captures/bbfa28dd02ee">https://www.cloudshark.org/captures/bbfa28dd02ee</a></p><p>Both sides are receiving the RST. The only thing I noticed out of the ordinary on the client was a lot of 'reassembly error' messages. Could these have something to do with the RST? Thanks again for your help! Regards, Cameron</p></div><div id="comment-34804-info" class="comment-info"><span class="comment-age">(21 Jul '14, 12:15)</span> dcdeheer</div></div></div><div id="comment-tools-34768" class="comment-tools"></div><div class="clear"></div><div id="comment-34768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34806"></span>

<div id="answer-container-34806" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34806-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is a "WatchGuard" proxy next to the client. Looking at the SYN packets they clearly show they have been modified from a windows fingerprint to a linux-ish one (TTL=64). Also, the ip.id of the packets are different. So it is probably an idle-timer that pops after having not seen any traffic within 60 seconds kicking the session out by sending a RST to each end.<br />
<img src="https://osqa-ask.wireshark.org/upfiles/Selection_236.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '14, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div></div><div id="comments-container-34806" class="comments-container"></div><div id="comment-tools-34806" class="comment-tools"></div><div class="clear"></div><div id="comment-34806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

