+++
type = "question"
title = "Can we add extra column in existing pcap with help of C language"
description = '''I want to add extra columns called Ue_Identity in existing pcap not by following manual procedure of wireshark .but with help of c language.I have to do like this when i will run that script as pcpa in put then it will add extra column into that pcap......'''
date = "2013-08-05T04:12:00Z"
lastmod = "2013-08-07T04:01:00Z"
weight = 23551
keywords = [ "columns" ]
aliases = [ "/questions/23551" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Can we add extra column in existing pcap with help of C language](/questions/23551/can-we-add-extra-column-in-existing-pcap-with-help-of-c-language)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23551-score" class="post-score" title="current number of votes">0</div><span id="post-23551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to add extra columns called Ue_Identity in existing pcap not by following manual procedure of wireshark .but with help of c language.I have to do like this when i will run that script as pcpa in put then it will add extra column into that pcap......</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-columns" rel="tag" title="see questions tagged &#39;columns&#39;">columns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '13, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/bcee72ced4763fe4b835a94e861d5115?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gst&#39;s gravatar image" /><p><span>gst</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gst has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Aug '13, 01:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-23551" class="comments-container"></div><div id="comment-tools-23551" class="comment-tools"></div><div class="clear"></div><div id="comment-23551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="23555"></span>

<div id="answer-container-23555" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23555-score" class="post-score" title="current number of votes">0</div><span id="post-23555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are no columns in PCAP. PCAP stands for the fileformat which contains packet capture data. Columns can be found in the output of Wireshark (on screen or print) which are defined in the currently applicable configuration file for the current profile.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '13, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-23555" class="comments-container"><span id="23558"></span><div id="comment-23558" class="comment"><div id="post-23558-score" class="comment-score"></div><div class="comment-text"><p>So then can we add extra column as I specified earlier in the output of wireshark or not?</p></div><div id="comment-23558-info" class="comment-info"><span class="comment-age">(05 Aug '13, 06:28)</span> <span class="comment-user userinfo">gst</span></div></div><span id="23559"></span><div id="comment-23559" class="comment"><div id="post-23559-score" class="comment-score"></div><div class="comment-text"><p>The answer is much the same as in your previous attempt at the same question <a href="http://ask.wireshark.org/questions/23495/dissector-to-add-column-in-existing-pcap.">http://ask.wireshark.org/questions/23495/dissector-to-add-column-in-existing-pcap.</a></p></div><div id="comment-23559-info" class="comment-info"><span class="comment-age">(05 Aug '13, 06:39)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-23555" class="comment-tools"></div><div class="clear"></div><div id="comment-23555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23569"></span>

<div id="answer-container-23569" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23569-score" class="post-score" title="current number of votes">0</div><span id="post-23569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As has been said, you can't change GUI aspects from dissector code. But if you need to run a script that processes the data, you can change the GUI preferences from the command line. Use the following for instance to add the tcp.stream field to the output:</p><pre><code>tshark -r &lt;file&gt; -R &lt;filter&gt; -o &#39;gui.column.format:&quot;No.&quot;,&quot;%m&quot;,&quot;Time&quot;,&quot;%t&quot;,&quot;Stream index&quot;,&quot;%Cus:tcp.stream:0:R&quot;,
     &quot;Source&quot;, &quot;%s&quot;,&quot;Destination&quot;, &quot;%d&quot;,&quot;Protocol&quot;, &quot;%p&quot;,&quot;Length&quot;, &quot;%L&quot;,&quot;Info&quot;, &quot;%i&quot;&#39;</code></pre><p>You can also use the <code>-T fields</code> option of tshark:</p><pre><code>tshark -r &lt;file&gt; -R &lt;filter&gt; -T fields -e frame.number -e ip.src -e ip.dst -e ...</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '13, 22:45</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23569" class="comments-container"><span id="23578"></span><div id="comment-23578" class="comment"><div id="post-23578-score" class="comment-score"></div><div class="comment-text"><p>Hey I want more explanation about thshark -o option with more examples and outputs so will you please provide me the link where i can get more explanation about this plz?</p></div><div id="comment-23578-info" class="comment-info"><span class="comment-age">(06 Aug '13, 03:23)</span> <span class="comment-user userinfo">gst</span></div></div><span id="23580"></span><div id="comment-23580" class="comment"><div id="post-23580-score" class="comment-score"></div><div class="comment-text"><p>All the info can be found in the TShark <a href="http://www.wireshark.org/docs/man-pages/tshark.html">man</a> page. A summary can also be seen by passing a <code>-h</code> or <code>-?</code> argument to tshark.</p></div><div id="comment-23580-info" class="comment-info"><span class="comment-age">(06 Aug '13, 03:26)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-23569" class="comment-tools"></div><div class="clear"></div><div id="comment-23569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23595"></span>

<div id="answer-container-23595" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23595-score" class="post-score" title="current number of votes">0</div><span id="post-23595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>GST, what is the value of "ue_identity" that you would want to be present in such a column? If by "UE" you're referring to the 3GPP term, there'd be a great many different temporary and permanent identities used for a UE across the different signaling interfaces/protocols used by most mobility procedures you'd be tracing in Wireshark.</p><p>What specifically are you trying to accomplish? I've actually written a great many perl scripts to work with tshark to parse most of the relevant protocols to uniquely map out messages related to a given UE (through GTP-C, TCAP, MAP, Diameter/Gx/Gy/S6a-d, S1AP, RANAP, etc.), since in Wireshark alone it can be a total pain.</p><p>Anyway, if you're trying to trace a UE identity through a .pcap file, and by UE you mean the 3GPP 'user equipment', I wish it were as simple as a column. If you can be specific on your end goal, there's a good chance I have a scripted solution already written for it.</p><p>Edit: Oh, and if it really is just one field you want there, in the GUI, right-click the field in a packet and click "Apply as Column".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '13, 21:05</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Aug '13, 21:08</strong> </span></p></div></div><div id="comments-container-23595" class="comments-container"><span id="23598"></span><div id="comment-23598" class="comment"><div id="post-23598-score" class="comment-score"></div><div class="comment-text"><p>Hello Quadratic, what i have to do is that when i will run my program with pcap file as input then it should show the header No Time Src Dst Protocol Length Ue_Identity Info in wireshark and in the column of Ue_Identity it will represent the its TMSI value as ue_identity for related message in that.(Basically what I m trying to trace whole Ue signaling in wireshark how many times it connected and disconnected with what context so in front related messages to Ue it will show its TMSI in that column but this should be done by C not manually by following to add column through wireshark)</p></div><div id="comment-23598-info" class="comment-info"><span class="comment-age">(06 Aug '13, 21:58)</span> <span class="comment-user userinfo">gst</span></div></div><span id="23608"></span><div id="comment-23608" class="comment"><div id="post-23608-score" class="comment-score"></div><div class="comment-text"><p>Which type of TMSI (TMSI, P-TMSI, M-TMSI, S-TMSI, GUTI) in which protocol container (RANAP/NAS, NBAP/NAS, S1AP/NAS)?</p><p>The dissector can decode TMSI values and you can display it in its own column. The value will change for the subscriber so you'll need to track old TMSI to new as well, and a precise how-to for that depends on what TMSI you're talking about and for what protocol.</p></div><div id="comment-23608-info" class="comment-info"><span class="comment-age">(07 Aug '13, 04:01)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-23595" class="comment-tools"></div><div class="clear"></div><div id="comment-23595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

