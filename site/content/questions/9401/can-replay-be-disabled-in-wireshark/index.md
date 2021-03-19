+++
type = "question"
title = "Can Replay be disabled in Wireshark?"
description = '''Can Replay be disabled in Wireshark? I need a version of Wireshark or I need to modify Wireshark so that packets can not be replayed. Is this possible? If so, how?'''
date = "2012-03-06T10:41:00Z"
lastmod = "2012-03-06T12:11:00Z"
weight = 9401
keywords = [ "replay" ]
aliases = [ "/questions/9401" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Can Replay be disabled in Wireshark?](/questions/9401/can-replay-be-disabled-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9401-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can Replay be disabled in Wireshark? I need a version of Wireshark or I need to modify Wireshark so that packets can not be replayed. Is this possible? If so, how?</p></div><div id="question-tags" class="tags-container tags">replay</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '12, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/44850965fe13ffa8bb157c49ab60e61b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Balthazar2007&#39;s gravatar image" /><p>Balthazar2007<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Balthazar2007 has no accepted answers">0%</span></p></div></div><div id="comments-container-9401" class="comments-container"></div><div id="comment-tools-9401" class="comment-tools"></div><div class="clear"></div><div id="comment-9401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="9403"></span>

<div id="answer-container-9403" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9403-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you mean you want Wireshark to make a capture file non-replayable by a third party, I don't think there's a feature for that. If your pcap contains src and dst IPs, it can be replayed, so you simply need to anonymize your pcap to prevent replay to the actual endpoints (the anonymization rewrites the IPs). You can do that with a variety of packet-rewrite tools, including <a href="http://bittwist.sourceforge.net/"><code>bittwiste</code></a> or <a href="http://tcpreplay.synfin.net/wiki/tcprewrite"><code>tcprewrite</code></a>. For <code>tcprewrite</code>, see <a href="http://tcpreplay.synfin.net/wiki/tcprewrite#RandomizingIPAddresses"><strong>Randomizing IP addresses</strong></a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '12, 10:55</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p>bstn<br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-9403" class="comments-container"></div><div id="comment-tools-9403" class="comment-tools"></div><div class="clear"></div><div id="comment-9403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9406"></span>

<div id="answer-container-9406" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9406-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can think of two mechanisms to prevent replaying VoIP/VTC, filtering and slicing.</p><ul><li><em>Filtering.</em> You can create a capture filter that will not capture VoIP/VTC traffic, but will capture all the rest for your intrusion analysis. However, it might be difficult to achieve this when random ports are used.</li><li><em>Slicing.</em> You can slice off the RTP data by setting a snap length. You might want to try 96 which will keep the Ethernet, IP, TCP and UDP layer and a few bytes of payload, so reconstructing a VoIP or VTC call will not be possible anymore. However, you might also lose the information that you are after.</li></ul><p>The best way to deal with this is to capture all traffic and make sure that only certain people are able to access the capture files. There will need to be trust in those people that the files will not be used for replaying. You can then discuss some procedures on how to access, filter and delete the data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '12, 12:11</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9406" class="comments-container"><span id="9408"></span><div id="comment-9408" class="comment"><div id="post-9408-score" class="comment-score"></div><div class="comment-text"><p>Basically: If someone can capture (and save) all the bits, then (obviously) there's enough to be able to decipher a conversation (assuming no encryption).</p><p><a href="http://www.schneier.com/blog/archives/2006/04/voip_encryption.html">Blog entry on VOIP encryption</a></p></div><div id="comment-9408-info" class="comment-info"><span class="comment-age">(06 Mar '12, 12:43)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-9406" class="comment-tools"></div><div class="clear"></div><div id="comment-9406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9402"></span>

<div id="answer-container-9402" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9402-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark doesn't have a "replay" (send packets from a capture file to the network) capability.</p><p>Please explain in a bit more detail what you are trying to disable.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '12, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-9402" class="comments-container"><span id="9404"></span><div id="comment-9404" class="comment"><div id="post-9404-score" class="comment-score"></div><div class="comment-text"><p>My system is used for corporate communications and the bosses are afraid that someone could use Wireshark to reconstruct VoIP calls or TeleConferences and actually replay the conversations. I need the wireshark to help in investigating intrusion attempts/events. Is there a middle ground where I can still view packets but not be able to reconstruct an actual phone call or VTC?</p></div><div id="comment-9404-info" class="comment-info"><span class="comment-age">(06 Mar '12, 11:32)</span> Balthazar2007</div></div></div><div id="comment-tools-9402" class="comment-tools"></div><div class="clear"></div><div id="comment-9402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

