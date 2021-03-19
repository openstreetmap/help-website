+++
type = "question"
title = "tshark output data in not completly correct"
description = '''Hello, I am using tshark to retreive a lot of data from a captured file. I am using the command: tshark.exe -r C:&#92;Temp&#92;input.pcap -z &quot;follow,tcp,hex,0&quot; -w C:&#92;Temp&#92;output.ps -Y &quot;tcp.stream eq 0&quot; The output contains extra header and trailer (unwanted) data in front of the requested data  I expect that...'''
date = "2015-10-22T07:27:00Z"
lastmod = "2015-10-22T08:53:00Z"
weight = 46833
keywords = [ "output", "tshark" ]
aliases = [ "/questions/46833" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark output data in not completly correct](/questions/46833/tshark-output-data-in-not-completly-correct)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46833-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am using tshark to retreive a lot of data from a captured file.</p><p>I am using the command:</p><p>tshark.exe -r C:\Temp\input.pcap -z "follow,tcp,hex,0" -w C:\Temp\output.ps -Y "tcp.stream eq 0"</p><p>The output contains extra header and trailer (unwanted) data in front of the requested data</p><p>I expect that the comandline is not correct, but I am unable to find the problem</p><p>Header data</p><p>X M&lt;+ ÿÿÿÿÿÿÿÿ 3 TShark 1.12.8 (v1.12.8-0-g5b6e543 from master-1.12) X       l 2 |Y€J J ÝåjÄ„&lt;Š°+ä E &lt;Õ[email protected] 9vN°daÀ¨ ò¾f#Œj’;A 9¥± ¬ ýXî  l  <code>2 I[€&gt;   &gt;   &lt;Š°+ä ÝåjÄ„ E  0M  ÿ¬_À¨ ò°da#Œ¾f mýbj’;Bp û\  ´</code>  \ 2 E”€&lt; &lt; ÝåjÄ„&lt;Š°+ä E (Õ[email protected] 9va°daÀ¨ ò¾f#Œj’;B mýcP9û \  \ 2 B˜€&lt; &lt; &lt;Š°+ä ÝåjÄ„ E (N ÿ¬fÀ¨ ò°da#Œ¾f mýcj’;BP` Ô ´\   2 ±Ç½â â ÝåjÄ„&lt;Š°+ä E ÔÕ[email protected] 9p´°daÀ¨ ò¾f#Œj’;B mýcP9þ<br />
</p><p>Trailer data</p><pre><code>     \       2 \RÁ&lt;   &lt;   &lt;Š°+ä ÝåjÄ„ E  (a  ÿ¬SÀ¨ ò°da#Œ¾f mýcj“œ²P&gt;ý“²  ´\      \       2 YSÁ&lt;   &lt;   &lt;Š°+ä ÝåjÄ„ E  (b  ÿ¬RÀ¨ ò°da#Œ¾f mýcj“œ²P&gt;ý“±  ´\      \       2 FˆÁ&lt;   &lt;    ÝåjÄ„&lt;Š°+ä E  (Õ”@ 9v °daÀ¨ ò¾f#Œj“œ² mýdP9™¦        \</code></pre><p>X M&lt;+ ÿÿÿÿÿÿÿÿ 3 TShark 1.12.8 (v1.12.8-0-g5b6e543 from master-1.12) X       l 2 |Y€J J ÝåjÄ„&lt;Š°+ä E &lt;Õ[email protected] 9vN°daÀ¨ ò¾f#Œj’;A 9¥± ¬ ýXî  l  <code>2 I[€&gt;   &gt;   &lt;Š°+ä ÝåjÄ„ E  0M  ÿ¬_À¨ ò°da#Œ¾f mýbj’;Bp û\  ´</code>  \ 2 E”€&lt; &lt; ÝåjÄ„&lt;Š°+ä E (Õ[email protected] 9va°daÀ¨ ò¾f#Œj’;B mýcP9û \  \ 2 B˜€&lt; &lt; &lt;Š°+ä ÝåjÄ„ E (N ÿ¬fÀ¨ ò°da#Œ¾f mýcj’;BP` Ô ´\   2 ±Ç½â â ÝåjÄ„&lt;Š°+ä E ÔÕ[email protected] 9p´°daÀ¨ ò¾f#Œj’;B mýcP9þ<br />
</p></div><div id="question-tags" class="tags-container tags">output tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '15, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/c72b4cb1a266757ec318febb2cc62d1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ton%20Helmerhorst&#39;s gravatar image" /><p>Ton Helmerhorst<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ton Helmerhorst has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-46833" class="comments-container"></div><div id="comment-tools-46833" class="comment-tools"></div><div class="clear"></div><div id="comment-46833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46839"></span>

<div id="answer-container-46839" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46839-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are <strong>writing a pcap file</strong> with the option <strong>-w ....</strong>. That's certainly not what you want if you are using <strong>-z follow</strong>.</p><p>Please try this, to direct the output of tshark into a file.</p><blockquote><p>tshark.exe -r C:\Temp\input.pcap -z "follow,tcp,hex,0" -q &gt; C:\Temp\output.txt</p></blockquote><p>BTW: You don't need the option "-Y ...." as you specified the TCP Stream already in the follow option.</p><p>The output would be hex data and you need to parse that with a script to get the payload.</p><pre><code>===================================================================
Follow: tcp,hex
Filter: tcp.stream eq 2
Node 0: 192.168.90.57:41170
Node 1: 104.25.10.6:443
00000000  17 03 03 03 52 00 00 00  00 00 00 00 4e f1 aa 31  ....R... ....N..1
00000010  43 37 e6 74 ed cc cf fa  ec fb 18 0f 72 65 9d 57  C7.t.... ....re.W
00000020  df f9 d9 0c 9f 17 3a 3c  3a 42 11 92 11 4a 87 76  ......:&lt; :B...J.v
00000030  30 9c e0 68 e0 e4 d1 8f  ce af 7a a5 bf 24 cd 06  0..h.... ..z..$..
00000040  30 47 cd 60 00 85 44 f8  00 3f 12 c1 5a 1b 16 cd  0G.`..D. .?..Z...
00000050  64 5f a7 df d5 75 1f b1  fe b7 5d b6 4a cf 76 71  d_...u.. ..].J.vq
00000060  dd 60 50 d1 30 4a e6 a1  4d 4f 3c 2e b4 3b bf 55  .`P.0J.. MO&lt;..;.U
00000070  1b 37 d1 c1 2e 88 9b a3  04 9a ce 6e 8b 5b 1e 86  .7...... ...n.[..
00000080  f2 47 ad fe 45 25 e3 7f  03 e1 71 af 38 c2 c4 e3  .G..E%.. ..q.8...
00000090  5e bb 0b 0e 99 d5 7a c9  01 f1 d5 9d 49 51 5c 21  ^.....z. ....IQ\!
000000A0  0b 1e dd 57 fc 71 2d b2  53 01 78 bb 01 75 13 66  ...W.q-. S.x..u.f
000000B0  20 3e 94 04 6c 19 f8 b4  e9 92 45 0d 59 a5 e6 14   &gt;..l... ..E.Y...</code></pre><p>If you need <strong>raw data</strong>, please run this:</p><blockquote><p>tshark.exe -r C:\Temp\input.pcap -z "follow,tcp,raw,0" -q &gt; C:\Temp\output.raw</p></blockquote><p>This will give slightly different output.</p><pre><code>===================================================================
Follow: tcp,raw
Filter: tcp.stream eq 2
Node 0: 192.168.90.57:41170
Node 1: 104.25.10.6:443
1703030352000000000000004ef1aa314337e674edcccffaecfb180f72659d57dff9
bf24cd063047cd60008544f8003f12c15a1b16cd645fa7dfd5751fb1feb75db64acf
049ace6e8b5b1e86f247adfe4525e37f03e171af38c2c4e35ebb0b0e99d57ac901f1
6c19f8b4e992450d59a5e614b3b4bddff9f70cd6e485d6744d4157a7df44edad3cd7
5b651c7bae4ede2cc5fe85fbf626eb6ed75492256ffd7573bd4a779fe03705f84b32</code></pre><p>If you need <strong>'text' data</strong>, please run this:</p><blockquote><p>tshark.exe -r C:\Temp\input.pcap -z "follow,tcp,ascii,0" -q &gt; C:\Temp\output.text</p></blockquote><p><strong>++UPDATE++</strong></p><p>based on your comment, I'd like to add this:</p><p>Now I understand what you want. It's the <strong>binary</strong> data, as saved in the of <strong>TCP Follow Stream</strong> pop-up in Wireshark.</p><p><strong>Unfortunately</strong>, there is no such functionality in tshark. So, what you can do is this:</p><ul><li>let tshark output hex data (-z follow,tcp,hex,0)</li><li>use a script (perl, python, whatever) or an editor (notepad++) to convert the output to something that xxd (included in gvim), understands (see below)</li><li>run xxd to convert the <strong>hex</strong> data to <strong>binary</strong> data</li></ul><p>This is what tshark generates:</p><pre><code>===================================================================
Follow: tcp,hex
Filter: tcp.stream eq 36
Node 0: 176.31.100.97:56001
Node 1: 192.168.32.242:9100
00000000  1b 25 2d 31 32 33 34 35  58 40 50 4a 4c 0a 40 50  .%-12345 X@PJL.@P
00000010  4a 4c 20 4a 4f 42 20 4e  41 4d 45 20 3d 20 22 36  JL JOB N AME = &quot;6
00000020  31 39 30 38 33 2d 35 35  64 64 64 63 30 37 34 64  19083-55 dddc074d
00000030  65 38 36 2e 70 64 66 22  20 44 49 53 50 4c 41 59  e86.pdf&quot;  DISPLAY
00000040  20 3d 20 22 33 30 37 35  33 37 20 61 70 61 63 68   = &quot;3075 37 apach
</code></pre><p>this is what <strong>xxd</strong> needs to be able to convert it to binary</p><pre><code>00000000  1b 25 2d 31 32 33 34 35 58 40 50 4a 4c 0a 40 50  .%-12345 X@PJL.@P
00000010  4a 4c 20 4a 4f 42 20 4e 41 4d 45 20 3d 20 22 36  JL JOB N AME = &quot;6
00000020  31 39 30 38 33 2d 35 35 64 64 64 63 30 37 34 64  19083-55 dddc074d
00000030  65 38 36 2e 70 64 66 22 20 44 49 53 50 4c 41 59  e86.pdf&quot;  DISPLAY
00000040  20 3d 20 22 33 30 37 35 33 37 20 61 70 61 63 68   = &quot;3075 37 apach
00000050  65 20 36 31 39 30 38 33 2d 35 35 64 64 64 63 30  e 619083 -55dddc0
00000060  37 34 64 65 22 0a 40 50 4a 4c 20 45 4e 54 45 52  74de&quot;.@P JL ENTER
00000070  20 4c 41 4e 47 55 41 47 45 20 3d 20 50 4f 53 54   LANGUAG E = POST</code></pre><p>So, basically, the process is:</p><ul><li>run tshark: <strong>tshark -nr input.pcap -q -z follow,tcp,hex,0 &gt; tshark.out.hex</strong></li><li>open <strong>tshark.out.hex</strong> with an editor or use a script to do the following:</li><li>remove the 'comment' lines at the beginning</li><li>remove the double space in the middle of the output, so '35__58' becomes '35_58', etc.</li><li>save <strong>tshark.out.hex</strong></li><li>run xxd: <strong>xxd.exe -r -g 1 tshark.out.hex tshark.out.bin</strong></li></ul><p><strong>Result:</strong> tshark.out.bin is identical to your file 'correct_data.raw' in the ZIP file.</p><p>You will find <strong>xxd.exe</strong> in the installation directory of <a href="http://www.vim.org/">vim</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '15, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Oct '15, 15:23</p></div></div><div id="comments-container-46839" class="comments-container"><span id="46854"></span><div id="comment-46854" class="comment"><div id="post-46854-score" class="comment-score"></div><div class="comment-text"><p>Dear all,</p><p>Many thanks for your kind response. I tried all the options you mentioned, but unfortunatly without success. I still observe unwanted data in the header and trailer of the datastream.</p><p>I published the related files on the following URL:</p><p><a href="https://www.hidrive.strato.com/lnk/hQzNGqJd">https://www.hidrive.strato.com/lnk/hQzNGqJd</a></p><p>Password: [email protected]</p><p>In this zip file you will find the procedure (avi file) to retrieve the correct data from wireshark. Also a batch file with all the used (tried) commands and the output of the related commands. In the file correct_data.raw you can observe the expected data without the unwanted data in the header and trailer.</p><p>I appriciate your help very much !!!</p><p>Ton</p></div><div id="comment-46854-info" class="comment-info"><span class="comment-age">(22 Oct '15, 13:28)</span> Ton Helmerhorst</div></div><span id="46862"></span><div id="comment-46862" class="comment"><div id="post-46862-score" class="comment-score"></div><div class="comment-text"><p>Please see the <strong>++UPDATE++</strong> in my answer!</p></div><div id="comment-46862-info" class="comment-info"><span class="comment-age">(22 Oct '15, 15:23)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-46839" class="comment-tools"></div><div class="clear"></div><div id="comment-46839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

