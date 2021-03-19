+++
type = "question"
title = "How can I decrypt SSL session with Lua dissector ?"
description = '''Hello everyone I used to decrypt HTTPS session by providing &quot;Client Random&quot; and &quot;Master Secret&quot; into wireshark. Recently, I need to decrypt SSL session which is created in USB communication. USB header is parsed by wireshark.  But some byte and SSL header are not parsed by wireshark. it just show me...'''
date = "2016-10-03T23:05:00Z"
lastmod = "2016-10-16T13:33:00Z"
weight = 56115
keywords = [ "ssl_decrypt", "ssl", "dissector", "sub-dissector", "lua" ]
aliases = [ "/questions/56115" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I decrypt SSL session with Lua dissector ?](/questions/56115/how-can-i-decrypt-ssl-session-with-lua-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56115-score" class="post-score" title="current number of votes">1</div><span id="post-56115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone</p><p>I used to decrypt HTTPS session by <a href="https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/">providing "Client Random" and "Master Secret" into wireshark.</a></p><p>Recently, I need to decrypt SSL session which is created in USB communication. USB header is parsed by wireshark.</p><p>But some byte and SSL header are not parsed by wireshark. it just show me payload as "Leftover Capture Data"</p><p><img src="https://osqa-ask.wireshark.org/upfiles/1_49orC6T.jpg" alt="alt text" /></p><p>So I decide to use Lua script for parsing "Leftover Capture Data" as 28-byte unknown protocol and SSL.</p><p>My Lua script is</p><pre><code>    local ios_usb = Proto(&quot;iOS_USB&quot;, &quot;iOS USB Protocol&quot;)
    local ios_temp = Proto(&quot;iOS&quot;, &quot;iOS USB TEMP Protocol&quot;)

    local msgtype  = ProtoField.new( &quot;Unknown #1&quot;,&quot;ios.msgtype&quot;, ftypes.UINT32)
    local memaddr  = ProtoField.new( &quot;Unknown #2&quot;,&quot;ios.memaddr&quot;, ftypes.UINT32)
    local memlen   = ProtoField.new( &quot;Unknown #3&quot;, &quot;ios.memlen&quot;,ftypes.UINT32)
    local regdata  = ProtoField.new( &quot;Unknown #4&quot;,&quot;ios.regdata&quot;, ftypes.UINT32)
    local stopdata1 = ProtoField.new( &quot;Unknown #5&quot;,&quot;ios.stopdata1&quot;, ftypes.UINT32)
    local stopdata2 = ProtoField.new( &quot;Unknown #6&quot;,&quot;ios.stopdata2&quot;, ftypes.UINT32)
    local stopdata3 = ProtoField.new( &quot;Unknown #7&quot;, &quot;ios.stopdata3&quot;,ftypes.UINT32)

    ios_usb.fields = {msgtype, memaddr, memlen, regdata, stopdata1, stopdata2, stopdata3}

    local f_urb_type = Field.new(&quot;usb.urb_type&quot;)
    local f_transfer_type = Field.new(&quot;usb.transfer_type&quot;)
    local f_endpoint = Field.new(&quot;usb.endpoint_number.endpoint&quot;)

    function ios_usb.dissector(tvbuf, pktinfo, root)
     pktinfo.cols.protocol:set(&quot;iOS_USB&quot;)
     local pktlen = tvbuf:reported_length_remaining()

     if pktlen &lt; 28 then
        return pktlen
    end

    if pktlen == 28 then

        root:add(ios_temp,tvbuf:range(0,0))
        return 28
    end

     local tree = root:add(ios_usb, tvbuf:range(0,pktlen))
     local transfer_type = tonumber(tostring(f_transfer_type))
     local ssl_dis =Dissector.get(&quot;ssl&quot;)

                pktinfo.cols.protocol = ios_usb.name

                tree:add(msgtype, tvbuf:range(0,4))
                tree:add(memaddr, tvbuf:range(4,4))
                tree:add(memlen, tvbuf:range(8,4))
                tree:add(regdata, tvbuf:range(12,4))
                tree:add(stopdata1, tvbuf:range(16,4))
                tree:add(stopdata2, tvbuf:range(20,4))
                tree:add(stopdata3, tvbuf:range(24,4))

    local newbuf = tvbuf:range(28,pktlen-28):tvb()
    local first = tvbuf:range(28,1):uint()

    if first == 0x16 or first == 0x17 then

            ssl_dis:call(newbuf,pktinfo,root)
    end

        return pktlen
    end

function ios_usb.init()

    local usb_bulk_dissectors = DissectorTable.get(&quot;usb.bulk&quot;)
    usb_bulk_dissectors:add(0xFF, ios_usb)

end</code></pre><p>This script can parse SSL header successfully</p><p>I also extract Client Random and Master secret. And I put it in the Preferences -&gt; Protocols -&gt; SSL -&gt; (Pre)master-Secret Log file</p><p>Even though I give key file for decrypting, I cannot get decrypted payload of SSL.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2_F0BITN4.jpg" alt="alt text" /></p><p>Is there any tips for decrypting ssl session using Lua ssl dissector?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-sub-dissector" rel="tag" title="see questions tagged &#39;sub-dissector&#39;">sub-dissector</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '16, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/417042f4a5ae00104a6b7683d86f1687?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yobob&#39;s gravatar image" /><p><span>yobob</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yobob has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Oct '16, 02:13</strong> </span></p></div></div><div id="comments-container-56115" class="comments-container"><span id="56120"></span><div id="comment-56120" class="comment"><div id="post-56120-score" class="comment-score">1</div><div class="comment-text"><p>Wow for the idea. However, I'm afraid that to get a real solution, you'll need to file a bug (category enhancement), because currently, part of ssl decryption configuration is to tell the ssl dissector what other dissector to use to handle the decrypted data, and the fields used as index to the table are IP address and tcp port.</p><p>As a temporary workaround I could imagine to use tshark to extract the payload from the URBs (<code>-T fields -e usb.addr -e usb.capdata</code>) and feed its output to a script which would provide fake TCP headers to the data - which, however, would also not be an easy task as you would have to properly imitate at least the seq and ack numbers so that the tcp dissector would be happy. The script could output a simple hexdump format which you would then feed to text2pcap or import it to Wireshark using <code>File -&gt; Import from Hex Dump</code>.</p></div><div id="comment-56120-info" class="comment-info"><span class="comment-age">(04 Oct '16, 02:26)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="56123"></span><div id="comment-56123" class="comment"><div id="post-56123-score" class="comment-score"></div><div class="comment-text"><p>An idea which didn't come to my mind instantly would be to use Lua to create these fake TCP and IP headers during dissection (you'd have to create a new tvb containing the fake headers followed by the data extracted from the URB), and you would have to save the values for the headers as each frame may be dissected multiple times - they are dissected in sequence only once during loading or capture of the file.</p></div><div id="comment-56123-info" class="comment-info"><span class="comment-age">(04 Oct '16, 03:05)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="56124"></span><div id="comment-56124" class="comment"><div id="post-56124-score" class="comment-score"></div><div class="comment-text"><p>Would it be easier to create UDP headers, and then you'd have <a href="https://en.wikipedia.org/wiki/Datagram_Transport_Layer_Security">DTLS</a>?</p></div><div id="comment-56124-info" class="comment-info"><span class="comment-age">(04 Oct '16, 03:13)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="56126"></span><div id="comment-56126" class="comment"><div id="post-56126-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure. DTLS uses its own sequence numbering to ensure that the TLS PDUs are properly ordered, plus it uses an indicator of cipher state changes, so instead of generating TCP's <code>seq</code> and <code>ack</code> values <strong>outside</strong> the original encrypted data, you'd have to take care about DTLS's <code>sequence_number</code> and <code>epoch</code> <strong>in the middle of</strong> the encrypted data.</p></div><div id="comment-56126-info" class="comment-info"><span class="comment-age">(04 Oct '16, 03:26)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="56128"></span><div id="comment-56128" class="comment not_top_scorer"><div id="post-56128-score" class="comment-score"></div><div class="comment-text"><p>Ah, I've only looked at DTLS ever so briefly and obviously didn't understand the intricacies.</p></div><div id="comment-56128-info" class="comment-info"><span class="comment-age">(04 Oct '16, 03:43)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="56174"></span><div id="comment-56174" class="comment not_top_scorer"><div id="post-56174-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your comments. I will try to replace USB header to TCP dummy header. By the way, the Lua ssl dissector is different with the default ssl dissector of wireshark?</p></div><div id="comment-56174-info" class="comment-info"><span class="comment-age">(05 Oct '16, 20:01)</span> <span class="comment-user userinfo">yobob</span></div></div><span id="56177"></span><div id="comment-56177" class="comment"><div id="post-56177-score" class="comment-score">1</div><div class="comment-text"><p>There is no such thing like "Lua SSL dissector" (unless you have written your own one but in such case the question would make no sense, right?). Lua dissectors can invoke C dissectors and vice versa.</p><p><strong>Replacing</strong> USB header with a TCP dummy header is not exactly what I had in mind. A dissector normally acts on the actual bytes of a captured frame and from its point of view, these bytes are read-only. But any dissector can create additional bytes of data and ask a higher layer dissector to handle them as if they were part of the captured frame.</p><p>So what I've recommended was to create the IP and TCP header as a byte array, concatenate to it the payload extracted from the URB, and use the <a href="https://wiki.wireshark.org/LuaAPI/ByteArray#ByteArray.tvb.28bytearray.2C_name.29">bytearray:tvb</a> function to create a new tvb from it and call the existing IP dissector, giving it your new tvb as a target.</p><p>The IP header must be there too because the SSL dissector uses both IP address and port as keys to the table choosing the right dissector for the decrypted payload, and because you have to specify even <code>data</code> (i.e. no dissection, just display of the contents in hexadecimal) explicitly.</p><p>Myself I would use IP address <code>10.0.0.1</code> to represent the USB host and <code>10.0.bus.device</code> to represent the USB endpoint, so an URB from <code>host</code> to <code>2.1.4</code> would have <code>10.0.0.1</code> as IP source and <code>10.0.2.1</code> as IP destination, and vice versa. The server side TCP port should be set to a value to which no other dissector of TCP payload is linked by default, something like <code>33333</code>, and you may link the <code>ssl</code> dissector to that TCP port already in your initialization code:</p><pre><code>DissectorTable.get(&quot;tcp.port&quot;):add(33333,Dissector.get(&quot;ssl&quot;))</code></pre><p>The client side port should be in the range from <code>40000</code> up.</p><p>As already written, the TCP header cannot be totally dummy because otherwise the TCP dissector would not invoke the higher layer dissector (in our case, the SSL one). I believe, though, that it is not necessary to simulate the SYN, SYN+ACK, ACK session establishment sequence.</p></div><div id="comment-56177-info" class="comment-info"><span class="comment-age">(05 Oct '16, 22:29)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="56213"></span><div id="comment-56213" class="comment not_top_scorer"><div id="post-56213-score" class="comment-score"></div><div class="comment-text"><p>One more point, as USB by nature uses distinct data endpoints for in and out directions even if they form up a bi-directional logical channel, the <code>ssl</code> dissector would not even know that the messages to one endpoint and the messages from the other one belong to the same conversation. To let the <code>ssl</code> dissector handle the conversation properly, the fake IP and TCP headers must use the same pair of IP:port tuples, properly oriented as source and destination depending on the URB direction. What my workaround suggestion ignores is that the USB device may theoretically use several pairs of data endpoints and that in such case, the only way to determine which IN endpoint works in tandem with which OUT endpoint would be to analyse the descriptors.</p><p>For the record, of course the clean way would be to file an enhancement "bug" asking for the <code>ssl</code> dissector to understand USB conversations directly, without the need to create fake IP and TCP headers, as stated in my first reaction. But that would require some investigation into the issue above, i.e. to verify and describe a method of determination which endpoints form up a bi-directional logical channel.</p></div><div id="comment-56213-info" class="comment-info"><span class="comment-age">(07 Oct '16, 01:08)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-56115" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-56115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56230"></span>

<div id="answer-container-56230" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56230-score" class="post-score" title="current number of votes">2</div><span id="post-56230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yobob has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For SSL/TLS decryption, a client and server side must be known identified since both sides contribute to the session secret via the nonces in their Hello messages (Client Random and Server Random). This client/server is determined automatically when using UDP/TCP, but for other protocols you (as the parent layer) must provide this information.</p><p>On the USB level, data packets go from the host to the device (for an OUT endpoint) or from the device to the host (for an IN endpoint). These endpoint numbers are not necessarily the same and in that case Wireshark sees two separate conversations:</p><pre><code>2.1.5 &lt;-&gt; host
2.1.4 &lt;-&gt; host</code></pre><p>Thus the SSL dissector is unable to understand that these two data streams are paired. According to the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Pinfo.html#lua_class_Pinfo">WSLUA</a> documentation, fields like <code>pinfo.src</code> and <code>pinfo.dst</code> are actually writable, so you could put your fake "source" and "destination" addresses inside.</p><p>Note that these properties form a "conversation" (see <code>find_or_create_conversation</code> in <code>epan/conversation.c</code>):</p><ul><li><code>pinfo.src</code> / <code>pinfo.dst</code></li><li><code>pinfo.port_type</code> (<code>PT_USB</code> (12) in the case of USB)</li><li><code>pinfo.src_port</code> / <code>pinfo.dst_port</code></li></ul><p>To ensure that the old, USB-specific conversations are not accidentally matched, chose source/destination addresses that are definitely different or pick any other port type.</p><p>The SSL dissector currently does not check the port type, so if you for example have HTTP, you could set a conversation like this (swap roles accordingly):</p><ul><li><code>pinfo.src</code>: CLIENT</li><li><code>pinfo.dst</code>: SERVER</li><li><code>pinfo.port_type</code>: <code>PT_TCP</code> (numeric value is 2, could probably pick any other value)</li><li><code>pinfo.src_port</code>: 0 (choice does not matter)</li><li><code>pinfo.dst_port</code>: 443</li></ul><p>(If you pick <code>port_type</code> 0, be sure to use Wireshark 2.2.1 which <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=aeaf42724def75fdf5d591d27c4ab6ca2f64d342">fixed</a> an issue that resulted in misdetection of the client/server side.)</p><p>If this still does not give the expected result, enable the SSL debug log. For example, if the log shows two different "ssl_session" pointer addresses, then you know that the conversation is messed up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '16, 15:57</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Oct '16, 08:21</strong> </span></p></div></div><div id="comments-container-56230" class="comments-container"><span id="56305"></span><div id="comment-56305" class="comment"><div id="post-56305-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your comment.</p><p>As you told, I should have set pinfo.src_port and pinfo.dst_port to decrypt packets. I could get decrypted packets after that.</p><p>thank you again, Lekensteyn</p></div><div id="comment-56305-info" class="comment-info"><span class="comment-age">(11 Oct '16, 21:55)</span> <span class="comment-user userinfo">yobob</span></div></div><span id="56426"></span><div id="comment-56426" class="comment"><div id="post-56426-score" class="comment-score"></div><div class="comment-text"><p><span>@yobob</span> If your question is answered, consider pressing accepting this answer by pressing the tick on the left. Thanks!</p></div><div id="comment-56426-info" class="comment-info"><span class="comment-age">(16 Oct '16, 13:33)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-56230" class="comment-tools"></div><div class="clear"></div><div id="comment-56230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

