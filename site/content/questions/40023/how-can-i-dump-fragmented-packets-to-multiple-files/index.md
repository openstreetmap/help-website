+++
type = "question"
title = "How can I dump fragmented packets to multiple files?"
description = '''I have to read a capture file and dump its packets to multiple files, according to several field values of the packets. In order to do that, I have created a postdissector using Lua to extract the field values of the packets.  The problem is with the fragmented packets. These packets are divided in ...'''
date = "2015-02-23T07:58:00Z"
lastmod = "2015-06-28T10:37:00Z"
weight = 40023
keywords = [ "multiple-files", "lua", "fragmentation", "dissector", "dump" ]
aliases = [ "/questions/40023" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I dump fragmented packets to multiple files?](/questions/40023/how-can-i-dump-fragmented-packets-to-multiple-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40023-score" class="post-score" title="current number of votes">0</div><span id="post-40023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have to read a capture file and dump its packets to multiple files, according to several field values of the packets. In order to do that, I have created a postdissector using Lua to extract the field values of the packets.</p><p>The problem is with the fragmented packets. These packets are divided in several frames and the "Fragmented" frames don't have the necessary field values in order to dump them in the correct file. And if I ignore the fragmented packets, I will have the result below.</p><p>In the following image I have the frames of the source capture file. Look as one of the packets is fragmented in frames 8 and 9.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/source_capture_file.png" alt="alt text" /></p><p>In the following image I have the frames of the result pcap. As I ignored the fragmented frame in the original capture file, in the result file I have a fragmented packet without the required information, as shown in the source file, packet 9. <img src="https://osqa-ask.wireshark.org/upfiles/dumped.png" alt="alt text" /></p><p>So I would like that my result pcap would contain the same packets as the source pcap. I don't know if the "ip.reassembled_in" field could be useful, as it could allow me to associate the "Fragmented" frame to the frame with the information I need. But as this frame with the information appears always after the fragmented frame, maybe I could keep the fragmented frame temporarily in a array, and after that, when the frame with the information was reached, I could associate them, bring the fragmented frame and dump both to a file, but I don't know how I can keep a frame and after dump it to a file.</p><p>Do you know how to do that or any way to solve my problem with the fragmented packets?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-multiple-files" rel="tag" title="see questions tagged &#39;multiple-files&#39;">multiple-files</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-fragmentation" rel="tag" title="see questions tagged &#39;fragmentation&#39;">fragmentation</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-dump" rel="tag" title="see questions tagged &#39;dump&#39;">dump</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '15, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/4e4811c2faea7fb721e80c71961bca0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nn15&#39;s gravatar image" /><p><span>nn15</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nn15 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Feb '15, 09:41</strong> </span></p></div></div><div id="comments-container-40023" class="comments-container"><span id="40024"></span><div id="comment-40024" class="comment"><div id="post-40024-score" class="comment-score"></div><div class="comment-text"><p>The question should be: do you need all the complete frames with (the possible fragmented) data, or do you need frames with (the possible reassembled) data? The former is tricky, the latter should be doable.</p></div><div id="comment-40024-info" class="comment-info"><span class="comment-age">(23 Feb '15, 08:15)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="40027"></span><div id="comment-40027" class="comment"><div id="post-40027-score" class="comment-score"></div><div class="comment-text"><p>Ideally I would like to obtain all the complete frames with the possible fragmented data, but if I can not do that, the frames with the reassembled data would be an acceptable result.</p></div><div id="comment-40027-info" class="comment-info"><span class="comment-age">(23 Feb '15, 09:04)</span> <span class="comment-user userinfo">nn15</span></div></div></div><div id="comment-tools-40023" class="comment-tools"></div><div class="clear"></div><div id="comment-40023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43634"></span>

<div id="answer-container-43634" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43634-score" class="post-score" title="current number of votes">0</div><span id="post-43634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>[This is an old question, but since no one's answered it yet...]</p><p>Saving the fragments in a Lua table won't work very well - for one thing, the <code>Tvb</code> and <code>Pinfo</code> objects passed into the <code>proto.dissector()</code> function are not safe to keep around past the life/scope of the <code>proto.dissector()</code> function; and if you extracted all of it into something that <em>is</em> safe to keep around (like <code>ByteArrays</code> and strings and so on) that would be a lot of data.</p><p>But you don't need to do that - what you need is to have the packets dissected or tapped <strong>twice</strong>. The first time to figure out which SIP messages you want to export to which files, and to let the IP fragments be associated with each other; and the second time to export the IP packet frames to the relevant file, based on the decisions of the first time.</p><p>In Wireshark (not tshark) you can force the packets to be re-tapped again with the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Gui.html#lua_fn_retap_packets__"><code>retap_packets()</code></a> function, which also makes them be dissected again. In tshark the packets will be processed twice if the <code>-2</code> command line option is used, but I'll assume you only need Wireshark support not tshark.</p><p>The "trick" is to know when to invoke <code>retap_packets()</code> in your Lua script, and one way to do so is to create a <code>Listener</code> tap and define its <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Listener.html#lua_class_attrib_listener_reset"><code>listener.reset()</code></a> function to call <code>retap_packets()</code>. Since the <code>listener.reset()</code> function is invoked by Wireshark at the end of the capture file, calling <code>retap_packets()</code> at that time will do it all again. (you may need to prevent <code>retap_packets()</code> from being invoked again and again, so wrap it in a if-then with a boolean) Another way to do it is if your Lua script creates a GUI menu item to trigger this exporting, then you can just invoke <code>retap_packets()</code> inside the menu item's callback function.</p><p>So once you decide how you want to proceed with that model, you could use the "ip.reassembled_in" field of every packet and match the value to a Lua table of SIP packets you want to export - a Lua table which you created in the first pass based on the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Pinfo.html#lua_class_attrib_pinfo_number"><code>pinfo.number</code></a> of the SIP messages you want. Or you could do the reverse: keep a Lua table of all the packet numbers you want to export by using the "ip.fragment" field in the SIP packets you want to export, and query the table in the second pass using <code>pinfo.number</code>) of every packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '15, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></img></div></div><div id="comments-container-43634" class="comments-container"></div><div id="comment-tools-43634" class="comment-tools"></div><div class="clear"></div><div id="comment-43634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

