+++
type = "question"
title = "Seeing PKTAP metadata in Wireshark GUI"
description = '''I&#x27;ve just discovered pktap, an Apple pseudo interface which adds info about the process id particularly. sudo tcpdump -q -n -i pktap,en0 -k 21:02:59.849248 (en0, proc Google Chrome:244, svc BE, out) IP 192.168.178.54.53338 &amp;gt; 199.16.156.230.443: tcp 0  As I&#x27;ve seen this page regarding pktap displa...'''
date = "2016-07-04T12:12:00Z"
lastmod = "2016-07-06T03:01:00Z"
weight = 53818
keywords = [ "osx", "macosx", "pktap" ]
aliases = [ "/questions/53818" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Seeing PKTAP metadata in Wireshark GUI](/questions/53818/seeing-pktap-metadata-in-wireshark-gui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53818-score" class="post-score" title="current number of votes">0</div><span id="post-53818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've just discovered pktap, an Apple pseudo interface which adds info about the process id particularly.</p><pre><code>sudo tcpdump -q -n -i pktap,en0 -k
21:02:59.849248 (en0, proc Google Chrome:244, svc BE, out) IP 192.168.178.54.53338 &gt; 199.16.156.230.443: tcp 0</code></pre><p>As I've seen this page regarding pktap display filter, <a href="https://www.wireshark.org/docs/dfref/p/pktap.html">https://www.wireshark.org/docs/dfref/p/pktap.html</a>, my guess was that Wireshark was able to decode that as well, not only the cli of macOS.</p><p>I've tried to save the file, but I didn't succeed to reopen the pcapng with the medata informations.</p><pre><code>sudo tcpdump -q -n -i pktap,en0 -k -w mytrace.pcapng</code></pre><p>I've discovered that launching tcpdump -i pktap creates a pseudo pktap0 interface during the capture, and running a second tcpdump on that pktap0 interface doesn't save any medatadata neither...</p><p>How can I save a pcapng on macOS and be able to reopen it later, showing that processus metadata in Wireshark GUI and using PKTAP display filters?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span> <span class="post-tag tag-link-pktap" rel="tag" title="see questions tagged &#39;pktap&#39;">pktap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '16, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p><span>TomLaBaude</span><br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div></div><div id="comments-container-53818" class="comments-container"></div><div id="comment-tools-53818" class="comment-tools"></div><div class="clear"></div><div id="comment-53818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53819"></span>

<div id="answer-container-53819" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53819-score" class="post-score" title="current number of votes">0</div><span id="post-53819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>tcpdump, when capturing from a pktap interface, doesn't write out the raw PKTAP header; what Wireshark can dissect is the raw pktap header. Instead, it writes out the pktap metadata using various pcap-ng features - including the "local use" block types, which they use for a block they call a Process Information Block (PIB), with a block code of 0x80000001, containing information about a process, and the "local use" option types, which they use for an Enhanced Packet Block option they call the "PIB index", with an option code of PCAPNG_EPB_E_PIB_IN, containing the index of the previously-seen Process Information Block corresponding to the process to or from which the packet was sent.</p><p>Sadly, that means that their pcapng files might be misread by programs in which a block code of 0x80000001 is interpreted as another type of block or in which an EPB option code of 0x8003 is interpreted as another type of option.</p><p>Wireshark won't have a problem with that block or that option - it'll just <em>ignore</em> them.</p><p>Wireshark would have to be changed to have a preference to let it interpret them as the Apple-specific local blocks and options.</p><p>The pcapng specification has been updated to include support for "custom" blocks and options, the tags for which include a "Private Enterprise Number" (PEN) for an organization, so that Apple could have a block type and option types with a PEN of 63, which would always be interpreted as their block and options.</p><p>Or they could get together with the HONE people and others and come up with something to put into the pcapng standard to use to mark packets as going to or from a particular process.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '16, 16:56</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-53819" class="comments-container"><span id="53852"></span><div id="comment-53852" class="comment"><div id="post-53852-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy, thanks for your detailed answer. Thanks to your answer, I've successfully seen the process id and process string in an hexa editor before some packets of my pcapng file. ("Google Chrome", "firefox", ...)</p><p>Considering Wireshark/tshark development, perhaps an alternative, while Apple metadata are not standard yet, would be to show/access the various blocks of the pcapng (which are standards) After it would be up to the user to deal/interpret with the content of each block. I'll fill a bug about it.</p></div><div id="comment-53852-info" class="comment-info"><span class="comment-age">(06 Jul '16, 03:01)</span> <span class="comment-user userinfo">TomLaBaude</span></div></div></div><div id="comment-tools-53819" class="comment-tools"></div><div class="clear"></div><div id="comment-53819-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

