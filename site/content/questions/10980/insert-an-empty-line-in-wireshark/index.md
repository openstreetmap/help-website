+++
type = "question"
title = "Insert an empty line in Wireshark"
description = '''Is there a possibility to insert an empty line in the &quot;packet list pane&quot; of Wireshark on some particular spot?  It should be as in the picture below - lines 8 and 10 look like &quot;inserted&quot;. Wenn an empty line is marked, the packet details pane and the packet bytes pane shouls be empty too. I think abo...'''
date = "2012-05-15T02:01:00Z"
lastmod = "2016-02-29T06:29:00Z"
weight = 10980
keywords = [ "packetpane", "diff", "compare", "difference" ]
aliases = [ "/questions/10980" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Insert an empty line in Wireshark](/questions/10980/insert-an-empty-line-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10980-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a possibility to insert an empty line in the "packet list pane" of Wireshark on some particular spot?</p><p>It should be as in the picture below - lines 8 and 10 look like "inserted". Wenn an empty line is marked, the packet details pane and the packet bytes pane shouls be empty too.</p><p>I think about two possibilities:</p><ol><li>The PCAP File should not be changed, only the view of the file, or</li><li>insert an "empty Packet" in PCAP File, and than show the changed file in Wireshark</li></ol><p>Is something like this possible?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/InsertEmptyLineInWireshark.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">packetpane diff compare difference</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '12, 02:01</strong></p><img src="https://secure.gravatar.com/avatar/f45848e2181a57e335916a9bc57aa0c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ZvDj&#39;s gravatar image" /><p>ZvDj<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ZvDj has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 06 Nov '13, 04:38</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-10980" class="comments-container"></div><div id="comment-tools-10980" class="comment-tools"></div><div class="clear"></div><div id="comment-10980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="10981"></span>

<div id="answer-container-10981" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10981-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think it is possible, because Wireshark is a tool to dissect and analyze what is there, and not an editor.</p><p>Out of curiosity - why would you need a feature like that? I can't think of any reason why someone would want to add empty lines at all...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '12, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10981" class="comments-container"></div><div id="comment-tools-10981" class="comment-tools"></div><div class="clear"></div><div id="comment-10981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10982"></span>

<div id="answer-container-10982" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10982-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You cannot insert an empty line, but you can <strong>ignore</strong> a certain packet, which looks almost <strong>like an empty line</strong>.</p><ol><li>select a packet</li><li>press CTRL-X (or right-click and select "Ignore Packet (toggle)"</li><li>to unhide, press CTRL-X again</li></ol><p>You can combine this with previously injected/inserted packets in the pcap file (e.g. ICMP packets with a certain length, to identify them).</p><p>Unfortunately, I don't know any tool that is able to insert packets into a pcap file at a certain position.</p><p><strong>EDIT</strong>: I just remembered <strong>Network Expect</strong>. You can 'possibly' do it with Network Expect, however it requires quite some scripting know-how.</p><p><strong>Sample</strong><br />
just modifying a pcap file (ip rewrite). Inserting should be possible by calling 'send_network ip' twice at a certain position (counter) in the pcap file. Once for the original IP packet and once again for a newly created (injected/inserted) IP/ICMP packet.</p><blockquote><p><code>http://netexpect.org/wiki/RewriteAndReplay</code></p></blockquote><p>If you just want a <strong>marker</strong> in your capture file please use that function (<strong>CTRL-M</strong>).</p><p>Otherwise, please tell us more, as @Jasper already mentioned.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '12, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 May '12, 03:24</p></div></div><div id="comments-container-10982" class="comments-container"><span id="10983"></span><div id="comment-10983" class="comment"><div id="post-10983-score" class="comment-score"></div><div class="comment-text"><p>I thought of that, too, but that would remove a packet from view which I don't think was intended - if you want to have an empty line without losing anything you can't ignore a packet :-)</p></div><div id="comment-10983-info" class="comment-info"><span class="comment-age">(15 May '12, 02:52)</span> Jasper ♦♦</div></div><span id="10984"></span><div id="comment-10984" class="comment"><div id="post-10984-score" class="comment-score"></div><div class="comment-text"><p>that's true and I'm suggesting it only out of thin air, as there was not enough information in the original post ;-)</p></div><div id="comment-10984-info" class="comment-info"><span class="comment-age">(15 May '12, 03:02)</span> Kurt Knochner ♦</div></div><span id="10985"></span><div id="comment-10985" class="comment"><div id="post-10985-score" class="comment-score"></div><div class="comment-text"><p>see latest EDIT above</p></div><div id="comment-10985-info" class="comment-info"><span class="comment-age">(15 May '12, 03:20)</span> Kurt Knochner ♦</div></div><span id="10986"></span><div id="comment-10986" class="comment"><div id="post-10986-score" class="comment-score"></div><div class="comment-text"><p>Thanks for answers.</p><p>My intention is to open two instances of wireshark (thanks Kurt) and to compare two PCAP Files. If some Packet in a first file is absent, there should be shown an empty line (in the firstInstance), and at the second file (in the second instance) should be shown the whole packet.</p><p>The "packet list pane" is nothing but some kind of ListView Control, and there should be possible to insert un empty line. The question is only, if something like this in Wireshark possible is.</p><p>@Kurt: I will try NetExect soon. Thx</p><p>Best regards to all Zvonko</p></div><div id="comment-10986-info" class="comment-info"><span class="comment-age">(15 May '12, 04:49)</span> ZvDj</div></div><span id="10987"></span><div id="comment-10987" class="comment"><div id="post-10987-score" class="comment-score"></div><div class="comment-text"><p>I mean NetExpect ;)</p></div><div id="comment-10987-info" class="comment-info"><span class="comment-age">(15 May '12, 04:49)</span> ZvDj</div></div><span id="10988"></span><div id="comment-10988" class="comment not_top_scorer"><div id="post-10988-score" class="comment-score"></div><div class="comment-text"><p>&gt; <em>The question is only, if something like this in Wireshark possible is</em>.</p><p>Unfortunately no. See answers/comments above.</p><p>Regarding "pcap diff", see my answer below.</p></div><div id="comment-10988-info" class="comment-info"><span class="comment-age">(15 May '12, 05:24)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-10982" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-10982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10992"></span>

<div id="answer-container-10992" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10992-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To answer your question regarding <strong>pcap diff</strong></p><p>If you "just" want a PCAP diff, there are tools available for that (e.g. pcapdiff). These tools will not show the differences in a graphical way, as they are mostly console tools.</p><p><strong>tpcat (Windows)</strong><br />
<code>http://sourceforge.net/projects/tpcat/</code></p><p><strong>PcapDiff (Perl)</strong><br />
<code>http://sourceforge.net/projects/pcapdiff/</code></p><p><strong>tracediff</strong><br />
<code>http://www.wand.net.nz/trac/libtrace/wiki/TraceDiff</code></p><p><strong>pcapdiff (python)</strong><br />
<code>http://www.eff.org/testyourisp/pcapdiff/</code></p><p>Apparently, the later one is no longer accessible, however it's in several linux repositories (e.g. Fedora - <code>yum install pcapdiff</code>).</p><p>Of course, you can also use the <strong>built-in compare</strong> option<br />
<code>http://www.wireshark.org/docs/wsug_html_chunked/ChStatCompareCaptureFiles.html</code></p><p>It is also possible to compare the text form of the captures. <strong>HOWEVER</strong> this will only work, if there are NO major changes in the cpature files, like NAT, packet reordering, etc !!</p><p>Export the cpature files with tshark into text form and diff the output with <strong>WinMerge</strong>.</p><blockquote><p><code>tshark -r cap1.cap &gt; cap1.txt</code><br />
<code>tshark -r cap2.cap &gt; cap2.txt</code></p></blockquote><p>Diff both files with <strong>WinMerge</strong>:</p><blockquote><p><code>http://justpaste.it/zky</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '12, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-10992" class="comments-container"><span id="10998"></span><div id="comment-10998" class="comment"><div id="post-10998-score" class="comment-score"></div><div class="comment-text"><p>It would be nice, when "just PCAP diff" were :)</p><p>There should be Compare options, compare filter, and of course, it should funct fast and also with very long files.</p></div><div id="comment-10998-info" class="comment-info"><span class="comment-age">(15 May '12, 08:53)</span> ZvDj</div></div><span id="10999"></span><div id="comment-10999" class="comment"><div id="post-10999-score" class="comment-score"></div><div class="comment-text"><p>feel free to implement all that in wireshark :-) You will gain a lot of friends ;-) In the meantime you have all the options described above.</p></div><div id="comment-10999-info" class="comment-info"><span class="comment-age">(15 May '12, 09:11)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-10992" class="comment-tools"></div><div class="clear"></div><div id="comment-10992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50578"></span>

<div id="answer-container-50578" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50578-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Pretty sure scapy can do this, but the easiest one will be ColaSoft PacketBuilder</p><p>Original capture <img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2016-02-29_at_15.18.37.png" alt="alt text" /></p><p>After importing it to PacketBuilder and inserting 2 entries ( see new frames 4 and 7)</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2016-02-29_at_15.23.37.png" alt="alt text" /></p><p>you can then edit the values of the fields you inserted</p><p>out of curiosity, why would you want to do this? I use colasoft sometimes for a way to create asynchronous environments</p><p>hope this helps</p><p>thx</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Feb '16, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/5002cb544de33c526f994599d3ae391f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppcap&#39;s gravatar image" /><p>ppcap<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppcap has one accepted answer">50%</span> </br></br></p></img></div></div><div id="comments-container-50578" class="comments-container"></div><div id="comment-tools-50578" class="comment-tools"></div><div class="clear"></div><div id="comment-50578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

