+++
type = "question"
title = "Writing a dissector for a non ethernet protocol - Which type of &quot;dissector_add&quot; should I use?"
description = '''Hi all, we have a complex protocol, which is not ethernet based (it has nothing to do with ethernet) and which consists of frames with timestamps. In order to analyze and display the individual protocol parts, I would like to use Wireshark. What I have done so far:  I have written a converter, so th...'''
date = "2012-08-01T00:41:00Z"
lastmod = "2012-08-01T02:26:00Z"
weight = 13211
keywords = [ "dissector_add_uint", "dissector_add" ]
aliases = [ "/questions/13211" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Writing a dissector for a non ethernet protocol - Which type of "dissector\_add" should I use?](/questions/13211/writing-a-dissector-for-a-non-ethernet-protocol-which-type-of-dissector_add-should-i-use)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13211-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>we have a complex protocol, which is not ethernet based (it has nothing to do with ethernet) and which consists of frames with timestamps.</p><p>In order to analyze and display the individual protocol parts, I would like to use Wireshark. What I have done so far:</p><ol><li>I have written a converter, so that our frames are now inside a pcapng file.</li><li>I have setup the source for my own (plugin) dissector.</li></ol><p>I am new in writing dissectors and I have no (deep) knowledge of frame formats. I have understood, that when I call for example</p><p>dissector_add_uint("tcp.port", 999, my_handle);</p><p>my dissect function will get called, when I have an IP frame with port 999.</p><p>When I open my pcapng files with wireshark and lets say my frame is</p><p>04 04 04 04 01 02 03</p><p>then wireshark displays them as</p><p>Frame (7 bytes on wire)</p><p>Null/Loopback</p><p>Type unknown (0x0404)</p><p>Data (3 Byte) 01 02 03</p><p>My non ethernet frames start with complete random hex bytes, but I could prefix a certain flag (e.g. 0x11, 0x22, 0x33, 0x44 or whatever) to all my frames, before I put them into a pcapng file.</p><p>Can you give me a tip, which kind of dissector_add_(uint) with which parameters I should call, so that my dissect function gets called?</p><p>Thanks a lot.</p><p>Carsten from Germany</p></div><div id="question-tags" class="tags-container tags">dissector_add_uint dissector_add</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '12, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/68c0004a25e9e1742fba20d34a50a24b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gyroblau&#39;s gravatar image" /><p>gyroblau<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gyroblau has no accepted answers">0%</span></p></div></div><div id="comments-container-13211" class="comments-container"></div><div id="comment-tools-13211" class="comment-tools"></div><div class="clear"></div><div id="comment-13211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13218"></span>

<div id="answer-container-13218" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13218-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should probably request a link layer type here <a href="http://www.tcpdump.org/linktypes.html">http://www.tcpdump.org/linktypes.html</a> or use one of th user DLT:s for your frames.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '12, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-13218" class="comments-container"><span id="13231"></span><div id="comment-13231" class="comment"><div id="post-13231-score" class="comment-score"></div><div class="comment-text"><p>... or maybe your link-layer type is already there.</p></div><div id="comment-13231-info" class="comment-info"><span class="comment-age">(01 Aug '12, 04:20)</span> Jaap ♦</div></div><span id="13241"></span><div id="comment-13241" class="comment"><div id="post-13241-score" class="comment-score"></div><div class="comment-text"><p>... and then use <code>dissector_add_uint("wtap_encap",</code><em>your link layer's wtap type</em><code>,</code><em>your handle</em><code>);</code></p></div><div id="comment-13241-info" class="comment-info"><span class="comment-age">(01 Aug '12, 06:23)</span> JeffMorriss ♦</div></div><span id="13342"></span><div id="comment-13342" class="comment"><div id="post-13342-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot, that works.</p></div><div id="comment-13342-info" class="comment-info"><span class="comment-age">(03 Aug '12, 02:26)</span> gyroblau</div></div><span id="13347"></span><div id="comment-13347" class="comment"><div id="post-13347-score" class="comment-score"></div><div class="comment-text"><p>Please don't forget to Accept the answer if it answers your question--see the FAQ for how this site works.</p></div><div id="comment-13347-info" class="comment-info"><span class="comment-age">(03 Aug '12, 05:51)</span> JeffMorriss ♦</div></div><span id="13361"></span><div id="comment-13361" class="comment"><div id="post-13361-score" class="comment-score"></div><div class="comment-text"><p>Which was the "that" in "that works"? Presumably not "request a link-layer type here", as nobody's requested or been assigned a link-layer header type in the past 2 days; was it "use one of the user DLTs" or "use one of the existing link-layer types"?</p><p>(Note that if you aren't just using this network type in your {university,laboratory,corporation,etc.}, so that you'd prefer to have a <em>standard</em> link-layer header type assigned, sending a message to [email protected]<a href="http://lists.tcpdump.org">lists.tcpdump.org</a> to request the link-layer header type, as per the page to which Jaap's answer points, is the first step.</p></div><div id="comment-13361-info" class="comment-info"><span class="comment-age">(03 Aug '12, 16:59)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-13218" class="comment-tools"></div><div class="clear"></div><div id="comment-13218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

