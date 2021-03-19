+++
type = "question"
title = "NetScaler to Pcap"
description = '''Hi,  I have a script in order to apply a lot of test about one trace that I give in the argument of script. Today, I have to add the feature of support traces of NetScaler and My script work in libpcap format. So I have tried to convert netscaler trace to libcap format with wireshark because I am kn...'''
date = "2014-02-19T03:38:00Z"
lastmod = "2017-04-27T05:02:00Z"
weight = 30000
keywords = [ "netscaler", "convert", "libpcap", "format" ]
aliases = [ "/questions/30000" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [NetScaler to Pcap](/questions/30000/netscaler-to-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30000-score" class="post-score" title="current number of votes">0</div><span id="post-30000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,<br />
I have a script in order to apply a lot of test about one trace that I give in the argument of script. Today, I have to add the feature of support traces of NetScaler and My script work in libpcap format. So I have tried to convert netscaler trace to libcap format with wireshark because I am know that wireshark support this format but, I have been able to change the format. How Could I change the format of this trace?<br />
Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-netscaler" rel="tag" title="see questions tagged &#39;netscaler&#39;">netscaler</span> <span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span> <span class="post-tag tag-link-format" rel="tag" title="see questions tagged &#39;format&#39;">format</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '14, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/1755f4baee4c2c555287ee3527c7bc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cansado2930&#39;s gravatar image" /><p><span>Cansado2930</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cansado2930 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-30000" class="comments-container"></div><div id="comment-tools-30000" class="comment-tools"></div><div class="clear"></div><div id="comment-30000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30002"></span>

<div id="answer-container-30002" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30002-score" class="post-score" title="current number of votes">4</div><span id="post-30002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Cansado2930 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>AFIAK, you cannot convert a Netscaler format to pcap/pcapng directly with Wireshark/tshark/editcap, at least it did not work in my tests.</p><pre><code>tshark -nr nstrace1_test.cap -w output.pcap
tshark: The capture file being read can&#39;t be written as a &quot;pcapng&quot; file.

editcap nstrace1_test.cap output.pcap
editcap: Can&#39;t open or create output.pcap: Files from that network type can&#39;t be saved in that format</code></pre><p>However, there seems to be a Citrix tool to convert those files.</p><blockquote><p>nsapimgr -s tcpdump=1 -K nstrace1.cap -k output.pcap</p></blockquote><p>Please ask in the Citrix forum for details</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '14, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Feb '14, 05:40</strong> </span></p></div></div><div id="comments-container-30002" class="comments-container"><span id="61069"></span><div id="comment-61069" class="comment"><div id="post-61069-score" class="comment-score"></div><div class="comment-text"><p>The <a href="https://support.citrix.com/article/CTX205438">citrix doc</a> lists commands to covert nstrace files (.cap) to pcap files.</p><p>I've just used it with a current Netscaler 11.1.</p></div><div id="comment-61069-info" class="comment-info"><span class="comment-age">(27 Apr '17, 05:02)</span> <span class="comment-user userinfo">Uli</span></div></div></div><div id="comment-tools-30002" class="comment-tools"></div><div class="clear"></div><div id="comment-30002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

