+++
type = "question"
title = "library for display filters"
description = '''I am implementing dissector for sip and rtp protocols. I have search a lot on libpcap and wireshark support for filtering sip traffic. Currently, I am using tshark process to execute display filters to capture sip traffic based on some sip header values (eg. call-id).  I want to use this feature as ...'''
date = "2014-06-10T18:20:00Z"
lastmod = "2014-06-12T11:38:00Z"
weight = 33630
keywords = [ "display-filter", "tshark", "wireshark" ]
aliases = [ "/questions/33630" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [library for display filters](/questions/33630/library-for-display-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33630-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am implementing dissector for sip and rtp protocols. I have search a lot on libpcap and wireshark support for filtering sip traffic.</p><p>Currently, I am using tshark process to execute display filters to capture sip traffic based on some sip header values (eg. call-id).</p><p>I want to use this feature as a library to integrate with my module. Let me know if this is possible to do by compiling any source as library.</p></div><div id="question-tags" class="tags-container tags">display-filter tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '14, 18:20</strong></p><img src="https://secure.gravatar.com/avatar/b20893bc6249bcae9120f27d61284953?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="creativeDrive&#39;s gravatar image" /><p>creativeDrive<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="creativeDrive has no accepted answers">0%</span></p></div></div><div id="comments-container-33630" class="comments-container"><span id="33703"></span><div id="comment-33703" class="comment"><div id="post-33703-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I am <strong>implementing dissector for sip</strong> and rtp protocols.<br />
I want to use this feature as a library to integrate with my <strong>module.</strong></p></blockquote><p>If you say <strong>module</strong> do you mean your dissector?</p><p>If so, is your question how to use display filters in the code of your dissector?</p></div><div id="comment-33703-info" class="comment-info"><span class="comment-age">(12 Jun '14, 05:25)</span> Kurt Knochner ♦</div></div><span id="33729"></span><div id="comment-33729" class="comment"><div id="post-33729-score" class="comment-score"></div><div class="comment-text"><p>Well, currently I am reading existing pcap which dumps all IP packets (because I need all of them in general) and filter through using tshark command (tshark -r &lt;input.pcap&gt; -w &lt;output.pcap&gt; 'sip.Call-Id == "xxxxx"').</p><p>As Sip display filters are already available (<a href="http://www.wireshark.org/docs/dfref/s/sip.html)">http://www.wireshark.org/docs/dfref/s/sip.html)</a> I would like to use them as an API with my code to filter out interested traffic. This is kind of 2 pass filter.</p><p>But, it would be help if I can apply the display filter while capturing live traffic.</p></div><div id="comment-33729-info" class="comment-info"><span class="comment-age">(12 Jun '14, 11:03)</span> creativeDrive</div></div></div><div id="comment-tools-33630" class="comment-tools"></div><div class="clear"></div><div id="comment-33630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33733"></span>

<div id="answer-container-33733" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33733-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>O.K. according to your comment, it sounds to me, like you want to create your own version of Wireshark/tshark, limited to SIP/RTP and that you intend to use display filters during the capturing process.</p><p>Well, then the answer is: There is no 'official' library that's easy to use, because behind the scenes of display filters you will find the whole dissection engine of Wireshark. Yes, you can use that functionality (libwireshark) in your own code, but <strong>no</strong> it's not simply linking the library against your code.</p><p>Please read the following answer:</p><blockquote><p><a href="http://stackoverflow.com/questions/10308127/using-libwireshark-to-get-wireshark-functionality-programatically">http://stackoverflow.com/questions/10308127/using-libwireshark-to-get-wireshark-functionality-programatically</a></p></blockquote><p>Then, if you still think you need that, take a look at projects using libwireshark and learn from their example.</p><blockquote><p><a href="https://www.altamiracorp.com/blog/employee-posts/how-to-use-libwireshark-to-dis">https://www.altamiracorp.com/blog/employee-posts/how-to-use-libwireshark-to-dis</a><br />
<a href="https://github.com/joeferner/node-shark">https://github.com/joeferner/node-shark</a><br />
<a href="http://wirepy.readthedocs.org/">http://wirepy.readthedocs.org/</a><br />
<a href="https://github.com/armenb/sharktools">https://github.com/armenb/sharktools</a><br />
<a href="http://netexpect.org/wiki">http://netexpect.org/wiki</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '14, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-33733" class="comments-container"><span id="33736"></span><div id="comment-33736" class="comment"><div id="post-33736-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt for giving me pointers in right direction. I need to explore more as per my requirement.</p></div><div id="comment-33736-info" class="comment-info"><span class="comment-age">(12 Jun '14, 12:09)</span> creativeDrive</div></div></div><div id="comment-tools-33733" class="comment-tools"></div><div class="clear"></div><div id="comment-33733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

