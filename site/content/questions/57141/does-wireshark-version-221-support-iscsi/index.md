+++
type = "question"
title = "Does WireShark Version 2.2.1 support iSCSI"
description = '''I am trying to use WireShark version 2.2.1 to examine a pcapng file that contains iSCSI PDUs. The problem that I am having is when the trace is opened the iSCSI PDUs are not decoded and they show up as tcp frames with a payload. Can you please tell me what I need to do in order to get these frames d...'''
date = "2016-11-08T01:46:00Z"
lastmod = "2016-11-11T04:21:00Z"
weight = 57141
keywords = [ "decode", "iscsi", "support", "decodes", "wireshark" ]
aliases = [ "/questions/57141" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Does WireShark Version 2.2.1 support iSCSI](/questions/57141/does-wireshark-version-221-support-iscsi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57141-score" class="post-score" title="current number of votes">0</div><span id="post-57141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to use WireShark version 2.2.1 to examine a pcapng file that contains iSCSI PDUs. The problem that I am having is when the trace is opened the iSCSI PDUs are not decoded and they show up as tcp frames with a payload. Can you please tell me what I need to do in order to get these frames decoded.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-iscsi" rel="tag" title="see questions tagged &#39;iscsi&#39;">iscsi</span> <span class="post-tag tag-link-support" rel="tag" title="see questions tagged &#39;support&#39;">support</span> <span class="post-tag tag-link-decodes" rel="tag" title="see questions tagged &#39;decodes&#39;">decodes</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '16, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/b2d0183529e31bcca9461e7348206c16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LouD&#39;s gravatar image" /><p><span>LouD</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LouD has no accepted answers">0%</span></p></div></div><div id="comments-container-57141" class="comments-container"></div><div id="comment-tools-57141" class="comment-tools"></div><div class="clear"></div><div id="comment-57141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="57147"></span>

<div id="answer-container-57147" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57147-score" class="post-score" title="current number of votes">1</div><span id="post-57147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>iSCSI is supported by Wireshark. Port 3260/tcp is the default port of the dissector.</p><p>If your connection is running on a different port please use 'Decode as' and choose 'iSCSI'.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '16, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-57147" class="comments-container"><span id="57163"></span><div id="comment-57163" class="comment"><div id="post-57163-score" class="comment-score"></div><div class="comment-text"><p>My iSCSI traffic is using port 3260 but the traffic is not being dissected. When I try using the 'Decode as' I do not get iSCSI listed as a choice.</p></div><div id="comment-57163-info" class="comment-info"><span class="comment-age">(08 Nov '16, 07:56)</span> <span class="comment-user userinfo">LouD</span></div></div><span id="57167"></span><div id="comment-57167" class="comment"><div id="post-57167-score" class="comment-score"></div><div class="comment-text"><p>When you choose <code>Analyze -&gt; Enabled Protocols</code> and write <code>iscsi</code> to the <code>Search</code> field at the bottom of the window, what can you see in the protocol list in the upper part of the window?</p></div><div id="comment-57167-info" class="comment-info"><span class="comment-age">(08 Nov '16, 08:12)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="57255"></span><div id="comment-57255" class="comment"><div id="post-57255-score" class="comment-score"></div><div class="comment-text"><p>iSCSI shows up as an Enabled Protocol.</p><p>Another interesting thing is I uploaded the trace to CloudShark and CloudShark decodes the packets as iSCSI PDUs, but for some reason WireShark does not.</p></div><div id="comment-57255-info" class="comment-info"><span class="comment-age">(10 Nov '16, 03:53)</span> <span class="comment-user userinfo">LouD</span></div></div><span id="57257"></span><div id="comment-57257" class="comment"><div id="post-57257-score" class="comment-score"></div><div class="comment-text"><p>Can you share the pcap file (link to Cloudshark) publicly?</p></div><div id="comment-57257-info" class="comment-info"><span class="comment-age">(10 Nov '16, 04:19)</span> <span class="comment-user userinfo">Uli</span></div></div><span id="57258"></span><div id="comment-57258" class="comment"><div id="post-57258-score" class="comment-score"></div><div class="comment-text"><p>Here is the link to the trace in cloud shark</p><p><a href="https://www.cloudshark.org/captures/37eba34a4db8">https://www.cloudshark.org/captures/37eba34a4db8</a></p></div><div id="comment-57258-info" class="comment-info"><span class="comment-age">(10 Nov '16, 05:04)</span> <span class="comment-user userinfo">LouD</span></div></div><span id="57259"></span><div id="comment-57259" class="comment not_top_scorer"><div id="post-57259-score" class="comment-score"></div><div class="comment-text"><p>Wireshark 2.2.1 decodes the iSCSI frames here. Is 'iscsi_tcp' enabled (Analyze -&gt; Enabled Protocols) at your site?</p></div><div id="comment-57259-info" class="comment-info"><span class="comment-age">(10 Nov '16, 05:39)</span> <span class="comment-user userinfo">Uli</span></div></div><span id="57260"></span><div id="comment-57260" class="comment not_top_scorer"><div id="post-57260-score" class="comment-score"></div><div class="comment-text"><p>Do you have anything in the Decode As... dialog (Analyze -&gt; Decode As...)?</p></div><div id="comment-57260-info" class="comment-info"><span class="comment-age">(10 Nov '16, 05:50)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="57262"></span><div id="comment-57262" class="comment not_top_scorer"><div id="post-57262-score" class="comment-score"></div><div class="comment-text"><p>no there is nothing in the Decode as field</p></div><div id="comment-57262-info" class="comment-info"><span class="comment-age">(10 Nov '16, 06:07)</span> <span class="comment-user userinfo">LouD</span></div></div><span id="57263"></span><div id="comment-57263" class="comment not_top_scorer"><div id="post-57263-score" class="comment-score"></div><div class="comment-text"><p>As you can see in the screen shot below there is nothing in the Decode as field and iSCSI does not show as an option to add to the Decode as field.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2016_11_10_07_04_27_Greenshot2.PNG" width="600" height="320" /></p></div><div id="comment-57263-info" class="comment-info"><span class="comment-age">(10 Nov '16, 06:12)</span> <span class="comment-user userinfo">LouD</span></div></div><span id="57266"></span><div id="comment-57266" class="comment not_top_scorer"><div id="post-57266-score" class="comment-score"></div><div class="comment-text"><p>Look at the bottom of the Decode as list, lower case initial letters come last in the list.</p></div><div id="comment-57266-info" class="comment-info"><span class="comment-age">(10 Nov '16, 06:22)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="57268"></span><div id="comment-57268" class="comment not_top_scorer"><div id="post-57268-score" class="comment-score"></div><div class="comment-text"><p>Maybe my last comment has been overlooked:</p><p>Is 'iscsi_tcp' enabled (Analyze -&gt; Enabled Protocols) at your site?</p></div><div id="comment-57268-info" class="comment-info"><span class="comment-age">(10 Nov '16, 06:29)</span> <span class="comment-user userinfo">Uli</span></div></div><span id="57292"></span><div id="comment-57292" class="comment not_top_scorer"><div id="post-57292-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for your help the problem has been solved. I found iSCSI in the bottom of the Decode list and when I selected it the frames are now decoded. Thank you for your help</p></div><div id="comment-57292-info" class="comment-info"><span class="comment-age">(11 Nov '16, 00:53)</span> <span class="comment-user userinfo">LouD</span></div></div></div><div id="comment-tools-57147" class="comment-tools"><span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a></div><div class="clear"></div><div id="comment-57147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57310"></span>

<div id="answer-container-57310" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57310-score" class="post-score" title="current number of votes">0</div><span id="post-57310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for providing the capture file. The iSCSI packets do show up as iSCSI in my Wireshark 2.2.1 installation. You might want to check your iSCSI protocol preferences. Here are the settings of my Wireshark profile:</p><pre><code>$ tshark -G currentprefs | egrep &quot;^#?iscsi&quot;
#iscsi.protocol_version: Draft 13
#iscsi.desegment_iscsi_messages: TRUE
#iscsi.bogus_pdu_filter: TRUE
#iscsi.demand_good_f_bit: FALSE
#iscsi.bogus_pdu_max_data_len: 262144
#iscsi.target_ports: 3260
#iscsi.target_system_port: 860
$</code></pre><p>If that does not help, maybe removing your <code>preferences</code> file altogether might solve the issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '16, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></img></div></div><div id="comments-container-57310" class="comments-container"></div><div id="comment-tools-57310" class="comment-tools"></div><div class="clear"></div><div id="comment-57310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

