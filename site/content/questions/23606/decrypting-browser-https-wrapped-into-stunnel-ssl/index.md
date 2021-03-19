+++
type = "question"
title = "Decrypting browser HTTPS wrapped into stunnel SSL"
description = '''I&#x27;m trying to decrypt browser&#x27;s HTTPS traffic which passes through stunnel. Essentially, I&#x27;ve got HTTPS wrapped into stunnel&#x27;s SSL. I realized that wireshark is unable to decrypt SSL within SSL. I provided wireshark with stunnel&#x27;s key as well as sslkeylogfile for HTTPS traffic. I can see that wiresh...'''
date = "2013-08-07T02:37:00Z"
lastmod = "2013-08-09T02:46:00Z"
weight = 23606
keywords = [ "stunnel" ]
aliases = [ "/questions/23606" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting browser HTTPS wrapped into stunnel SSL](/questions/23606/decrypting-browser-https-wrapped-into-stunnel-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23606-score" class="post-score" title="current number of votes">0</div><span id="post-23606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decrypt browser's HTTPS traffic which passes through stunnel. Essentially, I've got HTTPS wrapped into stunnel's SSL. I realized that wireshark is unable to decrypt SSL within SSL.</p><p>I provided wireshark with stunnel's key as well as sslkeylogfile for HTTPS traffic. I can see that wireshark successfully decrypts the outer layer - stunnel's SSL, but it fails to inspect the inner HTTPS.</p><p>I know that sslkeylogfile contains the necessary pre-master to decrypt inner HTTPS, because when I tell wireshark to listen to traffic after it passes stunnel, browser's HTTPS gets decrypted successfully.</p><p>Is there a way to tell wireshark to perform two-pass decryption? If it was possible to save the decrypted wireshark capture, I would save it after the stunnel SSL got decrypted, then I would feed it back to wireshark and it would decrypt the browser's HTTPS. Unfortunately saving the decrypted capture is not supported yet.</p><p>P.S. neither browser nor stunnel use DH-ciphers or TLS session tickets and there are no out-of-order frames.</p><p>EDIT1:<br />
here is a sample capture<br />
<a href="http://cloudshark.org/captures/67dea7c0e684">http://cloudshark.org/captures/67dea7c0e684</a><br />
stunnel key:<br />
<a href="http://pastebin.com/ivRTTNJp">http://pastebin.com/ivRTTNJp</a><br />
sslkeylogfile to decrypt HTTPS:<br />
<a href="http://pastebin.com/fah4Zebx">http://pastebin.com/fah4Zebx</a><br />
</p><p>Note: I use "Decode as SSL" for source and destination port 33310<br />
Sometimes when both "RSA key list" and "Master Secret log filename" given, wireshark fails to decrypt stunnel SSL. So I removed MS log filename and decryption worked.<br />
I successfully Exported PDUs with this capture and opened it in a new wireshark instance but was confronted with a failure in decrypting the HTTPS.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-stunnel" rel="tag" title="see questions tagged &#39;stunnel&#39;">stunnel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '13, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/5539b49a6661453d168b03c047917c5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dansmith&#39;s gravatar image" /><p><span>dansmith</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dansmith has one accepted answer">50%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Aug '13, 10:15</strong> </span></p></div></div><div id="comments-container-23606" class="comments-container"></div><div id="comment-tools-23606" class="comment-tools"></div><div class="clear"></div><div id="comment-23606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23632"></span>

<div id="answer-container-23632" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23632-score" class="post-score" title="current number of votes">1</div><span id="post-23632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please see the answer of <span>@JeffMorriss</span>.</p><p>to the following question.</p><blockquote><p><a href="http://ask.wireshark.org/questions/23614/save-a-capture-after-decryption">http://ask.wireshark.org/questions/23614/save-a-capture-after-decryption</a></p></blockquote><p>With the "export PDUs" function, you should be able to save the decrypted stunnel packets and then load that file into Wireshark again, to decrypt the HTTPS packets.</p><p>Link to current development releases</p><blockquote><p><a href="http://www.wireshark.org/download/automated/">http://www.wireshark.org/download/automated/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Aug '13, 08:14</strong> </span></p></div></div><div id="comments-container-23632" class="comments-container"><span id="23653"></span><div id="comment-23653" class="comment"><div id="post-23653-score" class="comment-score"></div><div class="comment-text"><p>I compiled the latest built. I open my pcap, select File-&gt;Export PDUs to File Filter: ip &amp; OSI Layer 7 followed by OK Then it opens a new wireshark window called *(Untitled) not showing a single packet. Have you been successful in using the Export PDUs feature?</p></div><div id="comment-23653-info" class="comment-info"><span class="comment-age">(08 Aug '13, 08:12)</span> <span class="comment-user userinfo">dansmith</span></div></div><span id="23654"></span><div id="comment-23654" class="comment"><div id="post-23654-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Have you been successful in using the Export PDUs feature?</p></blockquote><p>I did not try yet. I just wanted to give you a hint about a possible solution. I will try it myself now ;-)</p><p>Is it possible for you to post the capture files and the keys (only for a test environment)?</p></div><div id="comment-23654-info" class="comment-info"><span class="comment-age">(08 Aug '13, 08:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="23658"></span><div id="comment-23658" class="comment"><div id="post-23658-score" class="comment-score"></div><div class="comment-text"><p>I provided the sample capture in my OP</p></div><div id="comment-23658-info" class="comment-info"><span class="comment-age">(08 Aug '13, 10:16)</span> <span class="comment-user userinfo">dansmith</span></div></div><span id="23661"></span><div id="comment-23661" class="comment"><div id="post-23661-score" class="comment-score"></div><div class="comment-text"><p>O.K. the "export PDU" feature finally does something, although I'm not quite sure what to do with the exported data in your case.</p><p>Exported PDU file: <a href="https://www.cloudshark.org/captures/4342db79406c">https://www.cloudshark.org/captures/4342db79406c</a></p><p>After decryption of the stunnel connection (choose 'data' as Protocol in the RSA Key list), I was able to export the PDUs with this filter during export: 'tcp.stream eq 0' and 'OSI Layer 7'.</p><p>However the exported PDUs are in a very special form and Wireshark does not detect the decrypted data (exported PDUs) as HTTP, although you can see the CONNECT command in the packet bytes (see frame #1 in the file above).</p><p>So, currently I don't see a way to decrypt the SSL/TLS connection within that exported PDU capture file, until Wireshark dissects that as HTTP.</p><p>But hey, this feature is still under development, so maybe it will work in a later snapshot ;-)</p><p>Regards<br />
Kurt</p></div><div id="comment-23661-info" class="comment-info"><span class="comment-age">(08 Aug '13, 15:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="23663"></span><div id="comment-23663" class="comment"><div id="post-23663-score" class="comment-score"></div><div class="comment-text"><p>O.K. you <strong>could</strong> do this.</p><ul><li>remove the first 60 bytes of every frame with editcap. This will leave only the HTTP protocol in the new capture file.</li></ul><blockquote><p>editcap -C 60 exported_pdu.pcapng exported_pdu_trunc.pcap</p></blockquote><ul><li>Then use tshark to print the payload bytes in HEX</li></ul><blockquote><p>tshark -nr exported_pdu_trunc.pcap -T fields -e data</p></blockquote><p>Format that output into something that text2pcap understands and add a new IP/TCP header via text2pcap (-T). Then open the newly created capture file and try to decrypt the data.</p><p>Just an idea .... ;-)</p></div><div id="comment-23663-info" class="comment-info"><span class="comment-age">(08 Aug '13, 15:28)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="23671"></span><div id="comment-23671" class="comment not_top_scorer"><div id="post-23671-score" class="comment-score"></div><div class="comment-text"><p>The payload can be exported as HTTP (see <a href="http://cloudshark.org/captures/ed9681934778">http://cloudshark.org/captures/ed9681934778</a> ). You just need to choose 'http' instead of 'data' in the RSA keylist dialog box.</p></div><div id="comment-23671-info" class="comment-info"><span class="comment-age">(09 Aug '13, 02:46)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-23632" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-23632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

