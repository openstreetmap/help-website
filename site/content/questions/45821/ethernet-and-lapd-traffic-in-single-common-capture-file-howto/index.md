+++
type = "question"
title = "ethernet and LAPD traffic in single common capture file - howto?"
description = '''Hello, I have a TDM interface which can capture LAPD traffic, and I have an Application which can output the captured packets both in pcap or in pcap-ng format and both to file or to output pipe. I need to capture on both an Ethernet interface and the TDM interface at the same time, and get a single...'''
date = "2015-09-13T04:02:00Z"
lastmod = "2015-11-11T02:08:00Z"
weight = 45821
keywords = [ "pipe", "merge", "pcapng", "encapsulation" ]
aliases = [ "/questions/45821" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [ethernet and LAPD traffic in single common capture file - howto?](/questions/45821/ethernet-and-lapd-traffic-in-single-common-capture-file-howto)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45821-score" class="post-score" title="current number of votes">0</div><span id="post-45821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a TDM interface which can capture LAPD traffic, and I have an Application which can output the captured packets both in pcap or in pcap-ng format and both to file or to output pipe.</p><p>I need to capture on both an Ethernet interface and the TDM interface at the same time, and get a single common file containing captured packets from both interfaces.</p><p><strong>Issue #1: merge fails</strong><br />
If I create the "ethernet" pcapng using Wireshark and the "LAPD" pcapng using my application, and then try to merge them together, my Wireshark (1.12.7 on 64-bit Windows 7 at the moment) crashes. The mergecap from the same package doesn't crash but fails with a complaint:</p><p>D:"c:mergecap.exe" -w merge-attempt.pcapng export-ether.pcapng export-lapd.pcapng -v<br />
mergecap: export-ether.pcapng is type Wireshark/... - pcapng.<br />
mergecap: export-lapd.pcapng is type Wireshark/... - pcapng.<br />
mergecap: multiple frame encapsulation types detected<br />
defaulting to WTAP-ENCAP-PER-PACKET<br />
export-ether.pcapng had type Ethernet (ether)<br />
export-lapd.pcapng had type LAPD (lapd)<br />
mergecap: selected frame-type Per packet (per-packet)<br />
mergecap: Can't open or create merge-attempt.pcapng: Files from that network type can't be saved in that format</p><p>Merging two pcapng files with same frame encapsulation types by Wireshark works fine, regardless the particular encapsulation type. As for the LAPD, encapsulations "LAPD" (203) and "LAPD with linux pseudo-header" (177) give same results when merged with "ether" (1).</p><p><strong>Issue #2: capture from a pipe doesn't accept pcapng</strong><br />
When I let Wireshark capture simultaneously from the ethernet interface and from the Application's output pipe, I do get my desired common file, but as Wireshark refuses the pcapng, the Application must send pcap over the pipe. This forces me to use "LAPD with linux pseudo-header" encapsulation for the TDM channel, as "LAPD" encapsulation itself does not carry any information about packet direction. The "packet flags" which can be used for this and other purposes (indication of errors during capture) do not fit into pcap.</p><p><strong>Questions:</strong><br />
Anyone knows how to make mergecap (or Wireshark itself) do the job?<br />
Anyone knows how to make Wireshark capture pcapng from the pipe?<br />
Or any of these would require a development request?<br />
</p><p>Edit: the two minimalistic pcapng files illustrating the issue can be found here:<br />
<a href="https://drive.google.com/file/d/0B1ygoNuxMOQqbEluS1BhSTYyUEU/view?usp=sharing">SIP INVITE</a><br />
<a href="https://drive.google.com/file/d/0B1ygoNuxMOQqVzIya1R6UDBiUzg/view?usp=sharing">Q.931 SETUP</a></p><p>Thank you<br />
Pavel</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pipe" rel="tag" title="see questions tagged &#39;pipe&#39;">pipe</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span> <span class="post-tag tag-link-encapsulation" rel="tag" title="see questions tagged &#39;encapsulation&#39;">encapsulation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '15, 04:02</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Nov '15, 01:55</strong> </span></p></div></div><div id="comments-container-45821" class="comments-container"><span id="46111"></span><div id="comment-46111" class="comment"><div id="post-46111-score" class="comment-score"></div><div class="comment-text"><p>OK, I'll answer to myself.</p><p>As of now, at least for the stable version, and although some page at Wireshark wiki states otherwise, <strong>pcapng is not an acceptable input to the pipe</strong>, dot.</p><p>And, as of now, the mergecap from the install package is not a suitable tool for the task either.</p><p>So the solution is: as you are able to generate pcapng in your application, it should not be a big deal for you to code your own "mergepcapng" application which will read the Ethernet frames from pcapng saved by Wireshark and LAPD frames with packet flags saved by your capturing application, and write them both into a pcapng file which, luckily, Wireshark <strong>is</strong> able to read. Your advantage over the Wireshark team is that you need not bother about support of all the timestamp resolutions, interface/system name merge/substitution etc. in an ad-hoc code.</p></div><div id="comment-46111-info" class="comment-info"><span class="comment-age">(24 Sep '15, 09:16)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-45821" class="comment-tools"></div><div class="clear"></div><div id="comment-45821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47490"></span>

<div id="answer-container-47490" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47490-score" class="post-score" title="current number of votes">1</div><span id="post-47490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sindy has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Anyone knows how to make mergecap (or Wireshark itself) do the job?</p></blockquote><p>Although mergecap does not work (as you said) the following two methods do work for me with Wireshark 1.12.8 on Windows.</p><ul><li><p>Open one pcap file, then use <code>File -&gt; Merge</code></p></li><li><p>Open Wireshark and drag-drop <strong>both files</strong> at once into the Wireshark window</p></li></ul><p>The merged file can be saved as pcapng. I used a sample pcapng file with LAPD encapsulation from bugs.wireshark.org</p><p>If these methods don't work for you, please post two (small) sample files, so we can check.</p><p>Edit: in Wireshark 2.0.0, drag-and-dropping both files opens just one of them, and for some reason, the ethernet encapsulated one is preferred regardless the order of their selection. <code>File-&gt;Merge</code> works normally.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '15, 18:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Dec '15, 09:41</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></br></p></div></div><div id="comments-container-47490" class="comments-container"><span id="47503"></span><div id="comment-47503" class="comment"><div id="post-47503-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>I didn't know drag and drop of two files at once was possible, and it <strong>does</strong> work with my files in Wireshark 1.12.8/W7-64bit.</p><p>Opening of one file followed by File-&gt;Merge of the other one <strong>does not</strong> work with the same two files (my current Wireshark freezes like the 1.12.7 did).</p><p>As the drag and drop works, I'll accept your answer. As the "traditional method" works for you but does not work for me (same 1.12.8 but I don't know what is your OS), are you interested in the two files anyway?</p><p>Pavel</p></div><div id="comment-47503-info" class="comment-info"><span class="comment-age">(10 Nov '15, 22:23)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="47507"></span><div id="comment-47507" class="comment"><div id="post-47507-score" class="comment-score"></div><div class="comment-text"><p>I've added links to the simplest possible files to my question (one frame per file). I hesitate to file a bug as the importance for the community is low now as you've found the right way to fulfil the task.</p></div><div id="comment-47507-info" class="comment-info"><span class="comment-age">(11 Nov '15, 02:08)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-47490" class="comment-tools"></div><div class="clear"></div><div id="comment-47490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

