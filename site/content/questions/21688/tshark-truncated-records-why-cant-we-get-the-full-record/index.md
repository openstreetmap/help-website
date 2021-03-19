+++
type = "question"
title = "tshark truncated records - why can&#x27;t we get the full record?"
description = '''I understand how to see the full non-truncated record (in my case it&#x27;s the actual HTML page that I&#x27;m trying to read, and it contains long lines) in Wireshark - it&#x27;s a clicking operation to copy into the buffer. But I want to do the same in tshark, so as to automate it. So far from Google I&#x27;ve found ...'''
date = "2013-06-02T00:46:00Z"
lastmod = "2017-06-06T21:32:00Z"
weight = 21688
keywords = [ "tshark", "truncated" ]
aliases = [ "/questions/21688" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tshark truncated records - why can't we get the full record?](/questions/21688/tshark-truncated-records-why-cant-we-get-the-full-record)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21688-score" class="post-score" title="current number of votes">0</div><span id="post-21688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I understand how to see the full non-truncated record (in my case it's the actual HTML page that I'm trying to read, and it contains long lines) in Wireshark - it's a clicking operation to copy into the buffer. But I want to do the same in tshark, so as to automate it. So far from Google I've found at least one person asking this, and the response was that the 240 char limit is hardcoded and would not be feasible to make dynamic, therefore you would have to make your own build of Wireshark.</p><p>On the other hand, it's clear that the pcap files are storing the full records, and indeed just getting tshark to mindlessly read from one pcap file and output to another one and then putting that into wireshark confirms that all the data is still there.</p><p>I just can't understand why this is not a huge problem for people - surely if you want to analyze traffic you sometimes (often) have to see the actual data being sent, and often it's in lines/records that are longer than 240 bytes. Can this not be fixed, or is there some workaround aside from the enormous task of rebuilding Wireshark itself?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-truncated" rel="tag" title="see questions tagged &#39;truncated&#39;">truncated</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '13, 00:46</strong></p><img src="https://secure.gravatar.com/avatar/40920813c79c306646f94e993af244da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AdamZSI&#39;s gravatar image" /><p><span>AdamZSI</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AdamZSI has no accepted answers">0%</span></p></div></div><div id="comments-container-21688" class="comments-container"><span id="21689"></span><div id="comment-21689" class="comment"><div id="post-21689-score" class="comment-score"></div><div class="comment-text"><p>In partial answer of my own question, the flag -x seems to dump the packet in hex/ascii. It's not a pretty solution, though, because what I am ultimately aiming to do is to recreate the html pages served. So if that's the only way to do it it's going to get a bit hack-y. Any other ideas offered appreciated; I'm still confused why this wouldn't be enabled in tshark if it is in wireshark. Thanks.</p></div><div id="comment-21689-info" class="comment-info"><span class="comment-age">(02 Jun '13, 02:51)</span> <span class="comment-user userinfo">AdamZSI</span></div></div></div><div id="comment-tools-21688" class="comment-tools"></div><div class="clear"></div><div id="comment-21688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21691"></span>

<div id="answer-container-21691" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21691-score" class="post-score" title="current number of votes">2</div><span id="post-21691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I just took a quick peek at the code and indeed it is not easy to change the truncation of displayed fields. If you want to reconstruct data sent over TCP sessions (and http in particular in your case) you can better use the follow stream options of tshark.</p><p>From the manpage:</p><pre><code>-z follow,prot,mode,filter[,range]

    Displays the contents of a TCP or UDP stream between two nodes. The data sent by the second node is prefixed with a tab to differentiate it from the data sent by the first node.

    prot specifies the transport protocol. It can be one of: tcp TCP udp UDP ssl SSL

    mode specifies the output mode. It can be one of: ascii ASCII output with dots for non-printable characters hex Hexadecimal and ASCII data with offsets raw Hexadecimal data

    Since the output in ascii mode may contain newlines, the length of each section of output plus a newline precedes each section of output.

    filter specifies the stream to be displayed. UDP streams are selected with IP address plus port pairs. TCP streams are selected with either the stream index or IP address plus port pairs. For example: ip-addr0:port0,ip-addr1:port1 tcp-stream-index

    range optionally specifies which &quot;chunks&quot; of the stream should be displayed.</code></pre><p>An example:</p><pre><code>for stream in $(tshark -r http.cap -R http.request -T fields -e tcp.stream | sort -n | uniq)
do
  echo &quot;Processing stream $stream&quot;
  tshark -r http.cap -q -z follow,tcp,raw,$stream &gt; /tmp/stream-$stream
done</code></pre><p>Which will result in:</p><pre><code>===================================================================
Follow: tcp,raw
Filter: tcp.stream eq 0
Node 0: 192.168.1.43:50166
Node 1: 66.102.13.103:80
474554202f20485454502f312e310d0a486f73743a207777772e676f6f676c652e6e6c0d0a557365722d4167656e743a204d6f7a696c6c612f352e3020284d6163696e746f73683b20553b20496e74656c204d6163204f5320582031302e363b20656e2d55533b2072763a312e392e3229204765636b6f2f32303130303131352046697265666f782f332e360d0a4163636570743a20746578742f68746d6c2c6170706c69636174696f6e2f7868746d6c2b786d6c2c6170706c69636174696f6e2f786d6c3b713d302e392c2a2f2a3b713d302e380d0a4163636570742d4c616e67756167653a20656e2d75732c656e3b713d302e350d0a4163636570742d456e636f64696e673a20677a69702c6465666c6174650d0a4163636570742d436861727365743a2049534f2d383835392d312c7574662d383b713d302e372c2a3b713d302e370d0a4b6565702d416c6976653a203131350d0a436f6e6e656374696f6e3a206b6565702d616c6976650d0a436f6f6b69653a20505245463d49443d333634376265366563336465356231393a553d623732313065313434336139316337313a544d3d313236333539353637363a4c4d3d313236383832373637343a4c3d304a703665444c6c5a37654e465775473730456d72364138784f67413a533d77304631706163334a4753736b6c396a3b204e49443d33373d5a455f7979716654635957445a576847616463774b5438312d714a32447243436c336374672d614e4e477076484d435249415a493075483541546c52585473724a626e43306562634b5441495342326a335931774d48536e723847444468494f706852756e706a35786c4d2d69547265386469674846713771314535755a424b3b204b42443d306e6c2d330d0a0d0a
    485454502f312e3120323030204f4b0d0a446174653a205468752c2031322041756720323031302030383a33343a353620474d540d0a457870697265733a202d310d0a43616368652d436f6e74726f6c3a20707269766174652c206d61782d6167653d300d0a436f6e74656e742d547970653a20746578742f68746d6c3b20636861727365743d5554462d380d0a436f6e74656e742d456e636f64696e673a20677a69700d0a5365727665723a206777730d0a436f6e74656e742d4c656e6774683a20353532340d0a582d5853532d50726f74656374696f6e3a20313b206d6f64653d626c6f636b0d0a0d0a1f8b08000000000002ffa53b695bdc38d2dff32b8cb369ecc5b80f20401b93071292c96c663207333bb30c9347b6655bb47c60bbb99afeef6f9564b9edee2664f70dc1b6ae52a96e95c4d14690f9d57d4eb5b84af8f1113eb52c4db2694993ec86ba7a946511a7bd9e7cdb2109ba0583ded0b43275184b49707c94d08a00b02adfa6d75376e3ea7e9656d0631b67d1b5bae4ea15bdabfa389da3f931294a5ab9bf9dbfdf3e0040
[...]</code></pre><p>Which can be parsed by a script quite easily.</p><p>Or use ascii, but then you end up with a lot of dots for the non-ascii-characters:</p><pre><code>===================================================================
Follow: tcp,ascii
Filter: tcp.stream eq 0
Node 0: 192.168.1.43:50166
Node 1: 66.102.13.103:80
649
GET / HTTP/1.1^M
Host: www.google.nl^M
User-Agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6^M
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8^M
Accept-Language: en-us,en;q=0.5^M
Accept-Encoding: gzip,deflate^M
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7^M
Keep-Alive: 115^M
Connection: keep-alive^M
Cookie: PREF=ID=3647be6ec3de5b19:U=b7210e1443a91c71:TM=1263595676:LM=1268827674:L=0Jp6eDLlZ7eNFWuG70Emr6A8xOgA:S=w0F1pac3JGSskl9j; NID=37=ZE_yyqfTcYWDZWhGadcwKT81-qJ2DrCCl3ctg-aNNGpvHMCRIAZI0uH5ATlRXTsrJbnC0ebcKTAISB2j3Y1wMHSnr8GDDhIOphRunpj5xlM-iTre8digHFq7q1E5uZBK; KBD=0nl-3^M
^M

    1212
HTTP/1.1 200 OK^M
Date: Thu, 12 Aug 2010 08:34:56 GMT^M
Expires: -1^M
Cache-Control: private, max-age=0^M
Content-Type: text/html; charset=UTF-8^M
Content-Encoding: gzip^M
Server: gws^M
Content-Length: 5524^M
X-XSS-Protection: 1; mode=block^M
^M
.........ÿ¥;i[Ü8Òßó+.³iìÅ¸. @.....Élf2.3;³..G¶e[´|`»¹.þïo.d¹íî&amp;d÷^MÁ¶®R©n.ÄÑF.ùÕ}Nµ¸Jøñ.&gt;µ,M²iI.ì.ºz.e.§½.|Û!.º..ÞÐ´2u.KIp|.Ð..°*ß¦×Svãê~.VÐc.gÑµºäê.½«ú8.£ù1)JZ¹¿.¿ß&gt;[email protected]«8=þ æ8êËÒQé.,¯.oY.d·¶DÀ.MÎ&gt;.õ.&gt;}.uþÓtç$ûn´}âÅ£ÿìÜ¼ûY·&amp;g.ü.ÍÃýÑÞ¡5Ú.íãsÿà.ZÞþúq&lt;£kÛ({.&quot;½ËÙºAs+áãp.ú.Ë
[...]</code></pre><p>All-in-all, if reconstructing html-pages is what you're after, I think there will be better tools available when you google for it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '13, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21691" class="comments-container"><span id="21700"></span><div id="comment-21700" class="comment"><div id="post-21700-score" class="comment-score"></div><div class="comment-text"><p>To SYN-bit, I really appreciate the in depth answer and suggestions, it will almost certainly be helpful in some cases, but as it happens (and I should have mentioned this), this is data passing over SSL. The decryption is working well with the SSLKEYLOGFILE set in the env, but I don't know if that will be a problem if I try to isolate streams and dump them out raw like this? You say it will be easy to convert the hex with a script, but could you give me some pointers as to what kind of script that would be? By the way the -x flag does really seem to give me what I want, with the tiny detail that the output format is 2 column hex/ascii. Looking for a tool now to just extract the ascii out of that directly.</p></div><div id="comment-21700-info" class="comment-info"><span class="comment-age">(02 Jun '13, 23:09)</span> <span class="comment-user userinfo">AdamZSI</span></div></div></div><div id="comment-tools-21691" class="comment-tools"></div><div class="clear"></div><div id="comment-21691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61817"></span>

<div id="answer-container-61817" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61817-score" class="post-score" title="current number of votes">0</div><span id="post-61817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I ran into this problem and I had trouble understanding the method used to access the un-truncated data in Wireshark (not tshark, I don't use that). Here is what I discovered. If you double-click a packet to open a detail view, and highlight the truncated field, then right-click, you don't get a context menu. I found it was necessary to highlight the truncated field in the 3-pane view, and then right-click, and select Copy &gt; Value (or use the shortcut &lt;ctr&gt; &lt;shift&gt; V) which copies the entire un-truncated field onto clipboard.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '17, 21:32</strong></p><img src="https://secure.gravatar.com/avatar/989f1d591d40a3a4f4ce713c8c87c8da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gaborkiss&#39;s gravatar image" /><p><span>gaborkiss</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gaborkiss has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jun '17, 21:33</strong> </span></p></div></div><div id="comments-container-61817" class="comments-container"></div><div id="comment-tools-61817" class="comment-tools"></div><div class="clear"></div><div id="comment-61817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

